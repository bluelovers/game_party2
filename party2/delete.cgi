#!/usr/local/bin/perl
require 'config.cgi';
require '_side_menu.cgi';
#================================================
# �Z���t�f�[�^�폜 Created by Merino
#================================================
&decode;
&header;
&run;
&footer;
exit;
#================================================
sub run {
	if (defined $in{login_name} && defined $in{pass}) {
		&delete_myself;
		return;
	}
	my $contents = <<"EOM";
<h2>�v���C�f�[�^���폜����</h2>

<div class="mes" style="width: 600px; background: #F00;">
	<ul>
		<li>�o�^���Ă��鎩���̃f�[�^��S�č폜</li>
		<li>���폜�����f�[�^�͓�x�ƌ��ɖ߂�܂���</li>
		<li>���m�F��ʂ͏o�܂���B�폜�{�^������������폜�ƂȂ�܂�</li>
		<li>���o�^�ˑ��폜�ˍēo�^�͂ł��܂���(���΂炭���Ԃ������Ȃ��Ƒ��d�o�^�����ɂȂ�܂�)</li>
	</ul>
</div>
<br />
<form method="$method" action="delete.cgi">
<table class="table1">
	<tr><th>���v���C���[��</th></tr><tr><td><input type="text" name="login_name" class="text_box1" /></td></tr>
	<tr><th>���p�X���[�h��</th></tr><tr><td><input type="password" name="pass" class="text_box1" /></td></tr>
	<tr><th><input type="submit" value="���f�[�^���폜����" /></th></tr>
</table>
</form>
EOM

	&side_menu($contents);
}

#=========================================================
# �폜����
#=========================================================
sub delete_myself {
	&read_user;
	
	&delete_guild_member($m{guild}, $m{name}) if $m{guild};
	&delete_directory("$userdir/$id");
	my $contents .= qq|<div class="mes" style="background: #F00;"><p>�v���C���[�w <b>$m</b> �x�̃f�[�^���폜���܂���</p></div>|;
	
	&minus_entry_count(1);

	&side_menu($contents);
}

