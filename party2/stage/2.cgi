# ��̒��g
@treasures = (
[5..14], # ����No
[4..10], # �h��No
[0,10,11,14,15,10,11,14..25,41,42,78..84], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '�S�쌕�m',
		hp			=> 1000,
		at			=> 60,
		df			=> 20,
		ag			=> 50,
		get_exp		=> 160,
		get_money	=> 50,
		icon		=> 'mon/500.gif',
		
		hit			=> 150, # ������p������150%
		job			=> 2, # ���m�����Ղ�����A�݂˂���
		sp			=> 10,
		mp			=> 45,
		
		tmp			=> '�U����',
	},
);

# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = (0,0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,7,8);


# �����X�^�[
@monsters = (
	{ # 0
		name		=> '�ް��',
		hp			=> 20,
		at			=> 36,
		df			=> 20,
		ag			=> 30,
		get_exp		=> 7,
		get_money	=> 4,
		icon		=> 'mon/035.gif',
	},
	{ # 1
		name		=> 'Ҳ�޺ް��',
		hp			=> 26,
		at			=> 32,
		df			=> 26,
		ag			=> 36,
		get_exp		=> 12,
		get_money	=> 6,
		icon		=> 'mon/036.gif',

		job			=> 6, # ���@�g����,ٶ�,���
		sp			=> 8,
		mp			=> 35,
	},
	{ # 2
		name		=> '���ް',
		hp			=> 21,
		at			=> 20,
		df			=> 35,
		ag			=> 44,
		get_exp		=> 11,
		get_money	=> 5,
		icon		=> 'mon/046.gif',

		job			=> 41, # ��׺�݂߂�������
		sp			=> 10,
		mp			=> 33,
	},
	{ # 3
		name		=> 'вגj',
		hp			=> 50,
		at			=> 40,
		df			=> 6,
		ag			=> 16,
		get_exp		=> 10,
		get_money	=> 7,
		icon		=> 'mon/040.gif',
		
		job			=> 9, # �����ߴ���д
		sp			=> 6,
		mp			=> 37,
	},
	{ # 4
		name		=> '�޲���m',
		hp			=> 45,
		at			=> 50,
		df			=> 15,
		ag			=> 20,
		get_exp		=> 12,
		get_money	=> 6,
		icon		=> 'mon/043.gif',
		
		job			=> 2, # ���m���񂭂�����A�݂˂���
		sp			=> 10,
		mp			=> 20,
	},
	{ # 5
		name		=> 'Ųĳ����',
		hp			=> 25,
		at			=> 30,
		df			=> 25,
		ag			=> 35,
		get_exp		=> 9,
		get_money	=> 5,
		icon		=> 'mon/070.gif',
		
		job			=> 19, # �Ŗ����mٶ��
		sp			=> 4,
		mp			=> 45,
	},
	{ # 6
		name		=> '�����۽',
		hp			=> 41,
		at			=> 31,
		df			=> 8,
		ag			=> 61,
		get_exp		=> 8,
		get_money	=> 4,
		icon		=> 'mon/203.gif',
	},
	{ # 7
		name		=> '����߷�',
		hp			=> 65,
		at			=> 55,
		df			=> 20,
		ag			=> 14,
		get_exp		=> 16,
		get_money	=> 8,
		icon		=> 'mon/039.gif',
	},
	{ # 8
		name		=> '�l�H����',
		hp			=> 120,
		at			=> 55,
		df			=> 10,
		ag			=> 200,
		get_exp		=> 30,
		get_money	=> 50,
		icon		=> 'mon/090.gif',
		
		job			=> 92, # ����n
		sp			=> 30,
		mp			=> 42,
		tmp			=> '�Q�{', 
	},
);



1;
