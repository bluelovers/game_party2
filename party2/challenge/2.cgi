# 設定
%k = (
	p_join		=> 2,			# 戦闘参加上限(人)
	need_join	=> '0',			# 参加条件(./lib/quest.cgi 192行目あたりを参考)
);

# 宝部屋(10階～20階以上。上位階ほど確率アップ)
$tresure_round = int(rand(11)+10);


# 宝の中身
@treasures = (
[], # 武器No
[], # 防具No
[4..6,10..13,23,57,72..74,85..87,101..103], # 道具No
);


# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = ();

# モンスター
@monsters = (
	{ # 0
		name		=> 'ｺﾞｰｽﾄ',
		hp			=> 340,
		at			=> 200,
		df			=> 150,
		ag			=> 200,
		get_exp		=> 30,
		get_money	=> 20,
		icon		=> 'mon/035.gif',

		job			=> 93, # 即死
		sp			=> 999,
		old_sp		=> 20,
		mp			=> 40,
	},
	{ # 1
		name		=> 'ﾒｲｼﾞｺﾞｰｽﾄ',
		hp			=> 360,
		at			=> 210,
		df			=> 160,
		ag			=> 220,
		get_exp		=> 31,
		get_money	=> 22,
		icon		=> 'mon/036.gif',

		job			=> 6, # 魔法使い
		sp			=> 999,
		old_sp		=> 20,
		mp			=> 70,
	},
	{ # 2
		name		=> 'ﾐｲﾗ男',
		hp			=> 420,
		at			=> 300,
		df			=> 60,
		ag			=> 160,
		get_exp		=> 40,
		get_money	=> 5,
		icon		=> 'mon/040.gif',
		
		job			=> 9, # 盗賊
		sp			=> 999,
		old_sp		=> 20,
		mp			=> 20,
	},
	{ # 3
		name		=> 'ﾏﾐｰ',
		hp			=> 510,
		at			=> 320,
		df			=> 80,
		ag			=> 180,
		get_exp		=> 45,
		get_money	=> 6,
		icon		=> 'mon/041.gif',

		job			=> 58, # ﾀﾞｰｸｴﾙﾌ
		sp			=> 999,
		old_sp		=> 20,
		mp			=> 70,
	},
	{ # 4
		name		=> 'ｶﾞｲｺﾂ剣士',
		hp			=> 400,
		at			=> 350,
		df			=> 120,
		ag			=> 150,
		get_exp		=> 40,
		get_money	=> 20,
		icon		=> 'mon/043.gif',
		
		job			=> 2, # 剣士
		sp			=> 999,
		old_sp		=> 20,
		mp			=> 40,
	},
	{ # 5
		name		=> 'ﾌﾞﾗｯﾄﾞﾊﾝﾄﾞ',
		hp			=> 380,
		at			=> 280,
		df			=> 150,
		ag			=> 200,
		get_exp		=> 35,
		get_money	=> 25,
		icon		=> 'mon/064.gif',

		job			=> 61, # ﾈｸﾛﾏﾝｻｰ よびだす
		sp			=> 10,
		old_sp		=> 20,
		mp			=> 62,
	},
	{ # 6
		name		=> '死霊',
		hp			=> 299,
		at			=> 229,
		df			=> 199,
		ag			=> 229,
		get_exp		=> 42,
		get_money	=> 30,
		icon		=> 'mon/072.gif',

		job			=> 31, # 青魔道士
		sp			=> 999,
		old_sp		=> 20,
		mp			=> 66,
	},
);



1; # 削除不可
