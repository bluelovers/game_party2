# 宝の中身
@treasures = (
[5..15], # 武器No
[8..20], # 防具No
[0,2,3,3,14..26,72,73,78..84], # 道具No
);

# ボス
@bosses= (
	{
		name		=> 'ゴーレム',
		hp			=> 1500,
		at			=> 100,
		df			=> 60,
		ag			=> 50,
		get_exp		=> 150,
		get_money	=> 100,
		icon		=> 'mon/546.gif',
		
		old_sp		=> 20,
		hit			=> 150, # 長期戦用命中率150%
		job			=> 27, # 風水士すなけむり
		sp			=> 10,
		mp			=> 77,
		tmp			=> '攻軽減',
	},
);

# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = (0,0,0,1,1,1,2,2,3,4,4,5,5,6,6,7,7,8,9);


# モンスター
@monsters = (
	{ # 0
		name		=> 'マッドハンド',
		hp			=> 70,
		at			=> 85,
		df			=> 36,
		ag			=> 50,
		get_exp		=> 10,
		get_money	=> 8,
		icon		=> 'mon/063.gif',

		job			=> 95, # しょうかん
		sp			=> 10,
		mp			=> 50,
	},
	{ # 1
		name		=> 'おおさそり',
		hp			=> 34,
		at			=> 76,
		df			=> 130,
		ag			=> 45,
		get_exp		=> 11,
		get_money	=> 9,
		icon		=> 'mon/052.gif',

		old_sp		=> 30, # テンション、防御
		job			=> 91, # まひこうげき
		sp			=> 10,
		mp			=> 19,
	},
	{ # 2
		name		=> 'ボム',
		hp			=> 50,
		at			=> 50,
		df			=> 60,
		ag			=> 50,
		get_exp		=> 15,
		get_money	=> 10,
		icon		=> 'mon/071.gif',

		old_sp		=> 30, # テンション、防御
		job			=> 20, # 青魔道士じばく
		sp			=> 10,
		mp			=> 42,
	},
	{ # 3
		name		=> 'まどうし',
		hp			=> 55,
		at			=> 35,
		df			=> 30,
		ag			=> 70,
		get_exp		=> 16,
		get_money	=> 6,
		icon		=> 'mon/060.gif',

		job			=> 39, # スライムギラ
		sp			=> 3,
		mp			=> 66,
	},
	{ # 4
		name		=> 'サボテンダー',
		hp			=> 100,
		at			=> 70,
		df			=> 50,
		ag			=> 150,
		get_exp		=> 20,
		get_money	=> 5,
		icon		=> 'mon/058.gif',

		job			=> 14, # 踊り子みかわしきゃく,ふしぎなおどり,うけながし
		sp			=> 16,
		mp			=> 50,
	},
	{ # 5
		name		=> 'アカテンダー',
		hp			=> 100,
		at			=> 70,
		df			=> 50,
		ag			=> 150,
		get_exp		=> 20,
		get_money	=> 5,
		icon		=> 'mon/059.gif',

		job			=> 14, # 踊り子みかわしきゃく,ふしぎなおどり,うけながし
		sp			=> 16,
		mp			=> 50,
	},
	{ # 6
		name		=> 'トゲボウズ',
		hp			=> 64,
		at			=> 55,
		df			=> 125,
		ag			=> 15,
		get_exp		=> 23,
		get_money	=> 7,
		icon		=> 'mon/212.gif',

		job			=> 21, # バーサーカーたいあたり
		sp			=> 10,
		mp			=> 24,
	},
	{ # 7
		name		=> 'チビベリー',
		hp			=> 50,
		at			=> 55,
		df			=> 15,
		ag			=> 120,
		get_exp		=> 15,
		get_money	=> 5,
		icon		=> 'mon/198.gif',

		old_sp		=> 20, # テンション
		job			=> 12, # 魔物使いひのいき
		sp			=> 5,
		mp			=> 16,
	},
	{ # 8
		name		=> 'ベロロン',
		hp			=> 120,
		at			=> 85,
		df			=> 40,
		ag			=> 10,
		get_exp		=> 28,
		get_money	=> 10,
		icon		=> 'mon/199.gif',

		job			=> 12, # 魔物使いひのいき,もうどくのきり,かえんのいき,しびれうち,なめまわす
		sp			=> 50,
		mp			=> 34,
	},
	{ # 9
		name		=> 'チビドラゴン',
		hp			=> 150,
		at			=> 85,
		df			=> 35,
		ag			=> 20,
		get_exp		=> 24,
		get_money	=> 7,
		icon		=> 'mon/083.gif',

		job			=> 12, # 魔物使いひのいき
		sp			=> 5,
		mp			=> 14,
	},
);



1;
