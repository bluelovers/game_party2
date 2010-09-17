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

sub event_5 { return if $event =~ /5/; $event .= '5'; $npc_com.=qq|<br /><span class="strong">←Yes【宝箱が大好きだ】No→</span>|; }
sub event_A { return if $event =~ /A|B/; $event .= 'A'; if (rand(5)<1) { &_add_treasure; } else { &get_boss_data1; &add_boss; };  }
sub event_B { return if $event =~ /A|B/; $event .= 'B'; if (rand(3)<1) { &add_boss; } else { &_add_monster; }; }

sub event_6 { return if $event =~ /6/; $event .= '6'; $npc_com.=qq|<br /><span class="strong">←Yes【強い敵と戦いたい】No→</span>|; }
sub event_C { return if $event =~ /C|D/; $event .= 'C'; &add_boss; }
sub event_D { return if $event =~ /C|D/; $event .= 'D'; if (rand(3)<1) { &_add_monster; } else { $npc_com.= "<b>！！！！？</b>ｶﾞﾗｶﾞﾗｶﾞﾗｯ！頭上から大きな岩が落ちてきた！"; &_trap_d(120); }; }

sub event_7 { return if $event =~ /7/; $event .= '7'; $npc_com.=qq|<br /><span class="strong">←Yes【猫より犬派だ】No→</span>|; }
sub event_E { return if $event =~ /E|F/; $event .= 'E'; &get_boss_data2; &add_boss; }
sub event_F { return if $event =~ /E|F/; $event .= 'F'; &get_boss_data3; &add_boss; }


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

sub get_boss_data2 {
	@bosses = (
		{
			name		=> 'ﾁﾋﾞﾍﾞﾛｽA',
			hp			=> 160,
			at			=> 160,
			df			=> 90,
			ag			=> 260,
			get_exp		=> 32,
			get_money	=> 15,
			icon		=> 'mon/203.gif',
			old_sp		=> 20,
		},
		{
			name		=> 'ｹﾙﾍﾞﾛｽ',
			hp			=> 300,
			at			=> 300,
			df			=> 100,
			ag			=> 100,
			get_exp		=> 48,
			get_money	=> 22,
			icon		=> 'mon/204.gif',
	
			old_sp		=> 20,
			job			=> 29, # 時魔道士スロウ、ヘイスト
			sp			=> 20,
			mp			=> 53,
		},
		{
			name		=> 'ﾁﾋﾞﾍﾞﾛｽB',
			hp			=> 160,
			at			=> 160,
			df			=> 90,
			ag			=> 260,
			get_exp		=> 32,
			get_money	=> 15,
			icon		=> 'mon/203.gif',
			old_sp		=> 20,
		},
	);
}
sub get_boss_data3 {
	@bosses = (
		{
			name		=> 'ﾍﾞﾋﾞｰﾊﾟﾝｻｰA',
			hp			=> 150,
			at			=> 180,
			df			=> 50,
			ag			=> 300,
			get_exp		=> 30,
			get_money	=> 18,
			icon		=> 'mon/206.gif',
			old_sp		=> 20,
		},
		{
			name		=> 'ｷﾗｰﾊﾟﾝｻｰ',
			hp			=> 340,
			at			=> 300,
			df			=> 30,
			ag			=> 120,
			get_exp		=> 50,
			get_money	=> 20,
			icon		=> 'mon/207.gif',
	
			old_sp		=> 20,
			job			=> 21, # 狂戦士たいあたり、うけながし、おたけび
			sp			=> 20,
			mp			=> 79,
		},
		{
			name		=> 'ﾍﾞﾋﾞｰﾊﾟﾝｻｰB',
			hp			=> 150,
			at			=> 180,
			df			=> 50,
			ag			=> 300,
			get_exp		=> 30,
			get_money	=> 18,
			icon		=> 'mon/206.gif',
			old_sp		=> 20,
		},
	);
}



1; # 削除不可
