# ��̒��g
@treasures = (
[8..20], # ����No
[6..16], # �h��No
[0,3..4,15..26,41..43,43,43,72..86], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '�ł̖��p�m',
		hp			=> 1400,
		at			=> 70,
		df			=> 20,
		ag			=> 100,
		get_exp		=> 180,
		get_money	=> 120,
		icon		=> 'mon/510.gif',
		
		hit			=> 150, # ������p������150%
		job			=> 40, # ʸ����ك����~
		sp			=> 25,
		mp			=> 250,
		tmp			=> '���y��',
	},
	{ # 1
		name		=> '���@�g��',
		hp			=> 144,
		at			=> 50,
		df			=> 45,
		ag			=> 76,
		get_exp		=> 24,
		get_money	=> 9,
		icon		=> 'mon/061.gif',

		job			=> 6, # ���@�g�������A���J�j�A�M���A�}�k�[�T
		sp			=> 14,
		mp			=> 72,
	},
	{ # 2
		name		=> '�ײт܂ǂ�',
		hp			=> 160,
		at			=> 45,
		df			=> 30,
		ag			=> 100,
		get_exp		=> 26,
		get_money	=> 8,
		icon		=> 'mon/013.gif',

		job			=> 19, # �Ŗ����m���J�i��,�}�z�J���^,���_�p�j
		sp			=> 16,
		mp			=> 84,
	},
);

# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = (0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,8,9);

# �����X�^�[
@monsters = (
	{ # 0
		name		=> '�܂ǂ���',
		hp			=> 55,
		at			=> 45,
		df			=> 40,
		ag			=> 70,
		get_exp		=> 18,
		get_money	=> 6,
		icon		=> 'mon/060.gif',

		job			=> 39, # �ײуM��
		sp			=> 3,
		mp			=> 66,
	},
	{ # 1
		name		=> '���@�g��',
		hp			=> 67,
		at			=> 40,
		df			=> 45,
		ag			=> 76,
		get_exp		=> 20,
		get_money	=> 9,
		icon		=> 'mon/061.gif',

		job			=> 6, # ���@�g�������A���J�j�A�M���A�}�k�[�T
		sp			=> 14,
		mp			=> 90,
	},
	{ # 2
		name		=> '�ײт܂ǂ�',
		hp			=> 70,
		at			=> 35,
		df			=> 30,
		ag			=> 100,
		get_exp		=> 19,
		get_money	=> 8,
		icon		=> 'mon/013.gif',

		job			=> 19, # �Ŗ����m���J�i��,�}�z�J���^,���_�p�j
		sp			=> 16,
		mp			=> 104,
	},
	{ # 3
		name		=> '����ٴ���',
		hp			=> 66,
		at			=> 66,
		df			=> 66,
		ag			=> 66,
		get_exp		=> 11,
		get_money	=> 6,
		icon		=> 'mon/065.gif',

		old_sp		=> 30,
		job			=> 7, # ���l�܂���������߂�A�S�[���h�n���}�[
		sp			=> 10,
		mp			=> 66,
	},
	{ # 4
		name		=> '���ް��',
		hp			=> 124,
		at			=> 64,
		df			=> 35,
		ag			=> 110,
		get_exp		=> 15,
		get_money	=> 6,
		icon		=> 'mon/066.gif',

		job			=> 8, # �V�ѐl
		sp			=> 26,
		mp			=> 16,
		state		=> '����',
	},
	{ # 5
		name		=> '�����߂���',
		hp			=> 90,
		at			=> 78,
		df			=> 55,
		ag			=> 60,
		get_exp		=> 21,
		get_money	=> 8,
		icon		=> 'mon/077.gif',

		job			=> 19, # �Ŗ����m���J�i��,�}�z�J���^,���_�p�j
		sp			=> 16,
		mp			=> 34,
	},
	{ # 6
		name		=> '��߸ï��',
		hp			=> 100,
		at			=> 65,
		df			=> 50,
		ag			=> 64,
		get_exp		=> 20,
		get_money	=> 11,
		icon		=> 'mon/078.gif',

		job			=> 37, # ���E�m�}�z�g�[���A�A�X�g�����A���ǂ�ӂ����A�}�W�b�N�o���A�A�}�z�J���^
		sp			=> 50,
		mp			=> 44,
	},
	{ # 8
		name		=> '�ޯ���׷�',
		hp			=> 180,
		at			=> 98,
		df			=> 10,
		ag			=> 180,
		get_exp		=> 40,
		get_money	=> 8,
		icon		=> 'mon/258.gif',

		job			=> 37, # ��׺�݂߂�������,������̂���
		sp			=> 30,
		mp			=> 24,
		state		=> '����',
	},
	{ # 9
		name		=> '�Я�',
		hp			=> 300,
		at			=> 100,
		df			=> 30,
		ag			=> 300,
		get_exp		=> 50,
		get_money	=> 100,
		icon		=> 'mon/091.gif',
		
		job			=> 93, # ����
		sp			=> 10,
		mp			=> 68,
		tmp			=> '�Q�{', 
	},
	{ # 10
		name		=> '��ٽײ�',
		hp			=> 8,
		at			=> 40,
		df			=> 1500,
		ag			=> 1500,
		get_exp		=> 250,
		get_money	=> 10,
		icon		=> 'mon/004.gif',

		job			=> 39, # �X���C���M��
		sp			=> 3,
		old_job		=> 99, # ������
		old_sp		=> 0,
		mp			=> 31,
		tmp			=> '������',
	},
);



1;
