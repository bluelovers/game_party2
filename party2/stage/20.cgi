# ��̒��g
@treasures = (
[29..40], # ����No
[35..40], # �h��No
[59,59,59,59], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '���ް�İ�',
		hp			=> 20,
		at			=> 500,
		df			=> 8000,
		ag			=> 3000,
		get_exp		=> 100,
		get_money	=> 1000,
		icon		=> 'mon/196.gif',
		
		job			=> 51, # �������m
		sp			=> 999,
		old_job		=> 54, # ���e�m
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '������',
	},
	{
		name		=> '�З��̓V�g',
		hp			=> 12000,
		at			=> 500,
		df			=> 300,
		ag			=> 300,
		get_exp		=> 3000,
		get_money	=> 2000,
		icon		=> 'mon/569.gif',
		
		hit			=> 500, # ������p������
		job			=> 98, # �����@�^
		sp			=> 999,
		old_job		=> 48, # �V�g
		old_sp		=> 999,
		mmp			=> 30000,
		mp			=> 8000,
		tmp			=> '������',
	},
	{
		name		=> '��ׯ��İ�',
		hp			=> 20,
		at			=> 500,
		df			=> 8000,
		ag			=> 3000,
		get_exp		=> 100,
		get_money	=> 1000,
		icon		=> 'mon/195.gif',
		
		job			=> 58, # �ް����
		sp			=> 999,
		old_job		=> 53, # 峎t
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '������',
	},
);

# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = ();


# �����X�^�[
@monsters = (
	{
		name		=> '�V�L��',
		hp			=> 400,
		at			=> 400,
		df			=> 200,
		ag			=> 400,
		get_exp		=> 100,
		get_money	=> 100,
		icon		=> 'mon/640.gif',

		job			=> 10, # �r�g��
		sp			=> 999,
		old_job		=> 32, # �����m
		old_sp		=> 999,
		mp			=> 199,
	},
	{
		name		=> '�V�L��',
		hp			=> 400,
		at			=> 400,
		df			=> 200,
		ag			=> 400,
		get_exp		=> 100,
		get_money	=> 100,
		icon		=> 'mon/641.gif',

		job			=> 48, # �V�g
		sp			=> 999,
		old_job		=> 30, # �Ԗ����m
		old_sp		=> 999,
		mp			=> 199,
	},
	{
		name		=> '�V�L��',
		hp			=> 400,
		at			=> 400,
		df			=> 200,
		ag			=> 400,
		get_exp		=> 100,
		get_money	=> 100,
		icon		=> 'mon/642.gif',

		job			=> 44, # �����
		sp			=> 999,
		old_job		=> 40, # ʸ�����
		old_sp		=> 999,
		mp			=> 199,
	},
	{
		name		=> '�V��',
		hp			=> 500,
		at			=> 350,
		df			=> 400,
		ag			=> 150,
		get_exp		=> 150,
		get_money	=> 120,
		icon		=> 'mon/630.gif',

		job			=> 18, # �V�g
		sp			=> 999,
		old_job		=> 45, # Ӱ���
		old_sp		=> 999,
		mp			=> 164,
	},
);



1;
