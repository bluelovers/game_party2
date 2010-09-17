$is_add_effect = 0; # 追加効果の場合は非表示にするフラグ
#=================================================
# 技･魔法 Created by Merino
#=================================================

#=================================================
# 戦闘用アクションセット(プレイヤー用)
#=================================================
sub set_action {
	&get_header_data;
	
	unless (defined $ms{$m}{name}) {
		push @actions, ('ささやき','にげる','すくしょ');
		$actions{'ささやき'} = [0, sub{ &sasayaki }];
		$actions{'にげる'}   = [0, sub{ &nigeru   }];
		$actions{'すくしょ'} = [0, sub{ &sukusho  }];
		return;
	}
	
	my @skills = ();
	if ($round > 0 && @enemys > 0) {
		if ($ms{$m}{sp}) {
			push @skills, &{ 'skill_'.$ms{$m}{job} };
			push @skills, ([0, 0, 'br', sub{ return } ]);
			for my $i (0.. $#skills) {
				next if $skills[$i][0] > $ms{$m}{sp};
				next if $skills[$i][1] > $ms{$m}{mp};
				push @actions, "$skills[$i][2]";
				$actions{$skills[$i][2]} = [ $skills[$i][1], $skills[$i][3] ];
			}
		}

		@skills = ();
		if ($ms{$m}{old_sp}) {
			push @skills, &{ 'skill_'.$ms{$m}{old_job} };
			push @skills, ([0, 0, 'br', sub{ return } ]);
		}

		push @skills, (
			[0,	0,	'こうげき',		sub{ &kougeki	}],
			[0,	0,	'ぼうぎょ',		sub{ $ms{$m}{tmp} = '防御'; $com.=qq|<span class="tmp">$mは身を固めている</span>|;	}],
			[0,	0,	'てんしょん',	sub{ &tenshon($m)	}],
		);
	}
	
	push @skills, ([0, 0, 'どうぐ',   sub{ &dougu }])  if $ites[$m{ite}][3] eq '1'; # 戦闘使用可アイテム持っている場合
	push @skills, ([0, 0, 'まえ',     sub{ &mae }],      [0, 0, 'うしろ', sub{ &ushiro }]) if @partys > 1; # 2人以上
	push @skills, ([0, 0, 'ささやき', sub{ &sasayaki }], [0, 0, 'にげる', sub{ &nigeru }], [0, 0, 'すくしょ', sub{ &sukusho }]); # 戦闘用追加アクション
	push @skills, ([0, 0, 'さそう',   sub{ &sasou  }]) if $round == 0; # 開始前 && ﾘｰﾀﾞｰのみ
	push @skills, ([0, 0, 'きっく',   sub{ &kick }])   if $round == 0 && $m eq $leader; # 開始前 && ﾘｰﾀﾞｰのみ

	for my $i (0.. $#skills) {
		next if $skills[$i][0] > $ms{$m}{old_sp};
		next if $skills[$i][1] > $ms{$m}{mp};
		push @actions, "$skills[$i][2]";
		$actions{$skills[$i][2]} = [ $skills[$i][1], $skills[$i][3] ];
	}

	&add_battle_action;
}

#=================================================
# ＠どうぐ
#=================================================
sub dougu {
	my $y = shift || $m;
	$com .= "$ites[$m{ite}][1] をつかった！";
	&{ $ites[$m{ite}][4] }($y);
	return if $mes;
	$m{ite} = 0;
}

