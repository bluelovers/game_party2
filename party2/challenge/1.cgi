# 設定
%k = (
	p_join		=> 2,			# 戦闘参加上限(人)
	need_join	=> 'hp_400_u',	# 参加条件(./lib/quest.cgi 192行目あたりを参考)
);

# 宝部屋(10階〜20階以上。上位階ほど確率アップ)
$tresure_round = int(rand(11)+10);


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
		name		=> 'ﾗｰｽｼｰﾌﾟ',
		hp			=> 200,
		at			=> 140,
		df			=> 100,
		ag			=> 140,
		get_exp		=> 40,
		get_money	=> 21,
		icon		=> 'chr/019.gif',

		job			=> 10, # 羊飼い
		sp			=> 999,
		old_sp		=> 20,
		mmp			=> 9999,
		mp			=> 40,
		ten			=> 3,
	},
);



1; # 削除不可
