# ��̒��g
@treasures = (
[1..39], # ����No
[1..39], # �h��No
[1..109,125..126,130..134], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '�l�H����',
		hp			=> 1000,
		at			=> 350,
		df			=> 50,
		ag			=> 400,
		get_exp		=> 200,
		get_money	=> 400,
		icon		=> 'mon/090.gif',
		
		old_sp		=> 20,
		job			=> 92, # ����n
		sp			=> 999,
		mp			=> 500,
		tmp			=> '�Q�{', 
	},
	{
		name		=> '�Я�',
		hp			=> 1500,
		at			=> 360,
		df			=> 100,
		ag			=> 700,
		get_exp		=> 400,
		get_money	=> 800,
		icon		=> 'mon/091.gif',
		
		hit			=> 150, # ������p������150%
		old_sp		=> 20,
		job			=> 93, # ����
		sp			=> 999,
		mp			=> 500,
		tmp			=> '�Q�{', 
	},
	{
		name		=> '�������ޯ��',
		hp			=> 2000,
		at			=> 370,
		df			=> 150,
		ag			=> 800,
		get_exp		=> 600,
		get_money	=> 1000,
		icon		=> 'mon/092.gif',
		
		hit			=> 150, # ������p������150%
		old_sp		=> 20,
		job			=> 93, # ����
		sp			=> 999,
		mp			=> 999,
		tmp			=> '�Q�{', 
	},
	{
		name		=> '�ׯ���ޯ��',
		hp			=> 2500,
		at			=> 380,
		df			=> 200,
		ag			=> 900,
		get_exp		=> 800,
		get_money	=> 2000,
		icon		=> 'mon/575.gif',

		hit			=> 200, # ������p������150%
		job			=> 19, # �Ŗ����m
		sp			=> 999,
		old_job		=> 93, # ����
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '�Q�{', 
	},
);

# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = ();


# �����X�^�[
@monsters = (
	{ # 0
		hit			=> 70,
		name		=> '��˰۰',
		hp			=> 270,
		at			=> 300,
		df			=> 150,
		ag			=> 150,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/100.gif',

		old_sp		=> 20,
		job			=> 34, # �E��
		sp			=> 999,
		mp			=> 200,
	},
	{ # 1
		hit			=> 70,
		name		=> '��̧���',
		hp			=> 280,
		at			=> 320,
		df			=> 250,
		ag			=> 50,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/101.gif',

		old_sp		=> 20,
		job			=> 1, # ��m
		sp			=> 999,
		mp			=> 100,
	},
	{ # 2
		hit			=> 70,
		name		=> '��ϰ��',
		hp			=> 240,
		at			=> 150,
		df			=> 100,
		ag			=> 300,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/102.gif',

		job			=> 6, # ���@�g��
		sp			=> 999,
		mp			=> 400,
	},
	{ # 3
		hit			=> 70,
		name		=> '����ذ��',
		hp			=> 250,
		at			=> 200,
		df			=> 150,
		ag			=> 200,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/103.gif',

		job			=> 5, # �m��
		sp			=> 999,
		mp			=> 300,
	},
	{ # 4
		name		=> '���˰۰',
		hp			=> 320,
		at			=> 280,
		df			=> 150,
		ag			=> 150,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/105.gif',

		old_sp		=> 20,
		job			=> 34, # �E��
		sp			=> 999,
		mp			=> 250,
	},
	{ # 5
		name		=> '���̧���',
		hp			=> 340,
		at			=> 320,
		df			=> 250,
		ag			=> 50,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/106.gif',

		old_sp		=> 20,
		job			=> 1, # ��m
		sp			=> 999,
		mp			=> 150,
	},
	{ # 6
		name		=> '���ϰ��',
		hp			=> 250,
		at			=> 150,
		df			=> 100,
		ag			=> 300,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/107.gif',

		job			=> 6, # ���@�g��
		sp			=> 999,
		mp			=> 300,
	},
	{ # 7
		name		=> '�����ذ��',
		hp			=> 270,
		at			=> 200,
		df			=> 150,
		ag			=> 200,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/108.gif',

		job			=> 5, # �m��
		sp			=> 999,
		mp			=> 250,
	},
);



1;
