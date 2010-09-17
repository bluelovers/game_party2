# 宝の中身
@treasures = (
[13..27], # 武器No
[13..19], # 防具No
[16..26,16..26,30,31,72..86], # 道具No
);

# ボス
@bosses= (
	{ # 7
		name		=> '死霊A',
		hp			=> 299,
		at			=> 119,
		df			=> 199,
		ag			=> 66,
		get_exp		=> 63,
		get_money	=> 13,
		icon		=> 'mon/072.gif',

		job			=> 31, # 青魔道士じばく、きゅうけつ、しのルーレット、？？？？、マイティガード
		sp			=> 60,
		mp			=> 42,
	},
	{
		name		=> '死霊の騎士',
		hp			=> 5500,
		at			=> 260,
		df			=> 180,
		ag			=> 180,
		get_exp		=> 666,
		get_money	=> 444,
		icon		=> 'mon/566.gif',
		
		hit			=> 200, # 長期戦用命中率150%
		job			=> 24, # 魔剣士かえんぎり、メタルぎり、バイキルト、いなずまぎり
		sp			=> 70,
		old_job		=> 2, # 剣士
		old_sp		=> 999,
		mmp			=> 5000,
		mp			=> 999,
		tmp			=> '受流し',
	},
	{ # 7
		name		=> '死霊B',
		hp			=> 299,
		at			=> 119,
		df			=> 199,
		ag			=> 66,
		get_exp		=> 63,
		get_money	=> 13,
		icon		=> 'mon/072.gif',

		job			=> 31, # 青魔道士じばく、きゅうけつ、しのルーレット、？？？？、マイティガード
		sp			=> 60,
		mp			=> 42,
	},
);

# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = ();


# モンスター
@monsters = (
	{ # 0
		name		=> 'ﾌﾞﾗｯﾄﾞﾊﾝﾄﾞ',
		hp			=> 160,
		at			=> 130,
		df			=> 50,
		ag			=> 60,
		get_exp		=> 41,
		get_money	=> 10,
		icon		=> 'mon/064.gif',

		job			=> 9, # 盗賊ボミエピオラいしつぶて
		sp			=> 10,
		old_job		=> 61, # ﾈｸﾛﾏﾝｻｰ よびだす
		old_sp		=> 10,
		mp			=> 41,
	},
	{ # 1
		name		=> 'ﾏﾐｰ',
		hp			=> 170,
		at			=> 150,
		df			=> 60,
		ag			=> 60,
		get_exp		=> 43,
		get_money	=> 16,
		icon		=> 'mon/041.gif',
		old_sp		=> 20,
	},
	{ # 2
		name		=> 'ｽｶﾙﾍｯﾄﾞ',
		hp			=> 90,
		at			=> 90,
		df			=> 180,
		ag			=> 60,
		get_exp		=> 44,
		get_money	=> 20,
		icon		=> 'mon/056.gif',

		job			=> 26, # 忍者かえんのいき、やけつくいき、マヌーサ、もうどくのきり、マホトーン
		sp			=> 60,
		mp			=> 96,
	},
	{ # 3
		name		=> '影の騎士',
		hp			=> 200,
		at			=> 170,
		df			=> 30,
		ag			=> 64,
		get_exp		=> 43,
		get_money	=> 25,
		icon		=> 'mon/044.gif',

		job			=> 24, # 魔剣士かえんぎり、メタルぎり、バイキルト、いなずまぎり
		sp			=> 30,
		mp			=> 16,
	},
	{ # 4
		name		=> 'ｼｬﾄﾞｰ',
		hp			=> 94,
		at			=> 90,
		df			=> 185,
		ag			=> 114,
		get_exp		=> 41,
		get_money	=> 20,
		icon		=> 'mon/046.gif',

		job			=> 41, # ﾄﾞﾗｺﾞﾝつめたいいき、こおりのいき
		sp			=> 30,
		mp			=> 44,
	},
	{ # 5
		name		=> 'あやしい影',
		hp			=> 98,
		at			=> 110,
		df			=> 190,
		ag			=> 144,
		get_exp		=> 43,
		get_money	=> 30,
		icon		=> 'mon/047.gif',

		job			=> 93, # 即死ザキ
		sp			=> 30,
		mp			=> 44,
	},
	{ # 6
		name		=> 'ｽﾗｲﾑﾊﾞｯﾄ',
		hp			=> 140,
		at			=> 145,
		df			=> 60,
		ag			=> 185,
		get_exp		=> 40,
		get_money	=> 15,
		icon		=> 'mon/027.gif',
		
		job			=> 38, # ﾊﾞﾝﾊﾟｲｱきゅうけつ、アスピル
		sp			=> 20,
		mp			=> 54,
	},
	{ # 7
		name		=> '死霊',
		hp			=> 199,
		at			=> 119,
		df			=> 199,
		ag			=> 66,
		get_exp		=> 45,
		get_money	=> 13,
		icon		=> 'mon/072.gif',

		job			=> 31, # 青魔道士じばく、きゅうけつ、しのルーレット、？？？？、マイティガード
		sp			=> 60,
		mp			=> 42,
	},
	{ # 8
		name		=> 'ﾊﾞﾌﾞﾙﾎﾟｲｽﾞﾝ',
		hp			=> 180,
		at			=> 160,
		df			=> 80,
		ag			=> 60,
		get_exp		=> 39,
		get_money	=> 21,
		icon		=> 'mon/237.gif',

		job			=> 90, # どくこうげき、ポイズン
		sp			=> 20,
		mp			=> 92,
	},
	{ # 9
		name		=> 'ﾃﾞﾋﾞﾙｷｬｯﾄ',
		hp			=> 160,
		at			=> 140,
		df			=> 80,
		ag			=> 160,
		get_exp		=> 41,
		get_money	=> 22,
		icon		=> 'mon/231.gif',

		job			=> 40, # ﾊｸﾞﾚﾏﾀﾙメラミ
		sp			=> 25,
		mp			=> 32,
	},
	{ # 10
		name		=> 'ｷﾘﾏ',
		hp			=> 200,
		at			=> 100,
		df			=> 10,
		ag			=> 200,
		get_exp		=> 50,
		get_money	=> 10,
		icon		=> 'mon/528.gif',

		job			=> 51, # 光魔道士まぶしいひかり,ひかりのみちびき,いやしのひかり,あやしいひかり,ひかりのさばき
		sp			=> 110,
		mp			=> 62,
	},
);



1;
