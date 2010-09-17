$is_add_effect = 0; # �ǉ����ʂ̏ꍇ�͔�\���ɂ���t���O
#=================================================
# �Z����@ Created by Merino
#=================================================

#=================================================
# �퓬�p�A�N�V�����Z�b�g(�v���C���[�p)
#=================================================
sub set_action {
	&get_header_data;
	
	unless (defined $ms{$m}{name}) {
		push @actions, ('�����₫','�ɂ���','��������');
		$actions{'�����₫'} = [0, sub{ &sasayaki }];
		$actions{'�ɂ���'}   = [0, sub{ &nigeru   }];
		$actions{'��������'} = [0, sub{ &sukusho  }];
		return;
	}
	
	my @skills = ();
	if ($round > 0 && @enemys > 0) {
		if ($ms{$m}{sp}) {
			push @skills, &{ 'skill_'.$ms{$m}{job} };
			push @skills, ([0, 0, 'br', sub{ return } ]);
			for my $i (0.. $#skills) {
				next if $skills[$i][0] > $ms{$m}{sp};
				next if $skills[$i][1] > $ms{$m}{mp};
				push @actions, "$skills[$i][2]";
				$actions{$skills[$i][2]} = [ $skills[$i][1], $skills[$i][3] ];
			}
		}

		@skills = ();
		if ($ms{$m}{old_sp}) {
			push @skills, &{ 'skill_'.$ms{$m}{old_job} };
			push @skills, ([0, 0, 'br', sub{ return } ]);
		}

		push @skills, (
			[0,	0,	'��������',		sub{ &kougeki	}],
			[0,	0,	'�ڂ�����',		sub{ $ms{$m}{tmp} = '�h��'; $com.=qq|<span class="tmp">$m�͐g���ł߂Ă���</span>|;	}],
			[0,	0,	'�Ă񂵂��',	sub{ &tenshon($m)	}],
		);
	}
	
	push @skills, ([0, 0, '�ǂ���',   sub{ &dougu }])  if $ites[$m{ite}][3] eq '1'; # �퓬�g�p�A�C�e�������Ă���ꍇ
	push @skills, ([0, 0, '�܂�',     sub{ &mae }],      [0, 0, '������', sub{ &ushiro }]) if @partys > 1; # 2�l�ȏ�
	push @skills, ([0, 0, '�����₫', sub{ &sasayaki }], [0, 0, '�ɂ���', sub{ &nigeru }], [0, 0, '��������', sub{ &sukusho }]); # �퓬�p�ǉ��A�N�V����
	push @skills, ([0, 0, '������',   sub{ &sasou  }]) if $round == 0; # �J�n�O && ذ�ް�̂�
	push @skills, ([0, 0, '������',   sub{ &kick }])   if $round == 0 && $m eq $leader; # �J�n�O && ذ�ް�̂�

	for my $i (0.. $#skills) {
		next if $skills[$i][0] > $ms{$m}{old_sp};
		next if $skills[$i][1] > $ms{$m}{mp};
		push @actions, "$skills[$i][2]";
		$actions{$skills[$i][2]} = [ $skills[$i][1], $skills[$i][3] ];
	}

	&add_battle_action;
}

#=================================================
# ���ǂ���
#=================================================
sub dougu {
	my $y = shift || $m;
	$com .= "$ites[$m{ite}][1] ���������I";
	&{ $ites[$m{ite}][4] }($y);
	return if $mes;
	$m{ite} = 0;
}

#=================================================
# ��������
#=================================================
sub sasou {
	my $y = shift;

	$act_time = 0;
	$this_file = "$logdir/quest";

	if ($y) {
		$to_name = $y;
		return;
	}
	$mes .= "�N���������܂����H<br />";
	open my $fh, "< ${this_file}_member.cgi" or &error("${this_file}_member.cgi�t�@�C�������J���܂���"); 
	while (my $line = <$fh>) {
		my($ltime, $is_npc, $name, $laddr, $icon, $color) = split /<>/, $line;
		next if $time - $limit_member_time > $ltime;
		next if $sames{$name}++; # �����l�Ȃ玟
		$mes .= qq|<span onclick="text_set('��������>$name ')" style="color: $color;"><img src="$icondir/$icon" alt="$name" />$name</span>|;
	}
	close $fh;
}

#=================================================
# ��������
#=================================================
sub kick {
	my $y = shift;
	
	$mes = "���������������邱�Ƃ͂ł��܂���"		if $y eq $m;
	$mes = "���[�_�[����Ȃ��̂ł������ł��܂���"	if $leader ne $m;
	$mes = "�N�G�X�g���͂������ł��܂���"			if $round > 0;
	return if $mes;

	unless ($y) {
		$mes = "�N�����������܂����H<br />";
		for my $name (@partys) {
			$mes .= qq|<span onclick="text_set('��������>$name')">$name</span>|;
		}
		return;
	}
	
	for my $i (0 .. $#members) {
		if ($members[$i] eq $y) {
			&regist_you_data($y, 'lib', 'quest');
			&regist_you_data($y, 'wt', $time + 60);
			$com.="$y�����������܂���";
			splice(@members, $i, 1);
			
			my @lines = ();
			open my $fh, "+< $logdir/quest.cgi" or &error("$logdir/quest.cgi�t�@�C�����J���܂���");
			eval { flock $fh, 2 };
			while (my $line = <$fh>) {
				push @lines, $line;
			}
			push @lines, $line;
			unshift @lines, "$time<>$date<>$npc_name<>NPC<>$npc_color<>$p_name�̃��[�_�[$m���炫��������܂���<>$y<>\n";
			seek  $fh, 0, 0;
			truncate $fh, 0;
			print $fh @lines;
			close $fh;
			
			last;
		}
	}
}

#=================================================
# �����̑f�����Ƒ���̑f����(*�R�{)���r(����E��S�̈ꌂ�̊m��)
#�w * 3�x�̐���������������Ή�����S���̊m�����オ��A������傫������Ή�����S���̊m����������
#=================================================
sub _is_exceed_ag {
	my($_m, $_y) = @_;
	return 0 if !$_m || !$_y;
	return rand(3) < 1 && rand($ms{$_m}{ag}) >= rand($ms{$_y}{ag}*3) ? 1 : 0;
}

#=================================================
# ����������
#=================================================
sub kougeki {
	my $y = shift;
	$y = $enemys[int(rand(@enemys))] if !defined($ms{$y}{name}) || $ms{$y}{color} eq $ms{$m}{color};

	if ( &_is_exceed_ag($m, $y) ) {
		$com .= qq|<span class="kaishin">��S�̈ꌂ�I�I</span>|;
		&_damage($y, $ms{$m}{at} * 0.75, '�U', 1);
	}
	else {
		&_damage($y, $ms{$m}{at}, '�U');
	}
}
#=================================================
# ���܂�
#=================================================
sub mae {
	@enemys = ();
	for my $name (@members) {
		next if !defined $ms{$m}{name};
		next if $ms{$m}{color} eq $ms{$name}{color};
		push @enemys, $name;
	}
	
	my @new_partys = ($m);
	for my $name (@partys) {
		next if $m eq $name;
		push @new_partys, $name;
	}
	@partys = @new_partys;
	@members = (@partys,@enemys);
}

#=================================================
# ��������
#=================================================
sub ushiro {
	@enemys = ();
	for my $name (@members) {
		next if !defined $ms{$m}{name};
		next if $ms{$m}{color} eq $ms{$name}{color};
		push @enemys, $name;
	}

	my @new_partys = ();
	for my $name (@partys) {
		next if $m{name} eq $name;
		push @new_partys, $name;
	}
	push @new_partys, $m;
	@partys = @new_partys;
	@members = (@partys,@enemys);
}

#=================================================
# ���Ă񂵂��
#=================================================
%ten_names = (
	1.7		=> qq|<font color="#FFFF99">�ݼ��</font>|,
	3		=> qq|<font color="#FFCC00">�ݼ��</font>|,
	5		=> qq|<font color="#FFFF00">ʲ�ݼ��</font>|,
	8		=> qq|<font color="#FF0000">Sʲ�ݼ��</font>|,
);
sub tenshon {
	my $y = shift || $m;
	if ($ms{$y}{ten} <= 1) {
		$ms{$y}{ten} = 1.7;
		$com .= qq|$y�̃e���V������ <span class="tenshon">5��</span> �ɂȂ����I|;
	}
	elsif ($ms{$y}{ten} <= 2) {
		$ms{$y}{ten} = 3;
		$com .= qq|$y�̃e���V������ <span class="tenshon">20��</span> �ɂȂ����I|;
	}
	elsif ($ms{$y}{ten} <= 3) {
		$ms{$y}{ten} = 5;
		$com .= qq|$y�̃e���V������ <span class="tenshon">50��</span> �ɂȂ����I$y��<span class="tenshon">�n�C�e���V����</span>�ɂȂ����I|;
	}
	else {
		if ( $m{lv} < 25 || $ms{$y}{ten} >= 8 || $m{lv} < int(rand(50)+20) ) {
			$com .= qq|$y�̃e���V�����͂���ȏ゠����Ȃ��悤��|;
		}
		else {
			$ms{$y}{ten} = 8;
			$com .= qq|$y�̃e���V������ <span class="tenshon">100��</span> �ɂȂ����I$y��<span class="tenshon">�X�[�p�[�n�C�e���V����</span>�ɂȂ����I|;
		}
	}
}

#=================================================
# �X�L���ꗗ
#=================================================
# �����c�����U�����U�A���@�U�������A�u���X�����A�x�遨�x
# ��Ԉُ�c��ჁA����A�ғŁA�����A�����A�x���A����
# �u$is_add_effect = 1;�v�́A�U���{��Ԉُ�ȂǂŎg�p�B�u�`�����킵���v�̃��b�Z�[�W���\������Ȃ��Ȃ�B
#=================================================
sub skill_0 { # �G�p�Ă񂵂��A�ڂ�����B�U������m�����������Ă��܂��̂ŁA���������̔z���ǉ�
	return (
	# [�K�vSP, �g�pMP, '�X�L����(����������)', sub{ �v���O�������� }],
		[8,		0,	'��������',		sub{ &kougeki	}],
		[9,		0,	'��������',		sub{ &kougeki	}],
		[10,	0,	'��������',		sub{ &kougeki	}],
		[20,	0,	'�Ă񂵂��',	sub{ &tenshon($m)	}],
		[30,	0,	'�ڂ�����',		sub{ $ms{$m}{tmp} = '�h��'; $com.=qq|<span class="tmp">$m�͐g���ł߂Ă���</span>|;	}],
	);
}
sub skill_1 { # ��m
	return (
		[5,		5,		'���ԂƂ��',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at}*0.9, '�U'); return if !$y || $ms{$y}{hp} <= 0; &_st_down($y, 0.15, '�U', 'df');	}],
		[8,		0,		'���΂�',			sub{ my($y) = &_check_party(shift, '���΂�', '�U'); return if !$y || $y eq $m; $ms{$m}{tmp} = '���΂���'; $ms{$y}{tmp} = '���΂�'; $com.=qq|<span class="tmp">$m��$y�����΂��Ă���</span>|;	}],
		[25,	8,		'����������߂�',	sub{ &_st_up($m, 1.0, '�U', 'at');	}],
		[50,	5,		'���񂹂��Ȃ�',		sub{ &_damages(90, '�U', 1);	}],
		[80,	10,		'�܂��񂬂�',		sub{ rand(2) < 1 ? &_damage(shift, $ms{$m}{at} * 3, '�U') : &_damage(shift, 20, '�U');	}],
	);
}
sub skill_2 { # ���m
	return (
		[5,		3,		'���񂭂�����',		sub{ &_damage(shift, $ms{$m}{ag}*1.5, '�U');	}],
		[10,	4,		'�݂˂���',			sub{ &_st_d(shift, '����', '�U', 80);	}],
		[20,	5,		'�����Ȃ���',		sub{ $ms{$m}{tmp} = '�󗬂�'; $com.=qq|<span class="tmp">$m�͍U�����󗬂����܂����Ƃ���</span>|;	}],
		[30,	0,		'���΂�',			sub{ my($y) = &_check_party(shift, '���΂�', '�U'); return if !$y || $y eq $m; $ms{$m}{tmp} = '���΂���'; $ms{$y}{tmp} = '���΂�'; $com.=qq|<span class="tmp">$m��$y�����΂��Ă���</span>|;	}],
		[50,	6,		'���^������',		sub{ &_damage(shift, $ms{$m}{at}*0.4, '��', 1);		}],
		[80,	12,		'�͂�Ԃ�����',		sub{ my $y = shift; for my $i (1..2) { last if $ms{$m}{hp} <= 0; &_damage($y, $ms{$m}{ag}*2.2, '�U'); };	}],
		[100,	21,		'���݂��ꂬ��',		sub{ &_damages($ms{$m}{at}, '�U');	}],
	);
}
sub skill_3 { # �R�m
	return (
		[1,		0,		'���΂�',			sub{ my($y) = &_check_party(shift, '���΂�', '�U'); return if !$y || $y eq $m; $ms{$m}{tmp} = '���΂���'; $ms{$y}{tmp} = '���΂�'; $com.=qq|<span class="tmp">$m��$y�����΂��Ă���</span>|;	}],
		[5,		2,		'�܂���������߂�',	sub{ &_st_up($m, 0.4, '�U', 'df');		}],
		[15,	5,		'���Ă�',			sub{ $com.=qq|<span class="tmp">$m�͎����C�ɂ������Ă݂ōU���I</span>|; &_damage(shift, $ms{$m}{at}*2, '�U'); $ms{$m}{tmp}='�Q�{';	}],
		[25,	3,		'�����ڂ�����',		sub{ $ms{$m}{tmp}='��h��'; $com.=qq|<span class="tmp">$m�͎��̂��܂����Ƃ����I</span>|;	}],
		[40,	7,		'�X�N���g',			sub{ &_st_ups(0.25, '��', 'df');	}],
		[60,	1,		'���K�U��',			sub{ $com.=qq|<span class="die">$m�͎����̖����������܂����I</span>|; for my $y (@partys) { next if $m eq $y; $com .= $ms{$y}{hp} > 0 ? qq|$y��$e2j{hp}��<span class="heal">�S��</span>�����I| : qq|<span class="revive">$y�������Ԃ����I</span>|; $ms{$y}{hp} = $ms{$y}{mhp}; }; &defeat($m); $ms{$m}{mp} = 1;	}],
		[80,	18,		'�O�����h�N���X',	sub{ &_damages($ms{$m}{df} * 1.5, '�U');	}],
	);
}
sub skill_4 { # ������
	return (
		[1,		0,		'��������Ƃ�����',	sub{ $ms{$m}{hit}=95; $com.=qq|<span class="st_up">$m�͐S�𗎂��������������񕜂���</span>|;	}],
		[5,		3,		'�݂��킵���Ⴍ',	sub{ &_st_up($m, 0.4, '�U', 'ag');				}],
		[14,	4,		'�Ђ�����',			sub{ &_damage(shift, $ms{$m}{at}*1.2, '�U');				}],
		[25,	3,		'�����΂炢',		sub{ &_st_d(shift, '����', '�U', 75);		}],
		[45,	11,		'���イ����Â�',	sub{ &_death(shift, '����', '�U', 19);	}],
		[70,	15,		'��������Â�',		sub{ &_damage(shift, $ms{$m}{at}*1.5, '�U');		}],
		[100,	20,		'�΂������',		sub{ my $v = int(rand(3)+3); for my $i (1..$v) { last if $ms{$m}{hp} <= 0; &_damage(undef, $ms{$m}{at} * 0.8, '�U'); };	}],
	);
}
sub skill_5 { # �m��
	return (
		[1,		3,		'�X�J��',	sub{ &_st_up(shift, 0.4, '��', 'df');	}],
		[3,		2,		'�L�A���[',	sub{ &_st_h(shift, '�ғ�', '��');	}],
		[6,		3,		'�z�C�~',	sub{ &_heal(shift, 30, '��');	}],
		[12,	4,		'�o�M',		sub{ &_damages(rand(25)+10, '��', 1);	}],
		[24,	10,		'�x�z�C�~',	sub{ &_heal(shift, 90, '��');	}],
		[45,	10,		'�o�M�}',	sub{ &_damages(rand(40)+25, '��', 1);	}],
		[60,	20,		'�U�I����',	sub{ my($y) = &_check_party(shift, '�h��', '��'); return if !$y || $ms{$y}{hp} > 0; if (rand(2) < 1) { $com.=qq|�Ȃ�ƁA<span class="revive">$y�������Ԃ�܂����I</span>|; $ms{$y}{hp}=int($ms{$y}{mhp} * 0.5); } else { $com.=qq|�������A$y�͐����Ԃ�Ȃ������c|; };	}],
		[100,	30,		'�x�z�}',	sub{ &_heal(shift, 999, '��');	}],
	);
}
sub skill_6 { # ���@�g��
	return (
		[1,		2,		'����',			sub{ &_damage(shift, 20, '��', 1);			}],
		[4,		4,		'���J�j',		sub{ &_st_down(shift, 0.4, '��', 'df');	}],
		[8,		5,		'�M��',			sub{ &_damages(25, '��', 1);				}],
		[14,	7,		'�}�k�[�T',		sub{ &_st_downs(0.2, '��', 'hit');			}],
		[20,	8,		'�����~',		sub{ &_damage(shift, 70, '��', 1);		}],
		[30,	8,		'�����z�[',		sub{ &_st_d(shift, '����', '��', 65);		}],
		[55,	11,		'�x�M���}',		sub{ &_damages(60, '��', 1)				}],
		[90,	30,		'�����]�[�}',	sub{ &_damage(shift, 220, '��', 1);		}],
	);
}
sub skill_7 { # ���l
	return (
		[2,		2,		'�܂���������߂�',	sub{ &_st_up($m, 0.4, '�U', 'df');		}],
		[7,		1,		'�S�[���h�n���}�[',	sub{ my($y, $v) = &_damage(shift, $ms{$m}{at}*0.8, '�U'); return if !$y; $v = int($v * 0.1)+5; $m{money}+=$v; $com.="$v G����ɓ���܂����I";	}],
		[12,	6,		'���Ȃ��ނ�',		sub{ &_st_downs(0.2, '��', 'hit');	}],
		[20,	0,		'�Ƃ������̂͂�',	sub{ my $y = shift; $y = $members[int(rand(@members))] if !defined($ms{$y}{name}); if ($y =~ /^@.+��.$/) { my $item_name = $ms{$y}{get_money} eq '0' ? '�������' : $ms{$y}{get_exp} eq '1' ? $weas[$ms{$y}{get_money}][1] : $ms{$y}{get_exp} eq '2' ? $arms[$ms{$y}{get_money}][1] : $ites[$ms{$y}{get_money}][1]; $com.="�󔠂̒��g�� $item_name �̂悤���c"; } else { my @smells=(qw/���� ������������ �o���� ���܂� �ς� ��΂� ����₩�� ���C���h��/); my $v=int(rand(@smells)); $com.="$y�� $smells[$v] �ɂ���������"; };	}],
		[35,	4,		'����������',		sub{ my($y, $v) = &_damage(shift, $ms{$m}{df} * 1.6, '�U'); return if $v <= 0; &_risk($v * 0.07);		}],
		[45,	1,		'�}�z�A�Q��',		sub{ my($y) = &_check_party(shift, '���^', '��'); return if !$y; $v = int($ms{$m}{mp} * 0.5); $ms{$m}{mp} -= $v; $com.= qq|$m��$e2j{mmp}��$y�� <span class="heal">$v</span> ���������I|; &_mp_h($y, $v, '��');	}],
		[65,	7,		'���_�p�j�_���X',	sub{ &_st_ds('����', '�x', 60);	}],
		[80,	1,		'���K���e',			sub{ $com.=qq|<span class="die">$m�͎��������I</span>|; &_deaths('����', '��', 60); &defeat($m); $ms{$m}{mp} = 1; 	}],
	);
}
sub skill_8 { # �V�ѐl
	return (
		[1,		0,		'�˂�',				sub{ $ms{$m}{state}='����'; $com.="$m�͖��肾����"; &_heal($m, $ms{$m}{mhp}*0.5);	}],
		[4,		0,		'�Ȃ�������',		sub{ my $y=$members[int(rand(@members))]; $ms{$y}{state}='���'; $ms{$y}{ten}=1; $com.=qq|$m��$y�ɓ����L�b�X����<span class="state">$y��Ⴢ�܂����I</span>|;		}],
		[8,		0,		'�p�t�p�t',			sub{ my $y=$members[int(rand(@members))]; $ms{$y}{state}='����'; $ms{$y}{ten}=1; $com.=qq|$m��$y�Ƀp�t�p�t�������I<span class="state">$y�͓������~�܂����I</span>|;	}],
		[12,	0,		'������Ȃ�����',	sub{ my $y=$members[int(rand(@members))]; $ms{$y}{state}='�ғ�'; $ms{$y}{ten}=1; $com.=qq|$m�̊댯�ȗV�тɂ��<span class="state">$y�͖ғłɂȂ�܂����I</span>|;	}],
		[18,	0,		'���傤�͂�',		sub{ for my $y (@members) { next if $ms{$y}{hp} <= 0 || $m eq $y || rand(2) < 1; &tenshon($y); };	}],
		[24,	0,		'���炩��',			sub{ my $y = shift; ($y) = defined($ms{$y}{name}) ? $y : &_check_enemy($y, '�e��', '��'); &tenshon($y);		}],
		[36,	0,		'�����ς��Ⴎ',	sub{ my @gags = ('����ɍs���͍̂��������H','���J�i���ł������邩�Ȃ��','����ȃX�e�e�R�p���c�����X�e�e�R���I','�X�J�����g���Ă�����ꂽ','�A���^������傩���H�������','�₭���������񂪂�₭������','���҂𔭌�����I'); my $gag = $gags[int(rand(@gags))]; $com.="�w$gag�x�c"; for my $y (@members) { next if $y eq $m; next if rand(3) < 1; $com.="$y�͏΂��]�����I"; $ms{$y}{state}='����'; $ms{$y}{ten}=1;	 };	}],
		[50,	0,		'�N�[���W���[�N',	sub{ for my $y (@enemys) { $ms{$y}{ten} = 1; }; $com.="�S���̃e���V���������������c";	}],
	);
}
sub skill_9 { # ����
	return (
		[3,		3,		'�{�~�G',			sub{ &_st_down(shift,  0.4, '��', 'ag');	}],
		[6,		3,		'�s�I��',			sub{ &_st_up(shift, 0.4, '��', 'ag');	}],
		[12,	7,		'�����Ԃ�',		sub{ &_st_ds('����', '��', 45);	}],
		[20,	0,		'�Ƃ������̂͂�',	sub{ my $y = shift; $y = $members[int(rand(@members))] if !defined($ms{$y}{name}); if ($y =~ /^@.+��.$/) { my $item_name = $ms{$y}{get_money} eq '0' ? '�������' : $ms{$y}{get_exp} eq '1' ? $weas[$ms{$y}{get_money}][1] : $ms{$y}{get_exp} eq '2' ? $arms[$ms{$y}{get_money}][1] : $ites[$ms{$y}{get_money}][1]; $com.="�󔠂̒��g�� $item_name �̂悤���c"; } else { my @smells=(qw/���� ������������ �o���� ���܂� �ς� ��΂� ����₩�� ���C���h��/); my $v=int(rand(@smells)); $com.="$y�� $smells[$v] �ɂ���������"; };	}],
		[35,	9,		'���܂�����',		sub{ &_st_ds('����', '��', 35);	}],
		[50,	1,		'�C���p�X',			sub{ my $y = shift; $y = $members[int(rand(@members))] if !defined($ms{$y}{name}); $com.="<br />$y $e2j{mhp}:$ms{$y}{hp}/$ms{$y}{mhp}, $e2j{mmp}:$ms{$y}{mp}/$ms{$y}{mmp}, $e2j{at}:$ms{$y}{mat}, $e2j{df}:$ms{$y}{mdf}, $e2j{ag}:$ms{$y}{mag}";	}],
		[70,	8,		'�܂Ђ�������',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at} * 1.2, '�U'); return if !$y || $ms{$y}{hp} <= 0; &_st_d($y, '���', '�U', 30);	}],
		[90,	15,		'�A�[�}�[�u���C�N',	sub{ my($y) = &_check_enemy(shift, '�j��', '�U'); return if !$y; $ms{$y}{tmp}=''; $ms{$y}{ten}=1; $ms{$y}{df}=$ms{$y}{mdf}; $com.="$y�̖h��̋����𕕂����I"; &_st_down($y, 0.1, '�U', 'df');	}],
	);
}
sub skill_10 { # �r�g��
	return (
		[1,		0,		'�˂�',				sub{ $ms{$m}{state}='����'; $com.=qq|<span class="state">$m�͖��肾����</span>|; &_heal($m, $ms{$m}{mhp}*0.5);	}],
		[3,		3,		'�X�J��',			sub{ &_st_up(shift, 0.4, '��', 'df');	}],
		[10,	4,		'����������',		sub{ my($y, $v) = &_damage(shift, $ms{$m}{df} * 1.6, '�U'); return if $v <= 0; &_risk($v * 0.07);		}],
		[20,	10,		'�x�z�C�~',			sub{ &_heal(shift, 90, '��');	}],
		[40,	9,		'�˂ނ�̂���',		sub{ &_st_ds('����', '��', 45);		}],
		[60,	1,		'�}�z�L�e',			sub{ return if &is_bad_state('��'); $ms{$m}{tmp} = '���z��'; $com.=qq|<span class="tmp">$m�͕s�v�c�Ȍ��ɕ�܂ꂽ�I</span>|;	}],
		[80,	7,		'�E�[���K�[�h',		sub{ &_st_up($m, 0.5, '��', 'df'); $ms{$m}{tmp} = '���y��'; $com.=qq|<span class="tmp">$m�͖��@�̌��Ŏ��ꂽ�I</span>|;	}],
		[100,	20,		'�ǂƂ��̂Ђ�',	sub{ my $v = int(rand(3)+2); for my $i (1..$v) { last if $ms{$m}{hp} <= 0; &_damage(undef, $ms{$m}{ag} * 1.6, '�U'); };	}],
	);
}
sub skill_11 { # �|�g��
	return (
		[5,		3,		'�����ʂ�',				sub{ &_st_d(shift, '����', '�U', 80);	}],
		[10,	0,		'��������Ƃ�����',		sub{ $ms{$m}{hit}=95; $com.=qq|<span class="st_up">$m�͐S�𗎂��������������񕜂���</span>|;	}],
		[20,	8,		'�ł���߂�',			sub{ &_damages($ms{$m}{ag}*1.4, '�U');	}],
		[40,	4,		'�悤�����̂�',			sub{ my($y, $v) = &_st_down(shift, 0.15, '�U', 'mp'); return if !$y; &_mp_h($m, $v, '�U');	}],
		[60,	6,		'�t���b�V���A���[',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at}*1.2, '�U'); return if !$y || $ms{$y}{hp} <= 0; &_st_down($y, 0.07, '�U', 'hit');	}],
		[90,	20,		'�����z�[�A���[',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at}*1.1, '�U'); return if !$y || $ms{$y}{hp} <= 0; &_st_d($y, '����', '�U', 55);	}],
		[110,	24,		'�݂��ꂤ��',			sub{ my $v = int(rand(2)+3); for my $i (1..$v) { last if $ms{$m}{hp} <= 0; &_damage(undef, $ms{$m}{at} * 0.85, '�U'); };		}],
	);
}
sub skill_12 { # �����g��
	return (
		[3,		2,		'�Ђ̂���',			sub{ &_damages(18, '��', 1);	}],
		[10,	7,		'�����ǂ��̂���',	sub{ &_st_ds('�ғ�', '��', 60);	}],
		[18,	5,		'������̂���',		sub{ &_damages(50, '��', 1);	}],
		[32,	11,		'���тꂤ��',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at}*1.1, '�U'); return if !$y || $ms{$y}{hp} <= 0; &_st_d($y, '���', '�U', 40);	}],
		[50,	5,		'�Ȃ߂܂킷',		sub{ &_st_d(shift, '����', '�U', 85);	}],
		[80,	14,		'�͂������ق̂�',	sub{ &_damages(90, '��', 1);	}],
		[110,	12,		'������イ����',	sub{ my $y = shift; for my $i (1..2) { last if $ms{$m}{hp} <= 0; &_damage($y, $ms{$m}{at}*1.6, '�U'); };	}],
	);
}
sub skill_13 { # ��V���l
	return (
		[5,		3,		'�ӂ����Ȃ���',			sub{ &_st_downs(0.25, '��', 'mp');	}],
		[15,	7,		'���₵�̂���',			sub{ &_heals(30, '��');				}],
		[30,	5,		'�߂��߂̂���',			sub{ &_st_hs('����', '��');			}],
		[40,	6,		'�܂���̂���',			sub{ &_st_ups(0.4, '��', 'df');		}],
		[60,	9,		'�˂ނ�̂���',			sub{ &_st_ds('����', '��', 50);		}],
		[90,	10,		'���������̂���',		sub{ &_st_ups(0.6, '��', 'at');		}],
	);
}
sub skill_14 { # �x��q
	return (
		[4,		3,		'�݂��킵���Ⴍ',	sub{ &_st_up($m, 0.4, '�x', 'ag');	}],
		[9,		3,		'�ӂ����Ȃ��ǂ�',	sub{ &_st_down(shift, 0.4, '�x', 'mp');	}],
		[16,	5,		'�����Ȃ���',		sub{ $ms{$m}{tmp} = '�󗬂�'; $com.=qq|<span class="tmp">$m�͍U�����󗬂����܂����Ƃ���</span>|;	}],
		[30,	9,		'���[���T���g',		sub{ &_damages($ms{$m}{at}*0.8, '�U');	}],
		[45,	1,		'���K�U���_���X',	sub{ $com.="$m�̖����������x��I"; for my $y (@partys) { next if $m eq $y; $com .= $ms{$y}{hp} > 0 ? qq|$y��$e2j{hp}��<span class="heal">�S��</span>�����I| : qq|<span class="revive">$y�������Ԃ����I</span>|; $ms{$y}{hp} = $ms{$y}{mhp}; }; &defeat($m); $ms{$m}{mp} = 1; $com.=qq|<span class="die">$m�͗͐s�����c</span>|;	}],
		[70,	16,		'�邬�̂܂�',		sub{ my $v = int(rand(3)+2); for my $i (1..$v) { last if $ms{$m}{hp} <= 0; &_damage(undef, $ms{$m}{at}*0.8, '�x'); };	}],
		[100,	12,		'�n�b�X���_���X',	sub{ &_heals(140, '�x');	}],
	);
}
sub skill_15 { # �������m
	return (
		[5,		6,		'�|�C�Y��',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, 30, '��', 1); return if !$y || $ms{$y}{hp} <= 0; &_st_d($y, '�ғ�', '��', 80);	}],
		[10,	5,		'�t�@�C�A',		sub{ &_damage(shift, 35, '��', 1);	}],
		[20,	8,		'�X���v��',		sub{ &_st_d(shift, '����', '��', 55);	}],
		[40,	7,		'���t���N',		sub{ my($y) = &_check_party(shift, '������', '��'); return if !$y; $ms{$y}{tmp} = '������'; $com.=qq|<span class="tmp">$y�͖��@�̕ǂŎ��ꂽ�I</span>|;	}],
		[60,	3,		'�A�X�s��',		sub{ my($y, $v) = &_st_down(shift, 0.2, '��', 'mp'); return if !$y; &_mp_h($m, $v, '��');	}],
		[80,	16,		'�h���C��',		sub{ my($y, $v) = &_damage(shift, rand(100)+50, '��', 1); return if !$y; &_heal($m, $v, '��');	}],
		[130,	40,		'�t���A',		sub{ &_damage(shift, 260, '��', 1);	}],
	);
}
sub skill_16 { # �������m
	return (
		[5,		5,		'�P�A��',		sub{ &_heal(shift, 60, '��');	}],
		[10,	2,		'���C�u��',		sub{ my $y = shift; $y = $members[int(rand(@members))] if !defined($ms{$y}{name}); $com.="<br />$y $e2j{mhp}:$ms{$y}{hp}/$ms{$y}{mhp}, $e2j{mmp}:$ms{$y}{mp}/$ms{$y}{mmp}, $e2j{at}:$ms{$y}{mat}, $e2j{df}:$ms{$y}{mdf}, $e2j{ag}:$ms{$y}{mag}";	}],
		[15,	6,		'�T�C���X',		sub{ &_st_d(shift, '����', '��', 90);	}],
		[30,	18,		'�P�A����',		sub{ &_heal(shift, 180, '��');			}],
		[60,	20,		'�����C�Y',		sub{ my($y) = &_check_party(shift, '����', '��'); return if !$y; $ms{$y}{tmp}='����'; $com.=qq|<span class="tmp">$y�͓V�g�̉��삪�����I</span>|;	}],
		[80,	5,		'�V�F��',		sub{ my($y) = &_check_party(shift, '���y��', '��'); return if !$y; $ms{$y}{tmp}='���y��'; $com.=qq|<span class="tmp">$y�͖��@�̌��Ŏ��ꂽ�I</span>|;	}],
		[100,	40,		'���C�Y',		sub{ my($y) = &_check_party(shift, '�h��', '��'); return if !$y || $ms{$y}{hp} > 0; $com.=qq|�Ȃ�ƁA<span class="revive">$y�������Ԃ�܂����I</span>|; $ms{$y}{hp}=int($ms{$y}{mhp}*0.25);	}],
		[140,	35,		'�z�[���[',		sub{ &_damage(shift, 180, '��', 1);	}],
	);
}
sub skill_17 { # ���R�m
	return (
		[10,	0,		'���΂�',			sub{ my($y) = &_check_party(shift, '���΂�', '�U'); return if !$y || $y eq $m; $ms{$m}{tmp} = '���΂���'; $ms{$y}{tmp} = '���΂�'; $com.=qq|<span class="tmp">$m��$y�����΂��Ă���</span>|;	}],
		[20,	3,		'�z�C�~',			sub{ &_heal(shift, 30, '��');	}],
		[40,	6,		'�}�W�b�N�o���A',	sub{ return if &is_bad_state('��'); for my $y (@partys) { return if $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '���y��'; $com.=qq|<span class="tmp">$y�͖��@�̌��Ŏ��ꂽ�I</span>|; };	}],
		[60,	5,		'�L�A���N',			sub{ &_st_hs('���', '��');	}],
		[100,	1,		'���K�U��',			sub{ $com.=qq|<span class="die">$m�͎����̖����������܂����I</span>|; for my $y (@partys) { next if $m eq $y; $com .= $ms{$y}{hp} > 0 ? qq|$y��$e2j{hp}��<span class="heal">�S��</span>�����I| : qq|<span class="revive">$y�������Ԃ����I</span>|; $ms{$y}{hp} = $ms{$y}{mhp}; }; &defeat($m); $ms{$m}{mp} = 1; 	}],
		[130,	20,		'�O�����h�N���X',	sub{ &_damages($ms{$m}{df} * 1.5, '�U');	}],
		[160,	80,		'�U�I���N',			sub{ my($y) = &_check_party(shift, '�h��', '��'); return if !$y || $ms{$y}{hp} > 0; $com.=qq|�Ȃ�ƁA<span class="revive">$y�������Ԃ�܂����I</span>|; $ms{$y}{hp}=$ms{$y}{mhp};	}],
	);
}
sub skill_18 { # �V�g
	return (
		[5,		2,		'�L�A���[',			sub{ &_st_h(shift, '�ғ�', '��');	}],
		[15,	6,		'���ǂ�ӂ���',		sub{ &_st_ds('�x��', '�x', 70);	}],
		[30,	5,		'�߂��߂̂���',		sub{ &_st_hs('����', '��');	}],
		[50,	5,		'�}�z�J���^',		sub{ my($y) = &_check_party(shift, '������', '��'); return if !$y; $ms{$y}{tmp} = '������'; $com.=qq|<span class="tmp">$y�͖��@�̕ǂŎ��ꂽ�I</span>|;	}],
		[70,	27,		'�Ă񂵂̂�������',	sub{ for my $y (@partys) { next if $ms{$y}{hp} > 0; if (rand(2) < 1) { $com.=qq|�Ȃ�ƁA<b>$y</b>�� <span class="heal">�����Ԃ�</span> �܂����I|; $ms{$y}{hp}=int($ms{$y}{mhp} * 0.5); } else { $com.=qq|�������A<b>$y</b>�͐����Ԃ�Ȃ������c|; }; }; 	}],
		[90,	25,		'�x�z�}���[',		sub{ &_heals(120, '��');	}],
		[120,	80,		'�U�I���N',			sub{ my($y) = &_check_party(shift, '�h��', '��'); return if !$y || $ms{$y}{hp} > 0; $com.=qq|�Ȃ�ƁA<span class="revive">$y�������Ԃ�܂����I</span>|; $ms{$y}{hp}=$ms{$y}{mhp};	}],
	);
}
sub skill_19 { # �Ŗ����m
	return (
		[4,		7,		'���J�i��',		sub{ &_st_downs(0.25, '��', 'df');	}],
		[8,		5,		'�}�z�J���^',	sub{ my($y) = &_check_party(shift, '������', '��'); return if !$y; $ms{$y}{tmp} = '������'; $com.=qq|<span class="tmp">$y�͖��@�̕ǂŎ��ꂽ�I</span>|;	}],
		[16,	10,		'���_�p�j',		sub{ &_st_ds('����', '��', 50);	}],
		[25,	14,		'�U�L',			sub{ &_death(shift, '����', '��', 20);	}],
		[40,	10,		'�}�z�g�[��',	sub{ &_st_ds('����', '��', 70);	}],
		[60,	18,		'�x�M���S��',	sub{ &_damages(125, '��', 1);	}],
		[70,	2,		'�}�z�g��',		sub{ my($y, $v) = &_st_down(shift, 0.25, '��', 'mp'); return if !$y; &_mp_h($m, $v, '��');	}],
		[110,	32,		'�U���L',		sub{ &_deaths('����', '��', 20);	}],
	);
}
sub skill_20 { # ����
	return (
		[4,		4,		'���������ǂ�',			sub{ &_st_d(shift, '����', '�x', 85);	}],
		[9,		6,		'���f�B�E�B�b�v',		sub{ my($y, $v) = &_damage(shift, $ms{$m}{at}*0.9, '�U'); return if !$y; $v = int($v * 0.1); &_mp_h($m, $v, '�U');		}],
		[16,	6,		'�}�W�b�N�o���A',		sub{ for my $y (@partys) { return if $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '���y��'; $com.=qq|<span class="tmp">$y�͖��@�̌��Ŏ��ꂽ�I</span>|; };	}],
		[20,	9,		'���܂�����',			sub{ &_st_ds('����', '��', 35);	}],
		[36,	7,		'���_�p�j�_���X',		sub{ &_st_ds('����', '�x', 60);	}],
		[60,	24,		'���̂��ǂ�',			sub{ &_deaths('����', '�x', 17);	}],
		[100,	18,		'�N�B�[���E�B�b�v',		sub{ my($y, $v) = &_damage(shift, $ms{$m}{at}*1.7, '�U'); return if !$y; $v = int($v * 0.5); &_heal($m, $v, '�U');		}],
	);
}
sub skill_21 { # �ް����
	return (
		[10,	4,		'����������',	sub{ my($y, $v) = &_damage(shift, $ms{$m}{df}*1.6, '�U'); return if $v <= 0; &_risk($v * 0.07);			}],
		[20,	5,		'�����Ȃ���',	sub{ $ms{$m}{tmp} = '�󗬂�'; $com.=qq|<span class="tmp">$m �͍U�����󗬂����܂����Ƃ���</span>|;	}],
		[40,	12,		'��������',		sub{ &_st_ds('����', '�U', 60);		}],
		[60,	5,		'���Ă�',		sub{ $com.=qq|<span class="tmp">$m�͎����C�ɂ������Ă݂ōU���I</span>|; &_damage(shift, $ms{$m}{at}*2, '�U'); $ms{$m}{tmp}='�Q�{';	}],
		[80,	6,		'����͂���',	sub{ my($y, $v) = &_damage(shift, $ms{$m}{at}*1.6, '�U'); return if $v <= 0; &_risk($v * 0.05);		}],
		[110,	9,		'�݂Ȃ��낵',	sub{ my $y= rand(4)<1 ? $partys[int rand @partys] : $enemys[int rand @enemys]; $y=$m if $ms{$y}{hp} <= 0; my $v = int( ($ms{$m}{at} * 3.0 - $ms{$y}{df} * 0.4) * ((rand(0.3)+0.9) * $ms{$m}{ten}) ); $v = int(rand(2)+1) if $v < 1; $ms{$m}{ten}=1; $ms{$y}{hp}-=$v; $ms{$y}{hp}=0 if $ms{$y}{hp}<0; $com.=qq|<b>$y</b>�� <span class="damage">$v</span> �̃_���[�W�I|; if ($ms{$y}{hp} <= 0) { $ms{$y}{hp} = 0; $com .= qq!<span class="die">$y��|�����I</span>!; &defeat($y); }	}],
	);
}
sub skill_22 { # �Í��R�m
	return (
		[10,	5,		'���񂱂�',			sub{ my($y, $v) = &_damage(shift, $ms{$m}{at}*1.5, '�U'); return if $v <= 0; $ms{$m}{hp} > 999 ? &_risk($v * 0.1) : &_risk($ms{$m}{hp} * 0.1);		}],
		[20,	9,		'�߂��₭',			sub{ my $v = int($ms{$m}{df} * 0.5); $ms{$m}{df} -= $v; $com.=qq|$m��<span class="st_down">$e2j{df}�� $v ������܂����I</span>|; &_st_up($m, 1.0, '��', 'at');	}],
		[40,	16,		'�i�C�g���A',		sub{ &_st_ds('����', '��', 50);	}],
		[70,	10,		'�_�[�N�u���C�N',	sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at}*1.2, '�U'); return if !$y || $ms{$y}{hp} <= 0; &_st_down($y, 0.1, '�U', 'hit');	}],
		[140,	40,		'���񂱂�����',		sub{ my($y, $v) = &_damage(shift, $ms{$m}{at}*2.5, '�U'); return if $v <= 0; $ms{$m}{hp} > 999 ? &_risk($v * 0.2) : &_risk($ms{$m}{hp} * 0.2);		}],
	);
}
sub skill_23 { # ���R�m
	return (
		[10,	5,		'�W�����v',			sub{ &_damage(shift, $ms{$m}{ag}*1.8, '�U');	}],
		[30,	25,		'�h���S���p���[',	sub{ &_st_up($m, 0.4, '�U', 'at'); &_st_up($m, 0.4, '�U', 'df');	}],
		[50,	18,		'��イ����',		sub{ my($y, $v) = &_damage(shift, $ms{$m}{at}*0.9, '�U'); return if !$y; &_heal($m, $v, '�U');	}],
		[70,	14,		'�n�C�W�����v',		sub{ for my $i (1..2) { last if $ms{$m}{hp} <= 0; &_damage(shift, $ms{$m}{ag} * 2.2, '�U'); };	}],
		[130,	35,		'�O���O�j��',		sub{ &_damage(shift, $ms{$m}{at}*1.4, '�U', 1);	}],
	);
}
sub skill_24 { # �����m
	return (
		[10,	6,		'�����񂬂�',		sub{ &_damage(shift, $ms{$m}{at}*1.2, '�U');	}],
		[30,	6,		'���^������',		sub{ &_damage(shift, $ms{$m}{at}*0.4, '��', 1);	}],
		[50,	16,		'�o�C�L���g',		sub{ &_st_up(shift, 1.0, '��', 'at');	}],
		[70,	14,		'���Ȃ��܂���',		sub{ &_damage(shift, $ms{$m}{at}*1.5, '�U');	}],
		[130,	25,		'�M�K�X���b�V��',	sub{ &_damage(shift, 230, '�U', 1);	}],
	);
}
sub skill_25 { # �ݸ
	return (
		[5,		8,		'�܂킵����',		sub{ &_damages($ms{$m}{at}*0.8, '�U');			}],
		[15,	3,		'�`���N��',			sub{ &_heal($m, 100, '�U'); $ms{$m}{hit} = 95;	}],
		[30,	15,		'���Ă�',			sub{ $com.=qq|<span class="st_down">$m�͎����C�ɂ������Ă݂ōU���I</span>|; &_damage(shift, $ms{$m}{at}*2, '�U'); $ms{$m}{tmp}='�Q�{';		}],
		[50,	5,		'�J�E���^�[',		sub{ $ms{$m}{tmp}='�U����'; $com.=qq|<span class="tmp">$m�͔����̂��܂����Ƃ����I</span>|;	}],
		[70,	3,		'�����ڂ�����',		sub{ $ms{$m}{tmp}='��h��'; $com.=qq|<span class="tmp">$m�͎��̂��܂����Ƃ����I</span>|;	}],
		[90,	12,		'���񂭂���',		sub{ &_damages(120, '�U', 1);	}],
		[110,	0,		'�ɂ�������',		sub{ $ms{$m}{tmp} = '���΂���'; for my $y (@partys) { next if $m eq $y; $ms{$y}{tmp} = '���΂�'; }; $com.=qq|<span class="tmp">$m�͒��Ԃ̑O�ɗ����͂��������I</span>|;	}],
		[130,	7,		'������������',		sub{ $ms{$m}{tmp} = '����'; $com.=qq|<span class="tmp">$m�͎��ʋC�̃I�[���ɂ܂ꂽ�I</span>|;	}],
	);
}
sub skill_26 { # �E��
	return (
		[5,		5,		'������̂���',		sub{ &_damages(50, '��', 1);	}],
		[15,	10,		'�₯������',		sub{ &_st_ds('���', '��', 35);		}],
		[30,	7,		'�}�k�[�T',			sub{ &_st_downs(0.2, '��', 'hit');			}],
		[40,	7,		'�����ǂ��̂���',	sub{ &_st_ds('�ғ�', '��', 60);		}],
		[50,	6,		'�s�I����',			sub{ &_st_ups(0.25, '��', 'ag');	}],
		[65,	11,		'���イ����Â�',	sub{ &_death(shift, '����', '�U', 19);	}],
		[80,	10,		'���̂т���',		sub{ &_st_up($m, 1.0, '��', 'ag');	}],
		[110,	15,		'�A�[�}�[�u���C�N',	sub{ my($y) = &_check_enemy(shift, '�j��', '�U'); return if !$y; $ms{$y}{tmp}=''; $ms{$y}{ten}=1; $ms{$y}{df}=$ms{$y}{mdf}; $com.="$y�̖h��̋����𕕂����I"; &_st_down($y, 0.1, '�U', 'df');	}],
	);
}
sub skill_27 { # �����m
	return (
		[5,		6,		'���Ȃ��ނ�',		sub{ &_st_downs(0.2, '��', 'hit');	}],
		[15,	5,		'���܂�����',		sub{ &_damage(shift, 80, '��', 1);	}],
		[25,	6,		'�{�~�I�X',			sub{ &_st_downs(0.3, '��', 'ag');	}],
		[40,	11,		'�q���_���R',		sub{ &_damages(80, '��', 1);	}],
		[55,	4,		'�U���n',			sub{ &_st_hs('����', '��');	}],
		[70,	5,		'��������',			sub{ for my $y (@partys) { next if $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '������'; $com.=qq|<span class="tmp">$y�̎���ɒǂ����������Ă���I</span>|;};	}],
		[90,	27,		'�}�q���h',			sub{ &_damages(160, '��', 1);	}],
		[110,	15,		'�E�F�|���u���C�N',	sub{ my($y) = &_check_enemy(shift, '�j��', '�U'); return if !$y; $ms{$y}{tmp}=''; $ms{$y}{ten}=1; $ms{$y}{at}=$ms{$y}{mat}; $com.="$y�̕���̋����𕕂����I"; &_st_down($y, 0.2, '�U', 'at');	}],
	);
}
sub skill_28 { # ��
	return (
		[5,		0,		'��������Ƃ�����',	sub{ $ms{$m}{hit}=95; $com.=qq|$m�͐S�𗎂�����<span class="st_up">���������񕜂���</span>|;	}],
		[15,	3,		'�݂˂���',			sub{ &_st_d(shift, '����', '�U', 80);	}],
		[30,	5,		'�����Ȃ���',		sub{ $ms{$m}{tmp} = '�󗬂�'; $com.=qq|<span class="tmp">$m�͍U�����󗬂����܂����Ƃ���</span>|;	}],
		[50,	0,		'���ɂȂ�',			sub{ if ($m{money} < 100) { $m{money} = 0; &_damages(50, '�U', 1); } else { $m{money} -= 100; &_damages(180, '�U', 1); }; 	}],
		[70,	4,		'����͂ǂ�',		sub{ $ms{$m}{tmp}='�U����'; $com.=qq|<span class="tmp">$m�͎��̂��܂����Ƃ����I</span>|;	}],
		[100,	20,		'����������',		sub{ &_st_ds('����', '�U', 65);	}],
		[140,	10,		'����Ă���',		sub{ &_death(shift, '����', '�U', 25);	}],
	);
}
sub skill_29 { # �������m
	return (
		[10,	4,		'�X���E',		sub{ &_st_down(shift,  0.45, '��', 'ag');	}],
		[20,	4,		'�w�C�X�g',		sub{ &_st_up(shift, 0.45, '��', 'ag');	}],
		[30,	14,		'�R���b�g',		sub{ my $v = int(rand(2)+2); for my $i (1..$v) { last if $ms{$m}{hp} <= 0; &_damage(undef, 50, '��', 1); };	}],
		[50,	9,		'�X���E�K',		sub{ &_st_downs(0.35, '��', 'ag');	}],
		[70,	9,		'�w�C�X�K',		sub{ &_st_ups(0.35, '��', 'ag');	}],
		[110,	30,		'�O���r�f',		sub{ &_st_down(shift, 0.5, '��', 'hp');	}],
		[150,	50,		'���e�I',		sub{ my $v = int(rand(3)+4); for my $i (1..$v) { last if $ms{$m}{hp} <= 0; &_damage(undef, 99, '��', 1); };	}],
	);
}
sub skill_30 { # �Ԗ����m
	return (
		[10,	5,		'�P�A��',			sub{ &_heal(shift, 60, '��');	}],
		[20,	5,		'�t�@�C�A',			sub{ &_damage(shift, 35, '��', 1);	}],
		[40,	5,		'�V�F��',			sub{ my($y) = &_check_party(shift, '���y��', '��'); return if !$y || $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '���y��'; $com.=qq|<span class="tmp">$y�͖��@�̌��Ŏ��ꂽ�I</span>|;	}],
		[60,	11,		'�t�@�C��',			sub{ &_damage(shift, 80, '��', 1);	}],
		[80,	7,		'���t���N',			sub{ my($y) = &_check_party(shift, '������', '��'); return if !$y; $ms{$y}{tmp} = '������'; $com.=qq|<span class="tmp">$y�͖��@�̕ǂŎ��ꂽ�I</span>|;	}],
		[100,	18,		'�P�A����',			sub{ &_heal(shift, 180, '��');			}],
		[120,	20,		'�����C�Y',			sub{ my($y) = &_check_party(shift, '����', '��'); return if !$y; $ms{$y}{tmp}='����'; $com.=qq|<span class="tmp">$y�͓V�g�̉��삪�����I</span>|;	}],
		[150,	40,		'��񂼂��܂ق�',	sub{ for my $i (1..2) { last if $ms{$m}{hp} <= 0; &_damage(undef, 180, '��', 1); };	}],
	);
}
sub skill_31 { # �����m
	return (
		[11,	11,		'���΂�',				sub{ $com.=qq|<span class="die">$m�͎��������I</span>|; &_damage(shift, $ms{$m}{hp}, '��', 1); &defeat($m);	}],
		[44,	4,		'���̃��[���b�g',		sub{ return if &is_bad_state('��'); my $y=$members[int(rand(@members))]; $y = $m if $ms{$y}{hp} <= 0; $com.="���̃��[���b�g����肾�����I�c�߯�c�߯�c�߯�߯��-[>[$y]"; if ($ms{$y}{hp} > 999 || $ms{$y}{df} > 999) { $com .= "$y�ɂ͂����Ȃ������c"; } else { $com .= qq|<span class="die">$y�͎���ł��܂����I</span>|; &defeat($y); };		}],
		[66,	18,		'�H�H�H�H',				sub{ &_damage(shift, $ms{$m}{mhp}-$ms{$m}{hp}+5, '��', 1);		}],
		[77,	34,		'�}�C�e�B�K�[�h',		sub{ &_st_ups(0.5, '��', 'df'); for my $y (@partys) { next if $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '���y��'; $com.=qq|<span class="tmp">$y�͖��@�̌��Ŏ��ꂽ�I</span>|;};	}],
		[94,	24,		'�l�o�S�O���r�K',		sub{ return if &is_bad_state('��'); for my $y (@members) { next unless $ms{$y}{mp}; next if $ms{$y}{hp} <= 0; next if $ms{$y}{mp} % 4 != 0; next if $ms{$y}{hp} > 999; $ms{$y}{hp} = int($ms{$y}{hp}*0.25); $ms{$y}{hp} = 1 if $ms{$y}{hp} <= 0; $com.=qq|$y��<span class="st_down">$e2j{mhp}��1/4�ɂȂ����I</span>|; };	}],
		[121,	36,		'�z���C�g�E�B���h',		sub{ &_heals($ms{$m}{hp}, '��');	}],
		[155,	25,		'�l�o�T�f�X',			sub{ return if &is_bad_state('��'); for my $y (@members) { next unless $ms{$y}{mp}; next if $ms{$y}{hp} <= 0; next if $ms{$y}{mp} % 5 != 0; next if $ms{$y}{hp} > 999; $ms{$y}{hp} = 0; $com.=qq|<span class="die">$y�͎���ł��܂����I</span>|; };	}],
	);
}
sub skill_32 { # �����m
	return (
		[5,		5,		'�`���R�{',			sub{ if (rand(4)<1) { $com.="���f�u�`���R�{��"; &_damage(shift, 100, '��', 1); } else { $com.="���`���R�{�L�b�N��"; &_damage(shift, 30, '��', 1); };	}],
		[25,	10,		'�V���t',			sub{ $com.="�������̕���"; &_heals(50, '��');		}],
		[50,	20,		'�S�[����',			sub{ return if &is_bad_state('��'); $com.="�����̕ǁ�";   for my $y (@partys) { next if $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '�U�y��'; $com.=qq|<span class="tmp">$y�̓S�[�����Ɏ���Ă���I</span>|;};	}],
		[70,	30,		'�J�[�o���N��',		sub{ return if &is_bad_state('��'); $com.="�����r�[�̌���"; for my $y (@partys) { next if $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '������'; $com.=qq|<span class="tmp">$y�͖��@�̕ǂɎ��ꂽ�I</span>|;};	}],
		[100,	40,		'�t�F�j�b�N�X',		sub{ return if &is_bad_state('��'); $com.="���]���̉���";   for my $y (@partys) { next if $ms{$y}{hp}  > 0; $ms{$y}{hp}=int($ms{$y}{mhp}*0.15); $com.=qq|<span class="revive">$y�������Ԃ����I</span>|; };	}],
		[150,	50,		'�o�n���[�g',		sub{ $com.="�����K�t���A��"; &_damages(220, '��', 1);	}],
	);
}
sub skill_33 { # ����
	return (
		[5,		6,		'�}�W�b�N�o���A',	sub{ return if &is_bad_state('��'); for my $y (@partys) { return if $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '���y��'; $com.=qq|<span class="tmp">$y�͖��@�̌��Ŏ��ꂽ�I</span>|; };	}],
		[15,	12,		'�C�I��',			sub{ &_damages(70, '��', 1);	}],
		[30,	7,		'�t�o�[�n',			sub{ return if &is_bad_state('��'); for my $y (@partys) { next if $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '���y��'; $com.=qq|<span class="tmp">$y�͕s�v�c�ȕ��ɕ�܂ꂽ�I</span>|;};	}],
		[70,	25,		'�x�z�}���[',		sub{ &_heals(120, '��');	}],
		[100,	16,		'�o�C�L���g',		sub{ &_st_up(shift, 1.0, '��', 'at')	}],
		[130,	34,		'�C�I�i�Y��',		sub{ &_damages(160, '��', 1);	}],
		[160,	80,		'�U�I���N',			sub{ my($y) = &_check_party(shift, '�h��', '��'); return if !$y || $ms{$y}{hp} > 0; $com.=qq|�Ȃ�ƁA<span class="revive">$y�������Ԃ�܂����I</span>|; $ms{$y}{hp}=$ms{$y}{mhp};	}],
	);
}
sub skill_34 { # �E��
	return (
		[10,	0,		'���΂�',			sub{ my($y) = &_check_party(shift, '���΂�', '�U'); return if !$y || $y eq $m; $ms{$m}{tmp} = '���΂���'; $ms{$y}{tmp} = '���΂�'; $com.=qq|<span class="tmp">$m��$y�����΂��Ă���</span>|;	}],
		[30,	15,		'���C�f�C��',		sub{ &_damage(shift, 110, '��', 1);			}],
		[60,	25,		'�߂�����',			sub{ &_heal($m, 300, '��');		}],
		[90,	40,		'�M�K�f�C��',		sub{ &_damages(180, '��', 1);			}],
		[120,	6,		'�A�X�g����',		sub{ return if &is_bad_state('��'); $ms{$m}{tmp}='������'; $com.=qq|<span class="tmp">$m�͖��@���������Ȃ��̂ɂȂ����I</span>|;	}],
		[150,	80,		'�x�z�}�Y��',		sub{ &_heals(999, '��');	}],
		[180,	30,		'�~�i�f�C��',		sub{ my($y) = &_check_enemy(shift, '�F', '��'); return if !$y; my $d = 100; for my $name (@partys) { next if $m eq $name || $ms{$name}{mp} < 15; $ms{$name}{mp}-=15; $d += 85; }; $com.=qq|$m�͒��Ԃ݂̂�Ȃ���͂��󂯂Ƃ����I| if $d > 100; &_damage($y, $d, '��', 1);	}],
	);
}
sub skill_35 { # ����
	return (
		[10,	4,		'�����Ȃ���',		sub{ $ms{$m}{tmp} = '�󗬂�'; $com.=qq|<span class="tmp">$m �͍U�����󗬂����܂����Ƃ���</span>|;	}],
		[30,	30,		'���Ă��͂ǂ�',	sub{ for my $y (@members) { my $tten=$ms{$y}{ten}; &reset_status($y); $ms{$y}{ten}=$tten; }; $com.=qq|<span class="st_down">�S�Ă̌��ʂ����������ꂽ�I</span>|;	}],
		[60,	14,		'�U�L',				sub{ &_death(shift, '����', '��', 20);	}],
		[90,	40,		'���Ⴍ�˂�',		sub{ &_damages(180, '��', 1);	}],
		[120,	25,		'�߂�����',			sub{ &_heal($m, 300, '��');	}],
		[150,	6,		'�A�X�g����',		sub{ return if &is_bad_state('��'); $ms{$m}{tmp}='������'; $com.=qq|<span class="tmp">$m�͖��@���������Ȃ��̂ɂȂ����I</span>|;	}],
		[180,	70,		'�W�S�X�p�[�N',		sub{ $is_add_effect = 1; &_damages(150, '��', 1); &_st_ds('���', '��', 20);		}],
	);
}
sub skill_36 { # ���̂܂ˎm
	return (
		[10,	5,		'���ǂ���̂܂�',	sub{ $ms{$m}{tmp} = '�x����'; $com.=qq|<span class="tmp">$m�͗x��܂˂��͂��߂��I</span>|;			}],
		[20,	5,		'�Ԃꂷ���̂܂�',	sub{ $ms{$m}{tmp} = '������'; $com.=qq|<span class="tmp">$m�͑���f���܂˂��͂��߂��I</span>|;		}],
		[40,	5,		'�܂ق����̂܂�',	sub{ $ms{$m}{tmp} = '������'; $com.=qq|<span class="tmp">$m�͖��@��������܂˂��͂��߂��I</span>|;	}],
		[60,	5,		'�����������̂܂�',	sub{ $ms{$m}{tmp} = '�U����'; $com.=qq|<span class="tmp">$m�͍U������܂˂��͂��߂��I</span>|;		}],
		[100,	50,		'���V���X',			sub{ my $y = shift; return if &is_bad_state('��'); $y = $members[int(rand(@members))] if !defined($ms{$y}{name}); return if $ms{$y}{hp} <= 0 || $ms{$y}{mhp} > 999 || $ms{$y}{mdf} > 999; for my $k (qw/hp mp at df ag/) { $ms{$m}{$k}=$ms{$y}{$k}; $ms{$m}{'m'.$k}=$ms{$y}{'m'.$k}; }; for my $k (qw/job sp old_job old_sp icon/) { $ms{$m}{$k}=$ms{$y}{$k}; }; $ms{$m}{mp} = 50 if $ms{$m}{mp} < 50; $com.=qq|<span class="st_up">$m��$y�Ɏp��ς��܂����I</span>|;	}],
	);
}
sub skill_37 { # ���E�m
	return (
		[5,		10,		'�}�z�g�[��',		sub{ &_st_ds('����', '��', 70);	}],
		[10,	1,		'�}�z�L�e',			sub{ return if &is_bad_state('��'); $ms{$m}{tmp} = '���z��'; $com.=qq|<span class="tmp">$m�͕s�v�c�Ȍ��ɕ�܂ꂽ�I</span>|;	}],
		[15,	6,		'���ǂ�ӂ���',		sub{ &_st_ds('�x��', '�x', 70);	}],
		[25,	6,		'�}�W�b�N�o���A',	sub{ for my $y (@partys) { return if $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '���y��'; $com.=qq|<span class="tmp">$y�͖��@�̌��Ŏ��ꂽ�I</span>|; };	}],
		[40,	5,		'�}�z�J���^',		sub{ my($y) = &_check_party(shift, '������', '��'); return if !$y; $ms{$y}{tmp} = '������'; $com.=qq|<span class="tmp">$y�͖��@�̕ǂŎ��ꂽ�I</span>|;	}],
		[60,	7,		'����΂�',			sub{ &_st_d(shift, '�U��', '��', 80);	}],
		[80,	25,		'�߂�����',			sub{ &_heal($m, 300, '��');	}],
		[100,	15,		'�ӂ�����',			sub{ my($y) = &_check_enemy(shift, '�j��', '�U'); return if !$y; $ms{$y}{tmp}=''; $ms{$y}{ten}=1; $ms{$y}{df}=$ms{$y}{mdf}; $ms{$y}{at}=$ms{$y}{mat}; $com.="$y�̕���Ɩh��̋����𕕈󂵂��I";		}],
	);
}
sub skill_38 { # ����߲�
	return (
		[10,	12,		'���イ����',		sub{ my($y, $v) = &_damage(shift, ($ms{$m}{mhp}-$ms{$m}{hp})*0.5+5, '��', 1); return if !$y; &_heal($m, $v, '��');	}],
		[20,	3,		'�A�X�s��',			sub{ my($y, $v) = &_st_down(shift, 0.2, '��', 'mp'); return if !$y; &_mp_h($m, $v, '��');	}],
		[30,	6,		'�A�X�g����',		sub{ return if &is_bad_state('��'); $ms{$m}{tmp}='������'; $com.=qq|<span class="tmp">$m�͖��@���������Ȃ��̂ɂȂ����I</span>|;	}],
		[60,	9,		'�߂��₭',			sub{ my $v = int($ms{$m}{df} * 0.5); $ms{$m}{df} -= $v; $com.=qq|<span class="st_down">$m��$e2j{df}�� $v ������܂����I</span>|; &_st_up($m, 1.0, '��', 'at');	}],
		[90,	9,		'���܂�����',		sub{ &_st_ds('����', '��', 35);		}],
		[130,	37,		'�M�K�h���C��',		sub{ my($y) = &_check_enemy(shift, '�z��', '��'); return if !$y; my $v = int($ms{$y}{hp}*0.5); $v = 300 if $v > 300; ($y) = &_damage($y, $v, '��', 1); return if !$y; &_heal($m, $v, '��');	}],
	);
}
sub skill_39 { # �ײ�
	return (
		[3,		5,		'�M��',			sub{ &_damages(25, '��', 1);	}],
		[7,		7,		'�X�N���g',		sub{ &_st_ups(0.25, '��', 'df');	}],
		[11,	3,		'�z�C�~',		sub{ &_heal(shift, 30, '��');	}],
		[16,	7,		'���J�i��',		sub{ &_st_downs(0.25, '��', 'df')	}],
		[28,	10,		'���_�p�j',		sub{ &_st_ds('����', '��', 50);	}],
		[50,	20,		'�U�I����',		sub{ my($y) = &_check_party(shift, '�h��', '��'); return if !$y || $ms{$y}{hp} > 0; if (rand(2) < 1) { $com.=qq|�Ȃ�ƁA<span class="revive">$y�������Ԃ�܂����I</span>|; $ms{$y}{hp}=int($ms{$y}{mhp} * 0.5); } else { $com.=qq|�������A$y�͐����Ԃ�Ȃ������c|; };	}],
		[99,	40,		'���Ⴍ�˂�',	sub{ &_damages(180, '��', 1);	}],
	);
}
sub skill_40 { # ʸ�����
	return (
		[25,	8,		'�����~',		sub{ &_damage(shift, 70, '��', 1);		}],
		[50,	11,		'�x�M���}',		sub{ &_damages(60, '��', 1);			}],
		[99,	1,		'�}�_���e',		sub{ &_damages($ms{$m}{mp} * 2, '��', 1); $ms{$m}{mp} = 1; 	}],
	);
}
sub skill_41 { # ��׺��
	return (
		[10,	1,		'�߂�������',		sub{ &_damages(15, '��', 1);	}],
		[30,	6,		'������̂���',		sub{ &_damages(55, '��', 1);	}],
		[60,	14,		'��������ӂԂ�',	sub{ &_damages(115, '��', 1);	}],
		[90,	9,		'�₯������',		sub{ &_st_ds('���', '��', 35);	}],
		[120,	34,		'�����₭����',		sub{ &_damages(195, '��', 1);	}],
	);
}
sub skill_42 { # ����
	return (
		[15,	7,		'�R���t��',			sub{ &_st_d(shift, '����', '��', 80);	}],
		[30,	6,		'�T�C���X',			sub{ &_st_d(shift, '����', '��', 90);	}],
		[55,	10,		'���̂т���',		sub{ &_st_up($m, 1.0, '��', 'ag');	}],
		[80,	4,		'�ǂ���������',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at} * 1.1, '�U'); return if !$y || $ms{$y}{hp} <= 0;  &_st_d($y, '�ғ�', '�U', 70);	}],
		[100,	8,		'�܂Ђ�������',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at} * 1.2, '�U'); return if !$y || $ms{$y}{hp} <= 0;  &_st_d($y, '���', '�U', 35);	}],
		[120,	42,		'���̂��񂱂�',		sub{ my($y) = &_check_enemy(shift, '�m��', '��'); return if !$y; if ($ms{$y}{mhp}>999 || $ms{$y}{mdf}>999) { $com.="$y�ɂ͂����Ȃ������I"; } elsif (rand(1.5)<1) { &_st_down($y, 0.75, '��', 'hp'); $ms{$y}{state}='�ғ�'; } else { $com.="$y�͂��킵���I"; };	}],
		[150,	24,		'���񂳂���',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at} * 1.7, '�U'); return if !$y || $ms{$y}{hp} <= 0; &_death($y, '����', '�U', 25);	}],
	);
}
sub skill_43 { # ��p�m
	return (
		[5,		2,		'�ǂ�����傤',		sub{ &_st_hs('�ғ�', '��');	}],
		[10,	3,		'�܂Ђ���傤',		sub{ &_st_hs('���', '��');	}],
		[20,	5,		'�߂��߂̂���',		sub{ &_st_hs('����', '��');	}],
		[40,	7,		'���W�F�l',			sub{ my($y) = &_check_party(shift, '��', '��'); return if !$y; $ms{$y}{tmp} = '��'; $com.=qq|<span class="tmp">$y�͗D�������ɕ�܂ꂽ�I</span>|;	}],
		[70,	10,		'�G�X�i',			sub{ my($y) = &_check_party(shift, '����', '��'); return if !$y; &_st_h($y, $ms{$y}{state}, '��');	}],
		[110,	35,		'�P�A���K',			sub{ &_heal(shift, 400, '��');			}],
		[150,	70,		'�A���C�Y',			sub{ my($y) = &_check_party(shift, '�h��', '��'); return if !$y || $ms{$y}{hp} > 0; $com.=qq|�Ȃ�ƁA<span class="revive">$y�������Ԃ�܂����I</span>|; $ms{$y}{hp}=$ms{$y}{mhp};	}],
	);
}
sub skill_44 { # �����
	return (
		[20,	4,		'�`���R�{�L�b�N',	sub{ &_damage(shift, $ms{$m}{at} * 1.4, '�U');	}],
		[40,	5,		'�`���R�K�[�h',		sub{ &_st_up($m, 0.5, '��', 'df');	}],
		[60,	8,		'�`���R�A�^�b�N',	sub{ my($y, $v) = &_damage(shift, $ms{$m}{df} * 2.0, '�U'); return if $v <= 0; &_risk($v * 0.07);	}],
		[80,	14,		'�`���R�{�[��',		sub{ &_damage(shift, 170, '��', 1);	}],
		[100,	7,		'�`���R�P�A��',		sub{ &_heal(shift, 150, '��');	}],
		[120,	15,		'�`���R�{�b�N��',	sub{ &_damage(shift, $ms{$m}{ag} * 1.8, '��', 1);		}],
	);
}
sub skill_45 { # Ӱ���
	return (
		[10,	5,		'���܂��Ȃ�',		sub{ my($y) = &_check_party(shift, '����', '��'); return if !$y; $ms{$y}{hit}=95; $com.=qq|<span class="st_up">$y�̖��������񕜂���</span>|;		}],
		[30,	8,		'�X�g�b�v',			sub{ &_st_d(shift, '����', '��', 85);	}],
		[50,	7,		'�E�[���K�[�h',		sub{ &_st_up($m, 0.5, '��', 'df'); $ms{$m}{tmp} = '���y��'; $com.=qq|<span class="tmp">$m�͖��@�̌��Ŏ��ꂽ�I</span>|;	}],
		[70,	3,		'�}�z�g�����ǂ�',	sub{ my($y, $v) = &_st_down(shift, 0.18, '�x', 'mp'); return if !$y; &_mp_h($m, $v, '�x');	}],
		[90,	30,		'�J�G���̂���',		sub{ my($y, $v) = &_st_down(shift, 0.4, '��', 'at'); return if !$y; &_st_down($y, 0.4, '��', 'df'); $ms{$y}{icon} = "chr/022.gif"; $com .= "$y�̓J�G���̎p�ɂȂ����I";	}],
		[120,	7,		'���W�F�l',			sub{ my($y) = &_check_party(shift, '��', '��'); return if !$y; $ms{$y}{tmp} = '��'; $com.=qq|<span class="tmp">$y�͗D�������ɕ�܂ꂽ�I</span>|;	}],
		[150,	40,		'�A���e�}�`���[�W',	sub{ &_damage(shift, 300, '�U', 1);		}],
	);
}
sub skill_46 { # �ެ���װ
	return (
		[10,	7,		'�w�u���X���b�g',		sub{ my @m = ('��','��','��','��','�V'); my @s = (); $s[$_] = int(rand(@m)) for (0 .. 2); $com .= "�y$m[$s[0]]�z�y$m[$s[1]]�z�y$m[$s[2]]�z"; if ($s[0] == $s[1] && $s[1] == $s[2]) { my $v = int( ($s[0]+2) * 100 ); $s[0] == $#m ? &_deaths('����', '��', 80) : $s[0] == 0 || $s[0] == 2 ? &_heals($v, '��') : &_damages($v, '��'); } else { my $v = int( ($s[0] + $s[1] + $s[2]) * 7 ); &_damages($v, '��', 1); };		}],
		[30,	14,		'���������̃_�[�c',		sub{ &_death(shift, '����', '�U', 20);	}],
		[60,	6,		'�����܂̃_�C�X',		sub{ my $d1 = int(rand(6)+1); my $d2 = int(rand(6)+1); my $d3 = int(rand(6)+1); my $v = int(($d1*100+$d2*10+$d1)*0.5); $com.="[$d1][$d2][$d3]"; &_damage(shift, $v, '��', 1); return if $v <= 0; &_risk((6-$d1)*10+(6-$d2)+(6-$d1)*0.1);		}],
		[80,	4,		'���̃��[���b�g',		sub{ return if &is_bad_state('��'); my $y=$members[int(rand(@members))]; $y = $m if $ms{$y}{hp} <= 0; $com.="���̃��[���b�g����肾�����I�c�߯�c�߯�c�߯�߯��-[>[$y] "; if ($ms{$y}{hp} > 999 || $ms{$y}{df} > 999) { $com .= "$y�ɂ͂����Ȃ������c"; } else { $com .= qq|<span class="die">$y�͎���ł��܂����I</span>|; &defeat($y); };	}],
		[140,	36,		'�C�J�T�}�̃_�C�X',		sub{ my $d1 = int(rand(3)+1); my $d2 = int(rand(6)+1); my $d3 = int(rand(6)+1); my $v = $d1*100+$d2*10+$d1; $com.="[$d1][$d2][$d3]"; &_damage(shift, $v, '��', 1);	}],
	);
}
sub skill_47 { # �ټެ�
	return (
		[20,	5,		'�u���C�o�[',				sub{ &_damage(shift, $ms{$m}{at}*1.2, '�U');	}],
		[50,	9,		'���傤����',				sub{ my($y, $v) = &_damage(shift, $ms{$m}{at}*1.6, '�U'); return if $v <= 0; &_risk($v * 0.06);	}],
		[80,	20,		'���e�I���C��',				sub{ my($y) = &_damage(shift, $ms{$m}{at}*1.8, '�U'); return if !$y; my $v = int($ms{$m}{at} * 0.1); $ms{$m}{at} -= $v; $com .= qq|$m��<span class="st_down">$e2j{at}�� $v ���������I</span>|;		}],
		[120,	36,		'�N���C���n�U�[�h',			sub{ my($y) = &_check_enemy(shift, '����', '�U'); return if !$y; my $v = $ms{$y}{mhp}-$ms{$y}{hp} + 10; $v = 400 if $v > 400; &_damage($y, $v, '�U', 1);	}],
		[160,	40,		'���傤���イ�Ԃ���͂���',	sub{ for my $i (1..4) { last if $ms{$m}{hp} <= 0; &_damage(undef, $ms{$m}{at}, '�U'); };		}],
	);
}
sub skill_48 { # �V�g
	return (
		[40,	56,		'�o�C�I�K',				sub{ $is_add_effect = 1; &_damages(120, '��', 1); &_st_ds('�ғ�', '��', 40);		}],
		[80,	66,		'��݂̂Ă�',			sub{ $is_add_effect = 1; &_damages(70, '��', 1);  &_st_ds('����', '��', 30);		}],
		[120,	66,		'�V���h�E�t���A',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, 300, '��', 1); return if !$y || $ms{$y}{hp} <= 0; &_st_down($y, 0.08, '��', 'hit');	}],
		[160,	44,		'������Ȃ��Ă�',		sub{ my($y) = &_check_enemy(shift, '�m��', '��'); return if !$y; if ($ms{$y}{mhp}>999 || $ms{$y}{mdf}>999) { $com.="$y�ɂ͂����Ȃ������I"; } elsif (rand(3)<1) { $ms{$y}{hp}=1; $com.=qq|$y��<span class="st_down">�����͂�������</span>�I|; } else { $com.="$y�͂��킵���I"; };	}],
		[200,	46,		'�͂��Ƃ���������',		sub{ &_damages($ms{$m}{at} * 1.2, '�U');		}],
	);
}

# ���p�[�e�B�[II�ǉ��� 
sub skill_49 { # ���܂˂����m
	return (
		[100,	10,		'���{��',			sub{ my($y) = &_check_party(shift, '����', '��'); return if !$y; &_st_h($y, $ms{$y}{state}, '��');	}],
		[200,	20,		'�I�j�I���V�[���h',	sub{ &_st_up($m, 0.6, '�U', 'df'); $ms{$m}{tmp} = '�U�y��'; $com.=qq|<span class="tmp">$m�͎����ł߂��I</span>|;	 	}],
		[300,	30,		'�I�j�I���\�[�h',	sub{ &_damage(shift, $ms{$m}{at}*1.6, '�U');	}],
	);
}
sub skill_50 { # ���юm
	return (
		[10,	5,		'�|�[�V����',			sub{ &_heal(shift, 80, '��');	}],
		[25,	3,		'�L���A�u���C���h',		sub{ my($y) = &_check_party(shift, '����', '��'); return if !$y; $ms{$y}{hit}=95; $com.=qq|<span class="st_up">$y�̖��������񕜂���</span>|;	}],
		[40,	14,		'�f�X�|�[�V����',		sub{ &_death(shift, '����', '��', 17);	}],
		[55,	10,		'�h���S���A�[�}�[',		sub{ my($y) = &_st_up(shift, 0.4, '��', 'df'); $ms{$y}{tmp} = '���y��'; $com.=qq|<span class="tmp">$y�͕s�v�c�ȕ��ɕ�܂ꂽ�I</span>|;	}],
		[75,	24,		'�n�C�|�[�V����',		sub{ &_heal(shift, 200, '��');	}],
		[110,	50,		'�G�[�e��',				sub{ &_mp_h(shift, 50, '��');	}],
		[145,	1,		'���X�g�G���N�T�[',		sub{ my($y) = &_check_party(shift, '�Ō�', '��'); return if !$y || $m eq $y; $com.=qq|<span class="die">$m�͎����̖����������܂����I</span>|; $com .= $ms{$y}{hp} > 0 ? qq|$y��$e2j{hp}��$e2j{mp}��<span class="heal">�S��</span>�����I| : qq|<span class="revive">$y�������Ԃ����I</span>|; $ms{$y}{hp} = $ms{$y}{mhp}; $ms{$y}{mp} = $ms{$y}{mmp}; &defeat($m); $ms{$m}{mp} = 1;	}],
	);
}
sub skill_51 { # �������m
	return (
		[10,	6,		'�܂Ԃ����Ђ���',		sub{ &_st_downs(0.2, '��', 'hit');		}],
		[30,	11,		'�Ђ���݂̂��т�',		sub{ for my $y (@partys) { $ms{$y}{hit}=95; }; $com.=qq|<span class="st_up">$m�����̖��������񕜂���</span>|;	}],
		[50,	14,		'���₵�̂Ђ���',		sub{ &_heals(int(rand(50)+50), '��');	}],
		[80,	16,		'���₵���Ђ���',		sub{ my @randoms = ('����', '����'); for my $name (@enemys) { &_st_d($name, $randoms[int(rand(@randoms))], '��', 50); };		}],
		[110,	34,		'�Ђ���̂��΂�',		sub{ &_damages(170, '��', 1);	}],
		[130,	30,		'���ڂ��̂Ђ���',		sub{ for my $y (@partys) { next if $ms{$y}{hp} > 0; if (rand(5) < 1) { $com.=qq|�Ȃ�ƁA<b>$y</b>�� <span class="heal">�����Ԃ�</span> �܂����I|; $ms{$y}{hp}=$ms{$y}{mhp}; } else { $com.=qq|�������A<b>$y</b>�͐����Ԃ�Ȃ������c|; }; }; 	}],
		[160,	46,		'���ڂ��̂Ђ���',		sub{ $is_add_effect = 1; &_deaths('����', '��', 10); &_damages(70, '��', 1); 		}],
	);
}
sub skill_52 { # ���l
	return (
		[20,	4,		'�Ђ�����',				sub{ &_damage(shift, $ms{$m}{at}*1.2, '�U');	}],
		[50,	8,		'����������߂�',		sub{ &_st_up($m, 1.0, '�U', 'at');		}],
		[80,	15,		'�A�[�}�[�u���C�N',		sub{ my($y) = &_check_enemy(shift, '�j��', '�U');  return if !$y; $ms{$y}{tmp}=''; $ms{$y}{ten}=1; $ms{$y}{df}=$ms{$y}{mdf}; $com.="$y�̖h��̋����𕕂����I"; &_st_down($y, 0.1, '�U', 'df');	}],
		[130,	20,		'����������',			sub{ $ms{$m}{tmp}='�Q�{'; &tenshon($m); &tenshon($m);	}],
		[150,	30,		'�����ڂ�����',			sub{ &_damages(200, '�U', 1); $ms{$m}{tmp}='�Q�{';	}],
	);
}
sub skill_53 { # 峎t
	return (
		[5,		3,		'�����̂���',		sub{ &_st_d(shift, '����', '��', 80);	}],
		[15,	4,		'�ǂ��̂���',		sub{ &_st_d(shift, '�ғ�', '��', 80);	}],
		[30,	16,		'�ނ��̂���',		sub{ my @randoms = ('�ғ�', '���', '����'); for my $name (@enemys) { &_st_d($name, $randoms[int(rand(@randoms))], '��', 60); };		}],
		[55,	15,		'�����܂̂��',		sub{ my($y) = &_check_party(shift, '�U����', '��'); return if !$y; $ms{$y}{tmp} = '�U����'; $com.=qq|<span class="tmp">$y�͓���Ȏ��Ŏ��ꂽ�I</span>|;	}],
		[80,	8,		'�����̂�',			sub{ &_st_d(shift, '�U��', '��', 80);	}],
		[120,	7,		'����肢��',		sub{ my($y) = &_check_enemy(shift, '����', '��'); return if !$y; $com.="$m��$y����������I$y: ���������� "; $buf_m = $m; $m = $y; &kougeki(); $m = $buf_m;	}],
	);
}
sub skill_54 { # ���e�m
	return (
		[5,		4,		'���������Ⴐ��',	sub{ &_st_d(shift, '����', '�U', 80);	}],
		[15,	7,		'������',			sub{ &_damage(shift, $ms{$m}{at}*0.6, '�U', 1);		}],
		[30,	0,		'�����̂�',			sub{ $ms{$m}{hit}=95; $com.=qq|$m�͐S�𗎂�����<span class="st_up">���������񕜂���</span>|;	}],
		[60,	12,		'���񂹂˂炢',	sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at}*0.5, '�U', 1); return if !$y || $ms{$y}{hp} <= 0; &_st_d($y, '����', '�U', 30);	}],
		[90,	34,		'�N���C���A',		sub{ &_damages(180, '�U', 1);	}],
		[130,	44,		'�݂��ꂤ��',		sub{ my $v = int(rand(2)+3); for my $i (1..$v) { last if $ms{$m}{hp} <= 0; &_damage(undef, $ms{$m}{at}*0.7, '�U', 1); };		}],
	);
}
sub skill_55 { # �d��
	return (
		[5,		0,		'�߂�����',			sub{ my $y=$members[int(rand(@members))]; $ms{$y}{hit} = int($ms{$y}{hit}*0.5); $com.=qq|$m��$y�ɖډB������<span class="st_down">$y�̖����������������I</span>|;	}],
		[10,	4,		'�悤�����̂�',		sub{ my($y, $v) = &_st_down(shift, 0.15, '�U', 'mp'); return if !$y; &_mp_h($m, $v, '�U');	}],
		[20,	0,		'�������ӂ���',		sub{ my $y=$members[int(rand(@members))]; $ms{$y}{state}='����'; $ms{$y}{ten}=1; $com.=qq|$m��$y�̌����ӂ���<span class="state">$y�͖����ɂȂ�܂����I</span>|;		}],
		[35,	0,		'���傤�͂�',		sub{ for my $y (@members) { next if $ms{$y}{hp} <= 0 || $m eq $y || rand(2) < 1; &tenshon($y); };	}],
		[50,	8,		'�ł���߂�',		sub{ &_damages($ms{$m}{ag}*1.4, '�U');	}],
		[65,	0,		'���炩��',			sub{ my $y = shift; ($y) = defined($ms{$y}{name}) ? $y : &_check_enemy($y, '�e��', '��'); &tenshon($y);		}],
		[80,	0,		'��т��ӂ�',		sub{ &_yubiwofuru;	}],
	);
}
sub skill_56 { # ���ް��
	return (
		[6,		5,		'�C�I',				sub{ &_damages(25, '��', 1);	}],
		[16,	1,		'�}�z�L�e',			sub{ return if &is_bad_state('��'); $ms{$m}{tmp} = '���z��'; $com.=qq|<span class="tmp">$m�͕s�v�c�Ȍ��ɕ�܂ꂽ�I</span>|;	}],
		[36,	12,		'�C�I��',			sub{ &_damages(70, '��', 1);	}],
		[46,	10,		'�p���v���e',		sub{ &_parupunte;	}],
		[66,	34,		'�C�I�i�Y��',		sub{ &_damages(160, '��', 1);	}],
		[96,	0,		'�f�r���e�C��',		sub{ &_yubiwofuru;	}],
	);
}
sub skill_57 { # ���
	return (
		[10,	3,		'�z�C�~',			sub{ &_heal(shift, 30, '��');	}],
		[20,	6,		'�t���b�V���A���[',	sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at}*1.2, '�U'); return if !$y || $ms{$y}{hp} <= 0; &_st_down($y, 0.07, '�U', 'hit');	}],
		[40,	10,		'�x�z�C�~',			sub{ &_heal(shift, 90, '��');	}],
		[60,	20,		'�����z�[�A���[',	sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at}*1.1, '�U'); return if !$y || $ms{$y}{hp} <= 0; &_st_d($y, '����', '�U', 55);	}],
		[80,	20,		'�U�I����',			sub{ my($y) = &_check_party(shift, '�h��', '��'); return if !$y || $ms{$y}{hp} > 0; if (rand(2) < 1) { $com.=qq|�Ȃ�ƁA<span class="revive">$y�������Ԃ�܂����I</span>|; $ms{$y}{hp}=int($ms{$y}{mhp} * 0.5); } else { $com.=qq|�������A$y�͐����Ԃ�Ȃ������c|; };	}],
		[100,	4,		'�悤�����̂�',		sub{ my($y, $v) = &_st_down(shift, 0.15, '�U', 'mp'); return if !$y; &_mp_h($m, $v, '�U');	}],
		[120,	33,		'�o�C�V�I��',		sub{ &_st_ups(0.7, '��', 'at');		}],
	);
}
sub skill_58 { # �ް����
	return (
		[20,	26,		'���C�t�V�F�C�o�[',		sub{ my($y) = &_check_enemy(shift, '�m��', '��'); return if !$y; if (rand(5)>1) { &_st_down($y, 0.7, '��', 'hp'); } else { $com.="$y�͂��킵���I"; };	}],
		[50,	9,		'�g�����X',				sub{ $ms{$m}{state}=''; &_st_up($m, 1.0, '�U', 'at'); &_st_up($m, 1.0, '�U', 'ag'); $ms{$m}{tmp} = '���z��'; $ms{$m}{state}='����'; $com.="$m�̓g�����X��ԂɂȂ����I";		}],
		[80,	16,		'�̂낢',				sub{ my @randoms = ('����', '�U��', '����'); for my $name (@enemys) { &_st_d($name, $randoms[int(rand(@randoms))], '��', 70); };		}],
		[110,	6,		'�l�o�o�X�^�[',			sub{ &_st_down(shift, 0.4, '��', 'mp');	}],
		[140,	33,		'��������',				sub{ $ms{$m}{tmp}='�Q�{'; &tenshon($m); &tenshon($m); 		}],
		[160,	66,		'�n���[�V����',			sub{ for my $y (@enemys) { if (rand(3)>1) { &_st_down($y, 0.75, '��', 'hp'); } else { $com.="$y�͂��킵���I"; }; };	}],
	);
}
sub skill_59 { # �ײ�ײ�ް
	return (
		[10,	30,		'��т���',				sub{ my $n = '@�ײ�@'; if (defined $ms{$n}{name}) { $com.="$n���Ăяo���̂Ɏ��s�����c"; return; }; $m{lv} < 40 ? &_add_party($n, 'mon/001.gif', 70, 120, 50, 30, 120) : $m{lv} < 70 ? &_add_party($n, 'mon/006.gif', 180, 80, 80, 50, 200) : &_add_party($n, 'mon/004.gif', 5, 10, 10, 950, 950); $com.="$n���퓬�ɎQ�������I"; 	}],
		[11,	0,		'�ɂ���',				sub{ my $n = '@�ײ�@'; return if !defined($ms{$n}{name}) || $ms{$n}{hp} <= 0; $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; $com.="$n���퓬���瓦���o�����I"; 	}],
		[12,	0,		'���������߂��ꂢ',		sub{ my $n = '@�ײ�@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(39); return if !$n || $ms{$n}{hp} <= 0; $com.="$n�F ���������� "; $buf_m = $m; $m = $n; &kougeki(shift); $m = $buf_m;	}],
		[30,	30,		'�Ђ����߂��ꂢ',		sub{ my $n = '@�ײ�@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(39); return if !$n || $ms{$n}{hp} <= 0; $com.="$n�F "; if (rand(2)<1) { $com.='���X���A�^�b�N '; &_damage(shift, $ms{$n}{at} * 1.5, '�U'); }elsif(rand(2)<1){ $com.='���X���X�g���C�N '; &_damage(shift, $ms{$n}{at} * 1.2, '�U', 1); }else{ $com.='�����Ⴍ�˂� '; &_damages(220, '��', 1); }; 	}],
		[100,	10,		'�ڂ�����߂��ꂢ',		sub{ my $n = '@�ײ�@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(39); return if !$n || $ms{$n}{hp} <= 0; $ms{$n}{tmp} = '�h��'; $com.=qq|$n�F ���ڂ����� <span class="tmp">$n�͐g���ł߂��I</span>|;	}],
		[150,	100,	'��������',				sub{ my $n = '@�ײ�@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(39); return if !$n || $ms{$n}{hp} <= 0; for my $k (qw/hp mp at df ag/){ my $v=$ms{$m}{$k}; $ms{$m}{$k}+=$ms{$n}{$k}; $ms{$n}{$k}+=$v; $ms{$m}{$k}=999 if $ms{$m}{$k}>999; $ms{$n}{$k}=999 if $ms{$n}{$k}>999; }; $com.=qq|<span class="tmp">$m��$n�͍��̂����I</span>|; $ms{$m}{icon}="job/59_$m{sex}_mix.gif"; if ($n =~ /^@/) { $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; } else { $ms{$n}{icon}="job/0.gif"; } 	}],
	);
}

sub skill_60 { # ��׺��ײ�ް
	return (
		[10,	30,		'��т���',				sub{ my $n = '@��׺��@'; if (defined $ms{$n}{name}) { $com.="$n���Ăяo���̂Ɏ��s�����c"; return; }; $m{lv} < 40 ? &_add_party($n, 'mon/083.gif', 160, 70, 180, 100, 70) : $m{lv} < 70 ? &_add_party($n, 'mon/084.gif', 250, 50, 300, 200, 100) : &_add_party($n, 'mon/224.gif', 400, 30, 400, 300, 100); $com.="$n���퓬�ɎQ�������I"; 	}],
		[11,	0,		'�ɂ���',				sub{ my $n = '@��׺��@'; return if !defined($ms{$n}{name}) || $ms{$n}{hp} <= 0; $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; $com.="$n���퓬���瓦���o�����I"; 	}],
		[12,	0,		'���������߂��ꂢ',		sub{ my $n = '@��׺��@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(41); return if !$n || $ms{$n}{hp} <= 0; $com.="$n�F ���������� "; $buf_m = $m; $m = $n; &kougeki(shift); $m = $buf_m;	}],
		[30,	30,		'�Ђ����߂��ꂢ',		sub{ my $n = '@��׺��@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(41); return if !$n || $ms{$n}{hp} <= 0; $com.="$n�F "; if (rand(2)<1) { $com.='�����肳�� '; &_damage(shift, $ms{$n}{at} * 1.7, '�U'); }elsif(rand(2)<1){ $com.='���������Ԃ� '; &_damage(shift, $ms{$n}{at} * 1.5, '�U', 1); }else{ $com.='�������₭���� '; &_damages(230, '��', 1); }; 	}],
		[100,	10,		'�ڂ�����߂��ꂢ',		sub{ my $n = '@��׺��@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(41); return if !$n || $ms{$n}{hp} <= 0; $ms{$n}{tmp} = '�h��'; $com.=qq|$n�F ���ڂ����� <span class="tmp">$n�͐g���ł߂��I</span>|;	}],
		[150,	100,	'��������',				sub{ my $n = '@��׺��@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(41); return if !$n || $ms{$n}{hp} <= 0; for my $k (qw/hp mp at df ag/){ my $v=$ms{$m}{$k}; $ms{$m}{$k}+=$ms{$n}{$k}; $ms{$n}{$k}+=$v; $ms{$m}{$k}=999 if $ms{$m}{$k}>999; $ms{$n}{$k}=999 if $ms{$n}{$k}>999; }; $com.=qq|<span class="tmp">$m��$n�͍��̂����I</span>|; $ms{$m}{icon}="job/60_$m{sex}_mix.gif"; if ($n =~ /^@/) { $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; } else { $ms{$n}{icon}="job/0.gif"; } 	}],
	);
}
sub skill_61 { # ȸ��ݻ�
	return (
		[10,	30,		'��т���',				sub{ my $n = '@�����@'; if (defined $ms{$n}{name}) { $com.="$n���Ăяo���̂Ɏ��s�����c"; return; }; $m{lv} < 40 ? &_add_party($n, 'mon/040.gif', 120, 120, 120, 60, 120) : $m{lv} < 70 ? &_add_party($n, 'mon/041.gif', 300, 200, 280, 90, 240) : &_add_party($n, 'mon/064.gif', 444, 444, 666, 222, 444); $com.="$n���퓬�ɎQ�������I"; 	}],
		[11,	0,		'�ɂ���',				sub{ my $n = '@�����@'; return if !defined($ms{$n}{name}) || $ms{$n}{hp} <= 0; $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; $com.="$n���퓬���瓦���o�����I"; 	}],
		[12,	0,		'���������߂��ꂢ',		sub{ my $n = '@�����@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(61); return if !$n || $ms{$n}{hp} <= 0; $com.="$n�F ���������� "; $buf_m = $m; $m = $n; &kougeki(shift); $m = $buf_m;	}],
		[30,	30,		'�Ђ����߂��ꂢ',		sub{ my $n = '@�����@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(61); return if !$n || $ms{$n}{hp} <= 0; $com.="$n�F "; if (rand(2)<1) { $com.='���U���L '; &_deaths('����', '��', 22); }elsif(rand(2)<1){ $com.='���o�C�I�K '; $is_add_effect = 1; &_damages(120, '��', 1); &_st_ds('�ғ�', '��', 40); }else{ $com.='�������ǂ��̂��� '; &_st_ds('�ғ�', '��', 70); }; 	}],
		[100,	10,		'�ڂ�����߂��ꂢ',		sub{ my $n = '@�����@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(61); return if !$n || $ms{$n}{hp} <= 0; $ms{$n}{tmp} = '�h��'; $com.=qq|$n�F ���ڂ����� <span class="tmp">$n�͐g���ł߂��I</span>|;	}],
		[150,	42,		'���N�C�G��',			sub{ my $n = '@�����@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(61); return if !$n || $ms{$n}{hp} <= 0; for my $y (@partys) { next if $ms{$y}{hp} > 0; $ms{$y}{hp}=int($ms{$y}{mhp}*0.42); $ms{$y}{at}+=300;$ms{$y}{ag}+=300; $com.=qq|<span class="revive">$y�������Ԃ����I</span>|; $ms{$y}{icon}="mon/040.gif"; }; 	}],
	);
}
sub skill_62 { # �ޯ�Ͻ��
	return (
		[10,	30,		'��т���',				sub{ my $n = '@�ޯ�@'; if (defined $ms{$n}{name}) { $com.="$n���Ăяo���̂Ɏ��s�����c"; return; }; $m{lv} < 40 ? &_add_party($n, 'mon/025.gif', 90, 80, 120, 10, 180) : $m{lv} < 70 ? &_add_party($n, 'mon/026.gif', 210, 270, 170, 30, 400) : &_add_party($n, 'mon/027.gif', 410, 350, 400, 50, 600); $com.="$n���퓬�ɎQ�������I"; 	}],
		[11,	0,		'�ɂ���',				sub{ my $n = '@�ޯ�@'; return if !defined($ms{$n}{name}) || $ms{$n}{hp} <= 0; $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; $com.="$n���퓬���瓦���o�����I"; 	}],
		[12,	0,		'���������߂��ꂢ',		sub{ my $n = '@�ޯ�@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(56); return if !$n || $ms{$n}{hp} <= 0; $com.="$n�F ���������� "; $buf_m = $m; $m = $n; &kougeki(shift); $m = $buf_m;	}],
		[30,	30,		'�Ђ����߂��ꂢ',		sub{ my $n = '@�ޯ�@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(56); return if !$n || $ms{$n}{hp} <= 0; $com.="$n�F "; if (rand(2)<1) { $com.='�����イ���� '; my($y, $v)= &_damage(shift, 100, '��', 1); return if !$y; &_heal($n, $v, '��');}elsif(rand(2)<1){ $com.='���A�X�s�� '; my($y, $v) = &_st_down(shift, 0.3, '��', 'mp'); return if !$y; &_mp_h($m, $v, '��'); }else{ $com.='�����傤����� '; &_st_ds('����', '��', 70); }; 	}],
		[100,	10,		'�ڂ�����߂��ꂢ',		sub{ my $n = '@�ޯ�@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(56); return if !$n || $ms{$n}{hp} <= 0; $ms{$n}{tmp} = '�h��'; $com.=qq|$n�F ���ڂ����� <span class="tmp">$n�͐g���ł߂��I</span>|;	}],
		[150,	37,		'�u���b�h���C��',		sub{ my $n = '@�ޯ�@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(56); return if !$n || $ms{$n}{hp} <= 0; &_damages(170, '��', 1); &_heals(150, '��'); 	}],
	);
}
sub skill_63 { # �ɺϽ��
	return (
		[10,	30,		'��т���',				sub{ my $n = '@�ɺ@'; if (defined $ms{$n}{name}) { $com.="$n���Ăяo���̂Ɏ��s�����c"; return; }; $m{lv} < 40 ? &_add_party($n, 'mon/030.gif', 100, 100, 80, 50, 80) : $m{lv} < 70 ? &_add_party($n, 'mon/031.gif', 300, 80, 150, 100, 100) : &_add_party($n, 'mon/032.gif', 400, 60, 200, 100, 100); $com.="$n���퓬�ɎQ�������I"; 	}],
		[11,	0,		'�ɂ���',				sub{ my $n = '@�ɺ@'; return if !defined($ms{$n}{name}) || $ms{$n}{hp} <= 0; $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; $com.="$n���퓬���瓦���o�����I"; 	}],
		[12,	0,		'���������߂��ꂢ',		sub{ my $n = '@�ɺ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(63); return if !$n || $ms{$n}{hp} <= 0; $com.="$n�F ���������� "; $buf_m = $m; $m = $n; &kougeki(shift); $m = $buf_m;	}],
		[30,	30,		'�Ђ����߂��ꂢ',		sub{ my $n = '@�ɺ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(63); return if !$n || $ms{$n}{hp} <= 0; $com.="$n�F "; if (rand(2)<1) { $com.='���ǂ��̂��� '; &_st_ds('�ғ�', '��', 90);}elsif(rand(2)<1){ $com.='�����тꂲ�� '; &_st_ds('���', '��', 50);}else{ $com.='���˂ނ育�� '; &_st_ds('����', '��', 50); }; 	}],
		[100,	10,		'�ڂ�����߂��ꂢ',		sub{ my $n = '@�ɺ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(63); return if !$n || $ms{$n}{hp} <= 0; $ms{$n}{tmp} = '�h��'; $com.=qq|$n�F ���ڂ����� <span class="tmp">$n�͐g���ł߂��I</span>|;	}],
		[150,	100,	'��������',				sub{ my $n = '@�ɺ@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(63); return if !$n || $ms{$n}{hp} <= 0; for my $k (qw/hp mp at df ag/){ my $v=$ms{$m}{$k}; $ms{$m}{$k}+=$ms{$n}{$k}; $ms{$n}{$k}+=$v; $ms{$m}{$k}=999 if $ms{$m}{$k}>999; $ms{$n}{$k}=999 if $ms{$n}{$k}>999; }; $com.=qq|<span class="tmp">$m��$n�͍��̂����I</span>|; $ms{$m}{icon}="job/63_$m{sex}_mix.gif"; if ($n =~ /^@/) { $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; } else { $ms{$n}{icon}="job/0.gif"; } 	}],
	);
}
sub skill_64 { # ��޹Ͻ��
	return (
		[10,	30,		'��т���',				sub{ my $n = '@�ް��@'; if (defined $ms{$n}{name}) { $com.="$n���Ăяo���̂Ɏ��s�����c"; return; }; $m{lv} < 40 ? &_add_party($n, 'mon/035.gif', 100, 100, 50, 100, 100) : $m{lv} < 70 ? &_add_party($n, 'mon/036.gif', 200, 80, 100, 150, 150) : &_add_party($n, 'mon/070.gif', 300, 60, 150, 200, 200); $com.="$n���퓬�ɎQ�������I"; 	}],
		[11,	0,		'�ɂ���',				sub{ my $n = '@�ް��@'; return if !defined($ms{$n}{name}) || $ms{$n}{hp} <= 0; $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; $com.="$n���퓬���瓦���o�����I"; 	}],
		[12,	0,		'���������߂��ꂢ',		sub{ my $n = '@�ް��@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(64); return if !$n || $ms{$n}{hp} <= 0; $com.="$n�F ���������� "; $buf_m = $m; $m = $n; &kougeki(shift); $m = $buf_m;	}],
		[30,	30,		'�Ђ����߂��ꂢ',		sub{ my $n = '@�ް��@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(64); return if !$n || $ms{$n}{hp} <= 0; $com.="$n�F "; if (rand(2)<1) { $com.='���Ђ傤�� '; my($y) = &_check_enemy(shift, '����', '��'); return if !$y; $com.="$n�F ���������� "; $buf_m = $m; $m = $y; &kougeki(); $m = $buf_m; }elsif(rand(2)<1){ $com.='������΂� '; &_st_d(shift, '�U��', '��', 80); }else{ $com.='�����ǂ납��'; &_st_ds('����', '�U', 60); }; 	}],
		[100,	10,		'�ڂ�����߂��ꂢ',		sub{ my $n = '@�ް��@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(64); return if !$n || $ms{$n}{hp} <= 0; $ms{$n}{tmp} = '�h��'; $com.=qq|$n�F ���ڂ����� <span class="tmp">$n�͐g���ł߂��I</span>|;	}],
		[150,	100,	'��������',				sub{ my $n = '@�ް��@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(64); return if !$n || $ms{$n}{hp} <= 0; for my $k (qw/hp mp at df ag/){ my $v=$ms{$m}{$k}; $ms{$m}{$k}+=$ms{$n}{$k}; $ms{$n}{$k}+=$v; $ms{$m}{$k}=999 if $ms{$m}{$k}>999; $ms{$n}{$k}=999 if $ms{$n}{$k}>999; }; $com.=qq|<span class="tmp">$m��$n�͍��̂����I</span>|; $ms{$m}{icon}="job/64_$m{sex}_mix.gif"; if ($n =~ /^@/) { $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; } else { $ms{$n}{icon}="job/0.gif"; } 	}],
	);
}
sub skill_65 { # ���Ͻ��
	return (
		[10,	30,		'��т���',				sub{ my $n = '@���@'; if (defined $ms{$n}{name}) { $com.="$n���Ăяo���̂Ɏ��s�����c"; return; }; $m{lv} < 40 ? &_add_party($n, 'mon/200.gif', 100, 60, 100, 60, 180) : $m{lv} < 70 ? &_add_party($n, 'mon/206.gif', 210, 90, 300, 80, 280) : &_add_party($n, 'mon/203.gif', 400, 230, 500, 160, 400); $com.="$n���퓬�ɎQ�������I"; 	}],
		[11,	0,		'�ɂ���',				sub{ my $n = '@���@'; return if !defined($ms{$n}{name}) || $ms{$n}{hp} <= 0; $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; $com.="$n���퓬���瓦���o�����I"; 	}],
		[12,	0,		'���������߂��ꂢ',		sub{ my $n = '@���@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(44); return if !$n || $ms{$n}{hp} <= 0; $com.="$n�F ���������� "; $buf_m = $m; $m = $n; &kougeki(shift); $m = $buf_m;	}],
		[30,	30,		'�Ђ����߂��ꂢ',		sub{ my $n = '@���@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(44); return if !$n || $ms{$n}{hp} <= 0; $com.="$n�F "; if (rand(2)<1) { $com.='���Ђ����� '; &_damage(shift, $ms{$n}{at} * 1.5, '�U'); }elsif(rand(2)<1){ $com.='�����݂� '; &_damage(shift, $ms{$n}{at} * 1.2, '�U', 1); }else{ $com.='���Ƃ��� '; &_damage(shift, $ms{$n}{at} * 2.0, '�U'); }; 	}],
		[100,	10,		'�ڂ�����߂��ꂢ',		sub{ my $n = '@���@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(44); return if !$n || $ms{$n}{hp} <= 0; $ms{$n}{tmp} = '�h��'; $com.=qq|$n�F ���ڂ����� <span class="tmp">$n�͐g���ł߂��I</span>|;	}],
		[150,	40,		'�ǂƂ��̂�����',		sub{ my $n = '@���@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(44); return if !$n || $ms{$n}{hp} <= 0; my $v = int(rand(2)+3); for my $i (1..$v) { last if $ms{$m}{hp} <= 0; &_damage(undef, $ms{$n}{ag} * 2.0, '�U'); };	}],
	);
}
sub skill_66 { # �޸�Ͻ��
	return (
		[10,	30,		'��т���',				sub{ my $n = '@�޲��@'; if (defined $ms{$n}{name}) { $com.="$n���Ăяo���̂Ɏ��s�����c"; return; }; $m{lv} < 40 ? &_add_party($n, 'mon/043.gif', 120, 110, 160, 90, 150) : $m{lv} < 70 ? &_add_party($n, 'mon/044.gif', 240, 210, 240, 120, 180) : &_add_party($n, 'mon/056.gif', 450, 280, 400, 240, 300); $com.="$n���퓬�ɎQ�������I"; 	}],
		[11,	0,		'�ɂ���',				sub{ my $n = '@�޲��@'; return if !defined($ms{$n}{name}) || $ms{$n}{hp} <= 0; $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; $com.="$n���퓬���瓦���o�����I"; 	}],
		[12,	0,		'���������߂��ꂢ',		sub{ my $n = '@�޲��@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(66); return if !$n || $ms{$n}{hp} <= 0; $com.="$n�F ���������� "; $buf_m = $m; $m = $n; &kougeki(shift); $m = $buf_m;	}],
		[30,	30,		'�Ђ����߂��ꂢ',		sub{ my $n = '@�޲��@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(66); return if !$n || $ms{$n}{hp} <= 0; $com.="$n�F "; if (rand(2)<1) { $com.='�����̂��ǂ� '; &_deaths('����', '�x', 20); }elsif(rand(2)<1){ $com.='���f�X '; &_death(shift, '����', '�U', 40);}else{ $com.='���̂낢 '; my @randoms = ('�U��', '����'); for my $name (@enemys) { &_st_d($name, $randoms[int(rand(@randoms))], '��', 75); }; }; 	 	}],
		[100,	10,		'�ڂ�����߂��ꂢ',		sub{ my $n = '@�޲��@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(66); return if !$n || $ms{$n}{hp} <= 0; $ms{$n}{tmp} = '�h��'; $com.=qq|$n�F ���ڂ����� <span class="tmp">$n�͐g���ł߂��I</span>|;	}],
		[150,	50,		'�݂�Ȃ̂����',		sub{ my $n = '@�޲��@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(66); return if !$n || $ms{$n}{hp} <= 0; my $d = 100; for my $y (@partys) { $d += 420 if $ms{$y}{hp} <= 0; } &_damages($d, '��', 1); 	}],
	);
}
sub skill_67 { # �����Ͻ��
	return (
		[10,	30,		'��т���',				sub{ my $n = '@�����@'; if (defined $ms{$n}{name}) { $com.="$n���Ăяo���̂Ɏ��s�����c"; return; }; $m{lv} < 40 ? &_add_party($n, 'mon/020.gif', 90, 120, 90, 50, 90) : $m{lv} < 70 ? &_add_party($n, 'mon/021.gif', 180, 280, 160, 120, 180) : &_add_party($n, 'mon/022.gif', 8, 500, 80, 950, 950); $com.="$n���퓬�ɎQ�������I"; 	}],
		[11,	0,		'�ɂ���',				sub{ my $n = '@�����@'; return if !defined($ms{$n}{name}) || $ms{$n}{hp} <= 0; $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; $com.="$n���퓬���瓦���o�����I"; 	}],
		[12,	0,		'���������߂��ꂢ',		sub{ my $n = '@�����@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(40); return if !$n || $ms{$n}{hp} <= 0; $com.="$n�F ���������� "; $buf_m = $m; $m = $n; &kougeki(shift); $m = $buf_m;	}],
		[30,	30,		'�Ђ����߂��ꂢ',		sub{ my $n = '@�����@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(40); return if !$n || $ms{$n}{hp} <= 0; $com.="$n�F "; if ($ms{$n}{icon} =~ /020/) { $com.='���h�N�h�N '; &_st_ds('�ғ�', '��', 80); }elsif($ms{$n}{icon} =~ /021/){ $com.='���}�O�} '; &_damages(220, '��', 1); }else{ $com.='���W�S�X�p�[�N '; $is_add_effect = 1; &_damages(150, '��', 1); &_st_ds('���', '��', 20);}	}],
		[100,	10,		'�ڂ�����߂��ꂢ',		sub{ my $n = '@�����@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(40); return if !$n || $ms{$n}{hp} <= 0; $ms{$n}{tmp} = '�h��'; $com.=qq|$n�F ���ڂ����� <span class="tmp">$n�͐g���ł߂��I</span>|;	}],
		[150,	40,		'�o�u���{��',			sub{ my $n = '@�����@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(40); return if !$n || $ms{$n}{hp} <= 0; $is_add_effect = 1; for my $y (@enemys) { my($_y) = &_damage($y, 150, '��', 1); next if rand(2)<1; $com.="$_y�͂��₵���t�̂����������I"; $ms{$_y}{tmp} = '�Q�{'; }; 	}],
	);
}
sub skill_68 { # ��˰۰
	return (
		[10,	30,		'��т���',				sub{ my $n = '@��@'; if (defined $ms{$n}{name}) { $com.="$n���Ăяo���̂Ɏ��s�����c"; return; }; rand(3) < 1 ? &_add_party($n, 'mon/101.gif', $ms{$m}{mhp}*0.8, $ms{$m}{mmp}*0.2, $ms{$m}{mat}*3.0, $ms{$m}{mdf}*2.0, $ms{$m}{mag}) : rand(3) < 1 ? &_add_party($n, 'mon/102.gif', $ms{$m}{mhp}*0.6, $ms{$m}{mmp}, $ms{$m}{mat}, $ms{$m}{mdf}, $ms{$m}{mag}*2.0) : &_add_party($n, 'mon/103.gif',  $ms{$m}{mhp}*0.7, $ms{$m}{mmp}, $ms{$m}{mat}*1.5, $ms{$m}{mdf}*1.5, $ms{$m}{mag}*1.5); $com.="$n���퓬�ɎQ�������I"; 	}],
		[11,	0,		'�ɂ���',				sub{ my $n = '@��@'; return if !defined($ms{$n}{name}) || $ms{$n}{hp} <= 0; $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; $com.="$n���퓬���瓦���o�����I"; 	}],
		[12,	0,		'���������߂��ꂢ',		sub{ my $n = '@��@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(68); return if !$n || $ms{$n}{hp} <= 0; $com.="$n�F ���������� "; $buf_m = $m; $m = $n; &kougeki(shift); $m = $buf_m;	}],
		[30,	30,		'�Ђ����߂��ꂢ',		sub{ my $n = '@��@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(68); return if !$n || $ms{$n}{hp} <= 0; $com.="$n�F "; if ($ms{$n}{icon} =~ /101/) { $com.='���܂��񂬂� '; rand(2) < 1 ? &_damage(shift, $ms{$m}{at} * 3, '�U') : &_damage(shift, 20, '�U'); }elsif($ms{$n}{icon} =~ /102/){ $com.='�������]�[�} '; &_damage(shift, 220, '��', 1); }else{ $com.='���x�z�} '; &_heal(shift, 999, '��'); }; 	}],
		[100,	10,		'�ڂ�����߂��ꂢ',		sub{ my $n = '@��@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(68); return if !$n || $ms{$n}{hp} <= 0; $ms{$n}{tmp} = '�h��'; $com.=qq|$n�F ���ڂ����� <span class="tmp">$n�͐g���ł߂��I</span>|;	}],
		[150,	50,		'�x�z�}�Y��',			sub{ my $n = '@��@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(68); return if !$n || $ms{$n}{hp} <= 0; &_heals(999, '��');	}],
	);
}
sub skill_69 { # ���˰۰
	return (
		[10,	30,		'��т���',				sub{ my $n = '@���@'; if (defined $ms{$n}{name}) { $com.="$n���Ăяo���̂Ɏ��s�����c"; return; }; rand(3) < 1 ? &_add_party($n, 'mon/106.gif', $ms{$m}{mhp}*0.8, $ms{$m}{mmp}*0.2, $ms{$m}{mat}*3.0, $ms{$m}{mdf}*2.0, $ms{$m}{mag}) : rand(3) < 1 ? &_add_party($n, 'mon/107.gif', $ms{$m}{mhp}*0.6, $ms{$m}{mmp}, $ms{$m}{mat}, $ms{$m}{mdf}, $ms{$m}{mag}*2.0) : &_add_party($n, 'mon/108.gif',  $ms{$m}{mhp}*0.7, $ms{$m}{mmp}, $ms{$m}{mat}*1.5, $ms{$m}{mdf}*1.5, $ms{$m}{mag}*1.5); $com.="$n���퓬�ɎQ�������I"; 	}],
		[11,	0,		'�ɂ���',				sub{ my $n = '@���@'; return if !defined($ms{$n}{name}) || $ms{$n}{hp} <= 0; $ms{$n}{color}=$npc_color; $ms{$n}{hp}=0; $com.="$n���퓬���瓦���o�����I"; 	}],
		[12,	0,		'���������߂��ꂢ',		sub{ my $n = '@���@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(69); return if !$n || $ms{$n}{hp} <= 0; $com.="$n�F ���������� "; $buf_m = $m; $m = $n; &kougeki(shift); $m = $buf_m;	}],
		[30,	30,		'�Ђ����߂��ꂢ',		sub{ my $n = '@���@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(69); return if !$n || $ms{$n}{hp} <= 0; $com.="$n�F "; if ($ms{$n}{icon} =~ /106/) { $com.='���܂��񂬂� '; rand(2) < 1 ? &_damage(shift, $ms{$m}{at} * 3, '�U') : &_damage(shift, 20, '�U'); }elsif($ms{$n}{icon} =~ /107/){ $com.='�������]�[�} '; &_damage(shift, 220, '��', 1); }else{ $com.='���x�z�} '; &_heal(shift, 999, '��'); }; 	}],
		[100,	10,		'�ڂ�����߂��ꂢ',		sub{ my $n = '@���@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(69); return if !$n || $ms{$n}{hp} <= 0; $ms{$n}{tmp} = '�h��'; $com.=qq|$n�F ���ڂ����� <span class="tmp">$n�͐g���ł߂��I</span>|;	}],
		[150,	20,		'�~�i�f�C��',			sub{ my $n = '@���@'; $n = defined($ms{$n}{name}) ? $n : &_search_job(69); return if !$n || $ms{$n}{hp} <= 0; my($y) = &_check_enemy(shift, '�F', '��'); return if !$y; my $d = 100; for my $name (@partys) { next if $m eq $name || $ms{$name}{mp} < 5; $ms{$name}{mp}-=5; $d += 85; }; $com.=qq|$m�͒��Ԃ݂̂�Ȃ���͂��󂯂Ƃ����I| if $d > 100; &_damage($y, $d, '��', 1);	}],
	);
}
sub skill_70 { # �V���l
	return (
		[50,	25,		'�߂�����',			sub{ &_heal($m, 300, '��');		}],
		[100,	25,		'�h���S���p���[',	sub{ &_st_up($m, 0.4, '�U', 'at'); &_st_up($m, 0.4, '�U', 'df');	}],
		[150,	40,		'�M�K�f�C��',		sub{ &_damages(180, '��', 1);			}],
		[200,	27,		'�Ă񂵂̂�������',	sub{ for my $y (@partys) { next if $ms{$y}{hp} > 0; if (rand(2) < 1) { $com.=qq|�Ȃ�ƁA<b>$y</b>�� <span class="heal">�����Ԃ�</span> �܂����I|; $ms{$y}{hp}=int($ms{$y}{mhp} * 0.5); } else { $com.=qq|�������A<b>$y</b>�͐����Ԃ�Ȃ������c|; }; }; 	}],
	);
}

# �G�p
sub skill_90 { # �ғŌn
	return (
		[10,	4,		'�ǂ���������',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at} * 1.1, '�U'); return if !$y || $ms{$y}{hp} <= 0; &_st_d($y, '�ғ�', '�U', 70);	}],
		[20,	6,		'�|�C�Y��',			sub{ $is_add_effect = 1; my($y) = &_damage(shift, 25, '��', 1); return if !$y || $ms{$y}{hp} <= 0; &_st_d($y, '�ғ�', '��', 80);	}],
		[30,	8,		'�����ǂ��̂���',	sub{ &_st_ds('�ғ�', '��', 60);		}],
	);
}
sub skill_91 { # ��჌n
	return (
		[10,	8,		'�܂Ђ�������',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at} * 1.2, '�U'); return if !$y || $ms{$y}{hp} <= 0; &_st_d($y, '���', '�U', 30);	}],
		[20,	11,		'���тꂤ��',		sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at} * 0.8, '�U'); return if !$y || $ms{$y}{hp} <= 0; &_st_d($y, '���', '�U', 40);	}],
		[30,	9,		'�₯������',		sub{ &_st_ds('���', '��', 35);		}],
	);
}
sub skill_92 { # ����n
	return (
		[10,	8,		'�����z�[',			sub{ &_st_d(shift, '����', '��', 65);		}],
		[20,	15,		'�˂ނ肱������',	sub{ $is_add_effect = 1; my($y) = &_damage(shift, $ms{$m}{at} * 0.8, '�U'); return if !$y || $ms{$y}{hp} <= 0; &_st_d($y, '����', '�U', 55);	}],
		[30,	9,		'���܂�����',		sub{ &_st_ds('����', '��', 35);	}],
	);
}
sub skill_93 { # ����
	return (
		[10,	14,		'�U�L',			sub{ &_death(shift, '����', '��', 20);	}],
		[20,	32,		'�U���L',		sub{ &_deaths('����', '��', 20);	}],
		[30,	24,		'���̂��ǂ�',	sub{ &_deaths('����', '�x', 17);	}],
		[40,	42,		'���̂��񂱂�',	sub{ my($y) = &_check_enemy(shift, '�m��', '��'); return if !$y; if ($ms{$y}{mhp}>999 || $ms{$y}{mdf}>999) { $com.="$y�ɂ͂����Ȃ������I"; } elsif (rand(2)<1) { &_st_down($y, 0.75, '��', 'hp'); $ms{$y}{state}='�ғ�'; } else { $com.="$y�͂��킵���I"; };	}],
	);
}
sub skill_94 { # ����
	return (
		[10,	1,		'���K���e',		sub{ $com.=qq|<span class="die">$m�͎��������I</span>|; &_deaths('����', '��', 60); &defeat($m); $ms{$m}{mp} = 1;	}],
		[20,	0,		'�˂�',			sub{ $ms{$m}{state}='����'; $com.=qq|<span class="state">$m�͖��肾����</span>|; &_heal($m, $ms{$m}{mhp}*0.5);	}],
	);
}
sub skill_95 { # ����
	return (
		[0,		50,		'���傤����',	sub{ &_add_enemy	}],
		[0,		50,		'���傤����',	sub{ &_add_enemy	}],
	);
}
sub skill_96 { # �ް�Ͻ��
	return (
		[0,	0,		'�����',			sub{ my($y) = &_check_enemy(shift, '����', '��'); my @alfas = ('A'..'Z'); $ms{$y}{name} = '@�l�`'.$alfas[int(rand(@alfas))]; $ms{$y}{color}=$ms{$m}{color}; $ms{$y}{addr} = 0; $com.=qq|<span class="die">$y��$m�̂����l�`�ƂȂ����I</span>|;	}],
		[0,	0,		'�N�[���W���[�N',	sub{ for my $y (@enemys) { $ms{$y}{ten} = 1; }; $com.="�S���̃e���V���������������c";	}],
	);
}
sub skill_97 { # ���U���^(�j��_[king1]�A�����̨�[21]�Aټ̧�[20])
	return (
		[0,		24,		'�݂��ꂤ��',		sub{ my $v = int(rand(2)+3); for my $i (1..$v) { last if $ms{$m}{hp} <= 0; &_damage(undef, $ms{$m}{at}*0.85, '�U'); };		}],
		[0,		20,		'�΂������',		sub{ my $v = int(rand(3)+3); for my $i (1..$v) { last if $ms{$m}{hp} <= 0; &_damage(undef, $ms{$m}{at}*0.9, '�U'); };	}],
		[0,		30,		'���Ă��͂ǂ�',	sub{ for my $y (@members) { my $tten=$ms{$y}{ten}; &reset_status($y); $ms{$y}{ten}=$tten; }; $com.=qq|<span class="st_down">�S�Ă̌��ʂ����������ꂽ�I</span>|;	}],
		[0,		9,		'�߂��₭',			sub{ my $v = int($ms{$m}{df} * 0.5); $ms{$m}{df} -= $v; $com.=qq|$m��<span class="st_down">$e2j{df}�� $v ������܂����I</span>|; &_st_up($m, 1.0, '��', 'at');	}],
		[0,		30,		'�����ڂ�����',		sub{ &_damages(300, '�U', 1); $ms{$m}{tmp}='�Q�{';	}],
		[0,		40,		'���񂱂�����',		sub{ my($y, $v) = &_damage(shift, $ms{$m}{at}*2.5, '�U'); return if $v <= 0; &_risk($v * 0.2);		}],
		[0,		33,		'����������',		sub{ $ms{$m}{tmp}='�Q�{'; &tenshon($m); &tenshon($m);	}],
		[0,		80,		'���������̂ق̂�',	sub{ &_damages(400, '��', 1);	}],
		[0,		70,		'�W�S�X�p�[�N',		sub{ $is_add_effect = 1; &_damages(250, '��', 1); &_st_ds('���', '��', 20);	}],
		[0,		42,		'���̂��񂱂�',		sub{ my($y) = &_check_enemy(shift, '�m��', '��'); return if !$y; if ($ms{$y}{mhp}>999 || $ms{$y}{mdf}>999) { $com.="$y�ɂ͂����Ȃ������I"; } else { &_st_down($y, 0.75, '��', 'hp'); $ms{$y}{state}='�ғ�'; };	}],
		[0,		66,		'��݂̂Ă�',		sub{ $is_add_effect = 1; &_damages(260, '��', 1); &_st_ds('����', '��', 30);		}],
	);
}
sub skill_98 { # �����@�^(����[map/10])
	return (
		[0,		44,		'������Ȃ��Ă�',	sub{ my($y) = &_check_enemy(shift, '�m��', '��'); return if !$y; if ($ms{$y}{mhp}>999 || $ms{$y}{mdf}>999) { $com.="$y�ɂ͂����Ȃ������I"; } else { $ms{$y}{hp}=1; $com.=qq|$y��<span class="st_down">�����͂�������</span>�I|;; };	}],
		[0,		30,		'���Ă��͂ǂ�',	sub{ for my $y (@members) { my $tten=$ms{$y}{ten}; &reset_status($y); $ms{$y}{ten}=$tten; }; $com.=qq|<span class="st_down">�S�Ă̌��ʂ����������ꂽ�I</span>|;	}],
		[0,		30,		'�J�[�o���N��',		sub{ return if &is_bad_state('��'); $com.="�����r�[�̌���"; for my $y (@partys) { next if $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '������'; $com.=qq|<span class="tmp">$y�͖��@�̕ǂɎ��ꂽ�I</span>|;};	}],
		[0,		23,		'�}�C�e�B�K�[�h',	sub{ &_st_ups(0.5, '��', 'df'); for my $y (@partys) { next if $ms{$y}{hp} <= 0; $ms{$y}{tmp} = '���y��'; $com.=qq|<span class="tmp">$y�͖��@�̌��Ŏ��ꂽ�I</span>|;};	}],
		[0,		44,		'��������',			sub{ $ms{$m}{tmp}='�Q�{'; &tenshon($m); &tenshon($m); 		}],
		[0,		44,		'������Ȃ��Ă�',	sub{ my($y) = &_check_enemy(shift, '�m��', '��'); return if !$y; if ($ms{$y}{mhp}>999 || $ms{$y}{mdf}>999) { $com.="$y�ɂ͂����Ȃ������I"; } else { $ms{$y}{hp}=1; $com.=qq|$y��<span class="st_down">�����͂�������</span>�I|;; };	}],
		[0,		40,		'�u���b�h���C��',	sub{ &_damages(200, '��', 1); &_heals(200, '��'); 	}],
		[0,		40,		'�o�u���{��',		sub{ for my $y (@enemys) { &_damage($y, 100, '��', 1); $com.="$y�͂��₵���t�̂����������I"; $ms{$y}{tmp}='�Q�{'; }; 	}],
		[0,		80,		'���������̂ق̂�',	sub{ &_damages(350, '��', 1);	}],
		[0,		99,		'�_�[�N���e�I',		sub{ my $v = int(rand(3)+4); for my $i (1..$v) { last if $ms{$m}{hp} <= 0; &_damage(undef, 250, '��', 1); };	}],
		[0,		99,		'�A���e�}',			sub{ &_damages(400, '��', 1);	}],
	);
}
sub skill_99 { # �ɂ�����
	return (
		[0,		0,	'�ɂ�����',		sub{ $com.="$m�͓����o�����I"; $ms{$m}{hp} = 0;	}],
	);
}
sub skill_100 { # �����
	return (
		[0,		99,		'�݂�Ȃ̂����',	sub{ &_damage(shift, $m{kill_m}*0.1, '�U', 1);	}],
		[0,		99,		'�ق����傤',		sub{ &_damage(shift, 666, '�U', 1);	}],
	);
}
sub skill_101 { # �Í���(�Ϻ�)
	return (
		[0,		50,		'���傤����',	sub{ if ($ms{$m}{icon} =~ /710/ && $ms{$m}{hp} < $ms{$m}{mhp} * 0.2) { $com.="�Ȃ�ƁA�^�}�S�Ƀq�r���c�I$m�̕��󂪊��S�ɉ����Ă��܂����I"; $ms{$m}{icon}='mon/712.gif'; $ms{$m}{job}=97; $ms{$m}{hp}=$ms{$m}{mhp}; $ms{$m}{mp}=int($ms{$m}{mmp}*0.1); for my $k (qw/at df ag/){ $ms{$m}{$k} = $ms{$m}{'m'.$k} = 600; }; } else { &_add_enemy }; 	}],
		[0,		50,		'���傤����',	sub{ if ($ms{$m}{icon} =~ /710/ && $ms{$m}{hp} < $ms{$m}{mhp} * 0.1) { $com.="�Ȃ�ƁA�^�}�S�Ƀq�r���c�I$m�̕��󂪊��S�ɉ����Ă��܂����I"; $ms{$m}{icon}='mon/712.gif'; $ms{$m}{job}=97; $ms{$m}{hp}=$ms{$m}{mhp}; $ms{$m}{mp}=int($ms{$m}{mmp}*0.1); for my $k (qw/at df ag/){ $ms{$m}{$k} = $ms{$m}{'m'.$k} = 600; }; } else { &_add_enemy }; 	}],
	);
}

#������������������������������������������������������������
# �����܂ŁB�ȉ��T�u���[�`��
#������������������������������������������������������������

#=================================================
# �_���[�W(to �G)
#=================================================
sub _damages { # �G�S��
	my($v, $z, $is_direct) = @_;
	return if &is_bad_state($z);
	
	if (@enemys < 1) { # �G�S��
		$mes = '�키���肪������܂���';
		return;
	}
	for my $y (@enemys) {
		last if $ms{$m}{hp} <= 0;
		&_damage($y, $v, $z, $is_direct);
		$v *= 0.85; # ���я��Ń_���[�W��
	}
}
sub _damage { # �G�P��
	my($y, $v, $z, $is_direct) = &_check_enemy(@_);
	return if $mes;
	return unless $v;

	if ($ms{$y}{hp} <= 0) {
		$y = $m;
		$com .= "$m�͂킯���킩�炸�������U�������I";
	}
	
	if ($z eq '�U' && ( $ms{$m}{hit} < rand(100) || &_is_exceed_ag($y, $m) ) ) {
		$com .= "�~�X�I$y�͂��킵���I";
		$y = '';

		$ms{$m}{ten} = 1;
		return $y, 0;
	}
	else {
		my $y_df = $ms{$y}{df};
		$v *= $ms{$m}{ten};
		$v  = $v * 0.5 - ($ms{$y}{df} + $arms[$ms{$y}{arm}][3]) * 0.3 if !$is_direct || $ms{$y}{mdf} > 999;
		$v  = int($v * (rand(0.3)+0.9) );
		$v  = int(rand(2)+1) if $v < 1;

		$ms{$y}{hp} -= $v;
		$com .= qq|<b>$y</b>�� <span class="damage">$v</span> �̃_���[�W�I|;
		$ms{$m}{ten} = 1;

		if ($ms{$y}{hp} <= 0) {
			$ms{$y}{hp} = 0;
			$com .= qq|<span class="die">$y�����������I</span>|;
			&defeat($y); # �|�����Ƃ��̏���
		}
	
		return $y, $v;
	}
}
sub _risk { # �����_���[�W
	my $v = shift;
	
	return if $ms{$m}{hp} <= 0;

	$v = int($v + 1);
	$ms{$m}{hp} -= $v;
	$ms{$m}{hp}  = 1 if $ms{$m}{hp} <= 0;
	$com.=qq|$m�͔����� <span class="damage">$v</span> �̃_���[�W���������I|;
}

#=================================================
# ��(to ����)
#=================================================
sub _heals { # �����S��
	my($v, $z) = @_;
	return if &is_bad_state($z);
	for my $y (@partys) {
		&_heal($y, $v, $z);
	}
}
sub _heal { # �����P��
	my($y, $v) = &_check_party(@_);
	return if $ms{$y}{hp} <= 0;
	return unless $v;

	$v = int($v * (rand(0.3)+0.9) * $ms{$m}{ten});
	$ms{$m}{ten} = 1;
	$ms{$y}{hp} += $v;
	$ms{$y}{hp}  = $ms{$y}{mhp} if $ms{$y}{hp} > $ms{$y}{mhp};
	$com .= qq|<b>$y</b>��$e2j{mhp}�� <span class="heal">$v</span> �񕜂����I|;
	return 1;
}

#=================================================
# ���͉�(to ����)
#=================================================
sub _mp_hs { # �����S��
	my($v, $z) = @_;
	return if &is_bad_state($z);
	for my $y (@partys) {
		&_mp_h($y, $v, $z);
	}
}
sub _mp_h { # �����P��
	my($y, $v) = &_check_party(@_);
	return if $ms{$y}{hp} <= 0;
	return unless $v;

	$v = int($v * (rand(0.3)+0.9) * $ms{$m}{ten}) + 1;
	$ms{$m}{ten} = 1;
	$ms{$y}{mp} += $v;
	$ms{$y}{mp}  = $ms{$y}{mmp} if $ms{$y}{mp} > $ms{$y}{mmp};
	$com .= qq|<b>$y</b>��$e2j{mmp}�� <span class="heal">$v</span> �񕜂����I|;
	return 1;
}

#=================================================
# ����(to �G)
#=================================================
sub _deaths { # �G�S��
	my($v, $z, $par) = @_;
	return if &is_bad_state($z);
	if (@enemys < 1) { # �G�S��
		$mes = '�키���肪������܂���';
		return;
	}
	for my $y (@enemys) {
		&_death($y, $v, $z, $par);
	}
}
sub _death { # �G�P��
	my($y, $v, $z, $par) = &_check_enemy(@_);
	return if $ms{$y}{hp} <= 0;
	return if $mes;
	return unless $v;
	
	if ($ms{$y}{hp} > 999 || $ms{$y}{mdf} > 999) {
		return if $is_add_effect; # �ǉ����ʂ̏ꍇ�͔�\��
		$com .= "$y�ɂ͂����Ȃ������c";
	}
	elsif ($par >= rand(100)) {
		$com .= qq|<span class="die">$y�͎���ł��܂����I</span>|;
		&defeat($y); # �|�����Ƃ��̏���
	}
	else {
		return if $is_add_effect; # �ǉ����ʂ̏ꍇ�͔�\��
		$com .= "$y�͂��킵���I";
	}
}

#=================================================
# �X�e�[�^�X�_�E��(to �G)
#=================================================
sub _st_downs { # �G�S��
	my($v, $z, $k) = @_;
	return if &is_bad_state($z);
	if (@enemys < 1) { # �G�S��
		$mes = '�키���肪������܂���';
		return;
	}
	for my $y (@enemys) {
		&_st_down($y, $v, $z, $k);
	}
}
sub _st_down { # �G�P��
	my($y, $v, $z, $k) = &_check_enemy(@_);
	return if $ms{$y}{hp} <= 0;
	return if $mes;
	return unless $v;

	if ($ms{$y}{mdf} > 999 || ( ($k eq 'hp' || $k eq 'at') && $ms{$y}{hp} > 999) ) {
		return if $is_add_effect; # �ǉ����ʂ̏ꍇ�͔�\��
		$com .= "$y�ɂ͂����Ȃ������c";
		return;
	}
	elsif ($ms{$y}{$k} <= $ms{$y}{'m'.$k} * 0.2 || ($k eq 'hit' && $ms{$y}{$k} <= 50) ) {
		return if $is_add_effect; # �ǉ����ʂ̏ꍇ�͔�\��
		$com .= "$y�ɂ͂���ȏ���ʂ��Ȃ��悤���c";
		return;
	}
	
	$v = int($ms{$y}{$k} * $v * $ms{$m}{ten});
	$v = int(rand(50) + 100 * $ms{$m}{ten}) if $k eq 'mp' && $v > 150 * $ms{$m}{ten};
	$ms{$m}{ten} = 1;
	$ms{$y}{$k} -= $v;
	$ms{$y}{$k} = int($ms{$y}{'m'.$k} * 0.2) if $ms{$y}{$k} < $ms{$y}{'m'.$k} * 0.2;
	$ms{$y}{$k} = 50 if $k eq 'hit' && $ms{$y}{$k} < 50;
	$com .= qq|$y��<span class="st_down">$e2j{$k}�� $v ���������I</span>|;
	return $y, $v;
}

#=================================================
# �X�e�[�^�X�A�b�v(to ����)
#=================================================
sub _st_ups { # �����S��
	my($v, $z, $k) = @_;
	return if &is_bad_state($z);
	for my $y (@partys) {
		&_st_up($y, $v, $z, $k);
	}
}
sub _st_up { # �����P��
	my($y, $v, $z, $k) = &_check_party(@_);
	return if $ms{$y}{hp} <= 0;
	return if $v <= 0;
	return unless $v;

	if ($ms{$y}{$k} >= $ms{$y}{'m'.$k} * 2.5) {
		return if $is_add_effect; # �ǉ����ʂ̏ꍇ�͔�\��
		$com .= "$y�ɂ͂���ȏ���ʂ͂Ȃ��悤���c";
		return $y, $v;
	}
	
	$v = int($ms{$y}{'m'.$k} * $v * $ms{$m}{ten});
	$ms{$m}{ten} = 1;
	$ms{$y}{$k} += $v;
	$ms{$y}{$k} = int($ms{$y}{'m'.$k} * 2.5) if $ms{$y}{$k} > $ms{$y}{'m'.$k} * 2.5;
	$com .= qq|$y��<span class="st_up">$e2j{$k}�� $v ���������I</span>|;
	return $y, $v;
}
#=================================================
# �X�e�[�^�X�ُ�(to �G)
#=================================================
sub _st_ds { # �G�S��
	my($v, $z, $par) = @_;
	return if &is_bad_state($z);
	if (@enemys < 1) { # �G�S��
		$mes = '�키���肪������܂���';
		return;
	}
	for my $y (@enemys) {
		&_st_d($y, $v, $z, $par);
	}
}
sub _st_d { # �G�P��
	my($y, $v, $z, $par) = &_check_enemy(@_);
	return if $ms{$y}{hp} <= 0;
	return if $mes;
	return unless $v;
	
	if ($ms{$y}{mhp} > 999 || $ms{$y}{mdf} > 999) {
		return if $is_add_effect; # �ǉ����ʂ̏ꍇ�͔�\��
		$com .= "$y�ɂ͂����Ȃ������c";
	}
	elsif ($par > rand(100)) {
		$ms{$y}{state} = $v;
		$ms{$y}{ten} = 1; # ����̃e���V������߂�
		$com .= qq|<span class="state">$y��$e2j{state}��$v�ɂȂ�܂����I</span>|;
	}
	elsif (!$is_add_effect) { # �ǉ����ʂ̏ꍇ�͔�\��
		$com .= "$y�͂��킵���I";
	}
	return $y, $v;
}

#=================================================
# �X�e�[�^�X�ُ��(to ����)
#=================================================
sub _st_hs { # �����S��
	my($v, $z) = @_;
	return if &is_bad_state($z);
	$is_add_effect = 1;
	for my $y (@partys) {
		&_st_h($y, $v, $z);
	}
}
sub _st_h { # �����P��
	my($y, $v) = &_check_party(@_);
	return if $ms{$y}{hp} <= 0;
	return if $v eq '';
	return unless $v;
	
	# ��Ԉُ�Ɖ񕜕��@�������������ǂ���
	if ($ms{$y}{state} eq $v) {
		$com .= qq|<span class="heal">$y��$ms{$y}{state}������܂����I</span>|;
		$ms{$y}{state} = '';
	}
	elsif (!$is_add_effect) { # �ǉ����ʂ̏ꍇ�͔�\��
		$com .= "$y�ɂ͌��ʂ��Ȃ��悤���c";
	}
	return $y, $v;
}

#=================================================
# ������ʁ@���ʂ͂P�^�[��
#=================================================
# $_[0]:���薼, $_[1]:�_���[�W�C$_[2]:����
# return (����C�_���[�W)
my %tmps = (
	'���΂�'	=> sub{ for my $name (@members) { next if $ms{$name}{tmp} ne '���΂���'; next if $ms{$name}{color} ne $ms{$_[0]}{color}; $com.="$name��$_[0]�����΂����I"; return $name; }; return; },

	'��h��'	=> sub{ return if $_[1] !~ /^[0-9\-\.]+$/; return $_[0], $_[1]*0.1; },
	'�h��'		=> sub{ return if $_[1] !~ /^[0-9\-\.]+$/; return $_[0], $_[1]*0.5; },
	'�U�y��'	=> sub{ return if $_[1] !~ /^[0-9\-\.]+$/ || $_[2] ne '�U'; return $_[0], $_[1]*0.25; },
	'���y��'	=> sub{ return if $_[1] !~ /^[0-9\-\.]+$/ || $_[2] ne '��'; return $_[0], $_[1]*0.25; },
	'���y��'	=> sub{ return if $_[1] !~ /^[0-9\-\.]+$/ || $_[2] ne '��'; return $_[0], $_[1]*0.25; },

	'�Q�{'		=> sub{ return if $_[1] !~ /^[0-9\-\.]+$/; return $_[0], $_[1]*2.0; },

	'�U����'	=> sub{ return if $_[2] ne '�U'; $com.=qq|$_[0]��<span class="tmp">�U�����͂˕Ԃ����I</span>|;   return $m; },
	'������'	=> sub{ return if $_[2] ne '��'; $com.=qq|$_[0]��<span class="tmp">���@���͂˕Ԃ����I</span>|;   return $m; },
	'������'	=> sub{ return if $_[2] ne '��'; $com.=qq|$_[0]��<span class="tmp">�u���X���͂˕Ԃ����I</span>|; return $m; },
	'�x����'	=> sub{ return if $_[2] ne '�x'; $com.=qq|$_[0]��<span class="tmp">�x��Ԃ����I</span>|;         return $m; },

	'�󗬂�'	=> sub{ return if $_[2] ne '�U'; $com.=qq|$_[0]��<span class="tmp">�󗬂����I</span>|; my $y = rand(2)<1 ? $partys[int(rand(@partys))] : $enemys[int(rand(@enemys))]; $com.="�������A$_[0]�͎󗬂��̂Ɏ��s�����I" if $_[0] eq $y; return $y; },

	'���z��'	=> sub{ return if $_[2] ne '��'; my $v = $_[1] < 50 ? int(rand(20)+30) : int( $_[1] * (rand(0.3)+0.2) ); $com.=qq|$_[0]��$e2j{mp}�� <span class="heal">$v</span> �z�������I|; $ms{$_[0]}{mp} += $v; $ms{$_[0]}{mp} = $ms{$_[0]}{mmp} if $ms{$_[0]}{mp} > $ms{$_[0]}{mmp};return; },

	'�U����'	=> sub{ return if $_[2] ne '�U'; $com.=qq|$_[0]��<span class="tmp">�U�����������Ȃ��I</span>|; return $_[0], 0; },
	'������'	=> sub{ return if $_[2] ne '��'; $com.=qq|$_[0]��<span class="tmp">���@���������Ȃ��I</span>|; return $_[0], 0; },
);

sub is_bad_state {
	my $z = shift;
	if ($z eq '��' && $ms{$m}{state} eq '����') {
		if (rand(4)<1) {
			$com .= qq|<span class="heal">$m�͖��@���g����悤�ɂȂ�܂����I</span>|;
			$ms{$m}{state} = '';
		}
		else {
			$com .= "�������A$m�͖��@���������Ă���";
			return 1;
		}
	}
	elsif ($z eq '�x' && $ms{$m}{state} eq '�x��') {
		if (rand(4)<1) {
			$com .= qq|<span class="heal">$m�͗x���悤�ɂȂ�܂����I</span>|;
			$ms{$m}{state} = '';
		}
		else {
			$com .= "�������A$m�͗x�肪�������Ă���";
			return 1;
		}
	}
	elsif ($z eq '�U' && $ms{$m}{state} eq '�U��') {
		if (rand(4)<1) {
			$com .= qq|<span class="heal">$m�͕����U�����ł���悤�ɂȂ�܂����I</span>|;
			$ms{$m}{state} = '';
		}
		else {
			$com .= "�������A$m�͕����U�����������Ă���";
			return 1;
		}
	}
	return 0;
}

#=================================================
# �����`�F�b�N
#=================================================
sub _check_party {
	my($y, $v, $z, @etcs) = @_;
	
	return if &is_bad_state($z);
	
	if ($ms{$m}{state} eq '����') {
		$y = $members[int(rand(@members))];
	}
	else {
		# �w��Ȃ� or �G�̏ꍇ�̓����_���Ŗ�����I��
		$y = $partys[int(rand(@partys))] if !defined($ms{$y}{name}) || $ms{$y}{color} ne $ms{$m}{color};
		$y = $m if $ms{$y}{hp} <= 0 && $v ne '�h��';
	}
	
	# ������ʂ�����ꍇ
	if ( $ms{$y}{tmp} && defined $tmps{ $ms{$y}{tmp} } ) {
		my($y2, $v2) = &{ $tmps{ $ms{$y}{tmp} } }($y, $v, $z);
		$y = $y2 if defined $y2;
		$v = $v2 if defined $v2;
	}
	
	return $y, $v, $z, @etcs;
}

#=================================================
# �G�`�F�b�N
#=================================================
sub _check_enemy {
	my($y, $v, $z, @etcs) = @_;
	
	# �G�S��
	if (@enemys < 1) {
		$mes = '�키���肪������܂���';
		return;
	}
	return if &is_bad_state($z);
	
	if ($ms{$m}{state} eq '����') {
		$y = $members[int(rand(@members))] unless $m eq $y;
	}
	else {
		# �w��Ȃ� or �����̏ꍇ�̓����_���œG��I��
		$y = $enemys[int(rand(@enemys))] if !defined($ms{$y}{name}) || $ms{$y}{color} eq $ms{$m}{color};
		return if $ms{$y}{hp} <= 0;
	}
	
	# ������ʂ�����ꍇ
	if ( $ms{$y}{tmp} && defined $tmps{ $ms{$y}{tmp} } ) {
		my($y2, $v2) = &{ $tmps{ $ms{$y}{tmp} } }($y, $v, $z);
		$y = $y2 if defined $y2;
		$v = $v2 if defined $v2;
	}
	return $y, $v, $z, @etcs;
}


#=================================================
# �p���v���e(to �S��)
#=================================================
sub _parupunte {
	if (rand(2)<1) { # �ꎞ���
		my @tmps = ('�Q�{','�U����','������','�󗬂�');
		my $v = $tmps[int(rand(@tmps))];
		for my $y (@members) {
			next if $ms{$y}{hp} <= 0;
			$ms{$y}{tmp} = $v;
		}
		$com .= qq|�Ȃ�ƁA<span class="tmp">�S���̏�Ԃ� $v �ɂȂ�܂����I</span>|;
	}
	elsif (rand(2)<1) { # ��Ԉُ�
		my @states = ('����','����','���','�ғ�');
		my $v = $states[int(rand(@states))];
		for my $y (@members) {
			next if $ms{$y}{hp} <= 0;
			$ms{$y}{state} = $v;
			$ms{$y}{ten} = 1;
		}
		$com .= qq|�Ȃ�ƁA<span class="state">�S���� $v ��ԂɂȂ�܂����I</span>|;
	}
	elsif (rand(2)<1) { # �g�o��
		for my $y (@members) {
			next if $ms{$y}{mhp} > 999;
			$com.= qq|<span class="revive">$y�������Ԃ���</span>| if $ms{$y}{hp} <= 0;
			$ms{$y}{hp} = $ms{$y}{mhp};
		}
		$com .= qq|<span class="heal">�S����$e2j{hp}���񕜂����I</span>|;
	}
	elsif (rand(3)<1) { # �f����0
		for my $y (@members) {
			$ms{$y}{ag} = 0;
		}
		$com .= qq|�Ȃ�ƁA<span class="st_down">�S���̑̂��Ȃ܂�̂悤�ɏd���Ȃ����I</span>|;
	}
	elsif (rand(2)<1) { # �m��
		for my $y (@members) {
			next if $ms{$y}{hp} <= 0;
			next if $ms{$y}{hp} > 999;
			$ms{$y}{hp} = 1;
		}
		$com .= qq|�Ȃ�ƁA�󂩂痬�����~�肻�������I�S����<span class="damage">$e2j{mhp}�� 1 </span>�ɂȂ����I|;
	}
	else { # �����Ȃ�
		$com.= qq|�c�c�c�B�������A�����N����Ȃ������c|;
	}
}

#=================================================
# ����т��ӂ�
#=================================================
sub _yubiwofuru {
	my @r_skills = &{ 'skill_'.int(rand(@jobs)+1) };
	if (@r_skills <= 0) {
		$com .= "�������A�����N����Ȃ������c";
		return;
	}
	my $i = int(rand(@r_skills));
	my $buf_mp = $ms{$m}{mp};
	&{ $r_skills[$i][3] };
	$ms{$m}{mp} = $buf_mp if $buf_mp > $ms{$m}{mp}; # ���K���e�A���K�U���ȂǑSMP����̃X�L���̏ꍇ�́A�����I��MP��1�ɂȂ�̂ŁB
}

#=================================================
# �����ǉ�(�g����A����т���) ������(���O)�͕K���擪��@������
#=================================================
sub _add_party {
	my %y_st;
	($y_st{name}, $y_st{icon}, $y_st{hp}, $y_st{mp}, $y_st{at}, $y_st{df}, $y_st{ag}) = @_;

	my $y = $y_st{name};
	for my $k (@battle_datas) {
		$ms{$y}{$k} = 0;
	}
	for my $k (qw/hp mp at df ag/) {
		$ms{$y}{$k} = $ms{$y}{'m'.$k} = int($y_st{$k}*(rand(0.3)+0.9));
	}
	$ms{$y}{icon} = $y_st{icon};
	$ms{$y}{hit} = 95;
	$ms{$y}{ten} = 1;
	$ms{$y}{name}  = $y;
	$ms{$y}{color} = $ms{$m}{color};
	$ms{$y}{tmp}   = '';
	$ms{$y}{state} = '';
	$ms{$y}{get_exp}   = int($m{lv} * 0.5);
	$ms{$y}{get_money} = int($m{lv} * 0.25);
	push @members, $y;
	push @partys,  $y;
}

#=================================================
# �G�ǉ�(��̂��Ă��ƁA�����傤����)
#=================================================
sub _add_enemy {
	if ($win || @members >= 10) { # ���Z��A�M���h��A10�l�ȏ�
		$com .= "�������A�����N����Ȃ������c";
		return;
	}
	
	require "$stagedir/$stage.cgi";

	my @alfas = ('I'..'Z'); # �������O�̃����X�^�[�����ʂ��邽�߂ɖ��O�̌�ɂ������
	my $i = int(rand(@alfas));
	
	my $no = @appears ? $appears[int(rand(@appears))] : int(rand(@monsters)); # �o�������X�^�[
	$no = 0 unless defined $monsters[$no]; # ���݂��Ȃ�No��������
	my $name = '@'.$monsters[$no]{name}.$alfas[$i];
	$name    = '@'.$monsters[$no]{name}.$alfas[$i-1] if defined $ms{$name}{name}; # ���łɓ��������X�^�[����������
	
	if (defined $ms{$name}{name}) { # ����ł����������X�^�[����������
		$com .= "�������A�����N����Ȃ������c";
		return;
	}
	
	for my $k (@battle_datas) {
		$ms{$name}{$k} = defined $monsters[$no]{$k} ? $monsters[$no]{$k} : 0;
	}
	
	# �����f�[�^�Z�b�g(�ǂݍ��񂾃f�[�^�ɂ��łɒl������ꍇ�͂�������D��)
	for my $k (qw/hp mp at df ag/) {
		$ms{$name}{$k} = int($ms{$name}{$k} * (1 + (@partys - 2) * 0.05) ); # �p�[�e�B�[�l���ɂ�鋭���␳
		$ms{$name}{'m'.$k} ||= $ms{$name}{$k};
	}
	$ms{$name}{name}  = $name;
	$ms{$name}{color} = $npc_color;
	$ms{$name}{hit}   ||= 95;
	$ms{$name}{ten}   ||= 1;
	$ms{$name}{tmp}   ||= '';
	$ms{$name}{state} ||= '';
	
	$com .= qq|<span class="revive">$name�������ꂽ�I</span>|;
	push @members, $name;
	if ($ms{$m}{color} eq $npc_color) {
		push @partys, $name;
	}
	else {
		push @enemys, $name;
	}
}

# ���Ԃ̌��E�Ɖ摜�������n�ƃ}�b�`���Ă��邩
sub _search_job {
	my $icon_no = shift;
	for my $y (@partys) {
		next if $y eq $m;
		next if $ms{$y}{icon} =~ /mix/;
		return $y if $ms{$y}{icon} =~ m|^job/$icon_no|;
	}
	return;
}


1; # �폜�s��
