# 設定
%k = (
	p_name		=> '@罪と罰@',			# クエスト名
	p_join		=> 4,					# 戦闘参加上限(人)
	p_leader	=> $leader,				# クエストリーダー名
	speed		=> 12,					# 進行スピード(秒)
	need_join	=> 'hp_200_o',			# 参加条件(./lib/quest.cgi 192行目あたりを参考)
);


# 封印戦戦利品(道具No)
@treasures = (
[], # 武器No
[], # 防具No
[59..65,107,107], # 道具No
);

# bosses
@bosses = ();
for my $name (@partys) {
	push @bosses, {
		name		=> $name,
		hp			=> $ms{$name}{mhp} * 50,
		mp			=> $ms{$name}{mmp} * 50,
		at			=> $ms{$name}{at} * 2,
		df			=> $ms{$name}{df} * 2,
		ag			=> $ms{$name}{ag} * 2,
		get_exp		=> $ms{$name}{get_exp} * 30,
		get_money	=> $ms{$name}{get_money} * 30,
		icon		=> $ms{$name}{icon},

		job			=> $ms{$name}{job},
		sp			=> $ms{$name}{sp},
		old_job		=> $ms{$name}{old_job},
		old_sp		=> $ms{$name}{old_sp},
		tmp			=> '大防御',
	}
}




1;
