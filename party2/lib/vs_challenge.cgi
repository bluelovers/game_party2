require "./lib/_battle.cgi";
require "./lib/_npc_action.cgi";
#=================================================
# チャレンジモード Created by Merino
#=================================================
@npc_skills = (
	[0,	0,	'こうげき',		sub{ &kougeki	}],
#	[0,	0,	'ぼうぎょ',		sub{ $ms{$m}{tmp} = '防御'; $com.="$mは身を固めている";	}],
);

#=================================================
# タイトル、背景画像
#=================================================
sub get_header_data {
	$bgimg = "$bgimgdir/challenge$stage.gif";
	$this_title = "$challenges[$stage] Lv.<b>$round</b>";
}
#=================================================
# 追加アクション
#=================================================
sub add_battle_action {
	if (defined $enemys[0] && $enemys[0] =~ /宝箱.$/) {
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
		$mes .= "※敵を全て倒すまで、次のLv.に進むことはできません";
		return;
	}
	elsif ($round < 1 && $leader ne $m) {
		$mes = "一番始めの ＠すすむ をすることができるのはリーダーのみです";
		return;
	}

	&update_record() if $round > $win; # 最高記録を超えていたら記録更新処理
	&reset_status_all;

	++$round;
	$npc_com .= "$p_nameは $challenges[$stage] Lv.$round に挑戦！<br />";
	&set_monster();
	&auto_reload;
}
# ------------------
# 戦闘メンバーにNPCモンスターを追加する
sub set_monster {
	&error("$challengedir/$stage.cgiモンスターデータファイルがありません") unless -f "$challengedir/$stage.cgi";
	require "$challengedir/$stage.cgi";

	@members = @partys;
	
	if (!$m{is_get} && $round >= $tresure_round && rand(10) < 1) { # お宝(未取得で、$tresure_round以上の階で、1/10の確立)
		&add_treasure();
	}
	else {
		&add_monster(0, 1 + 0.1 * $round );
	}
}

# 記録更新
sub update_record {
	open my $fh, "+< $logdir/challenge$stage.cgi" or &error("$logdir/challenge$stage.cgiファイルが開けません");;
	eval { flock $fh, 2; };
	my $line = <$fh>;
	my($max_round) = (split /<>/, $line)[0];

	if ($round > $max_round) { # 同時で更新されている場合があるので再確認
		my @lines = ("$round<>$date<>$p_name<>$ms{$m}{color}<>\n");
		for my $y (@partys) { # 記録表示に使いたいデータをつっこむ
			my $icon = $ms{$y}{hp} <= 0 ? 'chr/099.gif' : $ms{$y}{icon};
			push @lines, "$y<>$icon<>$ms{$y}{job}<>$ms{$y}{old_job}<>$ms{$y}{hp}<>$ms{$y}{mp}<>$ms{$y}{at}<>$ms{$y}{df}<>$ms{$y}{ag}<>\n";
		}
		
		$win = $round;
		$npc_com .= qq|<span class="lv_up">$challenges[$stage]の記録を更新しました！【Lv.<b>$round</b>クリア】</span><br />|;
		seek $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
	}
	close $fh;
}


1; # 削除不可
