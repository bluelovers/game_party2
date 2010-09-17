# 宝の中身
@treasures = (
[33..37], # 武器No
[36..38], # 防具No
[70,104,104], # 道具No
);

# ボス
@bosses= (
	{
		name		=> '悪の右目',
		hp			=> 3000,
		at			=> 380,
		df			=> 200,
		ag			=> 200,
		get_exp		=> 500,
		get_money	=> 100,
		icon		=> 'mon/580.gif',
		
		hit			=> 250, # 長期戦用命中率200%
		job			=> 58, # ﾀﾞｰｸｴﾙﾌ
		sp			=> 999,
		old_job		=> 20, # 悪魔
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '魔無効',
	},
	{
		name		=> '悪の口',
		hp			=> 5000,
		at			=> 450,
		df			=> 30,
		ag			=> 300,
		get_exp		=> 700,
		get_money	=> 300,
		icon		=> 'mon/582.gif',
		
		hit			=> 250, # 長期戦用命中率200%
		job			=> 41, # ﾄﾞﾗｺﾞﾝ
		sp			=> 999,
		old_job		=> 38, # ﾊﾞﾝﾊﾟｲｱ
		old_sp		=> 999,
		mp			=> 3000,
		tmp			=> '攻反撃',
	},
	{
		name		=> '悪の左目',
		hp			=> 3000,
		at			=> 380,
		df			=> 250,
		ag			=> 200,
		get_exp		=> 500,
		get_money	=> 100,
		icon		=> 'mon/581.gif',
		
		hit			=> 250, # 長期戦用命中率200%
		job			=> 57, # ｴﾙﾌ
		sp			=> 999,
		old_job		=> 50, # ｱｲﾃﾑ士
		old_sp		=> 90,
		mp			=> 999,
		tmp			=> '魔無効',
	},
);

# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = ();


# モンスター
@monsters = (
	{ # 0
		name		=> '黒ｽﾗｲﾑ',
		hp			=> 250,
		at			=> 300,
		df			=> 180,
		ag			=> 250,
		get_exp		=> 95,
		get_money	=> 85,
		icon		=> 'mon/160.gif',
		
		old_sp		=> 20,
		job			=> 39, # ｽﾗｲﾑ
		sp			=> 999,
		mp			=> 302,
		tmp			=> '魔吸収',
	},
	{ # 1
		name		=> '黒ﾄﾞﾗｷｰ',
		hp			=> 330,
		at			=> 380,
		df			=> 50,
		ag			=> 300,
		get_exp		=> 85,
		get_money	=> 65,
		icon		=> 'mon/161.gif',
		
		old_sp		=> 20,
		job			=> 38, # ﾊﾞﾝﾊﾟｲｱ
		sp			=> 90,
		mp			=> 333,
		state		=> '混乱',
	},
	{ # 2
		name		=> '黒ﾏﾈﾏﾈ',
		hp			=> 300,
		at			=> 250,
		df			=> 250,
		ag			=> 250,
		get_exp		=> 66,
		get_money	=> 66,
		icon		=> 'mon/162.gif',
		
		old_sp		=> 20,
		job			=> 36, # ものまね師
		sp			=> 999,
		mp			=> 362,
		tmp			=> '魔反撃',
	},
	{ # 3
		name		=> '黒ﾅｲﾄ',
		hp			=> 380,
		at			=> 390,
		df			=> 280,
		ag			=> 100,
		get_exp		=> 96,
		get_money	=> 46,
		icon		=> 'mon/163.gif',
		
		old_sp		=> 20,
		job			=> 1, # 戦士
		sp			=> 999,
		mp			=> 101,
		tmp			=> '攻反撃',
	},
	{ # 4
		name		=> '黒ﾎﾞﾑ',
		hp			=> 350,
		at			=> 280,
		df			=> 250,
		ag			=> 90,
		get_exp		=> 96,
		get_money	=> 46,
		icon		=> 'mon/164.gif',
		
		old_job		=> 94, # メガンテ
		old_sp		=> 20,
		job			=> 31, # 青魔道士じばく
		sp			=> 20,
		mp			=> 155,
		state		=> '眠り'
	},
	{ # 5
		name		=> '黒ﾄﾞｸﾛ',
		hp			=> 240,
		at			=> 270,
		df			=> 400,
		ag			=> 160,
		get_exp		=> 88,
		get_money	=> 88,
		icon		=> 'mon/165.gif',
		
		old_sp		=> 20,
		job			=> 58, # ﾀﾞｰｸｴﾙﾌ
		sp			=> 999,
		mp			=> 400,
		tmp			=> '魔軽減',
	},
);



1;
