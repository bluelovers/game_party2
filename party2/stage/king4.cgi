# 設定
%k = (
	p_name		=> '@全てを呪う者@',# クエスト名
	p_join		=> 6,				# 戦闘参加上限(人)
	p_leader	=> '暗黒の盾',		# クエストリーダー名
	speed		=> 12,				# 進行スピード(秒)
	need_join	=> 'hp_300_o',		# 参加条件(./lib/quest.cgi 192行目あたりを参考)
);

# 封印戦戦利品(道具No)
@treasures = (
[], # 武器No
[], # 防具No
[59,71,107], # 道具No
);

# ボス
@bosses= (
	{
		name		=> '暗黒の剣',
		hp			=> 100000,
		at			=> 500,
		df			=> 200,
		ag			=> 250,
		get_exp		=> 6000,
		get_money	=> 3000,
		icon		=> 'mon/707.gif',
		
		hit			=> 900, # 長期戦用命中率700%
		job			=> 22, # 暗黒騎士
		sp			=> 999,
		old_job		=> 95, # 召喚
		old_sp		=> 999,
		mmp			=> 999999,
		mp			=> 99999,
		tmp			=> '攻反撃',
	},
	{
		name		=> '暗黒の盾',
		hp			=> 100000,
		at			=> 300,
		df			=> 600,
		ag			=> 250,
		get_exp		=> 7000,
		get_money	=> 4000,
		icon		=> 'mon/708.gif',
		
		hit			=> 900, # 長期戦用命中率700%
		job			=> 35, # 結界士
		sp			=> 999,
		old_job		=> 95, # 召喚
		old_sp		=> 999,
		mmp			=> 999999,
		mp			=> 99999,
		tmp			=> '魔反撃',
	},
);


# 召喚されるモンスター
@monsters = (
	{ # 0
		name		=> '悪魔の剣',
		hp			=> 350,
		at			=> 500,
		df			=> 200,
		ag			=> 150,
		get_exp		=> 200,
		get_money	=> 50,
		icon		=> 'mon/620.gif',

		job			=> 20, # 悪魔
		sp			=> 999,
		old_job		=> 21, # バーサーカー
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '攻反撃',
	},
	{ # 1
		name		=> '闇の剣',
		hp			=> 350,
		at			=> 500,
		df			=> 200,
		ag			=> 150,
		get_exp		=> 200,
		get_money	=> 50,
		icon		=> 'mon/621.gif',

		job			=> 22, # 暗黒騎士
		sp			=> 999,
		old_job		=> 42, # アサシン
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '攻反撃',
	},
	{ # 2
		name		=> '呪の剣',
		hp			=> 350,
		at			=> 500,
		df			=> 200,
		ag			=> 150,
		get_exp		=> 200,
		get_money	=> 50,
		icon		=> 'mon/622.gif',

		job			=> 2, # 剣士
		sp			=> 999,
		old_job		=> 24, # 魔剣士
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '攻反撃',
	},
	{ # 3
		name		=> '悪魔の盾',
		hp			=> 350,
		at			=> 200,
		df			=> 500,
		ag			=> 200,
		get_exp		=> 150,
		get_money	=> 100,
		icon		=> 'mon/623.gif',

		job			=> 20, # 悪魔
		sp			=> 999,
		old_job		=> 48, # 堕天使
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '魔反撃',
	},
	{ # 4
		name		=> '呪の盾',
		hp			=> 350,
		at			=> 200,
		df			=> 500,
		ag			=> 200,
		get_exp		=> 150,
		get_money	=> 100,
		icon		=> 'mon/624.gif',

		job			=> 58, # ダークエルフ
		sp			=> 999,
		old_job		=> 56, # ミニデーモン
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '魔反撃',
	},
	{ # 5
		name		=> '闇の盾',
		hp			=> 350,
		at			=> 200,
		df			=> 500,
		ag			=> 200,
		get_exp		=> 150,
		get_money	=> 100,
		icon		=> 'mon/625.gif',

		job			=> 19, # 闇魔道士
		sp			=> 999,
		old_job		=> 31, # 青魔道士
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '魔反撃',
	},
	{ # 6
		name		=> '魔王の剣',
		hp			=> 350,
		at			=> 400,
		df			=> 400,
		ag			=> 300,
		get_exp		=> 200,
		get_money	=> 100,
		icon		=> 'mon/626.gif',

		job			=> 35, # 魔王
		sp			=> 999,
		old_job		=> 32, # 召喚士
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '攻反撃',
	},
);


1;
