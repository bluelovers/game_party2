# ��̒��g
@treasures = (
[15..25], # ����No
[15..25], # �h��No
[16..26,16..26,27,35,57,58,75..87,109], # ����No
);


# �{�X
@bosses= (
	{
		name		=> '��ٷݸ�A',
		hp			=> 25,
		at			=> 200,
		df			=> 8000,
		ag			=> 2000,
		get_exp		=> 4000,
		get_money	=> 100,
		icon		=> 'mon/517.gif',

		job			=> 40, # ʸ�����
		sp			=> 999,
		old_job		=> 99, # ������
		old_sp		=> 0,
		mp			=> 299,
		tmp			=> '������',
	},
	{
		name		=> '�ް���ݽײ�',
		hp			=> 10,
		at			=> 300,
		df			=> 15000,
		ag			=> 8000,
		get_exp		=> 5000,
		get_money	=> 10000,
		icon		=> 'mon/590.gif',

		job			=> 40, # ʸ�����
		sp			=> 999,
		old_job		=> 99, # ������
		old_sp		=> 0,
		mp			=> 399,
		tmp			=> '������',
	},
	{
		name		=> '��ٷݸ�B',
		hp			=> 25,
		at			=> 200,
		df			=> 8000,
		ag			=> 2000,
		get_exp		=> 4000,
		get_money	=> 100,
		icon		=> 'mon/517.gif',

		job			=> 40, # ʸ�����
		sp			=> 999,
		old_job		=> 99, # ������
		old_sp		=> 0,
		mp			=> 299,
		tmp			=> '������',
	},
);

# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = (0,0,0,0,1,1,2);

# �����X�^�[
@monsters = (
	{ # 0
		name		=> '��ٽײ�',
		hp			=> 8,
		at			=> 70,
		df			=> 2500,
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
	{ # 1
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
		mp			=> 61,
		tmp			=> '������',
	},
	{ # 2
		name		=> '��ٷݸ�',
		hp			=> 25,
		at			=> 200,
		df			=> 8000,
		ag			=> 2000,
		get_exp		=> 4000,
		get_money	=> 100,
		icon		=> 'mon/517.gif',

		job			=> 40, # ʸ�����
		sp			=> 999,
		old_job		=> 99, # ������
		old_sp		=> 0,
		mp			=> 199,
		tmp			=> '������',
	},
);



1;
