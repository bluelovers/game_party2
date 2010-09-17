# ダンジョン名
$d_name = "$dungeons[$stage]１階";

# 最大ターン
$max_round = 30;

# マップ
@maps = (
	[0,F,0],
	[0,0,0],
	[0,A,0],
	[1,0,1],
	[1,0,1],
	[1,0,1],
	[1,S,1],
);


# イベント
$map_imgs{F} = '凸';
$map_imgs{A} = '◎' if $event !~ /A/;
sub event_F { for my $y (@partys) { $ms{$y}{state} = '攻封' }; $map="_1"; $npc_com.="$p_nameは次の階へと進んだ…"; }
sub event_0 { for my $y (@partys) { $ms{$y}{state} = '攻封' }; return if rand(2) > 1; &add_monster; } # 道
sub event_A { for my $y (@partys) { $ms{$y}{state} = '攻封' }; return if $event =~ /A/; $event .= 'A'; &add_boss; } # ボス


# 敵と宝の設定
require "$mapdir/10/_data.cgi";

# ボス
@bosses= (
	{
		name		=> '闇の魔術士',
		hp			=> 8000,
		at			=> 300,
		df			=> 100,
		ag			=> 400,
		get_exp		=> 750,
		get_money	=> 250,
		icon		=> 'mon/510.gif',
		job			=> 40, # ﾊｸﾞﾚﾒﾀﾙメラミ
		sp			=> 50,
		old_job		=> 58, # ﾀﾞｰｸｴﾙﾌ
		old_sp		=> 999,
		mmp			=> 9999,
		mp			=> 999,
		tmp			=> '魔吸収',
	},
	{
		name		=> '魔法使い',
		hp			=> 1200,
		at			=> 250,
		df			=> 80,
		ag			=> 210,
		get_exp		=> 150,
		get_money	=> 30,
		icon		=> 'mon/061.gif',
		job			=> 6, # 魔法使い
		sp			=> 999,
		old_job		=> 48, # 堕天使
		old_sp		=> 160,
		mp			=> 542,
	},
	{
		name		=> 'ｽﾗｲﾑまどう',
		hp			=> 1300,
		at			=> 220,
		df			=> 50,
		ag			=> 300,
		get_exp		=> 160,
		get_money	=> 25,
		icon		=> 'mon/013.gif',
		job			=> 19, # 闇魔道士
		sp			=> 999,
		old_job		=> 40, # ﾊｸﾞﾚﾒﾀﾙ
		old_sp		=> 999,
		mp			=> 384,
	},
);


1; # 削除不可
