#!/usr/local/bin/perl
require 'config.cgi';
require '_side_menu.cgi';
#================================================
# �j���[�X�\�� Created by Merino
#================================================
&decode;
&header;
&run;
&footer;
exit;
#================================================
sub run {
	my $contents = qq|<h2>�ŋ߂̏o����</h2>\n|;
	open my $fh, "< $logdir/news.cgi" or &error("$logdir/news.cgi�t�@�C�����ǂݍ��߂܂���");
	$contents .= "$_<hr />" while <$fh>;
	close $fh;
	&side_menu($contents);
}

