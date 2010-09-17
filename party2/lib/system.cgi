&get_date; # 時間と日付は常時必要なので常に取得 Get $time,$date
#================================================
# サブルーチン集(よく使う処理) Created by Merino
#================================================
# 基本アクションコマンド
sub set_action {
	push @actions, ('br','いどう', 'まち', 'ほーむ');
	if ($m{guild}) {
		push @actions, 'ぎるど';
		$actions{'ぎるど'} = sub{ &girudo }
	}
	push @actions, ('ささやき', 'はなす', 'しらべる', 'ろぐあうと', 'すくしょ');
	$actions{'いどう'}   = sub{ &idou };
	$actions{'まち'}     = sub{ &machi };
	$actions{'ほーむ'}   = sub{ &homu };
	$actions{'はなす'}   = sub{ &hanasu };
	$actions{'しらべる'} = sub{ &shiraberu };
	$actions{'ささやき'} = sub{ &sasayaki };
	$actions{'ろぐあうと'} = sub{ &roguauto };
	$actions{'すくしょ'} = sub{ &sukusho }; 
}

#================================================
# プレイヤーデータ書き込み
#================================================
sub write_user {
	&error("プレイヤーデータの書き込みに失敗しました") if !$id || !$m{name};

	# -------------------
	# topのﾛｸﾞｲﾝﾘｽﾄに表示
	if ($time > $m{login_time} + $login_time * 60) {
		$m{login_time} = $time;
		
		open my $fh2, ">> $logdir/login.cgi";
		print $fh2 "$time<>$m{name}<>$m{color}<>$m{guild}<>$m{mes}<>$m{icon}<>\n";
		close $fh2;
	}

	$m{addr}  = $addr;
	$m{host}  = $host;
	$m{ltime} = $time;
	$m{ldate} = $date;
	# -------------------
	# ｽﾃｰﾀｽの最大値
	for my $k (qw/mhp hp mmp mp/) {
		$m{$k} = 999 if $m{$k} > 999;
	}
	for my $k (qw/at df ag/) {
		$m{$k} = 255 if $m{$k} > 255;
	}
	$m{coin}   = 0 if $m{coin} <= 0;
	$m{money}  = 999999 if $m{money} > 999999;
	
	# -------------------
	# 変数追加する場合は半角ｽﾍﾟｰｽか改行を入れて追加(順不同、並べ替え可(login_time以外))
	my @keys = (qw/
		login_time ldate name pass addr host lib wt sleep
		ltime quest home guild job_lv lv exp money medal coin coupon rare
		tired sex icon color job sp old_job old_sp mhp hp mmp mp at df ag wea arm ite
		orb is_full is_get is_eat kill_p kill_m cas_c hero_c mao_c alc_c help_c event recipe mes
	/);
	# ﾛｸﾞｲﾝした時間　最終ﾛｸﾞｲﾝ日　名前　ﾊﾟｽﾜｰﾄﾞ　IP　Host　lib　待ち時間　拘束時間
	# 最終ﾛｸﾞｲﾝ時間　参加ｸｴｽﾄ　滞在家　ｷﾞﾙﾄﾞ　転職回数　レベル経験値　お金　小さなメダル　福引券　レアポイント
	# 疲労度　性別　ｱｲｺﾝ　色　職業　ＳＰ　前職業　ＳＰ　最大HP　HP　最大MP　MP　攻　守　素　武器　防具　道具
	# ｵｰﾌﾞ　預かり所満杯ﾌﾗｸﾞ　宝取得ﾌﾗｸﾞ　飲食ﾌﾗｸﾞ　ﾌﾟﾚｲﾔｰ撃退数　ﾓﾝｽﾀｰ撃退数　カジノ熟練度　勇者熟練度　魔王熟練度　錬金数　手助け数　ダンジョンイベント　錬金レシピ　ﾒｯｾｰｼﾞ
	
	my $line;
	for my $k (@keys) {
		$line .= "$k;$m{$k}<>";
	}
	open my $fh, "> $userdir/$id/user.cgi";
	print $fh "$line\n";
	close $fh;
}

#================================================
# プレイヤーデータ読み込み
#================================================
sub read_user { # Get %m
	my $is_header = shift || 0;
	$id ||= unpack 'H*', $in{login_name};

	open my $fh, "< $userdir/$id/user.cgi" or &error("そのような名前$in{login_name}のプレイヤーが存在しません", $is_header);
	my $line = <$fh>;
	close $fh;
	
	%m = ();
	for my $hash (split /<>/, $line) {
		my($k, $v) = split /;/, $hash;
		$m{$k} = $v;
	}
	&error("パスワードが違います", $is_header) unless $m{pass} eq $pass;
	
	if ($m{ltime} + $wait_time > $time && !$in{is_auto}) {
		open my $fh2, ">> $userdir/$id/reload.cgi";
		print $fh2 "1<>";
		close $fh2;
		&error("更新の連打は禁止しています。最低でも $wait_time 秒は待ってください<br>※過度な更新連打は自動削除の対象となります", $is_header);
	}

	$m      = $m{name}; # 名前をよく使うので $m と省略
	$nokori = int($m{wt} - $time);
}

#=================================================
# ＠すくしょ
#=================================================
sub sukusho {
	my $target = shift || $this_title;
	
	my @lines = ();
	open my $fh, "+< $userdir/$id/screen_shot.cgi" or &error("$userdir/$id/screen_shot.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		push @lines, $line;
	}
	if (@lines >= $max_screen_shot) {
		$mes = qq|これ以上スクリーンショットを撮ることができません。フォトコン会場で「＠けす」してください</span>|;
		return;
	}
	my $new_line;
	$new_line .= qq|<div class="mes">【$target】</div>|;
	$new_line .= &member_html;
	$new_line .= &_sukusho_mes;
	unshift @lines, "$new_line\n";
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	&write_top_screen_shot($new_line);
	
	$mes = "スクリーンショットをとりました";
}
sub _sukusho_mes { # コメント三行取得
	my $count = 0;
	my $data = qq|<hr size="1" />|;
	open my $fh, "< $this_file.cgi" or &error("$this_file.cgi ファイルが開けません");
	while (my $line = <$fh>) {
		my($btime,$bdate,$bname,$baddr,$bcolor,$bcomment,$bto_name) = split /<>/, $line;
		next if $bto_name;
		$data .= qq|<font color="$bcolor">$bname</font>： $bcomment <font size="1">($bdate)</font><hr size="1" />|;
		last if ++$count >= 3;
	}
	close $fh;
	return $data;
}
sub write_top_screen_shot { # トップに表示するスクショのログに書き込み
	my $new_line = shift;
	my @lines = ();
	open my $fh, "+< $logdir/screen_shot.cgi" or &error("$logdir/screen_shot.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		push @lines, $line;
		last if @lines >= $max_log-1;
	}
	unshift @lines, "$new_line\n";
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}

#================================================
# ＠ぎるど
#================================================
sub girudo {
	$m{lib} = 'guild';
	$mes = "＠$m{guild}に移動します";
	&auto_reload;
	&leave_member($m)
}

#================================================
# ＠はなす
#================================================
sub hanasu {
	unless (@words) {
		$mes = "返事がない、ただのしかばねのようだ…" ;
		return;
	}
	$npc_com = $words[int(rand(@words))];
}
#================================================
# ＠ささやき
#================================================
sub sasayaki {
	$to_name = shift;
	if ($to_name) {
		my $yid = unpack 'H*', $to_name;
		unless (-f "$userdir/$yid/user.cgi") {
			$mes = "$to_nameというプレイヤーが存在しません";
			return;
		}
	}
	$is_npc_action = 0;
	$act_time = 0;
}
#================================================
# ＠いどう
#================================================
sub idou {
	my $target = shift;
	my $p = '';
	my $count = 0;
	for my $i (0 .. $#places) {
		if ($places[$i][0] eq $target) {
			if ($m{lib} eq $places[$i][1]) {
				$mes = "ここが$places[$i][0]です";
			}
			else {
				$m{lib} = $places[$i][1];
				$mes = "$places[$i][0]に移動します";
				&auto_reload;
				&leave_member($m);
			}
			return;
		}
		$p .= qq|<span onclick="text_set('＠いどう>$places[$i][0] ')">$places[$i][0] </span>/ |;
		$p .= qq|<br />| if ++$count % 7 == 0;
	}
	$mes = qq|どこに移動しますか？<br />$p|;
	$act_time = 0;
}
#================================================
# ＠まち
#================================================
sub machi {
	my $target = shift;
	my $p = '';
	@towns = reverse @towns; # 高級物件から表示
	for my $i (0 .. $#towns) {
		if ($towns[$i][0] eq $target) {
			if ($m{lib} eq $towns[$i][1]) {
				$mes = "ここが$towns[$i][0]です";
			}
			else {
				$m{lib} = $towns[$i][1];
				$mes = "$towns[$i][0]に移動します";
				&auto_reload;
				&leave_member($m);
			}
			return;
		}
		$p .= qq|<span onclick="text_set('＠まち>$towns[$i][0] ')">$towns[$i][0] </span>/ |;
	}
	$mes = qq|どの町に行きますか？<br />$p|;
	$act_time = 0;
}
#================================================
# ＠しらべる
#================================================
sub shiraberu {
	my $target = shift;
	
	if ($target eq $npc_name) {
		&shiraberu_npc;
		return;
	}
	
	my $yid = unpack 'H*', $target;
	
	if (-f "$userdir/$yid/user.cgi") { # 相手のステータス
		my %p = &get_you_datas($yid, 1);
		
		if ($time > $p{login_time} + $login_time * 60) {
			$mes .= "$targetはログインしていません";
		}
		elsif ($p{lib} eq 'home') {
			$mes .= "$targetは$p{home}の家にいます";
		}
		elsif ($p{lib} =~ /^vs_/) {
			$mes .= "$targetはクエスト中です";
		}
		else {
			for my $i (0..$#places) {
				if ($p{lib} eq $places[$i][1]) {
					$mes .= "$targetは$places[$i][0]にいます";
					last;
				}
			}
		}
		
		$mes .= " 最終更新時間 $p{ldate}<br />";
		if ($p{guild}) {
			my $gid = unpack 'H*', $p{guild};
			$mes .= qq|<img src="$guilddir/$gid/mark.gif" alt="ギルドマーク" />| if -f "$guilddir/$gid/mark.gif";
			$mes .= qq|$p{guild} |;
		}
		$mes .= qq|<img src="$icondir/$p{icon}" />$p{name} $e2j{$p{sex}} $e2j{lv}$p{lv} $jobs[$p{job}][1](Sp $p{sp})/$jobs[$p{old_job}][1](Sp $p{old_sp})<br />|;
		$mes .= qq|$e2j{tired}：$p{tired}％ $e2j{mhp}：$p{mhp} $e2j{mmp}：$p{mmp} $e2j{at}：$p{at} $e2j{df}：$p{df} $e2j{ag}：$p{ag}<br />|;
		$mes .= qq| 武器：$weas[$p{wea}][1]| if $p{wea};
		$mes .= qq| 防具：$arms[$p{arm}][1]| if $p{arm};
		$mes .= qq| 道具：$ites[$p{ite}][1]| if $p{ite};
		$mes .= qq|<br />☆『$p{mes}』| if $p{mes};
	}
	else { # 自分のステータス
		if ($m{guild}) {
			my $gid = unpack 'H*', $m{guild};
			$mes .= qq|<img src="$guilddir/$gid/mark.gif" alt="ギルドマーク" />| if -f "$guilddir/$gid/mark.gif";
			$mes .= qq|$m{guild} |;
		}
		my $next_lv = $m{lv} * $m{lv} * 10 - $m{exp};
		$mes .= qq|<img src="$icondir/$m{icon}" />$m $e2j{$m{sex}} / $e2j{lv}$m{lv} 次のレベルあと${next_lv}Exp / $e2j{tired}$m{tired}％ / 転職$m{job_lv}回<br />$jobs[$m{job}][1](Sp $m{sp})/$jobs[$m{old_job}][1](Sp $m{old_sp}) / $m{money}Ｇ / $m{coin}コイン / 小さなメダル$m{medal}枚 <br />|;
		$mes .= qq|$e2j{tired}：$m{tired}％ $e2j{mhp}：$m{mhp} $e2j{mmp}：$m{mmp} $e2j{at}：$m{at} $e2j{df}：$m{df} $e2j{ag}：$m{ag}<br />|;
		$mes .= qq| 武器：$weas[$m{wea}][1]| if $m{wea};
		$mes .= qq| 防具：$arms[$m{arm}][1]| if $m{arm};
		$mes .= qq| 道具：$ites[$m{ite}][1]| if $m{ite};
	}
}
sub shiraberu_npc { $mes = "しかし何も見つからなかった…"; }
#================================================
# ＠ほーむ
#================================================
sub homu {
	my $target = shift;
	my $yid = unpack 'H*', $target;
	$m{lib} = 'home';
	
	if (-f "$userdir/$yid/home.cgi") {
		$m{home} = $target;
	}
	else {
		$m{home} = $m;
	}
	$mes = "自分の家に帰ります";
	&auto_reload;
	&leave_member($m);
}

#================================================
# 場面切り替えその１
# メッセージを表示して手動で更新ボタン
#================================================
sub reload { # Manual Reaload
	my $message = shift;
	$m{wt}  = $time + $act_time;
	
	print <<"EOM";
<div class="strong">$message</div>
<form method="$method" action="$script">
	<input type="hidden" name="id" value="$id" />
	<input type="hidden" name="pass" value="$pass" />
	<input type="submit" value="[> Next" class="button_s" />
</form>
EOM
}
#================================================
# 場面切り替えその２
# JavaScriptによる強制リロードでページを動的に変える
#================================================
sub auto_reload { # Auto Reload
	$m{wt}  = $time + $act_time;
	print <<"EOM";
<script type="text/javascript"><!--
location.href="$script?id=$id&pass=$pass&is_auto=1&reload_time=$in{reload_time}";
// --></script>
<noscript>
	<form method="$method" action="$script">
		<input type="hidden" name="id" value="$id" />
		<input type="hidden" name="pass" value="$pass" />
		<input type="submit" value="[> Next" class="button_s" />
	</form>
</noscript>
EOM
}

#=================================================
# メンバー取得
#=================================================
sub read_member {
	%ms = ();
	my @lines   = ();
	my %sames   = ();
	my $is_find = 0;
	@members = ();
	open my $fh, "+< ${this_file}_member.cgi" or &error("${this_file}_member.cgiファイルが開けません"); 
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($ltime, $is_npc, $name, $laddr, $icon, $color) = split /<>/, $line;
		if (!$is_npc) {
			next if $time - $limit_member_time > $ltime;
			next if $sames{$name}++; # 同じ人なら次
		}
		
		if ($is_npc) {
			$name =~ /^@/ ?
				push @lines, "$time<>1<>$npc_name<>0<>$icon<>$npc_color<>\n":
				push @lines, "$time<>1<>$name<>0<>$icon<>$npc_color<>\n";
		}
		elsif ($name eq $m) {
			$is_find = 1;
			push @lines, "$time<>0<>$m<>$addr<>$m{icon}<>$m{color}<>\n";
		}
		else {
			push @lines, $line;
		}
		push @members, $name;
		$ms{$name}{icon}  = $icon;
		$ms{$name}{color} = $color;
	}
	unless ($is_find) {
		push @members, $m;
		$ms{$m}{icon}     = $m{icon};
		$ms{$m}{color}    = $m{color};
		push @lines, "$time<>0<>$m<>$addr<>$m{icon}<>$m{color}<>\n";
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}

#=================================================
# 画面一番上に表示(場所の名前、ステータスなど)
#=================================================
sub header_html {
	my $my_at = $m{at} + $weas[$m{wea}][3];
	my $my_df = $m{df} + $arms[$m{arm}][3];
	my $my_ag = $m{ag} - $weas[$m{wea}][4] - $arms[$m{arm}][4];
	$my_ag = 0 if $my_ag < 0;
	print qq|<div class="mes">【$this_title】 $e2j{money} <b>$m{money}</b>G|;
	print qq| / $e2j{at} <b>$my_at</b> / $e2j{df} <b>$my_df</b> / $e2j{ag} <b>$my_ag</b> /|;
	print qq| E：$weas[$m{wea}][1]| if $m{wea};
	print qq| E：$arms[$m{arm}][1]| if $m{arm};
	print qq| E：$ites[$m{ite}][1]| if $m{ite};
	print qq|</div>|;
}
#=================================================
# メンバー表示
#=================================================
sub member_html {
	my $member_html = '';
	$member_html .= qq|<div style="background: url($bgimg) #333 repeat-x left bottom;"><table><tr>|;
	for my $name (@members) {
		$member_html .= qq|<td onclick="text_set('>$name ')" align="center" valign="bottom"><span style="color: $ms{$name}{color}; font-size: 11px; background-color: #333;">$name</span><br /><img src="$icondir/$ms{$name}{icon}" alt="$name" /></td>|;
	}
	$member_html .=  qq|</tr></table></div>|;
	return $member_html;
}
#=================================================
# 画面表示
#=================================================
sub html {
	&header_html;
	print &member_html;
	print qq|<form method="$method" action="$script" name="form" id="form">\n<input type="hidden" name="reload_time" value="$in{reload_time}" />\n|;
	print qq|<input type="hidden" name="id" value="$id" />\n<input type="hidden" name="pass" value="$pass" />|;
	print qq|<input type="text"  name="comment" class="text_box_b" />\n<input type="submit" value="発言" class="button_s" />\n|;
	print qq| <input type="reset" value="ｸﾘｱ" /> |;
	print qq|<select name="reload_time"><option value="0">なし</option>\n|;
	for my $i (1 .. $#reload_times) {
		print $in{reload_time} eq $i ? qq|<option value="$i" selected="selected">$reload_times[$i]秒</option>\n| : qq|<option value="$i">$reload_times[$i]秒</option>\n|;
	}
	print qq|</select>\n|;
	print qq|更新 <span id="nokori_auto_time"></span>秒<script type="text/javascript"><!--\n count_down($reload_times[$in{reload_time}]);\n// --></script>\n| if $in{reload_time} > 0;
	print qq|<br />\n|;

	for my $action (@actions) {
		print $action eq 'br' ? qq|<br />| : qq|<span onclick="text_set('＠$action ')">＠$action</span> 　|;
	}
	print qq|</form>\n|;

	print qq|<font size="1">次の行動</font><div id="gage_back1" style="width: $gage_width"><img src="$htmldir/space.gif" width="0%" class="gage_bar1" /></div><br />\n|;
	print qq|<script type="text/javascript"><!--\n active_gage($nokori, $act_time);\n// --></script></form>\n|;
	print qq|<div class="strong">$mes</div>\n| if $mes;
	print qq|<hr size="1" />\n|;
	
	# ログ出力
	open my $fh, "< $this_file.cgi" or &error("$this_file.cgi ファイルが開けません");
	while (my $line = <$fh>) {
		my($btime,$bdate,$bname,$baddr,$bcolor,$bcomment,$bto_name) = split /<>/, $line;
		if ($bto_name) { # ささやき
			if ($m eq $bto_name || $m eq $bname) {
				print qq|<span class="whisper">$bname： $bcomment <font size="1">($bdate)</font></span><hr size="1" />\n|;
			}
		}
		else {
			print qq|<font color="$bcolor">$bname</font>： $bcomment <font size="1">($bdate)</font><hr size="1" />\n|;
		}
	}
	close $fh;
}

#=================================================
# 発言・アクション
#=================================================
sub action {
	$com .= "\x20";
	$com =~ /＠(.+?)(?:(?:\x20|　)?&gt;(.+?)(?:\x20|　)|\x20|　)/;
	my $action = $1;
	my $target = $2 ? $2 : '';
	return unless defined $actions{$action};
 	if ($nokori > 0) {
		$mes = "まだ行動することはできません";
		return;
	}
	
	&{ $actions{$action} }($target);
	return if $mes;
	
	$m{wt}  = $time + $act_time;
	$nokori = $act_time;
}

#=================================================
# ログ書き込み処理
#=================================================
sub write_comment {
	my @lines = ();
	open my $fh, "+< $this_file.cgi" or &error("$this_file.cgi ファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		push @lines, $line;
		last if @lines >= $max_log-1;
	}
	unshift @lines, "$time<>$date<>$m{name}<>$addr<>$m{color}<>$com<>$to_name<>\n";
	unshift @lines, "$time<>$date<>$npc_name<>NPC<>$npc_color<>$npc_com<>$to_name<>\n" if $npc_com;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}

#================================================
# デコード
#================================================
sub decode {
	local ($k,$v,$buf);

	if ($ENV{REQUEST_METHOD} eq 'POST') {
		&error('投稿量が大きすぎます',1) if $ENV{CONTENT_LENGTH} > 51200;
		read STDIN, $buf, $ENV{CONTENT_LENGTH};
	}
	else {
		&error('投稿量が大きすぎます',1) if length $ENV{QUERY_STRING} > 51200;
		$buf = $ENV{QUERY_STRING};
	}
	
	for my $pair (split /&/, $buf) {
		($k,$v) = split /=/, $pair;
		$v =~ tr/+/ /;
		$v =~ s/%([0-9A-Fa-f][0-9A-Fa-f])/pack 'H2', $1/eg;

		# 記号置換え
		$v =~ s/&/&amp/g;
		$v =~ s/;/&#59;/g;
		$v =~ s/&amp/&amp;/g;
		$v =~ s/,/&#44;/g;
		$v =~ s/</&lt;/g;
		$v =~ s/>/&gt;/g;
		$v =~ s/"/&quot;/g;
		$v =~ tr/\x0D\x0A//d; # 改行削除

		$in{$k} = $v;
		push @delfiles, $v if $k eq 'delete';
	}
	
	# よく使うので簡単な変数に代入
	$com  = $in{comment};
	$id   = $in{id};
	$pass = $in{pass};
	&error("本文が長すぎます(半角$max_comment文字まで)",1) if length $com > $max_comment; # 最大文字数制限
}

#================================================
# アクセスチェック Get $addr $host $agent
#================================================
sub access_check {
	$addr = $ENV{REMOTE_ADDR};
	$host = $ENV{REMOTE_HOST};
	$host = $addr if $host eq '';

	for my $deny (@deny_lists) {
		$deny =~ s/\./\\\./g;
		$deny =~ s/\*/\.\*/g;
		&error($deny_message, 1) if $addr =~ /^$deny$/i;
		&error($deny_message, 1) if $host =~ /^$deny$/i;
	}
}

#================================================
# 時間取得 Get $time $date
#================================================
sub get_date {
	$time = time();
	my($min,$hour,$mday,$mon,$year) = (localtime($time))[1..4];
	$date = sprintf("%d/%d %02d:%02d", $mon+1,$mday,$hour,$min);
}

#================================================
# header
#================================================
sub header {
	print "Content-type: text/html; charset=Shift_JIS\n";
	if ($gzip ne '' && $ENV{HTTP_ACCEPT_ENCODING} =~ /gzip/){  
		if ($ENV{HTTP_ACCEPT_ENCODING} =~ /x-gzip/) {
			print "Content-encoding: x-gzip\n\n";
		}
		else{
			print "Content-encoding: gzip\n\n";
		}
		open STDOUT, "| $gzip -1 -c";
	}
	else {
		print "\n";
	}
	
	my $meta_refresh = $in{reload_time} ? qq|<meta http-equiv="refresh" content="$reload_times[$in{reload_time}];URL=$script?id=$id&pass=$pass&is_auto=1&reload_time=$in{reload_time}" />| : '';

	print <<"EOM";
<html>
<head>
<meta http-equiv="Cache-Control" content="no-cache" />
<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS" />
$meta_refresh
<link rel="shortcut icon" href="$htmldir/favicon.ico" />
<link rel="stylesheet" type="text/css" href="$htmldir/party.css" />
<title>$title</title>
<script type="text/javascript" src="$htmldir/party.js"></script>
</head>
<body onLoad="text_focus()">
EOM
}
#================================================
# footer
#================================================
sub footer {
	print qq|<div id="footer">|;
	print qq|+ ＠パーティーII Ver$VERSION <a href="http://cgi-sweets.com/" target="_blank">CGI-Sweets</a> <a href="http://amaraku.net/" target="_blank">Ama楽.net</a>|; # 著作表示:削除・非表示 禁止!!
	print qq|$copyright +</div></body></html>|;
}

#==========================================================
# エラー画面表示
#==========================================================
sub error {
	my($error_mes, $is_need_header) = @_;
	
	&header if $is_need_header;
	print qq|<br /><div class="mes">$error_mes<br /><br /></div>\n|;
	print qq|<form action="$script_index"><p><input type="submit" value="ＴＯＰ" /></p></form>|;
	&footer;
	exit;
}

#================================================
# アイテムを送る
#================================================
sub send_item {
	my($send_name, $kind, $no, $send_from) = @_;
	my $send_id = unpack 'H*', $send_name;
	
	if (-f "$userdir/$send_id/depot.cgi") {
		open my $fh, ">> $userdir/$send_id/depot.cgi";
		print $fh "$kind<>$no<>\n";
		close $fh;
		
		if ($send_from) {
			my $item_name = $kind eq '1' ? $weas[$no][1]
						  : $kind eq '2' ? $arms[$no][1]
						  :				   $ites[$no][1]
						  ;
			open my $fh2, ">> $userdir/$send_id/send_item_mes.cgi";
			print $fh2 "預かり所に$send_fromから$item_nameが届いています\n";
			close $fh2; 
		}
	}
}

