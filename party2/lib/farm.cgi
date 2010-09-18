#=================================================
# モンスターじいさん Created by Merino
#=================================================
# 場所名
$this_title = 'モンスターじいさん';

# NPC名
$npc_name   = '@モンジィ';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/farm";

# 背景画像
$bgimg   = "$bgimgdir/farm.gif";

# 家に連れて行ける数
$max_monster = 8;

#=================================================
# ＠はなすの会話
#=================================================
@words = (
	"わしが有名な$npc_nameじゃ。モンスターのことなら何でも聞いてくれい",
	"何度かモンスターを倒していると、なついてくるモンスターがいるのじゃ",
	"人間を好むモンスターもいるということじゃ",
	"$mの純粋な強さにモンスターはひきつけられるのじゃ",
	"自分の家には$max_monster匹までペットを連れて行くことができるぞい",
	"モンスターは最大30匹まで預かっておけるぞい。それ以上は、残念じゃが＠わかれるしかないのぉ…",
	"モンスター預かり所がまんぱんの状態だと、モンスターは仲間にならんから注意じゃ",
	"自分が相手より強い方が仲間になりやすいぞい",
	"ふがふがふがふがふがふがふが",
);

#=================================================
# 追加アクション
#=================================================
push @actions, 'つれてく';
push @actions, 'なづける';
push @actions, 'あずける';
push @actions, 'おくる';
push @actions, 'わかれる';
$actions{'つれてく'} = sub{ &tureteku }; 
$actions{'なづける'} = sub{ &nazukeru }; 
$actions{'あずける'} = sub{ &azukeru }; 
$actions{'おくる'}   = sub{ &okuru }; 
$actions{'わかれる'} = sub{ &wakareru }; 

#=================================================
# ＠おくる
#=================================================
sub okuru {
	my $target = shift;
	my($pet, $yname) = split /＠あいて&gt;/, $target;
	
	if ($yname) {
		my $yid = unpack 'H*', $yname;
		unless (-f "$userdir/$yid/user.cgi") {
			$mes = "$ynameというプレイヤーは存在しません";
			return;
		}

		if ( &is_full_monster($yid) ) {
			$mes = "$nameのモンスター預かり所がいっぱいです";
			return
		}
	}

	my $p = '';
	my @lines = ();
	open my $fh, "+< $userdir/$id/monster.cgi" or &error("$userdir/$id/monster.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($mname, $micon) = split /<>/, $line;
		if ($yname && !$npc_com && $pet eq $mname) {
			my $yid = unpack 'H*', $yname;
			open my $fh2, ">> $userdir/$yid/monster.cgi" or &error("$userdir/$yid/monster.cgiファイルが開けません");
			print $fh2 "$mname<>$micon<>\n";
			close $fh2;
			$npc_com .= "$mnameを$ynameのモンスター預かり所に送っておいたぞ";
		}
		else {
			push @lines, $line;
			$p .= qq|<span onclick="text_set('＠おくる>$mname＠あいて')"><img src="$icondir/$micon" />$mname</span> |;
		}
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	return if $npc_com;
	$mes = qq|どのモンスターを誰に送るのじゃ？<br />$p|;
	$act_time = 0;
}
#=================================================
# ＠わかれる
#=================================================
sub wakareru {
	$y = shift;
	
	my $p = '';
	my @lines = ();
	open my $fh, "+< $userdir/$id/monster.cgi" or &error("$userdir/$id/monster.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($name, $icon) = split /<>/, $line;
		if (!$npc_com && $y eq $name) {
			$npc_com = "$nameを野生に帰しといたぞ";
		}
		else {
			push @lines, $line;
			$p .= qq|<span onclick="text_set('＠わかれる>$name ')"><img src="$icondir/$icon" />$name</span> |;
		}
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	return if $npc_com;
	$mes = qq|どのモンスターと別れるのじゃ？<br />$p|;
	$act_time = 0;
}

#=================================================
# ＠つれてく
#=================================================
sub tureteku {
	my $y = shift;
	
	my $p = '';
	my @lines = ();
	open my $fh, "+< $userdir/$id/monster.cgi" or &error("$userdir/$id/monster.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($name, $icon) = split /<>/, $line;
		if (!$npc_com && $y eq $name) {
			&_add_home_member($name, $icon);
			return if $mes;
			$npc_com = "$nameを$mの家に送っておいたぞ";
		}
		else {
			push @lines, $line;
			$p .= qq|<span onclick="text_set('＠つれてく>$name ')"><img src="$icondir/$icon" />$name</span> |;
		}
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;

	return if $npc_com;
	$mes = qq|どのモンスターを連れて行くのじゃ？<br />$p|;
	$act_time = 0;
}
sub _add_home_member {
	my($add_name, $add_icon) = @_;

	my $count = 0;
	open my $fh, "< $userdir/$id/home_member.cgi" or &error("$userdir/$id/home_member.cgiファイルが読み込めません");
	while (my $line = <$fh>) {
		my($ltime, $is_npc, $name, $laddr, $icon, $color) = split /<>/, $line;
		next unless $is_npc;
		if ($add_name eq $name) {
			$mes = qq|<span onclick="text_set('＠なづける>$add_name＠なまえ>')">$mの家に同じ名前のモンスターがいます。「＠なづける」で名前を変えてください</span>|;
			return;
		}
		++$count;
	}
	close $fh;

	if ($count >= $max_monster) {
		$mes = "これ以上、モンスターを家に連れて行くことはできません";
		return;
	}
	else {
		open my $fh2, ">> $userdir/$id/home_member.cgi" or &error("$userdir/$id/home_member.cgiファイルが開けません");
		print $fh2 "$time<>1<>$add_name<>0<>$add_icon<>$npc_color<>\n";
		close $fh2;
	}
}

#=================================================
# ＠あずける
#=================================================
sub azukeru {
	my $y = shift;
	
	if ( &is_full_monster($id) ) {
		$mes = "これ以上、モンスターを預かることはできんぞ";
		return;
	}
	
	my $p = '';
	my @lines = ();
	open my $fh, "+< $userdir/$id/home_member.cgi" or &error("$userdir/$id/home_member.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($ltime, $is_npc, $name, $laddr, $icon, $color) = split /<>/, $line;
		unless ($is_npc) {
			push @lines, $line;
			next;
		}
		if (!$npc_com && $y eq $name) {
			open my $fh2, ">> $userdir/$id/monster.cgi" or &error("$userdir/$id/monster.cgiファイルが開けません");
			print $fh2 "$name<>$icon<>\n";
			close $fh2;
			$npc_com = "$nameを預かっておくぞ";
		}
		else {
			push @lines, $line;
			$p .= qq|<span onclick="text_set('＠あずける>$name ')"><img src="$icondir/$icon" />$name</span> |;
		}
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;

	return if $npc_com;
	$mes = qq|どのモンスターを預けるのじゃ？<br />$p|;
	$act_time = 0;
}


#=================================================
# ＠なづける
#=================================================
sub nazukeru {
	my $target = shift;
	
	my($y, $new_name) = split /＠なまえ&gt;/, $target;
	
	if ($y && $new_name) {
		$mes = qq|<span onclick="text_set('＠なづける>$y＠なまえ>')">モンスター名に不正な空白が含まれています</span>|					if $new_name =~ /　|\s/;
		$mes = qq|<span onclick="text_set('＠なづける>$y＠なまえ>')">モンスター名に不正な文字( ,;\"\'&<> )が含まれています</span>| 	    if $new_name =~ /[,;\"\'&<>]/;
		$mes = qq|<span onclick="text_set('＠なづける>$y＠なまえ>')">モンスター名に不正な文字( ＠ )が含まれています</span>| 			if $new_name =~ /＠/;
		$mes = qq|<span onclick="text_set('＠なづける>$y＠なまえ>')">モンスター名は全角４文字[半角８文字]までです</span>|				if length($new_name) > 8;
		return if $mes;
	}

	my @lines = ();
	my $p = '';
	open my $fh, "+< $userdir/$id/monster.cgi" or &error("$userdir/$id/monster.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($name, $icon) = split /<>/, $line;
		if (!$npc_com && $new_name && $y eq $name) {
			push @lines, "$new_name<>$icon<>\n";
			$npc_com = "$yを$new_nameと名づけたぞ";
		}
		else {
			push @lines, $line;
		}
		$p .= qq|<span onclick="text_set('＠なづける>$name＠なまえ>')"><img src="$icondir/$icon" />$name</span> |;
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	return if $npc_com;
	$mes = qq|どのモンスターに何と名づけるのじゃ？<br />$p|;
	$act_time = 0;
}


1; # 削除不可
