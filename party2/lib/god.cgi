#=================================================
# 天空 Created by Merino
#=================================================
# 場所名
$this_title = "天界";

# NPC名
$npc_name   = '@神';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/god";

# 背景画像
$bgimg   = "$bgimgdir/god.gif";

# 願い事
@prizes = (
# 	['ねがいごと名',				'補足説明',			sub{ 処理($mesに何か文字を入れるとキャンセル)  }],	
	['強くなりたい',				'全ｽﾃｰﾀｽ 40 ｱｯﾌﾟ',	sub{ for my $k (qw/mhp mmp at df ag/) { $m{$k}+=40; };	}],
	['スキルを覚えたい',			'Sp 50 ｱｯﾌﾟ',		sub{ $m{sp}     += 50;		}],
	['お金がほしい',				'10 万G',			sub{ $m{money}  += 100000;		}],
	['カジノコインがほしい',		'5 万枚',			sub{ $m{coin}   += 50000;		}],
	['小さなメダルがほしい',		'20 枚',			sub{ $m{medal}  += 20;		}],
	['福引券がほしい',				'1000 枚',			sub{ $m{coupon} += 1000;	}],
	['ギルドランクをあげたい',		'1000 ﾎﾟｲﾝﾄ',		sub{ return unless $m{guild}; &regist_guild_data('point', 1000, $m{guild});	}],
	['ギルドをゴージャスにしたい',	'ギルドが…',		sub{ return unless $m{guild}; my $gid = unpack 'H*', $m{guild}; return unless -f "$guilddir/$gid/log_member.cgi"; open my $fh, ">> $guilddir/$gid/log_member.cgi" or &error("$guilddir/$gid/log_member.cgiファイルが開けません"); print $fh "$time<>1<>金ﾒﾀﾞﾙ<>0<>etc/win_medal3.gif<>$npc_color<>\n"; close $fh; &regist_guild_data('bgimg', 'god.gif', $m{guild});		}],
	['元気いっぱいになりたい',		'疲労度 -150 %',	sub{ $m{tired} -= 150;		}],
	['新しい冒険場所に行きたい',	'全オーブ',			sub{ $m{orb}    = 'byrpgs';		}],
	['天竜人になりたい',			'転職',				sub{ if ($m{job} eq '70' || $m{old_job} eq '70') { $mes="ふむ。すでに$mは天竜人だぞ…"; return; }; &job_change(70);		}],
	['新世界の神になりたい',		'自分の家が…',		sub{ $m{icon} = 'chr/052.gif'; &copy("$bgimgdir/god.gif", "$userdir/$id/bgimg.gif");		}],
	['オルテガを生き返らして',		'自分の家に…',		sub{ open my $fh, ">> $userdir/$id/home_member.cgi" or &error("$userdir/$id/home_member.cgiファイルが開けません"); print $fh "$time<>1<>ｵﾙﾃｶﾞ<>0<>chr/029.gif<>$npc_color<>\n"; close $fh;		}],
	['猫を飼いたい',				'自分の家に…',		sub{ open my $fh, ">> $userdir/$id/home_member.cgi" or &error("$userdir/$id/home_member.cgiファイルが開けません"); if (rand(2) < 1) { print $fh "$time<>1<>白猫<>0<>chr/030.gif<>$npc_color<>\n"; }else{ print $fh "$time<>1<>黒猫<>0<>chr/031.gif<>$npc_color<>\n"; }; close $fh;		}],
	['エッチな本がほしい',			'アイテム',			sub{ &send_item($m, 3, 58);		}],
	['錬金ﾚｼﾋﾟがほしい',			'アイテム',			sub{ &send_item( $m, 3, int(rand(2)+128) );	}],
	['素敵な恋人がほしい',			'恋人が…',			sub{ $mes = 'それは無理な願いだ…。アドバイスとしては積極的にアピールするのだ…';		}],

	# シークレット
	['メイドを雇いたい',			'お世話係',			sub{ open my $fh, ">> $userdir/$id/home_member.cgi" or &error("$userdir/$id/home_member.cgiファイルが開けません"); print $fh "$time<>1<>ﾒｲﾄﾞ<>0<>chr/026.gif<>$npc_color<>\n"; close $fh;		}],
);

# 猫を飼いたい
# ﾗｰﾐｧを飼いたい
# 変な

#=================================================
# ＠しらべる>NPC
#=================================================
sub shiraberu_npc {
	$mes = qq|<span onclick="text_set('＠ねがう>メイドを雇いたい')">$npc_name「本当の願いは自分の力で叶えるのだ…」</span>|;
}

#=================================================
# はなす言葉
#=================================================
@words = (
	"$mよ。よくぞここまできた。$mの願いを一つだけ叶えてやろう",
);

#=================================================
# 追加アクション
#=================================================
push @actions, 'ねがう';
$actions{ 'ねがう' } = sub{ &negau };

#=================================================
# ステータス表示
#=================================================
sub header_html {
	print qq|<div class="mes">【$this_title】</div>|;
}

#=================================================
# ＠ねがう
#=================================================
sub negau {
	my $target = shift;

	my $p = qq|<table class="table1">|;
	for my $i (0 .. $#prizes-1) {
		if ($prizes[$i][0] eq $target) {
			&{ $prizes[$i][2] };
			return if $mes;
			
			$npc_com = "ふむ。$mの願いは「$prizes[$i][0]」だな。<br />$mの願いを叶えたぞ…。機会があればまたあえるだろう…。さらばだ…";
			$m{lib} = 'home';
			&write_memory("$mの願い『$prizes[$i][0]』を叶えてもらう");
			return;
		}
		$p .= qq|<tr onclick="text_set('＠ねがう>$prizes[$i][0] ')"><td>$prizes[$i][0]($prizes[$i][1])</td></tr>|;
	}
	$p  .= qq|</table>|;
	$mes = qq|願いを一つだけ叶えてやろう…<br />$p|;
	$act_time = 0;
}

# ------------------
# 転職処理 ./lib/job_change.cgiからコピー
sub job_change {
	my $job = shift;
	
	&add_all_job_master;
	my $mastered_point = &add_job_master($job);
	
	# 違う職業に転職した場合の処理(同じ職業に転職した場合は、レベルとステータスを下げるだけ)
	unless ($m{job} eq $job) {
		my $buf_sp  = $m{old_sp};
		$m{old_sp}  = $m{sp};
		$m{sp}      = $job eq $m{old_job} ? $buf_sp : $mastered_point; # 前職業に転職する場合は前職業のSP
		$m{old_job} = $m{job};
		$m{job}     = $job;
		$m{icon}    = "job/$m{job}_$m{sex}.gif";
	}
	
	# ステータスダウン
	for my $k (qw/mhp mmp at df ag/) {
		$m{$k} = int($m{$k} * 0.5); 
		$m{$k} = 10 if $m{$k} < 10;
	}
	
	$m{hp} = $m{mhp};
	$m{mp} = $m{mmp};
	$m{lv}  = 1;
	$m{exp} = 0;
	$m{job_lv}++;
}

# 習得ジョブ
sub add_job_master {
	my $job = shift;

	require "./lib/_skill.cgi";
	my @skills = &{ 'skill_'.$m{job} };

	my $mastered_job_sp = 0;
	my $mastered_count = 0;
	my $is_find = 0;
	my @lines = ();
	open my $fh, "+< $userdir/$id/job_master.cgi" or &error("$userdir/$id/job_master.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($job_no, $job_sex, $job_point, $is_master) = split /<>/, $line;

		if ($m{job} eq $job_no) {
			$is_find = 1;
			if (!$is_master && $m{sp} >= $skills[-1][0]) {
				$is_master = 1;
				$com .= qq|<span class="comp">$mは <b>$jobs[$m{job}][1]</b> をマスターしました！</span>|;
				&write_memory("<b>★ $jobs[$m{job}][1] Job Master! ★</b>");
			}
			push @lines, "$m{job}<>$m{sex}<>$m{sp}<>$is_master<>\n";
		}
		elsif ($job eq $job_no && $is_master) {
			$mastered_job_sp = $job_point;
			push @lines, $line;
		}
		else {
			push @lines, $line;
		}
		$mastered_count++ if $is_master;
	}
	unless ($is_find) {
		my $is_master = 0;
		
		if ($m{sp} >= $skills[-1][0]) {
			$is_master = 1;
			$com .= qq|<span class="comp">$mは <b>$jobs[$m{job}][1]</b> をマスターしました！</span>|;
			&write_memory("<b>★ $jobs[$m{job}][1] Job Master! ★</b>");
		}
		push @lines, "$m{job}<>$m{sex}<>$m{sp}<>$is_master<>\n";
	}
	@lines = map { $_->[0] } sort { $a->[1] <=> $b->[1] } map { [$_, split /<>/] } @lines;
	
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	# 全ジョブコンプリート
	if ($mastered_count eq $#jobs-1 && !-f "$userdir/$id/comp_job_flag.cgi") { 
		open my $fh2, "> $userdir/$id/comp_job_flag.cgi" or &error("$userdir/$id/comp_job_flag.cgiファイルが開けません");
		close $fh2;
		
		&write_legend('comp_job');
		&write_memory(qq|<span class="comp">All Job Complete!!</span>|);
		&write_news(qq|<span class="comp">$mが全ての職業をマスターしました！</span>|);
		$com .= qq|<div class="comp">$mは <b>全ジョブ</b> をコンプリートしました！</div>|;
	}
	
	return $mastered_job_sp;
}

# 全体の転職の傾向
sub add_all_job_master {
	my $is_find = 0;
	
	my $add_point = int($m{lv} * 0.5);
	
	my @lines = ();
	open my $fh, "+< $logdir/job_ranking.cgi" or &error("$logdir/job_ranking.cgiファイルが開けません");
	eval { flock $fh, 2; };
	my $totale_point = <$fh>;
	$totale_point =~ tr/\x0D\x0A//d;
	$totale_point += $add_point;
	while (my $line = <$fh>) {
		my($job_no, $men_point, $female_point, $job_point) = split /<>/, $line;
		if ($m{job} eq $job_no) {
			$is_find = 1;
			
			if ($m{sex} eq 'm') {
				$men_point += $add_point;
			}
			else {
				$female_point += $add_point;
			}
			$job_point += $add_point;
		}
		push @lines, "$job_no<>$men_point<>$female_point<>$job_point<>\n";
	}
	unless ($is_find) {
		my $job_sex = $m{sex} eq 'm' ? "$add_point<>0" : "0<>$add_point";
		push @lines, "$m{job}<>$job_sex<>$add_point<>\n";
	}

	@lines = map { $_->[0] } sort { $b->[4] <=> $a->[4] } map { [$_, split /<>/] } @lines;
	unshift @lines, "$totale_point\n";
	
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}

1; # 削除不可
