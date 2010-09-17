# 設定
%k = (
	p_join		=> 1,			# 戦闘参加上限(人)
	need_join	=> '0',			# 参加条件(./lib/quest.cgi 192行目あたりを参考)
);

# 宝部屋(30階～50階以上。上位階ほど確率アップ)
$tresure_round = int(rand(21)+30);


# 宝の中身
@treasures = (
[], # 武器No
[], # 防具No
[5..6,10..13,23,57,72..74,85..87,101..103], # 道具No
);


# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = ();

# モンスター
@monsters = (
	{
		name		=> '人面樹',
		hp			=> 400,
		at			=> 350,
		df			=> 140,
		ag			=> 200,
		get_exp		=> 120,
		get_money	=> 100,
		icon		=> 'mon/503.gif',
		old_sp		=> 20,
		job			=> 7, # 商人
		sp			=> 999,
		mp			=> 123,
		tmp			=> '復活',
	},
	{
		name		=> '亡霊剣士',
		hp			=> 460,
		at			=> 400,
		df			=> 200,
		ag			=> 160,
		get_exp		=> 90,
		get_money	=> 40,
		icon		=> 'mon/500.gif',
		old_sp		=> 20,
		job			=> 2, # 剣士
		sp			=> 999,
		mp			=> 93,
		tmp			=> '攻反撃',
	},
	{
		name		=> 'ﾃﾞﾋﾞﾙｼｪﾙ',
		hp			=> 300,
		at			=> 300,
		df			=> 450,
		ag			=> 100,
		get_exp		=> 80,
		get_money	=> 200,
		icon		=> 'mon/506.gif',
		job			=> 5, # 僧侶
		old_sp		=> 30,
		sp			=> 999,
		mp			=> 240,
		tmp			=> '魔反撃',
	},
	{
		name		=> 'ｺﾞｰﾚﾑ',
		hp			=> 500,
		at			=> 350,
		df			=> 350,
		ag			=> 100,
		get_exp		=> 150,
		get_money	=> 100,
		icon		=> 'mon/546.gif',
		old_sp		=> 30,
		job			=> 27, # 風水士
		sp			=> 999,
		mp			=> 150,
		tmp			=> '攻軽減',
	},
	{
		name		=> '闇の魔術士',
		hp			=> 350,
		at			=> 250,
		df			=> 120,
		ag			=> 250,
		get_exp		=> 110,
		get_money	=> 180,
		icon		=> 'mon/510.gif',
		job			=> 40, # ﾊｸﾞﾚﾒﾀﾙ
		sp			=> 999,
		mp			=> 150,
		tmp			=> '魔吸収',
	},
	{
		name		=> 'ｷﾞｶﾞﾝﾃｽ',
		hp			=> 700,
		at			=> 500,
		df			=> 100,
		ag			=> 100,
		get_exp		=> 150,
		get_money	=> 5,
		icon		=> 'mon/563.gif',
		old_sp		=> 20,
		job			=> 21, # 狂戦士
		sp			=> 999,
		mp			=> 80,
		ten			=> 8,
	},
	{
		name		=> 'ひくいどり',
		hp			=> 480,
		at			=> 320,
		df			=> 160,
		ag			=> 280,
		get_exp		=> 100,
		get_money	=> 100,
		icon		=> 'mon/530.gif',
		job			=> 26, # 忍者
		sp			=> 999,
		old_job		=> 27, # 風水師
		old_sp		=> 999,
		mp			=> 297,
		tmp			=> '息軽減',
	},
	{
		name		=> 'ﾍﾞﾋｰﾓｽ',
		hp			=> 555,
		at			=> 333,
		df			=> 155,
		ag			=> 222,
		get_exp		=> 133,
		get_money	=> 33,
		icon		=> 'mon/553.gif',
		job			=> 23, # 竜騎士
		sp			=> 999,
		old_job		=> 25, # モンク
		old_sp		=> 999,
		mp			=> 120,
		tmp			=> '大防御',
	},
	{
		name		=> 'ｷﾝｸﾞｽﾗｲﾑ',
		hp			=> 500,
		at			=> 250,
		df			=> 100,
		ag			=> 250,
		get_exp		=> 150,
		get_money	=> 20,
		icon		=> 'mon/516.gif',
		old_sp		=> 20,
		job			=> 21, # 狂戦士
		sp			=> 999,
		mp			=> 300,
		tmp			=> '回復',
	},
	{
		name		=> '死霊の騎士',
		hp			=> 610,
		at			=> 333,
		df			=> 180,
		ag			=> 180,
		get_exp		=> 190,
		get_money	=> 120,
		icon		=> 'mon/566.gif',
		job			=> 24, # 魔剣士
		sp			=> 999,
		old_job		=> 2, # 剣士
		old_sp		=> 999,
		mp			=> 220,
		tmp			=> '受流し',
	},
	{
		name		=> '竜王',
		hp			=> 650,
		at			=> 300,
		df			=> 200,
		ag			=> 100,
		get_exp		=> 200,
		get_money	=> 50,
		icon		=> 'mon/560.gif',
		job			=> 41, # ﾄﾞﾗｺﾞﾝ
		sp			=> 999,
		old_job		=> 25, # ﾓﾝｸ、
		old_sp		=> 999,
		mp			=> 200,
		ten			=> 3,
	},
	{
		name		=> '片翼の天使',
		hp			=> 700,
		at			=> 300,
		df			=> 150,
		ag			=> 400,
		get_exp		=> 300,
		get_money	=> 100,
		icon		=> 'mon/569.gif',
		
		job			=> 98, # 超魔法型
		sp			=> 999,
		old_job		=> 48, # 堕天使
		old_sp		=> 999,
		mp			=> 999,
		ten			=> 3,
	},
	{
		name		=> 'ﾃﾞｨｱﾎﾞﾛｽ',
		hp			=> 750,
		at			=> 400,
		df			=> 200,
		ag			=> 200,
		get_exp		=> 300,
		get_money	=> 100,
		icon		=> 'mon/650.gif',
		
		job			=> 97, # 超攻撃型
		sp			=> 999,
		mp			=> 999,
		ten			=> 3,
	},
	{
		name		=> 'ﾎﾞﾏｰ',
		hp			=> 600,
		at			=> 200,
		df			=> 250,
		ag			=> 250,
		get_exp		=> 300,
		get_money	=> 0,
		icon		=> 'mon/652.gif',
		
		job			=> 94, # メガンテ,寝る
		sp			=> 20,
		old_job		=> 8, # 遊び人
		old_sp		=> 999,
		mp			=> 999,
		state		=> '大爆発',
		tmp			=> 'するぞ',
		ten			=> 3,
	},
);



1; # 削除不可
