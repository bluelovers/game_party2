# �ݒ�
%k = (
	p_join		=> 2,			# �퓬�Q�����(�l)
	need_join	=> '0',			# �Q������(./lib/quest.cgi 192�s�ڂ�������Q�l)
);

# �󕔉�(10�K�`20�K�ȏ�B��ʊK�قǊm���A�b�v)
$tresure_round = int(rand(11)+10);


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
	{ # 0
		name		=> '�ް��',
		hp			=> 340,
		at			=> 200,
		df			=> 150,
		ag			=> 200,
		get_exp		=> 30,
		get_money	=> 20,
		icon		=> 'mon/035.gif',

		job			=> 93, # ����
		sp			=> 999,
		old_sp		=> 20,
		mp			=> 40,
	},
	{ # 1
		name		=> 'Ҳ�޺ް��',
		hp			=> 360,
		at			=> 210,
		df			=> 160,
		ag			=> 220,
		get_exp		=> 31,
		get_money	=> 22,
		icon		=> 'mon/036.gif',

		job			=> 6, # ���@�g��
		sp			=> 999,
		old_sp		=> 20,
		mp			=> 70,
	},
	{ # 2
		name		=> 'вגj',
		hp			=> 420,
		at			=> 300,
		df			=> 60,
		ag			=> 160,
		get_exp		=> 40,
		get_money	=> 5,
		icon		=> 'mon/040.gif',
		
		job			=> 9, # ����
		sp			=> 999,
		old_sp		=> 20,
		mp			=> 20,
	},
	{ # 3
		name		=> '�а',
		hp			=> 510,
		at			=> 320,
		df			=> 80,
		ag			=> 180,
		get_exp		=> 45,
		get_money	=> 6,
		icon		=> 'mon/041.gif',

		job			=> 58, # �ް����
		sp			=> 999,
		old_sp		=> 20,
		mp			=> 70,
	},
	{ # 4
		name		=> '�޲���m',
		hp			=> 400,
		at			=> 350,
		df			=> 120,
		ag			=> 150,
		get_exp		=> 40,
		get_money	=> 20,
		icon		=> 'mon/043.gif',
		
		job			=> 2, # ���m
		sp			=> 999,
		old_sp		=> 20,
		mp			=> 40,
	},
	{ # 5
		name		=> '��ׯ������',
		hp			=> 380,
		at			=> 280,
		df			=> 150,
		ag			=> 200,
		get_exp		=> 35,
		get_money	=> 25,
		icon		=> 'mon/064.gif',

		job			=> 61, # ȸ��ݻ� ��т���
		sp			=> 10,
		old_sp		=> 20,
		mp			=> 62,
	},
	{ # 6
		name		=> '����',
		hp			=> 299,
		at			=> 229,
		df			=> 199,
		ag			=> 229,
		get_exp		=> 42,
		get_money	=> 30,
		icon		=> 'mon/072.gif',

		job			=> 31, # �����m
		sp			=> 999,
		old_sp		=> 20,
		mp			=> 66,
	},
);



1; # �폜�s��
