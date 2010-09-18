# 宝の中身
@treasures = (
[10..18], # 武器No
[10..23], # 防具No
[15..26,15..26,33,72..86], # 道具No
);

# ボス
@bosses= (
	{
		name		=> 'スライムA',
		hp			=> 150,
		at			=> 120,
		df			=> 20,
		ag			=> 100,
		get_exp		=> 30,
		get_money	=> 10,
		icon		=> 'mon/002.gif',
		
		job			=> 29, # 時魔道士スロウ、ヘイスト
		sp			=> 20,
		mp			=> 91,
	},
	{
		name		=> 'スライムB',
		hp			=> 150,
		at			=> 120,
		df			=> 20,
		ag			=> 100,
		get_exp		=> 30,
		get_money	=> 10,
		icon		=> 'mon/002.gif',
		
		job			=> 15, # 黒魔道士ポイズン、ファイア、スリプル、リフレク、アスピル
		sp			=> 80,
		mp			=> 91,
	},
	{
		name		=> 'キングスライム',
		hp			=> 3000,
		at			=> 200,
		df			=> 150,
		ag			=> 120,
		get_exp		=> 500,
		get_money	=> 400,
		icon		=> 'mon/516.gif',
		
		old_sp		=> 20,
		hit			=> 150, # 長期戦用命中率150%
		job			=> 21, # 狂戦士たいあたり
		sp			=> 5,
		mp			=> 400,
		tmp			=> '攻無効',
	},
	{
		name		=> 'スライムC',
		hp			=> 150,
		at			=> 120,
		df			=> 20,
		ag			=> 100,
		get_exp		=> 30,
		get_money	=> 10,
		icon		=> 'mon/002.gif',
		
		job			=> 16, # 白魔道士ケアル、ライブラ、サイレス、ケアルラ、コンフェ、シェル
		sp			=> 70,
		mp			=> 91,
	},
	{
		name		=> 'スライムD',
		hp			=> 150,
		at			=> 120,
		df			=> 20,
		ag			=> 100,
		get_exp		=> 30,
		get_money	=> 10,
		icon		=> 'mon/002.gif',
		
		job			=> 30, # 赤魔道士ケアル、シェル、ポイズン、ファイア、リフレク
		sp			=> 90,
		mp			=> 91,
	},
);

# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = (0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,11,11,12,13,14,15);


