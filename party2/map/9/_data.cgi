# 宝の中身
@treasures = (
[18..28,33..37], # 武器No
[18..31,36..38], # 防具No
[4..6,13,28,29,37,38,40,40,57,60..65,87,104..107], # 道具No
);

# ボス
@bosses= (
	{
		name		=> 'サイクロプスA',
		hp			=> 5000,
		at			=> 600,
		df			=> 50,
		ag			=> 100,
		get_exp		=> 500,
		get_money	=> 10,
		icon		=> 'mon/565.gif',
		old_sp		=> 20,
		job			=> 1, # 戦士
		sp			=> 999,
		old_job		=> 52, # 魔人
		mp			=> 999,
		tmp			=> '攻反撃',
	},
	{
		name		=> 'ナイトゴーレム',
		hp			=> 8000,
		at			=> 560,
		df			=> 400,
		ag			=> 200,
		get_exp		=> 1600,
		get_money	=> 200,
		icon		=> 'mon/701.gif',
		
		old_sp		=> 20,
		hit			=> 500, # 長期戦用命中率
		job			=> 97, # 超攻撃型
		sp			=> 999,
		mmp			=> 99999,
		mp			=> 4999,
		tmp			=> '攻無効',
	},
	{
		name		=> 'サイクロプスB',
		hp			=> 5000,
		at			=> 600,
		df			=> 50,
		ag			=> 100,
		get_exp		=> 500,
		get_money	=> 10,
		icon		=> 'mon/565.gif',
		old_sp		=> 20,
		job			=> 24, # 魔剣士
		sp			=> 999,
		old_job		=> 21, # 狂戦士
		mp			=> 999,
		tmp			=> '攻反撃',
	},
);

# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = ();

# モンスター
@monsters = (
	{
		name		=> 'キングベヒーモス',
		hp			=> 600,
		at			=> 350,
		df			=> 200,
		ag			=> 160,
		get_exp		=> 150,
		get_money	=> 100,
		icon		=> 'mon/554.gif',
		old_sp		=> 20,
		job			=> 21, # 狂戦士
		sp			=> 999,
		mp			=> 149,
		state		=> '魔封',
	},
	{
		name		=> 'イクロプス',
		hp			=> 700,
		at			=> 500,
		df			=> 50,
		ag			=> 100,
		get_exp		=> 170,
		get_money	=> 10,
		icon		=> 'mon/564.gif',
		old_sp		=> 20,
		job			=> 1, # 戦士
		sp			=> 999,
		old_job		=> 21, # 狂戦士
		mp			=> 999,
		state		=> '魔封',
	},
	{
		name		=> 'ストーンゴーレム',
		hp			=> 500,
		at			=> 350,
		df			=> 500,
		ag			=> 100,
		get_exp		=> 150,
		get_money	=> 250,
		icon		=> 'mon/547.gif',

		old_sp		=> 30,
		job			=> 3, # 騎士
		sp			=> 999,
		mp			=> 155,
		state		=> '魔封',
	},
	{
		name		=> 'ミラーナイト',
		hp			=> 300,
		at			=> 300,
		df			=> 300,
		ag			=> 300,
		get_exp		=> 100,
		get_money	=> 100,
		icon		=> 'mon/520.gif',

		job			=> 36, # ものまね士
		sp			=> 999,
		mp			=> 94,
		state		=> '魔封',
	},
	{
		name		=> 'キラーマシン',
		hp			=> 444,
		at			=> 333,
		df			=> 66,
		ag			=> 66,
		get_exp		=> 96,
		get_money	=> 96,
		icon		=> 'mon/521.gif',
		
		job			=> 24, # 魔剣士
		sp			=> 999,
		old_job		=> 11, # 弓使い
		old_sp		=> 999,
		mp			=> 333,
		state		=> '魔封',
	},
	{
		name		=> '竜魔人',
		hp			=> 480,
		at			=> 370,
		df			=> 80,
		ag			=> 50,
		get_exp		=> 145,
		get_money	=> 50,
		icon		=> 'mon/523.gif',
		
		old_sp		=> 20,
		job			=> 23, # 竜騎士
		sp			=> 999,
		mp			=> 285,
		state		=> '魔封',
	},
	{
		name		=> 'デスマシン',
		hp			=> 555,
		at			=> 333,
		df			=> 111,
		ag			=> 111,
		get_exp		=> 111,
		get_money	=> 111,
		icon		=> 'mon/522.gif',

		job			=> 24, # 魔剣士
		sp			=> 999,
		old_job		=> 11, # 弓使い
		old_sp		=> 999,
		mp			=> 111,
		state		=> '魔封',
	},
	{
		name		=> '白騎士',
		hp			=> 400,
		at			=> 350,
		df			=> 300,
		ag			=> 250,
		get_exp		=> 150,
		get_money	=> 100,
		icon		=> 'mon/501.gif',

		job			=> 54, # 魔銃士
		sp			=> 999,
		old_job		=> 17, # 聖騎士
		old_sp		=> 999,
		mp			=> 200,
		state		=> '魔封',
	},
	{
		name		=> '幻騎士',
		hp			=> 380,
		at			=> 370,
		df			=> 360,
		ag			=> 350,
		get_exp		=> 140,
		get_money	=> 130,
		icon		=> 'mon/502.gif',

		job			=> 53, # 蟲師
		sp			=> 999,
		old_job		=> 49, # たまねぎ剣士
		old_sp		=> 999,
		mp			=> 320,
		state		=> '魔封',
	},
);




1; # 削除不可
