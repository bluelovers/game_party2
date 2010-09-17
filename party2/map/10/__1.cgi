# ダンジョン名
$d_name = "$dungeons[$stage]３階";

# 最大ターン
$max_round = 30;

# マップ
@maps = (
	[2,3,4],
	[0,0,0],
	[0,C,0],
	[1,0,1],
	[1,0,1],
	[1,0,1],
	[1,0,1],
);


# イベント
$map_imgs{2} = '宝' if $event !~ /2/;
$map_imgs{3} = '宝' if $event !~ /3/;
$map_imgs{4} = '宝' if $event !~ /4/;
$map_imgs{C} = '◎' if $event !~ /C/;
sub event_2 { for my $y (@partys) { $ms{$y}{state} = '攻封' }; return if $event =~ /2/; $event .= '2'; &_add_treasure; }
sub event_3 { for my $y (@partys) { $ms{$y}{state} = '攻封' }; return if $event =~ /3/; $event .= '3'; &_add_treasure; }
sub event_4 { for my $y (@partys) { $ms{$y}{state} = '攻封' }; return if $event =~ /4/; $event .= '4'; &_add_treasure; }
sub event_0 { for my $y (@partys) { $ms{$y}{state} = '攻封' }; return if rand(2) > 1; &_add_monster; } # 道
sub event_C { for my $y (@partys) { $ms{$y}{state} = '攻封' }; return if $event =~ /C/; $event .= 'C'; $npc_com.="ただならぬ気配を感じる…。どうやら、このダンジョンのボスのようだ！<br />"; &add_boss; } # ボス


# 敵と宝の設定
require "$mapdir/10/_data.cgi";

# ボス
@bosses= (
	{
		name		=> '精霊',
		hp			=> 5000,
		at			=> 300,
		df			=> 200,
		ag			=> 800,
		get_exp		=> 500,
		get_money	=> 700,
		icon		=> 'mon/661.gif',
		job			=> 58, # ﾀﾞｰｸｴﾙﾌ
		sp			=> 999,
		old_job		=> 48, # 堕天使
		old_sp		=> 160,
		mmp			=> 99999,
		mp			=> 9999,
	},
	{
		name		=> 'ｱﾙﾃﾏ',
		hp			=> 8000,
		at			=> 400,
		df			=> 400,
		ag			=> 999,
		get_exp		=> 3000,
		get_money	=> 2500,
		icon		=> 'mon/660.gif',
		hit			=> 500, # 長期戦用命中率
		job			=> 98, # 超魔法型
		sp			=> 999,
		mmp			=> 99999,
		mp			=> 9999,
		tmp			=> '魔無効',
	},
	{
		name		=> '魔玉',
		hp			=> 5000,
		at			=> 300,
		df			=> 600,
		ag			=> 900,
		get_exp		=> 666,
		get_money	=> 666,
		icon		=> 'mon/697.gif',
		job			=> 95, # 召喚
		sp			=> 999,
		old_job		=> 31, # 青魔道士
		old_sp		=> 999,
		mmp			=> 99999,
		mp			=> 9999,
	},
);


1; # 削除不可
