# �ݒ�
%k = (
	p_join		=> 3,			# �퓬�Q�����(�l)
	need_join	=> '0',			# �Q������(./lib/quest.cgi 192�s�ڂ�������Q�l)
);

# �󕔉�(20�K�`30�K�ȏ�B��ʊK�قǊm���A�b�v)
$tresure_round = int(rand(11)+20);


# ��̒��g
@treasures = (
[], # ����No
[], # �h��No
[4..6,10..13,23,57,72..74,85..87,101..103], # ����No
);


# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = ();

# �����X�^�[
@monsters = (
	{
		name		=> 'گ�޽İ�',
		hp			=> 5,
		at			=> 200,
		df			=> 2000,
		ag			=> 500,
		get_exp		=> 50,
		get_money	=> 100,
		icon		=> 'mon/190.gif',
		
		job			=> 26, # �E��
		sp			=> 999,
		old_job		=> 6, # ���@�g��
		old_sp		=> 999,
		mmp			=> 99999,
		mp			=> 99,
		tmp			=> '������',
	},
	{
		name		=> '��ٰ�İ�',
		hp			=> 5,
		at			=> 200,
		df			=> 2000,
		ag			=> 500,
		get_exp		=> 50,
		get_money	=> 100,
		icon		=> 'mon/191.gif',
		
		job			=> 33, # ����
		sp			=> 130,
		old_job		=> 31, # �����m
		old_sp		=> 999,
		mmp			=> 99999,
		mp			=> 99,
		tmp			=> '������',
	},
	{
		name		=> '��۰�İ�',
		hp			=> 5,
		at			=> 200,
		df			=> 2000,
		ag			=> 500,
		get_exp		=> 50,
		get_money	=> 100,
		icon		=> 'mon/192.gif',
		
		job			=> 36, # ���̂܂ˎm
		sp			=> 999,
		old_job		=> 37, # ���E�m
		old_sp		=> 999,
		mmp			=> 99999,
		mp			=> 99,
		tmp			=> '������',
	},
	{
		name		=> '��ذݽİ�',
		hp			=> 5,
		at			=> 200,
		df			=> 2000,
		ag			=> 500,
		get_exp		=> 50,
		get_money	=> 100,
		icon		=> 'mon/193.gif',
		
		job			=> 90, # �ǂ����������A�|�C�Y���A�����ǂ��̂���
		sp			=> 999,
		old_job		=> 91, # �܂Ђ��������A���тꂤ���A�₫������
		old_sp		=> 999,
		mmp			=> 99999,
		mp			=> 99,
		tmp			=> '������',
	},
	{
		name		=> '�߰��ٽİ�',
		hp			=> 5,
		at			=> 200,
		df			=> 2000,
		ag			=> 500,
		get_exp		=> 50,
		get_money	=> 100,
		icon		=> 'mon/194.gif',
		
		job			=> 35, # ����
		sp			=> 999,
		old_job		=> 92, # �����z�[�A�˂ނ肱�������A���܂�����
		old_sp		=> 999,
		mmp			=> 99999,
		mp			=> 99,
		tmp			=> '������',
	},
	{
		name		=> '���ް�İ�',
		hp			=> 5,
		at			=> 200,
		df			=> 2000,
		ag			=> 500,
		get_exp		=> 50,
		get_money	=> 100,
		icon		=> 'mon/196.gif',
		
		job			=> 19, # �Ŗ����m
		sp			=> 999,
		old_job		=> 20, # ����
		old_sp		=> 999,
		mmp			=> 99999,
		mp			=> 99,
		tmp			=> '������',
	},
	{
		name		=> '��ׯ��İ�',
		hp			=> 5,
		at			=> 200,
		df			=> 2000,
		ag			=> 500,
		get_exp		=> 50,
		get_money	=> 100,
		icon		=> 'mon/195.gif',
		
		job			=> 58, # �ް����
		sp			=> 999,
		old_job		=> 53, # 峎t
		old_sp		=> 999,
		mmp			=> 99999,
		mp			=> 99,
		tmp			=> '������',
	},
	{
		name		=> '��ٽײ�',
		hp			=> 6,
		at			=> 200,
		df			=> 1000,
		ag			=> 500,
		get_exp		=> 200,
		get_money	=> 10,
		icon		=> 'mon/004.gif',

		job			=> 40, # ʸ�����
		sp			=> 999,
		old_job		=> 40, # ʸ�����
		old_sp		=> 999,
		mmp			=> 99999,
		mp			=> 180,
		tmp			=> '������',
	},
	{
		name		=> 'ʸ�����',
		hp			=> 10,
		at			=> 210,
		df			=> 2000,
		ag			=> 600,
		get_exp		=> 500,
		get_money	=> 20,
		icon		=> 'mon/022.gif',

		job			=> 40, # ʸ�����
		sp			=> 999,
		old_job		=> 40, # ʸ�����
		old_sp		=> 999,
		mmp			=> 99999,
		mp			=> 180,
		tmp			=> '������',
	},
);



1; # �폜�s��
