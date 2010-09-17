# ��̒��g
@treasures = (
[35..40], # ����No
[35..40], # �h��No
[59,59,59,59,59], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '����',
		hp			=> 14000,
		at			=> 650,
		df			=> 350,
		ag			=> 200,
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
		name		=> '�����̨�',
		hp			=> 15000,
		at			=> 750,
		df			=> 400,
		ag			=> 400,
		get_exp		=> 5000,
		get_money	=> 3000,
		icon		=> 'mon/801.gif',
		
		hit			=> 500, # ������p������500%
		job			=> 97, # ���U���^
		sp			=> 999,
		old_job		=> 47, # �ټެ�
		old_sp		=> 999,
		mmp			=> 30000,
		mp			=> 8000,
		ten			=> 8,
	},
	{
		name		=> '���_',
		hp			=> 14000,
		at			=> 600,
		df			=> 250,
		ag			=> 999,
		get_exp		=> 2000,
		get_money	=> 1500,
		icon		=> 'mon/702.gif',
		
		hit			=> 250, # ������p������200%
		job			=> 19, # �Ŗ����m
		sp			=> 999,
		old_job		=> 46, # �ެ���װ
		old_sp		=> 999,
		mmp			=> 14000,
		mp			=> 5000,
		tmp			=> '������',
	},
);

# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = ();


# �����X�^�[
@monsters = (
	{
		name		=> '�ޯ��ײ�',
		hp			=> 500,
		at			=> 500,
		df			=> 100,
		ag			=> 500,
		get_exp		=> 120,
		get_money	=> 50,
		icon		=> 'mon/006.gif',
		old_sp		=> 20,
		tmp			=> '��',
	},
	{
		name		=> '�l�ʎ�',
		hp			=> 700,
		at			=> 550,
		df			=> 200,
		ag			=> 250,
		get_exp		=> 170,
		get_money	=> 140,
		icon		=> 'mon/503.gif',
		old_sp		=> 20,
		job			=> 7, # ���l
		sp			=> 999,
		mp			=> 263,
		tmp			=> '����',
	},
	{
		name		=> '�S�쌕�m',
		hp			=> 860,
		at			=> 650,
		df			=> 200,
		ag			=> 150,
		get_exp		=> 180,
		get_money	=> 80,
		icon		=> 'mon/500.gif',
		old_sp		=> 20,
		job			=> 2, # ���m
		sp			=> 999,
		mp			=> 343,
		tmp			=> '�U����',
	},
	{
		name		=> '�װ���',
		hp			=> 600,
		at			=> 700,
		df			=> 600,
		ag			=> 300,
		get_exp		=> 150,
		get_money	=> 300,
		icon		=> 'mon/215.gif',
		old_sp		=> 20,
		job			=> 1, # ��m
		sp			=> 999,
		mp			=> 452,
		tmp			=> '������',
	},
	{
		name		=> '����ټ��',
		hp			=> 1000,
		at			=> 500,
		df			=> 700,
		ag			=> 200,
		get_exp		=> 160,
		get_money	=> 500,
		icon		=> 'mon/506.gif',
		job			=> 5, # �m��
		old_sp		=> 30,
		sp			=> 999,
		mp			=> 600,
		tmp			=> '������',
	},
	{
		name		=> '�ް��',
		hp			=> 1200,
		at			=> 500,
		df			=> 700,
		ag			=> 150,
		get_exp		=> 250,
		get_money	=> 150,
		icon		=> 'mon/546.gif',
		old_sp		=> 30,
		job			=> 27, # �����m
		sp			=> 999,
		mp			=> 777,
		tmp			=> '�U�y��',
	},
	{
		name		=> '�ł̖��p�m',
		hp			=> 800,
		at			=> 450,
		df			=> 200,
		ag			=> 200,
		get_exp		=> 180,
		get_money	=> 260,
		icon		=> 'mon/510.gif',
		job			=> 40, # ʸ�����
		sp			=> 999,
		mp			=> 300,
		tmp			=> '���z��',
	},
	{
		name		=> '�޶��ý',
		hp			=> 909,
		at			=> 909,
		df			=> 100,
		ag			=> 100,
		get_exp		=> 200,
		get_money	=> 5,
		icon		=> 'mon/563.gif',
		old_sp		=> 20,
		job			=> 21, # ����m
		sp			=> 999,
		mp			=> 909,
		ten			=> 8,
	},
	{
		name		=> '�Ђ����ǂ�',
		hp			=> 1100,
		at			=> 530,
		df			=> 270,
		ag			=> 380,
		get_exp		=> 180,
		get_money	=> 180,
		icon		=> 'mon/530.gif',
		job			=> 26, # �E��
		sp			=> 999,
		old_job		=> 27, # �����t
		old_sp		=> 999,
		mp			=> 997,
		tmp			=> '���y��',
	},
	{
		name		=> '��˰ӽ',
		hp			=> 909,
		at			=> 777,
		df			=> 255,
		ag			=> 555,
		get_exp		=> 211,
		get_money	=> 99,
		icon		=> 'mon/553.gif',
		job			=> 23, # ���R�m
		sp			=> 999,
		old_job		=> 25, # �����N
		old_sp		=> 999,
		mp			=> 909,
		tmp			=> '��h��',
	},
	{
		name		=> '�ݸ޽ײ�',
		hp			=> 1200,
		at			=> 500,
		df			=> 300,
		ag			=> 500,
		get_exp		=> 200,
		get_money	=> 250,
		icon		=> 'mon/516.gif',
		old_sp		=> 20,
		job			=> 21, # ����m
		sp			=> 999,
		mp			=> 999,
		tmp			=> '�U����',
	},
	{
		name		=> '����̋R�m',
		hp			=> 1200,
		at			=> 666,
		df			=> 280,
		ag			=> 280,
		get_exp		=> 240,
		get_money	=> 170,
		icon		=> 'mon/566.gif',
		job			=> 24, # �����m
		sp			=> 999,
		old_job		=> 2, # ���m
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '�󗬂�',
	},
	{
		name		=> '����',
		hp			=> 1500,
		at			=> 750,
		df			=> 440,
		ag			=> 200,
		get_exp		=> 250,
		get_money	=> 200,
		icon		=> 'mon/560.gif',
		job			=> 41, # ��׺��
		sp			=> 999,
		old_job		=> 25, # �ݸ�A
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '������',
	},
);



1;
