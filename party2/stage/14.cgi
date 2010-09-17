# 宝の中身
@treasures = (
[26..28,32..37,39], # 武器No
[30..39], # 防具No
[4..6,13,28,29,37,38,40,40,59..65,87,103..107], # 道具No
);

# ボス
@bosses= (
	{
		name		=> 'ｲﾋﾞﾙｻﾝﾀﾞｰA',
		hp			=> 5000,
		at			=> 400,
		df			=> 300,
		ag			=> 3000,
		get_exp		=> 300,
		get_money	=> 300,
		icon		=> 'mon/696.gif',
		
		job			=> 37, # 結界士
		sp			=> 999,
		old_job		=> 57, # ｴﾙﾌ
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '魔無効',
	},
	{
		name		=> 'ｻﾀﾝ',
		hp			=> 15000,
		at			=> 600,
		df			=> 300,
		ag			=> 250,
		get_exp		=> 3000,
		get_money	=> 3000,
		icon		=> 'mon/800.gif',
		
		hit			=> 400, # 長期戦用命中率400%
		job			=> 47, # 堕天使
		sp			=> 999,
		old_job		=> 48, # 暗黒騎士
		old_sp		=> 999,
		mmp			=> 30000,
		mp			=> 8000,
		tmp			=> '魔反撃',
	},
	{
		name		=> 'ｲﾋﾞﾙｻﾝﾀﾞｰB',
		hp			=> 5000,
		at			=> 400,
		df			=> 300,
		ag			=> 3000,
		get_exp		=> 300,
		get_money	=> 300,
		icon		=> 'mon/696.gif',
		
		job			=> 35, # 魔王
		sp			=> 999,
		old_job		=> 32, # 召喚士
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '魔無効',
	},
);

# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = (0,0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,6,6,6,6,7,7,8,9);


# モンスター
@monsters = (
	{ # 0
		name		=> 'ﾃﾞｽﾏｼﾝ',
		hp			=> 555,
		at			=> 333,
		df			=> 222,
		ag			=> 222,
		get_exp		=> 111,
		get_money	=> 111,
		icon		=> 'mon/522.gif',

		job			=> 24, # 魔剣士
		sp			=> 999,
		old_job		=> 11, # 弓使い
		old_sp		=> 999,
		mp			=> 222,
	},
	{ # 1
		name		=> 'ｷﾝｸﾞﾍﾞﾋｰﾓｽ',
		hp			=> 600,
		at			=> 350,
		df			=> 180,
		ag			=> 160,
		get_exp		=> 120,
		get_money	=> 100,
		icon		=> 'mon/554.gif',

		old_sp		=> 20,
		job			=> 21, # 狂戦士たいあたり、うけながし、おたけび、すてみ、もろはぎり
		sp			=> 40,
		mp			=> 149,
	},
	{ # 2
		name		=> 'ｲｸﾛﾌﾟｽ',
		hp			=> 700,
		at			=> 500,
		df			=> 50,
		ag			=> 50,
		get_exp		=> 150,
		get_money	=> 10,
		icon		=> 'mon/564.gif',

		old_sp		=> 20,
		job			=> 1, # 戦士
		sp			=> 999,
		old_job		=> 21, # 狂戦士たいあたり、うけながし、おたけび、すてみ、もろはぎり、みなごろし
		mp			=> 99,
	},
	{ # 3
		name		=> 'ﾀﾞｰｽﾄﾞﾗｺﾞﾝ',
		hp			=> 500,
		at			=> 300,
		df			=> 240,
		ag			=> 200,
		get_exp		=> 125,
		get_money	=> 95,
		icon		=> 'mon/534.gif',

		old_sp		=> 20,
		job			=> 41, # ﾄﾞﾗｺﾞﾝ
		sp			=> 999,
		mp			=> 149,
	},
	{ # 4
		name		=> 'ｽﾄｰﾝｺﾞｰﾚﾑ',
		hp			=> 300,
		at			=> 280,
		df			=> 400,
		ag			=> 100,
		get_exp		=> 100,
		get_money	=> 200,
		icon		=> 'mon/547.gif',

		old_sp		=> 30,
		job			=> 3, # 騎士かばう、まもりをかためる、すてみ、だいぼうぎょ、スクルト
		sp			=> 60,
		mp			=> 155,
	},
	{ # 5
		name		=> 'ﾗﾎﾞｽ',
		hp			=> 420,
		at			=> 270,
		df			=> 320,
		ag			=> 120,
		get_exp		=> 90,
		get_money	=> 400,
		icon		=> 'mon/540.gif',

		job			=> 29, # 時魔道士
		sp			=> 999,
		old_job		=> 93, # 即死ザキザラキ
		old_sp		=> 20,
		mp			=> 299,
	},
	{ # 6
		name		=> 'ｻｲｸﾙ',
		hp			=> 350,
		at			=> 280,
		df			=> 100,
		ag			=> 300,
		get_exp		=> 115,
		get_money	=> 125,
		icon		=> 'mon/235.gif',

		job			=> 48, # 堕天使バイオガやみのてんしシャドウフレアこころないてんし
		sp			=> 160,
		old_job		=> 46, # ｷﾞｬﾝﾌﾞﾗｰ
		old_sp		=> 999,
		mp			=> 149,
	},
	{ # 7
		name		=> 'ﾄﾞﾗｺﾞﾝｿﾞﾝﾋﾞ',
		hp			=> 650,
		at			=> 350,
		df			=> 260,
		ag			=> 100,
		get_exp		=> 155,
		get_money	=> 100,
		icon		=> 'mon/557.gif',

		job			=> 58, # ﾀﾞｰｸｴﾙﾌ
		sp			=> 999,
		old_job		=> 52, # 魔人
		old_sp		=> 999,
		mp			=> 92,
		tmp			=> '復活',
	},
	{ # 8
		name		=> 'ﾀﾞｲｼﾞｬ',
		hp			=> 760,
		at			=> 460,
		df			=> 160,
		ag			=> 260,
		get_exp		=> 255,
		get_money	=> 300,
		icon		=> 'mon/559.gif',

		job			=> 53, # 蟲師
		sp			=> 999,
		old_job		=> 48, # 堕天使バイオガ
		old_sp		=> 40,
		mp			=> 292,
		tmp			=> '復活',
	},
	{ # 9
		name		=> 'ﾒﾀﾙｷﾝｸﾞ',
		hp			=> 25,
		at			=> 200,
		df			=> 6000,
		ag			=> 2000,
		get_exp		=> 4000,
		get_money	=> 100,
		icon		=> 'mon/517.gif',

		job			=> 40, # ﾊｸﾞﾚﾒﾀﾙ
		sp			=> 999,
		old_job		=> 99, # 逃げる
		old_sp		=> 0,
		mp			=> 249,
		tmp			=> '魔無効',
	},
);



1;
