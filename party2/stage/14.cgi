# ��̒��g
@treasures = (
[26..28,32..37,39], # ����No
[30..39], # �h��No
[4..6,13,28,29,37,38,40,40,59..65,87,103..107], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '���ٻ��ްA',
		hp			=> 5000,
		at			=> 400,
		df			=> 300,
		ag			=> 3000,
		get_exp		=> 300,
		get_money	=> 300,
		icon		=> 'mon/696.gif',
		
		job			=> 37, # ���E�m
		sp			=> 999,
		old_job		=> 57, # ���
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '������',
	},
	{
		name		=> '���',
		hp			=> 15000,
		at			=> 600,
		df			=> 300,
		ag			=> 250,
		get_exp		=> 3000,
		get_money	=> 3000,
		icon		=> 'mon/800.gif',
		
		hit			=> 400, # ������p������400%
		job			=> 47, # �V�g
		sp			=> 999,
		old_job		=> 48, # �Í��R�m
		old_sp		=> 999,
		mmp			=> 30000,
		mp			=> 8000,
		tmp			=> '������',
	},
	{
		name		=> '���ٻ��ްB',
		hp			=> 5000,
		at			=> 400,
		df			=> 300,
		ag			=> 3000,
		get_exp		=> 300,
		get_money	=> 300,
		icon		=> 'mon/696.gif',
		
		job			=> 35, # ����
		sp			=> 999,
		old_job		=> 32, # �����m
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '������',
	},
);

# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = (0,0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,6,6,6,6,7,7,8,9);


# �����X�^�[
@monsters = (
	{ # 0
		name		=> '�޽ϼ�',
		hp			=> 555,
		at			=> 333,
		df			=> 222,
		ag			=> 222,
		get_exp		=> 111,
		get_money	=> 111,
		icon		=> 'mon/522.gif',

		job			=> 24, # �����m
		sp			=> 999,
		old_job		=> 11, # �|�g��
		old_sp		=> 999,
		mp			=> 222,
	},
	{ # 1
		name		=> '�ݸ���˰ӽ',
		hp			=> 600,
		at			=> 350,
		df			=> 180,
		ag			=> 160,
		get_exp		=> 120,
		get_money	=> 100,
		icon		=> 'mon/554.gif',

		old_sp		=> 20,
		job			=> 21, # ����m����������A�����Ȃ����A�������сA���Ă݁A����͂���
		sp			=> 40,
		mp			=> 149,
	},
	{ # 2
		name		=> '����߽',
		hp			=> 700,
		at			=> 500,
		df			=> 50,
		ag			=> 50,
		get_exp		=> 150,
		get_money	=> 10,
		icon		=> 'mon/564.gif',

		old_sp		=> 20,
		job			=> 1, # ��m
		sp			=> 999,
		old_job		=> 21, # ����m����������A�����Ȃ����A�������сA���Ă݁A����͂���A�݂Ȃ��낵
		mp			=> 99,
	},
	{ # 3
		name		=> '�ް���׺��',
		hp			=> 500,
		at			=> 300,
		df			=> 240,
		ag			=> 200,
		get_exp		=> 125,
		get_money	=> 95,
		icon		=> 'mon/534.gif',

		old_sp		=> 20,
		job			=> 41, # ��׺��
		sp			=> 999,
		mp			=> 149,
	},
	{ # 4
		name		=> '�İݺް��',
		hp			=> 300,
		at			=> 280,
		df			=> 400,
		ag			=> 100,
		get_exp		=> 100,
		get_money	=> 200,
		icon		=> 'mon/547.gif',

		old_sp		=> 30,
		job			=> 3, # �R�m���΂��A�܂���������߂�A���Ă݁A�����ڂ�����A�X�N���g
		sp			=> 60,
		mp			=> 155,
	},
	{ # 5
		name		=> '��޽',
		hp			=> 420,
		at			=> 270,
		df			=> 320,
		ag			=> 120,
		get_exp		=> 90,
		get_money	=> 400,
		icon		=> 'mon/540.gif',

		job			=> 29, # �������m
		sp			=> 999,
		old_job		=> 93, # �����U�L�U���L
		old_sp		=> 20,
		mp			=> 299,
	},
	{ # 6
		name		=> '����',
		hp			=> 350,
		at			=> 280,
		df			=> 100,
		ag			=> 300,
		get_exp		=> 115,
		get_money	=> 125,
		icon		=> 'mon/235.gif',

		job			=> 48, # �V�g�o�C�I�K��݂̂Ă񂵃V���h�E�t���A������Ȃ��Ă�
		sp			=> 160,
		old_job		=> 46, # �ެ���װ
		old_sp		=> 999,
		mp			=> 149,
	},
	{ # 7
		name		=> '��׺�ݿ����',
		hp			=> 650,
		at			=> 350,
		df			=> 260,
		ag			=> 100,
		get_exp		=> 155,
		get_money	=> 100,
		icon		=> 'mon/557.gif',

		job			=> 58, # �ް����
		sp			=> 999,
		old_job		=> 52, # ���l
		old_sp		=> 999,
		mp			=> 92,
		tmp			=> '����',
	},
	{ # 8
		name		=> '�޲�ެ',
		hp			=> 760,
		at			=> 460,
		df			=> 160,
		ag			=> 260,
		get_exp		=> 255,
		get_money	=> 300,
		icon		=> 'mon/559.gif',

		job			=> 53, # 峎t
		sp			=> 999,
		old_job		=> 48, # �V�g�o�C�I�K
		old_sp		=> 40,
		mp			=> 292,
		tmp			=> '����',
	},
	{ # 9
		name		=> '��ٷݸ�',
		hp			=> 25,
		at			=> 200,
		df			=> 6000,
		ag			=> 2000,
		get_exp		=> 4000,
		get_money	=> 100,
		icon		=> 'mon/517.gif',

		job			=> 40, # ʸ�����
		sp			=> 999,
		old_job		=> 99, # ������
		old_sp		=> 0,
		mp			=> 249,
		tmp			=> '������',
	},
);



1;
