# 宝の中身
@treasures = (
[24..28,33..37], # 武器No
[24..31,36..38], # 防具No
[4..6,12,21..23,23,28,29,36,39,40,87,109], # 道具No
);

# ボス
@bosses= (
	{
		name		=> 'ﾌﾞﾗｯｸｽﾄｰﾝ',
		hp			=> 20,
		at			=> 250,
		df			=> 6000,
		ag			=> 2000,
		get_exp		=> 100,
		get_money	=> 800,
		icon		=> 'mon/195.gif',
		
		job			=> 19, # 闇魔道士
		sp			=> 999,
		old_job		=> 20, # 悪魔
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '魔無効',
	},
	{
		name		=> '死神',
		hp			=> 12000,
		at			=> 360,
		df			=> 180,
		ag			=> 240,
		get_exp		=> 2000,
		get_money	=> 1500,
		icon		=> 'mon/702.gif',
		
		hit			=> 250, # 長期戦用命中率200%
		job			=> 19, # 闇魔道士
		sp			=> 70,
		old_job		=> 46, # ｷﾞｬﾝﾌﾞﾗｰ
		old_sp		=> 999,
		mmp			=> 14000,
		mp			=> 5000,
		tmp			=> '魔反撃',
	},
	{
		name		=> 'ﾌﾞﾙｰｽﾄｰﾝ',
		hp			=> 20,
		at			=> 250,
		df			=> 6000,
		ag			=> 2000,
		get_exp		=> 100,
		get_money	=> 800,
		icon		=> 'mon/191.gif',
		
		job			=> 33, # 賢者
		sp			=> 130,
		old_job		=> 31, # 青魔道士
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '魔無効',
	},
);

# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = ();


# モンスター
@monsters = (
	{ # 0
		name		=> '竜魔人',
		hp			=> 450,
		at			=> 270,
		df			=> 200,
		ag			=> 50,
		get_exp		=> 85,
		get_money	=> 70,
		icon		=> 'mon/523.gif',
		
		old_sp		=> 20,
		job			=> 23, # 竜騎士ジャンプ、ドラゴンパワー、りゅうけん
		sp			=> 50,
		mp			=> 85,
	},
	{ # 1
		name		=> 'ﾃﾞｽｻｲｽﾞ',
		hp			=> 250,
		at			=> 230,
		df			=> 80,
		ag			=> 200,
		get_exp		=> 86,
		get_money	=> 142,
		icon		=> 'mon/543.gif',
		
		job			=> 93, # 即死ザキ
		sp			=> 10,
		mp			=> 139,
	},
	{ # 2
		name		=> '魔王の影',
		hp			=> 200,
		at			=> 220,
		df			=> 300,
		ag			=> 150,
		get_exp		=> 80,
		get_money	=> 75,
		icon		=> 'mon/527.gif',
		
		job			=> 35, # 魔王うけながし、いてつくはどう、ザキ
		sp			=> 50,
		mp			=> 120,
	},
	{ # 3
		name		=> 'ｷﾗｰﾏｼﾝ',
		hp			=> 444,
		at			=> 244,
		df			=> 144,
		ag			=> 114,
		get_exp		=> 88,
		get_money	=> 88,
		icon		=> 'mon/521.gif',
		
		job			=> 24, # 魔剣士かえんぎり、メタルぎり、バイキルト、いなずまぎり、ギガスラッシュ
		sp			=> 50,
		old_job		=> 11, # 弓使いかげぬい、せいしんとういつ、でたらめや、ようせいのや、フラッシュアロー、ラリホーアロー
		old_sp		=> 90,
		mp			=> 111,
	},
	{ # 4
		name		=> 'ﾍﾞﾋｰﾓｽ',
		hp			=> 415,
		at			=> 265,
		df			=> 85,
		ag			=> 145,
		get_exp		=> 90,
		get_money	=> 40,
		icon		=> 'mon/553.gif',
		
		job			=> 23, # 竜騎士ジャンプ、ドラゴンパワー
		sp			=> 30,
		old_job		=> 25, # モンクまわしげり
		old_sp		=> 5,
		mp			=> 97,
	},
	{ # 5
		hit			=> 70,
		name		=> 'ｷﾞｶﾞﾝﾃｽ',
		hp			=> 600,
		at			=> 400,
		df			=> 50,
		ag			=> 10,
		get_exp		=> 100,
		get_money	=> 5,
		icon		=> 'mon/563.gif',
		
		old_sp		=> 20,
		job			=> 21, # 狂戦士
		sp			=> 999,
		mp			=> 59,
		ten			=> 3,
		state		=> '眠り',
		tmp			=> '２倍',
	},
	{ # 6
		name		=> 'ﾉﾛｲ',
		hp			=> 380,
		at			=> 200,
		df			=> 160,
		ag			=> 180,
		get_exp		=> 82,
		get_money	=> 65,
		icon		=> 'mon/542.gif',
		
		old_sp		=> 20,
		job			=> 46, # ｷﾞｬﾝﾌﾞﾗｰヘブンスロット、いちげきのダーツ、あくまのダイス、しのルーレット
		sp			=> 80,
		mp			=> 59,
	},
	{ # 7
		name		=> 'ﾔﾐ',
		hp			=> 410,
		at			=> 280,
		df			=> 150,
		ag			=> 120,
		get_exp		=> 88,
		get_money	=> 64,
		icon		=> 'mon/536.gif',
		
		old_sp		=> 20,
		job			=> 47, # ｿﾙｼﾞｬｰブレイバー、きょうぎり、メテオレイン、クライムハザード
		sp			=> 140,
		mp			=> 69,
	},
	{ # 8
		name		=> 'ﾊﾞｼﾞﾘｽｸ',
		hp			=> 400,
		at			=> 300,
		df			=> 40,
		ag			=> 280,
		get_exp		=> 90,
		get_money	=> 80,
		icon		=> 'mon/558.gif',
		
		old_sp		=> 20,
		job			=> 53, # 蟲師
		sp			=> 999,
		mp			=> 67,
	},
);



1;
