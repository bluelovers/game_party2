require "./lib/_battle.cgi";
require "./lib/_npc_action.cgi";
#=================================================
# 封印戦 Created by Merino
#=================================================

@npc_skills = (
	[0,	0,	'こうげき',		sub{ &kougeki	}],
	[0,	0,	'デジョン',		sub{ &dejon		}],
);

#=================================================
# タイトル、背景画像
#=================================================
sub get_header_data {
	$bgimg = "$bgimgdir/stage19.gif";
	$this_title = "$p_name";
}
#=================================================
# 追加アクション
#=================================================
sub add_battle_action {
	if ($round eq '2') {
		$is_npc_action = 0;
		push @actions, 'しらべる';
		$actions{'しらべる'} = [0,	sub{ &shiraberu }];
	}
	elsif (@enemys <= 0) {
		push @actions, 'ふういん';
		$actions{'ふういん'} = [0,	sub{ &fuuin }];
	}
}

#=================================================
# ＠ふういん
#=================================================
sub fuuin {
	return if @enemys;
	$is_npc_action = 0;
	if (@enemys > 0) {
		$mes .= "※全ての敵を倒さないと封印することはできません";
		return;
	}
	elsif ($round >= 2) {
		$mes .= "すでに封印済みです。＠にげるで解散してください<br />";
		return;
	}
	
	++$round;

	&error("$stagedir/$stage.cgiモンスターデータファイルがありません") unless -f "$stagedir/$stage.cgi";
	require "$stagedir/$stage.cgi";
	
	$npc_com .= "$p_nameを再び封印することに成功しました！イベント広場で祝賀会が開催されます！<br />";
	my $hero_name = join "、", @partys;
	&write_news(qq|<span class="tenshon">勇者$hero_nameが$p_nameを封印する</span>|);

	for my $name (@partys) {
		next if $name =~ /^@/;
		my %p = &get_you_datas($name);
		&regist_you_data($name, 'hero_c', $p{hero_c}+1);
	}

	&add_treasure();

	# イベント広場で祝賀会の人たちを追加
	require "./lib/_win_vs_king.cgi";
}

#=============================
# ＠デジョン やられた人を強制退場
#=============================
sub dejon {
	my @new_members;
	for my $name (@members) {
		if ($ms{$name}{hp} <= 0) {
			my $yid = unpack 'H*', $name;
			if (-f "$userdir/$yid/user.cgi") {
				my %p = &get_you_datas($yid, 1);
				&regist_you_data($name, 'lib', '');
				&regist_you_data($name, 'tired', $p{tired}+30);
			}
			$ms{$name}{color} = $npc_color;
			$com.="$nameが異空間へと吸い込まれた！";
		}
		else {
			push @new_members, $name;
		}
	}
	@members = @new_members;
}


1; # 削除不可
