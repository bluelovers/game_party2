# �ݒ�
%k = (
	p_join		=> 2,			# �퓬�Q�����(�l)
	need_join	=> 'hp_400_u',	# �Q������(./lib/quest.cgi 192�s�ڂ�������Q�l)
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
	{
		name		=> 'װ�����',
		hp			=> 200,
		at			=> 140,
		df			=> 100,
		ag			=> 140,
		get_exp		=> 40,
		get_money	=> 21,
		icon		=> 'chr/019.gif',

		job			=> 10, # �r����
		sp			=> 999,
		old_sp		=> 20,
		mmp			=> 9999,
		mp			=> 40,
		ten			=> 3,
	},
);



1; # �폜�s��
