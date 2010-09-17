# ��̒��g
@treasures = (
[10..18], # ����No
[10..23], # �h��No
[15..26,15..26,33,72..86], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '�ײ�A',
		hp			=> 150,
		at			=> 120,
		df			=> 20,
		ag			=> 100,
		get_exp		=> 30,
		get_money	=> 10,
		icon		=> 'mon/002.gif',
		
		job			=> 29, # �������m�X���E�A�w�C�X�g
		sp			=> 20,
		mp			=> 91,
	},
	{
		name		=> '�ײ�B',
		hp			=> 150,
		at			=> 120,
		df			=> 20,
		ag			=> 100,
		get_exp		=> 30,
		get_money	=> 10,
		icon		=> 'mon/002.gif',
		
		job			=> 15, # �������m�|�C�Y���A�t�@�C�A�A�X���v���A���t���N�A�A�X�s��
		sp			=> 80,
		mp			=> 91,
	},
	{
		name		=> '�ݸ޽ײ�',
		hp			=> 3000,
		at			=> 200,
		df			=> 150,
		ag			=> 120,
		get_exp		=> 500,
		get_money	=> 400,
		icon		=> 'mon/516.gif',
		
		old_sp		=> 20,
		hit			=> 150, # ������p������150%
		job			=> 21, # ����m����������
		sp			=> 5,
		mp			=> 400,
		tmp			=> '�U����',
	},
	{
		name		=> '�ײ�C',
		hp			=> 150,
		at			=> 120,
		df			=> 20,
		ag			=> 100,
		get_exp		=> 30,
		get_money	=> 10,
		icon		=> 'mon/002.gif',
		
		job			=> 16, # �������m�P�A���A���C�u���A�T�C���X�A�P�A�����A�R���t�F�A�V�F��
		sp			=> 70,
		mp			=> 91,
	},
	{
		name		=> '�ײ�D',
		hp			=> 150,
		at			=> 120,
		df			=> 20,
		ag			=> 100,
		get_exp		=> 30,
		get_money	=> 10,
		icon		=> 'mon/002.gif',
		
		job			=> 30, # �Ԗ����m�P�A���A�V�F���A�|�C�Y���A�t�@�C�A�A���t���N
		sp			=> 90,
		mp			=> 91,
	},
);

# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = (0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,11,11,12,13,14,15);


# �����X�^�[
@monsters = (
	{ # 0
		name		=> '����ײ�',
		hp			=> 77,
		at			=> 77,
		df			=> 77,
		ag			=> 77,
		get_exp		=> 22,
		get_money	=> 22,
		icon		=> 'mon/001.gif',
		old_sp		=> 20,
	},
	{ # 1
		name		=> '�ײ�',
		hp			=> 90,
		at			=> 90,
		df			=> 40,
		ag			=> 90,
		get_exp		=> 25,
		get_money	=> 20,
		icon		=> 'mon/002.gif',
		old_sp		=> 20,

		job			=> 59, # �ײ�ײ�ް ��т���
		sp			=> 10,
		mp			=> 30,
	},
	{ # 2
		name		=> '�ײ��޽',
		hp			=> 100,
		at			=> 105,
		df			=> 30,
		ag			=> 100,
		get_exp		=> 28,
		get_money	=> 24,
		icon		=> 'mon/003.gif',
		old_sp		=> 20,
	},
	{ # 3
		name		=> '����ٽײ�',
		hp			=> 140,
		at			=> 120,
		df			=> 50,
		ag			=> 70,
		get_exp		=> 35,
		get_money	=> 10,
		icon		=> 'mon/020.gif',

		job			=> 90, # �ǂ����������A�|�C�Y��
		sp			=> 20,
		mp			=> 32,
	},
	{ # 4
		name		=> 'βнײ�',
		hp			=> 100,
		at			=> 90,
		df			=> 30,
		ag			=> 100,
		get_exp		=> 30,
		get_money	=> 15,
		icon		=> 'mon/010.gif',

		job			=> 5, # �m���X�J���A�L�A���[�A�z�C�~
		sp			=> 6,
		mp			=> 45,
	},
	{ # 5
		name		=> '���т�׹�',
		hp			=> 120,
		at			=> 126,
		df			=> 42,
		ag			=> 65,
		get_exp		=> 36,
		get_money	=> 11,
		icon		=> 'mon/012.gif',

		job			=> 91, # �܂Ђ��������A���тꂤ��
		sp			=> 20,
		mp			=> 31,
	},
	{ # 6
		name		=> '�ײт܂ǂ�',
		hp			=> 110,
		at			=> 85,
		df			=> 30,
		ag			=> 100,
		get_exp		=> 34,
		get_money	=> 21,
		icon		=> 'mon/013.gif',

		job			=> 19, # �Ŗ����m���J�i��,�}�z�J���^,���_�p�j
		sp			=> 16,
		mp			=> 84,
	},
	{ # 7
		name		=> '�ײтނ�',
		hp			=> 60,
		at			=> 90,
		df			=> 130,
		ag			=> 40,
		get_exp		=> 32,
		get_money	=> 27,
		icon		=> 'mon/015.gif',

		job			=> 39, # �ײуM���X�N���g
		sp			=> 7,
		mp			=> 43,
	},
	{ # 8
		name		=> '̧����ײ�',
		hp			=> 125,
		at			=> 125,
		df			=> 85,
		ag			=> 75,
		get_exp		=> 40,
		get_money	=> 25,
		icon		=> 'mon/008.gif',

		job			=> 12, # �����g���Ђ̂���
		sp			=> 5,
		mp			=> 15,
	},
	{ # 9
		name		=> '�ײ��ޯ�',
		hp			=> 100,
		at			=> 115,
		df			=> 20,
		ag			=> 155,
		get_exp		=> 41,
		get_money	=> 11,
		icon		=> 'mon/027.gif',
		
		job			=> 38, # ����߲����イ���A�A�X�s��
		sp			=> 20,
		mp			=> 44,
	},
	{ # 10
		name		=> '���Ͻײ�',
		hp			=> 150,
		at			=> 90,
		df			=> 30,
		ag			=> 120,
		get_exp		=> 40,
		get_money	=> 30,
		icon		=> 'mon/011.gif',

		job			=> 5, # �m��
		sp			=> 999,
		mp			=> 99,
	},
	{ # 11
		name		=> 'ϸ�Ͻײ�',
		hp			=> 90,
		at			=> 148,
		df			=> 140,
		ag			=> 50,
		get_exp		=> 38,
		get_money	=> 31,
		icon		=> 'mon/021.gif',

		job			=> 7, # ���l�܂���������߂�
		sp			=> 3,
		mp			=> 10,
	},
	{ # 12
		name		=> '�ޯ��ײ�',
		hp			=> 300,
		at			=> 145,
		df			=> 10,
		ag			=> 40,
		get_exp		=> 40,
		get_money	=> 30,
		icon		=> 'mon/006.gif',
	},
	{ # 13
		name		=> '�ײ�̧׵',
		hp			=> 444,
		at			=> 144,
		df			=> 144,
		ag			=> 144,
		get_exp		=> 144,
		get_money	=> 144,
		icon		=> 'mon/234.gif',

		job			=> 19, # �Ŗ����m���J�i���A�}�z�J���^�A���_�p�j�A�U�L�A�}�z�g�[���A�x�M���S��
		sp			=> 60,
		mp			=> 144,
	},
	{ # 14
		name		=> '��ٽײ�',
		hp			=> 8,
		at			=> 70,
		df			=> 2500,
		ag			=> 1500,
		get_exp		=> 250,
		get_money	=> 10,
		icon		=> 'mon/004.gif',

		job			=> 39, # �X���C���M��
		sp			=> 3,
		old_job		=> 99, # ������
		old_sp		=> 0,
		mp			=> 31,
		tmp			=> '������',
	},
	{ # 15
		name		=> 'ʸ�����',
		hp			=> 14,
		at			=> 110,
		df			=> 4000,
		ag			=> 2000,
		get_exp		=> 1500,
		get_money	=> 30,
		icon		=> 'mon/022.gif',

		job			=> 40, # ʸ����ك����~
		sp			=> 25,
		old_job		=> 99, # ������
		old_sp		=> 0,
		mp			=> 61,
		tmp			=> '������',
	},
);



1;
