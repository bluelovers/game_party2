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
	[C,1,1],
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
$map_imgs{C} = '■' if $event !~ /C/;
sub event_X { return if $event =~ /X/; $event .= 'X'; $npc_com.="ただならぬ気配を感じる…。どうやら、このダンジョンのボスのようだ！<br />"; &add_boss } # ボス
sub event_2 { return if $event =~ /2/; $event .= '2'; &_add_treasure; }
sub event_3 { return if $event =~ /3/; $event .= '3'; &_add_treasure; }

sub event_5 { return if $event =~ /5/; $event .= '5'; $npc_com.=qq|<br /><span class="strong">←ボス【立て札】宝→</span>|; }
sub event_A { return if $event =~ /A|B/; $event .= 'A'; &add_boss; }
sub event_B { return if $event =~ /A|B/; $event .= 'B'; if (rand(6)<1) { &_add_treasure; } else { &get_boss_data1; &add_boss; }; }

sub event_6 { return if $event =~ /6/; $event .= '6'; $npc_com.=qq|<br /><span class="strong">←壁【立て札】行き止まり→</span>|; }
sub event_C { return if $event =~ /C|D/; $event .= 'C'; $npc_com .= "なんと！壁ではなく隠し通路になっていた！"; }
sub event_D { return if $event =~ /C|D/; $event .= 'D'; }

sub event_7 { return if $event =~ /7/; $event .= '7'; $npc_com.=qq|<br /><span class="strong">←実力【立て札】運→</span>|; }
sub event_E { return if $event =~ /E|F/; $event .= 'E'; if (rand(2)<1) { &add_boss; } else { &add_monster; }; }
sub event_F { return if $event =~ /E|F/; $event .= 'F'; if (rand(2)<1) { $npc_com.= "<b>！！！！？</b>ｶﾞﾗｶﾞﾗｶﾞﾗｯ！頭上から大きな岩が落ちてきた！"; &_trap_d(120); } else { $npc_com.= "<b>！！！！？</b>頭上から大きな岩が落ちてきた！…$mたちはかろうじてかわすことができた！"; };		 }


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



1; # 削除不可
