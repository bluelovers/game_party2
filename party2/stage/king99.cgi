# �ݒ�
%k = (
	p_name		=> '@�߂Ɣ�@',			# �N�G�X�g��
	p_join		=> 4,					# �퓬�Q�����(�l)
	p_leader	=> $leader,				# �N�G�X�g���[�_�[��
	speed		=> 12,					# �i�s�X�s�[�h(�b)
	need_join	=> 'hp_200_o',			# �Q������(./lib/quest.cgi 192�s�ڂ�������Q�l)
);


# �����험�i(����No)
@treasures = (
[], # ����No
[], # �h��No
[59..65,107,107], # ����No
);

# bosses
@bosses = ();
for my $name (@partys) {
	push @bosses, {
		name		=> $name,
		hp			=> $ms{$name}{mhp} * 50,
		mp			=> $ms{$name}{mmp} * 50,
		at			=> $ms{$name}{at} * 2,
		df			=> $ms{$name}{df} * 2,
		ag			=> $ms{$name}{ag} * 2,
		get_exp		=> $ms{$name}{get_exp} * 30,
		get_money	=> $ms{$name}{get_money} * 30,
		icon		=> $ms{$name}{icon},

		job			=> $ms{$name}{job},
		sp			=> $ms{$name}{sp},
		old_job		=> $ms{$name}{old_job},
		old_sp		=> $ms{$name}{old_sp},
		tmp			=> '��h��',
	}
}




1;
