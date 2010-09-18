require "./lib/_battle.cgi";
$is_npc_action = 0;
#=================================================
# ギルド戦 Created by Merino
#=================================================
# グレードアップに必要な枚数
my $need_medal = 5;

# 勝利メダル
my @win_medals = (
	# 名前		./icon/からの画像へのパス
	['銅メダル',	'etc/win_medal1.gif'], # 0
	['銀メダル',	'etc/win_medal2.gif'], # 5
	['金メダル',	'etc/win_medal3.gif'], # 25
	['勲章',	'etc/win_medal4.gif'], # 125
	['トロフィー',	'etc/win_medal5.gif'], # 625
	['優勝杯',	'etc/win_medal6.gif'], # 3125
	['王者杯',	'etc/win_medal7.gif'], # 15625
);

#=================================================
# タイトル、背景画像
#=================================================
sub get_header_data {
	$bgimg = "$bgimgdir/stage$stage.gif";
	$this_title = "$p_name(<b>$win</b>先勝) <b>$round</b>回戦目";
}
#=================================================
# 追加アクション
#=================================================
sub add_battle_action {
	if ($round <= 0) {
		push @actions, 'しらべる';
		$actions{'しらべる'}   = [0,	sub{ &shiraberu }];
	}

	push @actions, 'かいし';
	$actions{'かいし'}     = [0,	sub{ &kaishi }];
}

#=================================================
# ＠かいし
#=================================================
sub kaishi {
	# 戦闘開始前
	if ($round < 1) {
		my %teams = ();
		for my $name (@members) {
			++$teams{ $ms{$name}{color} } unless $teams{ $ms{$name}{color} };
		}
		if (keys %teams <= 1) {
			$mes = "対戦するギルドがいません";
			return;
		}
		elsif ($leader ne $m) {
			$mes = "一番始めの ＠かいし をすることができるのはリーダーのみです";
			return;
		}
	}
	else {
		# ＧＰ加算後
		unless (-s "$questdir/$m{quest}/bet.cgi") {
			$mes .= "※クエストは終了しました。＠にげるで解散してください";
			return;
		}
		# なかなか決着がつかない場合。強制終了
		if ($round > 10) {
			$mes = "$round ラウンドまで決着がつきませんでした。＠にげるで解散してください";
			return;
		}

		my $win_color    = '';
		my $alive_team_c = 0;
		
		for my $name (@members) {
			next if $ms{$name}{hp} < 1;
			unless ($win_color eq $ms{$name}{color}) {
				$win_color = $ms{$name}{color};
				++$alive_team_c;
			}
		}
		
		# 引分け
		if ($alive_team_c eq '0') {
			$npc_com = "第 $round ラウンドの勝負の結果は 「引き分け！」<br />";
		}
		# １パーティーのみ残っている状態
		elsif ($alive_team_c eq '1') {
			my $winner = '';
			my %win_c = ();

			open my $fh, "+< $questdir/$m{quest}/win.cgi" or &error("$questdir/$m{quest}/win.cgiファイルが開けません");
			eval { flock $fh, 2; };
			my $line = <$fh>;
			$line =~ tr/\x0D\x0A//d;
			$line .= "$win_color,";
			for my $c (split /,/, $line) {
				if (++$win_c{$c} >= $win) {
					$winner = $c;
					last;
				}
			}
			seek  $fh, 0, 0;
			truncate $fh, 0;
			print $fh $line;
			close $fh;
			
			# 優勝パーティー決定
			if ($winner) {
				&give_bet($winner);
				return;
			}
			# なかなか決着がつかない場合。強制終了
			elsif ($round > 10) {
				$mes = "$round ラウンドまで決着がつきませんでした。＠にげるで解散してください";
				return;
			}
			
			my %guilds = &get_guilds;
			
			&regist_guild_data('point', 3, $guilds{$win_color});
			
			# 現在の途中経過
			for my $c (sort { $b <=> $a } keys %win_c) {
				$npc_com .= qq|<font color="$c">$guilds{$c} $win_c{$c}勝</font> / |;
			}
		}
		# 残り１パーティーになるまで
		else {
			$mes .= "決着がついていません";
			return;
		}
	}
	
	&reset_status_all;

	# 並びを色ごとにシャッフル
	&shuffle;

	for my $name (@members) {
		# ラウンド毎に全プレイヤーのHP回復
		$ms{$name}{hp} = $ms{$name}{mhp};
		
		# 開始前の待機時間をそれぞれ与える
		next if $m eq $name;
		&regist_you_data($name, 'wt', int($time + $speed * 2 + rand(4)) );
	}
	$act_time = $speed * 2; # ＠開始した人用

	++$round;
	$npc_com .= "第 $round ラウンド試合開始！";
	&auto_reload;
}

# ギルド名とギルド色をハッシュにセット
sub get_guilds {
	my %guilds = ();
	open my $fh, "< $questdir/$m{quest}/guild.cgi" or &error("$questdir/$m{quest}/guild.cgiファイルが読み込めません");
	while (my $line = <$fh>) {
		my($gcolor, $gname) = split /<>/, $line;
		$guilds{$gcolor} = $gname;
	}
	close $fh;

	return %guilds;
}

# 優勝ギルドにギルドポイントをあたえる
sub give_bet {
	my $winner = shift;
	
	my %guilds = &get_guilds;

	open my $fh, "+< $questdir/$m{quest}/bet.cgi" or &error("$questdir/$m{quest}/bet.cgiファイルが開けません");
	eval { flock $fh, 2; };
	my $prize_money = <$fh>;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	close $fh;
	$prize_money =~ tr/\x0D\x0A//d;

	&regist_guild_data('point', $prize_money, $guilds{$winner});

	my $names = '';
	for my $name (@members) {
		&regist_guild_data('point', 4, $guilds{ $ms{$name}{color} });
		$names .= "$name," if $ms{$name}{color} eq $winner;
	}
	chop $names;
	$npc_com .= qq|優勝は$namesが所属する <b style="color: $winner;">*+.$guilds{$winner}ギルド.+*</b> です！|;

	&give_medal($guilds{$winner});
}

# 勝利ギルドに勝利メダルをあたえる
sub give_medal {
	my $gname = shift;
	
	my $gid = unpack 'H*', $gname;
	return unless -f "$guilddir/$gid/log_member.cgi"; # ギルド解散していた場合

	my %counts = ();
	my @lines = ();
	open my $fh, "+< $guilddir/$gid/log_member.cgi" or &error("$guilddir/$gid/log_member.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($ltime, $is_npc, $name, $laddr, $icon, $color) = split /<>/, $line;
		$counts{$icon}++ if $is_npc;
		push @lines, $line;
	}
	$counts{$win_medals[0][1]}++;
	push @lines, "$time<>1<>$win_medals[0][0]$counts{$win_medals[0][1]}<>0<>$win_medals[0][1]<>$npc_color<>\n";
	
	# 勝ちメダルのグレードアップ処理
	for my $i (0 .. $#win_medals-1) {
		next unless defined($counts{$win_medals[$i][1]});  # %win_medalsにないもの
		last if $counts{$win_medals[$i][1]} < $need_medal; # 必要枚数に到達していない

		# 必要メダル数になったものを除いてグレードアップさせる
		my @new_lines = ();
		for my $line (@lines) {
			my($ltime, $is_npc, $name, $laddr, $icon, $color) = split /<>/, $line;
			next if $icon eq $win_medals[$i][1];
			push @new_lines, $line;
		}
		$counts{$win_medals[$i+1][1]}++;
		push @new_lines, "$time<>1<>$win_medals[$i+1][0]$counts{$win_medals[$i+1][1]}<>0<>$win_medals[$i+1][1]<>$npc_color<>\n";
		@lines = @new_lines;
	}
	
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}

sub npc_turn { return } # 念のためハマリ防止

1; # 削除不可
