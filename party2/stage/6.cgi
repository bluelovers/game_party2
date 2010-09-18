# 宝の中身
@treasures = (
[7..18], # 武器No
[2..11], # 防具No
[16..26,43,72..86], # 道具No
);

# ボス
@bosses= (
	{
		name		=> 'ギガンテス',
		hp			=> 2500,
		at			=> 200,
		df			=> 20,
		ag			=> 20,
		get_exp		=> 200,
		get_money	=> 5,
		icon		=> 'mon/563.gif',
		
		old_sp		=> 20,
		hit			=> 150, # 長期戦用命中率150%
		job			=> 21, # 狂戦士
		sp			=> 60,
		mp			=> 60,
		state		=> '眠り',
		tmp			=> '２倍',
	},
);

# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = (0,0,0,0,1,1,1,1,2,2,2,3,3,3,3,4,4,4,4,5,5,5,6,6,7,7,8,8,9,9,10,10,11);


# モンスター
@monsters = (
	{ # 0
		name		=> 'マージマタンゴ',
		hp			=> 80,
		at			=> 65,
		df			=> 65,
		ag			=> 80,
		get_exp		=> 23,
		get_money	=> 18,
		icon		=> 'mon/032.gif',

		job			=> 90, # どくこうげき
		sp			=> 999,
		mp			=> 39,
	},
	{ # 1
		name		=> 'キングコブラ',
		hp			=> 100,
		at			=> 85,
		df			=> 35,
		ag			=> 60,
		get_exp		=> 21,
		get_money	=> 8,
		icon		=> 'mon/054.gif',
		old_sp		=> 20,
	},
	{ # 2
		name		=> 'レッドアイ',
		hp			=> 80,
		at			=> 50,
		df			=> 30,
		ag			=> 40,
		get_exp		=> 24,
		get_money	=> 10,
		icon		=> 'mon/074.gif',

		job			=> 42, # アサシンコンフェ
		sp			=> 15,
		mp			=> 61,
	},
	{ # 3
		name		=> 'ダークアイ',
		hp			=> 70,
		at			=> 60,
		df			=> 30,
		ag			=> 50,
		get_exp		=> 28,
		get_money	=> 11,
		icon		=> 'mon/075.gif',

		job			=> 42, # 闇魔道士ルカナンマホカンタメダパニ
		sp			=> 16,
		mp			=> 71,
	},
	{ # 4
		name		=> 'モヒカント',
		hp			=> 160,
		at			=> 120,
		df			=> 50,
		ag			=> 35,
		get_exp		=> 27,
		get_money	=> 14,
		icon		=> 'mon/210.gif',

		old_sp		=> 20,
		job			=> 10, # 羊使いねる、スカラ、たいあたり
		sp			=> 10,
		mp			=> 22,
		state		=> '眠り',
	},
	{ # 5
		name		=> 'ベビーパンサー',
		hp			=> 90,
		at			=> 75,
		df			=> 25,
		ag			=> 125,
		get_exp		=> 18,
		get_money	=> 12,
		icon		=> 'mon/206.gif',
		old_sp		=> 20,
	},
	{ # 6
		name		=> 'キラーパンサー',
		hp			=> 130,
		at			=> 105,
		df			=> 30,
		ag			=> 74,
		get_exp		=> 30,
		get_money	=> 10,
		icon		=> 'mon/207.gif',

		old_sp		=> 20,
		job			=> 21, # 狂戦士たいあたり、うけながし、おたけび
		sp			=> 20,
		mp			=> 19,
	},
	{ # 7
		hit			=> 70,
		name		=> 'ニョロロ',
		hp			=> 75,
		at			=> 96,
		df			=> 20,
		ag			=> 80,
		get_exp		=> 28,
		get_money	=> 26,
		icon		=> 'mon/229.gif',

		job			=> 37, # 結界士マホトーン
		sp			=> 5,
		mp			=> 34,
	},
	{ # 8
		name		=> 'ラフレシア',
		hp			=> 95,
		at			=> 86,
		df			=> 27,
		ag			=> 40,
		get_exp		=> 30,
		get_money	=> 26,
		icon		=> 'mon/230.gif',

		job			=> 20, # 悪魔さそうおどり、レディウィップ、マジックバリア、あまいいき、メダパニダンス
		sp			=> 26,
		mp			=> 44,
	},
	{ # 9
		name		=> 'モサモサ',
		hp			=> 100,
		at			=> 60,
		df			=> 40,
		ag			=> 70,
		get_exp		=> 15,
		get_money	=> 100,
		icon		=> 'mon/512.gif',

		job			=> 45, # モーグリおまじない、ストップ、ウールガード、かえるのうた
		sp			=> 100,
		mp			=> 59,
	},
	{ # 10
		name		=> 'デスローパー',
		hp			=> 80,
		at			=> 90,
		df			=> 80,
		ag			=> 60,
		get_exp		=> 32,
		get_money	=> 16,
		icon		=> 'mon/514.gif',

		job			=> 38, # バンパイアきゅうけつアスピル
		sp			=> 20,
		mp			=> 20,
	},
	{ # 11
		name		=> 'サンダーシープ',
		hp			=> 150,
		at			=> 70,
		df			=> 50,
		ag			=> 20,
		get_exp		=> 50,
		get_money	=> 50,
		icon		=> 'mon/513.gif',

		old_sp		=> 30,
		job			=> 34, # 勇者かばうライデイン
		sp			=> 30,
		mp			=> 50,
	},
);



1;
