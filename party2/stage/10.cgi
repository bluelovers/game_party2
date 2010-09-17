# ��̒��g
@treasures = (
[13..27], # ����No
[13..19], # �h��No
[16..26,16..26,30,31,72..86], # ����No
);

# �{�X
@bosses= (
	{ # 7
		name		=> '����A',
		hp			=> 299,
		at			=> 119,
		df			=> 199,
		ag			=> 66,
		get_exp		=> 63,
		get_money	=> 13,
		icon		=> 'mon/072.gif',

		job			=> 31, # �����m���΂��A���イ���A���̃��[���b�g�A�H�H�H�H�A�}�C�e�B�K�[�h
		sp			=> 60,
		mp			=> 42,
	},
	{
		name		=> '����̋R�m',
		hp			=> 5500,
		at			=> 260,
		df			=> 180,
		ag			=> 180,
		get_exp		=> 666,
		get_money	=> 444,
		icon		=> 'mon/566.gif',
		
		hit			=> 200, # ������p������150%
		job			=> 24, # �����m�����񂬂�A���^������A�o�C�L���g�A���Ȃ��܂���
		sp			=> 70,
		old_job		=> 2, # ���m
		old_sp		=> 999,
		mmp			=> 5000,
		mp			=> 999,
		tmp			=> '�󗬂�',
	},
	{ # 7
		name		=> '����B',
		hp			=> 299,
		at			=> 119,
		df			=> 199,
		ag			=> 66,
		get_exp		=> 63,
		get_money	=> 13,
		icon		=> 'mon/072.gif',

		job			=> 31, # �����m���΂��A���イ���A���̃��[���b�g�A�H�H�H�H�A�}�C�e�B�K�[�h
		sp			=> 60,
		mp			=> 42,
	},
);

# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = ();


# �����X�^�[
@monsters = (
	{ # 0
		name		=> '��ׯ������',
		hp			=> 160,
		at			=> 130,
		df			=> 50,
		ag			=> 60,
		get_exp		=> 41,
		get_money	=> 10,
		icon		=> 'mon/064.gif',

		job			=> 9, # �����{�~�G�s�I�������Ԃ�
		sp			=> 10,
		old_job		=> 61, # ȸ��ݻ� ��т���
		old_sp		=> 10,
		mp			=> 41,
	},
	{ # 1
		name		=> '�а',
		hp			=> 170,
		at			=> 150,
		df			=> 60,
		ag			=> 60,
		get_exp		=> 43,
		get_money	=> 16,
		icon		=> 'mon/041.gif',
		old_sp		=> 20,
	},
	{ # 2
		name		=> '���ͯ��',
		hp			=> 90,
		at			=> 90,
		df			=> 180,
		ag			=> 60,
		get_exp		=> 44,
		get_money	=> 20,
		icon		=> 'mon/056.gif',

		job			=> 26, # �E�҂�����̂����A�₯�������A�}�k�[�T�A�����ǂ��̂���A�}�z�g�[��
		sp			=> 60,
		mp			=> 96,
	},
	{ # 3
		name		=> '�e�̋R�m',
		hp			=> 200,
		at			=> 170,
		df			=> 30,
		ag			=> 64,
		get_exp		=> 43,
		get_money	=> 25,
		icon		=> 'mon/044.gif',

		job			=> 24, # �����m�����񂬂�A���^������A�o�C�L���g�A���Ȃ��܂���
		sp			=> 30,
		mp			=> 16,
	},
	{ # 4
		name		=> '���ް',
		hp			=> 94,
		at			=> 90,
		df			=> 185,
		ag			=> 114,
		get_exp		=> 41,
		get_money	=> 20,
		icon		=> 'mon/046.gif',

		job			=> 41, # ��׺�݂߂��������A������̂���
		sp			=> 30,
		mp			=> 44,
	},
	{ # 5
		name		=> '���₵���e',
		hp			=> 98,
		at			=> 110,
		df			=> 190,
		ag			=> 144,
		get_exp		=> 43,
		get_money	=> 30,
		icon		=> 'mon/047.gif',

		job			=> 93, # �����U�L
		sp			=> 30,
		mp			=> 44,
	},
	{ # 6
		name		=> '�ײ��ޯ�',
		hp			=> 140,
		at			=> 145,
		df			=> 60,
		ag			=> 185,
		get_exp		=> 40,
		get_money	=> 15,
		icon		=> 'mon/027.gif',
		
		job			=> 38, # ����߲����イ���A�A�X�s��
		sp			=> 20,
		mp			=> 54,
	},
	{ # 7
		name		=> '����',
		hp			=> 199,
		at			=> 119,
		df			=> 199,
		ag			=> 66,
		get_exp		=> 45,
		get_money	=> 13,
		icon		=> 'mon/072.gif',

		job			=> 31, # �����m���΂��A���イ���A���̃��[���b�g�A�H�H�H�H�A�}�C�e�B�K�[�h
		sp			=> 60,
		mp			=> 42,
	},
	{ # 8
		name		=> '������߲���',
		hp			=> 180,
		at			=> 160,
		df			=> 80,
		ag			=> 60,
		get_exp		=> 39,
		get_money	=> 21,
		icon		=> 'mon/237.gif',

		job			=> 90, # �ǂ����������A�|�C�Y��
		sp			=> 20,
		mp			=> 92,
	},
	{ # 9
		name		=> '����ٷ���',
		hp			=> 160,
		at			=> 140,
		df			=> 80,
		ag			=> 160,
		get_exp		=> 41,
		get_money	=> 22,
		icon		=> 'mon/231.gif',

		job			=> 40, # ʸ����ك����~
		sp			=> 25,
		mp			=> 32,
	},
	{ # 10
		name		=> '���',
		hp			=> 200,
		at			=> 100,
		df			=> 10,
		ag			=> 200,
		get_exp		=> 50,
		get_money	=> 10,
		icon		=> 'mon/528.gif',

		job			=> 51, # �������m�܂Ԃ����Ђ���,�Ђ���݂̂��т�,���₵�̂Ђ���,���₵���Ђ���,�Ђ���̂��΂�
		sp			=> 110,
		mp			=> 62,
	},
);



1;
