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
$map_imgs{3} = '宝' if $event !~ /3/;;
$map_imgs{4} = '宝' if $event !~ /4/;;
sub event_2 { return if $event =~ /2/; $event .= '2'; my $_s = int(rand(8)+14); require "$stagedir/$_s.cgi"; &_add_treasure; }
sub event_3 { return if $event =~ /3/; $event .= '3'; my $_s = int(rand(8)+14); require "$stagedir/$_s.cgi"; &_add_treasure; }
sub event_4 { return if $event =~ /4/; $event .= '4'; my $_s = int(rand(8)+14); require "$stagedir/$_s.cgi"; &_add_treasure; }

$map_imgs{A} = '◎' if $event !~ /A/;
$map_imgs{B} = '◎' if $event !~ /B/;
$map_imgs{C} = '◎' if $event !~ /C/;
$map_imgs{D} = '◎' if $event !~ /D/;
$map_imgs{E} = '◎' if $event !~ /E/;
$map_imgs{F} = '◎' if $event !~ /F/;
sub event_A { return if $event =~ /A/; $event .= 'A'; $npc_com.="さきほどより強いパワーを感じる…。<br />"; &get_boss_data2; &add_boss; }
sub event_B { return if $event =~ /B/; $event .= 'B'; $npc_com.="ただならぬ気配を感じる…。どうやら、このダンジョンのボスのようだ！<br />"; &get_boss_data; &add_boss; }
sub event_C { return if $event =~ /C/; $event .= 'C'; require "$stagedir/13.cgi"; &add_boss; }
sub event_D { return if $event =~ /D/; $event .= 'D'; require "$stagedir/18.cgi"; &add_boss; }
sub event_E { return if $event =~ /E/; $event .= 'E'; require "$stagedir/12.cgi"; &add_boss; }
sub event_F { return if $event =~ /F/; $event .= 'F'; require "$stagedir/10.cgi"; &add_boss; }
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
			name		=> '竜の右目',
			hp			=> 6000,
			at			=> 500,
			df			=> 400,
			ag			=> 900,
			get_exp		=> 300,
			get_money	=> 300,
			icon		=> 'mon/588.gif',
			
			job			=> 41, # ドラゴン
			sp			=> 999,
			old_job		=> 90, # 猛毒系
			old_sp		=> 999,
			mp			=> 999,
			tmp			=> '受流し',
		},
		{
			name		=> 'ディアボロス',
			hp			=> 14000,
			at			=> 600,
			df			=> 200,
			ag			=> 200,
			get_exp		=> 2000,
			get_money	=> 500,
			icon		=> 'mon/650.gif',
			
			hit			=> 400, # 長期戦用命中率400%
			job			=> 97, # 超攻撃型
			sp			=> 999,
			mmp			=> 30000,
			mp			=> 8000,
			tmp			=> '魔無効',
		},
		{
			name		=> '竜の左目',
			hp			=> 6000,
			at			=> 500,
			df			=> 400,
			ag			=> 900,
			get_exp		=> 300,
			get_money	=> 300,
			icon		=> 'mon/589.gif',
			
			job			=> 41, # ドラゴン
			sp			=> 999,
			old_job		=> 91, # 麻痺系
			old_sp		=> 999,
			mp			=> 999,
			tmp			=> '受流し',
		},
	);
}
sub get_boss_data2 {
	@bosses= (
		{
			name		=> '片翼の天使',
			hp			=> 12000,
			at			=> 500,
			df			=> 300,
			ag			=> 300,
			get_exp		=> 3000,
			get_money	=> 2000,
			icon		=> 'mon/569.gif',
			
			hit			=> 500, # 長期戦用命中率
			job			=> 98, # 超魔法型
			sp			=> 999,
			old_job		=> 48, # 堕天使
			old_sp		=> 999,
			mmp			=> 30000,
			mp			=> 8000,
			tmp			=> '魔無効',
		},
		{
			name		=> 'ディアボロス',
			hp			=> 15000,
			at			=> 750,
			df			=> 300,
			ag			=> 700,
			get_exp		=> 5000,
			get_money	=> 1000,
			icon		=> 'mon/651.gif',
			
			hit			=> 500, # 長期戦用命中率
			job			=> 97, # 超攻撃型
			old_job		=> 38, # バンパイア
			old_sp		=> 999,
			sp			=> 999,
			mmp			=> 30000,
			mp			=> 8000,
			ten			=> 8,
		},
		{
			name		=> 'ボマー',
			hp			=> 9000,
			at			=> 600,
			df			=> 500,
			ag			=> 200,
			get_exp		=> 1000,
			get_money	=> 1,
			icon		=> 'mon/652.gif',
			
			hit			=> 500, # 長期戦用命中率
			job			=> 95, # 召喚
			sp			=> 999,
			old_job		=> 8, # 遊び人
			old_sp		=> 999,
			mp			=> 999,
			state		=> '大爆発',
			tmp			=> 'するぞ',
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
