# 設定
%k = (
	p_join		=> 3,			# 戦闘参加上限(人)
	need_join	=> '0',			# 参加条件(./lib/quest.cgi 192行目あたりを参考)
);

# 宝部屋(20階～40階以上。上位階ほど確率アップ)
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
		name		=> 'オバケキノコ',
		hp			=> 400,
		at			=> 300,
		df			=> 150,
		ag			=> 300,
		get_exp		=> 30,
		get_money	=> 20,
		icon		=> 'mon/030.gif',

		job			=> 42, # アサシン
		sp			=> 999,
		old_job		=> 91, # マヒ系
		old_sp		=> 999,
		mmp			=> 9999,
		mp			=> 99,
	},
	{ # 1
		name		=> 'ドクキノコ',
		hp			=> 400,
		at			=> 300,
		df			=> 150,
		ag			=> 300,
		get_exp		=> 40,
		get_money	=> 30,
		icon		=> 'mon/031.gif',

		job			=> 90, # 毒系
		sp			=> 999,
		old_job		=> 20, # 悪魔
		old_sp		=> 999,
		mmp			=> 9999,
		mp			=> 99,
	},
	{ # 2
		name		=> 'マージマタンゴ',
		hp			=> 400,
		at			=> 300,
		df			=> 150,
		ag			=> 300,
		get_exp		=> 50,
		get_money	=> 40,
		icon		=> 'mon/032.gif',

		job			=> 90, # 毒系
		sp			=> 999,
		old_job		=> 19, # 闇魔道士
		old_sp		=> 999,
		mmp			=> 9999,
		mp			=> 99,
	},
);



1; # 削除不可
