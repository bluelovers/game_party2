# �ݒ�
%k = (
	p_name		=> '@��d���E@',# �N�G�X�g��
	p_join		=> 6,				# �퓬�Q�����(�l)
	p_leader	=> '�ł̸ؽ��',	# �N�G�X�g���[�_�[��
	speed		=> 12,				# �i�s�X�s�[�h(�b)
	need_join	=> 'hp_200_o',		# �Q������(./lib/quest.cgi 192�s�ڂ�������Q�l)
);

# �����험�i(����No)
@treasures = (
[], # ����No
[], # �h��No
[23,59,60..65,107], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '�ł̸ؽ��',
		hp			=> 150000,
		at			=> 500,
		df			=> 300,
		ag			=> 300,
		get_exp		=> 4000,
		get_money	=> 3000,
		icon		=> 'mon/706.gif',
		
		hit			=> 900, # ������p������400%
		job			=> 95, # ����
		sp			=> 999,
		old_job		=> 95, # ����
		old_sp		=> 999,
		mmp			=> 999999,
		mp			=> 99999,
		tmp			=> '������',
	},
);


# ��������郂���X�^�[
@monsters = (
	{ # 0
		name		=> '�����̋�',
		hp			=> 300,
		at			=> 400,
		df			=> 300,
		ag			=> 300,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/570.gif',

		job			=> 20, # ����
		sp			=> 999,
		old_job		=> 36, # ���̂܂ˎt
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '������',
	},
	{ # 1
		name		=> '�􂢂̋�',
		hp			=> 300,
		at			=> 400,
		df			=> 300,
		ag			=> 300,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/571.gif',

		job			=> 58, # �ް����
		sp			=> 999,
		old_job		=> 36, # ���̂܂ˎt
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '������',
	},
	{ # 2
		name		=> '�Í��̋�',
		hp			=> 300,
		at			=> 400,
		df			=> 300,
		ag			=> 300,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/572.gif',

		job			=> 22, # �Í��R�m
		sp			=> 999,
		old_job		=> 36, # ���̂܂ˎt
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '������',
	},
	{ # 3
		name		=> '����̋�',
		hp			=> 300,
		at			=> 400,
		df			=> 300,
		ag			=> 300,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/573.gif',

		job			=> 51, # �������m
		sp			=> 999,
		old_job		=> 36, # ���̂܂ˎt
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '������',
	},
);


1;
