# ��̒��g
@treasures = (
[3..8], # ����No
[3..9], # �h��No
[0,1..3,1..3,7..11,7..11,18..21,23,24,41,42,79,80], # ����No
);


# �{�X
@bosses= (
	{
		name		=> '�޸�ɺA',
		hp			=> 30,
		at			=> 20,
		df			=> 10,
		ag			=> 11,
		get_exp		=> 15,
		get_money	=> 12,
		icon		=> 'mon/031.gif',

		job			=> 90, # �ǂ���������
		sp			=> 10,
		mp			=> 29,
	},
	{
		name		=> '�l�ʎ�',
		hp			=> 500,
		at			=> 40,
		df			=> 20,
		ag			=> 25,
		get_exp		=> 90,
		get_money	=> 60,
		icon		=> 'mon/503.gif',
		
		hit			=> 150, # ������p������150%
		job			=> 7, # ���l�܂���������߂�A�S�[���h�n���}�[�A���Ȃ��ނ�A�ǂ���������
		sp			=> 30,
		mp			=> 63,
	},
	{
		name		=> '�޸�ɺB',
		hp			=> 30,
		at			=> 20,
		df			=> 10,
		ag			=> 11,
		get_exp		=> 15,
		get_money	=> 12,
		icon		=> 'mon/031.gif',

		job			=> 90,
		sp			=> 10,
		mp			=> 29,
	},
);

# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = (0,0,0,1,1,1,1,2,2,2,3,4,4,5,5,6);


# �����X�^�[
@monsters = (
	{ # 0
		name		=> 'Ž�ް�',
		hp			=> 14,
		at			=> 16,
		ag			=> 25,
		get_exp		=> 4,
		get_money	=> 4,
		icon		=> 'mon/050.gif',
	},
	{ # 1
		name		=> '��޹�ɺ',
		hp			=> 15,
		at			=> 18,
		df			=> 9,
		ag			=> 12,
		get_exp		=> 5,
		get_money	=> 4,
		icon		=> 'mon/030.gif',
	},
	{ # 2
		name		=> '�޸�ɺ',
		hp			=> 18,
		at			=> 14,
		df			=> 8,
		ag			=> 10,
		get_exp		=> 6,
		get_money	=> 7,
		icon		=> 'mon/031.gif',

		job			=> 90,
		sp			=> 10,
		mp			=> 29,
	},
	{ # 3
		name		=> '���ް��ݻ�',
		hp			=> 20,
		at			=> 22,
		df			=> 7,
		ag			=> 24,
		get_exp		=> 8,
		get_money	=> 3,
		icon		=> 'mon/206.gif',
	},
	{ # 4
		hit			=> 70,
		name		=> '��׷�',
		hp			=> 15,
		at			=> 20,
		ag			=> 35,
		get_exp		=> 5,
		get_money	=> 3,
		icon		=> 'mon/025.gif',

		state		=> '����'
	},
	{ # 5
		name		=> '�ײ�',
		hp			=> 10,
		at			=> 11,
		ag			=> 16,
		get_exp		=> 3,
		get_money	=> 2,
		icon		=> 'mon/002.gif',
	},
	{ # 6
		name		=> '��޹�����',
		hp			=> 18,
		at			=> 20,
		df			=> 18,
		ag			=> 5,
		get_exp		=> 10,
		get_money	=> 10,
		icon		=> 'mon/038.gif',
	},
);



1;
