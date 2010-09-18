#=================================================
# 預かり所 Created by Merino
#=================================================
# 場所名
$this_title = 'フォトコン会場';

# NPC名
$npc_name   = '@ワコール';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/photo";

# 背景画像
$bgimg   = "$bgimgdir/photo.gif";

# 連続エントリー(0:不可能[現コンテストにエントリーしている場合は、次回のコンテストに参加できない],1:可能)
$is_renzoku_entry_contest = 0;


#=================================================
# ＠はなすの会話
#=================================================
@words = (
	"フォトコンテストの会場、略してフォトコン会場へようこそ。私が主催者のワコールざます",
	"ここでは、$mが撮ったスクリーンショットを消したり、コンテストに応募したりできるざます",
	"コンテスト上位入賞者には、ゴールドと賞品が授与されるざます",
	"コンテスト１位の作品に投票した参加者にも小さなメダルが配られるざます",
	"フォトコンで重要なのは、何が写っているかはもちろん。タイトルやコメントなども重要なポイントざます",
	"自分で撮ったスクリーンショットを見たり消すことができるざます",
	"ただ撮るだけではなく、コスプレしたり色々と工夫することが大事ざます",
	"スクリーンショットは最大$max_screen_shot枚まで所持することができるざます。それ以上は、＠けす必要があるざます",
);

#=================================================
# 追加アクション
#=================================================
push @actions, 'みる';
push @actions, 'けす';
push @actions, 'とうひょう';
push @actions, 'えんとりー';
$actions{'みる'}       = sub{ &miru }; 
$actions{'けす'}       = sub{ &kesu }; 
$actions{'とうひょう'} = sub{ &touhyou }; 
$actions{'えんとりー'} = sub{ &entori  }; 


#=================================================
# ＠みる
#=================================================
sub miru {
	$mes = qq|<form action="screen_shot.cgi"><input type="hidden" name="path" value="$userdir/$id" /><input type="hidden" name="id" value="$id" /><input type="hidden" name="pass" value="$pass" /><input type="submit" value="$mのスクリーンショット" /></form>|;
}

#=================================================
# ＠けす
#=================================================
sub kesu {
	my $target = shift;
	my $count = 0;
	my @lines = ();
	my $p = '';
	open my $fh, "+< $userdir/$id/screen_shot.cgi" or &error("$userdir/$id/screen_shot.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while ($line = <$fh>) {
		++$count;
		if ($target eq "$count枚目") {
			$mes = "$count枚目のスクリーンショットを削除しましたわよ";
		}
		else {
			push @lines, $line;
			$p .= qq|<span onclick="text_set('＠けす>$count枚目 ')">$count枚目<br>$line</span>|;
		}
	}
	if ($mes) {
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
		close $fh;
		return;
	}
	close $fh;

	$mes = qq|どのスクリーンショットを消しますか？<br><div class="view" style="font-weight: normal; color: #FFF;">$p</div>|;
}

#=================================================
# ＠えんとりー
#=================================================
sub entori {
	my $target = shift;
	my($photo, $ptitle) = split /＠だいめい&gt;/, $target;
	
	if (!$is_renzoku_entry_contest && &is_entry_contest) {
		$mes = "連続でコンテストにエントリーすることはできません<br />次回のコンテストまでお待ちください";
		return;
	}
	
	my $entry_photo = '';
	my $count = 0;
	open my $fh2, "< $userdir/$id/screen_shot.cgi" or &error("$userdir/$id/screen_shot.cgiファイルが開けません");
	while ($line2 = <$fh2>) {
		$line2 =~ tr/\x0D\x0A//d;
		++$count;
		if ($photo eq "$count枚目") {
			$entry_photo = $line2;
			last;
		}
		$p .= qq|<span onclick="text_set('＠えんとりー>$count枚目＠だいめい>')">$count枚目<br>$line2</span>|;
	}
	close $fh2;
	
	unless ($entry_photo) {
		$mes = qq|どの作品をエントリーしますか？<br><div class="view" style="font-weight: normal; color: #FFF;">$p</div>|;
		return;
	}

	$mes = "題名に不正な空白が含まれています"					if $ptitle =~ /　|\s/;
	$mes = "題名に不正な文字( ,;\"\'&<>\@ )が含まれています" 	if $ptitle =~ /[,;\"\'&<>\@]/;
	$mes = "題名に不正な文字( ＠ )が含まれています" 			if $ptitle =~ /＠/;
	$mes = "題名は全角20文字[半角40文字]までです"				if length($ptitle) > 40;
	$mes = "題名を記入してください"								unless $ptitle;
	return if $mes;

	open my $fh, "+< $logdir/contest_prepare.cgi" or &error("$logdir/contest_prepare.cgiファイルが開けません");
	eval { flock $fh, 2; };
	my $head_line = <$fh>;
	my($etime, $round) = split /<>/, $head_line;
	my @lines = ($head_line);
	while ($line = <$fh>) {
		my($stitle, $name, $guild, $vote, $comment, $vote_names, $content) = split /<>/, $line;
		
		if ($name eq $m) {
			$mes = "【$stitle】という作品で、すでにエントリー済みです";
			return;
		}
		elsif ($ptitle eq $stitle) {
			$mes = "同じタイトルの作品がすでにエントリーされています";
			return;
		}
		push @lines, $line;
	}
	push @lines, "$ptitle<>$m<>$m{guild}<>0<><><>$entry_photo<>\n";
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;

	$npc_com .= "第$round回フォトコンテストに『$ptitle』という題名でエントリーしました";
}
sub is_entry_contest {
	open my $fh, "< $logdir/contest_entry.cgi" or &error("$logdir/contest_entry.cgiファイルが読み込めません");
	my $head_line = <$fh>;
	while (my $line = <$fh>) {
		my($stitle, $name, $guild, $vote, $comment, $vote_names, $content) = split /<>/, $line;
		return 1 if $name eq $m;
	}
	close $fh;
	return 0;
}


#=================================================
# ＠とうひょう
#=================================================
sub touhyou {
	my $target = shift;
	my($ptitle, $pcom) = split /＠こめんと&gt;/, $target;

	my $count = 0;
	my $p = '';
	open my $fh, "+< $logdir/contest_entry.cgi" or &error("$logdir/contest_entry.cgiファイルが開けません");
	eval { flock $fh, 2; };
	my $head_line = <$fh>;
	my($etime, $round) = split /<>/, $head_line;
	my @lines = ($head_line);
	while ($line = <$fh>) {
		my($stitle, $name, $guild, $vote, $comment, $vote_names, $content) = split /<>/, $line;
		
		if ($ptitle eq $stitle) {
			if (&add_vote_name) {
				$mes = "第$round回のフォトコンテストには、すでに投票済みです";
				return;
			}
			else {
				++$vote;
				$vote_names .= "$m,";
				$comment .= "$m『$pcom』," if $pcom;
				$mes = "$stitleに投票しました";
			}
		}
		else {
			++$count;
			$p .= qq|<hr color="#CCCC00"/><span onclick="text_set('＠とうひょう>$stitle＠こめんと>')"><span class="strong">作品No.$count『$stitle』</span><br>$content</span>|;
		}
		push @lines, "$stitle<>$name<>$guild<>$vote<>$comment<>$vote_names<>$content<>\n";
	}
	if ($mes) {
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
		close $fh;
		return;
	}
	close $fh;

	$mes = qq|どの作品に投票しますか？<br><div class="view" style="font-weight: normal; color: #FFF;">$p</div>|;
}
# ------------------
sub add_vote_name {
	open my $fh, "+< $logdir/contest_vote_name.cgi" or &error("$logdir/contest_vote_name.cgiファイルが開けません");
	eval { flock $fh, 2; };
	my $line = <$fh>;
	$line =~ tr/\x0D\x0A//d;
	if ($line =~ /,\Q$m{name}\E,/) {
		close $fh;
		return 1;
	}
	$line .= "$m{name},";
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh $line;
	close $fh;
	return 0;
}


1; # 削除不可
