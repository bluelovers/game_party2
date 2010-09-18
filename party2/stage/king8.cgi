# 設定
%k = (
	p_name		=> '@闇でおおいつくす者@',	# クエスト名
	p_join		=> 6,				# 戦闘参加上限(人)
	p_leader	=> '魔人のツボ',	# クエストリーダー名
	speed		=> 12,				# 進行スピード(秒)
	need_join	=> 'hp_400_u',		# 参加条件(./lib/quest.cgi 192行目あたりを参考)
);


# 封印戦戦利品(道具No)
@treasures = (
[], # 武器No
[], # 防具No
[23,23,23,59,59..65,107], # 道具No
);

# ボス
@bosses= (
	{
		name		=> '魔人のツボ',
		hp			=> 80000,
		at			=> 300,
		df			=> 400,
		ag			=> 250,
		get_exp		=> 2500,
		get_money	=> 2000,
		icon		=> 'mon/605.gif',
		
		hit			=> 800, # 長期戦用命中率400%
		job			=> 95, # 召喚
		sp			=> 999,
		old_job		=> 95, # 召喚
		old_sp		=> 999,
		mmp			=> 999999,
		mp			=> 99999,
		tmp			=> '攻軽減',
	},
);


# 召喚されるモンスター
@monsters = (
	{ # 0
		name		=> '青魔人',
		hp			=> 250,
		at			=> 380,
		df			=> 50,
		ag			=> 150,
		get_exp		=> 100,
		get_money	=> 70,
		icon		=> 'mon/606.gif',

		old_sp		=> 20,
		job			=> 4, # 武闘家
		sp			=> 999,
		mp			=> 300,
		tmp			=> '攻反撃',
	},
	{ # 1
		name		=> '赤魔人',
		hp			=> 250,
		at			=> 380,
		df			=> 50,
		ag			=> 150,
		get_exp		=> 100,
		get_money	=> 70,
		icon		=> 'mon/607.gif',

		old_sp		=> 20,
		job			=> 1, # 戦士
		sp			=> 999,
		mp			=> 300,
		tmp			=> '攻反撃',
	},
	{ # 2
		name		=> '黒魔人',
		hp			=> 250,
		at			=> 380,
		df			=> 50,
		ag			=> 150,
		get_exp		=> 100,
		get_money	=> 70,
		icon		=> 'mon/608.gif',

		old_sp		=> 20,
		job			=> 52, # 魔人
		sp			=> 999,
		mp			=> 300,
		tmp			=> '攻反撃',
	},
	{ # 3
		name		=> '白魔人',
		hp			=> 250,
		at			=> 380,
		df			=> 50,
		ag			=> 150,
		get_exp		=> 100,
		get_money	=> 70,
		icon		=> 'mon/609.gif',

		old_sp		=> 20,
		job			=> 25, # モンク
		sp			=> 999,
		mp			=> 300,
		tmp			=> '攻反撃',
	},
);




1;
