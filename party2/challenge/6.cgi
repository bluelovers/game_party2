# 設定
%k = (
	p_join		=> 3,			# 戦闘参加上限(人)
	need_join	=> '0',			# 参加条件(./lib/quest.cgi 192行目あたりを参考)
);

# 宝部屋(20階～30階以上。上位階ほど確率アップ)
$tresure_round = int(rand(11)+20);


# 宝の中身
@treasures = (
[], # 武器No
[], # 防具No
[4..6,10..13,23,57,72..74,85..87,101..103], # 道具No
);


# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = ();

# モンスター
@monsters = (
	{
		name		=> 'レッドストーン',
		hp			=> 5,
		at			=> 200,
		df			=> 2000,
		ag			=> 500,
		get_exp		=> 50,
		get_money	=> 100,
		icon		=> 'mon/190.gif',
		
		job			=> 26, # 忍者
		sp			=> 999,
		old_job		=> 6, # 魔法使い
		old_sp		=> 999,
		mmp			=> 99999,
		mp			=> 99,
		tmp			=> '魔無効',
	},
	{
		name		=> 'ブルーストーン',
		hp			=> 5,
		at			=> 200,
		df			=> 2000,
		ag			=> 500,
		get_exp		=> 50,
		get_money	=> 100,
		icon		=> 'mon/191.gif',
		
		job			=> 33, # 賢者
		sp			=> 130,
		old_job		=> 31, # 青魔道士
		old_sp		=> 999,
		mmp			=> 99999,
		mp			=> 99,
		tmp			=> '魔無効',
	},
	{
		name		=> 'イエローストーン',
		hp			=> 5,
		at			=> 200,
		df			=> 2000,
		ag			=> 500,
		get_exp		=> 50,
		get_money	=> 100,
		icon		=> 'mon/192.gif',
		
		job			=> 36, # ものまね士
		sp			=> 999,
		old_job		=> 37, # 結界士
		old_sp		=> 999,
		mmp			=> 99999,
		mp			=> 99,
		tmp			=> '魔無効',
	},
	{
		name		=> 'グリーンストーン',
		hp			=> 5,
		at			=> 200,
		df			=> 2000,
		ag			=> 500,
		get_exp		=> 50,
		get_money	=> 100,
		icon		=> 'mon/193.gif',
		
		job			=> 90, # どくこうげき、ポイズン、もうどくのきり
		sp			=> 999,
		old_job		=> 91, # まひこうげき、しびれうち、やきつくいき
		old_sp		=> 999,
		mmp			=> 99999,
		mp			=> 99,
		tmp			=> '魔無効',
	},
	{
		name		=> 'パープルストーン',
		hp			=> 5,
		at			=> 200,
		df			=> 2000,
		ag			=> 500,
		get_exp		=> 50,
		get_money	=> 100,
		icon		=> 'mon/194.gif',
		
		job			=> 35, # 魔王
		sp			=> 999,
		old_job		=> 92, # ラリホー、ねむりこうげき、あまいいき
		old_sp		=> 999,
		mmp			=> 99999,
		mp			=> 99,
		tmp			=> '魔無効',
	},
	{
		name		=> 'シルバーストーン',
		hp			=> 5,
		at			=> 200,
		df			=> 2000,
		ag			=> 500,
		get_exp		=> 50,
		get_money	=> 100,
		icon		=> 'mon/196.gif',
		
		job			=> 19, # 闇魔道士
		sp			=> 999,
		old_job		=> 20, # 悪魔
		old_sp		=> 999,
		mmp			=> 99999,
		mp			=> 99,
		tmp			=> '魔無効',
	},
	{
		name		=> 'ブラックストーン',
		hp			=> 5,
		at			=> 200,
		df			=> 2000,
		ag			=> 500,
		get_exp		=> 50,
		get_money	=> 100,
		icon		=> 'mon/195.gif',
		
		job			=> 58, # ダークエルフ
		sp			=> 999,
		old_job		=> 53, # 蟲師
		old_sp		=> 999,
		mmp			=> 99999,
		mp			=> 99,
		tmp			=> '魔無効',
	},
	{
		name		=> 'メタルスライム',
		hp			=> 6,
		at			=> 200,
		df			=> 1000,
		ag			=> 500,
		get_exp		=> 200,
		get_money	=> 10,
		icon		=> 'mon/004.gif',

		job			=> 40, # ハグレメタル
		sp			=> 999,
		old_job		=> 40, # ハグレメタル
		old_sp		=> 999,
		mmp			=> 99999,
		mp			=> 180,
		tmp			=> '魔無効',
	},
	{
		name		=> 'ハグレメタル',
		hp			=> 10,
		at			=> 210,
		df			=> 2000,
		ag			=> 600,
		get_exp		=> 500,
		get_money	=> 20,
		icon		=> 'mon/022.gif',

		job			=> 40, # ハグレメタル
		sp			=> 999,
		old_job		=> 40, # ハグレメタル
		old_sp		=> 999,
		mmp			=> 99999,
		mp			=> 180,
		tmp			=> '魔無効',
	},
);



1; # 削除不可
