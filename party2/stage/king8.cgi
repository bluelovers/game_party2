# �ݒ�
%k = (
	p_name		=> '@�łł�����������@',	# �N�G�X�g��
	p_join		=> 6,				# �퓬�Q�����(�l)
	p_leader	=> '���l�����',	# �N�G�X�g���[�_�[��
	speed		=> 12,				# �i�s�X�s�[�h(�b)
	need_join	=> 'hp_400_u',		# �Q������(./lib/quest.cgi 192�s�ڂ�������Q�l)
);


# �����험�i(����No)
@treasures = (
[], # ����No
[], # �h��No
[23,23,23,59,59..65,107], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '���l�����',
		hp			=> 80000,
		at			=> 300,
		df			=> 400,
		ag			=> 250,
		get_exp		=> 2500,
		get_money	=> 2000,
		icon		=> 'mon/605.gif',
		
		hit			=> 800, # ������p������400%
		job			=> 95, # ����
		sp			=> 999,
		old_job		=> 95, # ����
		old_sp		=> 999,
		mmp			=> 999999,
		mp			=> 99999,
		tmp			=> '�U�y��',
	},
);


# ��������郂���X�^�[
@monsters = (
	{ # 0
		name		=> '���l',
		hp			=> 250,
		at			=> 380,
		df			=> 50,
		ag			=> 150,
		get_exp		=> 100,
		get_money	=> 70,
		icon		=> 'mon/606.gif',

		old_sp		=> 20,
		job			=> 4, # ������
		sp			=> 999,
		mp			=> 300,
		tmp			=> '�U����',
	},
	{ # 1
		name		=> '�Ԗ��l',
		hp			=> 250,
		at			=> 380,
		df			=> 50,
		ag			=> 150,
		get_exp		=> 100,
		get_money	=> 70,
		icon		=> 'mon/607.gif',

		old_sp		=> 20,
		job			=> 1, # ��m
		sp			=> 999,
		mp			=> 300,
		tmp			=> '�U����',
	},
	{ # 2
		name		=> '�����l',
		hp			=> 250,
		at			=> 380,
		df			=> 50,
		ag			=> 150,
		get_exp		=> 100,
		get_money	=> 70,
		icon		=> 'mon/608.gif',

		old_sp		=> 20,
		job			=> 52, # ���l
		sp			=> 999,
		mp			=> 300,
		tmp			=> '�U����',
	},
	{ # 3
		name		=> '�����l',
		hp			=> 250,
		at			=> 380,
		df			=> 50,
		ag			=> 150,
		get_exp		=> 100,
		get_money	=> 70,
		icon		=> 'mon/609.gif',

		old_sp		=> 20,
		job			=> 25, # �ݸ
		sp			=> 999,
		mp			=> 300,
		tmp			=> '�U����',
	},
);




1;
