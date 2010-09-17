# ��̒��g
@treasures = (
[20..28,32..37,39], # ����No
[20..39], # �h��No
[4..6,13,28,29,37,38,40,40,57,60..65,87,104..107,109,109,109], # ����No
);


# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = (0..10,0..10,11);

# �����X�^�[
@monsters = (
	{ # 0
		name		=> '��񂲂����傤',
		hp			=> 470,
		at			=> 320,
		df			=> 150,
		ag			=> 600,
		get_exp		=> 177,
		get_money	=> 72,
		icon		=> 'mon/532.gif',

		job			=> 41, # ��׺��
		sp			=> 999,
		old_job		=> 51, # �������m
		old_sp		=> 999,
		mp			=> 144,
		state		=> '�U��',
	},
	{ # 1
		name		=> '��ػް',
		hp			=> 400,
		at			=> 300,
		df			=> 210,
		ag			=> 500,
		get_exp		=> 146,
		get_money	=> 92,
		icon		=> 'mon/531.gif',

		job			=> 41, # ��׺��
		sp			=> 999,
		old_job		=> 27, # �����m
		old_sp		=> 999,
		mp			=> 174,
		state		=> '�U��',
	},
	{ # 2
		name		=> '���̂���',
		hp			=> 380,
		at			=> 280,
		df			=> 180,
		ag			=> 150,
		get_exp		=> 126,
		get_money	=> 62,
		icon		=> 'mon/541.gif',

		job			=> 42, # ����
		sp			=> 999,
		old_job		=> 93, # ����
		old_sp		=> 999,
		mp			=> 144,
		state		=> '�U��',
	},
	{ # 3
		name		=> '��',
		hp			=> 396,
		at			=> 296,
		df			=> 196,
		ag			=> 196,
		get_exp		=> 196,
		get_money	=> 96,
		icon		=> 'mon/544.gif',
		job			=> 15, # �������m
		sp			=> 999,
		old_job		=> 15, # �Ŗ����m
		old_sp		=> 999,
		mp			=> 196,
		state		=> '�U��',
	},
	{ # 4
		name		=> '����',
		hp			=> 400,
		at			=> 270,
		df			=> 150,
		ag			=> 300,
		get_exp		=> 126,
		get_money	=> 62,
		icon		=> 'mon/598.gif',

		job			=> 6, # ���@�g��
		sp			=> 999,
		old_job		=> 15, # �Ŗ����m
		old_sp		=> 999,
		mp			=> 144,
		state		=> '�U��',
	},
	{ # 5
		name		=> '����߲�',
		hp			=> 499,
		at			=> 380,
		df			=> 160,
		ag			=> 250,
		get_exp		=> 146,
		get_money	=> 70,
		icon		=> 'mon/568.gif',

		old_sp		=> 20,
		job			=> 38, # ����߲�
		sp			=> 999,
		mp			=> 121,
		state		=> '�U��',
	},
	{ # 6
		name		=> '�۲',
		hp			=> 410,
		at			=> 271,
		df			=> 160,
		ag			=> 280,
		get_exp		=> 162,
		get_money	=> 65,
		icon		=> 'mon/542.gif',
		old_sp		=> 20,
		job			=> 46, # �ެ���װ�w�u���X���b�g�A���������̃_�[�c�A�����܂̃_�C�X�A���̃��[���b�g
		sp			=> 80,
		mp			=> 59,
		state		=> '�U��',
	},
	{ # 7
		name		=> '�޽����',
		hp			=> 420,
		at			=> 440,
		df			=> 100,
		ag			=> 400,
		get_exp		=> 66,
		get_money	=> 242,
		icon		=> 'mon/543.gif',
		
		job			=> 93, # ����
		sp			=> 999,
		mp			=> 142,
		state		=> '�U��',
	},
	{ # 8
		name		=> '����',
		hp			=> 400,
		at			=> 424,
		df			=> 150,
		ag			=> 666,
		get_exp		=> 164,
		get_money	=> 155,
		icon		=> 'mon/235.gif',

		job			=> 48, # �V�g
		sp			=> 999,
		old_job		=> 46, # �ެ���װ
		old_sp		=> 999,
		mp			=> 149,
		state		=> '�U��',
	},
	{ # 9
		name		=> '��޽',
		hp			=> 430,
		at			=> 280,
		df			=> 520,
		ag			=> 180,
		get_exp		=> 120,
		get_money	=> 500,
		icon		=> 'mon/540.gif',

		job			=> 29, # �������m
		sp			=> 999,
		old_job		=> 93, # ����
		old_sp		=> 999,
		mp			=> 299,
		state		=> '�U��',
	},
	{ # 10
		name		=> '�ް���׺��',
		hp			=> 500,
		at			=> 360,
		df			=> 240,
		ag			=> 300,
		get_exp		=> 175,
		get_money	=> 125,
		icon		=> 'mon/534.gif',

		old_sp		=> 20,
		job			=> 41, # ��׺��
		sp			=> 999,
		mp			=> 149,
		state		=> '�U��',
	},
	{ # 11
		name		=> '��ٷݸ�',
		hp			=> 25,
		at			=> 200,
		df			=> 6000,
		ag			=> 3000,
		get_exp		=> 4000,
		get_money	=> 100,
		icon		=> 'mon/517.gif',

		job			=> 40, # ʸ�����
		sp			=> 999,
		old_job		=> 99, # ������
		old_sp		=> 0,
		mp			=> 499,
		tmp			=> '������',
		state		=> '�U��',
	},
);




1; # �폜�s��
