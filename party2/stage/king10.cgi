# �ݒ�
%k = (
	p_name		=> '@�����ɑ��B�����@',	# �N�G�X�g��
	p_join		=> 6,						# �퓬�Q�����(�l)
	p_leader	=> '�ײ��ޯ��',			# �N�G�X�g���[�_�[��
	speed		=> 12,						# �i�s�X�s�[�h(�b)
	need_join	=> 'hp_100_u',				# �Q������(./lib/quest.cgi 192�s�ڂ�������Q�l)
);


# �����험�i(����No)
@treasures = (
[], # ����No
[], # �h��No
[1..43,59,72..89,101..103,107], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '�ײ��ޯ��',
		hp			=> 15000,
		at			=> 60,
		get_exp		=> 1500,
		get_money	=> 500,
		icon		=> 'mon/600.gif',
		
		hit			=> 300, # ������p������300%
		job			=> 95, # ����
		sp			=> 999,
		mmp			=> 99999,
		mp			=> 9999,
		tmp			=> '�U�y��',
	},
);


# ��������郂���X�^�[
@monsters = (
	{ # 0
		name		=> '����ײ�',
		hp			=> 20,
		at			=> 36,
		ag			=> 20,
		get_exp		=> 6,
		get_money	=> 3,
		icon		=> 'mon/001.gif',
		old_sp		=> 20,
	},
	{ # 1
		name		=> '�ײ�',
		hp			=> 25,
		at			=> 40,
		ag			=> 20,
		get_exp		=> 9,
		get_money	=> 4,
		icon		=> 'mon/002.gif',
		old_sp		=> 20,
	},
	{ # 2
		name		=> '�ײ��޽',
		hp			=> 30,
		at			=> 45,
		df			=> 5,
		ag			=> 25,
		get_exp		=> 10,
		get_money	=> 5,
		icon		=> 'mon/003.gif',
		old_sp		=> 20,
	},
	{ # 3
		name		=> '����ٽײ�',
		hp			=> 40,
		at			=> 45,
		df			=> 10,
		ag			=> 30,
		get_exp		=> 15,
		get_money	=> 10,
		icon		=> 'mon/020.gif',

		job			=> 90, # �ǂ����������A�|�C�Y��
		sp			=> 20,
		mp			=> 52,
	},
	{ # 4
		name		=> 'βнײ�',
		hp			=> 40,
		at			=> 35,
		ag			=> 40,
		get_exp		=> 20,
		get_money	=> 15,
		icon		=> 'mon/010.gif',

		job			=> 5, # �m���X�J���A�L�A���[�A�z�C�~
		sp			=> 6,
		mp			=> 65,
	},
	{ # 5
		name		=> '�ײт܂ǂ�',
		hp			=> 40,
		at			=> 30,
		ag			=> 45,
		get_exp		=> 24,
		get_money	=> 11,
		icon		=> 'mon/013.gif',

		job			=> 19, # �Ŗ����m���J�i��,�}�z�J���^,���_�p�j
		sp			=> 16,
		mp			=> 114,
	},
	{ # 6
		name		=> '��ٽײ�',
		hp			=> 6,
		at			=> 60,
		df			=> 2500,
		ag			=> 1500,
		get_exp		=> 250,
		get_money	=> 10,
		icon		=> 'mon/004.gif',

		job			=> 39, # �X���C���M��
		sp			=> 3,
		old_job		=> 99, # ������
		old_sp		=> 0,
		mp			=> 51,
		tmp			=> '������',
	},
);


1;
