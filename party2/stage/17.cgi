# 宝の中身
@treasures = (
[1..39], # 武器No
[1..39], # 防具No
[1..109,125..126,130..134], # 道具No
);

# ボス
@bosses= (
	{
		name		=> '人食い箱',
		hp			=> 1000,
		at			=> 350,
		df			=> 50,
		ag			=> 400,
		get_exp		=> 200,
		get_money	=> 400,
		icon		=> 'mon/090.gif',
		
		old_sp		=> 20,
		job			=> 92, # 眠り系
		sp			=> 999,
		mp			=> 500,
		tmp			=> '２倍', 
	},
	{
		name		=> 'ミミック',
		hp			=> 1500,
		at			=> 360,
		df			=> 100,
		ag			=> 700,
		get_exp		=> 400,
		get_money	=> 800,
		icon		=> 'mon/091.gif',
		
		hit			=> 150, # 長期戦用命中率150%
		old_sp		=> 20,
		job			=> 93, # 即死
		sp			=> 999,
		mp			=> 500,
		tmp			=> '２倍', 
	},
	{
		name		=> 'パンドラボックス',
		hp			=> 2000,
		at			=> 370,
		df			=> 150,
		ag			=> 800,
		get_exp		=> 600,
		get_money	=> 1000,
		icon		=> 'mon/092.gif',
		
		hit			=> 150, # 長期戦用命中率150%
		old_sp		=> 20,
		job			=> 93, # 即死
		sp			=> 999,
		mp			=> 999,
		tmp			=> '２倍', 
	},
	{
		name		=> 'トラップボックス',
		hp			=> 2500,
		at			=> 380,
		df			=> 200,
		ag			=> 900,
		get_exp		=> 800,
		get_money	=> 2000,
		icon		=> 'mon/575.gif',

		hit			=> 200, # 長期戦用命中率150%
		job			=> 19, # 闇魔道士
		sp			=> 999,
		old_job		=> 93, # 即死
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '２倍', 
	},
);

# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = ();


# モンスター
@monsters = (
	{ # 0
		hit			=> 70,
		name		=> 'コロヒーロー',
		hp			=> 270,
		at			=> 300,
		df			=> 150,
		ag			=> 150,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/100.gif',

		old_sp		=> 20,
		job			=> 34, # 勇者
		sp			=> 999,
		mp			=> 200,
	},
	{ # 1
		hit			=> 70,
		name		=> 'コロファイター',
		hp			=> 280,
		at			=> 320,
		df			=> 250,
		ag			=> 50,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/101.gif',

		old_sp		=> 20,
		job			=> 1, # 戦士
		sp			=> 999,
		mp			=> 100,
	},
	{ # 2
		hit			=> 70,
		name		=> 'コロマージ',
		hp			=> 240,
		at			=> 150,
		df			=> 100,
		ag			=> 300,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/102.gif',

		job			=> 6, # 魔法使い
		sp			=> 999,
		mp			=> 400,
	},
	{ # 3
		hit			=> 70,
		name		=> 'コロプリースト',
		hp			=> 250,
		at			=> 200,
		df			=> 150,
		ag			=> 200,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/103.gif',

		job			=> 5, # 僧侶
		sp			=> 999,
		mp			=> 300,
	},
	{ # 4
		name		=> 'プチヒーロー',
		hp			=> 320,
		at			=> 280,
		df			=> 150,
		ag			=> 150,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/105.gif',

		old_sp		=> 20,
		job			=> 34, # 勇者
		sp			=> 999,
		mp			=> 250,
	},
	{ # 5
		name		=> 'プチファイター',
		hp			=> 340,
		at			=> 320,
		df			=> 250,
		ag			=> 50,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/106.gif',

		old_sp		=> 20,
		job			=> 1, # 戦士
		sp			=> 999,
		mp			=> 150,
	},
	{ # 6
		name		=> 'プチマージ',
		hp			=> 250,
		at			=> 150,
		df			=> 100,
		ag			=> 300,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/107.gif',

		job			=> 6, # 魔法使い
		sp			=> 999,
		mp			=> 300,
	},
	{ # 7
		name		=> 'プチプリースト',
		hp			=> 270,
		at			=> 200,
		df			=> 150,
		ag			=> 200,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/108.gif',

		job			=> 5, # 僧侶
		sp			=> 999,
		mp			=> 250,
	},
);



1;
