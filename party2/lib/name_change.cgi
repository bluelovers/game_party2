#=================================================
# ���O�ύX Created by Merino
#=================================================
# �ꏊ��
$this_title = '�����̊�';

# NPC��
$npc_name   = '@����';

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$logdir/name_change";

# �w�i�摜
$bgimg   = "$bgimgdir/name_change.gif";

# ���O�̕ύX�ɂ����邨��
$need_money_name = 300000;

# ���ʂ̕ύX�ɂ����邨��
$need_money_sex  = 10000;


#=================================================
# �͂Ȃ����t
#=================================================
@words = (
	"������$this_title����B�����ł͂���̖��O��p�X���[�h�A���ʂ�ς��邱�Ƃ��ł��̂���",
	"���O��ς���Ƃ������Ƃ͉^����ς���Ƃ������Ƃ���B�ƂĂ��傫�Ȃ��ƂȂ̂���",
	"�����_�̓{��ɐG��閼�O�ɂ���ƁA���݂��������炵������C�����邱�Ƃ���",
	"�����͈ȉ��̒ʂ�ƂȂ��Ă���B<br />���O�ύX $need_money_name G<br />�p�X���[�h�ύX ����<br />���ʕύX$need_money_sex G",
	"�M���h�ɎQ�����Ă���ꍇ�́A���O��ύX���邱�Ƃ��ł���",
);


#=================================================
# �ǉ��A�N�V����
#=================================================
push @actions, '�Ȃ܂�';
push @actions, '�ς���[��';
push @actions, '�����Ă񂩂�';
$actions{'�Ȃ܂�'} = sub{ &namae }; 
$actions{'�ς���[��'} = sub{ &pasuwado }; 
$actions{'�����Ă񂩂�'} = sub{ &seitenkan }; 

#=================================================
# �������Ă񂩂�
#=================================================
sub seitenkan {
	my $target = shift;
	
	if ($target eq '�j') {
		if ($m{sex} eq 'm') {
			$mes = "$npc_name�u���ł�$m�͒j���Ⴜ�v";
		}
		elsif ($m{money} < $need_money_sex) {
			$mes = "$npc_name�u�j�ɐ��]�����邽�߂̂���������ʂ��v";
		}
		elsif (!-f "$icondir/job/$m{job}_m.gif") {
			$mes = "$npc_name�u�E�Ƃ� $jobs[$m{job}][1] �͐��]�����邱�Ƃ͂ł��ʂ��v";
		}
		else {
			$m{sex}    = "m";
			$m{icon}   = "job/$m{job}_m.gif";
			$m{money} -= $need_money_sex;
			$npc_com   = "������߂Ēj�Ƃ��Đ����Ă����̂��ȁB����ł́c�J�b�I�I<br />$m�͍�����j�Ƃ��Ă̐l���̎n�܂肶��";
			&write_memory("������߂Ēj�Ƃ��Đ��܂�ς��");
		}
	}
	elsif ($target eq '��') {
		if ($m{sex} eq 'f') {
			$mes = "$npc_name�u���ł�$m�͏����Ⴜ�v";
		}
		elsif ($m{money} < $need_money_sex) {
			$mes = "$npc_name�u���ɐ��]�����邽�߂̂���������ʂ��v";
		}
		elsif (!-f "$icondir/job/$m{job}_f.gif") {
			$mes = "$npc_name�u�E�Ƃ� $jobs[$m{job}][1] �͐��]�����邱�Ƃ͂ł��ʂ��v";
		}
		else {
			$m{sex}    = "f";
			$m{icon}   = "job/$m{job}_f.gif";
			$m{money} -= $need_money_sex;
			$npc_com   = "�j����߂ď��Ƃ��Đ����Ă����̂��ȁB����ł́c�J�b�I�I<br />$m�͍����珗�Ƃ��Ă̐l���̎n�܂肶��";
			&write_memory("�j����߂ď��Ƃ��Đ��܂�ς��");
		}
	}
	else {
		$mes = $m{sex} eq 'm'
			? qq|<span onclick="text_set('�������Ă񂩂�>��')">�������Ă񂩂�>��<br />���ɐ��]������ɂ� $need_money_sex G�K�v����</span>|
			: qq|<span onclick="text_set('�������Ă񂩂�>�j')">�������Ă񂩂�>�j<br />�j�ɐ��]������ɂ� $need_money_sex G�K�v����</span>|
			;
	}
}

#=================================================
# ���Ȃ܂�
#=================================================
sub namae {
	my $y = shift;
	
	unless ($y) {
		$mes = qq|<span onclick="text_set('���Ȃ܂�>')">���O�̕ύX�ɂ� $need_money_name G�K�v����<br />�w���Ȃ܂�>�������x �������ɐV�������O���L������̂�</span>|;
		return;
	}
	if ($m{money} < $need_money_name) {
		$mes = qq|���O�̕ύX�ɂ� $need_money_name G�K�v����|;
		return;
	}
	elsif ($m{guild}) {
		$mes = qq|���O��ύX����ɂ́A��x�M���h��E�ނ���K�v�����邼|;
		return;
	}

	my $new_id = unpack 'H*', $y;
	$mes = "�v���C���[���ɕs���ȕ���( ,;\"\'&<>\\\/@ )���܂܂�Ă��܂�"	if $y =~ /[,;\"\'&<>\\\/@]/;
	$mes = "�v���C���[���ɕs���ȕ���( �� )���܂܂�Ă��܂�"				if $y =~ /��/;
	$mes = "�v���C���[���ɕs���ȋ󔒂��܂܂�Ă��܂�"					if $y =~ /�@|\s/;
	$mes = "�v���C���[���͑S�p�S(���p�W)�����ȓ��ł�"					if length($y) > 8;
	$mes = "�v���C���[���ƃp�X���[�h�����ꕶ����ł�"					if $y eq $pass;
	$mes = "���łɓ������O�̃v���C���[�����݂��܂�"						if -f "$userdir/$new_id";
	return if $mes;
	
	rename "$userdir/$id", "$userdir/$new_id" or &error("���O�̕ύX�Ɏ��s���܂���");
	
	$com .= "$m�� $need_money_name G���������܂���";
	$npc_com = "������ $m �� $y �Ɩ���邪�悢<br />���O�C������Ƃ��̃v���C���[�����ς�������璍�ӂ���񂶂Ⴜ�I<br />�O�̂��߁A��x���O�A�E�g���ă��O�C�������ق����悢��";
	$id = $new_id;
	$m{name} = $y;
	$m{money} -= $need_money_name;
	
	&write_memory("<b>$y</b> �ɖ��O��ύX����");
	&write_news("$m�� <b>$y</b> �Ɩ��O��ύX����");
	&leave_member($m);
}

#=================================================
# ���ς���[��
#=================================================
sub pasuwado {
	my $y = shift;
	unless ($y) {
		$mes = qq|<span onclick="text_set('���ς���[��>')">�w���ς���[��>�������x �������ɐV�����p�X���[�h���L������̂�|;
		return;
	}

	$mes = "�p�X���[�h�͔��p�p�����œ��͂��ĉ�����"		if $y =~ m/[^0-9a-zA-Z]/;
	$mes = "�p�X���[�h�͔��p�p�����S�`12�����ł�"		if length $y < 4 || length $y > 12;
	$mes = "�v���C���[���ƃp�X���[�h�����ꕶ����ł�"	if $y eq $m;
	return if $mes;
	
	$npc_com = "���O�C������Ƃ��̃p�X���[�h��V�������̂ɕύX������<br />�O�̂��߁A��x���O�A�E�g���ă��O�C�������ق����悢��";
	$to_name = $m;
	$pass = $m{pass} = $y;
}


1; # �폜�s��
