#!/usr/local/bin/perl
require 'config.cgi';
require '_side_menu.cgi';
#================================================
# セルフデータ削除 Created by Merino
#================================================
&decode;
&header;
&run;
&footer;
exit;
#================================================
sub run {
	if (defined $in{login_name} && defined $in{pass}) {
		&delete_myself;
		return;
	}
	my $contents = <<"EOM";
<h2>プレイデータを削除する</h2>

<div class="mes" style="width: 600px; background: #F00;">
	<ul>
		<li>登録している自分のデータを全て削除</li>
		<li>※削除したデータは二度と元に戻りません</li>
		<li>※確認画面は出ません。削除ボタンを押したら削除となります</li>
		<li>※登録⇒即削除⇒再登録はできません(しばらく時間をあけないと多重登録扱いになります)</li>
	</ul>
</div>
<br />
<form method="$method" action="delete.cgi">
<table class="table1">
	<tr><th>§プレイヤー§</th></tr><tr><td><input type="text" name="login_name" class="text_box1" /></td></tr>
	<tr><th>§パスワード§</th></tr><tr><td><input type="password" name="pass" class="text_box1" /></td></tr>
	<tr><th><input type="submit" value="＠データを削除する" /></th></tr>
</table>
</form>
EOM

	&side_menu($contents);
}

#=========================================================
# 削除処理
#=========================================================
sub delete_myself {
	&read_user;
	
	&delete_guild_member($m{guild}, $m{name}) if $m{guild};
	&delete_directory("$userdir/$id");
	my $contents .= qq|<div class="mes" style="background: #F00;"><p>プレイヤー『 <b>$m</b> 』のデータを削除しました</p></div>|;
	
	&minus_entry_count(1);

	&side_menu($contents);
}

