my $yid = unpack 'H*', $m{home};
if (!$m{home} || !-d "$userdir/$yid") { my $yhome = $m{home}; $m{home} = $m; &write_user; &error("$yhomeという家は見つかりません"); }
#=================================================
# ホーム Created by Merino
#=================================================
# 手紙、手紙送る、アイテム使用 飾る

# 場所名
$this_title = "$m{home}の家";

# ログに使うファイル(.cgi抜き)
$this_file  = "$userdir/$yid/home";

# 背景画像
$bgimg   = "$userdir/$yid/bgimg.gif";

$max_monster_word = 120;

#=================================================
# 他人の家ならここまで
unless ($m eq $m{home}) {
	push @actions, 'ねる';
	push @actions, 'あいてむずかん';
	push @actions, 'もんすたーぶっく';
	push @actions, 'じょぶますたー';
	push @actions, 'ぷろふぃーる';
	$actions{'ねる'}             = sub{ &neru };
	$actions{'あいてむずかん'}   = sub{ &aitemuzukan  };
	$actions{'もんすたーぶっく'} = sub{ &monster_book };
	$actions{'じょぶますたー'}   = sub{ &job_master   };
	$actions{'ぷろふぃーる'}     = sub{ &profile      };
	return 1;
}

#=================================================

#=================================================
# 以下、自分の家なら
#=================================================
if (-f "$userdir/$yid/letter_flag.cgi") {
	print qq|<div class="get">手紙が届いています</div>|;
	unlink "$userdir/$yid/letter_flag.cgi" or &error("$userdir/$yid/letter_flag.cgiファイルが削除できません");
}
if (-f "$userdir/$yid/money_flag.cgi") {
	print qq|<div class="get">お金が預かり所に届いています</div>|;
	unlink "$userdir/$yid/money_flag.cgi" or &error("$userdir/$yid/money_flag.cgiファイルが削除できません");
}
if (-s "$userdir/$yid/send_item_mes.cgi") {
	open my $fh, "+< $userdir/$yid/send_item_mes.cgi" or &error("$userdir/$yid/send_item_mes.cgiファイルが開けません");
	while (my $send_message = <$fh>) {
		print qq|<div class="get">$send_message</div>|;
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	close $fh;
}


#=================================================
# 追加アクション
#=================================================
push @actions, 'ねる';
push @actions, 'あいてむずかん';
push @actions, 'もんすたーぶっく';
push @actions, 'じょぶますたー';
push @actions, 'ぷろふぃーる';
push @actions, 'br';
push @actions, 'つかう';
push @actions, 'てがみをかく';
push @actions, 'てがみをよむ';
push @actions, 'からー';
push @actions, 'ことばをおしえる';
$actions{'ねる'}         = sub{ &neru };
$actions{'あいてむずかん'}   = sub{ &aitemuzukan };
$actions{'もんすたーぶっく'} = sub{ &monster_book };
$actions{'じょぶますたー'}   = sub{ &job_master   };
$actions{'ぷろふぃーる'}     = sub{ &profile      };
$actions{'つかう'}       = sub{ &thukau };
$actions{'てがみをかく'} = sub{ &tegamiwokaku };
$actions{'てがみをよむ'} = sub{ &tegamiwoyomu };
$actions{'からー'}       = sub{ &color };
$actions{'ことばをおしえる'} = sub{ &kotobawooshieru };
#=================================================
# 画面一番上に表示(場所の名前、ステータスなど)
#=================================================
sub header_html { 
	if ($m{home} eq $m) {
		my $next_lv = $m{lv} * $m{lv} * 10;
		print qq|<div class="mes">【$this_title】 $e2j{lv}<b>$m{lv}</b> / $e2j{exp}<b>$m{exp}</b>Exp / 次の$e2j{lv}<b>$next_lv</b>Exp / 転職回数<b>$m{job_lv}</b>回 / $e2j{money}<b>$m{money}</b>G / 疲労度<b>$m{tired}</b>％|;
		print qq|<span onclick="text_set('＠つかう>$weas[$m{wea}][1] ')"> / E：$weas[$m{wea}][1]</span>| if $m{wea};
		print qq|<span onclick="text_set('＠つかう>$arms[$m{arm}][1] ')"> / E：$arms[$m{arm}][1]</span>| if $m{arm};
		print qq|<span onclick="text_set('＠つかう>$ites[$m{ite}][1] ')"> / E：$ites[$m{ite}][1]</span>| if $m{ite};
		print qq|</div>|
	}
	else {
		print qq|<div class="mes">【$this_title】</div>|;
	}
}

#=================================================
# ＠もんすたーぶっく
#=================================================
sub monster_book {
	$mes = qq|<form action="$userdir/$yid/monster_book.html" target="_blank"><input type="submit" value="$m{home}のモンスターブック" /></form>|;
}

#=================================================
# ＠あいてむずかん
#=================================================
sub aitemuzukan {
	$mes = "$m{home}のアイテム図鑑";
	$m{lib} = 'collection';
	&auto_reload;
}
#=================================================
# ＠じょぶますたー
#=================================================
sub job_master {
	$mes = "$m{home}のジョブマスター";
	$m{lib} = 'job_master';
	&auto_reload;
}
#=================================================
# ＠ぷろふぃーる
#=================================================
sub profile {
	$mes = "$m{home}のプロフィール";
	$m{lib} = 'profile';
	&auto_reload;
}

#=================================================
# ＠ねる
#=================================================
sub neru {
	my($login_list, $login_count) = &get_login_member;
	
	$m{sleep} = $login_count >= 30 ? $sleep_time * 60 * 3
			  : $login_count >= 20 ? $sleep_time * 60 * 2
			  : 				     $sleep_time * 60;
	$com .= qq|$mはベッドにもぐりこんだ！|;
	
	$m{recipe} =~ s/^0/1/o;
}


#=================================================
# ＠からー
#=================================================
sub color {
	$target = shift;
	
	if ($target =~ /(#[0-9a-fA-F]{6})/) {
		$com .= qq|カラーを<font color="$1">$1</font>に変更しました|;
		$m{color} = $1;
		return;
	}
	else {
		my %sample_colors = (
			'レッド'		=> '#FF3333',
			'ピンク'		=> '#FF33CC',
			'オレンジ'		=> '#FF9933',
			'イエロー'		=> '#FFFF33',
			'グリーン'		=> '#33FF33',
			'アクア'		=> '#33CCFF',
			'ブルー'		=> '#6666FF',
			'パープル'		=> '#CC66FF',
			'グレイ'		=> '#CCCCFF',
			'ホワイト'		=> '#FFFFFF',
			'エメラルド'	=> '#33FF99',
		);
		
		$mes  = qq|#から始まる(16進数の)カラーコードを記入してください<br />サンプル＞|;
		
		while (my($name, $c_code) = each %sample_colors) {
			$mes .= qq|<span onclick="text_set('＠からー>$c_code ')" style="color: $c_code;">$name</span> |;
		}
		return;
	}
}


#=================================================
# ＠つかう
#=================================================
sub thukau {
	my $target = shift;

	unless ($target) {
		$mes .= qq|<span onclick="text_set('＠つかう>$weas[$m{wea}][1] ')">$weas[$m{wea}][1]</span> / | if $m{wea};
		$mes .= qq|<span onclick="text_set('＠つかう>$arms[$m{arm}][1] ')">$arms[$m{arm}][1]</span> / | if $m{arm};
		$mes .= qq|<span onclick="text_set('＠つかう>$ites[$m{ite}][1] ')">$ites[$m{ite}][1]</span> / | if $m{ite};
		
		$mes .= qq|<br />|;
		open my $fh, "< $userdir/$id/depot.cgi" or &error("$userdir/$id/depot.cgiファイルが開けません");
		while (my $line = <$fh>) {
			my($kind, $no) = split /<>/, $line;
			if    ($kind eq '1') {
				$mes .= qq|<span onclick="text_set('＠つかう>$weas[$no][1] ')">$weas[$no][1]</span> / |;
			}
			elsif ($kind eq '2') {
				$mes .= qq|<span onclick="text_set('＠つかう>$arms[$no][1] ')">$arms[$no][1]</span> / |;
			}
			elsif ($kind eq '3') {
				$mes .= qq|<span onclick="text_set('＠つかう>$ites[$no][1] ')">$ites[$no][1]</span> / |;
			}
		}
		close $fh;
		
		return;
	}
	
	if    ($target eq $weas[$m{wea}][1]) {
		$mes = qq|武器名：$weas[$m{wea}][1] / 強さ：<b>$weas[$m{wea}][3]</b> / 重さ：<b>$weas[$m{wea}][4]</b> / 価格：<b>$weas[$m{wea}][2]</b>G|;
	}
	elsif ($target eq $arms[$m{arm}][1]) {
		$mes = qq|防具名：$arms[$m{arm}][1] / 強さ：<b>$arms[$m{arm}][3]</b> / 重さ：<b>$arms[$m{arm}][4]</b> / 価格：<b>$arms[$m{arm}][2]</b>G|;
	}
	elsif ($target eq $ites[$m{ite}][1]) {
		if ($ites[$m{ite}][3] eq '1') {
			$mes = "$ites[$m{ite}][1]は戦闘中でしか使えません";
		}
		elsif ($ites[$m{ite}][3] eq '2') {
			$com .= "$ites[$m{ite}][1]をつかった！";
			&{ $ites[$m{ite}][4] };
			return if $mes;
			$m{ite} = 0;
		}
		else {
			$mes = "$ites[$m{ite}][1]はここでは使えません";
		}
	}
	else {
		my $is_lost = 0;
		my @lines = ();
		open my $fh, "+< $userdir/$id/depot.cgi" or &error("$userdir/$id/depot.cgiファイルが開けません");
		eval { flock $fh, 2; };
		while (my $line = <$fh>) {
			my($kind, $no) = split /<>/, $line;

			if ($is_lost) {
				push @lines, $line;
				next;
			}
			elsif ($kind eq '1' && $weas[$no][1] eq $target) {
				$mes = qq|武器名：$weas[$no][1] / 強さ：<b>$weas[$no][3]</b> / 重さ：<b>$weas[$no][4]</b> / 価格：<b>$weas[$no][2]</b>G|;
				last;
			}
			elsif ($kind eq '2' && $arms[$no][1] eq $target) {
				$mes = qq|防具名：$arms[$no][1] / 強さ：<b>$arms[$no][3]</b> / 重さ：<b>$arms[$no][4]</b> / 価格：<b>$arms[$no][2]</b>G|;
				last;
			}
			elsif ($kind eq '3' && $ites[$no][1] eq $target) {
				if ($ites[$no][3] eq '2') {
					$com .= "$ites[$no][1]をつかった！";
					&{ $ites[$no][4] };
					return if $mes;
					$is_lost = 1;
					next;
				}
				else {
					$mes = "$ites[$no][1]はここでは使えません";
					last;
				}
			}
			push @lines, $line;
		}
		if ($is_lost) {
			seek  $fh, 0, 0;
			truncate $fh, 0;
			print $fh @lines;
			&get_depot_c; # 満杯かどうかチェック
		}
		close $fh;
	}
}

#=================================================
# ＠てがみをかく
#=================================================
sub tegamiwokaku {
	my $y = shift;

	$this_file = "$userdir/$id/letter_log";
	if ($y) {
		&send_letter($y, $com);
		return if $mes;
		$mes = "$yに手紙を送りました";
		
		my $new_line = "$time<>$date<>$m<>$addr<>$m{color}<>$com<><>\n";
		# 自分用の送信ログ
		my @lines = ();
		open my $fh, "+< $userdir/$id/letter_log.cgi" or &error("$userdir/$id/letter_log.cgiファイルが開けません");
		eval { flock $fh, 2; };
		while (my $line = <$fh>) {
			push @lines, $line;
			last if @lines+1 >= $max_log;
		}
		unshift @lines, $new_line;
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
		close $fh;
	}
	else {
		$mes = qq|<span onclick="text_set('＠てがみをかく')">『△△△＠てがみをかく>○○○』△△△に送りたい文を○○○に送り先の名前を書いてください。</span><br />↓送信済みの手紙|;
	}
}

#=================================================
# ＠てがみをよむ
#=================================================
sub tegamiwoyomu {
	$this_file = "$userdir/$id/letter";
	$mes = "$mの受け取った手紙";
}


#================================================
# ＠はなす
#================================================
sub hanasu {
	if (@members <= 1) {
		$mes = "しかし、誰もいなかった…" ;
		return;
	}
	
	my $line;
	open my $fh, "< $userdir/$yid/hanasu.cgi" or &error("$userdir/$yid/hanasu.cgiファイルが読み込めません");
	rand($.) < 1 and $line = $_ while <$fh>;
	close $fh;
	$line =~ tr/\x0D\x0A//d; # 改行削除

	$npc_name = $members[int(rand(@members))];
	$npc_name = $members[0] unless $ms{$npc_name}{color} eq $npc_color;
	$npc_com  = $line;
}

#================================================
# ＠ことばをおしえる
#================================================
sub kotobawooshieru {
	my $target = shift;
	
	unless ($target) {
		$mes = qq|<span onclick="text_set('＠ことばをおしえる> ')">＠ことばをおしえる>○○○ で家にいるモンスターが＠はなすで話すようになります|;
		return;
	}
	
	if (@members <= 1) {
		$mes = "教える相手がいません";
	}
	elsif (length $target > $max_monster_word) {
		$mes = "言葉が長すぎます(半角$max_monster_word文字まで)";
	}
	else {
		$npc_name = $members[int(rand(@members))];
		$npc_name = $members[0] unless $ms{$npc_name}{color} eq $npc_color;
		$npc_com  = $target;

		my @lines = ();
		open my $fh, "+< $userdir/$id/hanasu.cgi" or &error("$userdir/$id/hanasu.cgiファイルが開けません");
		eval { flock $fh, 2; };
		while (my $line = <$fh>) {
			push @lines, $line;
			last if @lines >= $max_log-1;
		}
		unshift @lines, "$target\n";
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
		close $fh;
	}
}

#================================================
# レシピ使用
#================================================
sub learn_recipe {
	my @learns = @_;

	# レシピ一覧読み込み
	require './lib/_alchemy_recipe.cgi';

	# 完成させているレシピを除く
	my @lines = ();
	open my $fh, "+< $userdir/$id/recipe.cgi" or &errror("$userdir/$id/recipe.cgiファイルが読み込めません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		push @lines, $line;
		my($base, $sozai) = (split /<>/, $line)[1,2];
		delete($recipes{$base}{$sozai});
	}

	my %new_recipes = ();
	if (@learns) { # 習得できるレシピ制限
		for my $learn (@learns) {
			$new_recipes{$learn} = $recipes{$learn} if defined($recipes{$learn}) && values %{ $recipes{$learn} };
		}
	}
	else { # 全部習得可能(神のレシピ)
		for my $k (keys %recipes) {
			$new_recipes{$k} = $recipes{$k} if values %{ $recipes{$k} };
		}
	}
	
	my @bases = keys %new_recipes;
	if (@bases) {
		# 未習得のレシピをランダムで取得
		my $base = $bases[int rand @bases];
		my @sozais = keys %{ $recipes{$base} };
		my $sozai = $sozais[int rand @sozais];
		my $mix = $recipes{$base}{$sozai};

		push @lines, "0<>$base<>$sozai<>$mix<>\n";
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
		
		$com = "$m は錬金レシピを読んだ！【$base × $sozai ＝ ？？？】の錬金方法を習得した！";

	}
	else {
		$com = "この錬金レシピからこれ以上習得できる錬金方法はないようだ…";
	}

	close $fh;
}


1; # 削除不可
