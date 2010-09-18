#!/usr/local/bin/perl
require 'config.cgi';
require '_side_menu.cgi';
require './lib/_data.cgi';
#================================================
# 新規登録 Created by Merino
#================================================
# 初期で選べる職業(No)
my @default_jobs = (1..12);


#================================================
&decode;
&access_check;
&header;
&error("現在メンテナンス中です。しばらくお待ちください(約 $mente_min 分間)") if $mente_min;
$in{mode} eq 'new_entry' ? &new_entry : &new_form;
&footer;
exit;

#================================================
# 新規登録フォーム
#================================================
sub new_form {
	my $job_html = qq|<select class="select1" name="job">|;
	for my $i (@default_jobs) {
		$job_html .= qq|<option value="$i">$jobs[$i][1]</option>|;
	}
	$job_html .= qq|</select>|;
	
	my $yid = $ENV{'QUERY_STRING'};
	my $contents = <<"EOM";
<h2>新規登録</h2>

<form method="$method" action="new_entry.cgi">
	<input type="hidden" name="mode" value="new_entry" />
	<input type="hidden" name="yid" value="$yid" />
	<ul>
		<li>記号(,;"'&<>\\/@)や空白は使えません。</li>
		<li>ネットマナーを守って楽しく遊びましょう。</li>
		<li><b>他人が不愉快になるような書き込みや多重登録は禁止です。見つけ次第削除します。</b></li>
	</ul>
	<table class="table1">
		<tr><td>プレイヤー名：</td><td><input type="text" name="name" class="text_box1" /></td></th></tr>
		<tr><td>　</td><td>全角４(半角８)文字まで</td></tr>
		<tr><td>パスワード：</td><td><input type="text" name="pass" class="text_box1" /></td></th></tr>
		<tr><td>　</td><td>半角英数字４～12文字まで</td></tr>
		<tr><td>職業：</td><td>$job_html</td></th></tr>
		<tr><td>　</td><td>職業は重要です。説明書の特徴をよく読み、自分に合った職業を選びましょう</td></tr>
		<tr><td>$e2j{sex}：</td><td><input type="radio" name="sex" value="m" checked="checked" />男　<input type="radio" name="sex" value="f" />女</td></tr>
		<tr><td>　</td><td>性別によって転職できる職業やアイコンが違います</td></tr>
	</table>
	<p><input type="submit" value="＠登録" /></p>
</form>
<br />
EOM

	&side_menu($contents);
}
#================================================
# 新規登録チェック＆完了処理
#================================================
sub new_entry {
	&check_black_list;
	&check_entry;
	&check_registered;
	&create_user;

	$contents = <<"EOM";
<p>以下の内容で登録しました</p>

<p class="strong">※プレイヤー名とパスワードはログインするときに必要なので、忘れないように!<p>
<table class="table1">
	<tr><th>プレイヤー</th><td>$m{name}</td>
	<tr><th>パスワード</th><td>$m{pass}</td>
	<tr><th>$e2j{sex}</th><td>$e2j{$m{sex}}</td>
	<tr><th>職業</th><td>$jobs[$m{job}][1]</td>
	<tr><th>$e2j{hp}</th><td align="right">$m{hp}</td>
	<tr><th>$e2j{mp}</th><td align="right">$m{mp}</td>
	<tr><th>$e2j{at}</th><td align="right">$m{at}</td>
	<tr><th>$e2j{df}</th><td align="right">$m{df}</td>
	<tr><th>$e2j{ag}</th><td align="right">$m{ag}</td>
</table>
<div>
説明書は読みましたか？<br />
わからないことがある場合は、まず説明書を読みましょう。
</div>
<form method="$method" action="login.cgi">
	<input type="hidden" name="is_cookie" value="1" />
	<input type="hidden" name="login_name" value="$in{name}" />
	<input type="hidden" name="pass" value="$in{pass}" />
	<input type="submit" value="＠プレイ" />
</form>
EOM
&side_menu($contents);
}

#================================================
# 登録チェック
#================================================
sub check_entry {
	&error("不正な登録処理です")				if $ENV{QUERY_STRING};
	&error("プレイヤー名が入力されていません")	unless $in{name};
	&error("パスワードが入力されていません")	if $in{pass} eq '';
	&error("$e2j{sex}が入力されていません")		if $in{sex} eq '';

	&error("プレイヤー名に不正な文字( ,;\"\'&<>\@ )が含まれています")	if $in{name} =~ /[,;\"\'&<>\@]/;
	&error("プレイヤー名に不正な文字( ＠ )が含まれています")			if $in{name} =~ /＠/;
	&error("プレイヤー名に不正な空白が含まれています")					if $in{name} =~ /　|\s/;
	&error("プレイヤー名は全角４(半角８)文字以内です")					if length($in{name}) > 8;
	&error("パスワードは半角英数字で入力して下さい")					if $in{pass} =~ m/[^0-9a-zA-Z]/;
	&error("パスワードは半角英数字４～12文字です")						if length $in{pass} < 4 || length $in{pass} > 12;
	&error("プレイヤー名とパスワードが同一文字列です")					if $in{name} eq $in{pass};
	&error("$e2j{sex}が異常です")										unless $in{sex} eq 'm' || $in{sex} eq 'f';

	my $is_ng_job = 1;
	for my $i (@default_jobs) {
		if ($i eq $in{job}) {
			$is_ng_job = 0;
			last;
		}
	}
	&error("職業が異常です") if $is_ng_job;
	
	$id = unpack 'H*', $in{name};
	&error("その名前はすでに登録されています") if -d "$userdir/$id";
	
	open my $fh, "< $logdir/entry.cgi" or &error("$logdir/entry.cgiファイルが読み込めません");
	my $line = <$fh>;
	close $fh;
	my($entry_count, $last_addr) = split /<>/, $line;
	&error("現在定員のため、新規登録は受け付けておりません") if $entry_count >= $max_entry;
	&error("多重登録は禁止しています") if $addr eq $last_addr;
}
#================================================
# 登録処理
#================================================
sub create_user {
	$id = unpack 'H*', $in{name};
	
	# フォルダ・ファイル作成
	mkdir "$userdir/$id", $mkdir or &error("その名前はすでに登録されています");
	for my $file_name (qw/collection depot hanasu home home_member item_send_mes job_master letter letter_log memory money monster monster_book profile recipe reload screen_shot send_item_mes stock user/) {
		my $output_file = "$userdir/$id/$file_name.cgi";
		open my $fh, "> $output_file" or &error("$output_file ファイルが作れませんでした");
		close $fh;
		chmod $chmod, $output_file;
	}
	open my $fh2, ">> $userdir/$id/collection.cgi" or &error("$userdir/$id/collection.cgiファイルが作れませんでした");
	print $fh2 ",\n,\n,\n";
	close $fh2;
	
	%m = ();
	$m = $m{name} = $in{name};
	$m{pass} = $in{pass};
	$m{job}  = $in{job};
	$m{sex}  = $in{sex};
	$m{money} = 200;
	$m{mhp}  = int(rand(3)) + 30;
	$m{mmp}  = int(rand(3)) + 6;
	$m{at}   = int(rand(3)) + 6;
	$m{df}   = int(rand(3)) + 6;
	$m{ag}   = int(rand(3)) + 6;
	$m{hp}   = $m{mhp};
	$m{mp}   = $m{mmp};
	$m{lv}   = 1;
	$m{icon} = "job/$m{job}_$m{sex}.gif";
	$m{color} = $default_color;
	$m{home} = $m;

	for my $k (qw/sleep job_lv exp medal coin coupon rare tired sp old_job old_sp wea arm ite is_full is_get is_eat kill_p kill_m cas_c hero_c mao_c/) {
		$m{$k} = 0;
	}
	
	&write_user;
	&write_memory("冒険者 <b>$m</b> 誕生！");
	&write_news("<b>$m</b> という冒険者が参加しました");

	require './lib/_add_monster_book.cgi';
	&write_monster_book;

	&plus_entry_count;
	&copy("$htmldir/space.gif", "$userdir/$id/bgimg.gif");
	
	# 紹介ID付なら紹介者に小さなメダル送信
	if ($in{yid}) {
		my $send_name = pack 'H*', $in{yid};
		&send_item($send_name, 3, 23, "$m{name}(紹介加入)");
	}
}


#================================================
# 登録者数プラス
#================================================
sub plus_entry_count {
	open my $fh, "+< $logdir/entry.cgi" or &error("$logdir/entry.cgiファイルが開けません");
	eval { flock $fh, 2; };
	my $line = <$fh>;
	my($entry_count, $last_addr) = split /<>/, $line;
	++$entry_count;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh "$entry_count<>$addr<>";
	close $fh;
}

#================================================
# ブラックリストのＩＰと同じかチェック
#================================================
sub check_black_list {
	open my $fh, "< $logdir/black_list.cgi" or &error("$logdir/black_list.cgiファイルが読み込めません");
	my $line = <$fh>;
	close $fh;
	&error("あなたのホストからは登録することが禁止されています") if $line =~ /,$host,/;
}

#================================================
# 多重登録禁止：全ユーザーのＩＰアドレスを調べる
#================================================
sub check_registered {
	opendir my $dh, "$userdir" or &error("ユーザーディレクトリが開けません");
	while (my $dir_name = readdir $dh) {
		next if $dir_name =~ /\./;
		
		my %datas = &get_you_datas($dir_name, 1);
		if ($addr eq $datas{addr}) {
#			&add_black_list($addr);
			&error("多重登録は禁止しています");
		}
	}
	closedir $dh;
}

