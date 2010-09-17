# 設定
%k = (
	p_name		=> '@悪の城@',	# クエスト名
	p_join		=> 6,				# 戦闘参加上限(人)
	p_leader	=> '悪の城',	# クエストリーダー名
	speed		=> 12,				# 進行スピード(秒)
	need_join	=> 'hp_200_u',		# 参加条件(./lib/quest.cgi 192行目あたりを参考)
);


# 封印戦戦利品(道具No)
@treasures = (
[], # 武器No
[], # 防具No
[1..43,23,23,59,59,72..89,101..103,107], # 道具No
);

# ボス
@bosses= (
	{
		name		=> '悪の城',
		hp			=> 30000,
		at			=> 150,
		df			=> 150,
		ag			=> 100,
		get_exp		=> 1800,
		get_money	=> 2000,
		icon		=> 'mon/603.gif',
		
		hit			=> 800, # 長期戦用命中率400%
		job			=> 95, # 召喚
		sp			=> 999,
		old_job		=> 95, # 召喚
		old_sp		=> 999,
		mmp			=> 999999,
		mp			=> 99999,
		tmp			=> '攻軽減',
	},
);


# 召喚されるモンスター
@monsters = (
	{
		name		=> 'ﾐﾗｰﾅｲﾄ',
		hp			=> 150,
		at			=> 150,
		df			=> 100,
		ag			=> 150,
		get_exp		=> 50,
		get_money	=> 50,
		icon		=> 'mon/520.gif',

		job			=> 36, # ものまね士
		sp			=> 999,
		mp			=> 94,
	},
	{
		name		=> '地獄の鎧',
		hp			=> 166,
		at			=> 116,
		df			=> 166,
		df			=> 66,
		ag			=> 66,
		get_exp		=> 66,
		get_money	=> 66,
		icon		=> 'mon/240.gif',

		old_sp		=> 30,
		job			=> 3, # 騎士かばう、まもりをかためる、すてみ、だいぼうぎょ、スクルト
		sp			=> 40,
		mp			=> 66,
	},
	{
		name		=> '地獄の騎士',
		hp			=> 166,
		at			=> 166,
		df			=> 66,
		ag			=> 66,
		get_exp		=> 66,
		get_money	=> 66,
		icon		=> 'mon/223.gif',
		
		job			=> 24, # 魔剣士かえんぎり、メタルぎり、バイキルト、いなずまぎり、ギガスラッシュ
		sp			=> 50,
		old_job		=> 22, # 暗黒騎士あんこく、めいやく
		old_sp		=> 20,
		mp			=> 66,
	},
	{
		name		=> 'ﾌﾞﾙｰﾅｲﾄ',
		hp			=> 120,
		at			=> 150,
		df			=> 60,
		ag			=> 50,
		get_exp		=> 50,
		get_money	=> 30,
		icon		=> 'mon/519.gif',
		
		old_sp		=> 20,
		job			=> 23, # 竜騎士ジャンプ、ドラゴンパワー、りゅうけん
		sp			=> 50,
		mp			=> 85,
	},
	{
		name		=> 'ﾌﾞﾗｯｸﾅｲﾄ',
		hp			=> 196,
		at			=> 196,
		df			=> 96,
		ag			=> 96,
		get_exp		=> 96,
		get_money	=> 96,
		icon		=> 'mon/524.gif',

		job			=> 21, # ﾊﾞｰｻｰｶｰ
		sp			=> 999,
		old_job		=> 22, # 暗黒騎士あんこく、めいやく
		old_sp		=> 20,
		mp			=> 96,
	},
);




1;
