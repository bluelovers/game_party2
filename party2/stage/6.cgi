# ��̒��g
@treasures = (
[7..18], # ����No
[2..11], # �h��No
[16..26,43,72..86], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '�޶��ý',
		hp			=> 2500,
		at			=> 200,
		df			=> 20,
		ag			=> 20,
		get_exp		=> 200,
		get_money	=> 5,
		icon		=> 'mon/563.gif',
		
		old_sp		=> 20,
		hit			=> 150, # ������p������150%
		job			=> 21, # ����m
		sp			=> 60,
		mp			=> 60,
		state		=> '����',
		tmp			=> '�Q�{',
	},
);

# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = (0,0,0,0,1,1,1,1,2,2,2,3,3,3,3,4,4,4,4,5,5,5,6,6,7,7,8,8,9,9,10,10,11);


# �����X�^�[
@monsters = (
	{ # 0
		name		=> 'ϰ����ݺ�',
		hp			=> 80,
		at			=> 65,
		df			=> 65,
		ag			=> 80,
		get_exp		=> 23,
		get_money	=> 18,
		icon		=> 'mon/032.gif',

		job			=> 90, # �ǂ���������
		sp			=> 999,
		mp			=> 39,
	},
	{ # 1
		name		=> '�ݸ޺���',
		hp			=> 100,
		at			=> 85,
		df			=> 35,
		ag			=> 60,
		get_exp		=> 21,
		get_money	=> 8,
		icon		=> 'mon/054.gif',
		old_sp		=> 20,
	},
	{ # 2
		name		=> 'گ�ޱ�',
		hp			=> 80,
		at			=> 50,
		df			=> 30,
		ag			=> 40,
		get_exp		=> 24,
		get_money	=> 10,
		icon		=> 'mon/074.gif',

		job			=> 42, # ���݃R���t�F
		sp			=> 15,
		mp			=> 61,
	},
	{ # 3
		name		=> '�ް���',
		hp			=> 70,
		at			=> 60,
		df			=> 30,
		ag			=> 50,
		get_exp		=> 28,
		get_money	=> 11,
		icon		=> 'mon/075.gif',

		job			=> 42, # �Ŗ����m���J�i���}�z�J���^���_�p�j
		sp			=> 16,
		mp			=> 71,
	},
	{ # 4
		name		=> '�˶��',
		hp			=> 160,
		at			=> 120,
		df			=> 50,
		ag			=> 35,
		get_exp		=> 27,
		get_money	=> 14,
		icon		=> 'mon/210.gif',

		old_sp		=> 20,
		job			=> 10, # �r�g���˂�A�X�J���A����������
		sp			=> 10,
		mp			=> 22,
		state		=> '����',
	},
	{ # 5
		name		=> '���ް��ݻ�',
		hp			=> 90,
		at			=> 75,
		df			=> 25,
		ag			=> 125,
		get_exp		=> 18,
		get_money	=> 12,
		icon		=> 'mon/206.gif',
		old_sp		=> 20,
	},
	{ # 6
		name		=> '�װ��ݻ�',
		hp			=> 130,
		at			=> 105,
		df			=> 30,
		ag			=> 74,
		get_exp		=> 30,
		get_money	=> 10,
		icon		=> 'mon/207.gif',

		old_sp		=> 20,
		job			=> 21, # ����m����������A�����Ȃ����A��������
		sp			=> 20,
		mp			=> 19,
	},
	{ # 7
		hit			=> 70,
		name		=> 'Ʈ��',
		hp			=> 75,
		at			=> 96,
		df			=> 20,
		ag			=> 80,
		get_exp		=> 28,
		get_money	=> 26,
		icon		=> 'mon/229.gif',

		job			=> 37, # ���E�m�}�z�g�[��
		sp			=> 5,
		mp			=> 34,
	},
	{ # 8
		name		=> '��ڼ�',
		hp			=> 95,
		at			=> 86,
		df			=> 27,
		ag			=> 40,
		get_exp		=> 30,
		get_money	=> 26,
		icon		=> 'mon/230.gif',

		job			=> 20, # �������������ǂ�A���f�B�E�B�b�v�A�}�W�b�N�o���A�A���܂������A���_�p�j�_���X
		sp			=> 26,
		mp			=> 44,
	},
	{ # 9
		name		=> 'ӻӻ',
		hp			=> 100,
		at			=> 60,
		df			=> 40,
		ag			=> 70,
		get_exp		=> 15,
		get_money	=> 100,
		icon		=> 'mon/512.gif',

		job			=> 45, # ���[�O�����܂��Ȃ��A�X�g�b�v�A�E�[���K�[�h�A������̂���
		sp			=> 100,
		mp			=> 59,
	},
	{ # 10
		name		=> '�޽۰�߰',
		hp			=> 80,
		at			=> 90,
		df			=> 80,
		ag			=> 60,
		get_exp		=> 32,
		get_money	=> 16,
		icon		=> 'mon/514.gif',

		job			=> 38, # ����߲����イ���A�X�s��
		sp			=> 20,
		mp			=> 20,
	},
	{ # 11
		name		=> '���ް����',
		hp			=> 150,
		at			=> 70,
		df			=> 50,
		ag			=> 20,
		get_exp		=> 50,
		get_money	=> 50,
		icon		=> 'mon/513.gif',

		old_sp		=> 30,
		job			=> 34, # �E�҂��΂����C�f�C��
		sp			=> 30,
		mp			=> 50,
	},
);



1;
