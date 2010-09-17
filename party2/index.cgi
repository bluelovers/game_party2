#!/usr/local/bin/perl
require 'config.cgi';
require '_side_menu.cgi';
require './lib/_data.cgi';
#================================================
# Index Created by Merino
#================================================
&header;
&run;
&footer;
exit;
#=================================================
sub run {
	my($cookie_name, $cookie_pass, $cookie_mes) = &get_cookie;
	my $checked = $cookie_name ? 'checked="checked"' : '';
	my $entry_count = &get_entry_count;
	my($login_list, $login_count) = &get_login_member;

	my $contents = <<"EOM";
		<table><tr><td valign="top">
			<div class="login_list">$login_list</div>
			<div>ログイン中 $login_count 人</div>
			ﾌﾟﾚｲﾔｰ保存期間 $auto_delete_day日（転職0回 $e2j{lv}2以下の場合は7日）<br />
			定員 $entry_count / $max_entry人
		</td><td valign="top">
EOM
	if ($login_count >= $max_login) {
		$contents .= qq|<table class="table1"><tr><th><p>ただいま、ログイン規制中です</p><p>ログイン人数が$max_login人未満になるまで<br />しばらくお待ちください</p></th></tr></table>|;
	}
	else {
		$contents .= <<"EOM";
		<form method="$method" action="login.cgi">
			<table class="table1" style="margin: 0 0.5em; padding: 1em">
				<tr><th>§プレイヤー§</th></tr><tr><td align="center"><input type="text" name="login_name" class="text_box1" value="$cookie_name" /></td></tr>
				<tr><th>§パスワード§</th></tr><tr><td align="center"><input type="password" name="pass"   class="text_box1" value="$cookie_pass" /></td></tr>
				<tr><th>§メッセージ§</th></tr><tr><td align="center"><input type="text" name="login_message" class="text_box1" value="$cookie_mes" /></td></tr>
				<tr><th><input type="checkbox" name="is_cookie" $checked /> 次回から入力省略</th></tr>
				<tr><th><input type="submit" value="＠ログイン" /></th></tr>
			</table>
		</form>
EOM
	}
	$contents .= qq|</td></tr></table>|;
	
	open my $fh, "< $logdir/screen_shot.cgi" or &error("$logdir/screen_shot.cgiファイルが読み込めません");
	my $line = <$fh>;
	close $fh;

	$contents .= <<"EOM";
<br>
<a href="screen_shot.cgi">最近のスクリーンショット</a><br /><div>$line</div>
EOM
	
	&side_menu($contents);
}


#=========================================================
# クッキー取得
#=========================================================
sub get_cookie {
	my %cooks;
	my @cooks;

	for my $pair (split /;/, $ENV{HTTP_COOKIE}) {
		my($k, $v) = split /=/, $pair;
		$k =~ s/\s//g;
		$cook{$k} = $v;
	}
	for my $c (split /<>/, $cook{party}) {
		$c =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack 'H2', $1/eg;
		push @cooks, $c;
	}
	return @cooks;
}

