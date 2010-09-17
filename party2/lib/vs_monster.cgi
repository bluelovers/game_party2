require "./lib/_battle.cgi";
require "./lib/_npc_action.cgi";
#=================================================
# 冒険(VS モンスター) Created by Merino
#=================================================

# ボス戦の階数(+1 が宝部屋となる)
$boss_round = 10;


@npc_skills = (
	[0,	0,	'こうげき',		sub{ &kougeki	}],
#	[0,	0,	'ぼうぎょ',		sub{ $ms{$m}{tmp} = '防御'; $com.="$mは身を固めている";	}],
);

#=================================================
# タイトル、背景画像
#=================================================
sub get_header_data {
	$bgimg = "$bgimgdir/stage$stage.gif";
	$this_title = "$stages[$stage] <b>$round</b>階";
}
#=================================================
# 追加アクション
#=================================================
sub add_battle_action {
	if ($round eq $boss_round+1) {
		$is_npc_action = 0;
		push @actions, 'しらべる';
		$actions{'しらべる'} = [0,	sub{ &shiraberu }];
	}

	return if @enemys;
	push @actions, 'すすむ';
	$actions{'すすむ'} = [0,	sub{ &susumu }];
}

#=================================================
# ＠すすむ
#=================================================
sub susumu {
	$is_npc_action = 0;
	if (@enemys > 0) {
		$mes .= "※敵を全て倒すまで、次の階に進むことはできません";
		return;
	}
	elsif ($round < 1 && $leader ne $m) {
		$mes = "一番始めの ＠すすむ をすることができるのはリーダーのみです";
		return;
	}
	elsif ($round >= $boss_round+1) {
		$mes .= "※クエストは終了しました。＠にげるで解散してください";
		return;
	}
	
	&reset_status_all;

	++$round;
	$npc_com .= "$p_nameは $stages[$stage] の奥へと進みました…<br />";
	&set_monster();
	&auto_reload;
}
# ------------------
# 戦闘メンバーにNPCモンスターを追加する
sub set_monster {
	&error("$stagedir/$stage.cgiモンスターデータファイルがありません") unless -f "$stagedir/$stage.cgi";
	require "$stagedir/$stage.cgi";

	@members = @partys;
	
	if ($round eq $boss_round+1) { # お宝(デフォルト11階)
		my $count = $stage eq '17' || $stage eq '20' || $stage eq '21' ? ($#partys+1) * 3 : $#partys;
		++$count if $m{job} eq '7'; # 商人の場合+1
		&add_treasure($count);
		&make_vs_king if $stage eq '19';
	}
	elsif ($round eq $boss_round) { # ボス戦(デフォルト10階)
		&add_boss();
	}
	else {
		&add_monster();
	}
}
# ------------------
# 封印戦作成
sub make_vs_king {
	opendir my $dh, $stagedir or &error("$stagedirディレクトリが開けません");
	while (my $file_name = readdir $dh) {
		next if $file_name =~ /^\./;
		next if $file_name !~ /^king/;
		my($k_stage) = ($file_name =~ /^(.+)\.cgi$/);
		
		require "$stagedir/$file_name";
		my $quest_id = unpack 'H*', $k{p_name};
		next if -d "$questdir/$quest_id"; # 同じクエスト名があった場合は作らない(作れない)

		$k{p_join}++; # ボスが1人分占有しているため
		my $boss_name = '@'.$k{p_leader};

		# 新規パーティー作成
		mkdir "$questdir/$quest_id" or &error("$questdir/$quest_idディレクトリが作成できません");
		open my $fh, "> $questdir/$quest_id/member.cgi" or &error("$questdir/$quest_id/member.cgiファイルが作成できません");
		print $fh "$k{speed}<>$k_stage<>1<>$boss_name<>$k{p_name}<><>$k{p_join}<>0<>0<>1<>$k{need_join}<>6<><>0<>0<><>\n";
		
		my @lines = ();
		for my $no (0 .. $#bosses) {
			my %p = ();
			
			# 初期データセット(読み込んだデータにすでに値がある場合はそっちを優先)
			$bosses[$no]{tmp}   ||= '';
			$bosses[$no]{state} ||= '';
			$bosses[$no]{hit}   ||= 95;
			$bosses[$no]{ten}   ||= 1;
			$bosses[$no]{name}  = '@'.$bosses[$no]{name};
			$bosses[$no]{color} = $npc_color;
			for my $k (qw/hp mp at df ag/) {
				$bosses[$no]{$k}       = $bosses[$no]{$k};
				$bosses[$no]{'m'.$k} ||= $bosses[$no]{$k};
			}
			
			my $line = '';
			for my $k (@battle_datas) {
				$line .= defined $bosses[$no]{$k} ? "$bosses[$no]{$k}<>" : "0<>";
			}
			push @lines, "$line\n";
		}

		print $fh @lines;
		close $fh;
		chmod $chmod, "$questdir/$quest_id/member.cgi";
		
		open my $fh2, "> $questdir/$quest_id/log.cgi" or &error("$questdir/$quest_id/log.cgiファイルが作成できません");
		close $fh2;
		chmod $chmod, "$questdir/$quest_id/log.cgi";
	}
	closedir $dh;
	
	for my $name (@partys) {
		next if $name =~ /^@/;
		my %p = &get_you_datas($name);
		&regist_you_data($name, 'mao_c', $p{mao_c}+1);
	}
	
	my $hero_name = join "、", @partys;
	&write_news(qq|<span class="die">$p_name($hero_name) によって封印されし者達の封印が解かれました！</span>|);
	$npc_com .= "<br />$leaderたちは、ただならぬ雰囲気を感じた…。なんと！世界から光が消え去り、世界は真っ黒な闇におおわれてしまった！";
}



1; # 削除不可
