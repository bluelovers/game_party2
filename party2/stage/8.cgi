# ��̒��g
@treasures = (
[10..21], # ����No
[10..17], # �h��No
[15..26,15..26,32,72..86], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '��˰ӽ',
		hp			=> 2800,
		at			=> 185,
		df			=> 125,
		ag			=> 145,
		get_exp		=> 350,
		get_money	=> 200,
		icon		=> 'mon/553.gif',
		
		hit			=> 150, # ������p������150%
		job			=> 23, # ���R�m�W�����v�A�h���S���p���[
		sp			=> 30,
		old_job		=> 25, # �����N�܂킵����
		old_sp		=> 5,
		mp			=> 299,
		tmp			=> '��h��',
	},
);

# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = (0,0,0,1,1,1,2,2,2,3,3,3,4,5,6,6,7,8,9);


# �����X�^�[
@monsters = (
	{ # 0
		hit			=> 70,
		name		=> '��˰۰',
		hp			=> 100,
		at			=> 80,
		df			=> 60,
		ag			=> 60,
		get_exp		=> 30,
		get_money	=> 15,
		icon		=> 'mon/100.gif',

		old_sp		=> 20,
		job			=> 34, # �E�҂��΂�
		sp			=> 10,
		mp			=> 21,
	},
	{ # 1
		hit			=> 70,
		name		=> '��̧���',
		hp			=> 120,
		at			=> 90,
		df			=> 70,
		ag			=> 10,
		get_exp		=> 30,
		get_money	=> 15,
		icon		=> 'mon/101.gif',

		old_sp		=> 20,
		job			=> 1, # ��m���ԂƂ��A���΂��A����������߂�
		sp			=> 30,
		mp			=> 11,
	},
	{ # 2
		hit			=> 70,
		name		=> '��ϰ��',
		hp			=> 80,
		at			=> 50,
		df			=> 30,
		ag			=> 80,
		get_exp		=> 30,
		get_money	=> 15,
		icon		=> 'mon/102.gif',

		job			=> 6, # ���@�g�������A���J�j�A�M���A�}�k�[�T
		sp			=> 14,
		mp			=> 61,
	},
	{ # 3
		hit			=> 70,
		name		=> '����ذ��',
		hp			=> 90,
		at			=> 60,
		df			=> 40,
		ag			=> 60,
		get_exp		=> 30,
		get_money	=> 15,
		icon		=> 'mon/103.gif',

		job			=> 5, # �m���X�J���A�L�A���[�A�z�C�~
		sp			=> 6,
		mp			=> 51,
	},
	{ # 4
		name		=> '���e��',
		hp			=> 100,
		at			=> 86,
		df			=> 40,
		ag			=> 10,
		get_exp		=> 40,
		get_money	=> 5,
		icon		=> 'mon/080.gif',

		job			=> 94, # �������K���e�A�˂�
		sp			=> 20,
		mp			=> 42,
	},
	{ # 5
		name		=> 'Ҷ޻��ۯ�',
		hp			=> 110,
		at			=> 75,
		df			=> 50,
		ag			=> 44,
		get_exp		=> 36,
		get_money	=> 10,
		icon		=> 'mon/081.gif',

		old_sp		=> 30,
		job			=> 3, # �R�m
		sp			=> 80,
		mp			=> 62,
	},
	{ # 6
		name		=> '����',
		hp			=> 133,
		at			=> 99,
		df			=> 33,
		ag			=> 99,
		get_exp		=> 33,
		get_money	=> 33,
		icon		=> 'mon/068.gif',

		job			=> 36, # ���̂܂ˎm
		sp			=> 999,
		mp			=> 99,
	},
	{ # 7
		name		=> '����חd��',
		hp			=> 140,
		at			=> 100,
		df			=> 40,
		ag			=> 120,
		get_exp		=> 27,
		get_money	=> 20,
		icon		=> 'mon/110.gif',

		job			=> 8, # �V�ѐl
		sp			=> 999,
		old_job		=> 55, # �d��
		old_sp		=> 999,
		mp			=> 50,
	},
	{ # 8
		name		=> '�ެ���ٗd��',
		hp			=> 104,
		at			=> 120,
		df			=> 40,
		ag			=> 130,
		get_exp		=> 28,
		get_money	=> 22,
		icon		=> 'mon/111.gif',

		job			=> 36, # �ެ���װ���̃��[���b�g�A�����܂̃_�C�X�A�w�u���X���b�g
		sp			=> 50,
		old_job		=> 55, # �d��
		old_sp		=> 999,
		mp			=> 20,
	},
	{ # 9
		name		=> 'ϳ���',
		hp			=> 104,
		at			=> 120,
		df			=> 40,
		ag			=> 130,
		get_exp		=> 28,
		get_money	=> 22,
		icon		=> 'mon/260.gif',

		job			=> 8, # �V�ѐl
		sp			=> 999,
		old_job		=> 36, # ���̂܂ˎm
		old_sp		=> 80,
		mp			=> 20,
	},
);



1;
