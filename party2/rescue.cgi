#!/usr/local/bin/perl
require 'config.cgi';
require '_side_menu.cgi';
$sleep_time *= 2;
#================================================
# 救出処理 Created by Merino
#================================================
&decode;
&header;
&run;
&footer;
exit;
#================================================
sub run {
	if (defined $in{login_name} && defined $in{pass}) {
		&refresh_player;
		return;
	}
	my $contents = <<"EOM";
<h2>救出処理</h2>

<div class="mes" style="width: 600px">
	<ul>
		<li>画面に何も表\示されなくなってしまった</li>
		<li>変な無限ループにはまってしまったなどの緊急救出処理用</li>
		<li>この処理は本当にどうしようもなくなった時以外は使用しないように！</li>
		<li>まずは、二次被害三次被害にならないように掲示板などに報告すること</li>
		<li>何をしていて、どのタイミングでそうなってしまったのかバグった内容を詳しく報告</li>
		<li><font color="#FF0000">使用ペナルティ：$sleep_time分睡眠</font></li>
		<li>寝ている状態などの待ち時間を解除するものではありません</li>
	</ul>
</div>
<br />
<form method="$method" action="rescue.cgi">
<table class="table1">
	<tr><th>§プレイヤー§</th></tr><tr><td><input type="text" name="login_name" class="text_box1" /></td></tr>
	<tr><th>§パスワード§</th></tr><tr><td><input type="password" name="pass" class="text_box1" /></td></tr>
	<tr><th><input type="submit" value="＠救出処理" /></th></tr>
</table>
</form>
EOM

	&side_menu($contents);
}

#=========================================================
# 画面が表示されない、ハマった場合に使用(何かしらの異常エラーの時)
# 管理画面のリセット処理にペナルティがついただけ
#=========================================================
sub refresh_player {
	&read_user;
	
	if ($m{lib}) {
		$m{lib} = '';
		$m{sleep} = $m{sleep} > 0 ? $m{sleep} + $sleep_time * 60 : $sleep_time * 60;
		&write_user;
		$contents = qq|<div class="mes"><p>$m{name}を救出処理しました</p></div>|;
	}
	else {
		$contents = qq|<div class="mes"><p>すでに救出処理がされています</p></div>|;
	}

	&side_menu($contents);
}

