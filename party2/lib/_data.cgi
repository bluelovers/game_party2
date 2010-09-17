#=================================================
# 職業・アイテム Created by Merino
# Noは管理側が何番目かわかるための印です。実際は配列の何番目かなので、削除並び換えをする場合は注意してください(Noを変更しただけでは意味がありません)
#=================================================

#=================================================
# 職業 ◎追加/変更 △削除/並び替え
# ※成長率(例＞3の場合は、レベルアップ時に0〜3上がる。ただし、HPは成長率が0でも最低1上がる仕様[./lib/_battle.cgi90行目])。
# ・道具消費で転職できる職業名を変更する場合は、./lib/job_change.cgiの道具を消費することで転職可能な職業も変更してください。
# ・./lib/_skill.cgiのスキル「sub skill_**」の数字番号は、@jobsの並び順と連動しています(例＞騎士を削除する場合は、「sub skill_3」を削除し、「sub skill_4」以降を１ずつ繰り上げ)。
#=================================================
@jobs = (
#0No	1名前,		※2HP,3MP,4力,5守,6素,		7転職条件
[0,		'----',			0,	0,	0,	0,	0,		sub{ 0 }],
[1,		'戦士',			6,	1,	3,	5,	2,		sub{ 1 }],
[2,		'剣士',			4,	1,	4,	2,	3,		sub{ 1 }],
[3,		'騎士',			6,	2,	2,	6,	2,		sub{ 1 }],
[4,		'武闘家',		4,	2,	3,	2,	4,		sub{ 1 }],
[5,		'僧侶',			3,	5,	2,	3,	3,		sub{ 1 }],
[6,		'魔法使い',		3,	6,	1,	1,	3,		sub{ 1 }],
[7,		'商人',			5,	2,	3,	4,	3,		sub{ 1 }],
[8,		'遊び人',		2,	1,	1,	1,	3,		sub{ 1 }],
[9,		'盗賊',			3,	3,	3,	1,	5,		sub{ 1 }],
[10,	'羊飼い',		4,	3,	2,	4,	2,		sub{ 1 }],
[11,	'弓使い',		4,	3,	3,	2,	4,		sub{ 1 }],
[12,	'魔物使い',		4,	2,	2,	3,	2,		sub{ 1 }],

[13,	'吟遊詩人',		4,	4,	2,	3,	4,		sub{ $m{sex} eq 'm' }],
[14,	'踊り子',		3,	4,	3,	2,	5,		sub{ $m{sex} eq 'f' }],
[15,	'黒魔道士',		3,	6,	1,	2,	3,		sub{ $m{sex} eq 'm' }],
[16,	'白魔道士',		3,	5,	2,	2,	3,		sub{ $m{sex} eq 'f' }],

[17,	'聖騎士',		4,	2,	3,	5,	2,		sub{ $m{sex} eq 'm' && &_is_need_job(1,2,3,17,22) }],
[18,	'天使',			4,	5,	2,	3,	4,		sub{ $m{sex} eq 'f' && &_is_need_job(5,8,10,14,16,18) }],
[19,	'闇魔道士',		3,	6,	2,	1,	3,		sub{ $m{sex} eq 'm' && &_is_need_job(6,8,15,19,51) }],
[20,	'悪魔',			3,	4,	3,	6,	3,		sub{ $m{sex} eq 'f' && &_is_need_job(6,8,20,22) }],

[21,	'ﾊﾞｰｻｰｶｰ',		6,	1,	5,	3,	2,		sub{ $m{kill_m} > 200 && &_is_need_job(1,4,12,21) }],
[22,	'暗黒騎士',		4,	3,	5,	1,	2,		sub{ $m{kill_p} > 50  && &_is_need_job(2,3,17,20,22,52) }],
[23,	'竜騎士',		4,	1,	3,	4,	5,		sub{ &_is_need_job(9,11,23,26) }],
[24,	'魔剣士',		3,	5,	4,	2,	2,		sub{ &_is_need_job(2,6,24,30) }],
[25,	'ﾓﾝｸ',			5,	1,	4,	3,	3,		sub{ &_is_need_job(4,12,21,25) }],
[26,	'忍者',			3,	3,	3,	2,	6,		sub{ &_is_need_job(9,11,23,26,53) }],
[27,	'風水士',		4,	3,	2,	4,	4,		sub{ &_is_need_job(7,8,10,27) }],
[28,	'侍',			4,	2,	4,	3,	4,		sub{ &_is_need_job(2,24,26,28) }],

[29,	'時魔道士',		3,	5,	1,	2,	4,		sub{ &_is_need_job(13,14,15,16,29) }],
[30,	'赤魔道士',		4,	3,	4,	3,	3,		sub{ &_is_need_job(15,16,29,30) }],
[31,	'青魔道士',		3,	4,	2,	2,	5,		sub{ &_is_need_job(8,13,14,27,31) }],
[32,	'召喚士',		3,	6,	1,	2,	3,		sub{ &_is_need_job(19,20,29,32) }],

[33,	'賢者',			3,	5,	1,	2,	2,		sub{ &_is_need_job(8,33) ||  $m{ite} eq '27' }],
[34,	'勇者',			5,	2,	4,	4,	2,		sub{ &_is_need_job(34)   || ($m{ite} eq '28' && $m{hero_c} >= 5) }],
[35,	'魔王',			4,	5,	3,	4,	4,		sub{ &_is_need_job(35)   || ($m{ite} eq '29' && $m{mao_c}  >= 1) }],
[36,	'ものまね士',	3,	3,	3,	3,	3,		sub{ &_is_need_job(36)   ||  $m{ite} eq '32' }],
[37,	'結界士',		3,	5,	3,	5,	3,		sub{ &_is_need_job(37)   ||  $m{ite} eq '30' }],
[38,	'ﾊﾞﾝﾊﾟｲｱ',		3,	4,	4,	1,	5,		sub{ &_is_need_job(38)   ||  $m{ite} eq '31' }],
[39,	'ｽﾗｲﾑ',			3,	4,	2,	3,	4,		sub{ &_is_need_job(39)   ||  $m{ite} eq '33' }],
[40,	'ﾊｸﾞﾚﾒﾀﾙ',		1,	7,	1,	7,	7,		sub{ &_is_need_job(40)   ||  $m{ite} eq '34' }],
[41,	'ﾄﾞﾗｺﾞﾝ',		6,	1,	6,	6,	1,		sub{ &_is_need_job(41)   ||  $m{ite} eq '35' }],
[42,	'ｱｻｼﾝ',			3,	2,	5,	1,	6,		sub{ &_is_need_job(42)   ||  $m{ite} eq '36' }],
[43,	'医術師',		4,	4,	1,	3,	3,		sub{ &_is_need_job(5,10,16,43,51) }],
[44,	'ﾁｮｺﾎﾞ',		6,	1,	3,	2,	5,		sub{ &_is_need_job(44)   ||  $m{ite} eq '37' }],
[45,	'ﾓｰｸﾞﾘ',		3,	4,	2,	4,	4,		sub{ &_is_need_job(45)   ||  $m{ite} eq '38' }],
[46,	'ｷﾞｬﾝﾌﾞﾗｰ',		3,	5,	3,	1,	5,		sub{ &_is_need_job(46)   || ($m{ite} eq '39' && $m{cas_c} >= 10) }],
[47,	'ｿﾙｼﾞｬｰ',		6,	1,	6,	4,	4,		sub{ $m{sex} eq 'm' && (&_is_need_job(47) || $m{ite} eq '40') }],
[48,	'堕天使',		3,	5,	4,	2,	3,		sub{ $m{sex} eq 'f' && (&_is_need_job(48) || $m{ite} eq '40') }],

[49,	'たまねぎ剣士',	$m{sp}*0.02,$m{sp}*0.02,$m{sp}*0.02,$m{sp}*0.02,$m{sp}*0.02,sub{ &_is_need_job(49) || $m{sp} >= 300 }],
[50,	'ｱｲﾃﾑ士',		3,	4,	2,	3,	4,		sub{ &_is_need_job(7,27,43,50) }],
[51,	'光魔道士',		3,	5,	2,	3,	4,		sub{ &_is_need_job(16,17,18,19,33,51) }],
[52,	'魔人',			5,	2,	5,	2,	3,		sub{ $m{kill_m} > 1000 && &_is_need_job(1,21,25,52) }],
[53,	'蟲師',			4,	3,	3,	4,	5,		sub{ &_is_need_job(8,12,26,53) }],
[54,	'魔銃士',		3,	4,	5,	1,	4,		sub{ &_is_need_job(54)   ||  $m{ite} eq '88' }],
[55,	'妖精',			3,	5,	2,	3,	5,		sub{ &_is_need_job(55)   ||  $m{ite} eq '75' }],
[56,	'ﾐﾆﾃﾞｰﾓﾝ',		3,	5,	2,	4,	4,		sub{ &_is_need_job(56)   ||  $m{ite} eq '85' }],
[57,	'ｴﾙﾌ',			4,	4,	3,	4,	4,		sub{ &_is_need_job(57)   ||  $m{ite} eq '13' }],
[58,	'ﾀﾞｰｸｴﾙﾌ',		3,	6,	3,	2,	4,		sub{ &_is_need_job(58)   ||  $m{ite} eq '89' }],

[59,	'ｽﾗｲﾑﾗｲﾀﾞｰ',	4,	3,	2,	1,	4,		sub{ &_is_need_job(59)   ||  $m{ite} eq '90' }],
[60,	'ﾄﾞﾗｺﾞﾝﾗｲﾀﾞｰ',	5,	2,	4,	4,	2,		sub{ &_is_need_job(60)   ||  $m{ite} eq '91' }],
[61,	'ﾈｸﾛﾏﾝｻｰ',		3,	5,	2,	1,	4,		sub{ &_is_need_job(61)   ||  $m{ite} eq '92' }],
[62,	'ﾊﾞｯﾄﾏｽﾀｰ',		4,	4,	3,	1,	5,		sub{ &_is_need_job(62)   ||  $m{ite} eq '93' }],
[63,	'ｷﾉｺﾏｽﾀｰ',		4,	3,	3,	3,	3,		sub{ &_is_need_job(63)   ||  $m{ite} eq '94' }],
[64,	'ｵﾊﾞｹﾏｽﾀｰ',		3,	4,	2,	3,	5,		sub{ &_is_need_job(64)   ||  $m{ite} eq '95' }],
[65,	'ｹﾓﾉﾏｽﾀｰ',		5,	2,	4,	3,	4,		sub{ &_is_need_job(65)   ||  $m{ite} eq '96' }],
[66,	'ﾄﾞｸﾛﾏｽﾀｰ',		4,	3,	3,	4,	3,		sub{ &_is_need_job(66)   ||  $m{ite} eq '97' }],
[67,	'ﾊﾞﾌﾞﾙﾏｽﾀｰ',	4,	4,	2,	2,	3,		sub{ &_is_need_job(67)   ||  $m{ite} eq '98' }],
[68,	'ｺﾛﾋｰﾛｰ',		5,	2,	4,	3,	3,		sub{ &_is_need_job(68)   ||  $m{ite} eq '99' }],
[69,	'ﾌﾟﾁﾋｰﾛｰ',		5,	2,	4,	3,	3,		sub{ &_is_need_job(69)   ||  $m{ite} eq '100' }],
[70,	'天竜人',		4,	5,	3,	2,	3,		sub{ &_is_need_job(70) }],
[71,	'ﾁｮｺﾎﾞﾗｲﾀﾞｰ',	5,	3,	2,	3,	2,		sub{ &_is_need_job(71)   ||  $m{ite} eq '108' }],
[72,	'算術士',		3,	6,	1,	3,	3,		sub{ &_is_need_job(72)   ||  $m{ite} eq '109' }],
[73,	'すっぴん',		5,	5,	4,	4,	4,		sub{ -f "$userdir/$id/comp_job_flag.cgi" }],
);
sub _is_need_job {
	my @need_jobs = @_;
	for my $need_job (@need_jobs) {
		return 1 if $m{job} eq $need_job || $m{old_job} eq $need_job;
	}
	return 0;
}


#=================================================
# 壁紙(表示は自動的に値段順になります) ◎追加/変更/削除/並び替え自由
#=================================================
%kabes = (
# 画像(./bgimgの中のファイル名) => 値段,
	'none.gif'			=> 0,
	'farm.gif'			=> 1000,
	'lot.gif'			=> 1000,
	'sp_change.gif'		=> 1500,
	'exile.gif'			=> 1500,
	'depot.gif'			=> 1500,
	'item.gif'			=> 2000,
	'medal.gif'			=> 2000,
	'bar.gif'			=> 2500,
	'casino.gif'		=> 2500,
	'goods.gif'			=> 2500,
	'armor.gif'			=> 3000,
	'job_change.gif'	=> 3000,
	'park.gif'			=> 3500,
	'auction.gif'		=> 4000,
	'weapon.gif'		=> 5000,
	'event.gif'			=> 5000,

	'stage0.gif'		=> 6000,
	'stage1.gif'		=> 6500,
	'stage2.gif'		=> 7000,
	'stage3.gif'		=> 7500,
	'stage4.gif'		=> 8000,
	'stage5.gif'		=> 8500,
	'stage6.gif'		=> 9000,
	'stage7.gif'		=> 9500,
	'stage8.gif'		=> 10000,
	'stage9.gif'		=> 10500,
	'stage10.gif'		=> 11000,
	'stage11.gif'		=> 11500,
	'stage12.gif'		=> 12000,
	'stage13.gif'		=> 12500,
	'stage14.gif'		=> 13000,
	
	'stage15.gif'		=> 20000,
	'stage16.gif'		=> 22000,
	'stage17.gif'		=> 24000,
	'stage18.gif'		=> 25000,
	'stage19.gif'		=> 30000,
	'stage20.gif'		=> 50000,

	'map1.gif'			=> 3000,
	'map2.gif'			=> 4500,
	'map3.gif'			=> 5000,
);

#=================================================
# 武器 ◎追加/変更/削除/並び替え自由
# $m{***}で自分のステータスの値を使うことが可能
#=================================================
@weas = (
#	[0]No,	[1]名前,			[2]価格,	[3]攻撃力,				[4]重さ,		
	[0,		'なし',				0,			0,						0,					],

	[1,		'ひのきの棒',		10,			2,						int(rand(2)),		],
	[2,		'竹の槍',			30,			4,						2,					],
	[3,		'こんぼう',			50,			int(int(rand(3))*8),	6,					],
	[4,		'かしの杖',			70,			6,						int(rand(5)),		],
	[5,		'いばらのむち',		180,		int(rand(15)),			5,					],
	[6,		'ﾌﾞﾛﾝｽﾞﾅｲﾌ',		120,		9,						int(rand(7)),		],
	[7,		'おおきづち',		250,		int(int(rand(2))*40),	12,					],
	[8,		'銅の剣',			400,		14,						9,					],
	[9,		'鎖がま',			540,		int(rand(24)),			10,					],

	[10,	'聖なるﾅｲﾌ',		670,		18,						int(rand(15)),		],
	[11,	'鉄の斧',			900,		int(int(rand(3))*30),	25,					],
	[12,	'どくばり',			1500,		int(int(rand(2))*42),	4,					],
	[13,	'鋼鉄の剣',			1800,		30,						20,					],

	[14,	'ﾙｰﾝｽﾀｯﾌ',			2100,		27,						int(rand(25)),		],
	[15,	'ｿﾞﾝﾋﾞｷﾗｰ',			3500,		44,						24,					],
	[16,	'ﾁｪｰﾝｸﾛｽ',			3700,		int(rand(60)),			20,					],
	[17,	'ｱｻｼﾝﾀﾞｶﾞｰ',		5500,		int(int(rand(4))*18),	16,					],
	[18,	'ｸｻﾅｷﾞの剣',		8500,		54,						34,					],

	[19,	'ﾎｰﾘｰﾗﾝｽ',			7500,		47,						int(rand(50)),		],
	[20,	'ﾊﾞﾄﾙｱｯｸｽ',			7200,		int(int(rand(3))*50),	38,					],
	[21,	'ﾓｰﾆﾝｸﾞｽﾀｰ',		9500,		int(rand(90)),			32,					],
	[22,	'ｳｫｰﾊﾝﾏｰ',			11000,		int(int(rand(2))*150),	50,					],
	[23,	'ﾄﾞﾗｺﾞﾝｷﾗｰ',		15000,		75,						45,					],

	[24,	'妖精の剣',			13000,		65,						int(rand(70)),		],
	[25,	'ﾃﾞｰﾓﾝｽﾋﾟｱ',		16000,		99,						66,					],
	[26,	'ﾄﾞﾗｺﾞﾝﾃｲﾙ',		19500,		int(rand(120)),			45,					],
	[27,	'ﾋﾞｯｸﾞﾎﾞｳｶﾞﾝ',		22500,		int(int(rand(2))*180),	60,					],
	[28,	'諸刃の剣',			2000,		-20,					int(rand(40)*-1),	],

	[29,	'隼の剣',			21000,		5,						int(rand(40)*-1),	],
	[30,	'奇跡の剣',			17700,		70,						int(int(rand(2))*20),],
	[31,	'ｷﾗｰﾋﾟｱｽ',			14000,		int(rand($m{ag}*1.2)),	int(rand(50)),		],
	[32,	'正義のｿﾛﾊﾞﾝ',		18750,		int(rand($m{df}*1.2)),	40,					],
	[33,	'ｶﾞｲｱの剣',			24000,		int(rand($m{at}*1.2)),	40,					],
	[34,	'理力の杖',			17000,		int(rand($m{mmp}*0.6)),	int(rand(70)),		],
	[35,	'天空の剣',			30000,		int(rand($m{mhp}*0.6)),	50,					],

	[36,	'ﾄﾞﾗｺﾞﾝの杖',		22000,		90,						int(rand(100)),		],
	[37,	'魔人の斧',			20000,		int(int(rand(2))*300),	70,					],
	[38,	'ｸﾞﾘﾝｶﾞﾑのむち',	28000,		int(rand(200)),			55,					],
	[39,	'破壊の鉄球',		27750,		int(int(rand(3))*150),	80,					],
	[40,	'ﾊｸﾞﾚﾒﾀﾙの剣',		30000,		150,					75,					],

# ＠パーティーIIIより追加
	[41,	'古びた剣',			10,			1,						30,					],
	[42,	'鉄の槍',			740,		22,						12,					],
	[43,	'ﾀﾞｶﾞｰﾅｲﾌ',			300,		14,						int(rand(11)),		],
	[44,	'おおかなづち',		850,		int(int(rand(2))*60),	15,					],
	[45,	'ﾛﾝｸﾞｽﾋﾟｱ',			1100,		31,						19,					],
	[46,	'ﾊﾞﾄﾙﾌｫｰｸ',			2000,		36,						10,					],
	[47,	'金の斧',			4000,		int(int(rand(4))*20),	30,					],
	[48,	'山賊の斧',			6000,		int(int(rand(7))*20),	55,					],
	[49,	'氷の刃',			7400,		52,						26,					],
	[50,	'吹雪の剣',			17000,		80,						39,					],
	[51,	'隼の剣･改',		27000,		45,						int(rand(40)*-1),	],
	[52,	'諸刃の剣･改',		6000,		-30,					int(rand(60)*-1),	],
	[53,	'ｳｫｰﾊﾝﾏｰ･改',		16000,		int(int(rand(3))*120),	60,					],
	[54,	'奇跡の剣･改',		21100,		85,						int(int(rand(2))*10),],
	[55,	'ｿﾞﾝﾋﾞﾊﾞｽﾀｰ',		14000,		65,						45,					],
	[56,	'ﾄﾞﾗｺﾞﾝｽﾚｲﾔｰ',		20000,		96,						50,					],
	[57,	'ﾊﾞｽﾀｰﾄﾞｿｰﾄﾞ',		8000,		60,						20,					],
	[58,	'ﾗｲﾄｼｬﾑｰﾙ',			21000,		110,					55,					],
	[59,	'ﾌﾟﾗﾁﾅｿｰﾄﾞ',		16000,		84,						40,					],
	[60,	'ﾒｶﾞﾄﾝﾊﾝﾏｰ',		22000,		int(int(rand(2))*300),	85,					],
	[61,	'ﾑｰﾝｱｯｸｽ',			12000,		int(int(rand(4))*70),	55,					],
	[62,	'ｷﾝｸﾞｱｯｸｽ',			28000,		int(int(rand(4))*90),	65,					],
	[63,	'覇王の斧',			30000,		int(int(rand(4))*100),	80,					],
	[64,	'聖銀のﾚｲﾋﾟｱ',		7000,		54,						16,					],
	[65,	'堕天使のﾚｲﾋﾟｱ',	12000,		61,						11,					],
	[66,	'疾風のﾚｲﾋﾟｱ',		20000,		78,						int(rand(30)*-1),	],
	[67,	'ﾒﾀﾙｷﾝｸﾞの剣',		40000,		165,					80,					],
	[68,	'ﾛﾄの剣',			50000,		180,					int(rand($m{hp}*0.2)),	],
	[69,	'竜神の剣',			40000,		int(rand($m{at}*1.2)),	40,					],
	[70,	'竜神王の剣',		50000,		int(rand($m{at}*1.6)),	50,					],
);

#=================================================
# 防具 ◎追加/変更/削除/並び替え自由
# 武器と違って$m{***}は使えないので注意(攻撃する側のステータスになってしまう)
#=================================================
@arms = (
#	No,		名前,				価格		守備力,					重さ
#	[0]		[1]					[2]     	[3]						[4]		
	[0,		'なし',				0,			0,						0,		],
	[1,		'布の服',			20,			3,						0,		],
	[2,		'旅人の服',			50,			5,						int(rand(2)),		],
	[3,		'ｽﾃﾃｺﾊﾟﾝﾂ',			70,			-2,						int(rand(12)*-1),	],

	[4,		'皮の鎧',			150,		12,						4,					],
	[5,		'皮の腰巻',			240,		int(rand(11)),			int(rand(6)),		],
	[6,		'うろこの鎧',		380,		int(rand(10)+7),		6,					],
	[7,		'鎖かたびら',		540,		24,						8,					],
	[8,		'毛皮のﾏﾝﾄ',		350,		int(rand(20)),			int(rand(10)),		],
	[9,		'ｽﾗｲﾑの服',			600,		30,						int(rand(18)),		],
	[10,	'青銅の鎧',			830,		int(rand(20)+15),		12,					],
	[11,	'鉄の鎧',			1200,		43,						17,					],
	[12,	'安らぎのﾛｰﾌﾞ',		1700,		34,						int(rand(20)),		],
	[13,	'さまよう鎧',		900,		int(int(rand(2))*90),	22,					],
	[14,	'みかわしの服',		2800,		0,						int(rand(55)*-1),	],

	[15,	'ｽﾗｲﾑｱｰﾏｰ',			3000,		int(rand(30)+10),		int(rand(20)),		],
	[16,	'鋼鉄の鎧',			3700,		52,						20,					],

	[17,	'ｿﾞﾝﾋﾞﾒｲﾙ',			4400,		int(rand(30)+30),		22,					],
	[18,	'魔法の法衣',		5400,		45,						int(rand(25)),		],
	[19,	'銀の胸当て',		6700,		73,						24,					],
	[20,	'ﾃﾞﾋﾞﾙｱｰﾏｰ',		2000,		int(int(rand(2))*140),	22,					],
	[21,	'賢者のﾛｰﾌﾞ',		9000,		62,						int(rand(30)),		],

	[22,	'刃の鎧',			7000,		int(int(rand(3))*40),	27,					],
	[23,	'忍びの服',			16000,		int(rand(25)),			int(rand(30)*-1),	],
	[24,	'天使のﾛｰﾌﾞ',		15000,		70,						int(rand(35)),		],
	[25,	'ﾌﾞﾗｯﾄﾞﾒｲﾙ',		3500,		int(int(rand(2))*180),	33,					],

	[26,	'ﾄﾞﾗｺﾞﾝﾒｲﾙ',		17500,		76,						30,					],
	[27,	'水の羽衣',			18500,		int(rand(50)+30),		int(rand(40)),		],
	[28,	'闇の衣',			19000,		int(rand(40)),			int(rand(40)*-1),	],
	[29,	'炎の鎧',			22000,		90,						34,					],
	[30,	'光の鎧',			24000,		int(rand(70)+40),		32,					],
	[31,	'地獄の鎧',			6000,		int(int(rand(2))*220),	44,					],

	[32,	'戦士のﾊﾟｼﾞｬﾏ',		2100,		int(rand(10)+5),		int(rand(20)*-1),	],
	[33,	'不思議なﾎﾞﾚﾛ',		7777,		int(int(rand(2))*77),	int(int(rand(2))*-77),	],
	[34,	'危ない水着',		12800,		int(rand(30)*-1),		int(rand(100)*-1),	],
	[35,	'神秘の鎧',			25000,		int(rand(50)+70),		int(10*int(rand(3))),],

	[36,	'ﾄﾞﾗｺﾞﾝﾛｰﾌﾞ',		27000,		100,					int(rand(50)),		],
	[37,	'天空の鎧',			30000,		int(rand(50)+100),		42,					],
	[38,	'魔人の鎧',			18000,		int(int(rand(2))*300),	55,					],
	[39,	'王者のﾏﾝﾄ',		28000,		int(rand(150)),			int(rand(40)),		],
	[40,	'ﾊｸﾞﾚﾒﾀﾙの鎧',		30000,		150,					45,					],

# ＠パーティーIII追加分
	[41,	'古びた鎧',			10,			1,						30,					],
	[42,	'騎士団の服',		1200,		32,						int(rand(14)),		],
	[43,	'ｼﾙﾊﾞｰﾒｲﾙ',			2400,		55,						17,					],
	[44,	'ﾗｲﾄｱｰﾏｰ',			4700,		int(rand(35)+25),		20,					],
	[45,	'あつでの鎧',		5000,		75,						40,					],
	[46,	'金の胸当て',		16000,		92,						40,					],
	[47,	'ﾌﾟﾗﾁﾅﾒｲﾙ',			20000,		95,						38,					],
	[48,	'盗賊の衣',			14000,		int(rand(20)),			int(rand(10)*-5),	],
	[49,	'紅蓮のﾛｰﾌﾞ',		28000,		int(rand(40)),			int(rand(15)*-4),	],
	[50,	'ﾄﾞﾗｺﾞﾝｱｰﾏｰ',		27000,		90,						int(rand(50)),		],
	[51,	'ｷﾞｶﾞﾝﾄｱｰﾏｰ',		30000,		int(int(rand(3))*160),	60,					],
	[52,	'ﾒﾀﾙｷﾝｸﾞの鎧',		40000,		165,					50,					],
	[53,	'ﾛﾄの鎧',			50000,		180,					55,					],
	[54,	'竜神の鎧',			40000,		int(rand(10)*25),		int(rand(15)*5),	],
	[55,	'竜神王の鎧',		50000,		int(rand(15)*25),		int(rand(10)*5),	],
);


