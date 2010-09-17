#=================================================
# 冒険準備・作成 Created by Merino
#=================================================
# 場所名
$this_title = 'カジノ';

# NPC名
$npc_name = '@ﾊﾞﾆｰ';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/casino";

# 背景画像
$bgimg   = "$bgimgdir/casino.gif";

# 部屋名の最大文字数(半角)
$max_title = 50;

# 最大参加人数
$max_party = 8;

# 最低賭けｺｲﾝ
$min_bet   = 10;

# 賭けレート
@rates = (1, 5, 10, 20, 50, 100, 500, 1000, 5000);

# 進行スピード
%speeds = (
#	秒数	=> ['セレクト名', "画像ファイル"],
	12		=> ['さくさく', "$icondir/etc/speed_sakusaku.gif"],
	18		=> ['まったり', "$icondir/etc/speed_mattari.gif"],
	28		=> ['じっくり', "$icondir/etc/speed_jikkuri.gif"],
);


# 放置部屋(ログの更新なし)の自動削除時間(秒)
$auto_delete_casino_time = 1800;

# 交換リスト
my @prizes = (
# 種類 1=武器,2=防具,3=道具 
#*交換は必要枚数で判断しているので、同じ枚数が複数はダメ
#  [0]*必要枚数,[1]種類,[2]No
	[0,			0,		0,	],
	[100,		3,		4,	],
	[300,		3,		12,	],
	[700,		3,		6,	],
	[2000,		3,		32,	],
	[4000,		3,		38,	],
	[5000,		3,		39,	],
	[8000,		2,		34,	],
	[30000,		1,		31,	],
	[70000,		1,		40,	],
	[80000,		1,		38,	],
	[180000,	3,		106,],
	[200000,	3,		105,],
);


#=================================================
# 画面ヘッダー
#=================================================
sub header_html {
	print qq|<div class="mes">【$this_title】 コイン<b>$m{coin}</b>枚 / ゴールド<b>$m{money}</b>G</div>|;
	print qq|<div class="view">|;
	&casino_html;
	print qq|</div>|;
}


#=================================================
# はなす言葉
#=================================================
@words = (
	"コインは１枚20Gです☆",
	"ゴールドをコインに両替してね☆",
	"賞品は他ではなかなか手に入れることができないレアなアイテムばかりよ☆",
	"スロットの絵柄を３つそろえるとコインが増えて幸せになれるわよ☆",
	"ゆっくりしていってね☆",
);

sub shiraberu_npc {
	$mes = "$npc_name「きゃぁッ☆エッチィ～☆」";
}


#=================================================
# 追加アクション
#=================================================
push @actions, 'つくる';
push @actions, 'さんか';
push @actions, 'けんがく';
push @actions, ('＄1すろっと', '＄10すろっと', '＄50すろっと','＄100すろっと', 'こうかん', 'りょうがえ',);
$actions{'つくる'}   = sub{ &tsukuru }; 
$actions{'さんか'}   = sub{ &sanka }; 
$actions{'けんがく'} = sub{ &kengaku }; 
$actions{'ドッペル'} = sub{ &doppel }; 
$actions{'ハイロウ'} = sub{ &highlow }; 
$actions{'インディアン'} = sub{ &indian }; 
$actions{'＄1すろっと'}   = sub{ &slot_1   }; 
$actions{'＄10すろっと'}  = sub{ &slot_10  }; 
$actions{'＄50すろっと'}  = sub{ &slot_50  }; 
$actions{'＄100すろっと'} = sub{ &slot_100 }; 
$actions{'こうかん'}      = sub{ &koukan  }; 
$actions{'りょうがえ'}    = sub{ &ryougae }; 

#=================================================
# 部屋一覧
#=================================================
sub casino_html {
	opendir my $dh, "$casinodir" or &error("$casinodirディレクトリが開けません");
	while (my $dir_name = readdir $dh) {
		next if $dir_name =~ /\./;
		
		# 放置部屋削除(30分以上ログの更新なし)
		my($mtime) = (stat("$casinodir/$dir_name/log.cgi"))[9];
		if ($time > $mtime + $auto_delete_casino_time) {
			&auto_delete_casino($dir_name);
			next;
		}

		open my $fh, "< $casinodir/$dir_name/member.cgi";
		my $head_line = <$fh>;
		my($speed,$stage,$round,$leader,$p_name,$p_pass,$p_join,$win,$bet,$is_visit,$now_bet,$max_bet) = split /<>/, $head_line;
		my $count = 1;
		my $p = qq| <span onclick="text_set('＠しらべる>$leader ')"><img src="$icondir/etc/mark_leader.gif" alt="リーダー" />$leader</span> / |;
		while (my $line = <$fh>) {
			my($name,$laddr,$color) = split /<>/, $line;
			next if $leader eq $name;
			$p .= qq|<span onclick="text_set('＠しらべる>$name ')">$name</span> / |;
			++$count;
		}
		close $fh;
		my $bet_name = $stage eq 'ドッペル' ? "賭けｺｲﾝ<b>$bet</b>枚" : "レート<b>$bet</b>";
		my $party_data = qq|$p_name【$stage】<img src="$speeds{$speed}[1]" alt="$speeds{$speed}[0]" /> <span class="">$bet_name</span> 【<b>$count</b>/<b>$p_join</b>】|;
		my $aikotoba = $p_pass ? '＠あいことば>' : ' ';
		if ($round > 0) {
			if ($count >= $p_join) {
				print !$is_visit ? qq|<img src="$icondir/etc/full.gif" alt="対戦中" /> $party_data 見学× $p<hr size="1" />|
					: qq|<span onclick="text_set('＠けんがく>$p_name$aikotoba')"><img src="$icondir/etc/playing.gif" alt="対戦中" /> $party_data</span>$p<hr size="1" />|;
			}
			else {
				print !$is_visit ? qq|<img src="$icondir/etc/playing.gif" alt="対戦中" /> $party_data 見学× $p<hr size="1" />|
					: qq|<span onclick="text_set('＠さんか>$p_name$aikotoba')"><img src="$icondir/etc/playing.gif" alt="対戦中" /> $party_data</span>$p<hr size="1" />|;
			}
		}
		elsif ($count >= $p_join) {
			print !$is_visit ? qq|<img src="$icondir/etc/full.gif" alt="まんいん" /> $party_data 見学× $p<hr size="1" />|
				: qq|<span onclick="text_set('＠けんがく>$p_name$aikotoba')"><img src="$icondir/etc/full.gif" alt="まんいん" /> $party_data</span>$p<hr size="1" />|;
		}
		else {
			print qq|<span onclick="text_set('＠さんか>$p_name$aikotoba')"><img src="$icondir/etc/waitting.gif" alt="たいき中" /> $party_data</span>$p<hr size="1" />|;
		}
	}
	closedir $dh;
}
sub auto_delete_casino { # 放置自動削除
	my $dir_name = shift;
	open my $fh, "< $casinodir/$dir_name/member.cgi";
	my $head_line = <$fh>;
	while (my $line = <$fh>) {
		my($name,$color) = (split /<>/, $line)[0,2];
		next if $color eq $npc_color;
		&regist_you_data($name, 'lib', '');
		&regist_you_data($name, 'sleep', 3600);
	}
	close $fh;
	&delete_directory("$casinodir/$dir_name");
}

#=================================================
# ＠つくる
#=================================================
sub tsukuru {
	# 参加人数
	my $join_select = qq|<select name="p_join" class="select1">|;
	for my $i (2 .. $max_party-1) {
		$join_select .= qq|<option value="$i">$i人</option>|;
	}
	$join_select .= qq|<option value="$max_party" selected="selected">$max_party人</option>|;
	$join_select .= qq|</select>|;

	# レート
	my $rate_select = qq|<select name="bet" class="select1">|;
	for my $i (0..$#rates) {
		$rate_select .= qq|<option value="$i">$rates[$i]</option>|;
	}
	$rate_select .= qq|</select>|;

	# 進行速度
	my $speed_select = qq|<select name="speed" class="select1">|;
	for my $k (sort { $a <=> $b } keys %speeds) {
		$speed_select .= qq|<option value="$k">$speeds{$k}[0]</option>|;
	}
	$speed_select .= qq|</select>|;
	
	$mes = <<"EOM";
<table><tr><td>
<form method="$method" action="$script">
	<input type="hidden" name="comment" value="＠インディアン" />
	<input type="hidden" name="id" value="$id" /><input type="hidden" name="pass" value="$pass" />
	<table class="table1">
		<tr><th>＠インディアン</th></tr>
		<tr><td>部屋名：</td><td><input type="text" name="p_name" class="text_box1" /></td></tr>
		<tr><td>進行速度：</td><td>$speed_select</td></tr>
		<tr><td>参加人数：</td><td>$join_select</td></tr>
		<tr><td>レート：</td><td>$rate_select</td></tr>
		<tr><td>合言葉：</td><td><input type="text" name="p_pass" class="text_box_s" />　</td></tr>
		<tr><td>見学可：<input type="checkbox" name="is_visit" value="1" checked="checked"></td><td><input type="submit" value="＠インディアン" /></td></tr>
	</table>
</form>
</td><td>
<form method="$method" action="$script">
	<input type="hidden" name="comment" value="＠ハイロウ" />
	<input type="hidden" name="id" value="$id" /><input type="hidden" name="pass" value="$pass" />
	<table class="table1">
		<tr><th>＠ハイロウ</th></tr>
		<tr><td>部屋名：</td><td><input type="text" name="p_name" class="text_box1" /></td></tr>
		<tr><td>進行速度：</td><td>$speed_select</td></tr>
		<tr><td>参加人数：</td><td>$join_select</td></tr>
		<tr><td>レート：</td><td>$rate_select</td></tr>
		<tr><td>合言葉：</td><td><input type="text" name="p_pass" class="text_box_s" />　</td></tr>
		<tr><td>見学可：<input type="checkbox" name="is_visit" value="1" checked="checked"></td><td><input type="submit" value="＠ハイロウ" /></td></tr>
	</table>
</form>
</td><td>
<form method="$method" action="$script">
	<input type="hidden" name="comment" value="＠ドッペル" />
	<input type="hidden" name="id" value="$id" /><input type="hidden" name="pass" value="$pass" />
	<table class="table1">
		<tr><th>＠ドッペル</th></tr>
		<tr><td>部屋名：</td><td><input type="text" name="p_name" class="text_box1" /></td></tr>
		<tr><td>進行速度：</td><td>$speed_select</td></tr>
		<tr><td>参加人数：</td><td>$join_select</td></tr>
		<tr><td>賭けｺｲﾝ：</td><td><input type="text" name="bet" class="text_box_s" style="text-align: right;" value="$min_bet" />枚</td></tr>
		<tr><td>合言葉：</td><td><input type="text" name="p_pass" class="text_box_s" />　</td></tr>
		<tr><td>見学可：<input type="checkbox" name="is_visit" value="1" checked="checked"></td><td><input type="submit" value="＠ドッペル" /></td></tr>
	</table>
</form>
</td></tr></table>
EOM
}
#=================================================
# 入力チェック
#=================================================
sub check_create_casino {
	my($p_name) = @_;
	
	if ($p_name eq 'ドッペル') {
		$mes = "賭けｺｲﾝは最低でも $min_bet 枚必要です"	if $in{bet} < $min_bet;
		$mes = "賭けｺｲﾝは最低でも 1 枚必要です"			if $in{bet} < 1;
		$mes = "賭けｺｲﾝが足りません"					if $in{bet} > $m{coin};
	}
	else {
		$mes = "レートが異常です"							if $in{bet} < 0 || $in{bet} > @rates;
		$in{bet} = $rates[$in{bet}];
		$mes = "レート$in{bet}で遊ぶためのｺｲﾝが足りません"	if $m{coin} < $in{bet} * 5;
	}
	$mes = "参加人数が異常です"		if $in{p_join} < 2 || $in{p_join} > $max_party;
	return if $mes;

	$in{is_visit} = 1 if $in{is_visit} =~ /[^01]/;
	$mes = "進行速度が異常です"		unless defined $speeds{$in{speed}};
	$mes = "部屋名は半角$max_title文字までです"						if length($in{p_name}) > $max_title;
	$mes = "部屋名に不正な空白が含まれています"						if $in{p_name} =~ /　|\s/;
	$mes = "部屋名に不正な文字( ,;\"\'&<>\\\/@ )が含まれています"	if $in{p_name} =~ /[,;\"\'&<>\\\/@]/;
	$mes = "部屋名に不正な文字( ＠ )が含まれています"				if $in{p_name} =~ /＠/;
	$mes = "部屋名を決めてください"	unless $in{p_name};
}
#=================================================
# ＠インディアン
#=================================================
sub indian {
	&check_create_casino('インディアン');
	return if $mes;
	$in{stage} = 'インディアン';
	$in{now_bet} = $in{bet};
	&_create_room;
	$m{lib} = 'casino_indian';
}
#=================================================
# ＠ハイロウ
#=================================================
sub highlow {
	&check_create_casino('ハイロウ');
	return if $mes;
	$in{stage} = 'ハイロウ';
	$in{now_bet} = $in{bet};
	&_create_room;
	$m{lib} = 'casino_highlow';
}
#=================================================
# ＠ドッペル
#=================================================
sub doppel {
	&check_create_casino('ドッペル');
	return if $mes;
	$in{stage} = 'ドッペル';
	$in{now_bet} = 1;
	&_create_room;
	$m{lib} = 'casino_doppel';
}



# 新規部屋作成
sub _create_room {
	my $casino_id = unpack 'H*', $in{p_name};
	$mes = "同じ部屋名($in{p_name})がすでに存在します" if -d "$casinodir/$casino_id";
	return if $mes;

	my $bet_name = $in{stage} eq 'ドッペル' ? "賭けｺｲﾝ$in{bet}枚" : "レート$in{bet}";

	my $max_bet = $in{bet} * 5;
	mkdir "$casinodir/$casino_id", $mkdir or &error("$casinodir/$casino_idディレクトリが作成できません");
	open my $fh, "> $casinodir/$casino_id/member.cgi" or &error("$casinodir/$casino_id/member.cgiファイルが作成できません");
	print $fh "$in{speed}<>$in{stage}<>0<>$m<>$in{p_name}<>$in{p_pass}<>$in{p_join}<>0<>$in{bet}<>$in{is_visit}<>$in{now_bet}<>$max_bet<>\n";
	my $new_line = &get_battle_line($m{color},0);
	print $fh "$new_line\n";
	close $fh;
	chmod $chmod, "$casinodir/$casino_id/member.cgi";
	
	for my $k (qw/log bet win/) {
		open my $fh2, "> $casinodir/$casino_id/$k.cgi" or &error("$casinodir/$casino_id/$k.cgiファイルが作成できません");
		close $fh2;
		chmod $chmod, "$casinodir/$casino_id/$k.cgi";
	}
	
	$com = "<b>＠$in{stage}>$in{p_name}＠$bet_name＠参加人数>$in{p_join}人＠$speeds{$in{speed}}[0]";
 	if ($in{p_pass}) {
		$com .= "＠合言葉>必要";
	}
	else {
		$in{p_pass} = 'なし' ;
	}
	$com .= "</b>";

	$m{quest} = $casino_id;
	&reload("$in{p_name}部屋【$in{stage}】を作りました！<br />$bet_name, $speeds{$in{speed}}[0]，合言葉：$in{p_pass}，参加人数：$in{p_join}人");
	&leave_member($m);
}
#=================================================
# ＠さんか
#=================================================
sub sanka {
	my $target = shift;

	$mes = qq|<span onclick="text_set('＠ほーむ ')">$e2j{tired}がたまっています。「＠ほーむ」で家に帰り「＠ねる」で休んでください</span>|	if $m{tired} >= 100;
	return if $mes;

	unless ($target) {
		$mes = "どの部屋に参加しますか？";
		return;
	}
	
	my($p_name, $join_pass) = split /＠あいことば&gt;/, $target;
	my $casino_id = unpack 'H*', $p_name;
	$com =~ s/(.+)＠あいことば&gt;(.+)/$1/; # 発言した＠あいことば～を削除

	if ($p_name && -d "$casinodir/$casino_id") {
		&add_member($casino_id,$join_pass);
	}
	else {
		$mes = "参加しようとした部屋は、解散してしまったようです";
	}
}

#=================================================
# ＠さんか処理
#=================================================
sub add_member {
	my($casino_id,$join_pass) = @_;
	
	my @lines = ();
	open my $fh, "+< $casinodir/$casino_id/member.cgi" or &error("$casinodir/$casino_id/member.cgiファイルが作成できません");
	eval { flock $fh, 2; };
	my $head_line = <$fh>;
	my($speed,$stage,$round,$leader,$p_name,$p_pass,$p_join,$win,$bet,$is_visit) = split /<>/, $head_line;
	
	$mes = "$p_nameに参加するためのｺｲﾝが足りません"		if $bet > $m{coin};
	$mes = "$p_nameに参加するための合言葉が違います"	if $p_pass ne '' && $p_pass ne $join_pass;
#	$mes = "対戦途中から参加することはできません"		if $round > 0;
	return if $mes;
	
	push @lines, $head_line;

	while (my $line = <$fh>) {
		my($name,$laddr,$gcolor) = (split /<>/, $line)[0..2];
		if ($name eq $m) {
			$mes = "同じ名前のプレイヤーがすでに参加しています";
			return;
		}
		elsif ($addr eq $laddr) {
			$mes = "ＩＰアドレスが同じプレイヤーがすでに参加しています。";
#			$mes .= "<br />多重登録容疑で追放騎士団に追加申\請されました。";
#			$m{wt} = $time;
#			&add_exile($m,    "【多重登録容疑】$nameと同じIPアドレス");
#			&add_exile($name, "【多重登録容疑】$mと同じIPアドレス");
			return;
		}
		push @lines, $line;
	}
	if (@lines-1 >= $p_join) {
		$mes = "$p_nameは定員がいっぱいで参加することができません";
		return;
	}
	
	# 参加条件OK
	my($color) ||= (split /<>/, $lines[1])[2];
	my $new_line = &get_battle_line($color,$type);
	push @lines, "$new_line\n";
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	$m{lib} = $stage eq 'ドッペル' ? 'casino_doppel'
			: $stage eq 'ハイロウ' ? 'casino_highlow'
			:                        'casino_indian';
	$m{quest} = $casino_id;
	&reload("$p_nameに参加します");

	&leave_member($m);
}

#=================================================
# ＠けんがく
#=================================================
sub kengaku {
	my $target = shift;

	unless ($target) {
		$mes = "どの部屋を見学しますか？";
		return;
	}
	
	my($p_name, $join_pass) = split /＠あいことば&gt;/, $target;
	my $casino_id = unpack 'H*', $p_name;
	$com =~ s/(.+)＠あいことば&gt;(.+)/$1/; # 発言した＠あいことば～を削除

	if ($p_name && -d "$casinodir/$casino_id") {
		open my $fh, "< $casinodir/$casino_id/member.cgi" or &error("$casinodir/$casino_id/member.cgiファイルが読み込めません");
		my $head_line = <$fh>;
		close $fh;

		my($speed,$stage,$round,$leader,$p_name,$p_pass,$p_join,$win,$bet,$is_visit) = split /<>/, $head_line;
		if (!$is_visit) {
			$mes = "$p_nameの見学はできません";
			return;
		}
		elsif ($p_pass ne '' && $p_pass ne $join_pass) {
			$mes = "$p_nameを見学するための合言葉が違います";
			return;
		}
		
		$m{lib} = $stage eq 'ドッペル' ? 'casino_doppel'
				: $stage eq 'ハイロウ' ? 'casino_highlow'
				:                        'casino_indian';
		$m{quest} = $casino_id;
		$mes = "$p_nameを見学します";
		&reload("$p_nameを見学します");
		&leave_member($m);
	}
	else {
		$mes = "見学しようとした部屋は、解散してしまったようです";
	}
}


#=================================================
# ＠すろっと
#=================================================
sub slot_1   { &_slot(1) }
sub slot_10  { &_slot(10) }
sub slot_50  { &_slot(50) }
sub slot_100 { &_slot(100) }
sub _slot {
	my $bet = shift;
	
	if ($m{tired} >= 100) {
		$mes = qq|<span onclick="text_set('＠ほーむ ')">$e2j{tired}がたまっています。「＠ほーむ」で家に帰り「＠ねる」で休んでください</span>|;
		return;
	}
	if ($m{coin} < $bet) {
		$mes = qq|<span onclick="text_set('＠りょうがえ ')">＄$betスロットをするコインが足りません。「＠りょうがえ」でコインを両替してください</span>|;
		return;
	}
	
	my @m = ('∞','♪','†','★','７');
	my @o = (3,10, 20,  50,  70,  100); # オッズ 一番左はチェリーが2つそろいのとき
	my @s = ();
	$s[$_] = int(rand(@m)) for (0 .. 2);
	$mes .= qq|<span onclick="text_set('＠＄$betすろっと')">|;
	$mes .= "\$$betスロット<br />";
	$mes .= "【$m[$s[0]]】【$m[$s[1]]】【$m[$s[2]]】<br />";
	$m{coin} -= $bet;

	# 連打防止策
	$act_time *= 0.5;
	$m{wt}  = $time + $act_time;
	$nokori = $act_time;

	if ($s[0] == $s[1]) { # 1つ目と2つ目
		if ($s[1] == $s[2]) { # 2つ目と3つ目
			my $v = $bet * $o[$s[0]+1]; # +1 = チェリー2そろい
			$m{coin} += $v;
			$mes .= "なんと!! $m[$s[0]] が3つそろいました!!<br />";
			$mes .= "おめでとうございます!!<br />";
			$mes .= "***** コイン $v 枚 GET !! *****<br />";
		}
		elsif ($s[0] == 0) { # チェリーのみ1つ目と2つ目がそろえばよい
			my $v = $bet * $o[0];
			$m{coin} += $v;
			$mes .= "チェリーが2つそろいました♪<br />";
			$mes .= "コイン $v 枚Up♪<br />";
		}
		else {
			$mes .= "ハズレ<br />";
			$m{tired} += 1;
		}
	}
	else {
		$mes .= "ハズレ<br />";
		$m{tired} += 1;
	}
	$mes .= "</span>";
}


#=================================================
# ＠こうかん
#=================================================
sub koukan {
	my $target = shift;
	
	my $p = qq|<table class="table1"><tr><th>賞品</th><th>ｺｲﾝ</th></tr>|;
	for my $i (1 .. $#prizes) {
		if ("$prizes[$i][0]枚" eq $target) {
			if ($m{coin} >= $prizes[$i][0]) {
				if ($prizes[$i][1] eq '1') {
					&send_item($m, $prizes[$i][1], $prizes[$i][2]);
					$npc_com = "コイン$targetの賞品と交換ですね！$weas[ $prizes[$i][2] ][1]は$mの預かり所に送っておきました";
				}
				elsif ($prizes[$i][1] eq '2') {
					&send_item($m, $prizes[$i][1], $prizes[$i][2]);
					$npc_com = "コイン$targetの賞品と交換ですね！$arms[ $prizes[$i][2] ][1]は$mの預かり所に送っておきました";
				}
				else {
					&send_item($m, $prizes[$i][1], $prizes[$i][2]);
					$npc_com = "コイン$targetの賞品と交換ですね！$ites[ $prizes[$i][2] ][1]は$mの預かり所に送っておきました";
				}
				$m{coin} -= $prizes[$i][0];
			}
			else {
				$mes = "コイン$targetの賞品と交換するのにコインが足りません";
			}
			return;
		}
	
		$p .= qq|<tr onclick="text_set('＠こうかん>$prizes[$i][0]枚 ')"><td>|;
		$p .= $prizes[$i][1] eq '1' ? $weas[$prizes[$i][2]][1]
		    : $prizes[$i][1] eq '2' ? $arms[$prizes[$i][2]][1]
		    :                         $ites[$prizes[$i][2]][1]
		    ;
		$p .= qq|</td><td align="right">$prizes[$i][0]枚</td></tr>|;
	}
	$p  .= qq|</table>|;
	$mes = qq|どれと交換しますか？<br />$p|;
	$act_time = 0;
}


#=================================================
# ＠りょうがえ
#=================================================
sub ryougae {
	my $target = shift;
	$target =~ s/枚//;

	if ($target < 1 || $target =~ /[^0-9]/) {
		$mes = qq|<span onclick="text_set('＠りょうがえ>')">コイン１枚 20 Gです。いくら両替しますか？</span>|;
		return;
	}

	my $need_money = $target * 20;
	if ($need_money > $m{money}) {
		$mes = "ゴールドが足りません。コイン$target枚を両替するには $need_money G必要です";
		return;
	}
	
	$m{coin}  += $target;
	$m{money} -= $need_money;
	$npc_com = "$target枚のコインと両替しました";
}


#=================================================
# バトル用データ作成 @casino_datasの値をセット
#=================================================
sub get_battle_line {
	my $color = shift;
	my %p = %m;
	
	$p{card}   = 0;
	$p{action} = '待機中';
	
	my $line = '';
	for my $k (@casino_datas) {
		$line .= "$p{$k}<>";
	}
	return $line;
}


1; # 削除不可
