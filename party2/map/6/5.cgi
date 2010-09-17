# 最大ターン
$max_round = 30;

# マップ
@maps = (
	[2,0,3],
	[1,X,1],
	[1,0,1],
	[0,0,0],
	[A,1,B],
	[0,5,0],
	[1,0,1],
	[1,0,1],
	[0,0,0],
	[C,1,D],
	[0,6,0],
	[1,0,1],
	[1,0,1],
	[0,0,0],
	[E,1,F],
	[0,7,0],
	[1,0,1],
	[1,S,1],
);

# イベント
$map_imgs{X} = '◎' if $event !~ /X/;
$map_imgs{2} = '宝' if $event !~ /2/;
$map_imgs{3} = '宝' if $event !~ /3/;
sub event_X { return if $event =~ /X/; $event .= 'X'; $npc_com.="ただならぬ気配を感じる…。どうやら、このダンジョンのボスのようだ！<br />"; &add_boss } # ボス
sub event_2 { return if $event =~ /2/; $event .= '2'; &_add_treasure; }
sub event_3 { return if $event =~ /3/; $event .= '3'; &_add_treasure; }

sub event_5 { return if $event =~ /5/; $event .= '5'; $npc_com.=qq|<br /><span class="strong">←小さい【立て札】大きい→</span>|; }
sub event_A { return if $event =~ /A|B/; $event .= 'A'; if (rand(3)<1) { &get_monster_data1; &_add_monster; } else { &get_monster_data2; &_add_monster; };  }
sub event_B { return if $event =~ /A|B/; $event .= 'B'; if (rand(7)<1) { &get_monster_data3; &_add_monster; } else { &get_monster_data4; &_add_monster; };  }

sub event_6 { return if $event =~ /6/; $event .= '6'; $npc_com.=qq|<br /><span class="strong">←全員【立て札】１人→</span>|; }
sub event_C { return if $event =~ /C|D/; $event .= 'C'; if (rand(3)<1) { $npc_com.= "<b>！！！！？</b>床に描かれている魔法陣が反応した！"; &_heals(rand(100), '無'); } else { $npc_com.= "<b>！！！！？</b>ｶﾞﾗｶﾞﾗｶﾞﾗｯ！頭上から大きな岩が落ちてきた！"; &_trap_d(120); };  }
sub event_D { return if $event =~ /C|D/; $event .= 'D'; if (rand(3)<1) { &_trap_d(rand(200)); } else { &_heals(rand(100), '無'); };  }

sub event_7 { return if $event =~ /7/; $event .= '7'; $npc_com.=qq|<br /><span class="strong">←宝【立て札】お金→</span>|; }
sub event_E { return if $event =~ /E|F/; $event .= 'E'; if (rand(5)<1) { &_add_treasure; } else { &get_boss_data1; &add_boss; };  }
sub event_F { return if $event =~ /E|F/; $event .= 'F'; if (rand(3)<1) { my $v = int(rand(2000)); $m{money}+=$v; $npc_com.="$mは ${v}G 拾った！"; } else { my $v = int(rand(2000)); $m{money}-=$v; $npc_com.="$mは ${v}G 落としてしまった！"; $m{money}-=0 if $m{money} < 0; };   }


# 敵と宝の設定
require "$mapdir/6/_data.cgi";


sub get_boss_data1 {
	@bosses = (
		{
			name		=> '人食い箱',
			hp			=> 500,
			at			=> 250,
			df			=> 35,
			ag			=> 400,
			get_exp		=> 50,
			get_money	=> 100,
			icon		=> 'mon/090.gif',
			job			=> 92, # 眠り系
			sp			=> 30,
			mp			=> 42,
			tmp			=> '２倍', 
		},
		{
			name		=> 'ﾐﾐｯｸ',
			hp			=> 700,
			at			=> 280,
			df			=> 65,
			ag			=> 600,
			get_exp		=> 60,
			get_money	=> 150,
			icon		=> 'mon/091.gif',
			job			=> 93, # 即死
			sp			=> 10,
			mp			=> 68,
			tmp			=> '２倍', 
		},
		{
			name		=> 'ﾊﾟﾝﾄﾞﾗﾎﾞｯｸｽ',
			hp			=> 900,
			at			=> 300,
			df			=> 95,
			ag			=> 800,
			get_exp		=> 100,
			get_money	=> 500,
			icon		=> 'mon/092.gif',
			job			=> 93, # 即死
			sp			=> 20,
			mp			=> 69,
			tmp			=> '２倍', 
		},
	);
}
sub get_monster_data1 {
	@monsters = (
		{
			name		=> 'ﾒﾀﾙｽﾗｲﾑ',
			hp			=> 8,
			at			=> 70,
			df			=> 2500,
			ag			=> 1500,
			get_exp		=> 250,
			get_money	=> 10,
			icon		=> 'mon/004.gif',
			job			=> 39, # スライムギラ
			sp			=> 3,
			old_job		=> 99, # 逃げる
			old_sp		=> 0,
			mp			=> 31,
			tmp			=> '魔無効',
		},
	);
}
sub get_monster_data2 {
	@monsters = (
		{
			name		=> 'ｽﾗｲﾑ',
			hp			=> 500,
			at			=> 200,
			df			=> 100,
			ag			=> 500,
			get_exp		=> 50,
			get_money	=> 30,
			icon		=> 'mon/002.gif',
			job			=> 40, # ﾊｸﾞﾚﾒﾀﾙ
			sp			=> 999,
			old_sp		=> 20,
			mp			=> 149,
		},
	);
}
sub get_monster_data3 {
	@monsters = (
		{
			name		=> 'ﾒﾀﾙｷﾝｸﾞ',
			hp			=> 25,
			at			=> 200,
			df			=> 6000,
			ag			=> 2000,
			get_exp		=> 4000,
			get_money	=> 100,
			icon		=> 'mon/517.gif',
			job			=> 40, # ﾊｸﾞﾚﾒﾀﾙ
			sp			=> 999,
			old_job		=> 99, # 逃げる
			old_sp		=> 0,
			mp			=> 299,
			tmp			=> '魔無効',
		},
	);
}
sub get_monster_data4 {
	@monsters = (
		{
			name		=> 'ｷﾝｸﾞｽﾗｲﾑ',
			hp			=> 2000,
			at			=> 250,
			df			=> 150,
			ag			=> 120,
			get_exp		=> 200,
			get_money	=> 200,
			icon		=> 'mon/516.gif',
			old_sp		=> 20,
			hit			=> 150, # 長期戦用命中率150%
			job			=> 21, # 狂戦士たいあたり
			sp			=> 5,
			mp			=> 400,
			tmp			=> '攻無効',
		},
	);
}



1; # 削除不可