#=================================================
# 道具 ◎追加/変更　△削除/並び替え自由(転職ｱｲﾃﾑなど配列番号で指定しているので変更する必要あり)
# ※使用可能場所[0=自動(ダーマ神殿など),1=戦闘中の＠どうぐ,2=＠ほーむ,3=戦闘中自動,4=クエスト参加時]
#=================================================
@ites = (
#	[0]No,	[1]名前,			[2]価格,[3]※使用場所,	[4]効果
	[0,		'なし',				0,			0,			sub{	}],
	[1,		'薬草',				30,			1,			sub{ &_heal(shift, 40, '道具');		}],
	[2,		'上薬草',			100,		1,			sub{ &_heal(shift, 100, '道具');		}],
	[3,		'特薬草',			300,		1,			sub{ &_heal(shift, 250, '道具');	}],
	[4,		'賢者の石',			1500,		1,			sub{ &_heals(200, '道具');	}],
	[5,		'世界樹のしずく',	5000,		1,			sub{ &_heals(999, '道具');	}],
	[6,		'世界樹の葉',		5000,		1,			sub{ my($y) = &_check_party(shift, '蘇生', '道具'); return if !$y || $ms{$y}{hp} > 0; $com.=qq|なんと、<b>$y</b>が <span class="revive">生き返り</span> ました！|; $ms{$y}{hp}=$ms{$y}{mhp};		}],
	[7,		'毒消し草',			20,			1,			sub{ &_st_h(shift, '猛毒', '道具');		}],
	[8,		'満月草',			20,			1,			sub{ &_st_h(shift, '麻痺', '道具');		}],
	[9,		'天使の鈴',			20,			1,			sub{ &_st_h(shift, '混乱', '道具');		}],
	[10,	'ﾊﾟﾃﾞｷｱの根っこ',	250,		1,			sub{ my($y) = &_check_party(shift, '治療', '道具'); return if !$y; &_st_h($y, $ms{$y}{state}, '道具');		}],
	[11,	'魔法の聖水',		500,		1,			sub{ &_mp_h(shift, 40,  '道具');	}],
	[12,	'祈りの指輪',		2000,		1,			sub{ &_mp_h(shift, 100, '道具');	}],
	[13,	'ｴﾙﾌの飲み薬',		8000,		1,			sub{ &_mp_h(shift, 999, '道具');	}],
	[14,	'守りの石',			100,		1,			sub{ my($y) = &_check_party(shift, '攻軽減', '道具'); return if !$y; $ms{$y}{tmp} = '攻軽減'; $com.=qq|<span class="tmp">$yはゴーレムに守られている！</span>|;		}],
	[15,	'魔法の鏡',			300,		1,			sub{ my($y) = &_check_party(shift, '魔反撃', '道具'); return if !$y; $ms{$y}{tmp} = '魔反撃'; $com.=qq|<span class="tmp">$yは魔法の壁で守られた！</span>|;		}],
	[16,	'命の木の実',		500,		2,			sub{ my $v = int(rand(4)+3); $m{mhp}+=$v; $com.="$mの$e2j{hp}が $v あがった！";	}],
	[17,	'不思議な木の実',	500,		2,			sub{ my $v = int(rand(4)+3); $m{mmp}+=$v; $com.="$mの$e2j{mp}が $v あがった！";	}],
	[18,	'力の種',			500,		2,			sub{ my $v = int(rand(6)+1); $m{at}+=$v; $com.="$mの$e2j{at}が $v あがった！";	}],
	[19,	'守りの種',			500,		2,			sub{ my $v = int(rand(6)+1); $m{df}+=$v; $com.="$mの$e2j{df}が $v あがった！";	}],
	[20,	'素早さの種',		500,		2,			sub{ my $v = int(rand(6)+1); $m{ag}+=$v; $com.="$mの$e2j{ag}が $v あがった！";	}],
	[21,	'ｽｷﾙの種',			1000,		2,			sub{ my $v = int(rand(3)+1); $m{sp}+=$v; $com.="$mの$e2j{sp}が $v あがった！";	}],
	[22,	'幸せの種',			3000,		2,			sub{ $m{exp} = $m{lv} * $m{lv} * 10; $com.="次のクエスト時にレベルアップ！";		}],
	[23,	'小さなﾒﾀﾞﾙ',		500,		2,			sub{ $m{medal}++; $com.="メダル王にメダルを１枚献上しました";	}],
	[24,	'ﾓﾝｽﾀｰ銅貨',		1000,		0,			sub{	}],
	[25,	'ﾓﾝｽﾀｰ銀貨',		3000,		0,			sub{	}],
	[26,	'ﾓﾝｽﾀｰ金貨',		6000,		0,			sub{	}],

	[27,	'賢者の悟り',		10000,		0,			sub{	}],
	[28,	'勇者の証',			10000,		0,			sub{	}],
	[29,	'邪神像',			10000,		0,			sub{	}],
	[30,	'精霊の守り',		5000,		0,			sub{	}],
	[31,	'伯爵の血',			5000,		0,			sub{	}],
	[32,	'ﾏﾈﾏﾈの心',			5000,		0,			sub{	}],
	[33,	'ｽﾗｲﾑの心',			5000,		0,			sub{	}],
	[34,	'ﾊｸﾞﾚﾒﾀﾙの心',		8000,		0,			sub{	}],
	[35,	'ﾄﾞﾗｺﾞﾝの心',		5000,		0,			sub{	}],
	[36,	'闇のﾛｻﾞﾘｵ',		8000,		0,			sub{	}],
	[37,	'ｷﾞｻﾞｰﾙの野菜',		8000,		0,			sub{	}],
	[38,	'ｸﾎﾟの実',			5000,		0,			sub{	}],
	[39,	'ｷﾞｬﾝﾌﾞﾙﾊｰﾄ',		5000,		0,			sub{	}],
	[40,	'ｼﾞｪﾉﾊﾞ細胞',		10000,		0,			sub{	}],

	[41,	'ﾄﾞﾗｺﾞﾝ草',			150,		1,			sub{ &_damage(shift, 80, '道具', 1);		}],
	[42,	'爆弾石',			300,		1,			sub{ &_damages(60, '道具', 1);				}],
	[43,	'へんげの杖',		1000,		2,			sub{ my $no = sprintf("%03d",int(rand(108)+1)); $m{icon} = (-f "$icondir/mon/$no.gif") ? "mon/$no.gif" : "chr/038.gif"; $com.="$mはモンスターに姿を変えた！"	}],
	[44,	'ﾋﾟﾝｸｽｶｰﾄ',			300,		2,			sub{ $m{icon} = 'chr/001.gif'; $com.="$mはﾋﾟﾝｸｽｶｰﾄのコスプレをした！"	}],
	[45,	'ﾀﾝｸﾄｯﾌﾟﾊﾝﾏｰ',		300,		2,			sub{ $m{icon} = 'chr/005.gif'; $com.="$mはﾀﾝｸﾄｯﾌﾟﾊﾝﾏｰのコスプレをした！"	}],
	[46,	'ﾁｮﾋﾞﾋｹﾞﾀｸｼｰﾄﾞ',	300,		2,			sub{ $m{icon} = $m{sex} eq 'm' ? 'chr/012.gif' : 'chr/007.gif';  $com.="$mはﾁｮﾋﾞﾋｹﾞﾀｸｼｰﾄﾞのコスプレをした！"	}],
	[47,	'ﾈｺﾐﾐﾒｲﾄﾞ',			300,		2,			sub{ $m{icon} = 'chr/004.gif'; $com.="$mはﾈｺﾐﾐﾒｲﾄﾞのコスプレをした！"	}],
	[48,	'ﾎﾋﾞｯﾄ',			300,		2,			sub{ $m{icon} = 'chr/014.gif'; $com.="$mはﾎﾋﾞｯﾄのコスプレをした！"	}],
	[49,	'ﾊﾅﾒｶﾞﾈ',			300,		2,			sub{ $m{icon} = 'chr/021.gif'; $com.="$mはﾊﾅﾒｶﾞﾈのコスプレをした！"	}],
	[50,	'ぬいぐるみ',		300,		2,			sub{ $m{icon} = 'chr/023.gif'; $com.="$mはぬいぐるみのコスプレをした！"	}],
	[51,	'冒険家の衣装',		300,		2,			sub{ $m{icon} = 'chr/003.gif'; $com.="$mは冒険家のコスプレをした！"	}],
	[52,	'騎士団の衣装',		300,		2,			sub{ $m{icon} = 'chr/015.gif'; $com.="$mは騎士団のコスプレをした！"	}],
	[53,	'老人の衣装',		300,		2,			sub{ $m{icon} = 'chr/013.gif'; $com.="$mは老人のコスプレをした！"	}],
	[54,	'精霊の衣装',		300,		2,			sub{ $m{icon} = 'chr/011.gif'; $com.="$mは精霊のコスプレをした！"	}],
	[55,	'聖職者の衣装',		400,		2,			sub{ $m{icon} = $m{sex} eq 'm' ? 'chr/016.gif' : 'chr/017.gif'; $com.="$mは聖職者のコスプレをした！"	}],
	[56,	'王族の衣装',		500,		2,			sub{ $m{icon} = $m{sex} eq 'm' ? 'chr/002.gif' : 'chr/018.gif'; $com.="$mは王様のコスプレをした！"	}],

	[57,	'ﾌｧｲﾄ一発',			3000,		2,			sub{ $m{tired} = 0; $com.="元気全快！$mの疲労が回復した！";	}],
	[58,	'ｴｯﾁな本',			100,		2,			sub{ $m{icon}="job/8_$m{sex}.gif"; $m{mes}="性格：ムッツリスケベ"; $com.="$mはｴｯﾁな本をじっくり読んだ………<br />$mの性格がムッツリスケベになった！"; open my $fh, "+< $userdir/$id/profile.cgi" or return; my $line=<$fh>; my $new_line=''; for my $hash (split /<>/, $line) { my($k, $v) = split /;/, $hash; next if $k eq 'character'; $new_line .= "$k;$v<>"; }; $new_line.="character;ムッツリスケベ<>"; seek $fh, 0, 0; truncate $fh, 0; print $fh $new_line; close $fh;	&write_news(qq|<span class="whisper">＠ささやき>全員 $mがムッツリスケベになりました！</span>|);	}],
	[59,	'天馬のたづな',		20000,		2,			sub{ $m{lib} = 'god'; $com.="$mは、天馬に乗り天界へと導かれた！";	}],
	[60,	'ｼﾙﾊﾞｰｵｰﾌﾞ',		1000,		2,			sub{ if ($m{orb} =~ /s/) { $mes="すでにささげられています"; }else{ $com.="ｼﾙﾊﾞｰｵｰﾌﾞを復活の祭壇にささげた！";	$m{orb} .= 's'; };	}], # 月の色月曜日
	[61,	'ﾚｯﾄﾞｵｰﾌﾞ',			1000,		2,			sub{ if ($m{orb} =~ /r/) { $mes="すでにささげられています"; }else{ $com.="ﾚｯﾄﾞｵｰﾌﾞを復活の祭壇にささげた！";	$m{orb} .= 'r'; }; 	}], # 火の色火曜日
	[62,	'ﾌﾞﾙｰｵｰﾌﾞ',			1000,		2,			sub{ if ($m{orb} =~ /b/) { $mes="すでにささげられています"; }else{ $com.="ﾌﾞﾙｰｵｰﾌﾞを復活の祭壇にささげた！";	$m{orb} .= 'b'; }; 	}], # 水の色水曜日
	[63,	'ｸﾞﾘｰﾝｵｰﾌﾞ',		1000,		2,			sub{ if ($m{orb} =~ /g/) { $mes="すでにささげられています"; }else{ $com.="ｸﾞﾘｰﾝｵｰﾌﾞを復活の祭壇にささげた！";	$m{orb} .= 'g'; }; 	}], # 木の色木曜日
	[64,	'ｲｴﾛｰｵｰﾌﾞ',			1000,		2,			sub{ if ($m{orb} =~ /y/) { $mes="すでにささげられています"; }else{ $com.="ｲｴﾛｰｵｰﾌﾞを復活の祭壇にささげた！";	$m{orb} .= 'y'; }; 	}], # 金の色金曜日
	[65,	'ﾊﾟｰﾌﾟﾙｵｰﾌﾞ',		1000,		2,			sub{ if ($m{orb} =~ /p/) { $mes="すでにささげられています"; }else{ $com.="ﾊﾟｰﾌﾟﾙｵｰﾌﾞを復活の祭壇にささげた！";	$m{orb} .= 'p'; }; 	}], # 土の色土曜日
	[66,	'ﾗｰの鏡',			5000,		1,			sub{ if ($m{lib} eq 'vs_monster') { $stage = 15; $round = 1; $com.="$mたちは、ﾗｰの鏡の中へと吸い込まれた！";	} else { $mes="しかし、何も起こらなかった…"; };	}],
	[67,	'ﾏﾀﾞﾑの招待状',		5000,		1,			sub{ if ($m{lib} eq 'vs_monster') { $stage = 16; $round = 1; $com.="$mたちは、$stages[$stage]に招待された！";	} else { $mes="しかし、何も起こらなかった…"; };	}],
	[68,	'宝の地図',			5000,		1,			sub{ if ($m{lib} eq 'vs_monster') { $stage = 17; $round = 1; $com.="$mたちは、$stages[$stage]にたどり着いた！";	} else { $mes="しかし、何も起こらなかった…"; };	}],
	[69,	'闇のﾗﾝﾌﾟ',			5000,		1,			sub{ if ($m{lib} eq 'vs_monster') { $stage = 18; $round = 1; $com.="$mたちは、闇のﾗﾝﾌﾟの中へと吸い込まれた！";	} else { $mes="しかし、何も起こらなかった…"; };	}],
	[70,	'闇のｵｰﾌﾞ',			5000,		1,			sub{ if ($m{lib} eq 'vs_monster') { $stage = 19; $round = 1; $com.="$mたちは、$stages[$stage]にたどり着いた！";	} else { $mes="しかし、何も起こらなかった…"; };	}],
	[71,	'天空の盾と兜',		5000,		1,			sub{ if ($m{lib} eq 'vs_monster' && $weas[$m{wea}][1] eq '天空の剣' && $arms[$m{arm}][1] eq '天空の鎧') { $stage = 20; $round = 1; $com.="$mたちは、不思議な光に包まれ空高くまいあがっていく…。"; } else { $mes="しかし、何も起こらなかった…"; };	}],

	[72,	'身代わり人形',		800,		1,			sub{ my $n = '@ﾀﾞﾐｰ@'; if (defined $ms{$n}{name}) { $com.="しかし、身代わり人形は消滅した…"; } else { &_add_party($n, 'item/001.gif', 150, 999, 400,  50, 150); };	}],
	[73,	'身代わり石像',		1000,		1,			sub{ my $n = '@ﾀﾞﾐｰ@'; if (defined $ms{$n}{name}) { $com.="しかし、身代わり石像は消滅した…"; } else { &_add_party($n, 'item/002.gif', 120, 300, 700, 900, 100); };	}],
	[74,	'身代わり騎士',		1200,		1,			sub{ my $n = '@ﾀﾞﾐｰ@'; if (defined $ms{$n}{name}) { $com.="しかし、身代わり騎士は消滅した…"; } else { &_add_party($n, 'item/003.gif', 300, 100, 999, 200, 100); };	}],
	[75,	'妖精の笛',			1500,		1,			sub{ my($y) = &_check_enemy($y, 'テン', '道具'); $ms{$y}{ten} = 1; $com.="$yは心が安らいだ。$yのテンションが元にもどりました！";		}],
	[76,	'戦いのﾄﾞﾗﾑ',		600,		1,			sub{ &_st_up(shift, 1.0, '道具', 'at');		}],
	[77,	'魔物のｴｻ',			5000,		1,			sub{ my($y) = &_check_enemy($y, 'テン', '道具'); &tenshon($y);		}],
	[78,	'銀のたてごと',		1400,		1,			sub{ &_add_enemy;	}],
	[79,	'竜のｳﾛｺ',			400,		1,			sub{ my($y) = &_st_up(shift, 0.3, '道具', 'df'); $ms{$y}{tmp} = '息軽減'; $com.=qq|<span class="tmp">$yは不思議な風に包まれた！</span>|;	}],
	[80,	'守りのﾙﾋﾞｰ',		500,		1,			sub{ my($y) = &_check_party(shift, '魔軽減', '道具'); return if !$y || $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '魔軽減'; $com.=qq|<span class="tmp">$yは魔法の光で守られた！</span>|;		}],
	[81,	'魔法の粉',			1200,		1,			sub{ my($y) = &_check_party(shift, '魔吸収', '道具'); return if !$y || $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '魔吸収'; $com.=qq|<span class="tmp">$mは不思議な光に包まれた！</span>|;	}],
	[82,	'悪魔の粉',			1600,		1,			sub{ my($y) = &_check_enemy(shift, '２倍', '道具'); $ms{$y}{tmp} = '２倍'; $com.=qq|<span class="tmp">$yは弱体化した！</span>|;		}],
	[83,	'ｷﾒﾗの翼',			1700,		1,			sub{ $com.="$mはｷﾒﾗの翼を空高く放り投げた！"; if ($m{lib} eq 'vs_monster' && $round < 9) { $round++; }else{ $com.="しかし、不思議な力にかきけされた！"; };		}],
	[84,	'魔石のｶｹﾗ',		700,		1,			sub{ my @r_skills = &{ 'skill_'.$ms{$m}{job} }; my $i = int(rand(@r_skills)); my $buf_mp = $ms{$m}{mp}; &{ $r_skills[$i][3] }; $ms{$m}{mp} = $buf_mp if $buf_mp > $ms{$m}{mp};	}],
	[85,	'悪魔のしっぽ',		3600,		1,			sub{ &_yubiwofuru;	}],
	[86,	'不思議なﾀﾝﾊﾞﾘﾝ',	1000,		1,			sub{ my($y) = &_check_party($y, 'テン', '道具'); &tenshon($y);		}],
	[87,	'時の砂',			7000,		1,			sub{ &reset_status_all; for my $y (@members) { $ms{$y}{hp}=$ms{$y}{mhp}; $ms{$y}{mp}=$ms{$y}{mmp}; }; $com.="時がさかのぼり敵味方全員の$e2j{hp}・$e2j{mp}、ステータスが回復した！";		}],

	[88,	'魔銃',				5000,		0,			sub{	}],
	[89,	'禁じられた果実',	7000,		0,			sub{	}],
	[90,	'ｽﾗｲﾑﾋﾟｱｽ',			20000,		0,			sub{	}],
	[91,	'飛竜のﾋｹﾞ',		20000,		0,			sub{	}],
	[92,	'禁断の書',			18000,		0,			sub{	}],
	[93,	'ｺｳﾓﾘの羽',			15000,		0,			sub{	}],
	[94,	'ﾏｼﾞｯｸﾏｯｼｭﾙｰﾑ',		20000,		0,			sub{	}],
	[95,	'透明ﾏﾝﾄ',			20000,		0,			sub{	}],
	[96,	'獣の血',			18000,		0,			sub{	}],
	[97,	'死者の骨',			18000,		0,			sub{	}],
	[98,	'謎の液体',			15000,		0,			sub{	}],
	[99,	'ﾋｰﾛｰｿｰﾄﾞ',			20000,		0,			sub{	}],
	[100,	'ﾋｰﾛｰｿｰﾄﾞ2',		20000,		0,			sub{	}],
	[101,	'小人のﾊﾟﾝ',		950,		1,			sub{ if ($m{lib} eq 'vs_dungeon') { &chizu(2); } else { &_mp_h(shift, 50, '道具'); };	}],
	[102,	'ﾘｼﾞｪﾈﾎﾟｰｼｮﾝ',		700,		1,			sub{ my($y) = &_check_party(shift, '回復', '道具'); return if !$y; $ms{$y}{tmp}='回復'; $com.=qq|<span class="tmp">$yは優しい光に包まれた！</span>|;	}],
	[103,	'復活の草',			2000,		1,			sub{ my($y) = &_check_party(shift, '復活', '道具'); return if !$y; $ms{$y}{tmp}='復活'; $com.=qq|<span class="tmp">$yは復活の草を食べた！</span>|;	}],
	[104,	'次元のｶｹﾗ',		5000,		1,			sub{ if ($m{lib} eq 'vs_monster') { $stage = 21; $round = 1; $com.="$mたちは、$stages[$stage]に吸い込まれた！";	} else { $mes="しかし、何も起こらなかった…"; };	}],
	[105,	'幸せのくつ',		777,		0,			sub{	}],
	[106,	'金の鶏',			7000,		0,			sub{ 	}],
	[107,	'宝物庫の鍵',		10000,		1,			sub{ if ($m{lib} eq 'vs_monster') { $round = 10; $com.="$mは宝物庫の鍵をかざした！…鍵はまばゆい光を放ちあたり一面を包み込んでいく！";	} else { $mes="しかし、何も起こらなかった…"; };	}],
	[108,	'ﾁｮｺﾎﾞの羽',		20000,		0,			sub{ 	}],
	[109,	'ｲﾝﾃﾘﾒｶﾞﾈ',			10000,		0,			sub{ 	}],

# ＠パーティーIII追加分
	[110,	'ﾒｶﾞﾝﾃの腕輪',		500,		3,			sub{ my $y = shift; return if $ms{$y}{hp} > 0; $com.=qq|<span class="die">なんと、$yがつけていたﾒｶﾞﾝﾃの腕輪が砕け散った！</span>|; @buf_ps = @partys; @partys = @enemys; @partys = @buf_ps; &_deaths('即死', '無', 60); &regist_you_data($y, 'ite', 0); @buf_es = @enemys; @enemys = @partys; @partys = @buf_es;	}],
	[111,	'幸せの帽子',		777,		3,			sub{ my $y = shift; return if $ms{$y}{hp} <= 0; $ms{$y}{mp}+=int(rand(9)+5); $ms{$y}{mp}=999 if $ms{$y}{mp} > 999;		}],
	[112,	'命の指輪',			1200,		3,			sub{ my $y = shift; return if $ms{$y}{hp} <= 0; $ms{$y}{hp}+=int(rand(9)+9); $ms{$y}{hp}=999 if $ms{$y}{hp} > 999;		}],
	[113,	'命のﾌﾞﾚｽﾚｯﾄ',		1100,		4,			sub{ my %p = @_; $p{mhp}+=100; $p{mhp}=999 if $p{mhp} > 999; return %p;		}],
	[114,	'ｿｰｻﾘｰﾘﾝｸﾞ',		2000,		4,			sub{ my %p = @_; $p{mmp}+=100; $p{mmp}=999 if $p{mmp} > 999; return %p;		}],
	[115,	'怒りのﾀﾄｩｰ',		2000,		3,			sub{ my $y = shift; return if rand(3) > 1; $ms{$y}{ten}=1.7; $ms{$y}{tmp}='２倍';	}],
	[116,	'ﾄﾞｸﾛの指輪',		666,		3,			sub{ my $y = shift; $ms{$y}{at}+=30; $ms{$y}{df}+=30; $ms{$y}{state}='動封';		}],
	[117,	'金のﾛｻﾞﾘｵ',		1100,		3,			sub{ my $y = shift; $ms{$y}{df}+=30;	}],
	[118,	'金の指輪',			800,		3,			sub{ my $y = shift; $ms{$y}{df}+=15;	}],
	[119,	'金のﾌﾞﾚｽﾚｯﾄ',		1500,		3,			sub{ my $y = shift; $ms{$y}{df}+=50;	}],
	[120,	'はやてのﾘﾝｸﾞ',		1500,		3,			sub{ my $y = shift; $ms{$y}{ag}+=30;	}],
	[121,	'ほしふる腕輪',		3000,		3,			sub{ my $y = shift; $ms{$y}{ag}+=60;	}],
	[122,	'力の指輪',			1500,		3,			sub{ my $y = shift; $ms{$y}{at}+=20;	}],
	[123,	'ごうけつの腕輪',	3000,		3,			sub{ my $y = shift; $ms{$y}{at}+=40;	}],
	[124,	'ｱﾙｺﾞﾝﾘﾝｸﾞ',		6000,		3,			sub{ my $y = shift; $ms{$y}{at}+=30; $ms{$y}{ag}+=30;		}],

	[125,	'福袋',				1000,		2,			sub{ my @lists=(1,1,1,1,1,1,7,7..10,1..26,41..56,72..87,101..103,125..128,130,130,130,130..134); my $v = $lists[ int(rand($#lists)+1) ]; $npc_com .= "なんと、福袋の中身は $ites[$v][1] だった！"; &send_item($m, 3, $v);		}],
	[126,	'幸福袋',			7000,		2,			sub{ my @lists=(128..134,128..136); my $v = $lists[ int(rand($#lists)+1) ]; $npc_com .= "なんと、幸福袋の中身は $ites[$v][1] だった！"; &send_item($m, 3, $v);		}],
	[127,	'基本錬金ﾚｼﾋﾟ',		500,		2,			sub{ &learn_recipe(qw/薬草 上薬草 特薬草 毒消し草 身代わり人形 竜のｳﾛｺ ﾓﾝｽﾀｰ銅貨 ﾓﾝｽﾀｰ銀貨 闇のﾛｻﾞﾘｵ 魔獣の皮 祈りの指輪 金の指輪 ひのきの棒 こんぼう ﾌﾞﾛﾝｽﾞﾅｲﾌ ﾀﾞｶﾞｰﾅｲﾌ ﾙｰﾝｽﾀｯﾌ ﾛﾝｸﾞｽﾋﾟｱ ｸｻﾅｷﾞの剣 銅の剣 聖銀のﾚｲﾋﾟｱ 鎖がま 鉄の斧 金の斧 おおきづち 布の服 旅人の服 皮の鎧 鎖かたびら 鉄の鎧 鋼鉄の鎧 さまよう鎧 ｿﾞﾝﾋﾞﾒｲﾙ 魔法の法衣/);	}],
	[128,	'応用錬金ﾚｼﾋﾟ',		2000,		2,			sub{ &learn_recipe(qw/世界樹の葉 魔法の聖水 幸せの種 ｽｷﾙの種 身代わり石像 銀のたてごと 魔法の粉 悪魔の粉 金の鶏 ﾓﾝｽﾀｰ金貨 金のﾌﾞﾚｽﾚｯﾄ 怒りのﾀﾄｩｰ ｿｰｻﾘｰﾘﾝｸﾞ ｿﾞﾝﾋﾞｷﾗｰ ﾊﾞﾄﾙﾌｫｰｸ ﾎｰﾘｰﾗﾝｽ ﾓｰﾆﾝｸﾞｽﾀｰ 鋼鉄の剣 ｽﾗｲﾑﾋﾟｱｽ 理力の杖 ﾊﾞｽﾀｰﾄﾞｿｰﾄﾞ 堕天使のﾚｲﾋﾟｱ ﾊﾞﾄﾙｱｯｸｽ 山賊の斧 銀の胸当て みかわしの服 ｼﾙﾊﾞｰﾒｲﾙ 賢者のﾛｰﾌﾞ 毛皮のﾏﾝﾄ 魔人の鎧/);	}],
	[129,	'神の錬金ﾚｼﾋﾟ',		7000,		2,			sub{ &learn_recipe();	}],
	[130,	'馬のﾌﾝ',			1,			1,			sub{ $com.="$mは馬のﾌﾝをにぎりしめた！………$mは後悔した…"	}],
	[131,	'魔獣の皮',			500,		0,			sub{ 	}],
	[132,	'魔除けの聖印',		800,		0,			sub{ 	}],
	[133,	'聖者の灰',			1200,		0,			sub{ 	}],
	[134,	'金塊',				10000,		0,			sub{ 	}],
	[135,	'ｽﾗｲﾑの冠',			15000,		0,			sub{ 	}],
	[136,	'ｵﾘﾊﾙｺﾝ',			20000,		0,			sub{ 	}],
	[137,	'ﾛﾄの印',			30000,		0,			sub{ 	}],
	[138,	'ﾀｸｼｰﾄﾞ',			500,		2,			sub{ $m{icon} = 'chr/027.gif'; $com.="$mはﾀｸｼｰﾄﾞのコスプレをした！"	}],
	[139,	'闇人の衣装',		600,		2,			sub{ $m{icon} = 'chr/025.gif'; $com.="$mは闇人のコスプレをした！"	}],
	[140,	'英雄の衣装',		700,		2,			sub{ $m{icon} = $m{sex} eq 'm' ? 'chr/034.gif' : 'chr/028.gif'; $com.="$mは英雄のコスプレをした！"	}],
	[141,	'ﾓｼｬｽの巻物',		1500,		2,			sub{ my $no = sprintf("%03d",int(rand(40)+1)); $m{icon} = -f "$icondir/chr/$no.gif" ? "chr/$no.gif" : "chr/098.gif"; $com.="$mはﾓｼｬｽの巻物を読んだ！"	}],
);




1; # 削除不可
