#!/usr/local/bin/perl
require 'config.cgi';
require '_side_menu.cgi';
$sleep_time *= 2;
#================================================
# �~�o���� Created by Merino
#================================================
&decode;
&header;
&run;
&footer;
exit;
#================================================
sub run {
	if (defined $in{login_name} && defined $in{pass}) {
		&refresh_player;
		return;
	}
	my $contents = <<"EOM";
<h2>�~�o����</h2>

<div class="mes" style="width: 600px">
	<ul>
		<li>��ʂɉ����\\������Ȃ��Ȃ��Ă��܂���</li>
		<li>�ςȖ������[�v�ɂ͂܂��Ă��܂����Ȃǂً̋}�~�o�����p</li>
		<li>���̏����͖{���ɂǂ����悤���Ȃ��Ȃ������ȊO�͎g�p���Ȃ��悤�ɁI</li>
		<li>�܂��́A�񎟔�Q�O����Q�ɂȂ�Ȃ��悤�Ɍf���Ȃǂɕ񍐂��邱��</li>
		<li>�������Ă��āA�ǂ̃^�C�~���O�ł����Ȃ��Ă��܂����̂��o�O�������e���ڂ�����</li>
		<li><font color="#FF0000">�g�p�y�i���e�B�F$sleep_time������</font></li>
		<li>�Q�Ă����ԂȂǂ̑҂����Ԃ�����������̂ł͂���܂���</li>
	</ul>
</div>
<br />
<form method="$method" action="rescue.cgi">
<table class="table1">
	<tr><th>���v���C���[��</th></tr><tr><td><input type="text" name="login_name" class="text_box1" /></td></tr>
	<tr><th>���p�X���[�h��</th></tr><tr><td><input type="password" name="pass" class="text_box1" /></td></tr>
	<tr><th><input type="submit" value="���~�o����" /></th></tr>
</table>
</form>
EOM

	&side_menu($contents);
}

#=========================================================
# ��ʂ��\������Ȃ��A�n�}�����ꍇ�Ɏg�p(��������ُ̈�G���[�̎�)
# �Ǘ���ʂ̃��Z�b�g�����Ƀy�i���e�B����������
#=========================================================
sub refresh_player {
	&read_user;
	
	if ($m{lib}) {
		$m{lib} = '';
		$m{sleep} = $m{sleep} > 0 ? $m{sleep} + $sleep_time * 60 : $sleep_time * 60;
		&write_user;
		$contents = qq|<div class="mes"><p>$m{name}���~�o�������܂���</p></div>|;
	}
	else {
		$contents = qq|<div class="mes"><p>���łɋ~�o����������Ă��܂�</p></div>|;
	}

	&side_menu($contents);
}

