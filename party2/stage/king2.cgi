# �ݒ�
%k = (
	p_name		=> '@�S�Ă𑞂ގ�@',# �N�G�X�g��
	p_join		=> 6,				# �퓬�Q�����(�l)
	p_leader	=> '�Í���',		# �N�G�X�g���[�_�[��
	speed		=> 12,				# �i�s�X�s�[�h(�b)
	need_join	=> 'hp_400_o',		# �Q������(./lib/quest.cgi 192�s�ڂ�������Q�l)
);

# �����험�i(����No)
@treasures = (
[], # ����No
[], # �h��No
[59,59,59,59,71,104], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '�Í���',
		hp			=> 140000,
		at			=> 300,
		df			=> 200,
		ag			=> 0,
		get_exp		=> 8000,
		get_money	=> 5000,
		icon		=> 'mon/710.gif',
		
		hit			=> 900, # ������p������
		job			=> 0, # ���������A�Ă񂵂��A�ڂ�����
		sp			=> 999,
		old_job		=> 101, # ����&�z��
		old_sp		=> 999,
		mmp			=> 999999,
		mp			=> 99999,
		tmp			=> '�󗬂�',
	},
);


# ��������郂���X�^�[
@monsters = (
	{
		name		=> '����',
		hp			=> 600,
		at			=> 550,
		df			=> 400,
		ag			=> 100,
		get_exp		=> 250,
		get_money	=> 100,
		icon		=> 'mon/560.gif',
		job			=> 41, # ��׺��
		sp			=> 999,
		old_job		=> 25, # �ݸ�A
		old_sp		=> 999,
		mp			=> 299,
		tmp			=> '������',
	},
	{
		name		=> '�Η�',
		hp			=> 600,
		at			=> 550,
		df			=> 400,
		ag			=> 100,
		get_exp		=> 250,
		get_money	=> 100,
		icon		=> 'mon/561.gif',
		job			=> 35, # ����
		sp			=> 999,
		old_job		=> 91, # ��჌n
		old_sp		=> 999,
		mp			=> 299,
		tmp			=> '������',
	},
	{
		name		=> '����',
		hp			=> 600,
		at			=> 550,
		df			=> 400,
		ag			=> 100,
		get_exp		=> 250,
		get_money	=> 100,
		icon		=> 'mon/562.gif',
		job			=> 41, # ��׺��
		sp			=> 999,
		old_job		=> 27, # �����m
		old_sp		=> 999,
		mp			=> 299,
		tmp			=> '������',
	},
	{
		name		=> '��˰ӽ',
		hp			=> 480,
		at			=> 500,
		df			=> 240,
		ag			=> 400,
		get_exp		=> 240,
		get_money	=> 90,
		icon		=> 'mon/553.gif',
		job			=> 23, # ���R�m
		sp			=> 999,
		old_job		=> 25, # �����N
		old_sp		=> 999,
		mp			=> 209,
		tmp			=> '��h��',
	},
	{
		name		=> '�ݸ���˰ӽ',
		hp			=> 540,
		at			=> 500,
		df			=> 240,
		ag			=> 400,
		get_exp		=> 240,
		get_money	=> 90,
		icon		=> 'mon/554.gif',
		job			=> 21, # ����m
		sp			=> 999,
		old_job		=> 25, # �����N
		old_sp		=> 999,
		mp			=> 209,
		tmp			=> '�U����',
	},
	{
		name		=> '��ذ�',
		hp			=> 540,
		at			=> 500,
		df			=> 240,
		ag			=> 400,
		get_exp		=> 240,
		get_money	=> 90,
		icon		=> 'mon/555.gif',
		job			=> 70, # �V���l�߂������h���S���p���[�M�K�f�C��
		sp			=> 150,
		old_job		=> 52, # ���l
		old_sp		=> 999,
		mp			=> 209,
		tmp			=> '�U����',
	},
	{
		name		=> '��׺��ϯ�',
		hp			=> 480,
		at			=> 600,
		df			=> 360,
		ag			=> 150,
		get_exp		=> 200,
		get_money	=> 100,
		icon		=> 'mon/556.gif',
		old_sp		=> 20,
		job			=> 41, # ��׺��
		sp			=> 999,
		mp			=> 99,
		tmp			=> '�󗬂�',
	},
	{
		name		=> '��׺�ݿ����',
		hp			=> 560,
		at			=> 520,
		df			=> 300,
		ag			=> 120,
		get_exp		=> 255,
		get_money	=> 100,
		icon		=> 'mon/557.gif',
		job			=> 58, # �ް����
		sp			=> 999,
		old_job		=> 52, # ���l
		old_sp		=> 999,
		mp			=> 192,
		tmp			=> '����',
	},
);


1;
