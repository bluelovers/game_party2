#!/usr/local/bin/perl
require 'config.cgi';
#================================================
# �v���t�B�[���\��(�v���C���[�ꗗ�p) Created by Merino
#================================================
&decode;
&header;
&run;
&footer;
exit;
#================================================
sub run {
	&error("���̂悤�ȃv���C���[�͑��݂��܂���") unless $in{name};
	my $yid = unpack 'H*', $in{name};
	&error("�v���t�B�[��������܂���") unless -f "$userdir/$yid/profile.cgi";

	$m{home} = $in{name};
	$is_top_profile = 1;

	require './lib/profile.cgi';
	print qq|<table><tr><td><form action="player.cgi"><input type="hidden" name="id" value="$yid"><input type="submit" value="�߂�" /></form></td><td><form><input type="button" onclick="window.close(); return false;" value="����"></form></td></tr></table>|;
	&view_profile;
}

