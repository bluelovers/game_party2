# ��̒��g
@treasures = (
[1..7], # ����No
[1..7], # �h��No
[0,1,2,1,2,7..9,14,18..20,23,24,41,72], # ����No
);


# �{�X
@bosses= (
	{
		name		=> '�ޯ��ײ�',
		hp			=> 300,
		at			=> 35,
		df			=> 10,
		ag			=> 40,
		get_exp		=> 60,
		get_money	=> 20,
		icon		=> 'mon/006.gif',
	},
);

# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = (0,0,0,0,0,0,1,1,1,1,1,2,2,2,3,4,5);

# �����X�^�[
@monsters = (
	{ # 0
		name		=> '����ײ�',
		hp			=> 5,
		at			=> 7,
		ag			=> 7,
		get_exp		=> 1,
		get_money	=> 2,
		icon		=> 'mon/001.gif',
	},
	{ # 1
		name		=> '�ײ�',
		hp			=> 7,
		at			=> 11,
		ag			=> 9,
		get_exp		=> 2,
		get_money	=> 2,
		icon		=> 'mon/002.gif',
	},
	{ # 2
		name		=> '�ײ��޽',
		hp			=> 8,
		at			=> 15,
		ag			=> 10,
		get_exp		=> 3,
		get_money	=> 2,
		icon		=> 'mon/003.gif',
	},
	{ # 3
		name		=> '��޲�è',
		hp			=> 11,
		at			=> 12,
		ag			=> 20,
		get_exp		=> 4,
		get_money	=> 2,
		icon		=> 'mon/200.gif',
	},
	{ # 4
		hit			=> 70,
		name		=> '��׷�',
		hp			=> 10,
		at			=> 16,
		ag			=> 24,
		get_exp		=> 5,
		get_money	=> 3,
		icon		=> 'mon/025.gif',
		
		state		=> '����'
	},
	{ # 5
		name		=> '��ֺ',
		hp			=> 12,
		at			=> 12,
		ag			=> 16,
		get_exp		=> 6,
		get_money	=> 4,
		icon		=> 'mon/120.gif',
	},
);



1; # �폜�s��
