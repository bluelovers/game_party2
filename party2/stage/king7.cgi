# 設定
%k = (
	p_name		=> '@全てを爆発させる者@',	# クエスト名
	p_join		=> 6,						# 戦闘参加上限(人)
	p_leader	=> 'ﾎﾞﾏｰ',					# クエストリーダー名
	speed		=> 12,						# 進行スピード(秒)
	need_join	=> 'hp_200_o',				# 参加条件(./lib/quest.cgi 192行目あたりを参考)
);


# 封印戦戦利品(道具No)
@treasures = (
[], # 武器No
[3], # 防具No
[42,58,58,57..59,57..59], # 道具No
);

# ボス
@bosses= (
	{
		name		=> 'ﾎﾞﾏｰ',
		hp			=> 60000,
		at			=> 450,
		df			=> 250,
		ag			=> 150,
		get_exp		=> 5000,
		get_money	=> 1,
		icon		=> 'mon/652.gif',
		
		job			=> 8, # 遊び人
		sp			=> 999,
		old_job		=> 95, # 召喚
		old_sp		=> 999,
		mmp			=> 999999,
		mp			=> 99999,
		state		=> '大爆発',
		tmp			=> 'するぞ',
	},
);


# 召喚されるモンスター
@monsters = (
	{
		name		=> '爆弾岩',
		hp			=> 150,
		at			=> 300,
		df			=> 300,
		ag			=> 50,
		get_exp		=> 90,
		get_money	=> 5,
		icon		=> 'mon/080.gif',

		job			=> 94, # 自爆メガンテ、ねる
		sp			=> 20,
		old_sp		=> 30, # てんしょん,ぼうぎょ
		mp			=> 42,
	},
	{
		name		=> '爆弾王',
		hp			=> 300,
		at			=> 400,
		df			=> 300,
		ag			=> 100,
		get_exp		=> 180,
		get_money	=> 20,
		icon		=> 'mon/579.gif',

		job			=> 94, # 自爆メガンテ、ねる
		sp			=> 20,
		old_sp		=> 30, # てんしょん,ぼうぎょ
		mp			=> 42,
	},
	{
		name		=> 'ﾎﾞﾑ',
		hp			=> 200,
		at			=> 350,
		df			=> 60,
		ag			=> 400,
		get_exp		=> 100,
		get_money	=> 50,
		icon		=> 'mon/071.gif',

		job			=> 31, # 青魔道士じばく
		sp			=> 20,
		old_sp		=> 30, # てんしょん,ぼうぎょ
		mp			=> 42,
	},
	{
		name		=> 'ﾋﾞｯｸﾎﾞﾑ',
		hp			=> 400,
		at			=> 450,
		df			=> 120,
		ag			=> 280,
		get_exp		=> 200,
		get_money	=> 100,
		icon		=> 'mon/577.gif',

		job			=> 31, # 青魔道士じばく
		sp			=> 20,
		old_sp		=> 30, # てんしょん,ぼうぎょ
		mp			=> 42,
	},
	{
		name		=> 'ﾁﾋﾞﾎﾞﾑ',
		hp			=> 50,
		at			=> 300,
		df			=> 900,
		ag			=> 900,
		get_exp		=> 100,
		get_money	=> 1,
		icon		=> 'mon/208.gif',

		job			=> 94, # 自爆メガンテ、ねる
		sp			=> 20,
		old_sp		=> 30, # てんしょん,ぼうぎょ
		mp			=> 42,
		tmp			=> '魔無効',
	},
	{
		name		=> 'ｷﾗｰﾎﾞﾑ',
		hp			=> 100,
		at			=> 400,
		df			=> 700,
		ag			=> 900,
		get_exp		=> 150,
		get_money	=> 10,
		icon		=> 'mon/209.gif',

		job			=> 94, # 自爆メガンテ、ねる
		sp			=> 20,
		old_sp		=> 30, # てんしょん,ぼうぎょ
		mp			=> 42,
	},
);




1;
