#!/usr/local/bin/perl
require 'config.cgi';
#================================================
# スクリーンショット一覧表示 Created by Merino
# 保存数は config.cgiの$max_log
#================================================
&decode;
&header;
&run;
&footer;
exit;
#================================================
sub run {
	$in{path} ||= "$logdir";
	my $back = $id && $pass
		? qq|<form action="$script"><input type="hidden" name="id" value="$id" /><input type="hidden" name="pass" value="$pass" /><input type="submit" value="戻る" /></form>|
		: qq|<form action="$script_index"><input type="submit" value="ＴＯＰへ戻る" /></form>|
		;
	print $back;
	open my $fh, "< $in{path}/screen_shot.cgi" or &error("$in{path}/screen_shot.cgiファイルが読み込めません");
	print $_ while <$fh>;
	close $fh;
	print $back;
}

