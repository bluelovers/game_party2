# �ݒ�
%k = (
	p_name		=> '@�S�Ă𖳂Ɋ҂���@',# �N�G�X�g��
	p_join		=> 6,					# �퓬�Q�����(�l)
	p_leader	=> '�j��_',			# �N�G�X�g���[�_�[��
	speed		=> 12,					# �i�s�X�s�[�h(�b)
	need_join	=> 'hp_400_o',			# �Q������(./lib/quest.cgi 192�s�ڂ�������Q�l)
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
		name		=> 'گ�޽İ�',
		hp			=> 50,
		at			=> 400,
		df			=> 9000,
		ag			=> 3000,
		get_exp		=> 1000,
		get_money	=> 2000,
		icon		=> 'mon/190.gif',
		
		job			=> 26, # �E��
		sp			=> 999,
		old_job		=> 6, # ���@�g��
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '������',
	},
	{
		name		=> '��ٰ�İ�',
		hp			=> 50,
		at			=> 500,
		df			=> 9000,
		ag			=> 3000,
		get_exp		=> 1000,
		get_money	=> 2000,
		icon		=> 'mon/191.gif',
		
		job			=> 33, # ����
		sp			=> 130,
		old_job		=> 31, # �����m
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '������',
	},
	{
		name		=> '��۰�İ�',
		hp			=> 50,
		at			=> 500,
		df			=> 9000,
		ag			=> 3000,
		get_exp		=> 1000,
		get_money	=> 2000,
		icon		=> 'mon/192.gif',
		
		job			=> 36, # ���̂܂ˎm
		sp			=> 999,
		old_job		=> 37, # ���E�m
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '������',
	},
	{
		name		=> '�j��_',
		hp			=> 150000,
		at			=> 600,
		df			=> 300,
		ag			=> 300,
		get_exp		=> 10000,
		get_money	=> 5000,
		icon		=> 'mon/850.gif',
		
		hit			=> 2000, # ������p������
		job			=> 97, # ���U���n
		sp			=> 999,
		mmp			=> 9999999,
		mp			=> 999999,
		tmp			=> '�U�y��',
	},
	{
		name		=> '��ذݽİ�',
		hp			=> 50,
		at			=> 500,
		df			=> 9000,
		ag			=> 3000,
		get_exp		=> 1000,
		get_money	=> 2000,
		icon		=> 'mon/193.gif',
		
		job			=> 90, # �ǂ����������A�|�C�Y���A�����ǂ��̂���
		sp			=> 999,
		old_job		=> 91, # �܂Ђ��������A���тꂤ���A�₫������
		old_sp		=> 999,
		mmp			=> 999999,
		mp			=> 99999,
		tmp			=> '������',
	},
	{
		name		=> '�߰��ٽİ�',
		hp			=> 50,
		at			=> 500,
		df			=> 9000,
		ag			=> 3000,
		get_exp		=> 1000,
		get_money	=> 2000,
		icon		=> 'mon/194.gif',
		
		job			=> 35, # ����
		sp			=> 999,
		old_job		=> 92, # �����z�[�A�˂ނ肱�������A���܂�����
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '������',
	},
	{
		name		=> '���ް�İ�',
		hp			=> 50,
		at			=> 500,
		df			=> 9000,
		ag			=> 3000,
		get_exp		=> 500,
		get_money	=> 2000,
		icon		=> 'mon/196.gif',
		
		job			=> 19, # �Ŗ����m
		sp			=> 999,
		old_job		=> 20, # ����
		old_sp		=> 999,
		mmp			=> 999999,
		mp			=> 99999,
		tmp			=> '������',
	},
);



1;