#================================================
# 他プレイヤーにお金を送金
#================================================
sub send_money {
	my($send_name, $money, $message) = @_;
	my $send_id = unpack 'H*', $send_name;
	$message ||= "$send_nameからの送金";

	if (-f "$userdir/$send_id/money.cgi") {
		open my $fh, ">> $userdir/$send_id/money.cgi";
		print $fh "$money<>$message<>\n";
		close $fh;

		open my $fh2, "> $userdir/$send_id/money_flag.cgi";
		close $fh2; 
	}
}

#================================================
# 相手ﾃﾞｰﾀ変更
#================================================
# 使い方: &regist_you_data('相手の名前', '変更したい変数', '値');
sub regist_you_data {
	my($name, $k, $v) = @_;
	return if $name eq '' || $k eq '';
	
	if ($m eq $name) {
		$m{$k} = $v;
	}
	else {
		my $y_id = unpack 'H*', $name;
		return unless -f "$userdir/$y_id/user.cgi";
		
		open my $fh, "+< $userdir/$y_id/user.cgi" or &error("$userdir/$y_id/user.cgiファイルが開けません");
		eval { flock $fh, 2; };
		my $line = <$fh>;
		if ($line) {
			$line =~ s/<>($k;).*?<>/<>$1$v<>/;
			seek  $fh, 0, 0;
			truncate $fh, 0;
			print $fh $line;
		}
		close $fh;
	}
}

#================================================
# 相手ﾃﾞｰﾀをGet 戻り値はハッシュ
#================================================
# 使い方: &get_you_datas('相手の名前');
sub get_you_datas {
	my($name, $is_unpack) = @_;
	
	my $y_id = '';
	if ($is_unpack) {
		return %m if $id eq $name;
		$y_id = $name;
	}
	else {
		return %m if $m eq $name;
		$y_id = unpack 'H*', $name;
	}
	
	open my $fh, "< $userdir/$y_id/user.cgi" or &error("$nameそのようなプレイヤーは存在しません");
	my $line = <$fh>;
	close $fh;
	
	%you_datas = ();
	for my $hash (split /<>/, $line) {
		my($k, $v) = split /;/, $hash;
		$you_datas{$k} = $v;
	}

	return %you_datas;
}

#=================================================
# ディレクトリごと削除
#=================================================
sub delete_directory {
	my $dir_name = shift;
	
	opendir my $dh, "$dir_name" or &error("$dir_nameディレクトリが開けません");
	while (my $file_name = readdir $dh) {
		next if $file_name =~ /^\./;
		unlink "$dir_name/$file_name" or &error("$dir_name/$file_nameファイルが削除できません");
	}
	closedir $dh;
	rmdir "$dir_name";
}

#=================================================
# ＠ろぐあうと
#=================================================
sub roguauto {
	$mes = "ログアウトしますか？";
	&leave_member($m);

	print <<"EOM";
<script type="text/javascript"><!--
	location.href="$script_index";
// --></script>
<noscript>
	<div>ログアウトしますか？</div>
	<form method="$method" action="$script_index">
		<input type="submit" value="＠ログアウト" class="button_s" />
	</form>
</noscript>
EOM
}

#=================================================
# メンバーから除く
#=================================================
sub leave_member {
	my $y = shift;
	
	my @lines = ();
	open my $fh, "+< ${this_file}_member.cgi" or &error("${this_file}_member.cgiファイルがが開けません"); 
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($ltime, $is_npc, $name, $laddr, $icon, $color, $guild) = split /<>/, $line;
		next if !$is_npc && $name eq $y;
		push @lines, $line;
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}

#================================================
# 登録者数
#================================================
sub get_entry_count {
	open my $fh, "< $logdir/entry.cgi" or &error("$logdir/entry.cgiファイルが読み込めません");
	my $line = <$fh>;
	close $fh;
	my($entry_count) = (split /<>/, $line)[0];
	return $entry_count;
}

#================================================
# 登録者数マイナス
#================================================
sub minus_entry_count {
	my $count = shift || 1;

	open my $fh, "+< $logdir/entry.cgi" or &error("$logdir/entry.cgiファイルが開けません");
	eval { flock $fh, 2; };
	my $line = <$fh>;
	my($entry_count, $last_addr) = split /<>/, $line;
	$entry_count -= $count;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh "$entry_count<>$last_addr<>";
	close $fh;
}

#================================================
# ブラックリストに追加
#================================================
sub add_black_list {
	my $baddr = shift;
	open my $fh, ">> $logdir/black_list.cgi" or &error("$logdir/black_list.cgiファイルが開けません");
	print $fh "$baddr,";
	close $fh;
}

#================================================
# 追放申請追加
#================================================
sub add_exile {
	my($bad_name, $because) = @_;
	
	my $is_find = 0;
	my @lines = ();
	open my $fh, "+< $logdir/violator.cgi" or &error("$logdir/violator.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($name, $violator, $message, $yess, $noss) = split /<>/, $line;
		
		# 追放申請が出ていてさらに違反行為をした場合＋１票
		if ($bad_name eq $violator) {
			$line = "$name<>$violator<>$message<>$yess,@追放騎士<>$noss<>\n";
			$is_find = 1;
		}
		push @lines, $line;
	}
	push @lines, "@追放騎士<>$bad_name<>$because<>@追放騎士<><>\n" unless $is_find;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}

