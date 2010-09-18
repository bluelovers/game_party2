#=================================================
# カジノ共通処理 Created by Merino
#=================================================
# ログに使うファイル(.cgi抜き)
$this_file = "$casinodir/$m{quest}/log";

#=================================================
# 戦闘用アクションセット(プレイヤー用)
#=================================================
sub set_action {
	unless (defined $ms{$m}{name}) {
		push @actions, ('にげる','すくしょ');
		$actions{'にげる'}   = sub{ &nigeru  };
		$actions{'すくしょ'} = sub{ &sukusho };
		return;
	}

	&add_casino_action;
	push @actions, ('にげる','すくしょ');
	$actions{'にげる'}   = sub{ &nigeru   };
	$actions{'すくしょ'} = sub{ &sukusho  };
	return unless defined $ms{$m}{name};

	if ($round == 0) { # 開始前
		push @actions, ('かいし','さそう');
		$actions{'かいし'} = sub{ &kaishi };
		$actions{'さそう'}  = sub{ &sasou  };
		if ($m eq $leader) { # リーダーのみ
			push @actions, ('きっく');
			$actions{'きっく'} = sub{ &kick };
		}
	}
}

#=================================================
# 画面ヘッダー
#=================================================
sub header_html {
	print qq|<div class="mes">【$this_title】 コイン<b>$m{coin}</b>枚</div>|;
}


# $FH 排他制御をするためのグローバル変数(このファイルのみ)。複数のプレイヤーが同じファイルを共有するため。
my $FH;
#=================================================
# メンバー読み込み
#=================================================
sub read_member {
	@members = ();
	%ms = (); # Members

	my $count = 0;
	open $FH, "+< $casinodir/$m{quest}/member.cgi" or do{ $m{lib} = ''; $m{quest} = ''; &write_user; &error("すでにパーティーが解散してしまったようです"); };
	eval { flock $FH, 2; };
	my $head_line = <$FH>;
	($speed,$stage,$round,$leader,$p_name,$p_pass,$p_join,$win,$bet,$is_visit,$now_bet,$max_bet) = split /<>/, $head_line;
	$act_time = $speed;
	while (my $line = <$FH>) {
		my @datas = split /<>/, $line;
		my $name  = $datas[0];
		my $i = 0;
		for my $k (@casino_datas) {
			$ms{$name}{$k} = $datas[$i];
			++$i;
		}
		push @members, $name;
	}
	
	$this_title = $stage eq 'ドッペル' ? "$p_name 賭けコイン<b>$bet</b>枚"
				: "$p_name ★レート<b>$bet</b>枚 ★現在のレート<b>$now_bet</b>枚 ★最大レート<b>$max_bet</b>枚";
	$bgimg = "$bgimgdir/casino.gif"; # 背景画像
}


#=================================================
# メンバー書き込み
#=================================================
sub write_member {
	return unless -d "$casinodir/$m{quest}";
	
	my $head_line = "$speed<>$stage<>$round<>$leader<>$p_name<>$p_pass<>$p_join<>$win<>$bet<>$is_visit<>$now_bet<>$max_bet<>\n";
	my @lines = ($head_line);
	for my $name (@members) {
		my $line = '';
		for my $k (@casino_datas) {
			$line .= "$ms{$name}{$k}<>";
		}
		push @lines, "$line\n";
	}
	
	seek  $FH, 0, 0;
	truncate $FH, 0;
	print $FH @lines;
	close $FH;
}

#=================================================
# 戦闘アクション
#=================================================
sub action {
	$com .= "\x20";
	$com =~ /＠(.+?)(?:(?:\x20|　)?&gt;(.+?)(?:\x20|　)|\x20|　)/;
	my $action = $1;
	my $target = $2 ? $2 : '';
	return unless defined $actions{$action};
 	if ($nokori > 0) {
		$mes = "まだ行動することはできません";
		return;
	}
	
	&{ $actions{$action} }($target);
	return if $mes;

	$m{wt}  = $time + $act_time;
	$nokori = $act_time;
	$ms{$m}{time} = $time;
	&write_member;
}


#=================================================
# ＠さそう
#=================================================
sub sasou {
	my $y = shift;

	$act_time = 0;
	$this_file = "$logdir/casino";

	if ($y) {
		$to_name = $y;
		return;
	}
	$mes .= "誰をさそいますか？<br />";
	open my $fh, "< ${this_file}_member.cgi" or &error("${this_file}_member.cgiファイルがが開けません"); 
	while (my $line = <$fh>) {
		my($ltime, $is_npc, $name, $laddr, $icon, $color) = split /<>/, $line;
		next if $time - $limit_member_time > $ltime;
		next if $sames{$name}++; # 同じ人なら次
		$mes .= qq|<span onclick="text_set('＠さそう>$name ')" style="color: $color;"><img src="$icondir/$icon" alt="$name" />$name</span>|;
	}
	close $fh;
}

#=================================================
# ＠きっく
#=================================================
sub kick {
	my $y = shift;
	
	$mes = "自分をきっくすることはできません"		if $y eq $m;
	$mes = "リーダーじゃないのできっくできません"	if $leader ne $m;
	$mes = "クエスト中はきっくできません"			if $round > 0;
	return if $mes;

	unless ($y) {
		$mes = "誰をきっくしますか？<br />";
		for my $name (@partys) {
			$mes .= qq|<span onclick="text_set('＠きっく>$name')">$name</span>|;
		}
		return;
	}
	
	for my $i (0 .. $#members) {
		if ($members[$i] eq $y) {
			&regist_you_data($y, 'lib', 'quest');
			&regist_you_data($y, 'wt', $time + 60);
			$com.="$yをきっくしました";
			splice(@members, $i, 1);
			
			my @lines = ();
			open my $fh, "+< $logdir/casino.cgi" or &error("$logdir/casino.cgiファイルが開けません");
			eval { flock $fh, 2 };
			while (my $line = <$fh>) {
				push @lines, $line;
			}
			push @lines, $line;
			unshift @lines, "$time<>$date<>$npc_name<>NPC<>$npc_color<>$p_nameのリーダー$mからきっくされました<>$y<>\n";
			seek  $fh, 0, 0;
			truncate $fh, 0;
			print $fh @lines;
			close $fh;
			
			last;
		}
	}
}


#=================================================
# ＠にげる
#=================================================
sub nigeru {
	$m{lib} = 'casino';

	# クエストのメンバーリストから除く
	my $is_join = 0;
	my @new_members = ();
	for my $name (@members) {
		if ($m eq $name) {
			$is_join = 1;
			next;
		}
		push @new_members, $name;
	}
	@members = @new_members;


	# 見学者はそのまま帰す
	unless ($is_join) {
		$mes ="$p_nameの見学から逃げ出しました";
		&reload("$p_nameの見学から逃げ出しました");
		return;
	}
	
	# 疲労度プラス
	$m{tired} += 1;
	$m{is_eat} = 0;
	
	&reload("部屋から逃げ出しました");

	# 誰もいなくなったらクエストを削除
	if (@members < 1) {
		&write_member;
		$this_file = "$logdir/casino";
		&delete_directory("$casinodir/$m{quest}");
		$mes = "部屋から逃げ出しました";
	}
	else {
		&next_round;

		# リーダーだった場合リーダー交代
		if ($leader eq $m) {
			$leader = $members[0];
			$npc_com = "$p_nameのリーダーが$leaderになりました";
		}
		&write_member;
	}
}


#================================================
# 闘技場、ギルド戦のゴールド、ギルドポイントの増減
#================================================
sub add_bet {
	my($quest_id, $add_bet) = @_;

	open my $fh, "+< $casinodir/$quest_id/bet.cgi" or &error("$casinodir/$quest_id/bet.cgiファイルが開けません");
	eval { flock $fh, 2; };
	my $bet = <$fh>;
	$bet =~ tr/\x0D\x0A//d;
	$bet += $add_bet;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh $bet;
	close $fh;
}



# コイン支払い
sub give_coin {
	my $give_coin = shift || $now_bet;
	$m{coin} -= $give_coin;
	&add_bet($m{quest}, $give_coin);
	$com.=qq|<span class="st_down">カジノコインを <b>$give_coin</b>枚 支払いました</span>|;
}


# コインがない人強制退場
sub reload_member {
	my $winner = shift;
	my @new_members = ();
	for my $name (@members) {
		my %p = &get_you_datas($name);
		if ($p{coin} <= 0) {
			$npc_com .= qq|<span class="die">$nameはコインがなくなった！</span><br />|;
			&regist_you_data($name, 'lib', 'casino');

			# リーダーだった場合リーダー交代
			if ($leader eq $name && $winner) {
				$leader = $winner;
				$npc_com .= "$p_nameのリーダーが$leaderになりました";
			}
		}
		else {
			$ms{$name}{action} = '待機中' unless $stage eq 'ハイロウ';
			push @new_members, $name;
		}
	}
	@members = @new_members;
}

# 賞金
sub get_coin {
	open my $fh, "+< $casinodir/$m{quest}/bet.cgi" or &error("$casinodir/$m{quest}/bet.cgiファイルが開けません");
	eval { flock $fh, 2; };
	my $get_coin = <$fh>;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh 0;
	close $fh;
	$get_coin =~ tr/\x0D\x0A//d;
	return $get_coin;
}

1; # 削除不可
