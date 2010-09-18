# 宝の中身
@treasures = (
[8..20], # 武器No
[6..16], # 防具No
[0,3..4,15..26,41..43,43,43,72..86], # 道具No
);

# ボス
@bosses= (
	{
		name		=> '闇の魔術士',
		hp			=> 1400,
		at			=> 70,
		df			=> 20,
		ag			=> 100,
		get_exp		=> 180,
		get_money	=> 120,
		icon		=> 'mon/510.gif',
		
		hit			=> 150, # 長期戦用命中率150%
		job			=> 40, # ハグレメタルメラミ
		sp			=> 25,
		mp			=> 250,
		tmp			=> '魔軽減',
	},
	{ # 1
		name		=> '魔法使い',
		hp			=> 144,
		at			=> 50,
		df			=> 45,
		ag			=> 76,
		get_exp		=> 24,
		get_money	=> 9,
		icon		=> 'mon/061.gif',

		job			=> 6, # 魔法使いメラ、ルカニ、ギラ、マヌーサ
		sp			=> 14,
		mp			=> 72,
	},
	{ # 2
		name		=> 'スライムまどう',
		hp			=> 160,
		at			=> 45,
		df			=> 30,
		ag			=> 100,
		get_exp		=> 26,
		get_money	=> 8,
		icon		=> 'mon/013.gif',

		job			=> 19, # 闇魔道士ルカナン,マホカンタ,メダパニ
		sp			=> 16,
		mp			=> 84,
	},
);

# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = (0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,8,9);

# モンスター
@monsters = (
	{ # 0
		name		=> 'まどうし',
		hp			=> 55,
		at			=> 45,
		df			=> 40,
		ag			=> 70,
		get_exp		=> 18,
		get_money	=> 6,
		icon		=> 'mon/060.gif',

		job			=> 39, # スライムギラ
		sp			=> 3,
		mp			=> 66,
	},
	{ # 1
		name		=> '魔法使い',
		hp			=> 67,
		at			=> 40,
		df			=> 45,
		ag			=> 76,
		get_exp		=> 20,
		get_money	=> 9,
		icon		=> 'mon/061.gif',

		job			=> 6, # 魔法使いメラ、ルカニ、ギラ、マヌーサ
		sp			=> 14,
		mp			=> 90,
	},
	{ # 2
		name		=> 'スライムまどう',
		hp			=> 70,
		at			=> 35,
		df			=> 30,
		ag			=> 100,
		get_exp		=> 19,
		get_money	=> 8,
		icon		=> 'mon/013.gif',

		job			=> 19, # 闇魔道士ルカナン,マホカンタ,メダパニ
		sp			=> 16,
		mp			=> 104,
	},
	{ # 3
		name		=> 'デビルエッグ',
		hp			=> 66,
		at			=> 66,
		df			=> 66,
		ag			=> 66,
		get_exp		=> 11,
		get_money	=> 6,
		icon		=> 'mon/065.gif',

		old_sp		=> 30,
		job			=> 7, # 商人まもりをかためる、ゴールドハンマー
		sp			=> 10,
		mp			=> 66,
	},
	{ # 4
		name		=> 'ミニデーモン',
		hp			=> 124,
		at			=> 64,
		df			=> 35,
		ag			=> 110,
		get_exp		=> 15,
		get_money	=> 6,
		icon		=> 'mon/066.gif',

		job			=> 8, # 遊び人
		sp			=> 26,
		mp			=> 16,
		state		=> '混乱',
	},
	{ # 5
		name		=> 'おおめだま',
		hp			=> 90,
		at			=> 78,
		df			=> 55,
		ag			=> 60,
		get_exp		=> 21,
		get_money	=> 8,
		icon		=> 'mon/077.gif',

		job			=> 19, # 闇魔道士ルカナン,マホカンタ,メダパニ
		sp			=> 16,
		mp			=> 34,
	},
	{ # 6
		name		=> 'スペクテッド',
		hp			=> 100,
		at			=> 65,
		df			=> 50,
		ag			=> 64,
		get_exp		=> 20,
		get_money	=> 11,
		icon		=> 'mon/078.gif',

		job			=> 37, # 結界士マホトーン、アストロン、おどりふうじ、マジックバリア、マホカンタ
		sp			=> 50,
		mp			=> 44,
	},
	{ # 8
		name		=> 'ビックドラキー',
		hp			=> 180,
		at			=> 98,
		df			=> 10,
		ag			=> 180,
		get_exp		=> 40,
		get_money	=> 8,
		icon		=> 'mon/258.gif',

		job			=> 37, # ドラゴンつめたいいき,こおりのいき
		sp			=> 30,
		mp			=> 24,
		state		=> '混乱',
	},
	{ # 9
		name		=> 'ミミック',
		hp			=> 300,
		at			=> 100,
		df			=> 30,
		ag			=> 300,
		get_exp		=> 50,
		get_money	=> 100,
		icon		=> 'mon/091.gif',
		
		job			=> 93, # 即死
		sp			=> 10,
		mp			=> 68,
		tmp			=> '２倍', 
	},
	{ # 10
		name		=> 'メタルスライム',
		hp			=> 8,
		at			=> 40,
		df			=> 1500,
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
);



1;
