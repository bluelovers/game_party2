# 宝の中身
@treasures = (
[29..40], # 武器No
[35..40], # 防具No
[59,59,59,59], # 道具No
);

# ボス
@bosses= (
	{
		name		=> 'シルバーストーン',
		hp			=> 20,
		at			=> 500,
		df			=> 8000,
		ag			=> 3000,
		get_exp		=> 100,
		get_money	=> 1000,
		icon		=> 'mon/196.gif',
		
		job			=> 51, # 光魔道士
		sp			=> 999,
		old_job		=> 54, # 魔銃士
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '魔無効',
	},
	{
		name		=> '片翼の天使',
		hp			=> 12000,
		at			=> 500,
		df			=> 300,
		ag			=> 300,
		get_exp		=> 3000,
		get_money	=> 2000,
		icon		=> 'mon/569.gif',
		
		hit			=> 500, # 長期戦用命中率
		job			=> 98, # 超魔法型
		sp			=> 999,
		old_job		=> 48, # 堕天使
		old_sp		=> 999,
		mmp			=> 30000,
		mp			=> 8000,
		tmp			=> '魔反撃',
	},
	{
		name		=> 'ブラックストーン',
		hp			=> 20,
		at			=> 500,
		df			=> 8000,
		ag			=> 3000,
		get_exp		=> 100,
		get_money	=> 1000,
		icon		=> 'mon/195.gif',
		
		job			=> 58, # ダークエルフ
		sp			=> 999,
		old_job		=> 53, # 蟲師
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '魔無効',
	},
);

# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = ();


# モンスター
@monsters = (
	{
		name		=> '天猫青',
		hp			=> 400,
		at			=> 400,
		df			=> 200,
		ag			=> 400,
		get_exp		=> 100,
		get_money	=> 100,
		icon		=> 'mon/640.gif',

		job			=> 10, # 羊使い
		sp			=> 999,
		old_job		=> 32, # 召喚士
		old_sp		=> 999,
		mp			=> 199,
	},
	{
		name		=> '天猫赤',
		hp			=> 400,
		at			=> 400,
		df			=> 200,
		ag			=> 400,
		get_exp		=> 100,
		get_money	=> 100,
		icon		=> 'mon/641.gif',

		job			=> 48, # 堕天使
		sp			=> 999,
		old_job		=> 30, # 赤魔道士
		old_sp		=> 999,
		mp			=> 199,
	},
	{
		name		=> '天猫黄',
		hp			=> 400,
		at			=> 400,
		df			=> 200,
		ag			=> 400,
		get_exp		=> 100,
		get_money	=> 100,
		icon		=> 'mon/642.gif',

		job			=> 44, # チョコボ
		sp			=> 999,
		old_job		=> 40, # ハグレメタル
		old_sp		=> 999,
		mp			=> 199,
	},
	{
		name		=> '天卵',
		hp			=> 500,
		at			=> 350,
		df			=> 400,
		ag			=> 150,
		get_exp		=> 150,
		get_money	=> 120,
		icon		=> 'mon/630.gif',

		job			=> 18, # 天使
		sp			=> 999,
		old_job		=> 45, # モーグリ
		old_sp		=> 999,
		mp			=> 164,
	},
);



1;
