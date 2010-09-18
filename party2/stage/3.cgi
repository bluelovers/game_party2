# 宝の中身
@treasures = (
[3..12], # 武器No
[6..17], # 防具No
[0,10,11,10,11,14..25,41,42,72,78..84], # 道具No
);

# ボス
@bosses= (
	{
		name		=> 'キラーシェル',
		hp			=> 450,
		at			=> 90,
		df			=> 90,
		ag			=> 30,
		get_exp		=> 100,
		get_money	=> 150,
		icon		=> 'mon/215.gif',
		
		hit			=> 150, # 長期戦用命中率150%
		job			=> 1, # 戦士かぶとわり、かばう、ちからをためる
		sp			=> 30,
		mp			=> 50,
		tmp			=> '魔反撃',
	},
	{
		name		=> 'デビルシェル',
		hp			=> 1000,
		at			=> 60,
		df			=> 50,
		ag			=> 30,
		get_exp		=> 120,
		get_money	=> 200,
		icon		=> 'mon/506.gif',
		
		hit			=> 150, # 長期戦用命中率150%
		job			=> 5, # 僧侶スカラ、キアリー、ホイミ、バギ
		sp			=> 12,
		mp			=> 100,
		tmp			=> '魔反撃',
	},
);

# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = ();


# モンスター
@monsters = (
	{ # 0
		name		=> 'ホイミスライム',
		hp			=> 50,
		at			=> 30,
		df			=> 15,
		ag			=> 50,
		get_exp		=> 14,
		get_money	=> 5,
		icon		=> 'mon/010.gif',

		job			=> 5, # 僧侶スカラ、キアリー、ホイミ
		sp			=> 6,
		mp			=> 45,
	},
	{ # 1
		name		=> 'しびれクラゲ',
		hp			=> 60,
		at			=> 36,
		df			=> 18,
		ag			=> 35,
		get_exp		=> 13,
		get_money	=> 6,
		icon		=> 'mon/012.gif',

		job			=> 91, # まひこうげき、しびれうち
		sp			=> 20,
		mp			=> 31,
	},
	{ # 2
		name		=> 'スライムつむり',
		hp			=> 40,
		at			=> 20,
		df			=> 80,
		ag			=> 20,
		get_exp		=> 16,
		get_money	=> 9,
		icon		=> 'mon/015.gif',

		job			=> 39, # スライムギラスクルト
		sp			=> 7,
		mp			=> 43,
	},
	{ # 3
		hit			=> 70,
		name		=> 'メイジドラキー',
		hp			=> 54,
		at			=> 40,
		df			=> 20,
		ag			=> 75,
		get_exp		=> 14,
		get_money	=> 6,
		icon		=> 'mon/026.gif',

		job			=> 39, # スライムギラ
		sp			=> 4,
		mp			=> 59,
	},
	{ # 4
		name		=> '亀戦士',
		hp			=> 48,
		at			=> 64,
		df			=> 70,
		ag			=> 5,
		get_exp		=> 13,
		get_money	=> 4,
		icon		=> 'mon/217.gif',

		old_sp		=> 30,
		job			=> 1, # 戦士かぶとわり、かばう
		sp			=> 10,
		mp			=> 15,
	},
	{ # 5
		name		=> 'チビイエティ',
		hp			=> 64,
		at			=> 46,
		df			=> 15,
		ag			=> 80,
		get_exp		=> 7,
		get_money	=> 3,
		icon		=> 'mon/200.gif',
	},
	{ # 6
		name		=> 'イエティ',
		hp			=> 150,
		at			=> 78,
		df			=> 25,
		ag			=> 22,
		get_exp		=> 20,
		get_money	=> 8,
		icon		=> 'mon/201.gif',

		job			=> 10, # 羊飼いねる、スカラ、たいあたり
		sp			=> 10,
		mp			=> 24,
		state		=> '眠り', 
	},
);



1;
