# �ݒ�
%k = (
	p_join		=> 4,			# �퓬�Q�����(�l)
	need_join	=> '0',			# �Q������(./lib/quest.cgi 192�s�ڂ�������Q�l)
);

# �󕔉�(10�K�`20�K�ȏ�B��ʊK�قǊm���A�b�v)
$tresure_round = int(rand(11)+10);


# ��̒��g
@treasures = (
[], # ����No
[], # �h��No
[6,15,57,72..74,87,101..103], # ����No
);


# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = ();

# �����X�^�[
@monsters = (
	{ # 0
		name		=> '����חd��',
		hp			=> 320,
		at			=> 240,
		df			=> 100,
		ag			=> 300,
		get_exp		=> 40,
		get_money	=> 50,
		icon		=> 'mon/110.gif',

		job			=> 31, # �����m���΂�,���̃��[���b�g
		sp			=> 44,
		old_job		=> 8, # �V�ѐl
		old_sp		=> 999,
		mmp			=> 9999,
		mp			=> 100,
		ten			=> 3,
	},
	{ # 1
		name		=> '�ެ���ٗd��',
		hp			=> 320,
		at			=> 240,
		df			=> 100,
		ag			=> 300,
		get_exp		=> 40,
		get_money	=> 50,
		icon		=> 'mon/111.gif',

		job			=> 31, # �����m���΂�,���̃��[���b�g
		sp			=> 44,
		old_job		=> 36, # �ެ���װ
		old_sp		=> 999,
		mmp			=> 9999,
		mp			=> 100,
		ten			=> 3,
	},
	{ # 2
		name		=> '��ٰ�İ�',
		hp			=> 5,
		at			=> 200,
		df			=> 2000,
		ag			=> 500,
		get_exp		=> 50,
		get_money	=> 100,
		icon		=> 'mon/191.gif',
		
		job			=> 31, # �����m���΂�,���̃��[���b�g
		sp			=> 44,
		old_job		=> 31, # �����m���΂�,���̃��[���b�g
		old_sp		=> 44,
		mmp			=> 9999,
		mp			=> 100,
		tmp			=> '������',
	},
	{ # 3
		name		=> '���₵���e',
		hp			=> 280,
		at			=> 280,
		df			=> 160,
		ag			=> 200,
		get_exp		=> 45,
		get_money	=> 40,
		icon		=> 'mon/047.gif',

		job			=> 93, # �����U�L�A�U���L
		sp			=> 20,
		old_job		=> 93, # �����U�L�A�U���L
		old_sp		=> 20,
		mmp			=> 9999,
		mp			=> 70,
	},
	{ # 4
		name		=> '�Я�',
		hp			=> 420,
		at			=> 280,
		df			=> 70,
		ag			=> 400,
		get_exp		=> 50,
		get_money	=> 100,
		icon		=> 'mon/091.gif',
		
		job			=> 93, # �����U�L�A�U���L
		sp			=> 20,
		old_job		=> 93, # �����U�L�A�U���L
		old_sp		=> 20,
		mmp			=> 9999,
		mp			=> 120,
		tmp			=> '�Q�{', 
	},
	{ # 5
		name		=> '�������ޯ��',
		hp			=> 450,
		at			=> 300,
		df			=> 75,
		ag			=> 600,
		get_exp		=> 70,
		get_money	=> 120,
		icon		=> 'mon/092.gif',
		
		job			=> 93, # �����U�L�A�U���L
		sp			=> 20,
		old_job		=> 93, # �����U�L�A�U���L
		old_sp		=> 20,
		mmp			=> 9999,
		mp			=> 120,
		tmp			=> '�Q�{', 
	},
);



1; # �폜�s��
