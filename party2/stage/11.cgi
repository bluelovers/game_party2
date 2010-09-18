# 宝の中身
@treasures = (
[15..23], # 武器No
[17..27], # 防具No
[16..26,16..26,27,35,72..86], # 道具No
);


# ボス
@bosses= (
	{
		name		=> '竜王',
		hp			=> 8000,
		at			=> 300,
		df			=> 240,
		ag			=> 100,
		get_exp		=> 999,
		get_money	=> 500,
		icon		=> 'mon/560.gif',
		
		hit			=> 200, # 長期戦用命中率150%
		job			=> 41, # ドラゴン
		sp			=> 999,
		old_job		=> 25, # モンク、
		old_sp		=> 1999,
		mmp			=> 8000,
		mp			=> 3000,
		tmp			=> '息反撃',
	},
	{
		name		=> 'ブルーストーン',
		hp			=> 15,
		at			=> 200,
		df			=> 5000,
		ag			=> 1000,
		get_exp		=> 70,
		get_money	=> 500,
		icon		=> 'mon/191.gif',
		
		job			=> 33, # 賢者
		sp			=> 130,
		old_job		=> 31, # 青魔道士
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '魔無効',
	},
);

# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = (0,0,1,1,2,2,3,3,4,5,6,7,8);

# モンスター
@monsters = (
	{ # 0
		name		=> 'プチヒーロー',
		hp			=> 220,
		at			=> 140,
		df			=> 120,
		ag			=> 110,
		get_exp		=> 50,
		get_money	=> 20,
		icon		=> 'mon/105.gif',

		old_sp		=> 20,
		job			=> 34, # 勇者かばう、ライデイン、いてつくはどう
		sp			=> 60,
		mp			=> 61,
	},
	{ # 1
		name		=> 'プチファイター',
		hp			=> 250,
		at			=> 170,
		df			=> 150,
		ag			=> 20,
		get_exp		=> 50,
		get_money	=> 20,
		icon		=> 'mon/106.gif',

		old_sp		=> 20,
		job			=> 1, # 戦士
		sp			=> 999,
		mp			=> 41,
	},
	{ # 2
		name		=> 'プチマージ',
		hp			=> 160,
		at			=> 100,
		df			=> 60,
		ag			=> 150,
		get_exp		=> 50,
		get_money	=> 20,
		icon		=> 'mon/107.gif',

		job			=> 6, # 魔法使いメラ、ルカニ、ギラ、マヌーサ、メラミ、ラリホー、べギラマ
		sp			=> 60,
		mp			=> 191,
	},
	{ # 3
		name		=> 'プチプリースト',
		hp			=> 170,
		at			=> 120,
		df			=> 80,
		ag			=> 90,
		get_exp		=> 50,
		get_money	=> 20,
		icon		=> 'mon/108.gif',

		job			=> 5, # 僧侶スカラ、キアリー、ホイミ、バギ、ベホイミ、バギマ
		sp			=> 55,
		mp			=> 181,
	},
	{ # 4
		name		=> 'ブルードラゴン',
		hp			=> 150,
		at			=> 155,
		df			=> 80,
		ag			=> 120,
		get_exp		=> 51,
		get_money	=> 15,
		icon		=> 'mon/226.gif',

		job			=> 41, # ドラゴンつめたいいき、こおりのいき
		sp			=> 90,
		mp			=> 38,
	},
	{ # 5
		name		=> 'ハクリュウ',
		hp			=> 200,
		at			=> 160,
		df			=> 90,
		ag			=> 180,
		get_exp		=> 60,
		get_money	=> 20,
		icon		=> 'mon/232.gif',

		job			=> 26, # 忍者かえんのいき、やけつくいき、マヌーサ、もうどくのきり、マホトーン
		sp			=> 60,
		mp			=> 69,
	},
	{ # 6
		name		=> 'サラマンダー',
		hp			=> 280,
		at			=> 170,
		df			=> 150,
		ag			=> 110,
		get_exp		=> 63,
		get_money	=> 24,
		icon		=> 'mon/533.gif',

		job			=> 26, # 忍者かえんのいき、やけつくいき、マヌーサ、もうどくのきり、マホトーン
		sp			=> 60,
		mp			=> 79,
	},
	{ # 7
		name		=> 'ドラゴンマット',
		hp			=> 300,
		at			=> 200,
		df			=> 170,
		ag			=> 50,
		get_exp		=> 66,
		get_money	=> 20,
		icon		=> 'mon/556.gif',

		job			=> 41, # ドラゴン
		sp			=> 100,
		mp			=> 99,
	},
	{ # 8
		name		=> 'デンデンリュウ',
		hp			=> 340,
		at			=> 210,
		df			=> 180,
		ag			=> 120,
		get_exp		=> 68,
		get_money	=> 22,
		icon		=> 'mon/550.gif',

		job			=> 41, # ドラゴン
		sp			=> 30,
		old_job		=> 26, # 忍者かえんのいき、やけつくいき
		old_sp		=> 15,
		mp			=> 99,
	},
);



1;
