# ��̒��g
@treasures = (
[18..28,33..37], # ����No
[18..31,36..38], # �h��No
[4..6,13,28,29,37,38,40,40,57,60..65,87,104..107], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '�����߽A',
		hp			=> 5000,
		at			=> 600,
		df			=> 50,
		ag			=> 100,
		get_exp		=> 500,
		get_money	=> 10,
		icon		=> 'mon/565.gif',
		old_sp		=> 20,
		job			=> 1, # ��m
		sp			=> 999,
		old_job		=> 52, # ���l
		mp			=> 999,
		tmp			=> '�U����',
	},
	{
		name		=> 'Ųĺް��',
		hp			=> 8000,
		at			=> 560,
		df			=> 400,
		ag			=> 200,
		get_exp		=> 1600,
		get_money	=> 200,
		icon		=> 'mon/701.gif',
		
		old_sp		=> 20,
		hit			=> 500, # ������p������
		job			=> 97, # ���U���^
		sp			=> 999,
		mmp			=> 99999,
		mp			=> 4999,
		tmp			=> '�U����',
	},
	{
		name		=> '�����߽B',
		hp			=> 5000,
		at			=> 600,
		df			=> 50,
		ag			=> 100,
		get_exp		=> 500,
		get_money	=> 10,
		icon		=> 'mon/565.gif',
		old_sp		=> 20,
		job			=> 24, # �����m
		sp			=> 999,
		old_job		=> 21, # ����m
		mp			=> 999,
		tmp			=> '�U����',
	},
);

# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = ();

# �����X�^�[
@monsters = (
	{
		name		=> '�ݸ���˰ӽ',
		hp			=> 600,
		at			=> 350,
		df			=> 200,
		ag			=> 160,
		get_exp		=> 150,
		get_money	=> 100,
		icon		=> 'mon/554.gif',
		old_sp		=> 20,
		job			=> 21, # ����m
		sp			=> 999,
		mp			=> 149,
		state		=> '����',
	},
	{
		name		=> '����߽',
		hp			=> 700,
		at			=> 500,
		df			=> 50,
		ag			=> 100,
		get_exp		=> 170,
		get_money	=> 10,
		icon		=> 'mon/564.gif',
		old_sp		=> 20,
		job			=> 1, # ��m
		sp			=> 999,
		old_job		=> 21, # ����m
		mp			=> 999,
		state		=> '����',
	},
	{
		name		=> '�İݺް��',
		hp			=> 500,
		at			=> 350,
		df			=> 500,
		ag			=> 100,
		get_exp		=> 150,
		get_money	=> 250,
		icon		=> 'mon/547.gif',

		old_sp		=> 30,
		job			=> 3, # �R�m
		sp			=> 999,
		mp			=> 155,
		state		=> '����',
	},
	{
		name		=> '�װŲ�',
		hp			=> 300,
		at			=> 300,
		df			=> 300,
		ag			=> 300,
		get_exp		=> 100,
		get_money	=> 100,
		icon		=> 'mon/520.gif',

		job			=> 36, # ���̂܂ˎm
		sp			=> 999,
		mp			=> 94,
		state		=> '����',
	},
	{
		name		=> '�װϼ�',
		hp			=> 444,
		at			=> 333,
		df			=> 66,
		ag			=> 66,
		get_exp		=> 96,
		get_money	=> 96,
		icon		=> 'mon/521.gif',
		
		job			=> 24, # �����m
		sp			=> 999,
		old_job		=> 11, # �|�g��
		old_sp		=> 999,
		mp			=> 333,
		state		=> '����',
	},
	{
		name		=> '�����l',
		hp			=> 480,
		at			=> 370,
		df			=> 80,
		ag			=> 50,
		get_exp		=> 145,
		get_money	=> 50,
		icon		=> 'mon/523.gif',
		
		old_sp		=> 20,
		job			=> 23, # ���R�m
		sp			=> 999,
		mp			=> 285,
		state		=> '����',
	},
	{
		name		=> '�޽ϼ�',
		hp			=> 555,
		at			=> 333,
		df			=> 111,
		ag			=> 111,
		get_exp		=> 111,
		get_money	=> 111,
		icon		=> 'mon/522.gif',

		job			=> 24, # �����m
		sp			=> 999,
		old_job		=> 11, # �|�g��
		old_sp		=> 999,
		mp			=> 111,
		state		=> '����',
	},
	{
		name		=> '���R�m',
		hp			=> 400,
		at			=> 350,
		df			=> 300,
		ag			=> 250,
		get_exp		=> 150,
		get_money	=> 100,
		icon		=> 'mon/501.gif',

		job			=> 54, # ���e�m
		sp			=> 999,
		old_job		=> 17, # ���R�m
		old_sp		=> 999,
		mp			=> 200,
		state		=> '����',
	},
	{
		name		=> '���R�m',
		hp			=> 380,
		at			=> 370,
		df			=> 360,
		ag			=> 350,
		get_exp		=> 140,
		get_money	=> 130,
		icon		=> 'mon/502.gif',

		job			=> 53, # 峎t
		sp			=> 999,
		old_job		=> 49, # ���܂˂����m
		old_sp		=> 999,
		mp			=> 320,
		state		=> '����',
	},
);




1; # �폜�s��
