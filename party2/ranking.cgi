#!/usr/local/bin/perl
require 'config.cgi';
require '_side_menu.cgi';
#================================================
# ���ҁE�p�Y Created by Merino
#================================================
my @files = (
#	[ '�^�C�g��', '���O�t�@�C����'],
	['���҃����L���O',	'kill_p'],
	['�p�Y�����L���O',	'kill_m'],
	['���������L���O',	'mao_c'],
	['�E�҃����L���O',	'hero_c'],
	['�����t�����L���O','cas_c'],
	['�菕�������L���O','help_c'],
	['�B�������L���O',	'alc_c'],
);

#================================================
&decode;
&header;
&run;
&footer;
exit;
#================================================
sub run {
	my @nos = ();
	my $contents = '<p>';
	for my $i (0 .. $#files) {
		next unless -s "$logdir/$files[$i][1].cgi";
		$contents .= $i eq $in{no} ? qq|$files[$i][0] / | : qq|<a href="ranking.cgi?no=$i">$files[$i][0]</a> / |;
		push @nos, $i;
	}
	$in{no} ||= $nos[0] || 0;
	$in{no} = 0 if $in{no} >= @files;

	$contents .= qq!</p><h2>$files[$in{no}][0]</h2><table class="table1"><tr><th>�����N</th><th>�|�C���g</th><th>���O���M���h</th><th>�R�����g</th></tr>!;
	my $count = 1;
	open my $fh, "< $logdir/$files[$in{no}][1].cgi" or &error("$logdir/$files[$in{no}][1]�t�@�C�����ǂݍ��߂܂���");
	while (my $line = <$fh>) {
		my($name, $guild, $color, $icon, $message, $point) = split /<>/, $line;
		$name .= "��$guild" if $guild;
		$contents .= qq|<tr><td align="center">$count��</td><td align="center"><b>$point</b></td><td style="color: $color;"><img src="$icondir/$icon">$name</td><td>$message</td></tr>\n|;
		++$count;
	}
	close $fh;
	
	$contents .= qq|</table>|;
	&side_menu($contents);
}

