# 設定
%k = (
	p_name		=> '@全てを破壊する者@',# クエスト名
	p_join		=> 6,					# 戦闘参加上限(人)
	p_leader	=> '悪魔の書',			# クエストリーダー名
	speed		=> 12,					# 進行スピード(秒)
	need_join	=> 'hp_300_o',			# 参加条件(./lib/quest.cgi 192行目あたりを参考)
);

# 封印戦戦利品(道具No)
@treasures = (
[], # 武器No
[], # 防具No
[59,59,71,71], # 道具No
);

# ボス
@bosses= (
	{
		name		=> '悪魔の書',
		hp			=> 160000,
		at			=> 100,
		df			=> 100,
		ag			=> 700,
		get_exp		=> 5000,
		get_money	=> 5000,
		icon		=> 'mon/615.gif',
		
		job			=> 98, # 超魔法型
		sp			=> 999,
		old_job		=> 95, # 召喚
		old_sp		=> 999,
		mmp			=> 999999,
		mp			=> 99999,
		tmp			=> '魔無効',
	},
);


# 召喚されるモンスター
@monsters = (
	{
		name		=> '一賢者',
		hp			=> 250,
		at			=> 100,
		df			=> 60,
		ag			=> 300,
		get_exp		=> 70,
		get_money	=> 150,
		icon		=> 'mon/508.gif',

		job			=> 51, # 光魔道士
		sp			=> 999,
		old_job		=> 16, # 白魔道士
		old_sp		=> 999,
		mp			=> 399,
		tmp			=> '魔無効',
	},
	{
		name		=> '二賢者',
		hp			=> 250,
		at			=> 100,
		df			=> 60,
		ag			=> 300,
		get_exp		=> 70,
		get_money	=> 150,
		icon		=> 'mon/507.gif',
		
		job			=> 15, # 黒魔道士
		sp			=> 999,
		old_job		=> 40, # ハグレメタル
		old_sp		=> 999,
		mp			=> 299,
		tmp			=> '魔吸収',
	},
	{
		name		=> '三賢者',
		hp			=> 250,
		at			=> 100,
		df			=> 60,
		ag			=> 300,
		get_exp		=> 70,
		get_money	=> 150,
		icon		=> 'mon/509.gif',
		
		job			=> 6, # 魔法使い
		sp			=> 999,
		old_job		=> 19, # 闇魔道士
		old_sp		=> 999,
		mp			=> 399,
		tmp			=> '魔反撃',
	},
	{
		name		=> '四賢者',
		hp			=> 250,
		at			=> 100,
		df			=> 60,
		ag			=> 300,
		get_exp		=> 70,
		get_money	=> 150,
		icon		=> 'mon/511.gif',

		job			=> 33, # 賢者
		sp			=> 999,
		old_job		=> 30, # 赤魔道士
		old_sp		=> 999,
		mp			=> 399,
		tmp			=> '魔反撃',
	},
	{
		name		=> '青魔',
		hp			=> 400,
		at			=> 200,
		df			=> 100,
		ag			=> 400,
		get_exp		=> 70,
		get_money	=> 150,
		icon		=> 'mon/250.gif',

		job			=> 31, # 青魔道士
		sp			=> 999,
		old_job		=> 95, # 召喚
		old_sp		=> 999,
		mp			=> 299,
		tmp			=> '魔吸収',
	},
	{
		name		=> '黒魔',
		hp			=> 320,
		at			=> 120,
		df			=> 60,
		ag			=> 300,
		get_exp		=> 80,
		get_money	=> 160,
		icon		=> 'mon/254.gif',

		job			=> 15, # 黒魔道士
		sp			=> 999,
		old_job		=> 95, # 召喚
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '魔無効',
	},
	{
		name		=> 'ミニモン',
		hp			=> 350,
		at			=> 500,
		df			=> 200,
		ag			=> 500,
		get_exp		=> 66,
		get_money	=> 66,
		icon		=> 'mon/245.gif',

		job			=> 56, # ミニデーモン
		sp			=> 999,
		old_job		=> 95, # 召喚
		old_sp		=> 999,
		mp			=> 301,
		state		=> '混乱',
	},
	{
		name		=> 'スライムまどう',
		hp			=> 260,
		at			=> 180,
		df			=> 50,
		ag			=> 400,
		get_exp		=> 100,
		get_money	=> 150,
		icon		=> 'mon/013.gif',
		job			=> 19, # 闇魔道士
		sp			=> 999,
		old_job		=> 40, # ハグレメタル
		old_sp		=> 999,
		mp			=> 384,
	},
);


1;
