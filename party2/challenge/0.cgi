# �ݒ�
%k = (
	p_join		=> 1,			# �퓬�Q�����(�l)
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
		name		=> '�ײ�',
		hp			=> 150,
		at			=> 100,
		df			=> 50,
		ag			=> 200,
		get_exp		=> 20,
		get_money	=> 5,
		icon		=> 'mon/002.gif',

		job			=> int(rand(59)), # �����_��
		sp			=> 999,
		old_sp		=> 20,
		mp			=> 50,
	},
);



1; # �폜�s��
