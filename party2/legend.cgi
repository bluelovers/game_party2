#!/usr/local/bin/perl
require 'config.cgi';
require '_side_menu.cgi';
#================================================
# �`�� Created by Merino
#================================================
# �\��������́@���ǉ��폜���בւ��\
my @files = (
#	['�^�C�g��',			'���O�t�@�C����'],
	['�W���u�}�X�^�[',		'comp_job'	],
	['�����X�^�[�}�X�^�[',	'comp_mon'	],
	['�E�F�|���L���[',		'comp_wea'	],
	['�A�[�}�[�L���O',		'comp_arm'	],
	['�A�C�e���j�X�g',		'comp_ite'	],
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
		$contents .= $i eq $in{no} ? qq|$files[$i][0] / | : qq|<a href="legend.cgi?no=$i">$files[$i][0]</a> / |;
		push @nos, $i;
	}
	$in{no} ||= $nos[0] || 0;
	$in{no} = 0 if $in{no} >= @files;

	$contents .= qq|</p><h2>$files[$in{no}][0]</h2><table class="table1"><tr><th>�L�O��</th><th>���O���M���h</th><th>�R�����g</th></tr>|;
	open my $fh, "< $logdir/$files[$in{no}][1].cgi" or &error("$logdir/$files[$in{no}][1]�t�@�C�����ǂݍ��߂܂���");
	while (my $line = <$fh>) {
		my($name, $guild, $color, $icon, $message, $ldate) = split /<>/, $line;
		$name .= "��$guild" if $guild;
		$contents .= qq|<tr><td>$ldate</td><td style="color: $color;"><img src="$icondir/$icon">$name</td><td>$message</td></tr>\n|;
	}
	close $fh;
	
	$contents .= "</table>";
	&side_menu($contents);
}

