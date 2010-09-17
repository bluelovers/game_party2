# ��̒��g
@treasures = (
[24..28,33..37], # ����No
[24..31,36..38], # �h��No
[4..6,12,21..23,28,29,28,29,40,72..86], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '�߰��ٽİ�',
		hp			=> 20,
		at			=> 250,
		df			=> 6000,
		ag			=> 2000,
		get_exp		=> 100,
		get_money	=> 500,
		icon		=> 'mon/194.gif',
		
		job			=> 90, # �ǂ����������A�|�C�Y���A�����ǂ��̂���
		sp			=> 999,
		old_job		=> 92, # �����z�[�A�˂ނ肱�������A���܂�����
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '������',
	},
	{
		name		=> '����',
		hp			=> 14000,
		at			=> 320,
		df			=> 300,
		ag			=> 140,
		get_exp		=> 2000,
		get_money	=> 1500,
		icon		=> 'mon/700.gif',
		
		hit			=> 250, # ������p������200%
		job			=> 35, # ����
		sp			=> 999,
		old_job		=> 22, # �Í��R�m
		old_sp		=> 999,
		mmp			=> 10000,
		mp			=> 4000,
		tmp			=> '�U����',
	},
	{
		name		=> 'گ�޽İ�',
		hp			=> 20,
		at			=> 250,
		df			=> 6000,
		ag			=> 2000,
		get_exp		=> 100,
		get_money	=> 500,
		icon		=> 'mon/190.gif',
		
		job			=> 26, # �E��
		sp			=> 999,
		old_job		=> 6, # ���@�g��
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '������',
	},
);

# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = (0,0,0,0,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,7,7,8,8,9,10);


# �����X�^�[
@monsters = (
	{ # 0
		name		=> '�ޯ�ޱ�',
		hp			=> 180,
		at			=> 180,
		df			=> 100,
		ag			=> 180,
		get_exp		=> 70,
		get_money	=> 35,
		icon		=> 'mon/526.gif',

		old_sp		=> 30,
		job			=> 20, # �������������ǂ�A���f�B�E�B�b�v�A�}�W�b�N�o���A�A���܂������A���_�p�j�_���X
		sp			=> 26,
		mp			=> 64,
	},
	{ # 1
		name		=> '�����۽',
		hp			=> 150,
		at			=> 160,
		df			=> 80,
		ag			=> 200,
		get_exp		=> 45,
		get_money	=> 15,
		icon		=> 'mon/203.gif',
		old_sp		=> 20,
	},
	{ # 2
		name		=> '����۽',
		hp			=> 270,
		at			=> 220,
		df			=> 130,
		ag			=> 50,
		get_exp		=> 60,
		get_money	=> 60,
		icon		=> 'mon/204.gif',

		old_sp		=> 20,
		job			=> 29, # �������m�X���E�A�w�C�X�g
		sp			=> 20,
		mp			=> 33,
	},
	{ # 3
		name		=> '�ł̌��m',
		hp			=> 230,
		at			=> 215,
		df			=> 120,
		ag			=> 125,
		get_exp		=> 74,
		get_money	=> 50,
		icon		=> 'mon/220.gif',

		old_sp		=> 20,
		job			=> 2, # ���m���񂭂�����A�݂˂����A�����Ȃ����A���΂��A���^������A�͂�Ԃ�����
		sp			=> 80,
		mp			=> 64,
	},
	{ # 4
		name		=> '���̋R�m',
		hp			=> 255,
		at			=> 185,
		df			=> 155,
		ag			=> 35,
		get_exp		=> 75,
		get_money	=> 40,
		icon		=> 'mon/222.gif',

		old_sp		=> 30,
		job			=> 1, # ��m���ԂƂ��A���΂��A����������߂�A�܂��񂬂�
		sp			=> 70,
		mp			=> 54,
	},
	{ # 5
		name		=> '��ٷݸ�',
		hp			=> 210,
		at			=> 180,
		df			=> 110,
		ag			=> 110,
		get_exp		=> 70,
		get_money	=> 40,
		icon		=> 'mon/567.gif',

		job			=> 38, # ����߲����イ���A�A�X�s���A�A�X�g����
		sp			=> 50,
		mp			=> 48,
	},
	{ # 6
		name		=> '����߲�',
		hp			=> 280,
		at			=> 200,
		df			=> 120,
		ag			=> 150,
		get_exp		=> 76,
		get_money	=> 50,
		icon		=> 'mon/568.gif',

		old_sp		=> 20,
		job			=> 38, # ����߲�
		sp			=> 999,
		mp			=> 44,
	},
	{ # 7
		name		=> '�װŲ�',
		hp			=> 200,
		at			=> 200,
		df			=> 180,
		ag			=> 180,
		get_exp		=> 70,
		get_money	=> 70,
		icon		=> 'mon/520.gif',

		job			=> 36, # ���̂܂ˎm
		sp			=> 999,
		mp			=> 94,
	},
	{ # 8
		name		=> '����ٱ�',
		hp			=> 180,
		at			=> 220,
		df			=> 120,
		ag			=> 200,
		get_exp		=> 62,
		get_money	=> 20,
		icon		=> 'mon/539.gif',

		job			=> 42, # ���݃R���t�F
		sp			=> 30,
		mp			=> 64,
	},
	{ # 9
		name		=> '�������ޯ��',
		hp			=> 900,
		at			=> 300,
		df			=> 95,
		ag			=> 800,
		get_exp		=> 100,
		get_money	=> 500,
		icon		=> 'mon/092.gif',
		
		job			=> 93, # ����
		sp			=> 20,
		mp			=> 69,
		tmp			=> '�Q�{', 
	},
	{ # 10
		name		=> 'ʸ�����',
		hp			=> 14,
		at			=> 110,
		df			=> 4000,
		ag			=> 2000,
		get_exp		=> 1500,
		get_money	=> 30,
		icon		=> 'mon/022.gif',

		job			=> 40, # ʸ����ك����~
		sp			=> 25,
		old_job		=> 99, # ������
		old_sp		=> 0,
		mp			=> 91,
		tmp			=> '������',
	},
);



1;
