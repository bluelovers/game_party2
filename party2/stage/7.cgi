# ��̒��g
@treasures = (
[9..18], # ����No
[9..18], # �h��No
[15..26,72..86], # ����No
);

# �{�X
@bosses= (
	{
		name		=> '���A',
		hp			=> 100,
		at			=> 80,
		df			=> 80,
		ag			=> 80,
		get_exp		=> 55,
		get_money	=> 30,
		icon		=> 'mon/071.gif',

		old_sp		=> 20,
		job			=> 20, # �����m���΂�
		sp			=> 10,
		mp			=> 42,
	},
	{
		name		=> '�Ђ����ǂ�',
		hp			=> 1800,
		at			=> 160,
		df			=> 70,
		ag			=> 80,
		get_exp		=> 300,
		get_money	=> 180,
		icon		=> 'mon/530.gif',
		
		hit			=> 150, # ������p������150%
		job			=> 26, # �E�҂�����̂����A�₯������
		sp			=> 15,
		old_job		=> 27, # �����t���Ȃ��ނ�
		old_sp		=> 10,
		mp			=> 97,
		tmp			=> '���y��',
	},
	{
		name		=> '���B',
		hp			=> 100,
		at			=> 80,
		df			=> 80,
		ag			=> 80,
		get_exp		=> 55,
		get_money	=> 30,
		icon		=> 'mon/071.gif',

		old_sp		=> 20,
		job			=> 20, # �����m���΂�
		sp			=> 10,
		mp			=> 42,
	},
);

# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = ();


# �����X�^�[
@monsters = (
	{ # 0
		name		=> '̧����ײ�',
		hp			=> 100,
		at			=> 77,
		df			=> 58,
		ag			=> 82,
		get_exp		=> 25,
		get_money	=> 12,
		icon		=> 'mon/008.gif',

		job			=> 6, # ���@�g������
		sp			=> 16,
		mp			=> 100,
	},
	{ # 1
		name		=> 'ϸ�Ͻײ�',
		hp			=> 130,
		at			=> 93,
		df			=> 70,
		ag			=> 30,
		get_exp		=> 30,
		get_money	=> 27,
		icon		=> 'mon/021.gif',
		old_sp		=> 30,
	},
	{ # 2
		name		=> '���e��',
		hp			=> 100,
		at			=> 86,
		df			=> 40,
		ag			=> 10,
		get_exp		=> 50,
		get_money	=> 15,
		icon		=> 'mon/080.gif',

		job			=> 94, # �������K���e�A�˂�
		sp			=> 20,
		mp			=> 42,
	},
	{ # 3
		name		=> '���',
		hp			=> 111,
		at			=> 111,
		df			=> 75,
		ag			=> 20,
		get_exp		=> 34,
		get_money	=> 25,
		icon		=> 'mon/211.gif',

		old_sp		=> 30,
		job			=> 21, # ����m����������A�����Ȃ���
		sp			=> 10,
		mp			=> 26,
	},
	{ # 4
		name		=> '���',
		hp			=> 70,
		at			=> 60,
		df			=> 80,
		ag			=> 60,
		get_exp		=> 35,
		get_money	=> 20,
		icon		=> 'mon/071.gif',

		old_sp		=> 20,
		job			=> 20, # �����m���΂�
		sp			=> 10,
		mp			=> 42,
	},
	{ # 5
		name		=> '�����׺��',
		hp			=> 120,
		at			=> 78,
		df			=> 65,
		ag			=> 66,
		get_exp		=> 30,
		get_money	=> 12,
		icon		=> 'mon/083.gif',

		job			=> 12, # �����g���Ђ̂���
		sp			=> 5,
		mp			=> 26,
	},
	{ # 6
		name		=> '��ׯ���׺',
		hp			=> 110,
		at			=> 90,
		df			=> 100,
		ag			=> 50,
		get_exp		=> 32,
		get_money	=> 20,
		icon		=> 'mon/084.gif',

		job			=> 26, # �E�҂�����̂���
		sp			=> 5,
		mp			=> 17,
	},
	{ # 7
		name		=> '��׺��',
		hp			=> 200,
		at			=> 140,
		df			=> 75,
		ag			=> 68,
		get_exp		=> 60,
		get_money	=> 24,
		icon		=> 'mon/224.gif',

		job			=> 26, # �E�҂�����̂����A�₯������
		sp			=> 15,
		mp			=> 21,
	},
	{ # 8
		name		=> '��޴���',
		hp			=> 80,
		at			=> 70,
		df			=> 80,
		ag			=> 100,
		get_exp		=> 20,
		get_money	=> 14,
		icon		=> 'mon/114.gif',

		job			=> 45, # Ӱ��؂��܂��Ȃ��A�X�g�b�v�A�E�[���K�[�h�A�J�G���̂���
		sp			=> 100,
		mp			=> 60,
	},
	{ # 9
		name		=> '����ٽ',
		hp			=> 140,
		at			=> 112,
		df			=> 50,
		ag			=> 90,
		get_exp		=> 26,
		get_money	=> 18,
		icon		=> 'mon/115.gif',

		old_sp		=> 30,
		job			=> 45, # �r�g���˂�A�X�J���A����������
		sp			=> 10,
		mp			=> 20,
	},
	{ # 10
		name		=> '���̐�m',
		hp			=> 110,
		at			=> 152,
		df			=> 30,
		ag			=> 60,
		get_exp		=> 28,
		get_money	=> 10,
		icon		=> 'mon/576.gif',

		old_sp		=> 20,
		job			=> 26, # �E�҂�����̂���
		sp			=> 5,
		mp			=> 27,
	},
);



1;
