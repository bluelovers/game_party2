# 設定
%k = (
	p_name		=> '@全てを憎む者@',# クエスト名
	p_join		=> 6,				# 戦闘参加上限(人)
	p_leader	=> '暗黒竜',		# クエストリーダー名
	speed		=> 12,				# 進行スピード(秒)
	need_join	=> 'hp_400_o',		# 参加条件(./lib/quest.cgi 192行目あたりを参考)
);

# 封印戦戦利品(道具No)
@treasures = (
[], # 武器No
[], # 防具No
[59,59,59,59,71,104], # 道具No
);

# ボス
@bosses= (
	{
		name		=> '暗黒竜',
		hp			=> 140000,
		at			=> 300,
		df			=> 200,
		ag			=> 0,
		get_exp		=> 8000,
		get_money	=> 5000,
		icon		=> 'mon/710.gif',
		
		hit			=> 900, # 長期戦用命中率
		job			=> 0, # こうげき、てんしょん、ぼうぎょ
		sp			=> 999,
		old_job		=> 101, # 召喚&孵化
		old_sp		=> 999,
		mmp			=> 999999,
		mp			=> 99999,
		tmp			=> '受流し',
	},
);


# 召喚されるモンスター
@monsters = (
	{
		name		=> '竜王',
		hp			=> 600,
		at			=> 550,
		df			=> 400,
		ag			=> 100,
		get_exp		=> 250,
		get_money	=> 100,
		icon		=> 'mon/560.gif',
		job			=> 41, # ﾄﾞﾗｺﾞﾝ
		sp			=> 999,
		old_job		=> 25, # ﾓﾝｸ、
		old_sp		=> 999,
		mp			=> 299,
		tmp			=> '息反撃',
	},
	{
		name		=> '火竜',
		hp			=> 600,
		at			=> 550,
		df			=> 400,
		ag			=> 100,
		get_exp		=> 250,
		get_money	=> 100,
		icon		=> 'mon/561.gif',
		job			=> 35, # 魔王
		sp			=> 999,
		old_job		=> 91, # 麻痺系
		old_sp		=> 999,
		mp			=> 299,
		tmp			=> '息反撃',
	},
	{
		name		=> '水竜',
		hp			=> 600,
		at			=> 550,
		df			=> 400,
		ag			=> 100,
		get_exp		=> 250,
		get_money	=> 100,
		icon		=> 'mon/562.gif',
		job			=> 41, # ﾄﾞﾗｺﾞﾝ
		sp			=> 999,
		old_job		=> 27, # 風水士
		old_sp		=> 999,
		mp			=> 299,
		tmp			=> '息反撃',
	},
	{
		name		=> 'ﾍﾞﾋｰﾓｽ',
		hp			=> 480,
		at			=> 500,
		df			=> 240,
		ag			=> 400,
		get_exp		=> 240,
		get_money	=> 90,
		icon		=> 'mon/553.gif',
		job			=> 23, # 竜騎士
		sp			=> 999,
		old_job		=> 25, # モンク
		old_sp		=> 999,
		mp			=> 209,
		tmp			=> '大防御',
	},
	{
		name		=> 'ｷﾝｸﾞﾍﾞﾋｰﾓｽ',
		hp			=> 540,
		at			=> 500,
		df			=> 240,
		ag			=> 400,
		get_exp		=> 240,
		get_money	=> 90,
		icon		=> 'mon/554.gif',
		job			=> 21, # 狂戦士
		sp			=> 999,
		old_job		=> 25, # モンク
		old_sp		=> 999,
		mp			=> 209,
		tmp			=> '攻反撃',
	},
	{
		name		=> 'ｲﾌﾘｰﾄ',
		hp			=> 540,
		at			=> 500,
		df			=> 240,
		ag			=> 400,
		get_exp		=> 240,
		get_money	=> 90,
		icon		=> 'mon/555.gif',
		job			=> 70, # 天竜人めいそうドラゴンパワーギガデイン
		sp			=> 150,
		old_job		=> 52, # 魔人
		old_sp		=> 999,
		mp			=> 209,
		tmp			=> '攻無効',
	},
	{
		name		=> 'ﾄﾞﾗｺﾞﾝﾏｯﾄ',
		hp			=> 480,
		at			=> 600,
		df			=> 360,
		ag			=> 150,
		get_exp		=> 200,
		get_money	=> 100,
		icon		=> 'mon/556.gif',
		old_sp		=> 20,
		job			=> 41, # ﾄﾞﾗｺﾞﾝ
		sp			=> 999,
		mp			=> 99,
		tmp			=> '受流し',
	},
	{
		name		=> 'ﾄﾞﾗｺﾞﾝｿﾞﾝﾋﾞ',
		hp			=> 560,
		at			=> 520,
		df			=> 300,
		ag			=> 120,
		get_exp		=> 255,
		get_money	=> 100,
		icon		=> 'mon/557.gif',
		job			=> 58, # ﾀﾞｰｸｴﾙﾌ
		sp			=> 999,
		old_job		=> 52, # 魔人
		old_sp		=> 999,
		mp			=> 192,
		tmp			=> '復活',
	},
);


1;
