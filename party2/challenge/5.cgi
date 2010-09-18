# 設定
%k = (
	p_join		=> 4,			# 戦闘参加上限(人)
	need_join	=> '0',			# 参加条件(./lib/quest.cgi 192行目あたりを参考)
);

# 宝部屋(20階～30階以上。上位階ほど確率アップ)
$tresure_round = int(rand(11)+20);


# 宝の中身
@treasures = (
[], # 武器No
[], # 防具No
[6,15,57,72..74,87,101..103], # 道具No
);


# 出現率(@monstersの配列番号が多ければ多いほど出現。均等な出現率の場合は、から『()』)
@appears = ();


# モンスター
if ($stage > 20) { # 20階以降は じばく に変更
	@monsters = (
		{
			name		=> '爆弾岩',
			hp			=> 400,
			at			=> 250,
			df			=> 150,
			ag			=> 150,
			get_exp		=> 30,
			get_money	=> 100,
			icon		=> 'mon/080.gif',
	
			job			=> 94, # 自爆メガンテ、ねる
			sp			=> 20,
			old_job		=> 31, # 青魔道士じばく
			old_sp		=> 11,
			mmp			=> 9999,
			mp			=> 42,
		},
	);
}
else {
	@monsters = (
		{
			name		=> '爆弾岩',
			hp			=> 400,
			at			=> 250,
			df			=> 150,
			ag			=> 150,
			get_exp		=> 30,
			get_money	=> 100,
			icon		=> 'mon/080.gif',
	
			job			=> 94, # 自爆メガンテ、ねる
			sp			=> 20,
			old_job		=> 94, # 自爆メガンテ、ねる
			old_sp		=> 20,
			mmp			=> 9999,
			mp			=> 42,
		},
	);
}



1; # 削除不可
