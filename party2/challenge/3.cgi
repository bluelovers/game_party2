# �ݒ�
%k = (
	p_join		=> 3,			# �퓬�Q�����(�l)
	need_join	=> '0',			# �Q������(./lib/quest.cgi 192�s�ڂ�������Q�l)
);

# �󕔉�(20�K�`40�K�ȏ�B��ʊK�قǊm���A�b�v)
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
		name		=> '��޹�ɺ',
		hp			=> 400,
		at			=> 300,
		df			=> 150,
		ag			=> 300,
		get_exp		=> 30,
		get_money	=> 20,
		icon		=> 'mon/030.gif',

		job			=> 42, # ����
		sp			=> 999,
		old_job		=> 91, # �}�q�n
		old_sp		=> 999,
		mmp			=> 9999,
		mp			=> 99,
	},
	{ # 1
		name		=> '�޸�ɺ',
		hp			=> 400,
		at			=> 300,
		df			=> 150,
		ag			=> 300,
		get_exp		=> 40,
		get_money	=> 30,
		icon		=> 'mon/031.gif',

		job			=> 90, # �Ōn
		sp			=> 999,
		old_job		=> 20, # ����
		old_sp		=> 999,
		mmp			=> 9999,
		mp			=> 99,
	},
	{ # 2
		name		=> 'ϰ����ݺ�',
		hp			=> 400,
		at			=> 300,
		df			=> 150,
		ag			=> 300,
		get_exp		=> 50,
		get_money	=> 40,
		icon		=> 'mon/032.gif',

		job			=> 90, # �Ōn
		sp			=> 999,
		old_job		=> 19, # �Ŗ����m
		old_sp		=> 999,
		mmp			=> 9999,
		mp			=> 99,
	},
);



1; # �폜�s��
