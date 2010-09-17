# ��̒��g
@treasures = (
[24..28,33..37], # ����No
[24..31,36..38], # �h��No
[4..6,12,21..23,23,28,29,36,39,40,87,109], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '��ׯ��İ�',
		hp			=> 20,
		at			=> 250,
		df			=> 6000,
		ag			=> 2000,
		get_exp		=> 100,
		get_money	=> 800,
		icon		=> 'mon/195.gif',
		
		job			=> 19, # �Ŗ����m
		sp			=> 999,
		old_job		=> 20, # ����
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '������',
	},
	{
		name		=> '���_',
		hp			=> 12000,
		at			=> 360,
		df			=> 180,
		ag			=> 240,
		get_exp		=> 2000,
		get_money	=> 1500,
		icon		=> 'mon/702.gif',
		
		hit			=> 250, # ������p������200%
		job			=> 19, # �Ŗ����m
		sp			=> 70,
		old_job		=> 46, # �ެ���װ
		old_sp		=> 999,
		mmp			=> 14000,
		mp			=> 5000,
		tmp			=> '������',
	},
	{
		name		=> '��ٰ�İ�',
		hp			=> 20,
		at			=> 250,
		df			=> 6000,
		ag			=> 2000,
		get_exp		=> 100,
		get_money	=> 800,
		icon		=> 'mon/191.gif',
		
		job			=> 33, # ����
		sp			=> 130,
		old_job		=> 31, # �����m
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '������',
	},
);

# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = ();


# �����X�^�[
@monsters = (
	{ # 0
		name		=> '�����l',
		hp			=> 450,
		at			=> 270,
		df			=> 200,
		ag			=> 50,
		get_exp		=> 85,
		get_money	=> 70,
		icon		=> 'mon/523.gif',
		
		old_sp		=> 20,
		job			=> 23, # ���R�m�W�����v�A�h���S���p���[�A��イ����
		sp			=> 50,
		mp			=> 85,
	},
	{ # 1
		name		=> '�޽����',
		hp			=> 250,
		at			=> 230,
		df			=> 80,
		ag			=> 200,
		get_exp		=> 86,
		get_money	=> 142,
		icon		=> 'mon/543.gif',
		
		job			=> 93, # �����U�L
		sp			=> 10,
		mp			=> 139,
	},
	{ # 2
		name		=> '�����̉e',
		hp			=> 200,
		at			=> 220,
		df			=> 300,
		ag			=> 150,
		get_exp		=> 80,
		get_money	=> 75,
		icon		=> 'mon/527.gif',
		
		job			=> 35, # ���������Ȃ����A���Ă��͂ǂ��A�U�L
		sp			=> 50,
		mp			=> 120,
	},
	{ # 3
		name		=> '�װϼ�',
		hp			=> 444,
		at			=> 244,
		df			=> 144,
		ag			=> 114,
		get_exp		=> 88,
		get_money	=> 88,
		icon		=> 'mon/521.gif',
		
		job			=> 24, # �����m�����񂬂�A���^������A�o�C�L���g�A���Ȃ��܂���A�M�K�X���b�V��
		sp			=> 50,
		old_job		=> 11, # �|�g�������ʂ��A��������Ƃ����A�ł���߂�A�悤�����̂�A�t���b�V���A���[�A�����z�[�A���[
		old_sp		=> 90,
		mp			=> 111,
	},
	{ # 4
		name		=> '��˰ӽ',
		hp			=> 415,
		at			=> 265,
		df			=> 85,
		ag			=> 145,
		get_exp		=> 90,
		get_money	=> 40,
		icon		=> 'mon/553.gif',
		
		job			=> 23, # ���R�m�W�����v�A�h���S���p���[
		sp			=> 30,
		old_job		=> 25, # �����N�܂킵����
		old_sp		=> 5,
		mp			=> 97,
	},
	{ # 5
		hit			=> 70,
		name		=> '�޶��ý',
		hp			=> 600,
		at			=> 400,
		df			=> 50,
		ag			=> 10,
		get_exp		=> 100,
		get_money	=> 5,
		icon		=> 'mon/563.gif',
		
		old_sp		=> 20,
		job			=> 21, # ����m
		sp			=> 999,
		mp			=> 59,
		ten			=> 3,
		state		=> '����',
		tmp			=> '�Q�{',
	},
	{ # 6
		name		=> '�۲',
		hp			=> 380,
		at			=> 200,
		df			=> 160,
		ag			=> 180,
		get_exp		=> 82,
		get_money	=> 65,
		icon		=> 'mon/542.gif',
		
		old_sp		=> 20,
		job			=> 46, # �ެ���װ�w�u���X���b�g�A���������̃_�[�c�A�����܂̃_�C�X�A���̃��[���b�g
		sp			=> 80,
		mp			=> 59,
	},
	{ # 7
		name		=> '��',
		hp			=> 410,
		at			=> 280,
		df			=> 150,
		ag			=> 120,
		get_exp		=> 88,
		get_money	=> 64,
		icon		=> 'mon/536.gif',
		
		old_sp		=> 20,
		job			=> 47, # �ټެ��u���C�o�[�A���傤����A���e�I���C���A�N���C���n�U�[�h
		sp			=> 140,
		mp			=> 69,
	},
	{ # 8
		name		=> '�޼�ؽ�',
		hp			=> 400,
		at			=> 300,
		df			=> 40,
		ag			=> 280,
		get_exp		=> 90,
		get_money	=> 80,
		icon		=> 'mon/558.gif',
		
		old_sp		=> 20,
		job			=> 53, # 峎t
		sp			=> 999,
		mp			=> 67,
	},
);



1;
