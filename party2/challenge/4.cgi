# 設定
%k = (
	p_join		=> 4,			# 戦闘参加上限(人)
	need_join	=> '0',			# 参加条件(./lib/quest.cgi 192行目あたりを参考)
);

# 宝部屋(10階～20階以上。上位階ほど確率アップ)
$tresure_round = int(rand(11)+10);


# 宝の中身
@treasures = (
[], # 武器No
[], # 防具No
[6,15,57,72..74,87,101..103], # 道具No
);


# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = ();

# モンスター
@monsters = (
	{ # 0
		name		=> 'イタズラ妖精',
		hp			=> 320,
		at			=> 240,
		df			=> 100,
		ag			=> 300,
		get_exp		=> 40,
		get_money	=> 50,
		icon		=> 'mon/110.gif',

		job			=> 31, # 青魔道士じばく,しのルーレット
		sp			=> 44,
		old_job		=> 8, # 遊び人
		old_sp		=> 999,
		mmp			=> 9999,
		mp			=> 100,
		ten			=> 3,
	},
	{ # 1
		name		=> 'ギャンブル妖精',
		hp			=> 320,
		at			=> 240,
		df			=> 100,
		ag			=> 300,
		get_exp		=> 40,
		get_money	=> 50,
		icon		=> 'mon/111.gif',

		job			=> 31, # 青魔道士じばく,しのルーレット
		sp			=> 44,
		old_job		=> 36, # ギャンブラー
		old_sp		=> 999,
		mmp			=> 9999,
		mp			=> 100,
		ten			=> 3,
	},
	{ # 2
		name		=> 'ブルーストーン',
		hp			=> 5,
		at			=> 200,
		df			=> 2000,
		ag			=> 500,
		get_exp		=> 50,
		get_money	=> 100,
		icon		=> 'mon/191.gif',
		
		job			=> 31, # 青魔道士じばく,しのルーレット
		sp			=> 44,
		old_job		=> 31, # 青魔道士じばく,しのルーレット
		old_sp		=> 44,
		mmp			=> 9999,
		mp			=> 100,
		tmp			=> '魔無効',
	},
	{ # 3
		name		=> 'あやしい影',
		hp			=> 280,
		at			=> 280,
		df			=> 160,
		ag			=> 200,
		get_exp		=> 45,
		get_money	=> 40,
		icon		=> 'mon/047.gif',

		job			=> 93, # 即死ザキ、ザラキ
		sp			=> 20,
		old_job		=> 93, # 即死ザキ、ザラキ
		old_sp		=> 20,
		mmp			=> 9999,
		mp			=> 70,
	},
	{ # 4
		name		=> 'ミミック',
		hp			=> 420,
		at			=> 280,
		df			=> 70,
		ag			=> 400,
		get_exp		=> 50,
		get_money	=> 100,
		icon		=> 'mon/091.gif',
		
		job			=> 93, # 即死ザキ、ザラキ
		sp			=> 20,
		old_job		=> 93, # 即死ザキ、ザラキ
		old_sp		=> 20,
		mmp			=> 9999,
		mp			=> 120,
		tmp			=> '２倍', 
	},
	{ # 5
		name		=> 'パンドラボックス',
		hp			=> 450,
		at			=> 300,
		df			=> 75,
		ag			=> 600,
		get_exp		=> 70,
		get_money	=> 120,
		icon		=> 'mon/092.gif',
		
		job			=> 93, # 即死ザキ、ザラキ
		sp			=> 20,
		old_job		=> 93, # 即死ザキ、ザラキ
		old_sp		=> 20,
		mmp			=> 9999,
		mp			=> 120,
		tmp			=> '２倍', 
	},
);



1; # 削除不可
