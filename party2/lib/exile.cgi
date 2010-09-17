#=================================================
# 荒らし追放 Created by Merino
#=================================================
# 場所名
$this_title = '荒らし追放騎士団';

# NPC名
$npc_name   = '@追放騎士';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/exile";

# 背景画像
$bgimg   = "$bgimgdir/exile.gif";

# 誤った判断をした申請者への拘束時間(日)
$penalty_day = 25;

# 追放に必要な票数
$need_vote = 40;

# 1人が追放申請できる限度(申請中のが解決すると再度申請可能)
$max_violator = 1;

# 申請取り消し禁止時間(時)。誰かが投票を行ってからこの時間以内は取り消しできない。
$c_hour = 3;


#=================================================
# はなす言葉
#=================================================
@words = (
	"ここは荒らし追放騎士団！荒らしや不正プレイヤーを取り締まっている！",
	"荒らしや不正プレイヤーなどを追放して、楽しい環境を作ろう！",
	"荒らしを見かけたらここで追放投票をしてくれ！荒らしのいない楽しい環境はお前達がつくっていくのだ。",
	"荒らしの発言に対して反応してはいけない。相手の反応を楽しむのが荒らしなのだ。無視が一番効果的だ。",
	"荒らしの不快な言葉に不快な言葉で返してしまうのは、荒らしと一緒に荒らしているのと同じことだ。",
	"感情的になっているときは、クールになれ！冷静な時こそ正しい判断をすることができるはずだ。",
	"なんとなくムカつくなどの感情的な判断で誤った追放申\請をした場合、申\請者が逆に罰を受けることになるぞ。",
	"判決に必要な票数は$need_vote票必要だ！",
	"投票できるのは、転職回数が１回以上のプレイヤーのみだ！",
);


#=================================================
# 追加アクション
#=================================================
push @actions, 'ついほう';
push @actions, 'さんせい';
push @actions, 'はんたい';
$actions{'ついほう'} = sub{ &tuihou; }; 
$actions{'さんせい'} = sub{ &sansei; }; 
$actions{'はんたい'} = sub{ &hantai; }; 


#=================================================
# ＠ついほう
#=================================================
sub tuihou {
	my $target = shift;
	my($bad_name, $because) = split /＠りゆう&gt;/, $target;

	if ($bad_name eq '' || $because eq '') {
		$mes = "『＠ついほう>○○○＠りゆう>△△△』○○○には荒らしの名前、△△△にはなぜ追放したいのかの理由を書いてくれ";
		return;
	}

	if ($m{job_lv} < 1) {
		$mes = "未転職の方は、申\請することはできません";
		return;
	}
	elsif ($bad_name eq $m) {
		$mes = "自分自身を申\請することはできません";
		return;
	}

	my $yid = unpack 'H*', $bad_name;
	if (!-d "$userdir/$yid") {
		$mes = "$bad_nameというプレイヤーは存在しません";
		return;
	}
	
	my %sames = ();
	my @lines = ();
	open my $fh, "+< $logdir/violator.cgi" or &error("$logdir/violator.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($name, $violator, $message, $yess, $noss) = split /<>/, $line;
		if ($violator eq $bad_name) {
			$mes = "$bad_nameはすでに追放申\請されています";
			return;
		}
		elsif (++$sames{$name} > $max_violator) {
			$mes = "申\請した追放者の判決を待ってください";
			return;
		}
		
		push @lines, $line;
	}
	push @lines, "$m<>$bad_name<>$because<>$m,<><>\n";
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	$npc_com = qq|<span class="damage">$bad_nameを追放者リストに追加しておいたぞ。判決がくだるのを待て！</span>|;
	&write_news(qq|<span class="damage">$mが$bad_nameを$becauseの理由で追放申\請しました</span>|);
}

#=================================================
# ＠さんせい＠はんたい
#=================================================
sub sansei { &vote('yes', shift); }
sub hantai { &vote('no',  shift); }
sub vote {
	my($vote, $target) = @_;
	
	if ($m{job_lv} < 1) {
		$mes = "未転職の方は、投票することはできません";
		return;
	}
	
	my @lines = ();
	my $p = '';
	open my $fh, "+< $logdir/violator.cgi" or &error("$logdir/violator.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($name, $violator, $message, $yess, $noss) = split /<>/, $line;
		my $y_c = split /,/, $yess;
		my $n_c = split /,/, $noss;
		$p .= qq|<hr>申\請：$name / 追放：$violator / 理由：$message<br /><span onclick="text_set('＠さんせい>$violator ')">賛成 <b>$y_c</b> 票：$yess</span>　<span onclick="text_set('＠はんたい>$violator ')">反対 <b>$n_c</b> 票：$noss</span><br />\n|;
		next if $target eq '';

		# 追放申請取り消し
		if ($name eq $m && $vote eq 'no') {
			my $ftime = (stat "$logdir/violator.cgi")[9];
			if ($ftime + $c_hour * 3600 > $time) {
				$mes = "投票後しばらくは取り消すことはできません";
				return;
			}
			else {
				$npc_com = "$violatorの追放申\請を取り消しました";
				&write_news(qq|<span class="revive">$mが$violatorの追放申\請を取り消しました</span>|);
				next;
			}
		}
		
		if ($target eq $violator) {
			if ($yess =~ /\Q$m,\E/ || $noss =~ /\Q$m,\E/) {
				$mes = "すでに追放投票に参加しています";
				return;
			}
			elsif ($violator eq $m) {
				$mes = "申\請されている人は投票することはできません";
				return;
			}
			my $yid = unpack 'H*', $violator;
			if (!-d "$userdir/$yid") {
				$npc_com = "$violatorというプレイヤーは存在しません";
				next;
			}
			elsif ($vote eq 'yes') {
				++$y_c;
				# 追放
				if ($y_c >= $need_vote) {
					my %p = &get_you_datas($yid, 1);
					&add_black_list($p{host});
					&delete_guild_member($p{guild}, $p{name}) if $p{guild};
					&delete_directory("$userdir/$yid");
					&minus_entry_count;
					$npc_com = qq|<span class="die">【議決】賛成 $y_c 票 / 反対 $n_c 票。よって $violatorは有罪！追放とする！以上！</span>|;
					&write_news(qq|<span class="die">【議決】賛成 $y_c 票 / 反対 $n_c 票。よって $violatorは有罪として追放されました</span>|);
				}
				else {
					push @lines, "$name<>$violator<>$message<>$m,$yess<>$noss<>\n";
					$npc_com = "$violatorの追放：賛成 $y_c 票 / 反対 $n_c 票";
				}
			}
			elsif ($vote eq 'no') {
				++$n_c;
				# 申請者にペナルティ
				if ($n_c >= $need_vote) {
					$pid = unpack 'H*', $name;
					&regist_you_data($name, 'sleep', $penalty_day * 24 * 3600) if -d "$userdir/$pid";
					$npc_com  = qq|<span class="revive">【議決】賛成 $y_c 票 / 反対 $n_c票。よって $violatorは無罪！</span>|;
					&write_news(qq|<span class="revive">【議決】賛成 $y_c 票 / 反対 $n_c 票。よって $violatorは無罪となりました</span>|);
					
					if ($name && $name !~ /^@/) {
						$npc_com .= qq|<span class="die">申\請者の$nameは $penalty_day日間の眠りの刑とする！</span>|;
						&write_news(qq|<span class="die">申\請者の$nameは $penalty_day日間の眠りの刑となりました</span>|);
					}
					$npc_com .= "以上！</b>";
				}
				else {
					push @lines, "$name<>$violator<>$message<>$yess<>$m,$noss<>\n";
					$npc_com = "$violatorの追放の賛成 $y_c 票 / 反対 $n_c 票";
				}
			}
			else {
				push @lines, $line;
			}
		}
		else {
			push @lines, $line;
		}
	}
	if ($npc_com) {
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
	}
	else {
		$mes = qq|追放者申\請リスト<br />$p|;
	}
	close $fh;
}




1; # 削除不可
