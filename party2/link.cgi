#!/usr/local/bin/perl
require 'config.cgi';
#================================================
# �ݸ�����ݸ Created by Merino
#================================================
# ���݂����ID���߽���̧װ�Ȃǂɉk��Ă��܂����߁B

&header;
&run;
&footer;
exit;

#================================================

sub run {
	my $url = $ENV{'QUERY_STRING'};

	$url =~ s/&#44;/,/g;
	$url =~ s/&lt;/</g;
	$url =~ s/&gt;/>/g;
	$url =~ s/&quot;/"/g;
	$url =~ s/&amp;/&amp/g;
	$url =~ s/&#59;/;/g;
	$url =~ s/&amp/&/g;
	print qq|<div class="mes">���L�̃y�[�W�ɃW�����v���悤�Ƃ��Ă��܂��B���Ȃ��ꍇ�̓N���b�N���Ă��������B<p><a href="$url">$url</a></p><br /></div>|;
}