#=================================================
# ＠さそう
#=================================================
sub sasou {
	my $y = shift;

	$act_time = 0;
	$this_file = "$logdir/quest";

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
			open my $fh, "+< $logdir/quest.cgi" or &error("$logdir/quest.cgiファイルが開けません");
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
# 自分の素早さと相手の素早さ(*３倍)を比較(回避・会心の一撃の確率)
#『 * 3』の数字を小さくすれば回避や会心撃の確率が上がり、数字を大きくすれば回避や会心撃の確率が下がる
#=================================================
sub _is_exceed_ag {
	my($_m, $_y) = @_;
	return 0 if !$_m || !$_y;
	return rand(3) < 1 && rand($ms{$_m}{ag}) >= rand($ms{$_y}{ag}*3) ? 1 : 0;
}

#=================================================
# ＠こうげき
#=================================================
sub kougeki {
	my $y = shift;
	$y = $enemys[int(rand(@enemys))] if !defined($ms{$y}{name}) || $ms{$y}{color} eq $ms{$m}{color};

	if ( &_is_exceed_ag($m, $y) ) {
		$com .= qq|<span class="kaishin">会心の一撃！！</span>|;
		&_damage($y, $ms{$m}{at} * 0.75, '攻', 1);
	}
	else {
		&_damage($y, $ms{$m}{at}, '攻');
	}
}
#=================================================
# ＠まえ
#=================================================
sub mae {
	@enemys = ();
	for my $name (@members) {
		next if !defined $ms{$m}{name};
		next if $ms{$m}{color} eq $ms{$name}{color};
		push @enemys, $name;
	}
	
	my @new_partys = ($m);
	for my $name (@partys) {
		next if $m eq $name;
		push @new_partys, $name;
	}
	@partys = @new_partys;
	@members = (@partys,@enemys);
}

#=================================================
# ＠うしろ
#=================================================
sub ushiro {
	@enemys = ();
	for my $name (@members) {
		next if !defined $ms{$m}{name};
		next if $ms{$m}{color} eq $ms{$name}{color};
		push @enemys, $name;
	}

	my @new_partys = ();
	for my $name (@partys) {
		next if $m{name} eq $name;
		push @new_partys, $name;
	}
	push @new_partys, $m;
	@partys = @new_partys;
	@members = (@partys,@enemys);
}

#=================================================
# ＠てんしょん
#=================================================
%ten_names = (
	1.7		=> qq|<font color="#FFFF99">ﾃﾝｼｮﾝ</font>|,
	3		=> qq|<font color="#FFCC00">ﾃﾝｼｮﾝ</font>|,
	5		=> qq|<font color="#FFFF00">ﾊｲﾃﾝｼｮﾝ</font>|,
	8		=> qq|<font color="#FF0000">Sﾊｲﾃﾝｼｮﾝ</font>|,
);
sub tenshon {
	my $y = shift || $m;
	if ($ms{$y}{ten} <= 1) {
		$ms{$y}{ten} = 1.7;
		$com .= qq|$yのテンションが <span class="tenshon">5％</span> になった！|;
	}
	elsif ($ms{$y}{ten} <= 2) {
		$ms{$y}{ten} = 3;
		$com .= qq|$yのテンションが <span class="tenshon">20％</span> になった！|;
	}
	elsif ($ms{$y}{ten} <= 3) {
		$ms{$y}{ten} = 5;
		$com .= qq|$yのテンションが <span class="tenshon">50％</span> になった！$yは<span class="tenshon">ハイテンション</span>になった！|;
	}
	else {
		if ( $m{lv} < 25 || $ms{$y}{ten} >= 8 || $m{lv} < int(rand(50)+20) ) {
			$com .= qq|$yのテンションはこれ以上あがらないようだ|;
		}
		else {
			$ms{$y}{ten} = 8;
			$com .= qq|$yのテンションが <span class="tenshon">100％</span> になった！$yは<span class="tenshon">スーパーハイテンション</span>になった！|;
		}
	}
}

#=================================================
# スキル一覧
#=================================================
# 属性…物理攻撃→攻、魔法攻撃→魔、ブレス→息、踊る→踊
# 状態異常…麻痺、眠り、猛毒、混乱、魔封、踊封、動封
# 「$is_add_effect = 1;」は、攻撃＋状態異常などで使用。「～をかわした」のメッセージが表示されなくなる。
#=================================================
sub skill_0 { # 敵用てんしょん、ぼうぎょ。攻撃する確立が下がってしまうので、こうげきの配列を追加
	return (
	# [必要SP, 使用MP, 'スキル名(＠＊＊＊＊)', sub{ プログラム処理 }],
		[8,		0,	'こうげき',		sub{ &kougeki	}],
		[9,		0,	'こうげき',		sub{ &kougeki	}],
		[10,	0,	'こうげき',		sub{ &kougeki	}],
		[20,	0,	'てんしょん',	sub{ &tenshon($m)	}],
		[30,	0,	'ぼうぎょ',		sub{ $ms{$m}{tmp} = '防御'; $com.=qq|<span class="tmp">$mは身を固めている</span>|;	}],
	);
}
sub skill_1 { # 戦士
	return (
		[5,		5,		'かぶとわり',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at}*0.9, '攻'); return if !$y || $ms{$y}{hp} <= 0; &_st_down($y, 0.15, '攻', 'df');	}],
		[8,		0,		'かばう',			sub{ my($y) = &_check_party(shift, 'かばう', '攻'); return if !$y || $y eq $m; $ms{$m}{tmp} = 'かばい中'; $ms{$y}{tmp} = 'かばう'; $com.=qq|<span class="tmp">$mは$yをかばっている</span>|;	}],
		[25,	8,		'ちからをためる',	sub{ &_st_up($m, 1.0, '攻', 'at');	}],
		[50,	5,		'がんせきなげ',		sub{ &_damages(90, '攻', 1);	}],
		[80,	10,		'まじんぎり',		sub{ rand(2) < 1 ? &_damage(shift, $ms{$m}{at} * 3, '攻') : &_damage(shift, 20, '攻');	}],
	);
}
sub skill_2 { # 剣士
	return (
		[5,		3,		'しんくうぎり',		sub{ &_damage(shift, $ms{$m}{ag}*1.5, '攻');	}],
		[10,	4,		'みねうち',			sub{ &_st_d(shift, '動封', '攻', 80);	}],
		[20,	5,		'うけながし',		sub{ $ms{$m}{tmp} = '受流し'; $com.=qq|<span class="tmp">$mは攻撃を受流すかまえをとった</span>|;	}],
		[30,	0,		'かばう',			sub{ my($y) = &_check_party(shift, 'かばう', '攻'); return if !$y || $y eq $m; $ms{$m}{tmp} = 'かばい中'; $ms{$y}{tmp} = 'かばう'; $com.=qq|<span class="tmp">$mは$yをかばっている</span>|;	}],
		[50,	6,		'メタルぎり',		sub{ &_damage(shift, $ms{$m}{at}*0.4, '無', 1);		}],
		[80,	12,		'はやぶさぎり',		sub{ my $y = shift; for my $i (1..2) { last if $ms{$m}{hp} <= 0; &_damage($y, $ms{$m}{ag}*2.2, '攻'); };	}],
		[100,	21,		'さみだれぎり',		sub{ &_damages($ms{$m}{at}, '攻');	}],
	);
}
sub skill_3 { # 騎士
	return (
		[1,		0,		'かばう',			sub{ my($y) = &_check_party(shift, 'かばう', '攻'); return if !$y || $y eq $m; $ms{$m}{tmp} = 'かばい中'; $ms{$y}{tmp} = 'かばう'; $com.=qq|<span class="tmp">$mは$yをかばっている</span>|;	}],
		[5,		2,		'まもりをかためる',	sub{ &_st_up($m, 0.4, '攻', 'df');		}],
		[15,	5,		'すてみ',			sub{ $com.=qq|<span class="tmp">$mは守りを気にせずすてみで攻撃！</span>|; &_damage(shift, $ms{$m}{at}*2, '攻'); $ms{$m}{tmp}='２倍';	}],
		[25,	3,		'だいぼうぎょ',		sub{ $ms{$m}{tmp}='大防御'; $com.=qq|<span class="tmp">$mは守りのかまえをとった！</span>|;	}],
		[40,	7,		'スクルト',			sub{ &_st_ups(0.25, '魔', 'df');	}],
		[60,	1,		'メガザル',			sub{ $com.=qq|<span class="die">$mは自分の命をささげました！</span>|; for my $y (@partys) { next if $m eq $y; $com .= $ms{$y}{hp} > 0 ? qq|$yの$e2j{hp}が<span class="heal">全回復</span>した！| : qq|<span class="revive">$yが生き返った！</span>|; $ms{$y}{hp} = $ms{$y}{mhp}; }; &defeat($m); $ms{$m}{mp} = 1;	}],
		[80,	18,		'グランドクロス',	sub{ &_damages($ms{$m}{df} * 1.5, '攻');	}],
	);
}
sub skill_4 { # 武闘家
	return (
		[1,		0,		'せいしんとういつ',	sub{ $ms{$m}{hit}=95; $com.=qq|<span class="st_up">$mは心を落ちつかせ命中率が回復した</span>|;	}],
		[5,		3,		'みかわしきゃく',	sub{ &_st_up($m, 0.4, '攻', 'ag');				}],
		[14,	4,		'ひざげり',			sub{ &_damage(shift, $ms{$m}{at}*1.2, '攻');				}],
		[25,	3,		'あしばらい',		sub{ &_st_d(shift, '動封', '攻', 75);		}],
		[45,	11,		'きゅうしょづき',	sub{ &_death(shift, '即死', '攻', 19);	}],
		[70,	15,		'せいけんづき',		sub{ &_damage(shift, $ms{$m}{at}*1.5, '攻');		}],
		[100,	20,		'ばくれつけん',		sub{ my $v = int(rand(3)+3); for my $i (1..$v) { last if $ms{$m}{hp} <= 0; &_damage(undef, $ms{$m}{at} * 0.8, '攻'); };	}],
	);
}
sub skill_5 { # 僧侶
	return (
		[1,		3,		'スカラ',	sub{ &_st_up(shift, 0.4, '魔', 'df');	}],
		[3,		2,		'キアリー',	sub{ &_st_h(shift, '猛毒', '魔');	}],
		[6,		3,		'ホイミ',	sub{ &_heal(shift, 30, '魔');	}],
		[12,	4,		'バギ',		sub{ &_damages(rand(25)+10, '魔', 1);	}],
		[24,	10,		'ベホイミ',	sub{ &_heal(shift, 90, '魔');	}],
		[45,	10,		'バギマ',	sub{ &_damages(rand(40)+25, '魔', 1);	}],
		[60,	20,		'ザオラル',	sub{ my($y) = &_check_party(shift, '蘇生', '魔'); return if !$y || $ms{$y}{hp} > 0; if (rand(2) < 1) { $com.=qq|なんと、<span class="revive">$yが生き返りました！</span>|; $ms{$y}{hp}=int($ms{$y}{mhp} * 0.5); } else { $com.=qq|しかし、$yは生き返らなかった…|; };	}],
		[100,	30,		'ベホマ',	sub{ &_heal(shift, 999, '魔');	}],
	);
}
sub skill_6 { # 魔法使い
	return (
		[1,		2,		'メラ',			sub{ &_damage(shift, 20, '魔', 1);			}],
		[4,		4,		'ルカニ',		sub{ &_st_down(shift, 0.4, '魔', 'df');	}],
		[8,		5,		'ギラ',			sub{ &_damages(25, '魔', 1);				}],
		[14,	7,		'マヌーサ',		sub{ &_st_downs(0.2, '魔', 'hit');			}],
		[20,	8,		'メラミ',		sub{ &_damage(shift, 70, '魔', 1);		}],
		[30,	8,		'ラリホー',		sub{ &_st_d(shift, '眠り', '魔', 65);		}],
		[55,	11,		'ベギラマ',		sub{ &_damages(60, '魔', 1)				}],
		[90,	30,		'メラゾーマ',	sub{ &_damage(shift, 220, '魔', 1);		}],
	);
}
sub skill_7 { # 商人
	return (
		[2,		2,		'まもりをかためる',	sub{ &_st_up($m, 0.4, '攻', 'df');		}],
		[7,		1,		'ゴールドハンマー',	sub{ my($y, $v) = &_damage(shift, $ms{$m}{at}*0.8, '攻'); return if !$y; $v = int($v * 0.1)+5; $m{money}+=$v; $com.="$v Gを手に入れました！";	}],
		[12,	6,		'すなけむり',		sub{ &_st_downs(0.2, '息', 'hit');	}],
		[20,	0,		'とうぞくのはな',	sub{ my $y = shift; $y = $members[int(rand(@members))] if !defined($ms{$y}{name}); if ($y =~ /^@.+宝箱.$/) { my $item_name = $ms{$y}{get_money} eq '0' ? 'からっぽ' : $ms{$y}{get_exp} eq '1' ? $weas[$ms{$y}{get_money}][1] : $ms{$y}{get_exp} eq '2' ? $arms[$ms{$y}{get_money}][1] : $ites[$ms{$y}{get_money}][1]; $com.="宝箱の中身は $item_name のようだ…"; } else { my @smells=(qw/いい おいしそうな バラの あまい 変な やばい さわやかな ワイルドな/); my $v=int(rand(@smells)); $com.="$yは $smells[$v] においがする"; };	}],
		[35,	4,		'たいあたり',		sub{ my($y, $v) = &_damage(shift, $ms{$m}{df} * 1.6, '攻'); return if $v <= 0; &_risk($v * 0.07);		}],
		[45,	1,		'マホアゲル',		sub{ my($y) = &_check_party(shift, '魔与', '魔'); return if !$y; $v = int($ms{$m}{mp} * 0.5); $ms{$m}{mp} -= $v; $com.= qq|$mは$e2j{mmp}を$yに <span class="heal">$v</span> あたえた！|; &_mp_h($y, $v, '魔');	}],
		[65,	7,		'メダパニダンス',	sub{ &_st_ds('混乱', '踊', 60);	}],
		[80,	1,		'メガンテ',			sub{ $com.=qq|<span class="die">$mは自爆した！</span>|; &_deaths('即死', '無', 60); &defeat($m); $ms{$m}{mp} = 1; 	}],
	);
}
sub skill_8 { # 遊び人
	return (
		[1,		0,		'ねる',				sub{ $ms{$m}{state}='眠り'; $com.="$mは眠りだした"; &_heal($m, $ms{$m}{mhp}*0.5);	}],
		[4,		0,		'なげきっす',		sub{ my $y=$members[int(rand(@members))]; $ms{$y}{state}='麻痺'; $ms{$y}{ten}=1; $com.=qq|$mは$yに投げキッスをし<span class="state">$yは痺れました！</span>|;		}],
		[8,		0,		'パフパフ',			sub{ my $y=$members[int(rand(@members))]; $ms{$y}{state}='動封'; $ms{$y}{ten}=1; $com.=qq|$mは$yにパフパフをした！<span class="state">$yは動きが止まった！</span>|;	}],
		[12,	0,		'きけんなあそび',	sub{ my $y=$members[int(rand(@members))]; $ms{$y}{state}='猛毒'; $ms{$y}{ten}=1; $com.=qq|$mの危険な遊びにより<span class="state">$yは猛毒になりました！</span>|;	}],
		[18,	0,		'ちょうはつ',		sub{ for my $y (@members) { next if $ms{$y}{hp} <= 0 || $m eq $y || rand(2) < 1; &tenshon($y); };	}],
		[24,	0,		'からかう',			sub{ my $y = shift; ($y) = defined($ms{$y}{name}) ? $y : &_check_enemy($y, 'テン', '無'); &tenshon($y);		}],
		[36,	0,		'いっぱつぎゃぐ',	sub{ my @gags = ('教会に行くのは今日かい？','ルカナンでも唱えるかなん♪','そんなステテコパンツもうステテコい！','スカラを使ってすかられた','アンタそうりょかい？そうりょ','やくそうをこんがりやくぞう♪','賢者を発見じゃ！'); my $gag = $gags[int(rand(@gags))]; $com.="『$gag』…"; for my $y (@members) { next if $y eq $m; next if rand(3) < 1; $com.="$yは笑い転げた！"; $ms{$y}{state}='動封'; $ms{$y}{ten}=1;	 };	}],
		[50,	0,		'クールジョーク',	sub{ for my $y (@enemys) { $ms{$y}{ten} = 1; }; $com.="全員のテンションが下がった…";	}],
	);
}
sub skill_9 { # 盗賊
	return (
		[3,		3,		'ボミエ',			sub{ &_st_down(shift,  0.4, '魔', 'ag');	}],
		[6,		3,		'ピオラ',			sub{ &_st_up(shift, 0.4, '魔', 'ag');	}],
		[12,	7,		'いしつぶて',		sub{ &_st_ds('混乱', '息', 45);	}],
		[20,	0,		'とうぞくのはな',	sub{ my $y = shift; $y = $members[int(rand(@members))] if !defined($ms{$y}{name}); if ($y =~ /^@.+宝箱.$/) { my $item_name = $ms{$y}{get_money} eq '0' ? 'からっぽ' : $ms{$y}{get_exp} eq '1' ? $weas[$ms{$y}{get_money}][1] : $ms{$y}{get_exp} eq '2' ? $arms[$ms{$y}{get_money}][1] : $ites[$ms{$y}{get_money}][1]; $com.="宝箱の中身は $item_name のようだ…"; } else { my @smells=(qw/いい おいしそうな バラの あまい 変な やばい さわやかな ワイルドな/); my $v=int(rand(@smells)); $com.="$yは $smells[$v] においがする"; };	}],
		[35,	9,		'あまいいき',		sub{ &_st_ds('眠り', '息', 35);	}],
		[50,	1,		'インパス',			sub{ my $y = shift; $y = $members[int(rand(@members))] if !defined($ms{$y}{name}); $com.="<br />$y $e2j{mhp}:$ms{$y}{hp}/$ms{$y}{mhp}, $e2j{mmp}:$ms{$y}{mp}/$ms{$y}{mmp}, $e2j{at}:$ms{$y}{mat}, $e2j{df}:$ms{$y}{mdf}, $e2j{ag}:$ms{$y}{mag}";	}],
		[70,	8,		'まひこうげき',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at} * 1.2, '攻'); return if !$y || $ms{$y}{hp} <= 0; &_st_d($y, '麻痺', '攻', 30);	}],
		[90,	15,		'アーマーブレイク',	sub{ my($y) = &_check_enemy(shift, '破壊', '攻'); return if !$y; $ms{$y}{tmp}=''; $ms{$y}{ten}=1; $ms{$y}{df}=$ms{$y}{mdf}; $com.="$yの防具の強さを封じた！"; &_st_down($y, 0.1, '攻', 'df');	}],
	);
}
sub skill_10 { # 羊使い
	return (
		[1,		0,		'ねる',				sub{ $ms{$m}{state}='眠り'; $com.=qq|<span class="state">$mは眠りだした</span>|; &_heal($m, $ms{$m}{mhp}*0.5);	}],
		[3,		3,		'スカラ',			sub{ &_st_up(shift, 0.4, '魔', 'df');	}],
		[10,	4,		'たいあたり',		sub{ my($y, $v) = &_damage(shift, $ms{$m}{df} * 1.6, '攻'); return if $v <= 0; &_risk($v * 0.07);		}],
		[20,	10,		'ベホイミ',			sub{ &_heal(shift, 90, '魔');	}],
		[40,	9,		'ねむりのうた',		sub{ &_st_ds('眠り', '歌', 45);		}],
		[60,	1,		'マホキテ',			sub{ return if &is_bad_state('魔'); $ms{$m}{tmp} = '魔吸収'; $com.=qq|<span class="tmp">$mは不思議な光に包まれた！</span>|;	}],
		[80,	7,		'ウールガード',		sub{ &_st_up($m, 0.5, '無', 'df'); $ms{$m}{tmp} = '魔軽減'; $com.=qq|<span class="tmp">$mは魔法の光で守られた！</span>|;	}],
		[100,	20,		'どとうのひつじ',	sub{ my $v = int(rand(3)+2); for my $i (1..$v) { last if $ms{$m}{hp} <= 0; &_damage(undef, $ms{$m}{ag} * 1.6, '攻'); };	}],
	);
}
sub skill_11 { # 弓使い
	return (
		[5,		3,		'かげぬい',				sub{ &_st_d(shift, '動封', '攻', 80);	}],
		[10,	0,		'せいしんとういつ',		sub{ $ms{$m}{hit}=95; $com.=qq|<span class="st_up">$mは心を落ちつかせ命中率が回復した</span>|;	}],
		[20,	8,		'でたらめや',			sub{ &_damages($ms{$m}{ag}*1.4, '攻');	}],
		[40,	4,		'ようせいのや',			sub{ my($y, $v) = &_st_down(shift, 0.15, '攻', 'mp'); return if !$y; &_mp_h($m, $v, '攻');	}],
		[60,	6,		'フラッシュアロー',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at}*1.2, '攻'); return if !$y || $ms{$y}{hp} <= 0; &_st_down($y, 0.07, '攻', 'hit');	}],
		[90,	20,		'ラリホーアロー',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at}*1.1, '攻'); return if !$y || $ms{$y}{hp} <= 0; &_st_d($y, '眠り', '攻', 55);	}],
		[110,	24,		'みだれうち',			sub{ my $v = int(rand(2)+3); for my $i (1..$v) { last if $ms{$m}{hp} <= 0; &_damage(undef, $ms{$m}{at} * 0.85, '攻'); };		}],
	);
}
sub skill_12 { # 魔物使い
	return (
		[3,		2,		'ひのいき',			sub{ &_damages(18, '息', 1);	}],
		[10,	7,		'もうどくのきり',	sub{ &_st_ds('猛毒', '息', 60);	}],
		[18,	5,		'かえんのいき',		sub{ &_damages(50, '息', 1);	}],
		[32,	11,		'しびれうち',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at}*1.1, '攻'); return if !$y || $ms{$y}{hp} <= 0; &_st_d($y, '麻痺', '攻', 40);	}],
		[50,	5,		'なめまわす',		sub{ &_st_d(shift, '動封', '攻', 85);	}],
		[80,	14,		'はげしいほのお',	sub{ &_damages(90, '息', 1);	}],
		[110,	12,		'そうりゅううち',	sub{ my $y = shift; for my $i (1..2) { last if $ms{$m}{hp} <= 0; &_damage($y, $ms{$m}{at}*1.6, '攻'); };	}],
	);
}
sub skill_13 { # 吟遊詩人
	return (
		[5,		3,		'ふしぎなうた',			sub{ &_st_downs(0.25, '歌', 'mp');	}],
		[15,	7,		'いやしのうた',			sub{ &_heals(30, '歌');				}],
		[30,	5,		'めざめのうた',			sub{ &_st_hs('眠り', '歌');			}],
		[40,	6,		'まもりのうた',			sub{ &_st_ups(0.4, '歌', 'df');		}],
		[60,	9,		'ねむりのうた',			sub{ &_st_ds('眠り', '歌', 50);		}],
		[90,	10,		'たたかいのうた',		sub{ &_st_ups(0.6, '歌', 'at');		}],
	);
}
sub skill_14 { # 踊り子
	return (
		[4,		3,		'みかわしきゃく',	sub{ &_st_up($m, 0.4, '踊', 'ag');	}],
		[9,		3,		'ふしぎなおどり',	sub{ &_st_down(shift, 0.4, '踊', 'mp');	}],
		[16,	5,		'うけながし',		sub{ $ms{$m}{tmp} = '受流し'; $com.=qq|<span class="tmp">$mは攻撃を受流すかまえをとった</span>|;	}],
		[30,	9,		'ムーンサルト',		sub{ &_damages($ms{$m}{at}*0.8, '攻');	}],
		[45,	1,		'メガザルダンス',	sub{ $com.="$mの命をかけた踊り！"; for my $y (@partys) { next if $m eq $y; $com .= $ms{$y}{hp} > 0 ? qq|$yの$e2j{hp}が<span class="heal">全回復</span>した！| : qq|<span class="revive">$yが生き返った！</span>|; $ms{$y}{hp} = $ms{$y}{mhp}; }; &defeat($m); $ms{$m}{mp} = 1; $com.=qq|<span class="die">$mは力尽きた…</span>|;	}],
		[70,	16,		'つるぎのまい',		sub{ my $v = int(rand(3)+2); for my $i (1..$v) { last if $ms{$m}{hp} <= 0; &_damage(undef, $ms{$m}{at}*0.8, '踊'); };	}],
		[100,	12,		'ハッスルダンス',	sub{ &_heals(140, '踊');	}],
	);
}
sub skill_15 { # 黒魔道士
	return (
		[5,		6,		'ポイズン',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, 30, '魔', 1); return if !$y || $ms{$y}{hp} <= 0; &_st_d($y, '猛毒', '魔', 80);	}],
		[10,	5,		'ファイア',		sub{ &_damage(shift, 35, '魔', 1);	}],
		[20,	8,		'スリプル',		sub{ &_st_d(shift, '眠り', '魔', 55);	}],
		[40,	7,		'リフレク',		sub{ my($y) = &_check_party(shift, '魔反撃', '魔'); return if !$y; $ms{$y}{tmp} = '魔反撃'; $com.=qq|<span class="tmp">$yは魔法の壁で守られた！</span>|;	}],
		[60,	3,		'アスピル',		sub{ my($y, $v) = &_st_down(shift, 0.2, '魔', 'mp'); return if !$y; &_mp_h($m, $v, '魔');	}],
		[80,	16,		'ドレイン',		sub{ my($y, $v) = &_damage(shift, rand(100)+50, '魔', 1); return if !$y; &_heal($m, $v, '魔');	}],
		[130,	40,		'フレア',		sub{ &_damage(shift, 260, '魔', 1);	}],
	);
}
sub skill_16 { # 白魔道士
	return (
		[5,		5,		'ケアル',		sub{ &_heal(shift, 60, '魔');	}],
		[10,	2,		'ライブラ',		sub{ my $y = shift; $y = $members[int(rand(@members))] if !defined($ms{$y}{name}); $com.="<br />$y $e2j{mhp}:$ms{$y}{hp}/$ms{$y}{mhp}, $e2j{mmp}:$ms{$y}{mp}/$ms{$y}{mmp}, $e2j{at}:$ms{$y}{mat}, $e2j{df}:$ms{$y}{mdf}, $e2j{ag}:$ms{$y}{mag}";	}],
		[15,	6,		'サイレス',		sub{ &_st_d(shift, '魔封', '魔', 90);	}],
		[30,	18,		'ケアルラ',		sub{ &_heal(shift, 180, '魔');			}],
		[60,	20,		'リレイズ',		sub{ my($y) = &_check_party(shift, '復活', '魔'); return if !$y; $ms{$y}{tmp}='復活'; $com.=qq|<span class="tmp">$yは天使の加護がついた！</span>|;	}],
		[80,	5,		'シェル',		sub{ my($y) = &_check_party(shift, '魔軽減', '魔'); return if !$y; $ms{$y}{tmp}='魔軽減'; $com.=qq|<span class="tmp">$yは魔法の光で守られた！</span>|;	}],
		[100,	40,		'レイズ',		sub{ my($y) = &_check_party(shift, '蘇生', '魔'); return if !$y || $ms{$y}{hp} > 0; $com.=qq|なんと、<span class="revive">$yが生き返りました！</span>|; $ms{$y}{hp}=int($ms{$y}{mhp}*0.25);	}],
		[140,	35,		'ホーリー',		sub{ &_damage(shift, 180, '魔', 1);	}],
	);
}
sub skill_17 { # 聖騎士
	return (
		[10,	0,		'かばう',			sub{ my($y) = &_check_party(shift, 'かばう', '攻'); return if !$y || $y eq $m; $ms{$m}{tmp} = 'かばい中'; $ms{$y}{tmp} = 'かばう'; $com.=qq|<span class="tmp">$mは$yをかばっている</span>|;	}],
		[20,	3,		'ホイミ',			sub{ &_heal(shift, 30, '魔');	}],
		[40,	6,		'マジックバリア',	sub{ return if &is_bad_state('魔'); for my $y (@partys) { return if $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '魔軽減'; $com.=qq|<span class="tmp">$yは魔法の光で守られた！</span>|; };	}],
		[60,	5,		'キアリク',			sub{ &_st_hs('麻痺', '魔');	}],
		[100,	1,		'メガザル',			sub{ $com.=qq|<span class="die">$mは自分の命をささげました！</span>|; for my $y (@partys) { next if $m eq $y; $com .= $ms{$y}{hp} > 0 ? qq|$yの$e2j{hp}が<span class="heal">全回復</span>した！| : qq|<span class="revive">$yが生き返った！</span>|; $ms{$y}{hp} = $ms{$y}{mhp}; }; &defeat($m); $ms{$m}{mp} = 1; 	}],
		[130,	20,		'グランドクロス',	sub{ &_damages($ms{$m}{df} * 1.5, '攻');	}],
		[160,	80,		'ザオリク',			sub{ my($y) = &_check_party(shift, '蘇生', '魔'); return if !$y || $ms{$y}{hp} > 0; $com.=qq|なんと、<span class="revive">$yが生き返りました！</span>|; $ms{$y}{hp}=$ms{$y}{mhp};	}],
	);
}
sub skill_18 { # 天使
	return (
		[5,		2,		'キアリー',			sub{ &_st_h(shift, '猛毒', '魔');	}],
		[15,	6,		'おどりふうじ',		sub{ &_st_ds('踊封', '踊', 70);	}],
		[30,	5,		'めざめのうた',		sub{ &_st_hs('眠り', '歌');	}],
		[50,	5,		'マホカンタ',		sub{ my($y) = &_check_party(shift, '魔反撃', '魔'); return if !$y; $ms{$y}{tmp} = '魔反撃'; $com.=qq|<span class="tmp">$yは魔法の壁で守られた！</span>|;	}],
		[70,	27,		'てんしのうたごえ',	sub{ for my $y (@partys) { next if $ms{$y}{hp} > 0; if (rand(2) < 1) { $com.=qq|なんと、<b>$y</b>が <span class="heal">生き返り</span> ました！|; $ms{$y}{hp}=int($ms{$y}{mhp} * 0.5); } else { $com.=qq|しかし、<b>$y</b>は生き返らなかった…|; }; }; 	}],
		[90,	25,		'ベホマラー',		sub{ &_heals(120, '魔');	}],
		[120,	80,		'ザオリク',			sub{ my($y) = &_check_party(shift, '蘇生', '魔'); return if !$y || $ms{$y}{hp} > 0; $com.=qq|なんと、<span class="revive">$yが生き返りました！</span>|; $ms{$y}{hp}=$ms{$y}{mhp};	}],
	);
}
sub skill_19 { # 闇魔道士
	return (
		[4,		7,		'ルカナン',		sub{ &_st_downs(0.25, '魔', 'df');	}],
		[8,		5,		'マホカンタ',	sub{ my($y) = &_check_party(shift, '魔反撃', '魔'); return if !$y; $ms{$y}{tmp} = '魔反撃'; $com.=qq|<span class="tmp">$yは魔法の壁で守られた！</span>|;	}],
		[16,	10,		'メダパニ',		sub{ &_st_ds('混乱', '魔', 50);	}],
		[25,	14,		'ザキ',			sub{ &_death(shift, '即死', '魔', 20);	}],
		[40,	10,		'マホトーン',	sub{ &_st_ds('魔封', '魔', 70);	}],
		[60,	18,		'ベギラゴン',	sub{ &_damages(125, '魔', 1);	}],
		[70,	2,		'マホトラ',		sub{ my($y, $v) = &_st_down(shift, 0.25, '魔', 'mp'); return if !$y; &_mp_h($m, $v, '魔');	}],
		[110,	32,		'ザラキ',		sub{ &_deaths('即死', '魔', 20);	}],
	);
}
sub skill_20 { # 悪魔
	return (
		[4,		4,		'さそうおどり',			sub{ &_st_d(shift, '動封', '踊', 85);	}],
		[9,		6,		'レディウィップ',		sub{ my($y, $v) = &_damage(shift, $ms{$m}{at}*0.9, '攻'); return if !$y; $v = int($v * 0.1); &_mp_h($m, $v, '攻');		}],
		[16,	6,		'マジックバリア',		sub{ for my $y (@partys) { return if $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '魔軽減'; $com.=qq|<span class="tmp">$yは魔法の光で守られた！</span>|; };	}],
		[20,	9,		'あまいいき',			sub{ &_st_ds('眠り', '息', 35);	}],
		[36,	7,		'メダパニダンス',		sub{ &_st_ds('混乱', '踊', 60);	}],
		[60,	24,		'しのおどり',			sub{ &_deaths('即死', '踊', 17);	}],
		[100,	18,		'クィーンウィップ',		sub{ my($y, $v) = &_damage(shift, $ms{$m}{at}*1.7, '攻'); return if !$y; $v = int($v * 0.5); &_heal($m, $v, '攻');		}],
	);
}
sub skill_21 { # ﾊﾞｰｻｰｶｰ
	return (
		[10,	4,		'たいあたり',	sub{ my($y, $v) = &_damage(shift, $ms{$m}{df}*1.6, '攻'); return if $v <= 0; &_risk($v * 0.07);			}],
		[20,	5,		'うけながし',	sub{ $ms{$m}{tmp} = '受流し'; $com.=qq|<span class="tmp">$m は攻撃を受流すかまえをとった</span>|;	}],
		[40,	12,		'おたけび',		sub{ &_st_ds('動封', '攻', 60);		}],
		[60,	5,		'すてみ',		sub{ $com.=qq|<span class="tmp">$mは守りを気にせずすてみで攻撃！</span>|; &_damage(shift, $ms{$m}{at}*2, '攻'); $ms{$m}{tmp}='２倍';	}],
		[80,	6,		'もろはぎり',	sub{ my($y, $v) = &_damage(shift, $ms{$m}{at}*1.6, '攻'); return if $v <= 0; &_risk($v * 0.05);		}],
		[110,	9,		'みなごろし',	sub{ my $y= rand(4)<1 ? $partys[int rand @partys] : $enemys[int rand @enemys]; $y=$m if $ms{$y}{hp} <= 0; my $v = int( ($ms{$m}{at} * 3.0 - $ms{$y}{df} * 0.4) * ((rand(0.3)+0.9) * $ms{$m}{ten}) ); $v = int(rand(2)+1) if $v < 1; $ms{$m}{ten}=1; $ms{$y}{hp}-=$v; $ms{$y}{hp}=0 if $ms{$y}{hp}<0; $com.=qq|<b>$y</b>に <span class="damage">$v</span> のダメージ！|; if ($ms{$y}{hp} <= 0) { $ms{$y}{hp} = 0; $com .= qq!<span class="die">$yを倒した！</span>!; &defeat($y); }	}],
	);
}
sub skill_22 { # 暗黒騎士
	return (
		[10,	5,		'あんこく',			sub{ my($y, $v) = &_damage(shift, $ms{$m}{at}*1.5, '攻'); return if $v <= 0; $ms{$m}{hp} > 999 ? &_risk($v * 0.1) : &_risk($ms{$m}{hp} * 0.1);		}],
		[20,	9,		'めいやく',			sub{ my $v = int($ms{$m}{df} * 0.5); $ms{$m}{df} -= $v; $com.=qq|$mの<span class="st_down">$e2j{df}が $v さがりました！</span>|; &_st_up($m, 1.0, '無', 'at');	}],
		[40,	16,		'ナイトメア',		sub{ &_st_ds('混乱', '魔', 50);	}],
		[70,	10,		'ダークブレイク',	sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at}*1.2, '攻'); return if !$y || $ms{$y}{hp} <= 0; &_st_down($y, 0.1, '攻', 'hit');	}],
		[140,	40,		'あんこくけん',		sub{ my($y, $v) = &_damage(shift, $ms{$m}{at}*2.5, '攻'); return if $v <= 0; $ms{$m}{hp} > 999 ? &_risk($v * 0.2) : &_risk($ms{$m}{hp} * 0.2);		}],
	);
}
sub skill_23 { # 竜騎士
	return (
		[10,	5,		'ジャンプ',			sub{ &_damage(shift, $ms{$m}{ag}*1.8, '攻');	}],
		[30,	25,		'ドラゴンパワー',	sub{ &_st_up($m, 0.4, '攻', 'at'); &_st_up($m, 0.4, '攻', 'df');	}],
		[50,	18,		'りゅうけん',		sub{ my($y, $v) = &_damage(shift, $ms{$m}{at}*0.9, '攻'); return if !$y; &_heal($m, $v, '攻');	}],
		[70,	14,		'ハイジャンプ',		sub{ for my $i (1..2) { last if $ms{$m}{hp} <= 0; &_damage(shift, $ms{$m}{ag} * 2.2, '攻'); };	}],
		[130,	35,		'グングニル',		sub{ &_damage(shift, $ms{$m}{at}*1.4, '攻', 1);	}],
	);
}
sub skill_24 { # 魔剣士
	return (
		[10,	6,		'かえんぎり',		sub{ &_damage(shift, $ms{$m}{at}*1.2, '攻');	}],
		[30,	6,		'メタルぎり',		sub{ &_damage(shift, $ms{$m}{at}*0.4, '無', 1);	}],
		[50,	16,		'バイキルト',		sub{ &_st_up(shift, 1.0, '魔', 'at');	}],
		[70,	14,		'いなずまぎり',		sub{ &_damage(shift, $ms{$m}{at}*1.5, '攻');	}],
		[130,	25,		'ギガスラッシュ',	sub{ &_damage(shift, 230, '攻', 1);	}],
	);
}
sub skill_25 { # ﾓﾝｸ
	return (
		[5,		8,		'まわしげり',		sub{ &_damages($ms{$m}{at}*0.8, '攻');			}],
		[15,	3,		'チャクラ',			sub{ &_heal($m, 100, '攻'); $ms{$m}{hit} = 95;	}],
		[30,	15,		'すてみ',			sub{ $com.=qq|<span class="st_down">$mは守りを気にせずすてみで攻撃！</span>|; &_damage(shift, $ms{$m}{at}*2, '攻'); $ms{$m}{tmp}='２倍';		}],
		[50,	5,		'カウンター',		sub{ $ms{$m}{tmp}='攻反撃'; $com.=qq|<span class="tmp">$mは反撃のかまえをとった！</span>|;	}],
		[70,	3,		'だいぼうぎょ',		sub{ $ms{$m}{tmp}='大防御'; $com.=qq|<span class="tmp">$mは守りのかまえをとった！</span>|;	}],
		[90,	12,		'しんくうは',		sub{ &_damages(120, '攻', 1);	}],
		[110,	0,		'におうだち',		sub{ $ms{$m}{tmp} = 'かばい中'; for my $y (@partys) { next if $m eq $y; $ms{$y}{tmp} = 'かばう'; }; $com.=qq|<span class="tmp">$mは仲間の前に立ちはだかった！</span>|;	}],
		[130,	7,		'きしかいせい',		sub{ $ms{$m}{tmp} = '復活'; $com.=qq|<span class="tmp">$mは死ぬ気のオーラにつつまれた！</span>|;	}],
	);
}
sub skill_26 { # 忍者
	return (
		[5,		5,		'かえんのいき',		sub{ &_damages(50, '息', 1);	}],
		[15,	10,		'やけつくいき',		sub{ &_st_ds('麻痺', '息', 35);		}],
		[30,	7,		'マヌーサ',			sub{ &_st_downs(0.2, '魔', 'hit');			}],
		[40,	7,		'もうどくのきり',	sub{ &_st_ds('猛毒', '息', 60);		}],
		[50,	6,		'ピオリム',			sub{ &_st_ups(0.25, '魔', 'ag');	}],
		[65,	11,		'きゅうしょづき',	sub{ &_death(shift, '即死', '攻', 19);	}],
		[80,	10,		'しのびあし',		sub{ &_st_up($m, 1.0, '無', 'ag');	}],
		[110,	15,		'アーマーブレイク',	sub{ my($y) = &_check_enemy(shift, '破壊', '攻'); return if !$y; $ms{$y}{tmp}=''; $ms{$y}{ten}=1; $ms{$y}{df}=$ms{$y}{mdf}; $com.="$yの防具の強さを封じた！"; &_st_down($y, 0.1, '攻', 'df');	}],
	);
}
sub skill_27 { # 風水士
	return (
		[5,		6,		'すなけむり',		sub{ &_st_downs(0.2, '息', 'hit');	}],
		[15,	5,		'かまいたち',		sub{ &_damage(shift, 80, '無', 1);	}],
		[25,	6,		'ボミオス',			sub{ &_st_downs(0.3, '魔', 'ag');	}],
		[40,	11,		'ヒャダルコ',		sub{ &_damages(80, '魔', 1);	}],
		[55,	4,		'ザメハ',			sub{ &_st_hs('眠り', '魔');	}],
		[70,	5,		'おいかぜ',			sub{ for my $y (@partys) { next if $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '息反撃'; $com.=qq|<span class="tmp">$yの周りに追い風が吹いている！</span>|;};	}],
		[90,	27,		'マヒャド',			sub{ &_damages(160, '魔', 1);	}],
		[110,	15,		'ウェポンブレイク',	sub{ my($y) = &_check_enemy(shift, '破壊', '攻'); return if !$y; $ms{$y}{tmp}=''; $ms{$y}{ten}=1; $ms{$y}{at}=$ms{$y}{mat}; $com.="$yの武器の強さを封じた！"; &_st_down($y, 0.2, '攻', 'at');	}],
	);
}
sub skill_28 { # 侍
	return (
		[5,		0,		'せいしんとういつ',	sub{ $ms{$m}{hit}=95; $com.=qq|$mは心を落ちつかせ<span class="st_up">命中率が回復した</span>|;	}],
		[15,	3,		'みねうち',			sub{ &_st_d(shift, '動封', '攻', 80);	}],
		[30,	5,		'うけながし',		sub{ $ms{$m}{tmp} = '受流し'; $com.=qq|<span class="tmp">$mは攻撃を受流すかまえをとった</span>|;	}],
		[50,	0,		'ぜになげ',			sub{ if ($m{money} < 100) { $m{money} = 0; &_damages(50, '攻', 1); } else { $m{money} -= 100; &_damages(180, '攻', 1); }; 	}],
		[70,	4,		'しらはどり',		sub{ $ms{$m}{tmp}='攻無効'; $com.=qq|<span class="tmp">$mは守りのかまえをとった！</span>|;	}],
		[100,	20,		'いあいぎり',		sub{ &_st_ds('動封', '攻', 65);	}],
		[140,	10,		'ざんてつけん',		sub{ &_death(shift, '即死', '攻', 25);	}],
	);
}
sub skill_29 { # 時魔道士
	return (
		[10,	4,		'スロウ',		sub{ &_st_down(shift,  0.45, '魔', 'ag');	}],
		[20,	4,		'ヘイスト',		sub{ &_st_up(shift, 0.45, '魔', 'ag');	}],
		[30,	14,		'コメット',		sub{ my $v = int(rand(2)+2); for my $i (1..$v) { last if $ms{$m}{hp} <= 0; &_damage(undef, 50, '魔', 1); };	}],
		[50,	9,		'スロウガ',		sub{ &_st_downs(0.35, '魔', 'ag');	}],
		[70,	9,		'ヘイスガ',		sub{ &_st_ups(0.35, '魔', 'ag');	}],
		[110,	30,		'グラビデ',		sub{ &_st_down(shift, 0.5, '魔', 'hp');	}],
		[150,	50,		'メテオ',		sub{ my $v = int(rand(3)+4); for my $i (1..$v) { last if $ms{$m}{hp} <= 0; &_damage(undef, 99, '魔', 1); };	}],
	);
}
sub skill_30 { # 赤魔道士
	return (
		[10,	5,		'ケアル',			sub{ &_heal(shift, 60, '魔');	}],
		[20,	5,		'ファイア',			sub{ &_damage(shift, 35, '魔', 1);	}],
		[40,	5,		'シェル',			sub{ my($y) = &_check_party(shift, '魔軽減', '魔'); return if !$y || $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '魔軽減'; $com.=qq|<span class="tmp">$yは魔法の光で守られた！</span>|;	}],
		[60,	11,		'ファイラ',			sub{ &_damage(shift, 80, '魔', 1);	}],
		[80,	7,		'リフレク',			sub{ my($y) = &_check_party(shift, '魔反撃', '魔'); return if !$y; $ms{$y}{tmp} = '魔反撃'; $com.=qq|<span class="tmp">$yは魔法の壁で守られた！</span>|;	}],
		[100,	18,		'ケアルラ',			sub{ &_heal(shift, 180, '魔');			}],
		[120,	20,		'リレイズ',			sub{ my($y) = &_check_party(shift, '復活', '魔'); return if !$y; $ms{$y}{tmp}='復活'; $com.=qq|<span class="tmp">$yは天使の加護がついた！</span>|;	}],
		[150,	40,		'れんぞくまほう',	sub{ for my $i (1..2) { last if $ms{$m}{hp} <= 0; &_damage(undef, 180, '魔', 1); };	}],
	);
}
sub skill_31 { # 青魔道士
	return (
		[11,	11,		'じばく',				sub{ $com.=qq|<span class="die">$mは自爆した！</span>|; &_damage(shift, $ms{$m}{hp}, '魔', 1); &defeat($m);	}],
		[44,	4,		'しのルーレット',		sub{ return if &is_bad_state('魔'); my $y=$members[int(rand(@members))]; $y = $m if $ms{$y}{hp} <= 0; $com.="死のルーレットが廻りだした！…ﾋﾟｯ…ﾋﾟｯ…ﾋﾟｯﾋﾟｯﾋﾟ-[>[$y]"; if ($ms{$y}{hp} > 999 || $ms{$y}{df} > 999) { $com .= "$yにはきかなかった…"; } else { $com .= qq|<span class="die">$yは死んでしまった！</span>|; &defeat($y); };		}],
		[66,	18,		'？？？？',				sub{ &_damage(shift, $ms{$m}{mhp}-$ms{$m}{hp}+5, '魔', 1);		}],
		[77,	34,		'マイティガード',		sub{ &_st_ups(0.5, '魔', 'df'); for my $y (@partys) { next if $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '魔軽減'; $com.=qq|<span class="tmp">$yは魔法の光で守られた！</span>|;};	}],
		[94,	24,		'ＭＰ４グラビガ',		sub{ return if &is_bad_state('魔'); for my $y (@members) { next unless $ms{$y}{mp}; next if $ms{$y}{hp} <= 0; next if $ms{$y}{mp} % 4 != 0; next if $ms{$y}{hp} > 999; $ms{$y}{hp} = int($ms{$y}{hp}*0.25); $ms{$y}{hp} = 1 if $ms{$y}{hp} <= 0; $com.=qq|$yは<span class="st_down">$e2j{mhp}が1/4になった！</span>|; };	}],
		[121,	36,		'ホワイトウィンド',		sub{ &_heals($ms{$m}{hp}, '魔');	}],
		[155,	25,		'ＭＰ５デス',			sub{ return if &is_bad_state('魔'); for my $y (@members) { next unless $ms{$y}{mp}; next if $ms{$y}{hp} <= 0; next if $ms{$y}{mp} % 5 != 0; next if $ms{$y}{hp} > 999; $ms{$y}{hp} = 0; $com.=qq|<span class="die">$yは死んでしまった！</span>|; };	}],
	);
}
sub skill_32 { # 召喚士
	return (
		[5,		5,		'チョコボ',			sub{ if (rand(4)<1) { $com.="＠デブチョコボ＠"; &_damage(shift, 100, '魔', 1); } else { $com.="＠チョコボキック＠"; &_damage(shift, 30, '魔', 1); };	}],
		[25,	10,		'シルフ',			sub{ $com.="＠癒しの風＠"; &_heals(50, '魔');		}],
		[50,	20,		'ゴーレム',			sub{ return if &is_bad_state('魔'); $com.="＠守りの壁＠";   for my $y (@partys) { next if $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '攻軽減'; $com.=qq|<span class="tmp">$yはゴーレムに守られている！</span>|;};	}],
		[70,	30,		'カーバンクル',		sub{ return if &is_bad_state('魔'); $com.="＠ルビーの光＠"; for my $y (@partys) { next if $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '魔反撃'; $com.=qq|<span class="tmp">$yは魔法の壁に守られた！</span>|;};	}],
		[100,	40,		'フェニックス',		sub{ return if &is_bad_state('魔'); $com.="＠転生の炎＠";   for my $y (@partys) { next if $ms{$y}{hp}  > 0; $ms{$y}{hp}=int($ms{$y}{mhp}*0.15); $com.=qq|<span class="revive">$yが生き返った！</span>|; };	}],
		[150,	50,		'バハムート',		sub{ $com.="＠メガフレア＠"; &_damages(220, '魔', 1);	}],
	);
}
sub skill_33 { # 賢者
	return (
		[5,		6,		'マジックバリア',	sub{ return if &is_bad_state('魔'); for my $y (@partys) { return if $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '魔軽減'; $com.=qq|<span class="tmp">$yは魔法の光で守られた！</span>|; };	}],
		[15,	12,		'イオラ',			sub{ &_damages(70, '魔', 1);	}],
		[30,	7,		'フバーハ',			sub{ return if &is_bad_state('魔'); for my $y (@partys) { next if $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '息軽減'; $com.=qq|<span class="tmp">$yは不思議な風に包まれた！</span>|;};	}],
		[70,	25,		'ベホマラー',		sub{ &_heals(120, '魔');	}],
		[100,	16,		'バイキルト',		sub{ &_st_up(shift, 1.0, '魔', 'at')	}],
		[130,	34,		'イオナズン',		sub{ &_damages(160, '魔', 1);	}],
		[160,	80,		'ザオリク',			sub{ my($y) = &_check_party(shift, '蘇生', '魔'); return if !$y || $ms{$y}{hp} > 0; $com.=qq|なんと、<span class="revive">$yが生き返りました！</span>|; $ms{$y}{hp}=$ms{$y}{mhp};	}],
	);
}
sub skill_34 { # 勇者
	return (
		[10,	0,		'かばう',			sub{ my($y) = &_check_party(shift, 'かばう', '攻'); return if !$y || $y eq $m; $ms{$m}{tmp} = 'かばい中'; $ms{$y}{tmp} = 'かばう'; $com.=qq|<span class="tmp">$mは$yをかばっている</span>|;	}],
		[30,	15,		'ライデイン',		sub{ &_damage(shift, 110, '魔', 1);			}],
		[60,	25,		'めいそう',			sub{ &_heal($m, 300, '無');		}],
		[90,	40,		'ギガデイン',		sub{ &_damages(180, '魔', 1);			}],
		[120,	6,		'アストロン',		sub{ return if &is_bad_state('魔'); $ms{$m}{tmp}='魔無効'; $com.=qq|<span class="tmp">$mは魔法をうけつけない体になった！</span>|;	}],
		[150,	80,		'ベホマズン',		sub{ &_heals(999, '魔');	}],
		[180,	30,		'ミナデイン',		sub{ my($y) = &_check_enemy(shift, '皆', '魔'); return if !$y; my $d = 100; for my $name (@partys) { next if $m eq $name || $ms{$name}{mp} < 15; $ms{$name}{mp}-=15; $d += 85; }; $com.=qq|$mは仲間のみんなから力を受けとった！| if $d > 100; &_damage($y, $d, '魔', 1);	}],
	);
}
sub skill_35 { # 魔王
	return (
		[10,	4,		'うけながし',		sub{ $ms{$m}{tmp} = '受流し'; $com.=qq|<span class="tmp">$m は攻撃を受流すかまえをとった</span>|;	}],
		[30,	30,		'いてつくはどう',	sub{ for my $y (@members) { my $tten=$ms{$y}{ten}; &reset_status($y); $ms{$y}{ten}=$tten; }; $com.=qq|<span class="st_down">全ての効果がかき消された！</span>|;	}],
		[60,	14,		'ザキ',				sub{ &_death(shift, '即死', '魔', 20);	}],
		[90,	40,		'しゃくねつ',		sub{ &_damages(180, '息', 1);	}],
		[120,	25,		'めいそう',			sub{ &_heal($m, 300, '無');	}],
		[150,	6,		'アストロン',		sub{ return if &is_bad_state('魔'); $ms{$m}{tmp}='魔無効'; $com.=qq|<span class="tmp">$mは魔法をうけつけない体になった！</span>|;	}],
		[180,	70,		'ジゴスパーク',		sub{ $is_add_effect = 1; &_damages(150, '魔', 1); &_st_ds('麻痺', '魔', 20);		}],
	);
}
sub skill_36 { # ものまね士
	return (
		[10,	5,		'おどるものまね',	sub{ $ms{$m}{tmp} = '踊反撃'; $com.=qq|<span class="tmp">$mは踊るまねをはじめた！</span>|;			}],
		[20,	5,		'ぶれすものまね',	sub{ $ms{$m}{tmp} = '息反撃'; $com.=qq|<span class="tmp">$mは息を吐くまねをはじめた！</span>|;		}],
		[40,	5,		'まほうものまね',	sub{ $ms{$m}{tmp} = '魔反撃'; $com.=qq|<span class="tmp">$mは魔法を唱えるまねをはじめた！</span>|;	}],
		[60,	5,		'こうげきものまね',	sub{ $ms{$m}{tmp} = '攻反撃'; $com.=qq|<span class="tmp">$mは攻撃するまねをはじめた！</span>|;		}],
		[100,	50,		'モシャス',			sub{ my $y = shift; return if &is_bad_state('魔'); $y = $members[int(rand(@members))] if !defined($ms{$y}{name}); return if $ms{$y}{hp} <= 0 || $ms{$y}{mhp} > 999 || $ms{$y}{mdf} > 999; for my $k (qw/hp mp at df ag/) { $ms{$m}{$k}=$ms{$y}{$k}; $ms{$m}{'m'.$k}=$ms{$y}{'m'.$k}; }; for my $k (qw/job sp old_job old_sp icon/) { $ms{$m}{$k}=$ms{$y}{$k}; }; $ms{$m}{mp} = 50 if $ms{$m}{mp} < 50; $com.=qq|<span class="st_up">$mは$yに姿を変えました！</span>|;	}],
	);
}
sub skill_37 { # 結界士
	return (
		[5,		10,		'マホトーン',		sub{ &_st_ds('魔封', '魔', 70);	}],
		[10,	1,		'マホキテ',			sub{ return if &is_bad_state('魔'); $ms{$m}{tmp} = '魔吸収'; $com.=qq|<span class="tmp">$mは不思議な光に包まれた！</span>|;	}],
		[15,	6,		'おどりふうじ',		sub{ &_st_ds('踊封', '踊', 70);	}],
		[25,	6,		'マジックバリア',	sub{ for my $y (@partys) { return if $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '魔軽減'; $com.=qq|<span class="tmp">$yは魔法の光で守られた！</span>|; };	}],
		[40,	5,		'マホカンタ',		sub{ my($y) = &_check_party(shift, '魔反撃', '魔'); return if !$y; $ms{$y}{tmp} = '魔反撃'; $com.=qq|<span class="tmp">$yは魔法の壁で守られた！</span>|;	}],
		[60,	7,		'じゅばく',			sub{ &_st_d(shift, '攻封', '無', 80);	}],
		[80,	25,		'めいそう',			sub{ &_heal($m, 300, '無');	}],
		[100,	15,		'ふういん',			sub{ my($y) = &_check_enemy(shift, '破壊', '攻'); return if !$y; $ms{$y}{tmp}=''; $ms{$y}{ten}=1; $ms{$y}{df}=$ms{$y}{mdf}; $ms{$y}{at}=$ms{$y}{mat}; $com.="$yの武器と防具の強さを封印した！";		}],
	);
}
sub skill_38 { # ﾊﾞﾝﾊﾟｲｱ
	return (
		[10,	12,		'きゅうけつ',		sub{ my($y, $v) = &_damage(shift, ($ms{$m}{mhp}-$ms{$m}{hp})*0.5+5, '魔', 1); return if !$y; &_heal($m, $v, '魔');	}],
		[20,	3,		'アスピル',			sub{ my($y, $v) = &_st_down(shift, 0.2, '魔', 'mp'); return if !$y; &_mp_h($m, $v, '魔');	}],
		[30,	6,		'アストロン',		sub{ return if &is_bad_state('魔'); $ms{$m}{tmp}='魔無効'; $com.=qq|<span class="tmp">$mは魔法をうけつけない体になった！</span>|;	}],
		[60,	9,		'めいやく',			sub{ my $v = int($ms{$m}{df} * 0.5); $ms{$m}{df} -= $v; $com.=qq|<span class="st_down">$mの$e2j{df}が $v さがりました！</span>|; &_st_up($m, 1.0, '無', 'at');	}],
		[90,	9,		'あまいいき',		sub{ &_st_ds('眠り', '息', 35);		}],
		[130,	37,		'ギガドレイン',		sub{ my($y) = &_check_enemy(shift, '吸収', '魔'); return if !$y; my $v = int($ms{$y}{hp}*0.5); $v = 300 if $v > 300; ($y) = &_damage($y, $v, '魔', 1); return if !$y; &_heal($m, $v, '魔');	}],
	);
}
sub skill_39 { # ｽﾗｲﾑ
	return (
		[3,		5,		'ギラ',			sub{ &_damages(25, '魔', 1);	}],
		[7,		7,		'スクルト',		sub{ &_st_ups(0.25, '魔', 'df');	}],
		[11,	3,		'ホイミ',		sub{ &_heal(shift, 30, '魔');	}],
		[16,	7,		'ルカナン',		sub{ &_st_downs(0.25, '魔', 'df')	}],
		[28,	10,		'メダパニ',		sub{ &_st_ds('混乱', '魔', 50);	}],
		[50,	20,		'ザオラル',		sub{ my($y) = &_check_party(shift, '蘇生', '魔'); return if !$y || $ms{$y}{hp} > 0; if (rand(2) < 1) { $com.=qq|なんと、<span class="revive">$yが生き返りました！</span>|; $ms{$y}{hp}=int($ms{$y}{mhp} * 0.5); } else { $com.=qq|しかし、$yは生き返らなかった…|; };	}],
		[99,	40,		'しゃくねつ',	sub{ &_damages(180, '息', 1);	}],
	);
}
sub skill_40 { # ﾊｸﾞﾚﾒﾀﾙ
	return (
		[25,	8,		'メラミ',		sub{ &_damage(shift, 70, '魔', 1);		}],
		[50,	11,		'ベギラマ',		sub{ &_damages(60, '魔', 1);			}],
		[99,	1,		'マダンテ',		sub{ &_damages($ms{$m}{mp} * 2, '魔', 1); $ms{$m}{mp} = 1; 	}],
	);
}
sub skill_41 { # ﾄﾞﾗｺﾞﾝ
	return (
		[10,	1,		'つめたいいき',		sub{ &_damages(15, '息', 1);	}],
		[30,	6,		'こおりのいき',		sub{ &_damages(55, '息', 1);	}],
		[60,	14,		'こごえるふぶき',	sub{ &_damages(115, '息', 1);	}],
		[90,	9,		'やけつくいき',		sub{ &_st_ds('麻痺', '息', 35);	}],
		[120,	34,		'かがやくいき',		sub{ &_damages(195, '息', 1);	}],
	);
}
sub skill_42 { # ｱｻｼﾝ
	return (
		[15,	7,		'コンフュ',			sub{ &_st_d(shift, '混乱', '魔', 80);	}],
		[30,	6,		'サイレス',			sub{ &_st_d(shift, '魔封', '魔', 90);	}],
		[55,	10,		'しのびあし',		sub{ &_st_up($m, 1.0, '無', 'ag');	}],
		[80,	4,		'どくこうげき',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at} * 1.1, '攻'); return if !$y || $ms{$y}{hp} <= 0;  &_st_d($y, '猛毒', '攻', 70);	}],
		[100,	8,		'まひこうげき',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at} * 1.2, '攻'); return if !$y || $ms{$y}{hp} <= 0;  &_st_d($y, '麻痺', '攻', 35);	}],
		[120,	42,		'しのせんこく',		sub{ my($y) = &_check_enemy(shift, '瀕死', '魔'); return if !$y; if ($ms{$y}{mhp}>999 || $ms{$y}{mdf}>999) { $com.="$yにはきかなかった！"; } elsif (rand(1.5)<1) { &_st_down($y, 0.75, '魔', 'hp'); $ms{$y}{state}='猛毒'; } else { $com.="$yはかわした！"; };	}],
		[150,	24,		'あんさつけん',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at} * 1.7, '攻'); return if !$y || $ms{$y}{hp} <= 0; &_death($y, '即死', '攻', 25);	}],
	);
}
sub skill_43 { # 医術士
	return (
		[5,		2,		'どくちりょう',		sub{ &_st_hs('猛毒', '無');	}],
		[10,	3,		'まひちりょう',		sub{ &_st_hs('麻痺', '無');	}],
		[20,	5,		'めざめのうた',		sub{ &_st_hs('眠り', '歌');	}],
		[40,	7,		'リジェネ',			sub{ my($y) = &_check_party(shift, '回復', '魔'); return if !$y; $ms{$y}{tmp} = '回復'; $com.=qq|<span class="tmp">$yは優しい光に包まれた！</span>|;	}],
		[70,	10,		'エスナ',			sub{ my($y) = &_check_party(shift, '治療', '無'); return if !$y; &_st_h($y, $ms{$y}{state}, '魔');	}],
		[110,	35,		'ケアルガ',			sub{ &_heal(shift, 400, '魔');			}],
		[150,	70,		'アレイズ',			sub{ my($y) = &_check_party(shift, '蘇生', '魔'); return if !$y || $ms{$y}{hp} > 0; $com.=qq|なんと、<span class="revive">$yが生き返りました！</span>|; $ms{$y}{hp}=$ms{$y}{mhp};	}],
	);
}
sub skill_44 { # ﾁｮｺﾎﾞ
	return (
		[20,	4,		'チョコボキック',	sub{ &_damage(shift, $ms{$m}{at} * 1.4, '攻');	}],
		[40,	5,		'チョコガード',		sub{ &_st_up($m, 0.5, '無', 'df');	}],
		[60,	8,		'チョコアタック',	sub{ my($y, $v) = &_damage(shift, $ms{$m}{df} * 2.0, '攻'); return if $v <= 0; &_risk($v * 0.07);	}],
		[80,	14,		'チョコボール',		sub{ &_damage(shift, 170, '魔', 1);	}],
		[100,	7,		'チョコケアル',		sub{ &_heal(shift, 150, '魔');	}],
		[120,	15,		'チョコボックル',	sub{ &_damage(shift, $ms{$m}{ag} * 1.8, '魔', 1);		}],
	);
}
sub skill_45 { # ﾓｰｸﾞﾘ
	return (
		[10,	5,		'おまじない',		sub{ my($y) = &_check_party(shift, '命中', '無'); return if !$y; $ms{$y}{hit}=95; $com.=qq|<span class="st_up">$yの命中率が回復した</span>|;		}],
		[30,	8,		'ストップ',			sub{ &_st_d(shift, '動封', '魔', 85);	}],
		[50,	7,		'ウールガード',		sub{ &_st_up($m, 0.5, '無', 'df'); $ms{$m}{tmp} = '魔軽減'; $com.=qq|<span class="tmp">$mは魔法の光で守られた！</span>|;	}],
		[70,	3,		'マホトラおどり',	sub{ my($y, $v) = &_st_down(shift, 0.18, '踊', 'mp'); return if !$y; &_mp_h($m, $v, '踊');	}],
		[90,	30,		'カエルのうた',		sub{ my($y, $v) = &_st_down(shift, 0.4, '歌', 'at'); return if !$y; &_st_down($y, 0.4, '歌', 'df'); $ms{$y}{icon} = "chr/022.gif"; $com .= "$yはカエルの姿になった！";	}],
		[120,	7,		'リジェネ',			sub{ my($y) = &_check_party(shift, '回復', '魔'); return if !$y; $ms{$y}{tmp} = '回復'; $com.=qq|<span class="tmp">$yは優しい光に包まれた！</span>|;	}],
		[150,	40,		'アルテマチャージ',	sub{ &_damage(shift, 300, '攻', 1);		}],
	);
}
sub skill_46 { # ｷﾞｬﾝﾌﾞﾗｰ
	return (
		[10,	7,		'ヘブンスロット',		sub{ my @m = ('∞','♪','†','★','７'); my @s = (); $s[$_] = int(rand(@m)) for (0 .. 2); $com .= "【$m[$s[0]]】【$m[$s[1]]】【$m[$s[2]]】"; if ($s[0] == $s[1] && $s[1] == $s[2]) { my $v = int( ($s[0]+2) * 100 ); $s[0] == $#m ? &_deaths('即死', '無', 80) : $s[0] == 0 || $s[0] == 2 ? &_heals($v, '無') : &_damages($v, '無'); } else { my $v = int( ($s[0] + $s[1] + $s[2]) * 7 ); &_damages($v, '無', 1); };		}],
		[30,	14,		'いちげきのダーツ',		sub{ &_death(shift, '即死', '攻', 20);	}],
		[60,	6,		'あくまのダイス',		sub{ my $d1 = int(rand(6)+1); my $d2 = int(rand(6)+1); my $d3 = int(rand(6)+1); my $v = int(($d1*100+$d2*10+$d1)*0.5); $com.="[$d1][$d2][$d3]"; &_damage(shift, $v, '魔', 1); return if $v <= 0; &_risk((6-$d1)*10+(6-$d2)+(6-$d1)*0.1);		}],
		[80,	4,		'しのルーレット',		sub{ return if &is_bad_state('魔'); my $y=$members[int(rand(@members))]; $y = $m if $ms{$y}{hp} <= 0; $com.="死のルーレットが廻りだした！…ﾋﾟｯ…ﾋﾟｯ…ﾋﾟｯﾋﾟｯﾋﾟ-[>[$y] "; if ($ms{$y}{hp} > 999 || $ms{$y}{df} > 999) { $com .= "$yにはきかなかった…"; } else { $com .= qq|<span class="die">$yは死んでしまった！</span>|; &defeat($y); };	}],
		[140,	36,		'イカサマのダイス',		sub{ my $d1 = int(rand(3)+1); my $d2 = int(rand(6)+1); my $d3 = int(rand(6)+1); my $v = $d1*100+$d2*10+$d1; $com.="[$d1][$d2][$d3]"; &_damage(shift, $v, '魔', 1);	}],
	);
}
sub skill_47 { # ｿﾙｼﾞｬｰ
	return (
		[20,	5,		'ブレイバー',				sub{ &_damage(shift, $ms{$m}{at}*1.2, '攻');	}],
		[50,	9,		'きょうぎり',				sub{ my($y, $v) = &_damage(shift, $ms{$m}{at}*1.6, '攻'); return if $v <= 0; &_risk($v * 0.06);	}],
		[80,	20,		'メテオレイン',				sub{ my($y) = &_damage(shift, $ms{$m}{at}*1.8, '攻'); return if !$y; my $v = int($ms{$m}{at} * 0.1); $ms{$m}{at} -= $v; $com .= qq|$mの<span class="st_down">$e2j{at}が $v さがった！</span>|;		}],
		[120,	36,		'クライムハザード',			sub{ my($y) = &_check_enemy(shift, '半分', '攻'); return if !$y; my $v = $ms{$y}{mhp}-$ms{$y}{hp} + 10; $v = 400 if $v > 400; &_damage($y, $v, '攻', 1);	}],
		[160,	40,		'ちょうきゅうぶしんはざん',	sub{ for my $i (1..4) { last if $ms{$m}{hp} <= 0; &_damage(undef, $ms{$m}{at}, '攻'); };		}],
	);
}
sub skill_48 { # 堕天使
	return (
		[40,	56,		'バイオガ',				sub{ $is_add_effect = 1; &_damages(120, '魔', 1); &_st_ds('猛毒', '魔', 40);		}],
		[80,	66,		'やみのてんし',			sub{ $is_add_effect = 1; &_damages(70, '魔', 1);  &_st_ds('眠り', '魔', 30);		}],
		[120,	66,		'シャドウフレア',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, 300, '魔', 1); return if !$y || $ms{$y}{hp} <= 0; &_st_down($y, 0.08, '魔', 'hit');	}],
		[160,	44,		'こころないてんし',		sub{ my($y) = &_check_enemy(shift, '瀕死', '魔'); return if !$y; if ($ms{$y}{mhp}>999 || $ms{$y}{mdf}>999) { $com.="$yにはきかなかった！"; } elsif (rand(3)<1) { $ms{$y}{hp}=1; $com.=qq|$yは<span class="st_down">生命力を失った</span>！|; } else { $com.="$yはかわした！"; };	}],
		[200,	46,		'はっとういっせん',		sub{ &_damages($ms{$m}{at} * 1.2, '攻');		}],
	);
}

# ＠パーティーII追加分 
sub skill_49 { # たまねぎ剣士
	return (
		[100,	10,		'リボン',			sub{ my($y) = &_check_party(shift, '治療', '無'); return if !$y; &_st_h($y, $ms{$y}{state}, '無');	}],
		[200,	20,		'オニオンシールド',	sub{ &_st_up($m, 0.6, '攻', 'df'); $ms{$m}{tmp} = '攻軽減'; $com.=qq|<span class="tmp">$mは守りを固めた！</span>|;	 	}],
		[300,	30,		'オニオンソード',	sub{ &_damage(shift, $ms{$m}{at}*1.6, '攻');	}],
	);
}
sub skill_50 { # ｱｲﾃﾑ士
	return (
		[10,	5,		'ポーション',			sub{ &_heal(shift, 80, '魔');	}],
		[25,	3,		'キュアブラインド',		sub{ my($y) = &_check_party(shift, '命中', '魔'); return if !$y; $ms{$y}{hit}=95; $com.=qq|<span class="st_up">$yの命中率が回復した</span>|;	}],
		[40,	14,		'デスポーション',		sub{ &_death(shift, '即死', '魔', 17);	}],
		[55,	10,		'ドラゴンアーマー',		sub{ my($y) = &_st_up(shift, 0.4, '魔', 'df'); $ms{$y}{tmp} = '息軽減'; $com.=qq|<span class="tmp">$yは不思議な風に包まれた！</span>|;	}],
		[75,	24,		'ハイポーション',		sub{ &_heal(shift, 200, '魔');	}],
		[110,	50,		'エーテル',				sub{ &_mp_h(shift, 50, '魔');	}],
		[145,	1,		'ラストエリクサー',		sub{ my($y) = &_check_party(shift, '最後', '魔'); return if !$y || $m eq $y; $com.=qq|<span class="die">$mは自分の命をささげました！</span>|; $com .= $ms{$y}{hp} > 0 ? qq|$yの$e2j{hp}と$e2j{mp}が<span class="heal">全回復</span>した！| : qq|<span class="revive">$yが生き返った！</span>|; $ms{$y}{hp} = $ms{$y}{mhp}; $ms{$y}{mp} = $ms{$y}{mmp}; &defeat($m); $ms{$m}{mp} = 1;	}],
	);
}
sub skill_51 { # 光魔道士
	return (
		[10,	6,		'まぶしいひかり',		sub{ &_st_downs(0.2, '魔', 'hit');		}],
		[30,	11,		'ひかりのみちびき',		sub{ for my $y (@partys) { $ms{$y}{hit}=95; }; $com.=qq|<span class="st_up">$mたちの命中率が回復した</span>|;	}],
		[50,	14,		'いやしのひかり',		sub{ &_heals(int(rand(50)+50), '魔');	}],
		[80,	16,		'あやしいひかり',		sub{ my @randoms = ('混乱', '眠り'); for my $name (@enemys) { &_st_d($name, $randoms[int(rand(@randoms))], '魔', 50); };		}],
		[110,	34,		'ひかりのさばき',		sub{ &_damages(170, '魔', 1);	}],
		[130,	30,		'きぼうのひかり',		sub{ for my $y (@partys) { next if $ms{$y}{hp} > 0; if (rand(5) < 1) { $com.=qq|なんと、<b>$y</b>が <span class="heal">生き返り</span> ました！|; $ms{$y}{hp}=$ms{$y}{mhp}; } else { $com.=qq|しかし、<b>$y</b>は生き返らなかった…|; }; }; 	}],
		[160,	46,		'ぜつぼうのひかり',		sub{ $is_add_effect = 1; &_deaths('即死', '無', 10); &_damages(70, '魔', 1); 		}],
	);
}
sub skill_52 { # 魔人
	return (
		[20,	4,		'ひざげり',				sub{ &_damage(shift, $ms{$m}{at}*1.2, '攻');	}],
		[50,	8,		'ちからをためる',		sub{ &_st_up($m, 1.0, '攻', 'at');		}],
		[80,	15,		'アーマーブレイク',		sub{ my($y) = &_check_enemy(shift, '破壊', '攻');  return if !$y; $ms{$y}{tmp}=''; $ms{$y}{ten}=1; $ms{$y}{df}=$ms{$y}{mdf}; $com.="$yの防具の強さを封じた！"; &_st_down($y, 0.1, '攻', 'df');	}],
		[130,	20,		'きあいため',			sub{ $ms{$m}{tmp}='２倍'; &tenshon($m); &tenshon($m);	}],
		[150,	30,		'だいぼうそう',			sub{ &_damages(200, '攻', 1); $ms{$m}{tmp}='２倍';	}],
	);
}
sub skill_53 { # 蟲師
	return (
		[5,		3,		'くものいと',		sub{ &_st_d(shift, '動封', '息', 80);	}],
		[15,	4,		'どくのいと',		sub{ &_st_d(shift, '猛毒', '息', 80);	}],
		[30,	16,		'むしのいき',		sub{ my @randoms = ('猛毒', '麻痺', '眠り'); for my $name (@enemys) { &_st_d($name, $randoms[int(rand(@randoms))], '息', 60); };		}],
		[55,	15,		'あくまのわな',		sub{ my($y) = &_check_party(shift, '攻反撃', '息'); return if !$y; $ms{$y}{tmp} = '攻反撃'; $com.=qq|<span class="tmp">$yは特殊な糸で守られた！</span>|;	}],
		[80,	8,		'くものす',			sub{ &_st_d(shift, '攻封', '息', 80);	}],
		[120,	7,		'あやつりいと',		sub{ my($y) = &_check_enemy(shift, '操り', '息'); return if !$y; $com.="$mは$yをあやつった！$y: ＠こうげき "; $buf_m = $m; $m = $y; &kougeki(); $m = $buf_m;	}],
	);
}
sub skill_54 { # 魔銃士
	return (
		[5,		4,		'いかくしゃげき',	sub{ &_st_d(shift, '動封', '攻', 80);	}],
		[15,	7,		'そげき',			sub{ &_damage(shift, $ms{$m}{at}*0.6, '攻', 1);		}],
		[30,	0,		'たかのめ',			sub{ $ms{$m}{hit}=95; $com.=qq|$mは心を落ちつかせ<span class="st_up">命中率が回復した</span>|;	}],
		[60,	12,		'かんせつねらい',	sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at}*0.5, '攻', 1); return if !$y || $ms{$y}{hp} <= 0; &_st_d($y, '動封', '攻', 30);	}],
		[90,	34,		'クレイモア',		sub{ &_damages(180, '攻', 1);	}],
		[130,	44,		'みだれうち',		sub{ my $v = int(rand(2)+3); for my $i (1..$v) { last if $ms{$m}{hp} <= 0; &_damage(undef, $ms{$m}{at}*0.7, '攻', 1); };		}],
	);
}
sub skill_55 { # 妖精
	return (
		[5,		0,		'めかくし',			sub{ my $y=$members[int(rand(@members))]; $ms{$y}{hit} = int($ms{$y}{hit}*0.5); $com.=qq|$mは$yに目隠しをし<span class="st_down">$yの命中率がさがった！</span>|;	}],
		[10,	4,		'ようせいのや',		sub{ my($y, $v) = &_st_down(shift, 0.15, '攻', 'mp'); return if !$y; &_mp_h($m, $v, '攻');	}],
		[20,	0,		'くちをふさぐ',		sub{ my $y=$members[int(rand(@members))]; $ms{$y}{state}='魔封'; $ms{$y}{ten}=1; $com.=qq|$mは$yの口をふさぎ<span class="state">$yは魔封になりました！</span>|;		}],
		[35,	0,		'ちょうはつ',		sub{ for my $y (@members) { next if $ms{$y}{hp} <= 0 || $m eq $y || rand(2) < 1; &tenshon($y); };	}],
		[50,	8,		'でたらめや',		sub{ &_damages($ms{$m}{ag}*1.4, '攻');	}],
		[65,	0,		'からかう',			sub{ my $y = shift; ($y) = defined($ms{$y}{name}) ? $y : &_check_enemy($y, 'テン', '無'); &tenshon($y);		}],
		[80,	0,		'ゆびをふる',		sub{ &_yubiwofuru;	}],
	);
}
sub skill_56 { # ﾐﾆﾃﾞｰﾓﾝ
	return (
		[6,		5,		'イオ',				sub{ &_damages(25, '魔', 1);	}],
		[16,	1,		'マホキテ',			sub{ return if &is_bad_state('魔'); $ms{$m}{tmp} = '魔吸収'; $com.=qq|<span class="tmp">$mは不思議な光に包まれた！</span>|;	}],
		[36,	12,		'イオラ',			sub{ &_damages(70, '魔', 1);	}],
		[46,	10,		'パルプンテ',		sub{ &_parupunte;	}],
		[66,	34,		'イオナズン',		sub{ &_damages(160, '魔', 1);	}],
		[96,	0,		'デビルテイル',		sub{ &_yubiwofuru;	}],
	);
}
sub skill_57 { # ｴﾙﾌ
	return (
		[10,	3,		'ホイミ',			sub{ &_heal(shift, 30, '魔');	}],
		[20,	6,		'フラッシュアロー',	sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at}*1.2, '攻'); return if !$y || $ms{$y}{hp} <= 0; &_st_down($y, 0.07, '攻', 'hit');	}],
		[40,	10,		'ベホイミ',			sub{ &_heal(shift, 90, '魔');	}],
		[60,	20,		'ラリホーアロー',	sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at}*1.1, '攻'); return if !$y || $ms{$y}{hp} <= 0; &_st_d($y, '眠り', '攻', 55);	}],
		[80,	20,		'ザオラル',			sub{ my($y) = &_check_party(shift, '蘇生', '魔'); return if !$y || $ms{$y}{hp} > 0; if (rand(2) < 1) { $com.=qq|なんと、<span class="revive">$yが生き返りました！</span>|; $ms{$y}{hp}=int($ms{$y}{mhp} * 0.5); } else { $com.=qq|しかし、$yは生き返らなかった…|; };	}],
		[100,	4,		'ようせいのや',		sub{ my($y, $v) = &_st_down(shift, 0.15, '攻', 'mp'); return if !$y; &_mp_h($m, $v, '攻');	}],
		[120,	33,		'バイシオン',		sub{ &_st_ups(0.7, '魔', 'at');		}],
	);
}
sub skill_58 { # ﾀﾞｰｸｴﾙﾌ
	return (
		[20,	26,		'ライフシェイバー',		sub{ my($y) = &_check_enemy(shift, '瀕死', '魔'); return if !$y; if (rand(5)>1) { &_st_down($y, 0.7, '魔', 'hp'); } else { $com.="$yはかわした！"; };	}],
		[50,	9,		'トランス',				sub{ $ms{$m}{state}=''; &_st_up($m, 1.0, '攻', 'at'); &_st_up($m, 1.0, '攻', 'ag'); $ms{$m}{tmp} = '魔吸収'; $ms{$m}{state}='混乱'; $com.="$mはトランス状態になった！";		}],
		[80,	16,		'のろい',				sub{ my @randoms = ('魔封', '攻封', '動封'); for my $name (@enemys) { &_st_d($name, $randoms[int(rand(@randoms))], '魔', 70); };		}],
		[110,	6,		'ＭＰバスター',			sub{ &_st_down(shift, 0.4, '魔', 'mp');	}],
		[140,	33,		'かくせい',				sub{ $ms{$m}{tmp}='２倍'; &tenshon($m); &tenshon($m); 		}],
		[160,	66,		'ハレーション',			sub{ for my $y (@enemys) { if (rand(3)>1) { &_st_down($y, 0.75, '魔', 'hp'); } else { $com.="$yはかわした！"; }; };	}],
	);
}
sub skill_59 { # ｽﾗｲﾑﾗｲﾀﾞｰ
	return (
		[10,	30,		'よびだす',				sub{ my $n = '@ｽﾗｲﾑ@'; if (defined $ms{$n}{name}) { $com.="$nを呼び出すのに失敗した…"; return; }; $m{lv} < 40 ? &_add_party($n, 'mon/001.gif', 70, 120, 50, 30, 120) : $m{lv} < 70 ? &_add_party($n, 'mon/006.gif', 180, 80, 80, 50, 200) : &_add_party($n, 'mon/004.gif', 5, 10, 10, 950, 950); $com.="$nが戦闘に参加した！"; 	}],
		[11,	0,		'にげろ',				sub{ my $n = '@ｽﾗｲﾑ@'; return if !defined($ms{$n}{name}) || $ms{$n}{hp} <= 0; $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; $com.="$nが戦闘から逃げ出した！"; 	}],
		[12,	0,		'こうげきめいれい',		sub{ my $n = '@ｽﾗｲﾑ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(39); return if !$n || $ms{$n}{hp} <= 0; $com.="$n： ＠こうげき "; $buf_m = $m; $m = $n; &kougeki(shift); $m = $buf_m;	}],
		[30,	30,		'ひっさつめいれい',		sub{ my $n = '@ｽﾗｲﾑ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(39); return if !$n || $ms{$n}{hp} <= 0; $com.="$n： "; if (rand(2)<1) { $com.='＠スラアタック '; &_damage(shift, $ms{$n}{at} * 1.5, '攻'); }elsif(rand(2)<1){ $com.='＠スラストライク '; &_damage(shift, $ms{$n}{at} * 1.2, '攻', 1); }else{ $com.='＠しゃくねつ '; &_damages(220, '息', 1); }; 	}],
		[100,	10,		'ぼうぎょめいれい',		sub{ my $n = '@ｽﾗｲﾑ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(39); return if !$n || $ms{$n}{hp} <= 0; $ms{$n}{tmp} = '防御'; $com.=qq|$n： ＠ぼうぎょ <span class="tmp">$nは身を固めた！</span>|;	}],
		[150,	100,	'がったい',				sub{ my $n = '@ｽﾗｲﾑ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(39); return if !$n || $ms{$n}{hp} <= 0; for my $k (qw/hp mp at df ag/){ my $v=$ms{$m}{$k}; $ms{$m}{$k}+=$ms{$n}{$k}; $ms{$n}{$k}+=$v; $ms{$m}{$k}=999 if $ms{$m}{$k}>999; $ms{$n}{$k}=999 if $ms{$n}{$k}>999; }; $com.=qq|<span class="tmp">$mと$nは合体した！</span>|; $ms{$m}{icon}="job/59_$m{sex}_mix.gif"; if ($n =~ /^@/) { $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; } else { $ms{$n}{icon}="job/0.gif"; } 	}],
	);
}

sub skill_60 { # ﾄﾞﾗｺﾞﾝﾗｲﾀﾞｰ
	return (
		[10,	30,		'よびだす',				sub{ my $n = '@ﾄﾞﾗｺﾞﾝ@'; if (defined $ms{$n}{name}) { $com.="$nを呼び出すのに失敗した…"; return; }; $m{lv} < 40 ? &_add_party($n, 'mon/083.gif', 160, 70, 180, 100, 70) : $m{lv} < 70 ? &_add_party($n, 'mon/084.gif', 250, 50, 300, 200, 100) : &_add_party($n, 'mon/224.gif', 400, 30, 400, 300, 100); $com.="$nが戦闘に参加した！"; 	}],
		[11,	0,		'にげろ',				sub{ my $n = '@ﾄﾞﾗｺﾞﾝ@'; return if !defined($ms{$n}{name}) || $ms{$n}{hp} <= 0; $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; $com.="$nが戦闘から逃げ出した！"; 	}],
		[12,	0,		'こうげきめいれい',		sub{ my $n = '@ﾄﾞﾗｺﾞﾝ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(41); return if !$n || $ms{$n}{hp} <= 0; $com.="$n： ＠こうげき "; $buf_m = $m; $m = $n; &kougeki(shift); $m = $buf_m;	}],
		[30,	30,		'ひっさつめいれい',		sub{ my $n = '@ﾄﾞﾗｺﾞﾝ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(41); return if !$n || $ms{$n}{hp} <= 0; $com.="$n： "; if (rand(2)<1) { $com.='＠きりさく '; &_damage(shift, $ms{$n}{at} * 1.7, '攻'); }elsif(rand(2)<1){ $com.='＠たたきつぶす '; &_damage(shift, $ms{$n}{at} * 1.5, '攻', 1); }else{ $com.='＠かがやくいき '; &_damages(230, '息', 1); }; 	}],
		[100,	10,		'ぼうぎょめいれい',		sub{ my $n = '@ﾄﾞﾗｺﾞﾝ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(41); return if !$n || $ms{$n}{hp} <= 0; $ms{$n}{tmp} = '防御'; $com.=qq|$n： ＠ぼうぎょ <span class="tmp">$nは身を固めた！</span>|;	}],
		[150,	100,	'がったい',				sub{ my $n = '@ﾄﾞﾗｺﾞﾝ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(41); return if !$n || $ms{$n}{hp} <= 0; for my $k (qw/hp mp at df ag/){ my $v=$ms{$m}{$k}; $ms{$m}{$k}+=$ms{$n}{$k}; $ms{$n}{$k}+=$v; $ms{$m}{$k}=999 if $ms{$m}{$k}>999; $ms{$n}{$k}=999 if $ms{$n}{$k}>999; }; $com.=qq|<span class="tmp">$mと$nは合体した！</span>|; $ms{$m}{icon}="job/60_$m{sex}_mix.gif"; if ($n =~ /^@/) { $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; } else { $ms{$n}{icon}="job/0.gif"; } 	}],
	);
}
sub skill_61 { # ﾈｸﾛﾏﾝｻｰ
	return (
		[10,	30,		'よびだす',				sub{ my $n = '@ｿﾞﾝﾋﾞ@'; if (defined $ms{$n}{name}) { $com.="$nを呼び出すのに失敗した…"; return; }; $m{lv} < 40 ? &_add_party($n, 'mon/040.gif', 120, 120, 120, 60, 120) : $m{lv} < 70 ? &_add_party($n, 'mon/041.gif', 300, 200, 280, 90, 240) : &_add_party($n, 'mon/064.gif', 444, 444, 666, 222, 444); $com.="$nが戦闘に参加した！"; 	}],
		[11,	0,		'にげろ',				sub{ my $n = '@ｿﾞﾝﾋﾞ@'; return if !defined($ms{$n}{name}) || $ms{$n}{hp} <= 0; $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; $com.="$nが戦闘から逃げ出した！"; 	}],
		[12,	0,		'こうげきめいれい',		sub{ my $n = '@ｿﾞﾝﾋﾞ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(61); return if !$n || $ms{$n}{hp} <= 0; $com.="$n： ＠こうげき "; $buf_m = $m; $m = $n; &kougeki(shift); $m = $buf_m;	}],
		[30,	30,		'ひっさつめいれい',		sub{ my $n = '@ｿﾞﾝﾋﾞ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(61); return if !$n || $ms{$n}{hp} <= 0; $com.="$n： "; if (rand(2)<1) { $com.='＠ザラキ '; &_deaths('即死', '魔', 22); }elsif(rand(2)<1){ $com.='＠バイオガ '; $is_add_effect = 1; &_damages(120, '魔', 1); &_st_ds('猛毒', '魔', 40); }else{ $com.='＠もうどくのきり '; &_st_ds('猛毒', '息', 70); }; 	}],
		[100,	10,		'ぼうぎょめいれい',		sub{ my $n = '@ｿﾞﾝﾋﾞ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(61); return if !$n || $ms{$n}{hp} <= 0; $ms{$n}{tmp} = '防御'; $com.=qq|$n： ＠ぼうぎょ <span class="tmp">$nは身を固めた！</span>|;	}],
		[150,	42,		'レクイエム',			sub{ my $n = '@ｿﾞﾝﾋﾞ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(61); return if !$n || $ms{$n}{hp} <= 0; for my $y (@partys) { next if $ms{$y}{hp} > 0; $ms{$y}{hp}=int($ms{$y}{mhp}*0.42); $ms{$y}{at}+=300;$ms{$y}{ag}+=300; $com.=qq|<span class="revive">$yが生き返った！</span>|; $ms{$y}{icon}="mon/040.gif"; }; 	}],
	);
}
sub skill_62 { # ﾊﾞｯﾄﾏｽﾀｰ
	return (
		[10,	30,		'よびだす',				sub{ my $n = '@ﾊﾞｯﾄ@'; if (defined $ms{$n}{name}) { $com.="$nを呼び出すのに失敗した…"; return; }; $m{lv} < 40 ? &_add_party($n, 'mon/025.gif', 90, 80, 120, 10, 180) : $m{lv} < 70 ? &_add_party($n, 'mon/026.gif', 210, 270, 170, 30, 400) : &_add_party($n, 'mon/027.gif', 410, 350, 400, 50, 600); $com.="$nが戦闘に参加した！"; 	}],
		[11,	0,		'にげろ',				sub{ my $n = '@ﾊﾞｯﾄ@'; return if !defined($ms{$n}{name}) || $ms{$n}{hp} <= 0; $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; $com.="$nが戦闘から逃げ出した！"; 	}],
		[12,	0,		'こうげきめいれい',		sub{ my $n = '@ﾊﾞｯﾄ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(56); return if !$n || $ms{$n}{hp} <= 0; $com.="$n： ＠こうげき "; $buf_m = $m; $m = $n; &kougeki(shift); $m = $buf_m;	}],
		[30,	30,		'ひっさつめいれい',		sub{ my $n = '@ﾊﾞｯﾄ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(56); return if !$n || $ms{$n}{hp} <= 0; $com.="$n： "; if (rand(2)<1) { $com.='＠きゅうけつ '; my($y, $v)= &_damage(shift, 100, '魔', 1); return if !$y; &_heal($n, $v, '魔');}elsif(rand(2)<1){ $com.='＠アスピル '; my($y, $v) = &_st_down(shift, 0.3, '魔', 'mp'); return if !$y; &_mp_h($m, $v, '魔'); }else{ $com.='＠ちょうおんぱ '; &_st_ds('混乱', '歌', 70); }; 	}],
		[100,	10,		'ぼうぎょめいれい',		sub{ my $n = '@ﾊﾞｯﾄ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(56); return if !$n || $ms{$n}{hp} <= 0; $ms{$n}{tmp} = '防御'; $com.=qq|$n： ＠ぼうぎょ <span class="tmp">$nは身を固めた！</span>|;	}],
		[150,	37,		'ブラッドレイン',		sub{ my $n = '@ﾊﾞｯﾄ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(56); return if !$n || $ms{$n}{hp} <= 0; &_damages(170, '魔', 1); &_heals(150, '魔'); 	}],
	);
}
sub skill_63 { # ｷﾉｺﾏｽﾀｰ
	return (
		[10,	30,		'よびだす',				sub{ my $n = '@ｷﾉｺ@'; if (defined $ms{$n}{name}) { $com.="$nを呼び出すのに失敗した…"; return; }; $m{lv} < 40 ? &_add_party($n, 'mon/030.gif', 100, 100, 80, 50, 80) : $m{lv} < 70 ? &_add_party($n, 'mon/031.gif', 300, 80, 150, 100, 100) : &_add_party($n, 'mon/032.gif', 400, 60, 200, 100, 100); $com.="$nが戦闘に参加した！"; 	}],
		[11,	0,		'にげろ',				sub{ my $n = '@ｷﾉｺ@'; return if !defined($ms{$n}{name}) || $ms{$n}{hp} <= 0; $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; $com.="$nが戦闘から逃げ出した！"; 	}],
		[12,	0,		'こうげきめいれい',		sub{ my $n = '@ｷﾉｺ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(63); return if !$n || $ms{$n}{hp} <= 0; $com.="$n： ＠こうげき "; $buf_m = $m; $m = $n; &kougeki(shift); $m = $buf_m;	}],
		[30,	30,		'ひっさつめいれい',		sub{ my $n = '@ｷﾉｺ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(63); return if !$n || $ms{$n}{hp} <= 0; $com.="$n： "; if (rand(2)<1) { $com.='＠どくのこな '; &_st_ds('猛毒', '息', 90);}elsif(rand(2)<1){ $com.='＠しびれごな '; &_st_ds('麻痺', '息', 50);}else{ $com.='＠ねむりごな '; &_st_ds('眠り', '息', 50); }; 	}],
		[100,	10,		'ぼうぎょめいれい',		sub{ my $n = '@ｷﾉｺ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(63); return if !$n || $ms{$n}{hp} <= 0; $ms{$n}{tmp} = '防御'; $com.=qq|$n： ＠ぼうぎょ <span class="tmp">$nは身を固めた！</span>|;	}],
		[150,	100,	'がったい',				sub{ my $n = '@ｷﾉｺ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(63); return if !$n || $ms{$n}{hp} <= 0; for my $k (qw/hp mp at df ag/){ my $v=$ms{$m}{$k}; $ms{$m}{$k}+=$ms{$n}{$k}; $ms{$n}{$k}+=$v; $ms{$m}{$k}=999 if $ms{$m}{$k}>999; $ms{$n}{$k}=999 if $ms{$n}{$k}>999; }; $com.=qq|<span class="tmp">$mと$nは合体した！</span>|; $ms{$m}{icon}="job/63_$m{sex}_mix.gif"; if ($n =~ /^@/) { $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; } else { $ms{$n}{icon}="job/0.gif"; } 	}],
	);
}
sub skill_64 { # ｵﾊﾞｹﾏｽﾀｰ
	return (
		[10,	30,		'よびだす',				sub{ my $n = '@ｺﾞｰｽﾄ@'; if (defined $ms{$n}{name}) { $com.="$nを呼び出すのに失敗した…"; return; }; $m{lv} < 40 ? &_add_party($n, 'mon/035.gif', 100, 100, 50, 100, 100) : $m{lv} < 70 ? &_add_party($n, 'mon/036.gif', 200, 80, 100, 150, 150) : &_add_party($n, 'mon/070.gif', 300, 60, 150, 200, 200); $com.="$nが戦闘に参加した！"; 	}],
		[11,	0,		'にげろ',				sub{ my $n = '@ｺﾞｰｽﾄ@'; return if !defined($ms{$n}{name}) || $ms{$n}{hp} <= 0; $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; $com.="$nが戦闘から逃げ出した！"; 	}],
		[12,	0,		'こうげきめいれい',		sub{ my $n = '@ｺﾞｰｽﾄ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(64); return if !$n || $ms{$n}{hp} <= 0; $com.="$n： ＠こうげき "; $buf_m = $m; $m = $n; &kougeki(shift); $m = $buf_m;	}],
		[30,	30,		'ひっさつめいれい',		sub{ my $n = '@ｺﾞｰｽﾄ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(64); return if !$n || $ms{$n}{hp} <= 0; $com.="$n： "; if (rand(2)<1) { $com.='＠ひょうい '; my($y) = &_check_enemy(shift, '操り', '息'); return if !$y; $com.="$n： ＠こうげき "; $buf_m = $m; $m = $y; &kougeki(); $m = $buf_m; }elsif(rand(2)<1){ $com.='＠じゅばく '; &_st_d(shift, '攻封', '無', 80); }else{ $com.='＠おどろかす'; &_st_ds('動封', '攻', 60); }; 	}],
		[100,	10,		'ぼうぎょめいれい',		sub{ my $n = '@ｺﾞｰｽﾄ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(64); return if !$n || $ms{$n}{hp} <= 0; $ms{$n}{tmp} = '防御'; $com.=qq|$n： ＠ぼうぎょ <span class="tmp">$nは身を固めた！</span>|;	}],
		[150,	100,	'がったい',				sub{ my $n = '@ｺﾞｰｽﾄ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(64); return if !$n || $ms{$n}{hp} <= 0; for my $k (qw/hp mp at df ag/){ my $v=$ms{$m}{$k}; $ms{$m}{$k}+=$ms{$n}{$k}; $ms{$n}{$k}+=$v; $ms{$m}{$k}=999 if $ms{$m}{$k}>999; $ms{$n}{$k}=999 if $ms{$n}{$k}>999; }; $com.=qq|<span class="tmp">$mと$nは合体した！</span>|; $ms{$m}{icon}="job/64_$m{sex}_mix.gif"; if ($n =~ /^@/) { $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; } else { $ms{$n}{icon}="job/0.gif"; } 	}],
	);
}
sub skill_65 { # ｹﾓﾉﾏｽﾀｰ
	return (
		[10,	30,		'よびだす',				sub{ my $n = '@ｹﾓﾉ@'; if (defined $ms{$n}{name}) { $com.="$nを呼び出すのに失敗した…"; return; }; $m{lv} < 40 ? &_add_party($n, 'mon/200.gif', 100, 60, 100, 60, 180) : $m{lv} < 70 ? &_add_party($n, 'mon/206.gif', 210, 90, 300, 80, 280) : &_add_party($n, 'mon/203.gif', 400, 230, 500, 160, 400); $com.="$nが戦闘に参加した！"; 	}],
		[11,	0,		'にげろ',				sub{ my $n = '@ｹﾓﾉ@'; return if !defined($ms{$n}{name}) || $ms{$n}{hp} <= 0; $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; $com.="$nが戦闘から逃げ出した！"; 	}],
		[12,	0,		'こうげきめいれい',		sub{ my $n = '@ｹﾓﾉ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(44); return if !$n || $ms{$n}{hp} <= 0; $com.="$n： ＠こうげき "; $buf_m = $m; $m = $n; &kougeki(shift); $m = $buf_m;	}],
		[30,	30,		'ひっさつめいれい',		sub{ my $n = '@ｹﾓﾉ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(44); return if !$n || $ms{$n}{hp} <= 0; $com.="$n： "; if (rand(2)<1) { $com.='＠ひっかく '; &_damage(shift, $ms{$n}{at} * 1.5, '攻'); }elsif(rand(2)<1){ $com.='＠かみつく '; &_damage(shift, $ms{$n}{at} * 1.2, '攻', 1); }else{ $com.='＠とつげき '; &_damage(shift, $ms{$n}{at} * 2.0, '攻'); }; 	}],
		[100,	10,		'ぼうぎょめいれい',		sub{ my $n = '@ｹﾓﾉ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(44); return if !$n || $ms{$n}{hp} <= 0; $ms{$n}{tmp} = '防御'; $com.=qq|$n： ＠ぼうぎょ <span class="tmp">$nは身を固めた！</span>|;	}],
		[150,	40,		'どとうのけもの',		sub{ my $n = '@ｹﾓﾉ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(44); return if !$n || $ms{$n}{hp} <= 0; my $v = int(rand(2)+3); for my $i (1..$v) { last if $ms{$m}{hp} <= 0; &_damage(undef, $ms{$n}{ag} * 2.0, '攻'); };	}],
	);
}
sub skill_66 { # ﾄﾞｸﾛﾏｽﾀｰ
	return (
		[10,	30,		'よびだす',				sub{ my $n = '@ｶﾞｲｺﾂ@'; if (defined $ms{$n}{name}) { $com.="$nを呼び出すのに失敗した…"; return; }; $m{lv} < 40 ? &_add_party($n, 'mon/043.gif', 120, 110, 160, 90, 150) : $m{lv} < 70 ? &_add_party($n, 'mon/044.gif', 240, 210, 240, 120, 180) : &_add_party($n, 'mon/056.gif', 450, 280, 400, 240, 300); $com.="$nが戦闘に参加した！"; 	}],
		[11,	0,		'にげろ',				sub{ my $n = '@ｶﾞｲｺﾂ@'; return if !defined($ms{$n}{name}) || $ms{$n}{hp} <= 0; $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; $com.="$nが戦闘から逃げ出した！"; 	}],
		[12,	0,		'こうげきめいれい',		sub{ my $n = '@ｶﾞｲｺﾂ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(66); return if !$n || $ms{$n}{hp} <= 0; $com.="$n： ＠こうげき "; $buf_m = $m; $m = $n; &kougeki(shift); $m = $buf_m;	}],
		[30,	30,		'ひっさつめいれい',		sub{ my $n = '@ｶﾞｲｺﾂ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(66); return if !$n || $ms{$n}{hp} <= 0; $com.="$n： "; if (rand(2)<1) { $com.='＠しのおどり '; &_deaths('即死', '踊', 20); }elsif(rand(2)<1){ $com.='＠デス '; &_death(shift, '即死', '攻', 40);}else{ $com.='＠のろい '; my @randoms = ('攻封', '動封'); for my $name (@enemys) { &_st_d($name, $randoms[int(rand(@randoms))], '魔', 75); }; }; 	 	}],
		[100,	10,		'ぼうぎょめいれい',		sub{ my $n = '@ｶﾞｲｺﾂ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(66); return if !$n || $ms{$n}{hp} <= 0; $ms{$n}{tmp} = '防御'; $com.=qq|$n： ＠ぼうぎょ <span class="tmp">$nは身を固めた！</span>|;	}],
		[150,	50,		'みんなのうらみ',		sub{ my $n = '@ｶﾞｲｺﾂ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(66); return if !$n || $ms{$n}{hp} <= 0; my $d = 100; for my $y (@partys) { $d += 420 if $ms{$y}{hp} <= 0; } &_damages($d, '無', 1); 	}],
	);
}
sub skill_67 { # ﾊﾞﾌﾞﾙﾏｽﾀｰ
	return (
		[10,	30,		'よびだす',				sub{ my $n = '@ﾊﾞﾌﾞﾙ@'; if (defined $ms{$n}{name}) { $com.="$nを呼び出すのに失敗した…"; return; }; $m{lv} < 40 ? &_add_party($n, 'mon/020.gif', 90, 120, 90, 50, 90) : $m{lv} < 70 ? &_add_party($n, 'mon/021.gif', 180, 280, 160, 120, 180) : &_add_party($n, 'mon/022.gif', 8, 500, 80, 950, 950); $com.="$nが戦闘に参加した！"; 	}],
		[11,	0,		'にげろ',				sub{ my $n = '@ﾊﾞﾌﾞﾙ@'; return if !defined($ms{$n}{name}) || $ms{$n}{hp} <= 0; $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; $com.="$nが戦闘から逃げ出した！"; 	}],
		[12,	0,		'こうげきめいれい',		sub{ my $n = '@ﾊﾞﾌﾞﾙ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(40); return if !$n || $ms{$n}{hp} <= 0; $com.="$n： ＠こうげき "; $buf_m = $m; $m = $n; &kougeki(shift); $m = $buf_m;	}],
		[30,	30,		'ひっさつめいれい',		sub{ my $n = '@ﾊﾞﾌﾞﾙ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(40); return if !$n || $ms{$n}{hp} <= 0; $com.="$n： "; if ($ms{$n}{icon} =~ /020/) { $com.='＠ドクドク '; &_st_ds('猛毒', '息', 80); }elsif($ms{$n}{icon} =~ /021/){ $com.='＠マグマ '; &_damages(220, '息', 1); }else{ $com.='＠ジゴスパーク '; $is_add_effect = 1; &_damages(150, '魔', 1); &_st_ds('麻痺', '魔', 20);}	}],
		[100,	10,		'ぼうぎょめいれい',		sub{ my $n = '@ﾊﾞﾌﾞﾙ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(40); return if !$n || $ms{$n}{hp} <= 0; $ms{$n}{tmp} = '防御'; $com.=qq|$n： ＠ぼうぎょ <span class="tmp">$nは身を固めた！</span>|;	}],
		[150,	40,		'バブルボム',			sub{ my $n = '@ﾊﾞﾌﾞﾙ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(40); return if !$n || $ms{$n}{hp} <= 0; $is_add_effect = 1; for my $y (@enemys) { my($_y) = &_damage($y, 150, '息', 1); next if rand(2)<1; $com.="$_yはあやしい液体がかかった！"; $ms{$_y}{tmp} = '２倍'; }; 	}],
	);
}
sub skill_68 { # ｺﾛﾋｰﾛｰ
	return (
		[10,	30,		'よびだす',				sub{ my $n = '@ｺﾛ@'; if (defined $ms{$n}{name}) { $com.="$nを呼び出すのに失敗した…"; return; }; rand(3) < 1 ? &_add_party($n, 'mon/101.gif', $ms{$m}{mhp}*0.8, $ms{$m}{mmp}*0.2, $ms{$m}{mat}*3.0, $ms{$m}{mdf}*2.0, $ms{$m}{mag}) : rand(3) < 1 ? &_add_party($n, 'mon/102.gif', $ms{$m}{mhp}*0.6, $ms{$m}{mmp}, $ms{$m}{mat}, $ms{$m}{mdf}, $ms{$m}{mag}*2.0) : &_add_party($n, 'mon/103.gif',  $ms{$m}{mhp}*0.7, $ms{$m}{mmp}, $ms{$m}{mat}*1.5, $ms{$m}{mdf}*1.5, $ms{$m}{mag}*1.5); $com.="$nが戦闘に参加した！"; 	}],
		[11,	0,		'にげろ',				sub{ my $n = '@ｺﾛ@'; return if !defined($ms{$n}{name}) || $ms{$n}{hp} <= 0; $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; $com.="$nが戦闘から逃げ出した！"; 	}],
		[12,	0,		'こうげきめいれい',		sub{ my $n = '@ｺﾛ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(68); return if !$n || $ms{$n}{hp} <= 0; $com.="$n： ＠こうげき "; $buf_m = $m; $m = $n; &kougeki(shift); $m = $buf_m;	}],
		[30,	30,		'ひっさつめいれい',		sub{ my $n = '@ｺﾛ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(68); return if !$n || $ms{$n}{hp} <= 0; $com.="$n： "; if ($ms{$n}{icon} =~ /101/) { $com.='＠まじんぎり '; rand(2) < 1 ? &_damage(shift, $ms{$m}{at} * 3, '攻') : &_damage(shift, 20, '攻'); }elsif($ms{$n}{icon} =~ /102/){ $com.='＠メラゾーマ '; &_damage(shift, 220, '魔', 1); }else{ $com.='＠ベホマ '; &_heal(shift, 999, '魔'); }; 	}],
		[100,	10,		'ぼうぎょめいれい',		sub{ my $n = '@ｺﾛ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(68); return if !$n || $ms{$n}{hp} <= 0; $ms{$n}{tmp} = '防御'; $com.=qq|$n： ＠ぼうぎょ <span class="tmp">$nは身を固めた！</span>|;	}],
		[150,	50,		'ベホマズン',			sub{ my $n = '@ｺﾛ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(68); return if !$n || $ms{$n}{hp} <= 0; &_heals(999, '魔');	}],
	);
}
sub skill_69 { # ﾌﾟﾁﾋｰﾛｰ
	return (
		[10,	30,		'よびだす',				sub{ my $n = '@ﾌﾟﾁ@'; if (defined $ms{$n}{name}) { $com.="$nを呼び出すのに失敗した…"; return; }; rand(3) < 1 ? &_add_party($n, 'mon/106.gif', $ms{$m}{mhp}*0.8, $ms{$m}{mmp}*0.2, $ms{$m}{mat}*3.0, $ms{$m}{mdf}*2.0, $ms{$m}{mag}) : rand(3) < 1 ? &_add_party($n, 'mon/107.gif', $ms{$m}{mhp}*0.6, $ms{$m}{mmp}, $ms{$m}{mat}, $ms{$m}{mdf}, $ms{$m}{mag}*2.0) : &_add_party($n, 'mon/108.gif',  $ms{$m}{mhp}*0.7, $ms{$m}{mmp}, $ms{$m}{mat}*1.5, $ms{$m}{mdf}*1.5, $ms{$m}{mag}*1.5); $com.="$nが戦闘に参加した！"; 	}],
		[11,	0,		'にげろ',				sub{ my $n = '@ﾌﾟﾁ@'; return if !defined($ms{$n}{name}) || $ms{$n}{hp} <= 0; $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; $com.="$nが戦闘から逃げ出した！"; 	}],
		[12,	0,		'こうげきめいれい',		sub{ my $n = '@ﾌﾟﾁ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(69); return if !$n || $ms{$n}{hp} <= 0; $com.="$n： ＠こうげき "; $buf_m = $m; $m = $n; &kougeki(shift); $m = $buf_m;	}],
		[30,	30,		'ひっさつめいれい',		sub{ my $n = '@ﾌﾟﾁ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(69); return if !$n || $ms{$n}{hp} <= 0; $com.="$n： "; if ($ms{$n}{icon} =~ /106/) { $com.='＠まじんぎり '; rand(2) < 1 ? &_damage(shift, $ms{$m}{at} * 3, '攻') : &_damage(shift, 20, '攻'); }elsif($ms{$n}{icon} =~ /107/){ $com.='＠メラゾーマ '; &_damage(shift, 220, '魔', 1); }else{ $com.='＠ベホマ '; &_heal(shift, 999, '魔'); }; 	}],
		[100,	10,		'ぼうぎょめいれい',		sub{ my $n = '@ﾌﾟﾁ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(69); return if !$n || $ms{$n}{hp} <= 0; $ms{$n}{tmp} = '防御'; $com.=qq|$n： ＠ぼうぎょ <span class="tmp">$nは身を固めた！</span>|;	}],
		[150,	20,		'ミナデイン',			sub{ my $n = '@ﾌﾟﾁ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(69); return if !$n || $ms{$n}{hp} <= 0; my($y) = &_check_enemy(shift, '皆', '魔'); return if !$y; my $d = 100; for my $name (@partys) { next if $m eq $name || $ms{$name}{mp} < 5; $ms{$name}{mp}-=5; $d += 85; }; $com.=qq|$mは仲間のみんなから力を受けとった！| if $d > 100; &_damage($y, $d, '魔', 1);	}],
	);
}
sub skill_70 { # 天竜人
	return (
		[50,	25,		'めいそう',			sub{ &_heal($m, 300, '無');		}],
		[100,	25,		'ドラゴンパワー',	sub{ &_st_up($m, 0.4, '攻', 'at'); &_st_up($m, 0.4, '攻', 'df');	}],
		[150,	40,		'ギガデイン',		sub{ &_damages(180, '魔', 1);			}],
		[200,	27,		'てんしのうたごえ',	sub{ for my $y (@partys) { next if $ms{$y}{hp} > 0; if (rand(2) < 1) { $com.=qq|なんと、<b>$y</b>が <span class="heal">生き返り</span> ました！|; $ms{$y}{hp}=int($ms{$y}{mhp} * 0.5); } else { $com.=qq|しかし、<b>$y</b>は生き返らなかった…|; }; }; 	}],
	);
}

# 敵用
sub skill_90 { # 猛毒系
	return (
		[10,	4,		'どくこうげき',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at} * 1.1, '攻'); return if !$y || $ms{$y}{hp} <= 0; &_st_d($y, '猛毒', '攻', 70);	}],
		[20,	6,		'ポイズン',			sub{ $is_add_effect = 1; my($y) = &_damage(shift, 25, '魔', 1); return if !$y || $ms{$y}{hp} <= 0; &_st_d($y, '猛毒', '魔', 80);	}],
		[30,	8,		'もうどくのきり',	sub{ &_st_ds('猛毒', '息', 60);		}],
	);
}
sub skill_91 { # 麻痺系
	return (
		[10,	8,		'まひこうげき',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at} * 1.2, '攻'); return if !$y || $ms{$y}{hp} <= 0; &_st_d($y, '麻痺', '攻', 30);	}],
		[20,	11,		'しびれうち',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at} * 0.8, '攻'); return if !$y || $ms{$y}{hp} <= 0; &_st_d($y, '麻痺', '攻', 40);	}],
		[30,	9,		'やけつくいき',		sub{ &_st_ds('麻痺', '息', 35);		}],
	);
}
sub skill_92 { # 眠り系
	return (
		[10,	8,		'ラリホー',			sub{ &_st_d(shift, '眠り', '魔', 65);		}],
		[20,	15,		'ねむりこうげき',	sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at} * 0.8, '攻'); return if !$y || $ms{$y}{hp} <= 0; &_st_d($y, '眠り', '攻', 55);	}],
		[30,	9,		'あまいいき',		sub{ &_st_ds('眠り', '息', 35);	}],
	);
}
sub skill_93 { # 即死
	return (
		[10,	14,		'ザキ',			sub{ &_death(shift, '即死', '魔', 20);	}],
		[20,	32,		'ザラキ',		sub{ &_deaths('即死', '魔', 20);	}],
		[30,	24,		'しのおどり',	sub{ &_deaths('即死', '踊', 17);	}],
		[40,	42,		'しのせんこく',	sub{ my($y) = &_check_enemy(shift, '瀕死', '魔'); return if !$y; if ($ms{$y}{mhp}>999 || $ms{$y}{mdf}>999) { $com.="$yにはきかなかった！"; } elsif (rand(2)<1) { &_st_down($y, 0.75, '魔', 'hp'); $ms{$y}{state}='猛毒'; } else { $com.="$yはかわした！"; };	}],
	);
}
sub skill_94 { # 自爆
	return (
		[10,	1,		'メガンテ',		sub{ $com.=qq|<span class="die">$mは自爆した！</span>|; &_deaths('即死', '無', 60); &defeat($m); $ms{$m}{mp} = 1;	}],
		[20,	0,		'ねる',			sub{ $ms{$m}{state}='眠り'; $com.=qq|<span class="state">$mは眠りだした</span>|; &_heal($m, $ms{$m}{mhp}*0.5);	}],
	);
}
sub skill_95 { # 召喚
	return (
		[0,		50,		'しょうかん',	sub{ &_add_enemy	}],
		[0,		50,		'しょうかん',	sub{ &_add_enemy	}],
	);
}
sub skill_96 { # ﾄﾞｰﾙﾏｽﾀｰ
	return (
		[0,	0,		'あやつる',			sub{ my($y) = &_check_enemy(shift, '操る', '無'); my @alfas = ('A'..'Z'); $ms{$y}{name} = '@人形'.$alfas[int(rand(@alfas))]; $ms{$y}{color}=$ms{$m}{color}; $ms{$y}{addr} = 0; $com.=qq|<span class="die">$yは$mのあやつり人形となった！</span>|;	}],
		[0,	0,		'クールジョーク',	sub{ for my $y (@enemys) { $ms{$y}{ten} = 1; }; $com.="全員のテンションが下がった…";	}],
	);
}
sub skill_97 { # 超攻撃型(破壊神[king1]、ｶﾀｽﾄﾛﾌｨｰ[21]、ﾙｼﾌｧｰ[20])
	return (
		[0,		24,		'みだれうち',		sub{ my $v = int(rand(2)+3); for my $i (1..$v) { last if $ms{$m}{hp} <= 0; &_damage(undef, $ms{$m}{at}*0.85, '攻'); };		}],
		[0,		20,		'ばくれつけん',		sub{ my $v = int(rand(3)+3); for my $i (1..$v) { last if $ms{$m}{hp} <= 0; &_damage(undef, $ms{$m}{at}*0.9, '攻'); };	}],
		[0,		30,		'いてつくはどう',	sub{ for my $y (@members) { my $tten=$ms{$y}{ten}; &reset_status($y); $ms{$y}{ten}=$tten; }; $com.=qq|<span class="st_down">全ての効果がかき消された！</span>|;	}],
		[0,		9,		'めいやく',			sub{ my $v = int($ms{$m}{df} * 0.5); $ms{$m}{df} -= $v; $com.=qq|$mの<span class="st_down">$e2j{df}が $v さがりました！</span>|; &_st_up($m, 1.0, '無', 'at');	}],
		[0,		30,		'だいぼうそう',		sub{ &_damages(300, '攻', 1); $ms{$m}{tmp}='２倍';	}],
		[0,		40,		'あんこくけん',		sub{ my($y, $v) = &_damage(shift, $ms{$m}{at}*2.5, '攻'); return if $v <= 0; &_risk($v * 0.2);		}],
		[0,		33,		'きあいため',		sub{ $ms{$m}{tmp}='２倍'; &tenshon($m); &tenshon($m);	}],
		[0,		80,		'しっこくのほのお',	sub{ &_damages(400, '息', 1);	}],
		[0,		70,		'ジゴスパーク',		sub{ $is_add_effect = 1; &_damages(250, '魔', 1); &_st_ds('麻痺', '魔', 20);	}],
		[0,		42,		'しのせんこく',		sub{ my($y) = &_check_enemy(shift, '瀕死', '魔'); return if !$y; if ($ms{$y}{mhp}>999 || $ms{$y}{mdf}>999) { $com.="$yにはきかなかった！"; } else { &_st_down($y, 0.75, '魔', 'hp'); $ms{$y}{state}='猛毒'; };	}],
		[0,		66,		'やみのてんし',		sub{ $is_add_effect = 1; &_damages(260, '魔', 1); &_st_ds('眠り', '魔', 30);		}],
	);
}
sub skill_98 { # 超魔法型(ｱﾙﾃﾏ[map/10])
	return (
		[0,		44,		'こころないてんし',	sub{ my($y) = &_check_enemy(shift, '瀕死', '魔'); return if !$y; if ($ms{$y}{mhp}>999 || $ms{$y}{mdf}>999) { $com.="$yにはきかなかった！"; } else { $ms{$y}{hp}=1; $com.=qq|$yは<span class="st_down">生命力を失った</span>！|;; };	}],
		[0,		30,		'いてつくはどう',	sub{ for my $y (@members) { my $tten=$ms{$y}{ten}; &reset_status($y); $ms{$y}{ten}=$tten; }; $com.=qq|<span class="st_down">全ての効果がかき消された！</span>|;	}],
		[0,		30,		'カーバンクル',		sub{ return if &is_bad_state('魔'); $com.="＠ルビーの光＠"; for my $y (@partys) { next if $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '魔反撃'; $com.=qq|<span class="tmp">$yは魔法の壁に守られた！</span>|;};	}],
		[0,		23,		'マイティガード',	sub{ &_st_ups(0.5, '魔', 'df'); for my $y (@partys) { next if $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '魔軽減'; $com.=qq|<span class="tmp">$yは魔法の光で守られた！</span>|;};	}],
		[0,		44,		'かくせい',			sub{ $ms{$m}{tmp}='２倍'; &tenshon($m); &tenshon($m); 		}],
		[0,		44,		'こころないてんし',	sub{ my($y) = &_check_enemy(shift, '瀕死', '魔'); return if !$y; if ($ms{$y}{mhp}>999 || $ms{$y}{mdf}>999) { $com.="$yにはきかなかった！"; } else { $ms{$y}{hp}=1; $com.=qq|$yは<span class="st_down">生命力を失った</span>！|;; };	}],
		[0,		40,		'ブラッドレイン',	sub{ &_damages(200, '魔', 1); &_heals(200, '魔'); 	}],
		[0,		40,		'バブルボム',		sub{ for my $y (@enemys) { &_damage($y, 100, '息', 1); $com.="$yはあやしい液体がかかった！"; $ms{$y}{tmp}='２倍'; }; 	}],
		[0,		80,		'しっこくのほのお',	sub{ &_damages(350, '息', 1);	}],
		[0,		99,		'ダークメテオ',		sub{ my $v = int(rand(3)+4); for my $i (1..$v) { last if $ms{$m}{hp} <= 0; &_damage(undef, 250, '魔', 1); };	}],
		[0,		99,		'アルテマ',			sub{ &_damages(400, '魔', 1);	}],
	);
}
sub skill_99 { # にげだす
	return (
		[0,		0,	'にげだす',		sub{ $com.="$mは逃げ出した！"; $ms{$m}{hp} = 0;	}],
	);
}
sub skill_100 { # ﾄﾝﾍﾞﾘ
	return (
		[0,		99,		'みんなのうらみ',	sub{ &_damage(shift, $m{kill_m}*0.1, '攻', 1);	}],
		[0,		99,		'ほうちょう',		sub{ &_damage(shift, 666, '攻', 1);	}],
	);
}
sub skill_101 { # 暗黒竜(ﾀﾏｺﾞ)
	return (
		[0,		50,		'しょうかん',	sub{ if ($ms{$m}{icon} =~ /710/ && $ms{$m}{hp} < $ms{$m}{mhp} * 0.2) { $com.="なんと、タマゴにヒビが…！$mの封印が完全に解けてしまった！"; $ms{$m}{icon}='mon/712.gif'; $ms{$m}{job}=97; $ms{$m}{hp}=$ms{$m}{mhp}; $ms{$m}{mp}=int($ms{$m}{mmp}*0.1); for my $k (qw/at df ag/){ $ms{$m}{$k} = $ms{$m}{'m'.$k} = 600; }; } else { &_add_enemy }; 	}],
		[0,		50,		'しょうかん',	sub{ if ($ms{$m}{icon} =~ /710/ && $ms{$m}{hp} < $ms{$m}{mhp} * 0.1) { $com.="なんと、タマゴにヒビが…！$mの封印が完全に解けてしまった！"; $ms{$m}{icon}='mon/712.gif'; $ms{$m}{job}=97; $ms{$m}{hp}=$ms{$m}{mhp}; $ms{$m}{mp}=int($ms{$m}{mmp}*0.1); for my $k (qw/at df ag/){ $ms{$m}{$k} = $ms{$m}{'m'.$k} = 600; }; } else { &_add_enemy }; 	}],
	);
}

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ここまで。以下サブルーチン
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#=================================================
# ダメージ(to 敵)
#=================================================
sub _damages { # 敵全体
	my($v, $z, $is_direct) = @_;
	return if &is_bad_state($z);
	
	if (@enemys < 1) { # 敵全滅
		$mes = '戦う相手が見つかりません';
		return;
	}
	for my $y (@enemys) {
		last if $ms{$m}{hp} <= 0;
		&_damage($y, $v, $z, $is_direct);
		$v *= 0.85; # 並び順でダメージ減
	}
}
sub _damage { # 敵単体
	my($y, $v, $z, $is_direct) = &_check_enemy(@_);
	return if $mes;
	return unless $v;

	if ($ms{$y}{hp} <= 0) {
		$y = $m;
		$com .= "$mはわけもわからず自分を攻撃した！";
	}
	
	if ($z eq '攻' && ( $ms{$m}{hit} < rand(100) || &_is_exceed_ag($y, $m) ) ) {
		$com .= "ミス！$yはかわした！";
		$y = '';

		$ms{$m}{ten} = 1;
		return $y, 0;
	}
	else {
		my $y_df = $ms{$y}{df};
		$v *= $ms{$m}{ten};
		$v  = $v * 0.5 - ($ms{$y}{df} + $arms[$ms{$y}{arm}][3]) * 0.3 if !$is_direct || $ms{$y}{mdf} > 999;
		$v  = int($v * (rand(0.3)+0.9) );
		$v  = int(rand(2)+1) if $v < 1;

		$ms{$y}{hp} -= $v;
		$com .= qq|<b>$y</b>に <span class="damage">$v</span> のダメージ！|;
		$ms{$m}{ten} = 1;

		if ($ms{$y}{hp} <= 0) {
			$ms{$y}{hp} = 0;
			$com .= qq|<span class="die">$yをたおした！</span>|;
			&defeat($y); # 倒したときの処理
		}
	
		return $y, $v;
	}
}
sub _risk { # 反動ダメージ
	my $v = shift;
	
	return if $ms{$m}{hp} <= 0;

	$v = int($v + 1);
	$ms{$m}{hp} -= $v;
	$ms{$m}{hp}  = 1 if $ms{$m}{hp} <= 0;
	$com.=qq|$mは反動で <span class="damage">$v</span> のダメージをうけた！|;
}

#=================================================
# 回復(to 味方)
#=================================================
sub _heals { # 味方全体
	my($v, $z) = @_;
	return if &is_bad_state($z);
	for my $y (@partys) {
		&_heal($y, $v, $z);
	}
}
sub _heal { # 味方単体
	my($y, $v) = &_check_party(@_);
	return if $ms{$y}{hp} <= 0;
	return unless $v;

	$v = int($v * (rand(0.3)+0.9) * $ms{$m}{ten});
	$ms{$m}{ten} = 1;
	$ms{$y}{hp} += $v;
	$ms{$y}{hp}  = $ms{$y}{mhp} if $ms{$y}{hp} > $ms{$y}{mhp};
	$com .= qq|<b>$y</b>の$e2j{mhp}が <span class="heal">$v</span> 回復した！|;
	return 1;
}

#=================================================
# 魔力回復(to 味方)
#=================================================
sub _mp_hs { # 味方全体
	my($v, $z) = @_;
	return if &is_bad_state($z);
	for my $y (@partys) {
		&_mp_h($y, $v, $z);
	}
}
sub _mp_h { # 味方単体
	my($y, $v) = &_check_party(@_);
	return if $ms{$y}{hp} <= 0;
	return unless $v;

	$v = int($v * (rand(0.3)+0.9) * $ms{$m}{ten}) + 1;
	$ms{$m}{ten} = 1;
	$ms{$y}{mp} += $v;
	$ms{$y}{mp}  = $ms{$y}{mmp} if $ms{$y}{mp} > $ms{$y}{mmp};
	$com .= qq|<b>$y</b>の$e2j{mmp}が <span class="heal">$v</span> 回復した！|;
	return 1;
}

#=================================================
# 即死(to 敵)
#=================================================
sub _deaths { # 敵全体
	my($v, $z, $par) = @_;
	return if &is_bad_state($z);
	if (@enemys < 1) { # 敵全滅
		$mes = '戦う相手が見つかりません';
		return;
	}
	for my $y (@enemys) {
		&_death($y, $v, $z, $par);
	}
}
sub _death { # 敵単体
	my($y, $v, $z, $par) = &_check_enemy(@_);
	return if $ms{$y}{hp} <= 0;
	return if $mes;
	return unless $v;
	
	if ($ms{$y}{hp} > 999 || $ms{$y}{mdf} > 999) {
		return if $is_add_effect; # 追加効果の場合は非表示
		$com .= "$yにはきかなかった…";
	}
	elsif ($par >= rand(100)) {
		$com .= qq|<span class="die">$yは死んでしまった！</span>|;
		&defeat($y); # 倒したときの処理
	}
	else {
		return if $is_add_effect; # 追加効果の場合は非表示
		$com .= "$yはかわした！";
	}
}

#=================================================
# ステータスダウン(to 敵)
#=================================================
sub _st_downs { # 敵全体
	my($v, $z, $k) = @_;
	return if &is_bad_state($z);
	if (@enemys < 1) { # 敵全滅
		$mes = '戦う相手が見つかりません';
		return;
	}
	for my $y (@enemys) {
		&_st_down($y, $v, $z, $k);
	}
}
sub _st_down { # 敵単体
	my($y, $v, $z, $k) = &_check_enemy(@_);
	return if $ms{$y}{hp} <= 0;
	return if $mes;
	return unless $v;

	if ($ms{$y}{mdf} > 999 || ( ($k eq 'hp' || $k eq 'at') && $ms{$y}{hp} > 999) ) {
		return if $is_add_effect; # 追加効果の場合は非表示
		$com .= "$yにはきかなかった…";
		return;
	}
	elsif ($ms{$y}{$k} <= $ms{$y}{'m'.$k} * 0.2 || ($k eq 'hit' && $ms{$y}{$k} <= 50) ) {
		return if $is_add_effect; # 追加効果の場合は非表示
		$com .= "$yにはこれ以上効果がないようだ…";
		return;
	}
	
	$v = int($ms{$y}{$k} * $v * $ms{$m}{ten});
	$v = int(rand(50) + 100 * $ms{$m}{ten}) if $k eq 'mp' && $v > 150 * $ms{$m}{ten};
	$ms{$m}{ten} = 1;
	$ms{$y}{$k} -= $v;
	$ms{$y}{$k} = int($ms{$y}{'m'.$k} * 0.2) if $ms{$y}{$k} < $ms{$y}{'m'.$k} * 0.2;
	$ms{$y}{$k} = 50 if $k eq 'hit' && $ms{$y}{$k} < 50;
	$com .= qq|$yの<span class="st_down">$e2j{$k}が $v さがった！</span>|;
	return $y, $v;
}

#=================================================
# ステータスアップ(to 味方)
#=================================================
sub _st_ups { # 味方全体
	my($v, $z, $k) = @_;
	return if &is_bad_state($z);
	for my $y (@partys) {
		&_st_up($y, $v, $z, $k);
	}
}
sub _st_up { # 味方単体
	my($y, $v, $z, $k) = &_check_party(@_);
	return if $ms{$y}{hp} <= 0;
	return if $v <= 0;
	return unless $v;

	if ($ms{$y}{$k} >= $ms{$y}{'m'.$k} * 2.5) {
		return if $is_add_effect; # 追加効果の場合は非表示
		$com .= "$yにはこれ以上効果はないようだ…";
		return $y, $v;
	}
	
	$v = int($ms{$y}{'m'.$k} * $v * $ms{$m}{ten});
	$ms{$m}{ten} = 1;
	$ms{$y}{$k} += $v;
	$ms{$y}{$k} = int($ms{$y}{'m'.$k} * 2.5) if $ms{$y}{$k} > $ms{$y}{'m'.$k} * 2.5;
	$com .= qq|$yの<span class="st_up">$e2j{$k}が $v あがった！</span>|;
	return $y, $v;
}
#=================================================
# ステータス異常(to 敵)
#=================================================
sub _st_ds { # 敵全体
	my($v, $z, $par) = @_;
	return if &is_bad_state($z);
	if (@enemys < 1) { # 敵全滅
		$mes = '戦う相手が見つかりません';
		return;
	}
	for my $y (@enemys) {
		&_st_d($y, $v, $z, $par);
	}
}
sub _st_d { # 敵単体
	my($y, $v, $z, $par) = &_check_enemy(@_);
	return if $ms{$y}{hp} <= 0;
	return if $mes;
	return unless $v;
	
	if ($ms{$y}{mhp} > 999 || $ms{$y}{mdf} > 999) {
		return if $is_add_effect; # 追加効果の場合は非表示
		$com .= "$yにはきかなかった…";
	}
	elsif ($par > rand(100)) {
		$ms{$y}{state} = $v;
		$ms{$y}{ten} = 1; # 相手のテンションを戻す
		$com .= qq|<span class="state">$yの$e2j{state}が$vになりました！</span>|;
	}
	elsif (!$is_add_effect) { # 追加効果の場合は非表示
		$com .= "$yはかわした！";
	}
	return $y, $v;
}

#=================================================
# ステータス異常回復(to 味方)
#=================================================
sub _st_hs { # 味方全体
	my($v, $z) = @_;
	return if &is_bad_state($z);
	$is_add_effect = 1;
	for my $y (@partys) {
		&_st_h($y, $v, $z);
	}
}
sub _st_h { # 味方単体
	my($y, $v) = &_check_party(@_);
	return if $ms{$y}{hp} <= 0;
	return if $v eq '';
	return unless $v;
	
	# 状態異常と回復方法が同じ属性かどうか
	if ($ms{$y}{state} eq $v) {
		$com .= qq|<span class="heal">$yの$ms{$y}{state}が治りました！</span>|;
		$ms{$y}{state} = '';
	}
	elsif (!$is_add_effect) { # 追加効果の場合は非表示
		$com .= "$yには効果がないようだ…";
	}
	return $y, $v;
}

#=================================================
# 特殊効果　効果は１ターン
#=================================================
# $_[0]:相手名, $_[1]:ダメージ，$_[2]:属性
# return (相手，ダメージ)
my %tmps = (
	'かばう'	=> sub{ for my $name (@members) { next if $ms{$name}{tmp} ne 'かばい中'; next if $ms{$name}{color} ne $ms{$_[0]}{color}; $com.="$nameが$_[0]をかばった！"; return $name; }; return; },

	'大防御'	=> sub{ return if $_[1] !~ /^[0-9\-\.]+$/; return $_[0], $_[1]*0.1; },
	'防御'		=> sub{ return if $_[1] !~ /^[0-9\-\.]+$/; return $_[0], $_[1]*0.5; },
	'攻軽減'	=> sub{ return if $_[1] !~ /^[0-9\-\.]+$/ || $_[2] ne '攻'; return $_[0], $_[1]*0.25; },
	'魔軽減'	=> sub{ return if $_[1] !~ /^[0-9\-\.]+$/ || $_[2] ne '魔'; return $_[0], $_[1]*0.25; },
	'息軽減'	=> sub{ return if $_[1] !~ /^[0-9\-\.]+$/ || $_[2] ne '息'; return $_[0], $_[1]*0.25; },

	'２倍'		=> sub{ return if $_[1] !~ /^[0-9\-\.]+$/; return $_[0], $_[1]*2.0; },

	'攻反撃'	=> sub{ return if $_[2] ne '攻'; $com.=qq|$_[0]は<span class="tmp">攻撃をはね返した！</span>|;   return $m; },
	'魔反撃'	=> sub{ return if $_[2] ne '魔'; $com.=qq|$_[0]は<span class="tmp">魔法をはね返した！</span>|;   return $m; },
	'息反撃'	=> sub{ return if $_[2] ne '息'; $com.=qq|$_[0]は<span class="tmp">ブレスをはね返した！</span>|; return $m; },
	'踊反撃'	=> sub{ return if $_[2] ne '踊'; $com.=qq|$_[0]は<span class="tmp">踊り返した！</span>|;         return $m; },

	'受流し'	=> sub{ return if $_[2] ne '攻'; $com.=qq|$_[0]は<span class="tmp">受流した！</span>|; my $y = rand(2)<1 ? $partys[int(rand(@partys))] : $enemys[int(rand(@enemys))]; $com.="しかし、$_[0]は受流すのに失敗した！" if $_[0] eq $y; return $y; },

	'魔吸収'	=> sub{ return if $_[2] ne '魔'; my $v = $_[1] < 50 ? int(rand(20)+30) : int( $_[1] * (rand(0.3)+0.2) ); $com.=qq|$_[0]は$e2j{mp}を <span class="heal">$v</span> 吸収した！|; $ms{$_[0]}{mp} += $v; $ms{$_[0]}{mp} = $ms{$_[0]}{mmp} if $ms{$_[0]}{mp} > $ms{$_[0]}{mmp};return; },

	'攻無効'	=> sub{ return if $_[2] ne '攻'; $com.=qq|$_[0]は<span class="tmp">攻撃をうけつけない！</span>|; return $_[0], 0; },
	'魔無効'	=> sub{ return if $_[2] ne '魔'; $com.=qq|$_[0]は<span class="tmp">魔法をうけつけない！</span>|; return $_[0], 0; },
);

sub is_bad_state {
	my $z = shift;
	if ($z eq '魔' && $ms{$m}{state} eq '魔封') {
		if (rand(4)<1) {
			$com .= qq|<span class="heal">$mは魔法が使えるようになりました！</span>|;
			$ms{$m}{state} = '';
		}
		else {
			$com .= "しかし、$mは魔法が封じられていた";
			return 1;
		}
	}
	elsif ($z eq '踊' && $ms{$m}{state} eq '踊封') {
		if (rand(4)<1) {
			$com .= qq|<span class="heal">$mは踊れるようになりました！</span>|;
			$ms{$m}{state} = '';
		}
		else {
			$com .= "しかし、$mは踊りが封じられていた";
			return 1;
		}
	}
	elsif ($z eq '攻' && $ms{$m}{state} eq '攻封') {
		if (rand(4)<1) {
			$com .= qq|<span class="heal">$mは物理攻撃ができるようになりました！</span>|;
			$ms{$m}{state} = '';
		}
		else {
			$com .= "しかし、$mは物理攻撃が封じられていた";
			return 1;
		}
	}
	return 0;
}

#=================================================
# 味方チェック
#=================================================
sub _check_party {
	my($y, $v, $z, @etcs) = @_;
	
	return if &is_bad_state($z);
	
	if ($ms{$m}{state} eq '混乱') {
		$y = $members[int(rand(@members))];
	}
	else {
		# 指定なし or 敵の場合はランダムで味方を選択
		$y = $partys[int(rand(@partys))] if !defined($ms{$y}{name}) || $ms{$y}{color} ne $ms{$m}{color};
		$y = $m if $ms{$y}{hp} <= 0 && $v ne '蘇生';
	}
	
	# 特殊効果がある場合
	if ( $ms{$y}{tmp} && defined $tmps{ $ms{$y}{tmp} } ) {
		my($y2, $v2) = &{ $tmps{ $ms{$y}{tmp} } }($y, $v, $z);
		$y = $y2 if defined $y2;
		$v = $v2 if defined $v2;
	}
	
	return $y, $v, $z, @etcs;
}

#=================================================
# 敵チェック
#=================================================
sub _check_enemy {
	my($y, $v, $z, @etcs) = @_;
	
	# 敵全滅
	if (@enemys < 1) {
		$mes = '戦う相手が見つかりません';
		return;
	}
	return if &is_bad_state($z);
	
	if ($ms{$m}{state} eq '混乱') {
		$y = $members[int(rand(@members))] unless $m eq $y;
	}
	else {
		# 指定なし or 味方の場合はランダムで敵を選択
		$y = $enemys[int(rand(@enemys))] if !defined($ms{$y}{name}) || $ms{$y}{color} eq $ms{$m}{color};
		return if $ms{$y}{hp} <= 0;
	}
	
	# 特殊効果がある場合
	if ( $ms{$y}{tmp} && defined $tmps{ $ms{$y}{tmp} } ) {
		my($y2, $v2) = &{ $tmps{ $ms{$y}{tmp} } }($y, $v, $z);
		$y = $y2 if defined $y2;
		$v = $v2 if defined $v2;
	}
	return $y, $v, $z, @etcs;
}


#=================================================
# パルプンテ(to 全員)
#=================================================
sub _parupunte {
	if (rand(2)<1) { # 一時状態
		my @tmps = ('２倍','攻反撃','魔反撃','受流し');
		my $v = $tmps[int(rand(@tmps))];
		for my $y (@members) {
			next if $ms{$y}{hp} <= 0;
			$ms{$y}{tmp} = $v;
		}
		$com .= qq|なんと、<span class="tmp">全員の状態が $v になりました！</span>|;
	}
	elsif (rand(2)<1) { # 状態異常
		my @states = ('混乱','眠り','麻痺','猛毒');
		my $v = $states[int(rand(@states))];
		for my $y (@members) {
			next if $ms{$y}{hp} <= 0;
			$ms{$y}{state} = $v;
			$ms{$y}{ten} = 1;
		}
		$com .= qq|なんと、<span class="state">全員が $v 状態になりました！</span>|;
	}
	elsif (rand(2)<1) { # ＨＰ回復
		for my $y (@members) {
			next if $ms{$y}{mhp} > 999;
			$com.= qq|<span class="revive">$yが生き返った</span>| if $ms{$y}{hp} <= 0;
			$ms{$y}{hp} = $ms{$y}{mhp};
		}
		$com .= qq|<span class="heal">全員の$e2j{hp}が回復した！</span>|;
	}
	elsif (rand(3)<1) { # 素早さ0
		for my $y (@members) {
			$ms{$y}{ag} = 0;
		}
		$com .= qq|なんと、<span class="st_down">全員の体がなまりのように重くなった！</span>|;
	}
	elsif (rand(2)<1) { # 瀕死
		for my $y (@members) {
			next if $ms{$y}{hp} <= 0;
			next if $ms{$y}{hp} > 999;
			$ms{$y}{hp} = 1;
		}
		$com .= qq|なんと、空から流星が降りそそいだ！全員の<span class="damage">$e2j{mhp}が 1 </span>になった！|;
	}
	else { # 何もなし
		$com.= qq|………。しかし、何も起こらなかった…|;
	}
}

#=================================================
# ＠ゆびをふる
#=================================================
sub _yubiwofuru {
	my @r_skills = &{ 'skill_'.int(rand(@jobs)+1) };
	if (@r_skills <= 0) {
		$com .= "しかし、何も起こらなかった…";
		return;
	}
	my $i = int(rand(@r_skills));
	my $buf_mp = $ms{$m}{mp};
	&{ $r_skills[$i][3] };
	$ms{$m}{mp} = $buf_mp if $buf_mp > $ms{$m}{mp}; # メガンテ、メガザルなど全MP消費のスキルの場合は、強制的にMPが1になるので。
}

#=================================================
# 味方追加(身代わり、＠よびだす) 第一引数(名前)は必ず先頭に@をつける
#=================================================
sub _add_party {
	my %y_st;
	($y_st{name}, $y_st{icon}, $y_st{hp}, $y_st{mp}, $y_st{at}, $y_st{df}, $y_st{ag}) = @_;

	my $y = $y_st{name};
	for my $k (@battle_datas) {
		$ms{$y}{$k} = 0;
	}
	for my $k (qw/hp mp at df ag/) {
		$ms{$y}{$k} = $ms{$y}{'m'.$k} = int($y_st{$k}*(rand(0.3)+0.9));
	}
	$ms{$y}{icon} = $y_st{icon};
	$ms{$y}{hit} = 95;
	$ms{$y}{ten} = 1;
	$ms{$y}{name}  = $y;
	$ms{$y}{color} = $ms{$m}{color};
	$ms{$y}{tmp}   = '';
	$ms{$y}{state} = '';
	$ms{$y}{get_exp}   = int($m{lv} * 0.5);
	$ms{$y}{get_money} = int($m{lv} * 0.25);
	push @members, $y;
	push @partys,  $y;
}

#=================================================
# 敵追加(銀のたてごと、＠しょうかん)
#=================================================
sub _add_enemy {
	if ($win || @members >= 10) { # 闘技場、ギルド戦、10人以上
		$com .= "しかし、何も起こらなかった…";
		return;
	}
	
	require "$stagedir/$stage.cgi";

	my @alfas = ('I'..'Z'); # 同じ名前のモンスターを識別するために名前の後につけるもの
	my $i = int(rand(@alfas));
	
	my $no = @appears ? $appears[int(rand(@appears))] : int(rand(@monsters)); # 出現モンスター
	$no = 0 unless defined $monsters[$no]; # 存在しないNoだったら
	my $name = '@'.$monsters[$no]{name}.$alfas[$i];
	$name    = '@'.$monsters[$no]{name}.$alfas[$i-1] if defined $ms{$name}{name}; # すでに同じモンスター名がいたら
	
	if (defined $ms{$name}{name}) { # それでも同じモンスター名だったら
		$com .= "しかし、何も起こらなかった…";
		return;
	}
	
	for my $k (@battle_datas) {
		$ms{$name}{$k} = defined $monsters[$no]{$k} ? $monsters[$no]{$k} : 0;
	}
	
	# 初期データセット(読み込んだデータにすでに値がある場合はそっちを優先)
	for my $k (qw/hp mp at df ag/) {
		$ms{$name}{$k} = int($ms{$name}{$k} * (1 + (@partys - 2) * 0.05) ); # パーティー人数による強さ補正
		$ms{$name}{'m'.$k} ||= $ms{$name}{$k};
	}
	$ms{$name}{name}  = $name;
	$ms{$name}{color} = $npc_color;
	$ms{$name}{hit}   ||= 95;
	$ms{$name}{ten}   ||= 1;
	$ms{$name}{tmp}   ||= '';
	$ms{$name}{state} ||= '';
	
	$com .= qq|<span class="revive">$nameがあらわれた！</span>|;
	push @members, $name;
	if ($ms{$m}{color} eq $npc_color) {
		push @partys, $name;
	}
	else {
		push @enemys, $name;
	}
}

# 仲間の現職業画像が召喚系とマッチしているか
sub _search_job {
	my $icon_no = shift;
	for my $y (@partys) {
		next if $y eq $m;
		next if $ms{$y}{icon} =~ /mix/;
		return $y if $ms{$y}{icon} =~ m|^job/$icon_no|;
	}
	return;
}


1; # 削除不可
