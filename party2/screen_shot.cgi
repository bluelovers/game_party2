#!/usr/local/bin/perl
require 'config.cgi';
#================================================
# �X�N���[���V���b�g�ꗗ�\�� Created by Merino
# �ۑ����� config.cgi��$max_log
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
		? qq|<form action="$script"><input type="hidden" name="id" value="$id" /><input type="hidden" name="pass" value="$pass" /><input type="submit" value="�߂�" /></form>|
		: qq|<form action="$script_index"><input type="submit" value="�s�n�o�֖߂�" /></form>|
		;
	print $back;
	open my $fh, "< $in{path}/screen_shot.cgi" or &error("$in{path}/screen_shot.cgi�t�@�C�����ǂݍ��߂܂���");
	print $_ while <$fh>;
	close $fh;
	print $back;
}

