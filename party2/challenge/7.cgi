# �ݒ�
%k = (
	p_join		=> 1,			# �퓬�Q�����(�l)
	need_join	=> '0',			# �Q������(./lib/quest.cgi 192�s�ڂ�������Q�l)
);

# �󕔉�(30�K�`50�K�ȏ�B��ʊK�قǊm���A�b�v)
$tresure_round = int(rand(21)+30);


# ��̒��g
@treasures = (
[], # ����No
[], # �h��No
[5..6,10..13,23,57,72..74,85..87,101..103], # ����No
);


# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = ();

# �����X�^�[
@monsters = (
	{
		name		=> '�l�ʎ�',
		hp			=> 400,
		at			=> 350,
		df			=> 140,
		ag			=> 200,
		get_exp		=> 120,
		get_money	=> 100,
		icon		=> 'mon/503.gif',
		old_sp		=> 20,
		job			=> 7, # ���l
		sp			=> 999,
		mp			=> 123,
		tmp			=> '����',
	},
	{
		name		=> '�S�쌕�m',
		hp			=> 460,
		at			=> 400,
		df			=> 200,
		ag			=> 160,
		get_exp		=> 90,
		get_money	=> 40,
		icon		=> 'mon/500.gif',
		old_sp		=> 20,
		job			=> 2, # ���m
		sp			=> 999,
		mp			=> 93,
		tmp			=> '�U����',
	},
	{
		name		=> '����ټ��',
		hp			=> 300,
		at			=> 300,
		df			=> 450,
		ag			=> 100,
		get_exp		=> 80,
		get_money	=> 200,
		icon		=> 'mon/506.gif',
		job			=> 5, # �m��
		old_sp		=> 30,
		sp			=> 999,
		mp			=> 240,
		tmp			=> '������',
	},
	{
		name		=> '�ް��',
		hp			=> 500,
		at			=> 350,
		df			=> 350,
		ag			=> 100,
		get_exp		=> 150,
		get_money	=> 100,
		icon		=> 'mon/546.gif',
		old_sp		=> 30,
		job			=> 27, # �����m
		sp			=> 999,
		mp			=> 150,
		tmp			=> '�U�y��',
	},
	{
		name		=> '�ł̖��p�m',
		hp			=> 350,
		at			=> 250,
		df			=> 120,
		ag			=> 250,
		get_exp		=> 110,
		get_money	=> 180,
		icon		=> 'mon/510.gif',
		job			=> 40, # ʸ�����
		sp			=> 999,
		mp			=> 150,
		tmp			=> '���z��',
	},
	{
		name		=> '�޶��ý',
		hp			=> 700,
		at			=> 500,
		df			=> 100,
		ag			=> 100,
		get_exp		=> 150,
		get_money	=> 5,
		icon		=> 'mon/563.gif',
		old_sp		=> 20,
		job			=> 21, # ����m
		sp			=> 999,
		mp			=> 80,
		ten			=> 8,
	},
	{
		name		=> '�Ђ����ǂ�',
		hp			=> 480,
		at			=> 320,
		df			=> 160,
		ag			=> 280,
		get_exp		=> 100,
		get_money	=> 100,
		icon		=> 'mon/530.gif',
		job			=> 26, # �E��
		sp			=> 999,
		old_job		=> 27, # �����t
		old_sp		=> 999,
		mp			=> 297,
		tmp			=> '���y��',
	},
	{
		name		=> '��˰ӽ',
		hp			=> 555,
		at			=> 333,
		df			=> 155,
		ag			=> 222,
		get_exp		=> 133,
		get_money	=> 33,
		icon		=> 'mon/553.gif',
		job			=> 23, # ���R�m
		sp			=> 999,
		old_job		=> 25, # �����N
		old_sp		=> 999,
		mp			=> 120,
		tmp			=> '��h��',
	},
	{
		name		=> '�ݸ޽ײ�',
		hp			=> 500,
		at			=> 250,
		df			=> 100,
		ag			=> 250,
		get_exp		=> 150,
		get_money	=> 20,
		icon		=> 'mon/516.gif',
		old_sp		=> 20,
		job			=> 21, # ����m
		sp			=> 999,
		mp			=> 300,
		tmp			=> '��',
	},
	{
		name		=> '����̋R�m',
		hp			=> 610,
		at			=> 333,
		df			=> 180,
		ag			=> 180,
		get_exp		=> 190,
		get_money	=> 120,
		icon		=> 'mon/566.gif',
		job			=> 24, # �����m
		sp			=> 999,
		old_job		=> 2, # ���m
		old_sp		=> 999,
		mp			=> 220,
		tmp			=> '�󗬂�',
	},
	{
		name		=> '����',
		hp			=> 650,
		at			=> 300,
		df			=> 200,
		ag			=> 100,
		get_exp		=> 200,
		get_money	=> 50,
		icon		=> 'mon/560.gif',
		job			=> 41, # ��׺��
		sp			=> 999,
		old_job		=> 25, # �ݸ�A
		old_sp		=> 999,
		mp			=> 200,
		ten			=> 3,
	},
	{
		name		=> '�З��̓V�g',
		hp			=> 700,
		at			=> 300,
		df			=> 150,
		ag			=> 400,
		get_exp		=> 300,
		get_money	=> 100,
		icon		=> 'mon/569.gif',
		
		job			=> 98, # �����@�^
		sp			=> 999,
		old_job		=> 48, # �V�g
		old_sp		=> 999,
		mp			=> 999,
		ten			=> 3,
	},
	{
		name		=> '�ި���۽',
		hp			=> 750,
		at			=> 400,
		df			=> 200,
		ag			=> 200,
		get_exp		=> 300,
		get_money	=> 100,
		icon		=> 'mon/650.gif',
		
		job			=> 97, # ���U���^
		sp			=> 999,
		mp			=> 999,
		ten			=> 3,
	},
	{
		name		=> '��ϰ',
		hp			=> 600,
		at			=> 200,
		df			=> 250,
		ag			=> 250,
		get_exp		=> 300,
		get_money	=> 0,
		icon		=> 'mon/652.gif',
		
		job			=> 94, # ���K���e,�Q��
		sp			=> 20,
		old_job		=> 8, # �V�ѐl
		old_sp		=> 999,
		mp			=> 999,
		state		=> '�唚��',
		tmp			=> '���邼',
		ten			=> 3,
	},
);



1; # �폜�s��
