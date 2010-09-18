#!/usr/local/bin/perl
require 'config.cgi';
require '_side_menu.cgi';
#================================================
# ニュース表示 Created by Merino
#================================================
&decode;
&header;
&run;
&footer;
exit;
#================================================
sub run {
	my $contents = qq|<h2>最近の出来事</h2>\n|;
	open my $fh, "< $logdir/news.cgi" or &error("$logdir/news.cgiファイルが読み込めません");
	$contents .= "$_<hr />" while <$fh>;
	close $fh;
	&side_menu($contents);
}

