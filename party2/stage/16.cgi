# 宝の中身
@treasures = (
[15..25], # 武器No
[15..25], # 防具No
[16..26,16..26,27,35,57,58,75..87,109], # 道具No
);


# ボス
@bosses= (
	{
		name		=> 'ﾒﾀﾙｷﾝｸﾞA',
		hp			=> 25,
		at			=> 200,
		df			=> 8000,
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
	{
		name		=> 'ｺﾞｰﾙﾃﾞﾝｽﾗｲﾑ',
		hp			=> 10,
		at			=> 300,
		df			=> 15000,
		ag			=> 8000,
		get_exp		=> 5000,
		get_money	=> 10000,
		icon		=> 'mon/590.gif',

		job			=> 40, # ﾊｸﾞﾚﾒﾀﾙ
		sp			=> 999,
		old_job		=> 99, # 逃げる
		old_sp		=> 0,
		mp			=> 399,
		tmp			=> '魔無効',
	},
	{
		name		=> 'ﾒﾀﾙｷﾝｸﾞB',
		hp			=> 25,
		at			=> 200,
		df			=> 8000,
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

# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = (0,0,0,0,1,1,2);

# モンスター
@monsters = (
	{ # 0
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
	{ # 1
		name		=> 'ﾊｸﾞﾚﾒﾀﾙ',
		hp			=> 14,
		at			=> 110,
		df			=> 4000,
		ag			=> 2000,
		get_exp		=> 1500,
		get_money	=> 30,
		icon		=> 'mon/022.gif',

		job			=> 40, # ﾊｸﾞﾚﾒﾀﾙメラミ
		sp			=> 25,
		old_job		=> 99, # 逃げる
		old_sp		=> 0,
		mp			=> 61,
		tmp			=> '魔無効',
	},
	{ # 2
		name		=> 'ﾒﾀﾙｷﾝｸﾞ',
		hp			=> 25,
		at			=> 200,
		df			=> 8000,
		ag			=> 2000,
		get_exp		=> 4000,
		get_money	=> 100,
		icon		=> 'mon/517.gif',

		job			=> 40, # ﾊｸﾞﾚﾒﾀﾙ
		sp			=> 999,
		old_job		=> 99, # 逃げる
		old_sp		=> 0,
		mp			=> 199,
		tmp			=> '魔無効',
	},
);



1;
