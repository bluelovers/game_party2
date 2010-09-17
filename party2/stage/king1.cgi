# 設定
%k = (
	p_name		=> '@全てを無に還す者@',# クエスト名
	p_join		=> 6,					# 戦闘参加上限(人)
	p_leader	=> '破壊神',			# クエストリーダー名
	speed		=> 12,					# 進行スピード(秒)
	need_join	=> 'hp_400_o',			# 参加条件(./lib/quest.cgi 192行目あたりを参考)
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
		name		=> 'ﾚｯﾄﾞｽﾄｰﾝ',
		hp			=> 50,
		at			=> 400,
		df			=> 9000,
		ag			=> 3000,
		get_exp		=> 1000,
		get_money	=> 2000,
		icon		=> 'mon/190.gif',
		
		job			=> 26, # 忍者
		sp			=> 999,
		old_job		=> 6, # 魔法使い
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '魔無効',
	},
	{
		name		=> 'ﾌﾞﾙｰｽﾄｰﾝ',
		hp			=> 50,
		at			=> 500,
		df			=> 9000,
		ag			=> 3000,
		get_exp		=> 1000,
		get_money	=> 2000,
		icon		=> 'mon/191.gif',
		
		job			=> 33, # 賢者
		sp			=> 130,
		old_job		=> 31, # 青魔道士
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '魔無効',
	},
	{
		name		=> 'ｲｴﾛｰｽﾄｰﾝ',
		hp			=> 50,
		at			=> 500,
		df			=> 9000,
		ag			=> 3000,
		get_exp		=> 1000,
		get_money	=> 2000,
		icon		=> 'mon/192.gif',
		
		job			=> 36, # ものまね士
		sp			=> 999,
		old_job		=> 37, # 結界士
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '魔無効',
	},
	{
		name		=> '破壊神',
		hp			=> 150000,
		at			=> 600,
		df			=> 300,
		ag			=> 300,
		get_exp		=> 10000,
		get_money	=> 5000,
		icon		=> 'mon/850.gif',
		
		hit			=> 2000, # 長期戦用命中率
		job			=> 97, # 超攻撃系
		sp			=> 999,
		mmp			=> 9999999,
		mp			=> 999999,
		tmp			=> '攻軽減',
	},
	{
		name		=> 'ｸﾞﾘｰﾝｽﾄｰﾝ',
		hp			=> 50,
		at			=> 500,
		df			=> 9000,
		ag			=> 3000,
		get_exp		=> 1000,
		get_money	=> 2000,
		icon		=> 'mon/193.gif',
		
		job			=> 90, # どくこうげき、ポイズン、もうどくのきり
		sp			=> 999,
		old_job		=> 91, # まひこうげき、しびれうち、やきつくいき
		old_sp		=> 999,
		mmp			=> 999999,
		mp			=> 99999,
		tmp			=> '魔無効',
	},
	{
		name		=> 'ﾊﾟｰﾌﾟﾙｽﾄｰﾝ',
		hp			=> 50,
		at			=> 500,
		df			=> 9000,
		ag			=> 3000,
		get_exp		=> 1000,
		get_money	=> 2000,
		icon		=> 'mon/194.gif',
		
		job			=> 35, # 魔王
		sp			=> 999,
		old_job		=> 92, # ラリホー、ねむりこうげき、あまいいき
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '魔無効',
	},
	{
		name		=> 'ｼﾙﾊﾞｰｽﾄｰﾝ',
		hp			=> 50,
		at			=> 500,
		df			=> 9000,
		ag			=> 3000,
		get_exp		=> 500,
		get_money	=> 2000,
		icon		=> 'mon/196.gif',
		
		job			=> 19, # 闇魔道士
		sp			=> 999,
		old_job		=> 20, # 悪魔
		old_sp		=> 999,
		mmp			=> 999999,
		mp			=> 99999,
		tmp			=> '魔無効',
	},
);



1;
