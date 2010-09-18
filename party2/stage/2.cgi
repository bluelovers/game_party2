# 宝の中身
@treasures = (
[5..14], # 武器No
[4..10], # 防具No
[0,10,11,14,15,10,11,14..25,41,42,78..84], # 道具No
);

# ボス
@bosses= (
	{
		name		=> '亡霊剣士',
		hp			=> 1000,
		at			=> 60,
		df			=> 20,
		ag			=> 50,
		get_exp		=> 160,
		get_money	=> 50,
		icon		=> 'mon/500.gif',
		
		hit			=> 150, # 長期戦用命中率150%
		job			=> 2, # 剣士しっぷうぎり、みねうち
		sp			=> 10,
		mp			=> 45,
		
		tmp			=> '攻反撃',
	},
);

# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = (0,0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,7,8);


# モンスター
@monsters = (
	{ # 0
		name		=> 'ゴースト',
		hp			=> 20,
		at			=> 36,
		df			=> 20,
		ag			=> 30,
		get_exp		=> 7,
		get_money	=> 4,
		icon		=> 'mon/035.gif',
	},
	{ # 1
		name		=> 'メイジゴースト',
		hp			=> 26,
		at			=> 32,
		df			=> 26,
		ag			=> 36,
		get_exp		=> 12,
		get_money	=> 6,
		icon		=> 'mon/036.gif',

		job			=> 6, # 魔法使いメラ,ルカニ,ギラ
		sp			=> 8,
		mp			=> 35,
	},
	{ # 2
		name		=> 'シャドー',
		hp			=> 21,
		at			=> 20,
		df			=> 35,
		ag			=> 44,
		get_exp		=> 11,
		get_money	=> 5,
		icon		=> 'mon/046.gif',

		job			=> 41, # ドラゴンつめたいいき
		sp			=> 10,
		mp			=> 33,
	},
	{ # 3
		name		=> 'ミイラ男',
		hp			=> 50,
		at			=> 40,
		df			=> 6,
		ag			=> 16,
		get_exp		=> 10,
		get_money	=> 7,
		icon		=> 'mon/040.gif',
		
		job			=> 9, # 盗賊ピエラボミエ
		sp			=> 6,
		mp			=> 37,
	},
	{ # 4
		name		=> 'ガイコツ剣士',
		hp			=> 45,
		at			=> 50,
		df			=> 15,
		ag			=> 20,
		get_exp		=> 12,
		get_money	=> 6,
		icon		=> 'mon/043.gif',
		
		job			=> 2, # 剣士しんくうぎり、みねうち
		sp			=> 10,
		mp			=> 20,
	},
	{ # 5
		name		=> 'ナイトウィスプ',
		hp			=> 25,
		at			=> 30,
		df			=> 25,
		ag			=> 35,
		get_exp		=> 9,
		get_money	=> 5,
		icon		=> 'mon/070.gif',
		
		job			=> 19, # 闇魔道士ルカナン
		sp			=> 4,
		mp			=> 45,
	},
	{ # 6
		name		=> 'チビベロス',
		hp			=> 41,
		at			=> 31,
		df			=> 8,
		ag			=> 61,
		get_exp		=> 8,
		get_money	=> 4,
		icon		=> 'mon/203.gif',
	},
	{ # 7
		name		=> 'パンプキン',
		hp			=> 65,
		at			=> 55,
		df			=> 20,
		ag			=> 14,
		get_exp		=> 16,
		get_money	=> 8,
		icon		=> 'mon/039.gif',
	},
	{ # 8
		name		=> '人食い箱',
		hp			=> 120,
		at			=> 55,
		df			=> 10,
		ag			=> 200,
		get_exp		=> 30,
		get_money	=> 50,
		icon		=> 'mon/090.gif',
		
		job			=> 92, # 眠り系
		sp			=> 30,
		mp			=> 42,
		tmp			=> '２倍', 
	},
);



1;
