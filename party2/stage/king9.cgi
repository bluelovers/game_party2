# �ݒ�
%k = (
	p_name		=> '@���̏�@',	# �N�G�X�g��
	p_join		=> 6,				# �퓬�Q�����(�l)
	p_leader	=> '���̏�',	# �N�G�X�g���[�_�[��
	speed		=> 12,				# �i�s�X�s�[�h(�b)
	need_join	=> 'hp_200_u',		# �Q������(./lib/quest.cgi 192�s�ڂ�������Q�l)
);


# �����험�i(����No)
@treasures = (
[], # ����No
[], # �h��No
[1..43,23,23,59,59,72..89,101..103,107], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '���̏�',
		hp			=> 30000,
		at			=> 150,
		df			=> 150,
		ag			=> 100,
		get_exp		=> 1800,
		get_money	=> 2000,
		icon		=> 'mon/603.gif',
		
		hit			=> 800, # ������p������400%
		job			=> 95, # ����
		sp			=> 999,
		old_job		=> 95, # ����
		old_sp		=> 999,
		mmp			=> 999999,
		mp			=> 99999,
		tmp			=> '�U�y��',
	},
);


# ��������郂���X�^�[
@monsters = (
	{
		name		=> '�װŲ�',
		hp			=> 150,
		at			=> 150,
		df			=> 100,
		ag			=> 150,
		get_exp		=> 50,
		get_money	=> 50,
		icon		=> 'mon/520.gif',

		job			=> 36, # ���̂܂ˎm
		sp			=> 999,
		mp			=> 94,
	},
	{
		name		=> '�n���̊Z',
		hp			=> 166,
		at			=> 116,
		df			=> 166,
		df			=> 66,
		ag			=> 66,
		get_exp		=> 66,
		get_money	=> 66,
		icon		=> 'mon/240.gif',

		old_sp		=> 30,
		job			=> 3, # �R�m���΂��A�܂���������߂�A���Ă݁A�����ڂ�����A�X�N���g
		sp			=> 40,
		mp			=> 66,
	},
	{
		name		=> '�n���̋R�m',
		hp			=> 166,
		at			=> 166,
		df			=> 66,
		ag			=> 66,
		get_exp		=> 66,
		get_money	=> 66,
		icon		=> 'mon/223.gif',
		
		job			=> 24, # �����m�����񂬂�A���^������A�o�C�L���g�A���Ȃ��܂���A�M�K�X���b�V��
		sp			=> 50,
		old_job		=> 22, # �Í��R�m���񂱂��A�߂��₭
		old_sp		=> 20,
		mp			=> 66,
	},
	{
		name		=> '��ٰŲ�',
		hp			=> 120,
		at			=> 150,
		df			=> 60,
		ag			=> 50,
		get_exp		=> 50,
		get_money	=> 30,
		icon		=> 'mon/519.gif',
		
		old_sp		=> 20,
		job			=> 23, # ���R�m�W�����v�A�h���S���p���[�A��イ����
		sp			=> 50,
		mp			=> 85,
	},
	{
		name		=> '��ׯ�Ų�',
		hp			=> 196,
		at			=> 196,
		df			=> 96,
		ag			=> 96,
		get_exp		=> 96,
		get_money	=> 96,
		icon		=> 'mon/524.gif',

		job			=> 21, # �ް����
		sp			=> 999,
		old_job		=> 22, # �Í��R�m���񂱂��A�߂��₭
		old_sp		=> 20,
		mp			=> 96,
	},
);




1;
