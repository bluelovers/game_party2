# 宝の中身
@treasures = (
[9..18], # 武器No
[9..18], # 防具No
[15..26,72..86], # 道具No
);

# ボス
@bosses= (
	{
		name		=> 'ﾎﾞﾑA',
		hp			=> 100,
		at			=> 80,
		df			=> 80,
		ag			=> 80,
		get_exp		=> 55,
		get_money	=> 30,
		icon		=> 'mon/071.gif',

		old_sp		=> 20,
		job			=> 20, # 青魔道士じばく
		sp			=> 10,
		mp			=> 42,
	},
	{
		name		=> 'ひくいどり',
		hp			=> 1800,
		at			=> 160,
		df			=> 70,
		ag			=> 80,
		get_exp		=> 300,
		get_money	=> 180,
		icon		=> 'mon/530.gif',
		
		hit			=> 150, # 長期戦用命中率150%
		job			=> 26, # 忍者かえんのいき、やけつくいき
		sp			=> 15,
		old_job		=> 27, # 風水師すなけむり
		old_sp		=> 10,
		mp			=> 97,
		tmp			=> '息軽減',
	},
	{
		name		=> 'ﾎﾞﾑB',
		hp			=> 100,
		at			=> 80,
		df			=> 80,
		ag			=> 80,
		get_exp		=> 55,
		get_money	=> 30,
		icon		=> 'mon/071.gif',

		old_sp		=> 20,
		job			=> 20, # 青魔道士じばく
		sp			=> 10,
		mp			=> 42,
	},
);

# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = ();


# モンスター
@monsters = (
	{ # 0
		name		=> 'ﾌｧｲｱｰｽﾗｲﾑ',
		hp			=> 100,
		at			=> 77,
		df			=> 58,
		ag			=> 82,
		get_exp		=> 25,
		get_money	=> 12,
		icon		=> 'mon/008.gif',

		job			=> 6, # 魔法使いメラ
		sp			=> 16,
		mp			=> 100,
	},
	{ # 1
		name		=> 'ﾏｸﾞﾏｽﾗｲﾑ',
		hp			=> 130,
		at			=> 93,
		df			=> 70,
		ag			=> 30,
		get_exp		=> 30,
		get_money	=> 27,
		icon		=> 'mon/021.gif',
		old_sp		=> 30,
	},
	{ # 2
		name		=> '爆弾岩',
		hp			=> 100,
		at			=> 86,
		df			=> 40,
		ag			=> 10,
		get_exp		=> 50,
		get_money	=> 15,
		icon		=> 'mon/080.gif',

		job			=> 94, # 自爆メガンテ、ねる
		sp			=> 20,
		mp			=> 42,
	},
	{ # 3
		name		=> 'ﾁｸﾘ',
		hp			=> 111,
		at			=> 111,
		df			=> 75,
		ag			=> 20,
		get_exp		=> 34,
		get_money	=> 25,
		icon		=> 'mon/211.gif',

		old_sp		=> 30,
		job			=> 21, # 狂戦士たいあたり、うけながし
		sp			=> 10,
		mp			=> 26,
	},
	{ # 4
		name		=> 'ﾎﾞﾑ',
		hp			=> 70,
		at			=> 60,
		df			=> 80,
		ag			=> 60,
		get_exp		=> 35,
		get_money	=> 20,
		icon		=> 'mon/071.gif',

		old_sp		=> 20,
		job			=> 20, # 青魔道士じばく
		sp			=> 10,
		mp			=> 42,
	},
	{ # 5
		name		=> 'ﾁﾋﾞﾄﾞﾗｺﾞﾝ',
		hp			=> 120,
		at			=> 78,
		df			=> 65,
		ag			=> 66,
		get_exp		=> 30,
		get_money	=> 12,
		icon		=> 'mon/083.gif',

		job			=> 12, # 魔物使いひのいき
		sp			=> 5,
		mp			=> 26,
	},
	{ # 6
		name		=> 'ﾌﾞﾗｯｸﾄﾞﾗｺ',
		hp			=> 110,
		at			=> 90,
		df			=> 100,
		ag			=> 50,
		get_exp		=> 32,
		get_money	=> 20,
		icon		=> 'mon/084.gif',

		job			=> 26, # 忍者かえんのいき
		sp			=> 5,
		mp			=> 17,
	},
	{ # 7
		name		=> 'ﾄﾞﾗｺﾞﾝ',
		hp			=> 200,
		at			=> 140,
		df			=> 75,
		ag			=> 68,
		get_exp		=> 60,
		get_money	=> 24,
		icon		=> 'mon/224.gif',

		job			=> 26, # 忍者かえんのいき、やけつくいき
		sp			=> 15,
		mp			=> 21,
	},
	{ # 8
		name		=> 'ﾁﾋﾞｴｯｸﾞ',
		hp			=> 80,
		at			=> 70,
		df			=> 80,
		ag			=> 100,
		get_exp		=> 20,
		get_money	=> 14,
		icon		=> 'mon/114.gif',

		job			=> 45, # ﾓｰｸﾞﾘおまじない、ストップ、ウールガード、カエルのうた
		sp			=> 100,
		mp			=> 60,
	},
	{ # 9
		name		=> 'ﾐﾆﾀｳﾙｽ',
		hp			=> 140,
		at			=> 112,
		df			=> 50,
		ag			=> 90,
		get_exp		=> 26,
		get_money	=> 18,
		icon		=> 'mon/115.gif',

		old_sp		=> 30,
		job			=> 45, # 羊使いねる、スカラ、たいあたり
		sp			=> 10,
		mp			=> 20,
	},
	{ # 10
		name		=> '炎の戦士',
		hp			=> 110,
		at			=> 152,
		df			=> 30,
		ag			=> 60,
		get_exp		=> 28,
		get_money	=> 10,
		icon		=> 'mon/576.gif',

		old_sp		=> 20,
		job			=> 26, # 忍者かえんのいき
		sp			=> 5,
		mp			=> 27,
	},
);



1;
