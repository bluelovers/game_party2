# �ݒ�
%k = (
	p_name		=> '@�S�Ă𔚔��������@',	# �N�G�X�g��
	p_join		=> 6,						# �퓬�Q�����(�l)
	p_leader	=> '��ϰ',					# �N�G�X�g���[�_�[��
	speed		=> 12,						# �i�s�X�s�[�h(�b)
	need_join	=> 'hp_200_o',				# �Q������(./lib/quest.cgi 192�s�ڂ�������Q�l)
);


# �����험�i(����No)
@treasures = (
[], # ����No
[3], # �h��No
[42,58,58,57..59,57..59], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '��ϰ',
		hp			=> 60000,
		at			=> 450,
		df			=> 250,
		ag			=> 150,
		get_exp		=> 5000,
		get_money	=> 1,
		icon		=> 'mon/652.gif',
		
		job			=> 8, # �V�ѐl
		sp			=> 999,
		old_job		=> 95, # ����
		old_sp		=> 999,
		mmp			=> 999999,
		mp			=> 99999,
		state		=> '�唚��',
		tmp			=> '���邼',
	},
);


# ��������郂���X�^�[
@monsters = (
	{
		name		=> '���e��',
		hp			=> 150,
		at			=> 300,
		df			=> 300,
		ag			=> 50,
		get_exp		=> 90,
		get_money	=> 5,
		icon		=> 'mon/080.gif',

		job			=> 94, # �������K���e�A�˂�
		sp			=> 20,
		old_sp		=> 30, # �Ă񂵂��,�ڂ�����
		mp			=> 42,
	},
	{
		name		=> '���e��',
		hp			=> 300,
		at			=> 400,
		df			=> 300,
		ag			=> 100,
		get_exp		=> 180,
		get_money	=> 20,
		icon		=> 'mon/579.gif',

		job			=> 94, # �������K���e�A�˂�
		sp			=> 20,
		old_sp		=> 30, # �Ă񂵂��,�ڂ�����
		mp			=> 42,
	},
	{
		name		=> '���',
		hp			=> 200,
		at			=> 350,
		df			=> 60,
		ag			=> 400,
		get_exp		=> 100,
		get_money	=> 50,
		icon		=> 'mon/071.gif',

		job			=> 31, # �����m���΂�
		sp			=> 20,
		old_sp		=> 30, # �Ă񂵂��,�ڂ�����
		mp			=> 42,
	},
	{
		name		=> '�ޯ����',
		hp			=> 400,
		at			=> 450,
		df			=> 120,
		ag			=> 280,
		get_exp		=> 200,
		get_money	=> 100,
		icon		=> 'mon/577.gif',

		job			=> 31, # �����m���΂�
		sp			=> 20,
		old_sp		=> 30, # �Ă񂵂��,�ڂ�����
		mp			=> 42,
	},
	{
		name		=> '������',
		hp			=> 50,
		at			=> 300,
		df			=> 900,
		ag			=> 900,
		get_exp		=> 100,
		get_money	=> 1,
		icon		=> 'mon/208.gif',

		job			=> 94, # �������K���e�A�˂�
		sp			=> 20,
		old_sp		=> 30, # �Ă񂵂��,�ڂ�����
		mp			=> 42,
		tmp			=> '������',
	},
	{
		name		=> '�װ���',
		hp			=> 100,
		at			=> 400,
		df			=> 700,
		ag			=> 900,
		get_exp		=> 150,
		get_money	=> 10,
		icon		=> 'mon/209.gif',

		job			=> 94, # �������K���e�A�˂�
		sp			=> 20,
		old_sp		=> 30, # �Ă񂵂��,�ڂ�����
		mp			=> 42,
	},
);




1;
