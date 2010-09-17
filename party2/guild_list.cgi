#!/usr/local/bin/perl
require 'config.cgi';
require '_side_menu.cgi';
#================================================
# ギルド勢力 Created by Merino
#================================================
&decode;
&header;
&run;
&footer;
exit;
#================================================
sub run {
	my $file_time = (stat("$logdir/guild_list.cgi"))[9];
	my($min,$hour,$day,$month) = (localtime($file_time))[1..4];
	my $contents = sprintf("<p>更新日時 %d/%d %02d:%02d</p>", ++$month, $day, $hour, $min);

	$contents .= qq|<h2>ギルド勢力</h2>\n|;
	my $count = 1;
	
	open my $fh, "< $logdir/guild_list.cgi" or &error("$logdir/guild_list.cgiファイルが読み込めません");
	while (my $line = <$fh>) {
		$line =~ tr/\x0D\x0A//d; # 改行を除く
		my($gname,$gcount,$gcolor,$gmes,$gpoint,@gmembers) = split /<>/, $line;
		
		my $gid = unpack 'H*', $gname;
		$gname = qq|<img src="$guilddir/$gid/mark.gif" alt="ギルドマーク" /> $gname| if -f "$guilddir/$gid/mark.gif";
		$contents .= qq|<table class="table1" width="100%"><tr><td style="white-space: normal;">$count位 <span style="color: $gcolor;">$gname</span> 　<b>$gcount</b>人 　<b>$gpoint</b>Point　 $gmes</td></tr>\n|;
		$contents .= qq|<tr><td style="color: $gcolor; white-space: normal;"><img src="$icondir/etc/mark_leader.gif" />\n|;
		$contents .= join "、 ", @gmembers;
		$contents .= qq|</td></tr></table>\n|;
		++$count;
	}
	close $fh;
	&side_menu($contents);
}

