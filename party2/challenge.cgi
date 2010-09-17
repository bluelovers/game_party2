#!/usr/local/bin/perl
require 'config.cgi';
require '_side_menu.cgi';
require './lib/_data.cgi';
#================================================
# �`�������W�L�^�\�� Created by Merino
#================================================
&decode;
&header;
&run;
&footer;
exit;
#================================================
sub run {
	$in{no} ||= 0;

	my $contents = '<p>';
	for my $i (0 .. $#challenges) {
		$contents .= $i eq $in{no} ? qq|$challenges[$i] / | : qq|<a href="challenge.cgi?no=$i">$challenges[$i]</a> / |;
	}

	open my $fh, "< $logdir/challenge$in{no}.cgi" or &error("$logdir/challenge$in{no}.cgi�t�@�C�����ǂݍ��߂܂���");
	my $head_line = <$fh>;
	my($round, $ldate, $p_name, $color) = split /<>/, $head_line;

	$contents .= qq|</p><h2>�y$challenges[$in{no}]�z$p_name Lv.$round ($ldate)</h2>|;
	$contents .= qq|<table class="table1"><tr><th>���O</th><th>�E��</th><th>�X�e�[�^�X</th></tr>|;
	
	while (my $line = <$fh>) {
		my($name, $icon, $job, $old_job, $hp, $mp, $at, $df, $ag) = split /<>/, $line;
		$contents .= qq|<tr><td style="color: $color;"><img src="$icondir/$icon" />$name</td><td>[$jobs[$job][1] / $jobs[$old_job][1]]</td><td>$e2j{hp}<b>$hp</b> / $e2j{mp}<b>$mp</b> / $e2j{at}<b>$at</b> / $e2j{df}<b>$df</b> / $e2j{ag}<b>$ag</b></td></tr>\n|;
	}
	close $fh;
	
	$contents .= qq|</table>|;
	&side_menu($contents);
}

