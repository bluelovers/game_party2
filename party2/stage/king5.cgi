# �ݒ�
%k = (
	p_name		=> '@�S�Ă��x�z�����@',	# �N�G�X�g��
	p_join		=> 6,				# �퓬�Q�����(�l)
	p_leader	=> '�ް�Ͻ��',		# �N�G�X�g���[�_�[��
	speed		=> 12,				# �i�s�X�s�[�h(�b)
	need_join	=> 'hp_200_o',		# �Q������(./lib/quest.cgi 192�s�ڂ�������Q�l)
);


# �����험�i(����No)
@treasures = (
[], # ����No
[], # �h��No
[59,71,71,107], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '�ް�Ͻ��',
		hp			=> 150000,
		at			=> 500,
		df			=> 250,
		ag			=> 350,
		get_exp		=> 8000,
		get_money	=> 4000,
		icon		=> 'mon/705.gif',
		
		hit			=> 1000, # ������p������500%
		job			=> 55, # �d��
		sp			=> 999,
		old_job		=> 96, # ���]
		old_sp		=> 999,
		mmp			=> 9999999,
		mp			=> 999999,
		tmp			=> '100�{',
		state		=> '�S��',
	},
);



1;
