# �ݒ�
%k = (
	p_name		=> '@�S�Ă��􂤎�@',# �N�G�X�g��
	p_join		=> 6,				# �퓬�Q�����(�l)
	p_leader	=> '�Í��̏�',		# �N�G�X�g���[�_�[��
	speed		=> 12,				# �i�s�X�s�[�h(�b)
	need_join	=> 'hp_300_o',		# �Q������(./lib/quest.cgi 192�s�ڂ�������Q�l)
);

# �����험�i(����No)
@treasures = (
[], # ����No
[], # �h��No
[59,71,107], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '�Í��̌�',
		hp			=> 100000,
		at			=> 500,
		df			=> 200,
		ag			=> 250,
		get_exp		=> 6000,
		get_money	=> 3000,
		icon		=> 'mon/707.gif',
		
		hit			=> 900, # ������p������700%
		job			=> 22, # �Í��R�m
		sp			=> 999,
		old_job		=> 95, # ����
		old_sp		=> 999,
		mmp			=> 999999,
		mp			=> 99999,
		tmp			=> '�U����',
	},
	{
		name		=> '�Í��̏�',
		hp			=> 100000,
		at			=> 300,
		df			=> 600,
		ag			=> 250,
		get_exp		=> 7000,
		get_money	=> 4000,
		icon		=> 'mon/708.gif',
		
		hit			=> 900, # ������p������700%
		job			=> 35, # ���E�m
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
		name		=> '�����̌�',
		hp			=> 350,
		at			=> 500,
		df			=> 200,
		ag			=> 150,
		get_exp		=> 200,
		get_money	=> 50,
		icon		=> 'mon/620.gif',

		job			=> 20, # ����
		sp			=> 999,
		old_job		=> 21, # �ް����
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '�U����',
	},
	{ # 1
		name		=> '�ł̌�',
		hp			=> 350,
		at			=> 500,
		df			=> 200,
		ag			=> 150,
		get_exp		=> 200,
		get_money	=> 50,
		icon		=> 'mon/621.gif',

		job			=> 22, # �Í��R�m
		sp			=> 999,
		old_job		=> 42, # ����
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '�U����',
	},
	{ # 2
		name		=> '��̌�',
		hp			=> 350,
		at			=> 500,
		df			=> 200,
		ag			=> 150,
		get_exp		=> 200,
		get_money	=> 50,
		icon		=> 'mon/622.gif',

		job			=> 2, # ���m
		sp			=> 999,
		old_job		=> 24, # �����m
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '�U����',
	},
	{ # 3
		name		=> '�����̏�',
		hp			=> 350,
		at			=> 200,
		df			=> 500,
		ag			=> 200,
		get_exp		=> 150,
		get_money	=> 100,
		icon		=> 'mon/623.gif',

		job			=> 20, # ����
		sp			=> 999,
		old_job		=> 48, # �V�g
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '������',
	},
	{ # 4
		name		=> '��̏�',
		hp			=> 350,
		at			=> 200,
		df			=> 500,
		ag			=> 200,
		get_exp		=> 150,
		get_money	=> 100,
		icon		=> 'mon/624.gif',

		job			=> 58, # �ް����
		sp			=> 999,
		old_job		=> 56, # ���ް��
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '������',
	},
	{ # 5
		name		=> '�ł̏�',
		hp			=> 350,
		at			=> 200,
		df			=> 500,
		ag			=> 200,
		get_exp		=> 150,
		get_money	=> 100,
		icon		=> 'mon/625.gif',

		job			=> 19, # �Ŗ����m
		sp			=> 999,
		old_job		=> 31, # �����m
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '������',
	},
	{ # 6
		name		=> '�����̌�',
		hp			=> 350,
		at			=> 400,
		df			=> 400,
		ag			=> 300,
		get_exp		=> 200,
		get_money	=> 100,
		icon		=> 'mon/626.gif',

		job			=> 35, # ����
		sp			=> 999,
		old_job		=> 32, # �����m
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '�U����',
	},
);


1;
