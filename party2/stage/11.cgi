# ��̒��g
@treasures = (
[15..23], # ����No
[17..27], # �h��No
[16..26,16..26,27,35,72..86], # ����No
);


# �{�X
@bosses= (
	{
		name		=> '����',
		hp			=> 8000,
		at			=> 300,
		df			=> 240,
		ag			=> 100,
		get_exp		=> 999,
		get_money	=> 500,
		icon		=> 'mon/560.gif',
		
		hit			=> 200, # ������p������150%
		job			=> 41, # ��׺��
		sp			=> 999,
		old_job		=> 25, # �ݸ�A
		old_sp		=> 1999,
		mmp			=> 8000,
		mp			=> 3000,
		tmp			=> '������',
	},
	{
		name		=> '��ٰ�İ�',
		hp			=> 15,
		at			=> 200,
		df			=> 5000,
		ag			=> 1000,
		get_exp		=> 70,
		get_money	=> 500,
		icon		=> 'mon/191.gif',
		
		job			=> 33, # ����
		sp			=> 130,
		old_job		=> 31, # �����m
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '������',
	},
);

# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = (0,0,1,1,2,2,3,3,4,5,6,7,8);

# �����X�^�[
@monsters = (
	{ # 0
		name		=> '���˰۰',
		hp			=> 220,
		at			=> 140,
		df			=> 120,
		ag			=> 110,
		get_exp		=> 50,
		get_money	=> 20,
		icon		=> 'mon/105.gif',

		old_sp		=> 20,
		job			=> 34, # �E�҂��΂��A���C�f�C���A���Ă��͂ǂ�
		sp			=> 60,
		mp			=> 61,
	},
	{ # 1
		name		=> '���̧���',
		hp			=> 250,
		at			=> 170,
		df			=> 150,
		ag			=> 20,
		get_exp		=> 50,
		get_money	=> 20,
		icon		=> 'mon/106.gif',

		old_sp		=> 20,
		job			=> 1, # ��m
		sp			=> 999,
		mp			=> 41,
	},
	{ # 2
		name		=> '���ϰ��',
		hp			=> 160,
		at			=> 100,
		df			=> 60,
		ag			=> 150,
		get_exp		=> 50,
		get_money	=> 20,
		icon		=> 'mon/107.gif',

		job			=> 6, # ���@�g�������A���J�j�A�M���A�}�k�[�T�A�����~�A�����z�[�A�׃M���}
		sp			=> 60,
		mp			=> 191,
	},
	{ # 3
		name		=> '�����ذ��',
		hp			=> 170,
		at			=> 120,
		df			=> 80,
		ag			=> 90,
		get_exp		=> 50,
		get_money	=> 20,
		icon		=> 'mon/108.gif',

		job			=> 5, # �m���X�J���A�L�A���[�A�z�C�~�A�o�M�A�x�z�C�~�A�o�M�}
		sp			=> 55,
		mp			=> 181,
	},
	{ # 4
		name		=> '��ٰ��׺��',
		hp			=> 150,
		at			=> 155,
		df			=> 80,
		ag			=> 120,
		get_exp		=> 51,
		get_money	=> 15,
		icon		=> 'mon/226.gif',

		job			=> 41, # ��׺�݂߂��������A������̂���
		sp			=> 90,
		mp			=> 38,
	},
	{ # 5
		name		=> 'ʸح�',
		hp			=> 200,
		at			=> 160,
		df			=> 90,
		ag			=> 180,
		get_exp		=> 60,
		get_money	=> 20,
		icon		=> 'mon/232.gif',

		job			=> 26, # �E�҂�����̂����A�₯�������A�}�k�[�T�A�����ǂ��̂���A�}�z�g�[��
		sp			=> 60,
		mp			=> 69,
	},
	{ # 6
		name		=> '�����ް',
		hp			=> 280,
		at			=> 170,
		df			=> 150,
		ag			=> 110,
		get_exp		=> 63,
		get_money	=> 24,
		icon		=> 'mon/533.gif',

		job			=> 26, # �E�҂�����̂����A�₯�������A�}�k�[�T�A�����ǂ��̂���A�}�z�g�[��
		sp			=> 60,
		mp			=> 79,
	},
	{ # 7
		name		=> '��׺��ϯ�',
		hp			=> 300,
		at			=> 200,
		df			=> 170,
		ag			=> 50,
		get_exp		=> 66,
		get_money	=> 20,
		icon		=> 'mon/556.gif',

		job			=> 41, # ��׺��
		sp			=> 100,
		mp			=> 99,
	},
	{ # 8
		name		=> '������ح�',
		hp			=> 340,
		at			=> 210,
		df			=> 180,
		ag			=> 120,
		get_exp		=> 68,
		get_money	=> 22,
		icon		=> 'mon/550.gif',

		job			=> 41, # ��׺��
		sp			=> 30,
		old_job		=> 26, # �E�҂�����̂����A�₯������
		old_sp		=> 15,
		mp			=> 99,
	},
);



1;
