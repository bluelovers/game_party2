# ��̒��g
@treasures = (
[5..15], # ����No
[8..20], # �h��No
[0,2,3,3,14..26,72,73,78..84], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '�ް��',
		hp			=> 1500,
		at			=> 100,
		df			=> 60,
		ag			=> 50,
		get_exp		=> 150,
		get_money	=> 100,
		icon		=> 'mon/546.gif',
		
		old_sp		=> 20,
		hit			=> 150, # ������p������150%
		job			=> 27, # �����m���Ȃ��ނ�
		sp			=> 10,
		mp			=> 77,
		tmp			=> '�U�y��',
	},
);

# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = (0,0,0,1,1,1,2,2,3,4,4,5,5,6,6,7,7,8,9);


# �����X�^�[
@monsters = (
	{ # 0
		name		=> 'ϯ������',
		hp			=> 70,
		at			=> 85,
		df			=> 36,
		ag			=> 50,
		get_exp		=> 10,
		get_money	=> 8,
		icon		=> 'mon/063.gif',

		job			=> 95, # ���傤����
		sp			=> 10,
		mp			=> 50,
	},
	{ # 1
		name		=> '����������',
		hp			=> 34,
		at			=> 76,
		df			=> 130,
		ag			=> 45,
		get_exp		=> 11,
		get_money	=> 9,
		icon		=> 'mon/052.gif',

		old_sp		=> 30, # �e���V�����A�h��
		job			=> 91, # �܂Ђ�������
		sp			=> 10,
		mp			=> 19,
	},
	{ # 2
		name		=> '���',
		hp			=> 50,
		at			=> 50,
		df			=> 60,
		ag			=> 50,
		get_exp		=> 15,
		get_money	=> 10,
		icon		=> 'mon/071.gif',

		old_sp		=> 30, # �e���V�����A�h��
		job			=> 20, # �����m���΂�
		sp			=> 10,
		mp			=> 42,
	},
	{ # 3
		name		=> '�܂ǂ���',
		hp			=> 55,
		at			=> 35,
		df			=> 30,
		ag			=> 70,
		get_exp		=> 16,
		get_money	=> 6,
		icon		=> 'mon/060.gif',

		job			=> 39, # �ײуM��
		sp			=> 3,
		mp			=> 66,
	},
	{ # 4
		name		=> '������ް',
		hp			=> 100,
		at			=> 70,
		df			=> 50,
		ag			=> 150,
		get_exp		=> 20,
		get_money	=> 5,
		icon		=> 'mon/058.gif',

		job			=> 14, # �x��q�݂��킵���Ⴍ,�ӂ����Ȃ��ǂ�,�����Ȃ���
		sp			=> 16,
		mp			=> 50,
	},
	{ # 5
		name		=> '�����ް',
		hp			=> 100,
		at			=> 70,
		df			=> 50,
		ag			=> 150,
		get_exp		=> 20,
		get_money	=> 5,
		icon		=> 'mon/059.gif',

		job			=> 14, # �x��q�݂��킵���Ⴍ,�ӂ����Ȃ��ǂ�,�����Ȃ���
		sp			=> 16,
		mp			=> 50,
	},
	{ # 6
		name		=> 'Ĺ��޳��',
		hp			=> 64,
		at			=> 55,
		df			=> 125,
		ag			=> 15,
		get_exp		=> 23,
		get_money	=> 7,
		icon		=> 'mon/212.gif',

		job			=> 21, # �ް��������������
		sp			=> 10,
		mp			=> 24,
	},
	{ # 7
		name		=> '�����ذ',
		hp			=> 50,
		at			=> 55,
		df			=> 15,
		ag			=> 120,
		get_exp		=> 15,
		get_money	=> 5,
		icon		=> 'mon/198.gif',

		old_sp		=> 20, # �e���V����
		job			=> 12, # �����g���Ђ̂���
		sp			=> 5,
		mp			=> 16,
	},
	{ # 8
		name		=> '�����',
		hp			=> 120,
		at			=> 85,
		df			=> 40,
		ag			=> 10,
		get_exp		=> 28,
		get_money	=> 10,
		icon		=> 'mon/199.gif',

		job			=> 12, # �����g���Ђ̂���,�����ǂ��̂���,������̂���,���тꂤ��,�Ȃ߂܂킷
		sp			=> 50,
		mp			=> 34,
	},
	{ # 9
		name		=> '�����׺��',
		hp			=> 150,
		at			=> 85,
		df			=> 35,
		ag			=> 20,
		get_exp		=> 24,
		get_money	=> 7,
		icon		=> 'mon/083.gif',

		job			=> 12, # �����g���Ђ̂���
		sp			=> 5,
		mp			=> 14,
	},
);



1;
