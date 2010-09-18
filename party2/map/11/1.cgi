# 最大ターン
$max_round = 30;

# マップ
@maps = (
	[2,3,4],
	[1,0,1],
	[1,0,1],
	[0,A,0],
	[1,0,1],
	[1,0,1],
	[H,B,H],
	[1,0,1],
	[1,0,1],
	[H,C,H],
	[1,0,1],
	[1,0,1],
	[H,D,H],
	[1,0,1],
	[1,0,1],
	[H,E,H],
	[1,0,1],
	[1,0,1],
	[H,F,H],
	[1,0,1],
	[1,0,1],
	[1,S,1],
);

# イベント
$map_imgs{2} = '宝' if $event !~ /2/;
$map_imgs{3} = '宝' if $event !~ /3/;
$map_imgs{4} = '宝' if $event !~ /4/;
sub event_2 { return if $event =~ /2/; $event .= '2'; my $_s = int(rand(9)+13); require "$stagedir/$_s.cgi"; &_add_treasure; }
sub event_3 { return if $event =~ /3/; $event .= '3'; my $_s = int(rand(9)+13); require "$stagedir/$_s.cgi"; &_add_treasure; }
sub event_4 { return if $event =~ /4/; $event .= '4'; my $_s = int(rand(9)+13); require "$stagedir/$_s.cgi"; &_add_treasure; }

$map_imgs{A} = '◎' if $event !~ /A/;
$map_imgs{B} = '◎' if $event !~ /B/;
$map_imgs{C} = '◎' if $event !~ /C/;
$map_imgs{D} = '◎' if $event !~ /D/;
$map_imgs{E} = '◎' if $event !~ /E/;
$map_imgs{F} = '◎' if $event !~ /F/;#17
sub event_A { return if $event =~ /A/; $event .= 'A';  $npc_com.="ただならぬ気配を感じる…。どうやら、このダンジョンのボスのようだ！<br />"; &get_boss_data; &add_boss; }
sub event_B { return if $event =~ /B/; $event .= 'B'; require "$stagedir/20.cgi"; &add_boss; }
sub event_C { return if $event =~ /C/; $event .= 'C'; require "$stagedir/17.cgi"; &add_boss; }
sub event_D { return if $event =~ /D/; $event .= 'D'; require "$stagedir/11.cgi"; &add_boss; }
sub event_E { return if $event =~ /E/; $event .= 'E'; require "$stagedir/9.cgi"; &add_boss; }
sub event_F { return if $event =~ /F/; $event .= 'F'; require "$stagedir/8.cgi"; &add_boss; }
sub event_H {
	return if $event =~ /H/;
	$npc_com.="テーブルの上に何やらあやしげな薬や高度な医学書が散らばっている…";
	if ($m{job} eq '43') {
		$event .= 'H';
		$npc_com.="$mは本に書いてあることを解読し回復薬を作り出した！全員のＨＰとＭＰが回復した！";
		for my $y (@partys) {
			$ms{$y}{hp} = $ms{$y}{mhp};
			$ms{$y}{mp} = $ms{$y}{mmp};
		}
	}
}


sub get_boss_data {
	@bosses= (
		{
			name		=> '死の炎A',
			hp			=> 6666,
			at			=> 666,
			df			=> 222,
			ag			=> 999,
			get_exp		=> 333,
			get_money	=> 222,
			icon		=> 'mon/695.gif',
			
			job			=> 93, # 即死
			sp			=> 999,
			old_job		=> 41, # ドラゴン
			old_sp		=> 999,
			mp			=> 999,
			tmp			=> '魔吸収',
		},
		{
			name		=> 'ルシファー',
			hp			=> 15000,
			at			=> 650,
			df			=> 200,
			ag			=> 900,
			get_exp		=> 2000,
			get_money	=> 500,
			icon		=> 'mon/704.gif',
			
			hit			=> 400, # 長期戦用命中率
			job			=> 98, # 超魔法型
			sp			=> 999,
			mmp			=> 9999999,
			mp			=> 99999,
			ten			=> 8,
		},
		{
			name		=> '死の炎B',
			hp			=> 6666,
			at			=> 666,
			df			=> 222,
			ag			=> 999,
			get_exp		=> 333,
			get_money	=> 222,
			icon		=> 'mon/695.gif',
			
			job			=> 35, # 魔王
			sp			=> 999,
			old_job		=> 51, # 光魔道士
			old_sp		=> 999,
			mp			=> 999,
			tmp			=> '魔吸収',
		},
	);
}

# モンスター
@appears = ();
@monsters = (
	{
		name		=> '爆弾王',
		hp			=> 300,
		at			=> 500,
		df			=> 400,
		ag			=> 50,
		get_exp		=> 150,
		get_money	=> 30,
		icon		=> 'mon/579.gif',

		job			=> 94, # 自爆メガンテ、ねる
		sp			=> 20,
		mp			=> 42,
	},
	{
		name		=> 'ビックボム',
		hp			=> 600,
		at			=> 400,
		df			=> 200,
		ag			=> 200,
		get_exp		=> 120,
		get_money	=> 50,
		icon		=> 'mon/577.gif',

		job			=> 31, # 青魔道士じばく
		sp			=> 20,
		mp			=> 42,
	},
	{
		name		=> 'キラーボム',
		hp			=> 250,
		at			=> 500,
		df			=> 250,
		ag			=> 100,
		get_exp		=> 110,
		get_money	=> 50,
		icon		=> 'mon/209.gif',

		job			=> 94, # 自爆メガンテ
		sp			=> 10,
		mp			=> 42,
	},
	{
		name		=> 'チビボム',
		hp			=> 100,
		at			=> 50,
		df			=> 600,
		ag			=> 900,
		get_exp		=> 50,
		get_money	=> 1,
		icon		=> 'mon/208.gif',

		job			=> 94, # 自爆メガンテ
		sp			=> 10,
		mp			=> 42,
		tmp			=> '魔無効',
	},
	{
		name		=> 'トンベリ',
		hp			=> 300,
		at			=> 500,
		df			=> 200,
		ag			=> 200,
		get_exp		=> 180,
		get_money	=> 99,
		icon		=> 'mon/599.gif',

		job			=> 100, # トンベリ
		sp			=> 999,
		mp			=> 161,
	},
);



1; # 削除不可
