#=================================================
# 預かり所 Created by Merino
#=================================================
# 場所名
$this_title = '預かり所';

# NPC名
$npc_name   = '@ﾆｷｰﾀ';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/depot";

# 背景画像
$bgimg   = "$bgimgdir/depot.gif";

# 送るの禁止アイテム(例＞'wea' => [1,2,3,4,5],)
%taboo_items = (
	'wea' => [], # 武器
	'arm' => [], # 防具
	'ite' => [], # 道具
);


#=================================================
# ＠はなすの会話
#=================================================
my($my_depot, $max_depot) = &get_depot_c;
@words = (
	"ここは$this_titleだけど、何か用かい？",
	"$mは、最大$max_depot個まで預けることができるぜ",
	"転職回数が増えるごとに預けられる個数も増えていくぜ",
	"＠おくる時は、送るアイテムと相手の名前を教えてくれな",
	"＠せいとんすると、武器、防具、道具の順に整頓できるぜ",
	"預かり所がまんぱんだと、相手からのアイテムが受け取れないぜ",
	"預かり所がまんぱんだと、クエストでの宝物を手に入れることができないぜ",
	"ここで売るのも専門店で売るのも売値は変わらないぜ",
);


#=================================================
# 追加アクション
#=================================================
push @actions, 'うる';
push @actions, 'あずける';
push @actions, 'ひきだす';
push @actions, 'せいとん';
push @actions, 'おくる';
$actions{'うる'}     = sub{ &uru      }; 
$actions{'あずける'} = sub{ &azukeru  }; 
$actions{'ひきだす'} = sub{ &hikidasu }; 
$actions{'せいとん'} = sub{ &seiton   }; 
$actions{'おくる'  } = sub{ &okuru    }; 


#=================================================
# ヘッダー表示
#=================================================
sub header_html {
	my $my_at = $m{at} + $weas[$m{wea}][3];
	my $my_df = $m{df} + $arms[$m{arm}][3];
	my $my_ag = $m{ag} - $weas[$m{wea}][4] - $arms[$m{arm}][4];
	$my_ag = 0 if $my_ag < 0;
	print qq|<div class="mes">【$this_title】 倉庫：<b>$my_depot</b>/<b>$max_depot</b>個 / $e2j{money} <b>$m{money}</b>G|;
	print qq| / $e2j{at} <b>$my_at</b> / $e2j{df} <b>$my_df</b> / $e2j{ag} <b>$my_ag</b> /|;
	print qq| E：$weas[$m{wea}][1]| if $m{wea};
	print qq| E：$arms[$m{arm}][1]| if $m{arm};
	print qq| E：$ites[$m{ite}][1]| if $m{ite};
	print qq|</div>|;
}

#=================================================
# ＠うる
#=================================================
sub uru {
	my $target = shift;
	
	my $is_find = 0;
	my $p = '';
	my @lines = ();
	open my $fh, "+< $userdir/$id/depot.cgi" or &error("$userdir/$id/depot.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($kind, $no) = split /<>/, $line;
		if ($kind eq '1') { # 武器
			my $buy_price = int($weas[$no][2] * 0.5);
			if (!$is_find && $weas[$no][1] eq $target) {
				$is_find = 1;
				$npc_com = "$weas[$no][1] の買取代の $buy_price Gです！";
				$m{money} += $buy_price;
			}
			else {
				$p .= qq|<span onclick="text_set('＠うる>$weas[$no][1] ')">$weas[$no][1] $buy_price G</span> / |;
				push @lines, $line;
			}
		}
		elsif ($kind eq '2') { # 防具
			my $buy_price = int($arms[$no][2] * 0.5);
			if (!$is_find && $arms[$no][1] eq $target) {
				$is_find = 1;
				$npc_com = "$arms[$no][1] の買取代の $buy_price Gです！";
				$m{money} += $buy_price;
			}
			else {
				$p .= qq|<span onclick="text_set('＠うる>$arms[$no][1] ')">$arms[$no][1] $buy_price G</span> / |;
				push @lines, $line;
			}
		}
		elsif ($kind eq '3') { # 道具
			my $buy_price = int($ites[$no][2] * 0.5);
			if (!$is_find && $ites[$no][1] eq $target) {
				$is_find = 1;
				$npc_com = "$ites[$no][1] の買取代の $buy_price Gです！";
				$m{money} += $buy_price;
			}
			else {
				$p .= qq|<span onclick="text_set('＠うる>$ites[$no][1] ')">$ites[$no][1] $buy_price G</span> / |;
				push @lines, $line;
			}
		}
	}
	if ($npc_com) {
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
		close $fh;
		&get_depot_c;
		return;
	}
	close $fh;
	
	$mes = qq|どれを売りますか？<br />$p|;
	$act_time = 0;
}

#=================================================
# ＠あずける
#=================================================
sub azukeru {
	my $target = shift;
	
	if ($m{is_full}) {
		$mes = "$max_depot個までしか預けることはできない";
		return;
	}
	
	if ($weas[$m{wea}][1] eq $target) {
		$npc_com = "$weas[$m{wea}][1]をお預かりしました";
		&send_item($m, 1, $m{wea});
		$m{wea} = 0;
	}
	elsif ($arms[$m{arm}][1] eq $target) {
		$npc_com = "$arms[$m{arm}][1]をお預かりしました";
		&send_item($m, 2, $m{arm});
		$m{arm} = 0;
	}
	elsif ($ites[$m{ite}][1] eq $target) {
		$npc_com = "$ites[$m{ite}][1]をお預かりしました";
		&send_item($m, 3, $m{ite});
		$m{ite} = 0;
	}
	
	if ($npc_com) {
		&get_depot_c;
		return;
	}
	
	$mes = qq|どれを預ける？<br />|;
	$mes .= qq|<span onclick="text_set('＠あずける>$weas[$m{wea}][1] ')">$weas[$m{wea}][1]</span> / | if $m{wea};
	$mes .= qq|<span onclick="text_set('＠あずける>$arms[$m{arm}][1] ')">$arms[$m{arm}][1]</span> / | if $m{arm};
	$mes .= qq|<span onclick="text_set('＠あずける>$ites[$m{ite}][1] ')">$ites[$m{ite}][1]</span> / | if $m{ite};
	$act_time = 0;
}

#=================================================
# ＠ひきだす
#=================================================
sub hikidasu {
	my $target = shift;
	
	# 送金があれば最初に受け取る
	if (-s "$userdir/$id/money.cgi") {
		&_get_money;
		return;
	}
	
	my $is_find = 0;
	my $p = '';
	my @lines = ();
	open my $fh, "+< $userdir/$id/depot.cgi" or &error("$userdir/$id/depot.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($kind, $no) = split /<>/, $line;
		if ($kind eq '1') { # 武器
			if (!$is_find && $weas[$no][1] eq $target) { # 交換
				$is_find = 1;
				if ($m{wea}) {
					$npc_com .= "$weas[$m{wea}][1]をお預かりしました。";
					push @lines, "1<>$m{wea}<>\n";
				}
				$m{wea} = $no;
				$npc_com .= "$weas[$m{wea}][1]をお返しします";
			}
			else {
				$p .= qq|<span onclick="text_set('＠ひきだす>$weas[$no][1] ')">$weas[$no][1]</span> / |;
				push @lines, $line;
			}
		}
		elsif ($kind eq '2') { # 防具
			if (!$is_find && $arms[$no][1] eq $target) { # 交換
				$is_find = 1;
				if ($m{arm}) {
					$npc_com .= "$arms[$m{arm}][1]をお預かりしました。";
					push @lines, "2<>$m{arm}<>\n";
				}
				$m{arm} = $no;
				$npc_com .= "$arms[$m{arm}][1]をお返しします";
			}
			else {
				$p .= qq|<span onclick="text_set('＠ひきだす>$arms[$no][1] ')">$arms[$no][1]</span> / |;
				push @lines, $line;
			}
		}
		elsif ($kind eq '3') { # 道具
			if (!$is_find && $ites[$no][1] eq $target) { # 交換
				$is_find = 1;
				if ($m{ite}) {
					$npc_com .= "$ites[$m{ite}][1]をお預かりしました。";
					push @lines, "3<>$m{ite}<>\n";
				}
				$m{ite} = $no;
				$npc_com .= "$ites[$m{ite}][1]をお返しします";
			}
			else {
				$p .= qq|<span onclick="text_set('＠ひきだす>$ites[$no][1] ')">$ites[$no][1]</span> / |;
				push @lines, $line;
			}
		}
	}
	if ($npc_com) {
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
		close $fh;
		
		require "./lib/_add_collection.cgi";
		&add_collection;
		return;
	}
	close $fh;
	
	$mes = qq|どれをひきだす？<br />$p|;
	$act_time = 0;
}
# ------------------
# ゴールドを受けとる
sub _get_money {
	open my $fh, "+< $userdir/$id/money.cgi" or &error("$userdir/$id/money.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($money, $message) = split /<>/, $line;
		$m{money} += $money;
		if ($money >= 0) {
			$mes.="$message として $money Gを受け取りました<br />";
		}
		else {
			$money *= -1;
			$mes.="$message として $money Gを支払いました<br />";
		}
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	close $fh;
}


#=================================================
# ＠せいとん
#=================================================
sub seiton {
	my @lines = ();
	open my $fh, "+< $userdir/$id/depot.cgi" or &error("$userdir/$id/depot.cgiファイルが開けません");
	eval { flock $fh, 2; };
	push @lines, $_ while <$fh>;
	@lines = map { $_->[0] }
				sort { $a->[1] <=> $b->[1] || $a->[2] <=> $b->[2] }
					map { [$_, split /<>/ ] } @lines;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	$npc_com = "預かっているアイテムをせいとんした";
}



#=================================================
# ＠おくる
#=================================================
sub okuru {
	my $target = shift;
	my($send, $name) = split /＠あいて&gt;/, $target;
	
#	if ($m{job_lv} < 1) {
#		$mes = "未転職の方は、送ることはできません。";
#		return;
#	}

	if ($name) {
		my $yid = unpack 'H*', $name;
		unless (-d "$userdir/$yid") {
			$mes = "$nameというプレイヤーは存在しません";
			return;
		}
		my %p = &get_you_datas($yid, 1);
		if ($p{is_full}) {
			$mes = "$nameの預かり所がいっぱいです";
			return
		}
		
		if ($send =~ /^([0-9]+)\x20?G?$/) {
			my $send_money = int($1);
			if ($send_money > $m{money}) {
				$mes = "そんなにお金をもっていません";
				return;
			}
			elsif ($send_money <= 0) {
				$mes = "送金は最低でも 1 G以上です";
				return;
			}
			
			$m{money} -= $send_money;
			&send_money($name, $send_money, "$mからの送金");
			$npc_com = "$send_money Gを $name に送りました";
			return;
		}
		elsif ($m{wea} && $weas[$m{wea}][1] eq $send) {
			for my $taboo_item (@{ $taboo_items{wea} }) {
				if ($weas[$taboo_item][1] eq $weas[$m{wea}][1]) {
					$mes = "$weas[$m{wea}][1]は送ることができません";
					return;
				}
			}
			$npc_com = "$weas[$m{wea}][1]を$nameに送りました";
			&send_item($name, 1, $m{wea}, $m);
			$m{wea} = 0;
		}
		elsif ($m{arm} && $arms[$m{arm}][1] eq $send) {
			for my $taboo_item (@{ $taboo_items{arm} }) {
				if ($arms[$taboo_item][1] eq $arms[$m{arm}][1]) {
					$mes = "$arms[$m{arm}][1]は送ることができません";
					return;
				}
			}
			$npc_com = "$arms[$m{arm}][1]を$nameに送りました";
			&send_item($name, 2, $m{arm}, $m);
			$m{arm} = 0;
		}
		elsif ($m{ite} && $ites[$m{ite}][1] eq $send) {
			for my $taboo_item (@{ $taboo_items{ite} }) {
				if ($ites[$taboo_item][1] eq $ites[$m{ite}][1]) {
					$mes = "$ites[$m{ite}][1]は送ることができません";
					return;
				}
			}
			$npc_com = "$ites[$m{ite}][1]を$nameに送りました";
			&send_item($name, 3, $m{ite}, $m);
			$m{ite} = 0;
		}
		
		&get_depot_c;
		return;
	}
	
	$mes  = qq|どれをだれに送る？<br />$p|;
	$mes .= qq|<span onclick="text_set('＠おくる>$weas[$m{wea}][1]＠あいて')">$weas[$m{wea}][1]</span> / | if $m{wea};
	$mes .= qq|<span onclick="text_set('＠おくる>$arms[$m{arm}][1]＠あいて')">$arms[$m{arm}][1]</span> / | if $m{arm};
	$mes .= qq|<span onclick="text_set('＠おくる>$ites[$m{ite}][1]＠あいて')">$ites[$m{ite}][1]</span> / | if $m{ite};
	$mes .= qq|<span onclick="text_set('＠おくる>$m{money}G＠あいて')">$m{money}G</span> / |;
	$act_time = 0;
}



1; # 削除不可
