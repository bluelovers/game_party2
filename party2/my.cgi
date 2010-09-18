#!/usr/local/bin/perl
require './config.cgi';
require './lib/_data.cgi';
#================================================
# ブログパーツ１ Created by Merino
#================================================
print "Content-type: text/html; charset=Shift_JIS\n\n";
&run;
exit;

#================================================
sub run {
	my $yid = $ENV{'QUERY_STRING'};
	$yid =~ s/\W//g;
	
	if (-f "$userdir/$yid/user.cgi") {
		my %m = &get_you_datas($yid, 1);
		my $latest = $time < $m{login_time} + $login_time * 60 ? qq|<b style="color:#FF0;">ログイン中</b>| : qq|最終更新日<br />$m{ldate}|;
		my $mes    = $m{mes} ? $m{mes} : $title;

		my $html =<<"EOM";
<table style="font-size: 11px; background: #000; color: #FFF;"><tr><td valign="top">
	<div style="border: 1px solid #FFF; padding: 2px; margin-bottom: 2px; text-align:center;">
		$m{name}<br />
		$e2j{lv}$m{lv} $e2j{$m{sex}}<br />
		$jobs[$m{job}][1]<br />
		<a href="$game_path/index.cgi?$yid"><img src="$game_path/$icondir/$m{icon}" alt="$m{name}" border="0" /></a><br />
	</div>
	<div style="border: 1px solid #FFF; padding: 2px; margin-bottom: 2px; text-align:left;">
		E: $weas[$m{wea}][1]<br />
		E: $arms[$m{arm}][1]<br />
		E: $ites[$m{ite}][1]<br />
	</div>
	<div style="border: 1px solid #FFF; padding: 2px; margin-bottom: 2px; text-align:center;">
		$latest<br />
	</div>
</td><td valign="top">
	<table style="font-size: 11px; border: 1px solid #FFF; background: #000; color: #FFF;">
		<tr><td align="left">$e2j{at}</td><td align="right">$m{at}</td></tr>
		<tr><td align="left">$e2j{df}</td><td align="right">$m{df}</td></tr>
		<tr><td align="left">$e2j{ag}</td><td align="right">$m{ag}</td></tr>
		<tr><td align="left">ＳＰ</td><td align="right">$m{sp}</td></tr>
		<tr><td align="left">$e2j{mhp}</td><td align="right">$m{mhp}</td></tr>
		<tr><td align="left">$e2j{mmp}</td><td align="right">$m{mmp}</td></tr>
		<tr><td align="left">$e2j{exp}</td><td align="right">$m{exp}</td></tr>
		<tr><td align="left">$e2j{money}</td><td align="right">$m{money}</td></tr>
	</table>
</td></tr><tr><td colspan="2">
<a href="$game_path/index.cgi?$yid" style="color: #6CF;">$mes</a>
</td></tr></table>
EOM

		$html =~ tr/\x0D\x0A//d; # 改行削除
		$html =~ tr/\t//d; # タブ削除
		print qq|document.write('$html');|;
	}
	else {
		print qq|document.write("プレイヤーデータが見つかりません");|;
	}
}
