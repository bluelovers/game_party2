# 設定
%k = (
	p_name		=> '@無限に増殖する者@',	# クエスト名
	p_join		=> 6,						# 戦闘参加上限(人)
	p_leader	=> 'ｽﾗｲﾑﾎﾞｯｸｽ',			# クエストリーダー名
	speed		=> 12,						# 進行スピード(秒)
	need_join	=> 'hp_100_u',				# 参加条件(./lib/quest.cgi 192行目あたりを参考)
);


# 封印戦戦利品(道具No)
@treasures = (
[], # 武器No
[], # 防具No
[1..43,59,72..89,101..103,107], # 道具No
);

# ボス
@bosses= (
	{
		name		=> 'ｽﾗｲﾑﾎﾞｯｸｽ',
		hp			=> 15000,
		at			=> 60,
		get_exp		=> 1500,
		get_money	=> 500,
		icon		=> 'mon/600.gif',
		
		hit			=> 300, # 長期戦用命中率300%
		job			=> 95, # 召喚
		sp			=> 999,
		mmp			=> 99999,
		mp			=> 9999,
		tmp			=> '攻軽減',
	},
);


# 召喚されるモンスター
@monsters = (
	{ # 0
		name		=> 'ﾌﾞﾁｽﾗｲﾑ',
		hp			=> 20,
		at			=> 36,
		ag			=> 20,
		get_exp		=> 6,
		get_money	=> 3,
		icon		=> 'mon/001.gif',
		old_sp		=> 20,
	},
	{ # 1
		name		=> 'ｽﾗｲﾑ',
		hp			=> 25,
		at			=> 40,
		ag			=> 20,
		get_exp		=> 9,
		get_money	=> 4,
		icon		=> 'mon/002.gif',
		old_sp		=> 20,
	},
	{ # 2
		name		=> 'ｽﾗｲﾑﾍﾞｽ',
		hp			=> 30,
		at			=> 45,
		df			=> 5,
		ag			=> 25,
		get_exp		=> 10,
		get_money	=> 5,
		icon		=> 'mon/003.gif',
		old_sp		=> 20,
	},
	{ # 3
		name		=> 'ﾊﾞﾌﾞﾙｽﾗｲﾑ',
		hp			=> 40,
		at			=> 45,
		df			=> 10,
		ag			=> 30,
		get_exp		=> 15,
		get_money	=> 10,
		icon		=> 'mon/020.gif',

		job			=> 90, # どくこうげき、ポイズン
		sp			=> 20,
		mp			=> 52,
	},
	{ # 4
		name		=> 'ﾎｲﾐｽﾗｲﾑ',
		hp			=> 40,
		at			=> 35,
		ag			=> 40,
		get_exp		=> 20,
		get_money	=> 15,
		icon		=> 'mon/010.gif',

		job			=> 5, # 僧侶スカラ、キアリー、ホイミ
		sp			=> 6,
		mp			=> 65,
	},
	{ # 5
		name		=> 'ｽﾗｲﾑまどう',
		hp			=> 40,
		at			=> 30,
		ag			=> 45,
		get_exp		=> 24,
		get_money	=> 11,
		icon		=> 'mon/013.gif',

		job			=> 19, # 闇魔道士ルカナン,マホカンタ,メダパニ
		sp			=> 16,
		mp			=> 114,
	},
	{ # 6
		name		=> 'ﾒﾀﾙｽﾗｲﾑ',
		hp			=> 6,
		at			=> 60,
		df			=> 2500,
		ag			=> 1500,
		get_exp		=> 250,
		get_money	=> 10,
		icon		=> 'mon/004.gif',

		job			=> 39, # スライムギラ
		sp			=> 3,
		old_job		=> 99, # 逃げる
		old_sp		=> 0,
		mp			=> 51,
		tmp			=> '魔無効',
	},
);


1;
