# 設定
%k = (
	p_name		=> '@二重世界@',# クエスト名
	p_join		=> 6,				# 戦闘参加上限(人)
	p_leader	=> '闇のｸﾘｽﾀﾙ',	# クエストリーダー名
	speed		=> 12,				# 進行スピード(秒)
	need_join	=> 'hp_200_o',		# 参加条件(./lib/quest.cgi 192行目あたりを参考)
);

# 封印戦戦利品(道具No)
@treasures = (
[], # 武器No
[], # 防具No
[23,59,60..65,107], # 道具No
);

# ボス
@bosses= (
	{
		name		=> '闇のｸﾘｽﾀﾙ',
		hp			=> 150000,
		at			=> 500,
		df			=> 300,
		ag			=> 300,
		get_exp		=> 4000,
		get_money	=> 3000,
		icon		=> 'mon/706.gif',
		
		hit			=> 900, # 長期戦用命中率400%
		job			=> 95, # 召喚
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
		name		=> '悪魔の鏡',
		hp			=> 300,
		at			=> 400,
		df			=> 300,
		ag			=> 300,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/570.gif',

		job			=> 20, # 悪魔
		sp			=> 999,
		old_job		=> 36, # ものまね師
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '魔反撃',
	},
	{ # 1
		name		=> '呪いの鏡',
		hp			=> 300,
		at			=> 400,
		df			=> 300,
		ag			=> 300,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/571.gif',

		job			=> 58, # ﾀﾞｰｸｴﾙﾌ
		sp			=> 999,
		old_job		=> 36, # ものまね師
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '魔反撃',
	},
	{ # 2
		name		=> '暗黒の鏡',
		hp			=> 300,
		at			=> 400,
		df			=> 300,
		ag			=> 300,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/572.gif',

		job			=> 22, # 暗黒騎士
		sp			=> 999,
		old_job		=> 36, # ものまね師
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '魔反撃',
	},
	{ # 3
		name		=> '月夜の鏡',
		hp			=> 300,
		at			=> 400,
		df			=> 300,
		ag			=> 300,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/573.gif',

		job			=> 51, # 光魔道士
		sp			=> 999,
		old_job		=> 36, # ものまね師
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '魔反撃',
	},
);


1;
