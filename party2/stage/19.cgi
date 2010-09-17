# 宝の中身
@treasures = (
[25..39], # 武器No
[25..39], # 防具No
[4..6,12,21..23,28,29,36,39,40,60..71,88..109], # 道具No
);

# ボス
@bosses= (
	{
		name		=> '封印のﾂﾎﾞ',
		hp			=> 15000,
		at			=> 450,
		df			=> 400,
		ag			=> 200,
		get_exp		=> 1000,
		get_money	=> 100,
		icon		=> 'mon/585.gif',
		
		hit			=> 500, # 長期戦用命中率250%
		job			=> 95, # 召喚
		sp			=> 999,
		job			=> 95, # 召喚
		old_sp		=> 999,
		mmp			=> 15000,
		mp			=> 5000,
		tmp			=> '魔無効',
	},
);

# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = ();


# モンスター
@monsters = (
	{ # 0
		name		=> '封印石',
		hp			=> 400,
		at			=> 400,
		df			=> 400,
		ag			=> 150,
		get_exp		=> 100,
		get_money	=> 100,
		icon		=> 'mon/180.gif',
		
		job			=> 93, # 即死ザキ
		sp			=> 999,
		mp			=> 200,
		tmp			=> '攻無効',
	},
	{ # 1
		name		=> '封印石',
		hp			=> 400,
		at			=> 400,
		df			=> 400,
		ag			=> 150,
		get_exp		=> 100,
		get_money	=> 100,
		icon		=> 'mon/181.gif',
		
		job			=> 92, # 眠り系
		sp			=> 999,
		mp			=> 200,
		tmp			=> '魔無効',
	},
	{ # 2
		name		=> '封印石',
		hp			=> 400,
		at			=> 400,
		df			=> 400,
		ag			=> 150,
		get_exp		=> 100,
		get_money	=> 100,
		icon		=> 'mon/182.gif',
		
		job			=> 91, # 麻痺系
		sp			=> 999,
		mp			=> 200,
		tmp			=> '魔無効',
	},
);



1;
