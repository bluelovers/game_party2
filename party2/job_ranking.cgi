#!/usr/local/bin/perl
require 'config.cgi';
require '_side_menu.cgi';
require './lib/_data.cgi';
#================================================
# 王者・英雄 Created by Merino
#================================================
&decode;
&header;
&run;
&footer;
exit;
#================================================
sub run {
	my $contents = qq|<h2>人気職業ランキング</h2><table><tr><td valign="top"><table class="table1"><tr><th>順位</th><th>職業名</th><th>画像</th><th>男女比</th></tr>\n|;

	my $count = 0;
	open my $fh, "< $logdir/job_ranking.cgi" or &error("$logdir/job_ranking.cgiファイルが読み込めません");
	my $total_point = <$fh>;
	$total_point =~ tr/\x0D\x0A//d;
	while (my $line = <$fh>) {
		my($job_no, $men_point, $female_point, $job_point) = split /<>/, $line;
		my $male_par   = int($men_point    / $job_point   * 100 + 0.5);
		my $female_par = int($female_point / $job_point   * 100 + 0.5);
		
		my $icon_img = '';
		$icon_img .= -f "$icondir/job/${job_no}_m.gif" ? qq|<img src="$icondir/job/${job_no}_m.gif" alt="$jobs[$job_no][1]" />| : qq|<img src="$htmldir/space.gif" width="20" />|;
		$icon_img .= qq|<img src="$icondir/job/${job_no}_f.gif" alt="$jobs[$job_no][1]" />| if -f "$icondir/job/${job_no}_f.gif";
		++$count;

		$contents .= qq|<tr><td><b>$count</b>位</td><td>$jobs[$job_no][1]</td><td>$icon_img</td><td><img src="$htmldir/space.gif" style="background-color: #66F; height: 5px; width: $male_par;" alt="$male_par%" /><img src="$htmldir/space.gif" style="background-color: #F99; height: 5px; width: $female_par;" alt="$female_par%" /></td></tr>\n|;
		$contents .= qq|</table></td><td valign="top"><table class="table1"><tr><th>順位</th><th>職業名</th><th>画像</th><th>男女比</th></tr>\n| if $count % 37 == 0 && $#jobs != $count;
	}
	close $fh;
	$contents .= qq|</table></table>|;

	&side_menu($contents);
}

