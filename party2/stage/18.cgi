# ��̒��g
@treasures = (
[33..37], # ����No
[36..38], # �h��No
[70,104,104], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '���̉E��',
		hp			=> 3000,
		at			=> 380,
		df			=> 200,
		ag			=> 200,
		get_exp		=> 500,
		get_money	=> 100,
		icon		=> 'mon/580.gif',
		
		hit			=> 250, # ������p������200%
		job			=> 58, # �ް����
		sp			=> 999,
		old_job		=> 20, # ����
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '������',
	},
	{
		name		=> '���̌�',
		hp			=> 5000,
		at			=> 450,
		df			=> 30,
		ag			=> 300,
		get_exp		=> 700,
		get_money	=> 300,
		icon		=> 'mon/582.gif',
		
		hit			=> 250, # ������p������200%
		job			=> 41, # ��׺��
		sp			=> 999,
		old_job		=> 38, # ����߲�
		old_sp		=> 999,
		mp			=> 3000,
		tmp			=> '�U����',
	},
	{
		name		=> '���̍���',
		hp			=> 3000,
		at			=> 380,
		df			=> 250,
		ag			=> 200,
		get_exp		=> 500,
		get_money	=> 100,
		icon		=> 'mon/581.gif',
		
		hit			=> 250, # ������p������200%
		job			=> 57, # ���
		sp			=> 999,
		old_job		=> 50, # ���юm
		old_sp		=> 90,
		mp			=> 999,
		tmp			=> '������',
	},
);

# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = ();


# �����X�^�[
@monsters = (
	{ # 0
		name		=> '���ײ�',
		hp			=> 250,
		at			=> 300,
		df			=> 180,
		ag			=> 250,
		get_exp		=> 95,
		get_money	=> 85,
		icon		=> 'mon/160.gif',
		
		old_sp		=> 20,
		job			=> 39, # �ײ�
		sp			=> 999,
		mp			=> 302,
		tmp			=> '���z��',
	},
	{ # 1
		name		=> '����׷�',
		hp			=> 330,
		at			=> 380,
		df			=> 50,
		ag			=> 300,
		get_exp		=> 85,
		get_money	=> 65,
		icon		=> 'mon/161.gif',
		
		old_sp		=> 20,
		job			=> 38, # ����߲�
		sp			=> 90,
		mp			=> 333,
		state		=> '����',
	},
	{ # 2
		name		=> '������',
		hp			=> 300,
		at			=> 250,
		df			=> 250,
		ag			=> 250,
		get_exp		=> 66,
		get_money	=> 66,
		icon		=> 'mon/162.gif',
		
		old_sp		=> 20,
		job			=> 36, # ���̂܂ˎt
		sp			=> 999,
		mp			=> 362,
		tmp			=> '������',
	},
	{ # 3
		name		=> '��Ų�',
		hp			=> 380,
		at			=> 390,
		df			=> 280,
		ag			=> 100,
		get_exp		=> 96,
		get_money	=> 46,
		icon		=> 'mon/163.gif',
		
		old_sp		=> 20,
		job			=> 1, # ��m
		sp			=> 999,
		mp			=> 101,
		tmp			=> '�U����',
	},
	{ # 4
		name		=> '�����',
		hp			=> 350,
		at			=> 280,
		df			=> 250,
		ag			=> 90,
		get_exp		=> 96,
		get_money	=> 46,
		icon		=> 'mon/164.gif',
		
		old_job		=> 94, # ���K���e
		old_sp		=> 20,
		job			=> 31, # �����m���΂�
		sp			=> 20,
		mp			=> 155,
		state		=> '����'
	},
	{ # 5
		name		=> '���޸�',
		hp			=> 240,
		at			=> 270,
		df			=> 400,
		ag			=> 160,
		get_exp		=> 88,
		get_money	=> 88,
		icon		=> 'mon/165.gif',
		
		old_sp		=> 20,
		job			=> 58, # �ް����
		sp			=> 999,
		mp			=> 400,
		tmp			=> '���y��',
	},
);



1;
