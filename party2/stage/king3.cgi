# �ݒ�
%k = (
	p_name		=> '@�S�Ă�j�󂷂��@',# �N�G�X�g��
	p_join		=> 6,					# �퓬�Q�����(�l)
	p_leader	=> '�����̏�',			# �N�G�X�g���[�_�[��
	speed		=> 12,					# �i�s�X�s�[�h(�b)
	need_join	=> 'hp_300_o',			# �Q������(./lib/quest.cgi 192�s�ڂ�������Q�l)
);

# �����험�i(����No)
@treasures = (
[], # ����No
[], # �h��No
[59,59,71,71], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '�����̏�',
		hp			=> 160000,
		at			=> 100,
		df			=> 100,
		ag			=> 700,
		get_exp		=> 5000,
		get_money	=> 5000,
		icon		=> 'mon/615.gif',
		
		job			=> 98, # �����@�^
		sp			=> 999,
		old_job		=> 95, # ����
		old_sp		=> 999,
		mmp			=> 999999,
		mp			=> 99999,
		tmp			=> '������',
	},
);


# ��������郂���X�^�[
@monsters = (
	{
		name		=> '�ꌫ��',
		hp			=> 250,
		at			=> 100,
		df			=> 60,
		ag			=> 300,
		get_exp		=> 70,
		get_money	=> 150,
		icon		=> 'mon/508.gif',

		job			=> 51, # �������m
		sp			=> 999,
		old_job		=> 16, # �������m
		old_sp		=> 999,
		mp			=> 399,
		tmp			=> '������',
	},
	{
		name		=> '�񌫎�',
		hp			=> 250,
		at			=> 100,
		df			=> 60,
		ag			=> 300,
		get_exp		=> 70,
		get_money	=> 150,
		icon		=> 'mon/507.gif',
		
		job			=> 15, # �������m
		sp			=> 999,
		old_job		=> 40, # ʸ�����
		old_sp		=> 999,
		mp			=> 299,
		tmp			=> '���z��',
	},
	{
		name		=> '�O����',
		hp			=> 250,
		at			=> 100,
		df			=> 60,
		ag			=> 300,
		get_exp		=> 70,
		get_money	=> 150,
		icon		=> 'mon/509.gif',
		
		job			=> 6, # ���@�g��
		sp			=> 999,
		old_job		=> 19, # �Ŗ����m
		old_sp		=> 999,
		mp			=> 399,
		tmp			=> '������',
	},
	{
		name		=> '�l����',
		hp			=> 250,
		at			=> 100,
		df			=> 60,
		ag			=> 300,
		get_exp		=> 70,
		get_money	=> 150,
		icon		=> 'mon/511.gif',

		job			=> 33, # ����
		sp			=> 999,
		old_job		=> 30, # �Ԗ����m
		old_sp		=> 999,
		mp			=> 399,
		tmp			=> '������',
	},
	{
		name		=> '��',
		hp			=> 400,
		at			=> 200,
		df			=> 100,
		ag			=> 400,
		get_exp		=> 70,
		get_money	=> 150,
		icon		=> 'mon/250.gif',

		job			=> 31, # �����m
		sp			=> 999,
		old_job		=> 95, # ����
		old_sp		=> 999,
		mp			=> 299,
		tmp			=> '���z��',
	},
	{
		name		=> '����',
		hp			=> 320,
		at			=> 120,
		df			=> 60,
		ag			=> 300,
		get_exp		=> 80,
		get_money	=> 160,
		icon		=> 'mon/254.gif',

		job			=> 15, # �������m
		sp			=> 999,
		old_job		=> 95, # ����
		old_sp		=> 999,
		mp			=> 301,
		tmp			=> '������',
	},
	{
		name		=> '����',
		hp			=> 350,
		at			=> 500,
		df			=> 200,
		ag			=> 500,
		get_exp		=> 66,
		get_money	=> 66,
		icon		=> 'mon/245.gif',

		job			=> 56, # ���ް��
		sp			=> 999,
		old_job		=> 95, # ����
		old_sp		=> 999,
		mp			=> 301,
		state		=> '����',
	},
	{
		name		=> '�ײт܂ǂ�',
		hp			=> 260,
		at			=> 180,
		df			=> 50,
		ag			=> 400,
		get_exp		=> 100,
		get_money	=> 150,
		icon		=> 'mon/013.gif',
		job			=> 19, # �Ŗ����m
		sp			=> 999,
		old_job		=> 40, # ʸ�����
		old_sp		=> 999,
		mp			=> 384,
	},
);


1;
