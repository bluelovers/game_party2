require "./lib/_battle.cgi";
$is_npc_action = 0;
#=================================================
# パーティー戦 Created by Merino
#=================================================
# 勝ちカウントを計算
# 賞金計算

# パーティーカラー(NPCカラーとデフォルトカラーは使ったら×)
%colors = (
	'#FF3333'	=> 'レッド',
	'#FF33CC'	=> 'ピンク',
	'#FF9933'	=> 'オレンジ',
	'#FFFF33'	=> 'イエロー',
	'#33FF33'	=> 'グリーン',
	'#33CCFF'	=> 'アクア',
	'#6666FF'	=> 'ブルー',
	'#CC66FF'	=> 'パープル',
	'#CCCCCC'	=> 'グレイ',
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
		push @actions, 'ぱーてぃー';
		$actions{'しらべる'}   = [0,	sub{ &shiraberu }];
		$actions{'ぱーてぃー'} = [0,	sub{ &party }];
	}

	push @actions, 'かいし';
	$actions{'かいし'}     = [0,	sub{ &kaishi }];
}


#=================================================
# ＠ぱーてぃー
#=================================================
sub party {
	$target = shift;
	
	if ($round > 0) {
		$mes = "戦闘の途中で変更することはできません";
		return;
	}
	
	my %r_colors = reverse %colors;
	if (defined $r_colors{$target}) {
		$ms{$m}{color} = $r_colors{$target};
		$com.=qq|<font color="$r_colors{$target}">$target</font>パーティーに入りました！|;
		return;
	}
	
	my $p = '';
	for my $k (keys %colors) {
		$p .= qq|<span onclick="text_set('＠ぱーてぃー>$colors{$k} ')" style="color: $k;">$colors{$k}</span> / |;
	}
	$mes = "どのパーティーに入りますか？<br />$p";
}

#=================================================
# ＠かいし
#=================================================
sub kaishi {
	# 戦闘開始前
	if ($round < 1) {
		my %teams = ();
		for my $name (@members) {
			$mes .= "$name," if !$ms{$name}{color} || $ms{$name}{color} eq $default_color;
			++$teams{ $ms{$name}{color} } unless $teams{ $ms{$name}{color} };
		}
		if (keys %teams <= 1) {
			$mes = "対戦するパーティーがいません";
			return;
		}
		elsif ($mes) {
			$mes .= "のプレイヤーが、まだパーティーを決めていません";
			return;
		}
		elsif ($leader ne $m) {
			$mes = "一番始めの ＠かいし をすることができるのはリーダーのみです";
			return;
		}
	}
	else {
		# 賞金配り終わり。
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
			
			# 現在の途中経過
			for my $c (sort { $b <=> $a } keys %win_c) {
				$npc_com .= qq|<font color="$c">$colors{$c} $win_c{$c}勝</font> / |;
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

sub give_bet {
	my $winner = shift;
	
	my @win_members = ();
	for my $name (@members) {
		next unless $ms{$name}{color} eq $winner;
		push @win_members, $name;
	}
	
	open my $fh, "+< $questdir/$m{quest}/bet.cgi" or &error("$questdir/$m{quest}/bet.cgiファイルが開けません");
	eval { flock $fh, 2; };
	my $prize_money = <$fh>;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	close $fh;
	$prize_money =~ tr/\x0D\x0A//d;
	
	if (@win_members <= 0) {
		$npc_com .= "優勝パーティーがいないようです…";
		return;
	}
	
	my $p_money = int($prize_money / @win_members);
	
	for my $name (@win_members) {
		&send_money($name, $p_money, "$p_nameの闘技場の賞金");
		$names .= "$name,";
	}
	chop $names;
	$npc_com .= "優勝パーティーの$namesに <b>$p_money</b> Gが送られました！";
}


sub npc_turn { return } # 念のためハマリ防止


1; # 削除不可
