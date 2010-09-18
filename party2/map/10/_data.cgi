# 宝の中身
@treasures = (
[20..28,32..37,39], # 武器No
[20..39], # 防具No
[4..6,13,28,29,37,38,40,40,57,60..65,87,104..107,109,109,109], # 道具No
);


# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = (0..11,0..11,12,13);

# モンスター
@monsters = (
	{ # 0
		name		=> 'れんごくちょう',
		hp			=> 470,
		at			=> 320,
		df			=> 150,
		ag			=> 600,
		get_exp		=> 177,
		get_money	=> 72,
		icon		=> 'mon/532.gif',

		job			=> 41, # ドラゴン
		sp			=> 999,
		old_job		=> 51, # 光魔道士
		old_sp		=> 999,
		mp			=> 144,
		state		=> '攻封',
	},
	{ # 1
		name		=> 'ブリザー',
		hp			=> 400,
		at			=> 300,
		df			=> 210,
		ag			=> 500,
		get_exp		=> 146,
		get_money	=> 92,
		icon		=> 'mon/531.gif',

		job			=> 41, # ドラゴン
		sp			=> 999,
		old_job		=> 27, # 風水士
		old_sp		=> 999,
		mp			=> 174,
		state		=> '攻封',
	},
	{ # 2
		name		=> '死のつかい',
		hp			=> 380,
		at			=> 280,
		df			=> 180,
		ag			=> 150,
		get_exp		=> 126,
		get_money	=> 62,
		icon		=> 'mon/541.gif',

		job			=> 42, # アサシン
		sp			=> 999,
		old_job		=> 93, # 即死
		old_sp		=> 999,
		mp			=> 144,
		state		=> '攻封',
	},
	{ # 3
		name		=> 'クロ',
		hp			=> 396,
		at			=> 296,
		df			=> 196,
		ag			=> 196,
		get_exp		=> 196,
		get_money	=> 96,
		icon		=> 'mon/544.gif',
		job			=> 15, # 黒魔道士
		sp			=> 999,
		old_job		=> 15, # 闇魔導士
		old_sp		=> 999,
		mp			=> 196,
		state		=> '攻封',
	},
	{ # 4
		name		=> '炎魔',
		hp			=> 400,
		at			=> 270,
		df			=> 150,
		ag			=> 300,
		get_exp		=> 126,
		get_money	=> 62,
		icon		=> 'mon/598.gif',

		job			=> 6, # 魔法使い
		sp			=> 999,
		old_job		=> 15, # 闇魔導士
		old_sp		=> 999,
		mp			=> 144,
		state		=> '攻封',
	},
	{ # 5
		name		=> 'バンパイア',
		hp			=> 499,
		at			=> 380,
		df			=> 160,
		ag			=> 250,
		get_exp		=> 146,
		get_money	=> 70,
		icon		=> 'mon/568.gif',

		old_sp		=> 20,
		job			=> 38, # バンパイア
		sp			=> 999,
		mp			=> 121,
		state		=> '攻封',
	},
	{ # 6
		name		=> 'ノロイ',
		hp			=> 410,
		at			=> 271,
		df			=> 160,
		ag			=> 280,
		get_exp		=> 162,
		get_money	=> 65,
		icon		=> 'mon/542.gif',
		old_sp		=> 20,
		job			=> 46, # ギャンブラーヘブンスロット、いちげきのダーツ、あくまのダイス、しのルーレット
		sp			=> 80,
		mp			=> 59,
		state		=> '攻封',
	},
	{ # 7
		name		=> 'デスサイズ',
		hp			=> 420,
		at			=> 440,
		df			=> 100,
		ag			=> 400,
		get_exp		=> 66,
		get_money	=> 242,
		icon		=> 'mon/543.gif',
		
		job			=> 93, # 即死
		sp			=> 999,
		mp			=> 142,
		state		=> '攻封',
	},
	{ # 8
		name		=> 'サイクル',
		hp			=> 400,
		at			=> 424,
		df			=> 150,
		ag			=> 666,
		get_exp		=> 164,
		get_money	=> 155,
		icon		=> 'mon/235.gif',

		job			=> 48, # 堕天使
		sp			=> 999,
		old_job		=> 46, # ギャンブラー
		old_sp		=> 999,
		mp			=> 149,
		state		=> '攻封',
	},
	{ # 9
		name		=> 'ラボス',
		hp			=> 430,
		at			=> 280,
		df			=> 520,
		ag			=> 180,
		get_exp		=> 120,
		get_money	=> 500,
		icon		=> 'mon/540.gif',

		job			=> 29, # 時魔道士
		sp			=> 999,
		old_job		=> 93, # 即死
		old_sp		=> 999,
		mp			=> 299,
		state		=> '攻封',
	},
	{ # 10
		name		=> 'ダースドラゴン',
		hp			=> 500,
		at			=> 360,
		df			=> 240,
		ag			=> 300,
		get_exp		=> 175,
		get_money	=> 125,
		icon		=> 'mon/534.gif',

		old_sp		=> 20,
		job			=> 41, # ドラゴン
		sp			=> 999,
		mp			=> 149,
		state		=> '攻封',
	},
	{ # 11
		name		=> 'デスアイ',
		hp			=> 444,
		at			=> 300,
		df			=> 200,
		ag			=> 350,
		get_exp		=> 160,
		get_money	=> 90,
		icon		=> 'mon/538.gif',

		job			=> 93, # 即死
		sp			=> 999,
		mp			=> 149,
		state		=> '攻封',
	},
	{ # 12
		name		=> 'ハグレキング',
		hp			=> 22,
		at			=> 180,
		df			=> 5000,
		ag			=> 2500,
		get_exp		=> 3500,
		get_money	=> 100,
		icon		=> 'mon/238.gif',

		job			=> 40, # ハグレメタル
		sp			=> 999,
		old_job		=> 99, # 逃げる
		old_sp		=> 0,
		mp			=> 499,
		tmp			=> '魔無効',
		state		=> '攻封',
	},
	{ # 13
		name		=> 'メタルキング',
		hp			=> 25,
		at			=> 200,
		df			=> 6000,
		ag			=> 3000,
		get_exp		=> 4000,
		get_money	=> 100,
		icon		=> 'mon/517.gif',

		job			=> 40, # ハグレメタル
		sp			=> 999,
		old_job		=> 99, # 逃げる
		old_sp		=> 0,
		mp			=> 499,
		tmp			=> '魔無効',
		state		=> '攻封',
	},
);




1; # 削除不可
