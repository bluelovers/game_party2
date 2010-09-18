require "./lib/_battle.cgi";
require "./lib/_npc_action.cgi";
#=================================================
# 冒険(VS モンスター) Created by Merino
#=================================================

%map_imgs = (
	0	=> '□', # 道
	1	=> '■', # 壁
	'm'	=> '●', # 自分
);

@npc_skills = (
	[0,	0,	'こうげき',		sub{ &kougeki	}],
#	[0,	0,	'ぼうぎょ',		sub{ $ms{$m}{tmp} = '防御'; $com.="$mは身を固めている";	}],
);

#=================================================
# タイトル、背景画像
#=================================================
sub get_header_data {
	require "$mapdir/$stage/$map.cgi";
	$bgimg = "$bgimgdir/map$stage.gif"; # 背景画像
	$d_name ||= $dungeons[$stage];
	$this_title = "$d_name 限界ターン <b>$round</b>/<b>$max_round</b>";
}
#=================================================
# 追加アクション
#=================================================
sub add_battle_action {
	if ($round eq '0') {
		push @actions, 'すすむ';
		$actions{'すすむ'} = [0, sub{ &susumu }];
	}
	elsif (@enemys <= 0) {
		push @actions, ('にし','きた','みなみ','ひがし','ちず');
		$actions{'にし'}   = [0,	sub{ &nishi }];
		$actions{'きた'}   = [0,	sub{ &kita }];
		$actions{'みなみ'} = [0,	sub{ &minami }];
		$actions{'ひがし'} = [0,	sub{ &higashi }];
		$actions{'ちず'}   = [0,	sub{ $m{job} eq '9' || $m{job} eq '26' || $m{job} eq '27' ? &chizu(2) : &chizu(); }];
	}
	elsif ($enemys[0] =~ /^\@.+宝箱.$/) {
		$is_npc_action = 0;
		push @actions, 'しらべる';
		$actions{'しらべる'} = [0,	sub{ &shiraberu }];
	}
}
sub susumu {
	if ($round < 1 && $leader ne $m) {
		$mes = "一番始めの ＠すすむ をすることができるのはリーダーのみです";
		return;
	}
	&reset_status_all;
	++$round;
	&auto_reload;
}

#=================================================
# ＠にし＠きた＠みなみ＠ひがし
#=================================================
sub kita    { &_susumu('北', $py-1, $px)   }
sub minami  { &_susumu('南', $py+1, $px)   }
sub higashi { &_susumu('東', $py,   $px+1) }
sub nishi   { &_susumu('西', $py,   $px-1) }
sub _susumu {
	my($name, $y, $x) = @_;
	$is_npc_action = 0;
	if (@enemys > 0 && $event ne '宝') {
		$mes .= "※敵を全て倒すまで、先に進むことはできません";
		return;
	}
	elsif ($round >= $max_round) {
		$mes .= "※行動限界値を超えました。これ以上は動けません。＠にげるで解散してください";
		return;
	}
	elsif ($y < 0 || $x < 0 || !defined $maps[$y][$x] || $maps[$y][$x] eq '1') {
		my @tekitos = ('＞＜','＞o＜','＞_＜','＝.＝','×_×','×o×','×.×','￣◇￣;','￣□￣;');
		my $face = $tekitos[int rand @tekitos];
		$com .= "$m は壁にぶつかった！$face";
		$ms{$m}{state} = $face;
		&event_1;
		return;
	}
	&reset_status_all;
	++$round;
	$px = $x;
	$py = $y;

	$npc_com .= "$p_nameは $nameへと進みました…";
	&{'event_' .$maps[$py][$px] };
	&chizu();
	&auto_reload;
}

sub event_0 { return if rand(2) > 1; &add_monster(); } # 道
sub event_1 { return } # 壁
sub event_S { return } # スタート地点
sub event_B { return if $event =~ /B/; $event .= 'B'; $npc_com.="ただならぬ気配を感じる…。どうやら、このダンジョンのボスのようだ！<br />"; &add_boss } # ボス

#=================================================
# ＠ちず
#=================================================
sub chizu {
	my $v = shift || 1;
	$com .= '<br />';
	for my $y (-$v .. $v) {
		for my $x (-$v .. $v) {
			$com .= $y eq '0' && $x eq '0' ? $map_imgs{m} # 自分の位置 
				  : $py+$y < 0 || $px+$x < 0 || !defined $maps[$py+$y][$px+$x] ? $map_imgs{1} # Mapに存在しない部分は壁
				  : !defined $map_imgs{$maps[$py+$y][$px+$x]} eq '1' ? $map_imgs{0} # MapImgsに存在しない部分は道
				  :          $map_imgs{$maps[$py+$y][$px+$x]};
		}
		$com .= '<br />';
	}
}

# ＠ダンジョン用の宝の数
sub _add_treasure {
	&add_treasure();
}

# ＠ダンジョン用の敵の数
sub _add_monster {
	&add_monster();
}


# 味方全体ワナダメージ
sub _trap_d {
	my $d = shift;
	for my $y (@partys) {
		my $v = int($d * (rand(0.3)+0.9));
		$npc_com .= qq|<b>$y</b>に <span class="damage">$v</span> のダメージ！|;
		$ms{$y}{hp} -= $v;
		if ($ms{$y}{hp} <= 0) {
			$ms{$y}{hp} = 0;
			$npc_com .= qq!<span class="die">$yは倒れた！</span>!;
		}
	}
}


1; # 削除不可
