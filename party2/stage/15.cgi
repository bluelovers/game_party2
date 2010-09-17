# ��̒��g
@treasures = (
[15..39], # ����No
[15..39], # �h��No
[13,27..40,75,85,88..100,108,109], # ����No
);


# bosses
@bosses = ();
for my $name (@partys) {
	push @bosses, {
		name		=> $name,
		hp			=> $ms{$name}{mhp},
		mp			=> $ms{$name}{mmp},
		at			=> $ms{$name}{at},
		df			=> $ms{$name}{df},
		ag			=> $ms{$name}{ag},
		get_exp		=> $ms{$name}{get_exp},
		get_money	=> $ms{$name}{get_money},
		icon		=> $ms{$name}{icon},

		job			=> $ms{$name}{job},
		sp			=> $ms{$name}{sp},
		old_job		=> $ms{$name}{old_job},
		old_sp		=> $ms{$name}{old_sp},
		tmp			=> '������',
	}
}



# �o����(@monsters�̔z��ԍ���������Α����قǏo���B�ϓ��ȏo�����̏ꍇ�́A����w()�x)
@appears = ();

# monsters
@monsters = ();
for my $i (1..10) {
	my $m_sex = rand(2)<1 ? 'm':'f';
	my $m_job = int(rand(@jobs));
	unless (-f "$icondir/job/${m_job}_${m_sex}.gif") {
		$m_sex = $m_sex eq 'm' ? 'f' : 'm';
	}
	push @monsters, {
		name		=> $jobs[$m_job][1],
		hp			=> $ms{$m}{mhp},
		mp			=> $ms{$m}{mmp},
		at			=> $ms{$m}{mat},
		df			=> $ms{$m}{mdf},
		ag			=> $ms{$m}{mag},
		get_exp		=> $ms{$m}{get_exp},
		get_money	=> $ms{$m}{get_money},
		icon		=> "job/${m_job}_${m_sex}.gif",

		job			=> $m_job, # ��m
		sp			=> $ms{$m}{sp},
		old_job		=> 36, # ���̂܂ˎt
		old_sp		=> 999,
	};
}



1;
