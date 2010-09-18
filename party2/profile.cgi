#!/usr/local/bin/perl
require 'config.cgi';
#================================================
# プロフィール表示(プレイヤー一覧用) Created by Merino
#================================================
&decode;
&header;
&run;
&footer;
exit;
#================================================
sub run {
	&error("そのようなプレイヤーは存在しません") unless $in{name};
	my $yid = unpack 'H*', $in{name};
	&error("プロフィールがありません") unless -f "$userdir/$yid/profile.cgi";

	$m{home} = $in{name};
	$is_top_profile = 1;

	require './lib/profile.cgi';
	print qq|<table><tr><td><form action="player.cgi"><input type="hidden" name="id" value="$yid"><input type="submit" value="戻る" /></form></td><td><form><input type="button" onclick="window.close(); return false;" value="閉じる"></form></td></tr></table>|;
	&view_profile;
}

