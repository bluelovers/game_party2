# ダンジョン名
$d_name = "$dungeons[$stage]２階";

# 最大ターン
$max_round = 30;

# マップ
@maps = (
	[1,0,1],
	[1,0,1],
	[1,0,1],
	[1,0,1],
	[0,B,0],
	[0,0,0],
	[0,F,0],
);


# イベント
$map_imgs{F} = '凸';
$map_imgs{B} = '◎' if $event !~ /B/;
sub event_F { for my $y (@partys) { $ms{$y}{state} = '攻封' }; $map="__1"; $npc_com.="$p_nameは次の階へと進んだ…"; }
sub event_0 { for my $y (@partys) { $ms{$y}{state} = '攻封' }; return if rand(2) > 1; &add_monster; } # 道
sub event_B { for my $y (@partys) { $ms{$y}{state} = '攻封' }; return if $event =~ /B/; $event .= 'B'; &add_boss; } # ボス


# 敵と宝の設定
require "$mapdir/10/_data.cgi";

# ボス
@bosses= (
	{
		name		=> 'ﾋﾞｯｸﾞﾎﾞﾑA',
		hp			=> 1200,
		at			=> 450,
		df			=> 120,
		ag			=> 150,
		get_exp		=> 255,
		get_money	=> 50,
		icon		=> 'mon/577.gif',
		job			=> 31, # 青魔道士じばく
		sp			=> 20,
		mp			=> 142,
	},
	{
		name		=> 'ひくいどり',
		hp			=> 9800,
		at			=> 660,
		df			=> 210,
		ag			=> 310,
		get_exp		=> 1200,
		get_money	=> 300,
		icon		=> 'mon/530.gif',
		hit			=> 300, # 長期戦用命中率
		job			=> 26, # 忍者
		sp			=> 999,
		old_job		=> 27, # 風水師
		old_sp		=> 999,
		mmp			=> 9999,
		mp			=> 797,
		tmp			=> '魔無効',
	},
	{
		name		=> 'ﾋﾞｯｸﾞﾎﾞﾑB',
		hp			=> 1200,
		at			=> 450,
		df			=> 120,
		ag			=> 150,
		get_exp		=> 255,
		get_money	=> 50,
		icon		=> 'mon/577.gif',
		job			=> 31, # 青魔道士じばく
		sp			=> 20,
		mp			=> 142,
	},
);


1; # 削除不可
