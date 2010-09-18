# 宝の中身
@treasures = (
[35..40], # 武器No
[35..40], # 防具No
[59,59,59,59,59], # 道具No
);

# ボス
@bosses= (
	{
		name		=> '魔王',
		hp			=> 14000,
		at			=> 650,
		df			=> 350,
		ag			=> 200,
		get_exp		=> 2000,
		get_money	=> 1500,
		icon		=> 'mon/700.gif',
		
		hit			=> 250, # 長期戦用命中率200%
		job			=> 35, # 魔王
		sp			=> 999,
		old_job		=> 22, # 暗黒騎士
		old_sp		=> 999,
		mmp			=> 10000,
		mp			=> 4000,
		tmp			=> '攻反撃',
	},
	{
		name		=> 'カタストロフィー',
		hp			=> 15000,
		at			=> 750,
		df			=> 400,
		ag			=> 400,
		get_exp		=> 5000,
		get_money	=> 3000,
		icon		=> 'mon/801.gif',
		
		hit			=> 500, # 長期戦用命中率500%
		job			=> 97, # 超攻撃型
		sp			=> 999,
		old_job		=> 47, # ソルジャー
		old_sp		=> 999,
		mmp			=> 30000,
		mp			=> 8000,
		ten			=> 8,
	},
	{
		name		=> '死神',
		hp			=> 14000,
		at			=> 600,
		df			=> 250,
		ag			=> 999,
		get_exp		=> 2000,
		get_money	=> 1500,
		icon		=> 'mon/702.gif',
		
		hit			=> 250, # 長期戦用命中率200%
		job			=> 19, # 闇魔道士
		sp			=> 999,
		old_job		=> 46, # ギャンブラー
		old_sp		=> 999,
		mmp			=> 14000,
		mp			=> 5000,
		tmp			=> '魔反撃',
	},
);

# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = ();


# モンスター
@monsters = (
	{
		name		=> 'ビックスライム',
		hp			=> 500,
		at			=> 500,
		df			=> 100,
		ag			=> 500,
		get_exp		=> 120,
		get_money	=> 50,
		icon		=> 'mon/006.gif',
		old_sp		=> 20,
		tmp			=> '回復',
	},
	{
		name		=> '人面樹',
		hp			=> 700,
		at			=> 550,
		df			=> 200,
		ag			=> 250,
		get_exp		=> 170,
		get_money	=> 140,
		icon		=> 'mon/503.gif',
		old_sp		=> 20,
		job			=> 7, # 商人
		sp			=> 999,
		mp			=> 263,
		tmp			=> '復活',
	},
	{
		name		=> '亡霊剣士',
		hp			=> 860,
		at			=> 650,
		df			=> 200,
		ag			=> 150,
		get_exp		=> 180,
		get_money	=> 80,
		icon		=> 'mon/500.gif',
		old_sp		=> 20,
		job			=> 2, # 剣士
		sp			=> 999,
		mp			=> 343,
		tmp			=> '攻反撃',
	},
	{
		name		=> 'キラーシェル',
		hp			=> 600,
		at			=> 700,
		df			=> 600,
		ag			=> 300,
		get_exp		=> 150,
		get_money	=> 300,
		icon		=> 'mon/215.gif',
		old_sp		=> 20,
		job			=> 1, # 戦士
		sp			=> 999,
		mp			=> 452,
		tmp			=> '魔反撃',
	},
	{
		name		=> 'デビルシェル',
		hp			=> 1000,
		at			=> 500,
		df			=> 700,
		ag			=> 200,
		get_exp		=> 160,
		get_money	=> 500,
		icon		=> 'mon/506.gif',
		job			=> 5, # 僧侶
		old_sp		=> 30,
		sp			=> 999,
		mp			=> 600,
		tmp			=> '魔反撃',
	},
	{
		name		=> 'ゴーレム',
		hp			=> 1200,
		at			=> 500,
		df			=> 700,
		ag			=> 150,
		get_exp		=> 250,
		get_money	=> 150,
		icon		=> 'mon/546.gif',
		old_sp		=> 30,
		job			=> 27, # 風水士
		sp			=> 999,
		mp			=> 777,
		tmp			=> '攻軽減',
	},
	{
		name		=> '闇の魔術士',
		hp			=> 800,
		at			=> 450,
		df			=> 200,
		ag			=> 200,
		get_exp		=> 180,
		get_money	=> 260,
		icon		=> 'mon/510.gif',
		job			=> 40, # ハグレメタル
		sp			=> 999,
		mp			=> 300,
		tmp			=> '魔吸収',
	},
	{
		name		=> 'ギガンテス',
		hp			=> 909,
		at			=> 909,
		df			=> 100,
		ag			=> 100,
		get_exp		=> 200,
		get_money	=> 5,
		icon		=> 'mon/563.gif',
		old_sp		=> 20,
		job			=> 21, # 狂戦士
		sp			=> 999,
		mp			=> 909,
		ten			=> 8,
	},
	{
		name		=> 'ひくいどり',
		hp			=> 1100,
		at			=> 530,
		df			=> 270,
		ag			=> 380,
		get_exp		=> 180,
		get_money	=> 180,
		icon		=> 'mon/530.gif',
		job			=> 26, # 忍者
		sp			=> 999,
		old_job		=> 27, # 風水師
		old_sp		=> 999,
		mp			=> 997,
		tmp			=> '息軽減',
	},
	{
		name		=> 'ベヒーモス',
		hp			=> 909,
		at			=> 777,
		df			=> 255,
		ag			=> 555,
		get_exp		=> 211,
		get_money	=> 99,
		icon		=> 'mon/553.gif',
		job			=> 23, # 竜騎士
		sp			=> 999,
		old_job		=> 25, # モンク
		old_sp		=> 999,
		mp			=> 909,
		tmp			=> '大防御',
	},
	{
		name		=> 'キングスライム',
		hp			=> 1200,
		at			=> 500,
		df			=> 300,
		ag			=> 500,
		get_exp		=> 200,
		get_money	=> 250,
		icon		=> 'mon/516.gif',
		old_sp		=> 20,
		job			=> 21, # 狂戦士
		sp			=> 999,
		mp			=> 999,
		tmp			=> '攻無効',
	},
	{
		name		=> '死霊の騎士',
		hp			=> 1200,
		at			=> 666,
		df			=> 280,
		ag			=> 280,
		get_exp		=> 240,
		get_money	=> 170,
		icon		=> 'mon/566.gif',
		job			=> 24, # 魔剣士
		sp			=> 999,
		old_job		=> 2, # 剣士
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '受流し',
	},
	{
		name		=> '竜王',
		hp			=> 1500,
		at			=> 750,
		df			=> 440,
		ag			=> 200,
		get_exp		=> 250,
		get_money	=> 200,
		icon		=> 'mon/560.gif',
		job			=> 41, # ドラゴン
		sp			=> 999,
		old_job		=> 25, # モンク、
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '息反撃',
	},
);



1;
