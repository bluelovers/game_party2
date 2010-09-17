#!/usr/local/bin/perl
require 'config.cgi';
#================================================
# プレイヤー一覧HTML作成 + 期限切れプレイヤー削除
# & Cookieセット Created by Merino
#================================================
# プレイヤー一覧HTML更新周期(日) 1日～
my $update_cycle_day = 1;

# Cookie保存期間(日)
my $limit_cookie_day = 30;

# メッセージの最大文字数(半角)
my $max_login_message = 60;

$htmldir = './html';


#================================================
&decode;
&error("メッセージに不正な文字( ,;\"\'&<> )が含まれています",1)	if $in{login_message} =~ /[,;\"\'&<>]/;
&error("メッセージに不正な空白が含まれています",1)					if $in{login_message} =~ /　|\s/;
&error("メッセージが長すぎます(半角$max_login_message文字まで)",1)	if length $in{login_message} > $max_login_message; # 最大文字数制限
$in{is_cookie} ? &set_cookie($in{login_name},$in{pass},$in{login_message}) : &del_cookie;
# 更新連打していた場合のペナルティ
&read_user(1);
if (-s "$userdir/$id/reload.cgi") {
	open my $fh, "+< $userdir/$id/reload.cgi" or &error("$userdir/$id/reload.cgiファイルが開けません", 1);
	my $line = <$fh>;
	my @lines = split /<>/, $line;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	close $fh;
	
	if    (@lines > 30) {
#		&add_black_list($addr);
#		&delete_guild_member($m{guild}, $m{name}) if $m{guild};
#		&delete_directory("$userdir/$id");
#		&error(qq|<span class="die">前回のプレイ時に更新連打が30回を超えていたので、削除となります</span>|, 1);
		$sleep_time = 7 * 24 * 60;
		$m{sleep} = $m{sleep} > 0 ? $m{sleep} + $sleep_time * 60 : $sleep_time * 60;
		&write_user;
		&error(qq|<span class="die">前回のプレイ時に更新連打が30回を超えていたので、$sleep_time分間睡眠状態となります</span>|, 1);
	}
	elsif (@lines > 25) {
#		&add_black_list($addr);
#		&error(qq|<span class="die">前回のプレイ時に更新連打が25回を超えていたので、ブラックリスト追加となり$sleep_time分間睡眠状態となります</span>|, 1);
		$sleep_time = 3 * 24 * 60;
		$m{sleep} = $m{sleep} > 0 ? $m{sleep} + $sleep_time * 60 : $sleep_time * 60;
		&write_user;
		&error(qq|<span class="die">前回のプレイ時に更新連打が25回を超えていたので、$sleep_time分間睡眠状態となります</span>|, 1);
	}
	elsif (@lines > 20) {
		$sleep_time = 24 * 60;
		$m{sleep} = $m{sleep} > 0 ? $m{sleep} + $sleep_time * 60 : $sleep_time * 60;
		&write_user;
		&error(qq|<span class="die">前回のプレイ時に更新連打が20回を超えていたので、$sleep_time分間睡眠状態となります</span>|, 1);
	}
	elsif (@lines > 15) {
		$sleep_time = 6 * 60;
		$m{sleep} = $m{sleep} > 0 ? $m{sleep} + $sleep_time * 60 : $sleep_time * 60;
		&write_user;
		&error(qq|<span class="die">前回のプレイ時に更新連打が15回を超えていたので、$sleep_time分間睡眠状態となります</span>|, 1);
	}
	elsif (@lines > 10) {
		$sleep_time = 60;
		$m{sleep} = $m{sleep} > 0 ? $m{sleep} + $sleep_time * 60 : $sleep_time * 60;
		&write_user;
		&error(qq|<span class="die">前回のプレイ時に更新連打が10回を超えていたので、$sleep_time分間睡眠状態となります</span>|, 1);
	}
}

require 'party.cgi';
$m{mes} = $in{login_message};
&write_user;
&write_top_message;

if    (-M "$htmldir/player_list.html" >= $update_cycle_day) {
	&write_player_list_html;
}
elsif (-M "$logdir/guild_list.cgi"  >= $update_cycle_day) {
	&write_guild_list_html;
}
exit;

# ------------------

sub write_top_message {
	my @lines = ();
	open my $fh, "+< $logdir/login.cgi" or &error("$logdir/login.cgiファイルが開けません");
	eval { flock $fh, 2; };
	push @lines, $_ while <$fh>;
	unshift @lines, "$time<>$m{name}<>$m{color}<>$m{guild}<>$m{mes}<>$m{icon}<>\n";
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}


#=================================================
# クッキーセット
#=================================================
sub set_cookie {
	my @cooks = @_;

	local($csec,$cmin,$chour,$cmday,$cmon,$cyear,$cwday) = gmtime(time + $limit_cookie_day * 24 * 60 * 60); # 60日 24時間 * 60分 * 60秒
	local @mons = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec');
	local @week = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat');

	local $expirese_time = sprintf("%s, %02d-%s-%04d %02d:%02d:%02d GMT",
			$week[$cwday],$cmday,$mons[$cmon],$cyear+1900,$chour,$cmin,$csec);

	for my $c (@cooks) {
		$c =~ s/(\W)/sprintf("%%%02X", unpack "C", $1)/eg;
		$cook .= "$c<>";
	}

	print "Set-Cookie: party=$cook; expires=$expirese_time\n";
}
# ------------------
# クッキー削除
sub del_cookie {
	my $expires_time = 'Thu, 01-Jan-1970 00:00:00 GMT';
	print "Set-Cookie: party=dummy; expires=$expires_time\n";
}

#=================================================
# プレイヤー一覧作成
#=================================================
sub write_player_list_html {
	my $count = 0;
	my $html = qq|<table class="tablesorter"><thead><tr>|;
	for my $k (qw/名前 性別 ギルド Lv 転職 職業 前職業 ＨＰ ＭＰ 攻撃 守備 素早 ｺﾞｰﾙﾄﾞ ｺｲﾝ ﾒﾀﾞﾙ 武器 防具 道具 ﾓﾝｽﾀｰ撃退 ﾌﾟﾚｲﾔｰ撃退 封印 解放 ｶｼﾞﾉ 最終ログイン/) {
		$html .= qq|<th>$k</th>|;
	}
	$html .= qq|</tr></thead><tbody>\n|;
	
	my @datas = ();
	opendir my $dh, $userdir or &error("$userdirディレクトリが開けません");
	while (my $dir_name = readdir $dh) {
		next if $dir_name =~ /\./;
		my %p = &get_you_datas($dir_name, 1);
		
		# 自動削除期間
		if ( ($time > $p{ltime} + $auto_delete_day * 3600 * 24)
			|| ($p{job_lv} <= 0 && $p{lv} <= 2 && $time > $p{ltime} + 7 * 3600 * 24) ) { # 転職回数０でレベル2以下は７日で削除
				&delete_guild_member($p{guild}, $p{name}) if $p{guild};
				&delete_directory("$userdir/$dir_name");
				next;
		}
		++$count;
		push @datas, [$p{name},$p{guild},$p{color},$p{icon},$p{mes},$p{kill_p},$p{kill_m},$p{cas_c},$p{mao_c},$p{hero_c}];
		$html .= qq|<tr><td style="color: $p{color};"><img src="../$icondir/$p{icon}" /><a href="../player.cgi?id=$dir_name">$p{name}</a></td><td>$e2j{$p{sex}}</td><td>$p{guild}</td><td align="right">$p{lv}</td><td align="right">$p{job_lv}</td><td>$jobs[$p{job}][1]($p{sp})</td><td>$jobs[$p{old_job}][1]($p{old_sp})</td><td align="right">$p{mhp}</td><td align="right">$p{mmp}</td><td align="right">$p{at}</td><td align="right">$p{df}</td><td align="right">$p{ag}</td><td align="right">$p{money}</td><td align="right">$p{coin}</td><td align="right">$p{medal}</td><td>$weas[$p{wea}][1]</td><td>$arms[$p{arm}][1]</td><td>$ites[$p{ite}][1]</td><td align="right">$p{kill_m}</td><td align="right">$p{kill_p}</td><td align="right">$p{hero_c}</td><td align="right">$p{mao_c}</td><td align="right">$p{cas_c}</td><td>$p{ldate}</td></tr>\n|; 
	}
	closedir $dh;
	
	$html .= qq|\n</tbody></table>\n|;
	
	open my $fh, "> $htmldir/player_list.html" or &error("$htmldir/player_list.htmlファイルが開けません");
	print $fh &html_player_header;
	print $fh $html;
	print $fh &html_player_footer;
	close $fh;

	# 登録人数補正
	open my $fh2, "> $logdir/entry.cgi" or &error("$logdir/entry.cgiファイルが読み込めません");
	print $fh2 "$count<><>";
	close $fh2;
	
	&write_ranking(@datas);
}
#=================================================
# 王者・英雄のデータ作成
#=================================================
sub write_ranking {
	my @datas = @_;
	my @kills_ps = sort { $b->[5] <=> $a->[5] } @datas;
	my @kills_ms = sort { $b->[6] <=> $a->[6] } @datas;
	my @cas_cs   = sort { $b->[7] <=> $a->[7] } @datas;
	my @mao_cs   = sort { $b->[8] <=> $a->[8] } @datas;
	my @hero_cs  = sort { $b->[9] <=> $a->[9] } @datas;
	
	# 王者リスト
	my %sames = ();
	my $count = 0;
	my $line  = '';
	for my $ref (@kills_ps) {
		++$sames{ $ref->[0] };
		$line .= "$ref->[0]<>$ref->[1]<>$ref->[2]<>$ref->[3]<>$ref->[4]<>$ref->[5]<>\n";
		last if ++$count >= 10;
	}
	open my $fh, "> $logdir/kill_p.cgi" or &error("$logdir/kill_p.cgiファイルが開けません");
	print $fh $line;
	close $fh;
	
	# 英雄リスト
	$count = 0;
	$line  = '';
	for my $ref (@kills_ms) {
		next if $sames{ $ref->[0] }; # 王者ランキング者は排除
		$line .= "$ref->[0]<>$ref->[1]<>$ref->[2]<>$ref->[3]<>$ref->[4]<>$ref->[6]<>\n";
		last if ++$count >= 10;
	}
	open my $fh2, "> $logdir/kill_m.cgi" or &error("$logdir/kill_m.cgiファイルが開けません");
	print $fh2 $line;
	close $fh2;

	# 魔王リスト
	%sames = ();
	$count = 0;
	$line  = '';
	for my $ref (@mao_cs) {
		++$sames{ $ref->[0] };
		$line .= "$ref->[0]<>$ref->[1]<>$ref->[2]<>$ref->[3]<>$ref->[4]<>$ref->[8]<>\n";
		last if ++$count >= 10;
	}
	open my $fh3, "> $logdir/mao_c.cgi" or &error("$logdir/mao_c.cgiファイルが開けません");
	print $fh3 $line;
	close $fh3;

	# 勇者リスト
	$count = 0;
	$line  = '';
	for my $ref (@hero_cs) {
		next if $sames{ $ref->[0] }; # 魔王ランキング者は排除
		$line .= "$ref->[0]<>$ref->[1]<>$ref->[2]<>$ref->[3]<>$ref->[4]<>$ref->[9]<>\n";
		last if ++$count >= 10;
	}
	open my $fh4, "> $logdir/hero_c.cgi" or &error("$logdir/hero_c.cgiファイルが開けません");
	print $fh4 $line;
	close $fh4;

	# カジノ勝者リスト
	$count = 0;
	$line  = '';
	for my $ref (@cas_cs) {
		$line .= "$ref->[0]<>$ref->[1]<>$ref->[2]<>$ref->[3]<>$ref->[4]<>$ref->[7]<>\n";
		last if ++$count >= 10;
	}
	open my $fh5, "> $logdir/cas_c.cgi" or &error("$logdir/cas_c.cgiファイルが開けません");
	print $fh5 $line;
	close $fh5;
}


# ------------------
# プレイヤー一覧のヘッダー
sub html_player_header {
	return <<"EOM";
<html>
<head>
<title>$title / プレイヤー一覧</title>
<link rel="stylesheet" type="text/css" href="party.css">
<link rel="stylesheet" type="text/css" href="./jQuery/themes/green/style.css">
<script type="text/javascript" src="./jQuery/jquery-latest.js"></script>
<script type="text/javascript" src="./jQuery/jquery.tablesorter.js"></script>
<script type="text/javascript" src="./jQuery/jquery.tablesorter.pager.js"></script>
<script type="text/javascript">
<!--
\$(document).ready(function() {
	\$(".tablesorter")
		.tablesorter({
			widgets: ['zebra'],
			sortList: [[4,1],[3,1]]
		})
		.tablesorterPager({
			size: 50,
			positionFixed: false,
			container: \$("#pager")
		});
});
-->
</script>
</head>
<body>
<form action="../index.cgi"><input type="submit" value="ＴＯＰへ戻る" /></form>
<p>更新日時 $date</p>
<div id="pager" class="pager">
	<form>
		<img src="./jQuery/addons/pager/icons/first.png" class="first" />
		<img src="./jQuery/addons/pager/icons/prev.png" class="prev" />
		<input type="text" class="pagedisplay" />
		<img src="./jQuery/addons/pager/icons/next.png" class="next" />
		<img src="./jQuery/addons/pager/icons/last.png" class="last" />
		<select class="pagesize">
			<option value="30">30</option>
			<option value="50" selected="selected">50</option>
			<option value="100">100</option>
		</select>
	</form>
</div>
EOM
}

# ------------------
# プレイヤー一覧のフッター
sub html_player_footer {
	return <<"EOM";
<br />
<div align="right" style="font-size:11px">
＠パーティーII Ver$VERSION<br /><a href="http://cgi-sweets.com/" target="_blank">CGI-Sweets</a><br /><a href="http://amaraku.net/" target="_blank">Ama楽.net</a><br />
$copyright
</div>
</body>
</html>
EOM
}


#=================================================
# ギルド勢力作成
#=================================================
sub write_guild_list_html {
	my @guild_list = ();
	opendir my $dh, $guilddir or &error("$guilddirディレクトリが開けません");
	while (my $dir_name = readdir $dh) {
		next if $dir_name =~ /\./;
		
		open my $fh, "+< $guilddir/$dir_name/data.cgi" or &error("$guilddir/$dir_name/data.cgi");
		eval { flock $fh, 2; };
		my $line = <$fh>;
		my($gname,$gmaster,$gcolor,$gbgimg,$gmes,$gpoint) = split /<>/, $line;
		$gpoint = int($gpoint * 0.8); # ギルドポイントを１割減
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh "$gname<>$gmaster<>$gcolor<>$gbgimg<>$gmes<>$gpoint<>";
		close $fh;
		
		my $gmembers = '';
		my $gcount = 0;
		open my $fh2, "< $guilddir/$dir_name/member.cgi" or &error("$guilddir/$dir_name/member.cgiファイルが読み込めません");
		while (my $line2 = <$fh2>) {
			my($name, $position) = split /<>/, $line2;
			next if $position eq '参加申請中';
			$gmembers .= "$name＠$position<>";
			++$gcount;
		}
		close $fh2;
		
		push @guild_list, "$gname<>$gcount<>$gcolor<>$gmes<>$gpoint<>$gmembers\n";
	}
	closedir $dh;
	
	# ギルドポイント、人数が多い順にソート
	@guild_list = map { $_->[0] } sort { $b->[5] <=> $a->[5] || $b->[2] <=> $a->[2] } map { [$_, split /<>/] } @guild_list;
	
	open my $fh3, "> $logdir/guild_list.cgi";
	print $fh3 @guild_list;
	close $fh3;
}


