# �ݒ�
%k = (
	p_join		=> 4,			# �퓬�Q�����(�l)
	need_join	=> '0',			# �Q������(./lib/quest.cgi 192�s�ڂ�������Q�l)
);

# �󕔉�(20�K�`30�K�ȏ�B��ʊK�قǊm���A�b�v)
$tresure_round = int(rand(11)+20);


# ��̒��g
@treasures = (
[], # ����No
[], # �h��No
[6,15,57,72..74,87,101..103], # ����No
);


# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = ();


# �����X�^�[
if ($stage > 20) { # 20�K�ȍ~�� ���΂� �ɕύX
	@monsters = (
		{
			name		=> '���e��',
			hp			=> 400,
			at			=> 250,
			df			=> 150,
			ag			=> 150,
			get_exp		=> 30,
			get_money	=> 100,
			icon		=> 'mon/080.gif',
	
			job			=> 94, # �������K���e�A�˂�
			sp			=> 20,
			old_job		=> 31, # �����m���΂�
			old_sp		=> 11,
			mmp			=> 9999,
			mp			=> 42,
		},
	);
}
else {
	@monsters = (
		{
			name		=> '���e��',
			hp			=> 400,
			at			=> 250,
			df			=> 150,
			ag			=> 150,
			get_exp		=> 30,
			get_money	=> 100,
			icon		=> 'mon/080.gif',
	
			job			=> 94, # �������K���e�A�˂�
			sp			=> 20,
			old_job		=> 94, # �������K���e�A�˂�
			old_sp		=> 20,
			mmp			=> 9999,
			mp			=> 42,
		},
	);
}



1; # �폜�s��
