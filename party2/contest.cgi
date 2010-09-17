#!/usr/local/bin/perl
require 'config.cgi';
require '_side_menu.cgi';
#================================================
# コンテスト Created by Merino
# past 過去, prepare エントリー受付(次のコンテスト), entry 現コンテスト
#================================================
# コンテスト実施周期(日)
$contest_cycle_day = 10;

# 最低決行人数(人)
$min_entry_contest = 5;

# コンテストの賞金
@prizes = (
# 小さなﾒﾀﾞﾙ　賞金　ギルドポイント
	[10,	15000,	700],
	[6,		 7000,	300],
	[3,		 3000,	100],
);

#================================================
&decode;
&header;
&header_contest;
if    ($in{mode} eq 'past')   { &past }
elsif ($in{mode} eq 'legend') { &legend }
else { &now_contest }
&side_menu($contents);
&footer;
exit;
#================================================
# コンテスト用header
#================================================
sub header_contest {
	$contents .= '<p>';
	$contents .= $in{mode} eq 'legend' ? qq|<a href="contest.cgi">現在のコンテスト</a> / <a href="contest.cgi?mode=past">前回のコンテスト</a> / 殿堂入り|
			   : $in{mode} eq 'past'   ? qq|<a href="contest.cgi">現在のコンテスト</a> / 前回のコンテスト / <a href="contest.cgi?mode=legend">殿堂入り</a>|
			   :                         qq|現在のコンテスト / <a href="contest.cgi?mode=past">前回のコンテスト</a> / <a href="contest.cgi?mode=legend">殿堂入り</a>|
			   ;
	$contents .= '</p>';
}

#================================================
# 殿堂入り
#================================================
sub legend {
	$contents .= qq|<h2>殿堂入り</h2><hr />|;
	open my $fh, "< $logdir/contest_legend.cgi" or &error("$logdir/contest_legend.cgiファイルが読み込めません");
	while (my $line = <$fh>) {
		my($round, $stitle, $name, $guild, $vote, $ldate, $photo) = split /<>/, $line;
		$name .= "＠$guild" if $guild;
		$contents .= qq|<h3>第$round回優秀作品『$stitle』 <b>$vote</b>票 作：$name <span class="text_small">($ldate)</span></h3>$photo<br />|;
	}
	close $fh;
}

#================================================
# 前回のコンテスト結果
#================================================
sub past {
	if (-s "$logdir/contest_past.cgi") {
		my $count = 1;
		open my $fh, "< $logdir/contest_past.cgi" or &error("$logdir/contest_past.cgiファイルが読み込めません");
		my $head_line = <$fh>;
		my($etime, $round) = split /<>/, $head_line;
		$contents .= qq|<h2>第$round回結果発表\</h2> ※１位の作品に投票された人には小さなメダルが送られます<hr />|;
		while (my $line = <$fh>) {
			my($stitle, $name, $guild, $vote, $comment, $vote_names, $photo) = split /<>/, $line;
			$name .= "＠$guild" if $guild;
			$comment  .= qq|<hr />| if $comment;
			$contents .= qq|<h3>$count位 <b>$vote</b>票 題名『$stitle』 作:$name</h3>$photo$comment<br />\n|;
			++$count;
		}
		close $fh;
	}
	else {
		$contents .= qq|<p>前回のコンテストは開催されていません</p>|;
	}
}

#================================================
# 現在のコンテスト
#================================================
sub now_contest {
	my $count = 0;
	my $sub_mes = '';
	open my $fh, "< $logdir/contest_entry.cgi" or &error("$logdir/contest_entry.cgiファイルが読み込めません");
	my $head_line = <$fh>;
	my($etime, $round) = split /<>/, $head_line;
	while (my $line = <$fh>) {
		my($stitle, $name, $guild, $vote, $comment, $vote_names, $photo) = split /<>/, $line;
		$sub_mes .= qq|<h3>題名『$stitle』</h3>$photo<br />\n|;
		++$count;
	}
	close $fh;
	my($min,$hour,$day,$month) = (localtime($etime))[1..4];
	++$month;
	
	# 過去コンテスト削除→現コンテストを過去コンテスト→次コンテストを現コンテストにする処理
	if ($time > $etime) {
		$contents .= qq|<h2>第$round回フォトコンテスト</h2>|;
		$contents .= qq|<p>…集計処理中…</p>|;

		if ($count > 0) {
			&_send_goods_to_creaters if -s "$logdir/contest_past.cgi";
			&_result_contest;
		}
		&_start_contest;
	}
	elsif ($min_entry_contest > $count) {
		$contents .= qq|<h2>第$round回フォトコンテスト</h2>|;
		$contents .= qq|【投票終了日・次回コンテスト $month月$day日$hour時$min分】<hr />|;
		$contents .= qq|投稿作品が集まっていないため開催延期中です<br />|;
	}
	else {
		$contents .= qq|<h2>第$round回フォトコンテスト</h2>|;
		$contents .= qq|【投票終了日・次回コンテスト $month月$day日$hour時$min分】<hr />|;
		$contents .= $sub_mes;
	}
}


# ------------------
# 過去のコンテスト作品を作者に返品しファイル・フォルダ削除
sub _send_goods_to_creaters {
	my $count = 0;
	open my $fh, "+< $logdir/contest_past.cgi" or &error("$logdir/contest_past.cgiファイルが開けません");
	eval { flock $fh, 2; };
	my $head_line = <$fh>;
	my($etime, $round) = split /<>/, $head_line;
	while (my $line = <$fh>) {
		my($stitle, $name, $guild, $vote, $comment, $vote_names, $content) = split /<>/, $line;
		++$count;
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	close $fh;
}
# ------------------
# 結果を集計して過去コンテストにリネーム
sub _result_contest {
	my @lines = ();
	open my $fh, "+< $logdir/contest_entry.cgi" or &error("$logdir/contest_entry.cgiファイルが開けません");
	eval { flock $fh, 2; };
	my $head_line = <$fh>;
	while (my $line = <$fh>) {
		push @lines, $line;
	}
	
	# 多い順にsort
	@lines = map { $_->[0] } sort { $b->[4] <=> $a->[4] } map { [$_, split/<>/] } @lines;
	
	unshift @lines, $head_line;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	rename "$logdir/contest_entry.cgi", "$logdir/contest_past.cgi" or &error("Cannot rename $logdir/contest_entry.cgi to $logdir/contest_past.cgi");
	
	# 作品をコピーして殿堂入り
	&__copy_goods_to_legend($head_line, $lines[1]) if @lines > $min_entry_contest;
	
	&__send_prize(@lines);
}

# 上位に賞品送る
sub __send_prize {
	my @lines = @_;

	my $head_line = shift @lines;
	my($etime, $round) = split /<>/, $head_line;
	
	my $count = 1;
	for my $line (@lines) {
		my($stitle, $name, $guild, $vote, $comment, $vote_names, $content) = split /<>/, $line;
		
		if ($count eq '1') {
			for my $vname (split /,/, $vote_names) {
				next unless $vname;
				&send_item($vname, 3, 23, 'フォトコンテスト');
			}
		}
		
		my $send_id = unpack 'H*', $name;
		if (-f "$userdir/$send_id/depot.cgi") {
			open my $fh, ">> $userdir/$send_id/depot.cgi";
			for my $i (1..$prizes[$count-1][0]-1) {
				print $fh "3<>23<>\n";
			}
			close $fh;
			
			&send_item($vname, 3, 23, 'フォトコンテスト')
		}
		&send_money($name, $prizes[$count-1][1], "第$round回フォトコンテスト$count位の賞金");
		&write_memory("★第$round回フォトコンテスト$count位入賞★", $name);
		&regist_guild_data('point', $prizes[$count-1][2], $guild) if $guild;
		&write_news(qq|<span class="comp">★第$round回フォトコンテスト$count位 $name★</span>|);
		last if ++$count > @prizes;
	}
}

sub __copy_goods_to_legend {
	my($head_line, $line) = @_;
	my($etime, $round) = split /<>/, $head_line;
	my($stitle, $name, $guild, $vote, $comment, $vote_names, $content) = split /<>/, $line;
	
	my @lines = ();
	open my $fh, "+< $logdir/contest_legend.cgi" or &error("$logdir/contest_legend.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		push @lines, $line;
		last if @lines > $max_log - 1;
	}
	unshift @lines, "$round<>$stitle<>$name<>$guild<>$vote<>$date<>$content<>\n";
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}

# ------------------
# 次コンテストを現コンテストにリネーム
sub _start_contest {
	my $end_time = $time + 24 * 60 * 60 * $contest_cycle_day;

	my @lines = ();
	open my $fh, "+< $logdir/contest_prepare.cgi" or &error("$logdir/contest_prepare.cgiファイルが開けません");
	eval { flock $fh, 2; };
	my $head_line = <$fh>;
	my($etime, $round) = split /<>/, $head_line;
	push @lines, "$end_time<>$round<>\n";
	while (my $line = <$fh>) {
		push @lines, $line;
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;

	# エントリー数が最低エントリー数を超えた場合は開催
	if ( @lines > $min_entry_contest ) {
		rename "$logdir/contest_prepare.cgi", "$logdir/contest_entry.cgi" or &error("Cannot rename $logdir/contest_prepare.cgi to $logdir/contest_entry.cgi");
		
		# 投票/未投票識別ファイルを初期化
		open my $fh3, "> $logdir/contest_vote_name.cgi" or &error("$logdir/contest_vote_name.cgiファイルが作れません");
		print $fh3 ",";
		close $fh3;
		
		# 次コンテストを初期化
		++$round;
	 	open my $fh2, "> $logdir/contest_prepare.cgi" or &error("$logdir/contest_prepare.cgiファイルが開けません");
		print $fh2 "$end_time<>$round<>\n";
		close $fh2;
		chmod $chmod, "$logdir/contest_prepare.cgi";
	}
	else {
		# 時間を延長
	 	open my $fh2, "> $logdir/contest_entry.cgi" or &error("$logdir/contest_entry.cgiファイルが開けません");
		print $fh2 "$end_time<>$round<>\n";
		close $fh2;
		chmod $chmod, "$logdir/contest_entry.cgi";
	}
}


