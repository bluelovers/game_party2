# 宝の中身
@treasures = (
[24..28,33..37], # 武器No
[24..31,36..38], # 防具No
[4..6,12,21..23,28,29,28,29,40,72..86], # 道具No
);

# ボス
@bosses= (
	{
		name		=> 'ﾊﾟｰﾌﾟﾙｽﾄｰﾝ',
		hp			=> 20,
		at			=> 250,
		df			=> 6000,
		ag			=> 2000,
		get_exp		=> 100,
		get_money	=> 500,
		icon		=> 'mon/194.gif',
		
		job			=> 90, # どくこうげき、ポイズン、もうどくのきり
		sp			=> 999,
		old_job		=> 92, # ラリホー、ねむりこうげき、あまいいき
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '魔無効',
	},
	{
		name		=> '魔王',
		hp			=> 14000,
		at			=> 320,
		df			=> 300,
		ag			=> 140,
		get_exp		=> 2000,
		get_money	=> 1500,
		icon		=> 'mon/700.gif',
		
		hit			=> 250, # 長期戦用命中率200%
		job			=> 35, # 魔王
		sp			=> 999,
		old_job		=> 22, # 暗黒騎士
		old_sp		=> 999,
		mmp			=> 10000,
		mp			=> 4000,
		tmp			=> '攻反撃',
	},
	{
		name		=> 'ﾚｯﾄﾞｽﾄｰﾝ',
		hp			=> 20,
		at			=> 250,
		df			=> 6000,
		ag			=> 2000,
		get_exp		=> 100,
		get_money	=> 500,
		icon		=> 'mon/190.gif',
		
		job			=> 26, # 忍者
		sp			=> 999,
		old_job		=> 6, # 魔法使い
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '魔無効',
	},
);

# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = (0,0,0,0,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,7,7,8,8,9,10);


# モンスター
@monsters = (
	{ # 0
		name		=> 'ﾋﾞｯｸﾞｱｲ',
		hp			=> 180,
		at			=> 180,
		df			=> 100,
		ag			=> 180,
		get_exp		=> 70,
		get_money	=> 35,
		icon		=> 'mon/526.gif',

		old_sp		=> 30,
		job			=> 20, # 悪魔さそうおどり、レディウィップ、マジックバリア、あまいいき、メダパニダンス
		sp			=> 26,
		mp			=> 64,
	},
	{ # 1
		name		=> 'ﾁﾋﾞﾍﾞﾛｽ',
		hp			=> 150,
		at			=> 160,
		df			=> 80,
		ag			=> 200,
		get_exp		=> 45,
		get_money	=> 15,
		icon		=> 'mon/203.gif',
		old_sp		=> 20,
	},
	{ # 2
		name		=> 'ｹﾙﾍﾞﾛｽ',
		hp			=> 270,
		at			=> 220,
		df			=> 130,
		ag			=> 50,
		get_exp		=> 60,
		get_money	=> 60,
		icon		=> 'mon/204.gif',

		old_sp		=> 20,
		job			=> 29, # 時魔道士スロウ、ヘイスト
		sp			=> 20,
		mp			=> 33,
	},
	{ # 3
		name		=> '闇の剣士',
		hp			=> 230,
		at			=> 215,
		df			=> 120,
		ag			=> 125,
		get_exp		=> 74,
		get_money	=> 50,
		icon		=> 'mon/220.gif',

		old_sp		=> 20,
		job			=> 2, # 剣士しんくうぎり、みねうち、うけながし、かばう、メタルぎり、はやぶさぎり
		sp			=> 80,
		mp			=> 64,
	},
	{ # 4
		name		=> '黒の騎士',
		hp			=> 255,
		at			=> 185,
		df			=> 155,
		ag			=> 35,
		get_exp		=> 75,
		get_money	=> 40,
		icon		=> 'mon/222.gif',

		old_sp		=> 30,
		job			=> 1, # 戦士かぶとわり、かばう、ちからをためる、まじんぎり
		sp			=> 70,
		mp			=> 54,
	},
	{ # 5
		name		=> 'ｽｶﾙｷﾝｸﾞ',
		hp			=> 210,
		at			=> 180,
		df			=> 110,
		ag			=> 110,
		get_exp		=> 70,
		get_money	=> 40,
		icon		=> 'mon/567.gif',

		job			=> 38, # ﾊﾞﾝﾊﾟｲｱきゅうけつ、アスピル、アストロン
		sp			=> 50,
		mp			=> 48,
	},
	{ # 6
		name		=> 'ﾊﾞﾝﾊﾟｲｱ',
		hp			=> 280,
		at			=> 200,
		df			=> 120,
		ag			=> 150,
		get_exp		=> 76,
		get_money	=> 50,
		icon		=> 'mon/568.gif',

		old_sp		=> 20,
		job			=> 38, # ﾊﾞﾝﾊﾟｲｱ
		sp			=> 999,
		mp			=> 44,
	},
	{ # 7
		name		=> 'ﾐﾗｰﾅｲﾄ',
		hp			=> 200,
		at			=> 200,
		df			=> 180,
		ag			=> 180,
		get_exp		=> 70,
		get_money	=> 70,
		icon		=> 'mon/520.gif',

		job			=> 36, # ものまね士
		sp			=> 999,
		mp			=> 94,
	},
	{ # 8
		name		=> 'ﾃﾞﾋﾞﾙｱｲ',
		hp			=> 180,
		at			=> 220,
		df			=> 120,
		ag			=> 200,
		get_exp		=> 62,
		get_money	=> 20,
		icon		=> 'mon/539.gif',

		job			=> 42, # ｱｻｼﾝコンフェ
		sp			=> 30,
		mp			=> 64,
	},
	{ # 9
		name		=> 'ﾊﾟﾝﾄﾞﾗﾎﾞｯｸｽ',
		hp			=> 900,
		at			=> 300,
		df			=> 95,
		ag			=> 800,
		get_exp		=> 100,
		get_money	=> 500,
		icon		=> 'mon/092.gif',
		
		job			=> 93, # 即死
		sp			=> 20,
		mp			=> 69,
		tmp			=> '２倍', 
	},
	{ # 10
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
		mp			=> 91,
		tmp			=> '魔無効',
	},
);



1;