# モンスター
@monsters = (
	{ # 0
		name		=> 'ブチスライム',
		hp			=> 77,
		at			=> 77,
		df			=> 77,
		ag			=> 77,
		get_exp		=> 22,
		get_money	=> 22,
		icon		=> 'mon/001.gif',
		old_sp		=> 20,
	},
	{ # 1
		name		=> 'スライム',
		hp			=> 90,
		at			=> 90,
		df			=> 40,
		ag			=> 90,
		get_exp		=> 25,
		get_money	=> 20,
		icon		=> 'mon/002.gif',
		old_sp		=> 20,

		job			=> 59, # スライムライダー よびだす
		sp			=> 10,
		mp			=> 30,
	},
	{ # 2
		name		=> 'スライムベス',
		hp			=> 100,
		at			=> 105,
		df			=> 30,
		ag			=> 100,
		get_exp		=> 28,
		get_money	=> 24,
		icon		=> 'mon/003.gif',
		old_sp		=> 20,
	},
	{ # 3
		name		=> 'バブルスライム',
		hp			=> 140,
		at			=> 120,
		df			=> 50,
		ag			=> 70,
		get_exp		=> 35,
		get_money	=> 10,
		icon		=> 'mon/020.gif',

		job			=> 90, # どくこうげき、ポイズン
		sp			=> 20,
		mp			=> 32,
	},
	{ # 4
		name		=> 'ホイミスライム',
		hp			=> 100,
		at			=> 90,
		df			=> 30,
		ag			=> 100,
		get_exp		=> 30,
		get_money	=> 15,
		icon		=> 'mon/010.gif',

		job			=> 5, # 僧侶スカラ、キアリー、ホイミ
		sp			=> 6,
		mp			=> 45,
	},
	{ # 5
		name		=> 'しびれクラゲ',
		hp			=> 120,
		at			=> 126,
		df			=> 42,
		ag			=> 65,
		get_exp		=> 36,
		get_money	=> 11,
		icon		=> 'mon/012.gif',

		job			=> 91, # まひこうげき、しびれうち
		sp			=> 20,
		mp			=> 31,
	},
	{ # 6
		name		=> 'スライムまどう',
		hp			=> 110,
		at			=> 85,
		df			=> 30,
		ag			=> 100,
		get_exp		=> 34,
		get_money	=> 21,
		icon		=> 'mon/013.gif',

		job			=> 19, # 闇魔道士ルカナン,マホカンタ,メダパニ
		sp			=> 16,
		mp			=> 84,
	},
	{ # 7
		name		=> 'スライムつむり',
		hp			=> 60,
		at			=> 90,
		df			=> 130,
		ag			=> 40,
		get_exp		=> 32,
		get_money	=> 27,
		icon		=> 'mon/015.gif',

		job			=> 39, # スライムギラスクルト
		sp			=> 7,
		mp			=> 43,
	},
	{ # 8
		name		=> 'ファイアースライム',
		hp			=> 125,
		at			=> 125,
		df			=> 85,
		ag			=> 75,
		get_exp		=> 40,
		get_money	=> 25,
		icon		=> 'mon/008.gif',

		job			=> 12, # 魔物使いひのいき
		sp			=> 5,
		mp			=> 15,
	},
	{ # 9
		name		=> 'スライムバット',
		hp			=> 100,
		at			=> 115,
		df			=> 20,
		ag			=> 155,
		get_exp		=> 41,
		get_money	=> 11,
		icon		=> 'mon/027.gif',
		
		job			=> 38, # バンパイアきゅうけつ、アスピル
		sp			=> 20,
		mp			=> 44,
	},
	{ # 10
		name		=> 'ベホマスライム',
		hp			=> 150,
		at			=> 90,
		df			=> 30,
		ag			=> 120,
		get_exp		=> 40,
		get_money	=> 30,
		icon		=> 'mon/011.gif',

		job			=> 5, # 僧侶
		sp			=> 999,
		mp			=> 99,
	},
	{ # 11
		name		=> 'マグマスライム',
		hp			=> 90,
		at			=> 148,
		df			=> 140,
		ag			=> 50,
		get_exp		=> 38,
		get_money	=> 31,
		icon		=> 'mon/021.gif',

		job			=> 7, # 商人まもりをかためる
		sp			=> 3,
		mp			=> 10,
	},
	{ # 12
		name		=> 'ビックスライム',
		hp			=> 300,
		at			=> 145,
		df			=> 10,
		ag			=> 40,
		get_exp		=> 40,
		get_money	=> 30,
		icon		=> 'mon/006.gif',
	},
	{ # 13
		name		=> 'スライムファラオ',
		hp			=> 444,
		at			=> 144,
		df			=> 144,
		ag			=> 144,
		get_exp		=> 144,
		get_money	=> 144,
		icon		=> 'mon/234.gif',

		job			=> 19, # 闇魔道士ルカナン、マホカンタ、メダパニ、ザキ、マホトーン、ベギラゴン
		sp			=> 60,
		mp			=> 144,
	},
	{ # 14
		name		=> 'メタルスライム',
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
	{ # 15
		name		=> 'ハグレメタル',
		hp			=> 14,
		at			=> 110,
		df			=> 4000,
		ag			=> 2000,
		get_exp		=> 1500,
		get_money	=> 30,
		icon		=> 'mon/022.gif',

		job			=> 40, # ハグレメタルメラミ
		sp			=> 25,
		old_job		=> 99, # 逃げる
		old_sp		=> 0,
		mp			=> 61,
		tmp			=> '魔無効',
	},
);



1;
