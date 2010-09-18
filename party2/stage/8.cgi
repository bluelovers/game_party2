# 宝の中身
@treasures = (
[10..21], # 武器No
[10..17], # 防具No
[15..26,15..26,32,72..86], # 道具No
);

# ボス
@bosses= (
	{
		name		=> 'ベヒーモス',
		hp			=> 2800,
		at			=> 185,
		df			=> 125,
		ag			=> 145,
		get_exp		=> 350,
		get_money	=> 200,
		icon		=> 'mon/553.gif',
		
		hit			=> 150, # 長期戦用命中率150%
		job			=> 23, # 竜騎士ジャンプ、ドラゴンパワー
		sp			=> 30,
		old_job		=> 25, # モンクまわしげり
		old_sp		=> 5,
		mp			=> 299,
		tmp			=> '大防御',
	},
);

# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = (0,0,0,1,1,1,2,2,2,3,3,3,4,5,6,6,7,8,9);


# モンスター
@monsters = (
	{ # 0
		hit			=> 70,
		name		=> 'コロヒーロー',
		hp			=> 100,
		at			=> 80,
		df			=> 60,
		ag			=> 60,
		get_exp		=> 30,
		get_money	=> 15,
		icon		=> 'mon/100.gif',

		old_sp		=> 20,
		job			=> 34, # 勇者かばう
		sp			=> 10,
		mp			=> 21,
	},
	{ # 1
		hit			=> 70,
		name		=> 'コロファイター',
		hp			=> 120,
		at			=> 90,
		df			=> 70,
		ag			=> 10,
		get_exp		=> 30,
		get_money	=> 15,
		icon		=> 'mon/101.gif',

		old_sp		=> 20,
		job			=> 1, # 戦士かぶとわり、かばう、ちからをためる
		sp			=> 30,
		mp			=> 11,
	},
	{ # 2
		hit			=> 70,
		name		=> 'コロマージ',
		hp			=> 80,
		at			=> 50,
		df			=> 30,
		ag			=> 80,
		get_exp		=> 30,
		get_money	=> 15,
		icon		=> 'mon/102.gif',

		job			=> 6, # 魔法使いメラ、ルカニ、ギラ、マヌーサ
		sp			=> 14,
		mp			=> 61,
	},
	{ # 3
		hit			=> 70,
		name		=> 'コロプリースト',
		hp			=> 90,
		at			=> 60,
		df			=> 40,
		ag			=> 60,
		get_exp		=> 30,
		get_money	=> 15,
		icon		=> 'mon/103.gif',

		job			=> 5, # 僧侶スカラ、キアリー、ホイミ
		sp			=> 6,
		mp			=> 51,
	},
	{ # 4
		name		=> '爆弾岩',
		hp			=> 100,
		at			=> 86,
		df			=> 40,
		ag			=> 10,
		get_exp		=> 40,
		get_money	=> 5,
		icon		=> 'mon/080.gif',

		job			=> 94, # 自爆メガンテ、ねる
		sp			=> 20,
		mp			=> 42,
	},
	{ # 5
		name		=> 'メガザルロック',
		hp			=> 110,
		at			=> 75,
		df			=> 50,
		ag			=> 44,
		get_exp		=> 36,
		get_money	=> 10,
		icon		=> 'mon/081.gif',

		old_sp		=> 30,
		job			=> 3, # 騎士
		sp			=> 80,
		mp			=> 62,
	},
	{ # 6
		name		=> 'マネマネ',
		hp			=> 133,
		at			=> 99,
		df			=> 33,
		ag			=> 99,
		get_exp		=> 33,
		get_money	=> 33,
		icon		=> 'mon/068.gif',

		job			=> 36, # ものまね士
		sp			=> 999,
		mp			=> 99,
	},
	{ # 7
		name		=> 'イタズラ妖精',
		hp			=> 140,
		at			=> 100,
		df			=> 40,
		ag			=> 120,
		get_exp		=> 27,
		get_money	=> 20,
		icon		=> 'mon/110.gif',

		job			=> 8, # 遊び人
		sp			=> 999,
		old_job		=> 55, # 妖精
		old_sp		=> 999,
		mp			=> 50,
	},
	{ # 8
		name		=> 'ギャンブル妖精',
		hp			=> 104,
		at			=> 120,
		df			=> 40,
		ag			=> 130,
		get_exp		=> 28,
		get_money	=> 22,
		icon		=> 'mon/111.gif',

		job			=> 36, # ギャンブラーしのルーレット、あくまのダイス、ヘブンスロット
		sp			=> 50,
		old_job		=> 55, # 妖精
		old_sp		=> 999,
		mp			=> 20,
	},
	{ # 9
		name		=> 'マウサギ',
		hp			=> 104,
		at			=> 120,
		df			=> 40,
		ag			=> 130,
		get_exp		=> 28,
		get_money	=> 22,
		icon		=> 'mon/260.gif',

		job			=> 8, # 遊び人
		sp			=> 999,
		old_job		=> 36, # ものまね士
		old_sp		=> 80,
		mp			=> 20,
	},
);



1;