#================================================
# 手紙を送る
#================================================
sub send_letter {
	my($send_name, $send_message) = @_;

	my $yid = unpack 'H*', $send_name;
	unless (-f "$userdir/$yid/letter.cgi") {
		$mes = "$send_nameというプレイヤーが存在しません";
		return;
	}

	my $new_line = "$time<>$date<>$m<>$addr<>$m{color}<>$send_message<><>\n";
	my @lines = ();
	open my $fh, "+< $userdir/$yid/letter.cgi" or &error("$userdir/$yid/letter.cgiファイルが読み込めません");
	eval { flock $fh, 2; };
	my $head_line = <$fh>;
	my($ltime, $name) = (split /<>/, $head_line)[0,2];
	if ($name eq $m && $ltime + $bad_time > $time) {
		$mes = "連続で手紙を送ることはできません。しばらくしてから送ってください";
		return;
	}
	push @lines, $head_line;
	while (my $line = <$fh>) {
		push @lines, $line;
		last if @lines+1 >= $max_log;
	}
	unshift @lines, $new_line;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	open my $fh3, "> $userdir/$yid/letter_flag.cgi";
	close $fh3; 
}

#================================================
# ギルドデータを編集
#================================================
sub regist_guild_data {
	my($k, $v, $guild_name) = @_;
	
	$guild_name ||= $m{guild};
	return unless $guild_name;
	my $gid = unpack 'H*', $guild_name;
	unless (-f "$guilddir/$gid/data.cgi") {
		$mes = "$guild_nameギルドが存在しません";
		return;
	}

	open my $fh, "+< $guilddir/$gid/data.cgi" or &error("$guilddir/$gid/data.cgiファイルが開けません");
	eval { flock $fh, 2; };
	my $line = <$fh>;
	my($gname,$gmaster,$gcolor,$gbgimg,$gmes,$gpoint) = split /<>/, $line;
	if    ($k eq 'master') { $gmaster = $v }
	elsif ($k eq 'color')  { $gcolor  = $v }
	elsif ($k eq 'bgimg')  { $gbgimg  = $v }
	elsif ($k eq 'mes')    { $gmes    = $v }
	elsif ($k eq 'point')  { $gpoint += $v }
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh "$gname<>$gmaster<>$gcolor<>$gbgimg<>$gmes<>$gpoint<>";
	close $fh;
}


#=================================================
# ギルドメンバーから削除
#=================================================
sub delete_guild_member {
	my($gname, $delete_name) = @_;
	
	my $gid = unpack 'H*', $gname;
	return unless -f "$guilddir/$gid/member.cgi";
	
	my @lines = ();
	open my $fh, "< $guilddir/$gid/member.cgi" or &error("$guilddir/$gid/member.cgiファイルが読み込めません");
	while (my $line = <$fh>) {
		push @lines, $line;
	}
	close $fh;
	
	# 最後の１人の場合はギルド削除
	if (@lines <= 1) {
		&delete_directory("$guilddir/$gid");
		&write_news(qq|<span class="die">$gname ギルドが解散しました</span>|);
	}
	else {
		my($guild_master) = (split /<>/, $lines[0])[0];
		
		# ギルマスが脱退
		if ($delete_name eq $guild_master) {
			shift @lines;
			
			# ギルマス候補を探す(役職に[ギルマス]が含まれている人。いなければ２番目にメンバーになった人)
			my $is_find = 0;
			for my $i (0 .. $#lines) {
				my($name, $position) = split /<>/, $lines[$i];
				if ($position =~ /ギルマス/) {
					$is_find = 1;
					splice(@lines, $i, 1);
					unshift @lines, "$name<>ギルマス<>\n";
					&regist_guild_data('master', $name, $gname);
					last;
				}
			}
			
			# ２番目の人
			unless ($is_find) {
				my($name, $position) = split /<>/, $lines[0];
				$lines[0] = "$name<>ギルマス<>\n";
				&regist_guild_data('master', $name, $gname);
			}
		}
		else {
			for my $i (0 .. $#lines) {
				my($name, $position) = split /<>/, $lines[$i];
				if ($delete_name eq $name) {
					splice(@lines, $i, 1);
					last;
				}
			}
		}
		open my $fh2, "> $guilddir/$gid/member.cgi";
		print $fh2 @lines;
		close $fh2;
	}
}

#================================================
# 自分のギルドデータ取得
#================================================
sub read_guild_data {
	unless ($m{guild}) {
		$m{lib}='';
		&write_user;
		&error("ギルドに参加していません");
	}
	
	my $g_id = unpack 'H*', $m{guild};
	unless (-f "$guilddir/$g_id/data.cgi") {
		my $name  = $m{guild};
		$m{guild} = $m{lib} = '';
		&write_user;
		&error("$nameは解散してしまったようです");
	}

	open my $fh, "< $guilddir/$g_id/data.cgi" or &error("$guilddir/$g_id/data.cgiファイルが開けません");
	my $line = <$fh>;
	close $fh;
	
	return $g_id, split /<>/, $line;
}

#================================================
# コピー。使い方：&copy('コピー元のPath', 'コピー先のPath');
#================================================
sub copy {
	my($from, $to) = @_;
	
	open my $in, "< $from" or &error("コピー元$fromファイルが読み込めません");
	binmode $in;
	my @datas = <$in>;
	close $in;

	open my $out, "> $to" or &error("$fromから$toにコピーするのを失敗しました");
	binmode $out;
	print $out @datas;
	close $out;
}

#================================================
# 軌跡の書き込み※プレイヤー名がない場合は自分自身。
# 使い方：&write_memory('メッセージ', 'プレイヤー名');
#================================================
sub write_memory {
	my($message, $memory_name) = @_;
	my $yid;
	my %p;

	if ($memory_name) {
		$yid = unpack 'H*', $memory_name;
		return unless -f "$userdir/$yid/memory.cgi";
		%p = &get_you_datas($yid, 1);
	}
	else {
		$yid = $id;
		%p = %m;
	}
	
	my @lines = ();
	open my $fh, "+< $userdir/$yid/memory.cgi" or &error("$userdir/$yid/memory.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		push @lines, $line;
		last if @lines >= $max_log-1;
	}
	my $name = $p{guild} ? "$p{name}＠$p{guild}" : "$p{name}";
	unshift @lines, qq|<span color="$p{color}"><img src="$icondir/$p{icon}" />$name： $e2j{lv}$p{lv} $jobs[$p{job}][1]($p{sp}) $message <font size="1">($date)</font></span>\n|;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}

#=================================================
# 現在の預けている個数
#=================================================
sub get_depot_c {
	# 最大預かり所での保存数
	my $max_depot = $m{job_lv} >= 20 ? 100 : $m{job_lv} * 5 + 5;

	my $count = 0;
	open my $fh, "< $userdir/$id/depot.cgi" or &error("$userdir/$id/depot.cgiファイルが読み込めません");
	++$count while <$fh>;
	close $fh;
	$m{is_full} = $count >= $max_depot ? 1 : 0;	
	return $count, $max_depot;
}
#================================================
# 預けているモンスターが満杯かのチェック(デフォルト：50)
# 増減させる場合は『return $count >= 50 ? 1 : 0;』の30の部分を変更
#================================================
sub is_full_monster {
	my $yid = shift;
	my $count = 0;
	open my $fh, "< $userdir/$yid/monster.cgi" or &error("$userdir/$yid/monster.cgiファイルが読み込めません");
	++$count while <$fh>;
	close $fh;
	return $count >= 50 ? 1 : 0;
}

#================================================
# 伝説のプレイヤー書き込み
#================================================
sub write_legend {
	my $file = shift;
	
	my @lines = ();
	open my $fh, "+< $logdir/$file.cgi" or &error("$logdir/$file.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		push @lines, $line;
		last if @lines >= $max_log-1;
	}
	unshift @lines, "$m{name}<>$m{guild}<>$m{color}<>$m{icon}<>$m{mes}<>$date<>\n";;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}

#================================================
# 闘技場、ギルド戦のゴールド、ギルドポイントの増減
#================================================
sub add_bet {
	my($quest_id, $add_bet, $is_casino) = @_;

	open my $fh, "+< $questdir/$quest_id/bet.cgi" or &error("$questdir/$quest_id/bet.cgiファイルが開けません");
	eval { flock $fh, 2; };
	my $bet = <$fh>;
	$bet =~ tr/\x0D\x0A//d;
	$bet += $add_bet;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh $bet;
	close $fh;
}

#================================================
# 最近の大きな出来事
#================================================
sub write_news {
	my $message = shift;

	my @lines = ();
	open my $fh, "+< $logdir/news.cgi" or &error("$logdir/news.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		push @lines, $line;
		last if @lines >= $max_log-1;
	}
	unshift @lines, qq|$message <font size="1">($date)</font>\n|;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}


#=========================================================
# ログインメンバー取得
#=========================================================
sub get_login_member {
	my @lines = ();
	my %sames = ();
	my $list  = '';
	open my $fh, "+< $logdir/login.cgi" or &error("$logdir/login.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($ltime, $name, $color, $guild, $message, $icon) = split /<>/, $line;
		next if $time > $ltime + $login_time * 60;
		next if ++$sames{$name} > 1;
		
		my $yid = unpack 'H*', $name;
		$list .= qq|<div style="color: $color;"><a href="player.cgi?id=$yid" style="color: $color; text-decoration: none;" target="_blank"><img src="$icondir/$icon" />$name</a>|;
		$list .= qq|＠$guild| if $guild;
		$list .= qq|＠$message</div>\n|;
		
		++$count;
		push @lines, $line;
	}
	seek $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	my $login_count = @lines;
	return ($list, $login_count);
}
sub get_header_data { return }

#=========================================================
# 手助けクエストで依頼されているアイテムNoの取得 weapon.cgi, armor.cgi, item.cgi, secret.cgi
#=========================================================
sub get_helper_item {
	my $gkind = shift;

	my $gno = ',';
	open my $fh, "< $logdir/helper_quest.cgi" or &error("$logdir/helper_quest.cgiファイルが開けません");
	while (my $line = <$fh>) {
		my($limit_time,$limit_date,$name,$is_guild,$pay,$kind,$no,$need_c) = split /<>/, $line;
		$gno .= "$no," if $gkind eq $kind;
	}
	close $fh;
	return $gno;
}

sub get_header_data { return }


1; # 削除不可
