$is_npc_action = 1;

#=================================================
# ������ׂ�
#=================================================
sub shiraberu {
	my $y = shift;

	return unless defined $ms{$y}{name}; # ���݂��Ȃ��󔠖�
	return unless $ms{$y}{color} eq $npc_color;
	if ($ms{$y}{hp} <= 0) {
		$mes = "�������A�󔠂̒��g�͂�����ۂ������c";
		return;
	}
	elsif ($map) {
		if ($m{event} =~ /$maps[$py][$px]/) {
			$mes = "�P�l�P�܂ł����J���邱�Ƃ͂ł��܂���";
			return;
		}
		$m{event} = $maps[$py][$px]; # �P�l�P���̂��߂̊J�������t���O
	}
	else {
		if ($m{is_get}) {
			$mes = "�P�l�P�܂ł����J���邱�Ƃ͂ł��܂���";
			return;
		}
		$m{is_get} = 1; # �P�l�P���̂��߂̊J�������t���O
	}
	
	$ms{$y}{hp} = 0;
	
	if ($ms{$y}{get_exp} =~ /^[1-3]$/ && $ms{$y}{get_money}) {
		my $item_name = $ms{$y}{get_exp} eq '1' ? $weas[$ms{$y}{get_money}][1]
					  : $ms{$y}{get_exp} eq '2' ? $arms[$ms{$y}{get_money}][1]
					  :                           $ites[$ms{$y}{get_money}][1];

		$npc_com .= "�󔠂̒��g�́c <b>$item_name</b> �ł����I";
		if ($ms{$y}{get_exp} eq '3' && !$m{ite}) {
			$npc_com .= "$item_name����ɓ���܂����I";
			$m{ite} = $ms{$y}{get_money};
			require "./lib/_add_collection.cgi";
			&add_collection;
		}
		elsif ($m{is_full}) {
			$npc_com .= "�������A$m�̗a���菊�͂����ς��������c�B$m��$item_name��������߂�";
		}
		else {
			$npc_com .= "$item_name�͗a���菊�ɑ����܂���";
			&send_item($m, $ms{$y}{get_exp}, $ms{$y}{get_money});
		}
	}
	else {
		$npc_com .= "�������A�󔠂̒��g�͂�����ۂ������c";
	}
}

#=================================================
# NPC�̔���(���x������NPC���U�����Ȃ��悤�ɕ��ёւ���)
#=================================================
sub npc_turn {
	for my $y (@enemys) {
		next if $ms{$y}{hp} <= 0;
		next if $time - $ms{$y}{time} < $act_time;
		
		# �s���ł���NPC�������ꍇ
		my $buf_m   = $m;
		my $buf_com = $com;
		$com = '';
		$npc_name = $y;
		$m = $y;
		$ms{$y}{time} = $time;
		$is_add_effect = 0;
		
		my @buf_ps = ();
		@buf_ps = @partys;
		@partys = @enemys;
		@enemys = ();
		for my $name (@buf_ps) {
			next if $ms{$name}{hp} <= 0;
			push @enemys, $name;
		}
		
		&npc_action if @enemys >= 1;

		@enemys = @partys;
		@partys = @buf_ps;
		$npc_com = $com;
		$m   = $buf_m;
		$com = $buf_com;
		
		# �s�������L�������Ō���ɕ��ёւ�
		my $name = shift @enemys;
		@members = (@partys,@enemys,$name);
		last;
	}
}
# ------------------
# NPC�̃A�N�V��������
sub npc_action {
	push @npc_skills, &{ 'skill_'.$ms{$m}{job}     };
	
	my @npc_actions = ();
	my %npc_actions = ();
	for my $i (0.. $#npc_skills) {
		next if $npc_skills[$i][0] > $ms{$m}{sp};
		next if $npc_skills[$i][1] > $ms{$m}{mp};
		push @npc_actions, "$npc_skills[$i][2]";
		$npc_actions{$npc_skills[$i][2]} = [ $npc_skills[$i][1], $npc_skills[$i][3] ];
	}
	@npc_skills = &{ 'skill_'.$ms{$m}{old_job} };
	for my $i (0.. $#npc_skills) {
		next if $npc_skills[$i][0] > $ms{$m}{old_sp};
		next if $npc_skills[$i][1] > $ms{$m}{mp};
		push @npc_actions, "$npc_skills[$i][2]";
		$npc_actions{$npc_skills[$i][2]} = [ $npc_skills[$i][1], $npc_skills[$i][3] ];
	}
	
	# ��Ԉُ�
	if ($ms{$m}{state} eq '����') {
		$ms{$m}{state} = '';
		$com .="�������A$m�͓������Ƃ��ł��Ȃ��I";
	}
	elsif ($ms{$m}{state} eq '���') {
		if (rand(3) < 1) {
			$com .="$m�̂��тꂪ�Ȃ��Ȃ�܂����I";
			$ms{$m}{state} = '';
		}
		else {
			$com .= "$m�͂��т�ē������Ƃ��ł��Ȃ��I";
		}
	}
	elsif ($ms{$m}{state} eq '����') {
		if (rand(3) < 1) {
			$com .="$m�͖��肩�炳�߂܂����I";
			$ms{$m}{state} = '';
		}
		else {
			$com .= "$m�͖����Ă���I";
		}
	}
	else { # ����
		if ($ms{$m}{state} eq '����') {
			if (rand(3) < 1) {
				$com .="$m�͍������Ȃ���܂����I";
				$ms{$m}{state} = '';
			}
			else {
				$com .= "$m�͍������Ă���I";
			}
		}
		
		my $npc_action = $npc_actions[int(rand(@npc_actions))];
		$com .= "��$npc_action ";
		$ms{$m}{tmp} = '' if $ms{$m}{tmp} =~ /�h��|����/ || rand(3) < 1; # �h��Ɣ����ȊO�͐��^�[���c��
		&{ $npc_actions{$npc_action}[1] };
		$ms{$m}{mp} -= $npc_actions{$npc_action}[0];
		$ms{$m}{mp}  = 0 if $ms{$m}{mp} < 0;
		
		if ($ms{$m}{hp} > 0) {
			if ($ms{$m}{state} eq '�ғ�') {
				my $v = int($ms{$m}{mhp}*0.1);
				$v = int(rand(100)+950) if $v > 999;
				$ms{$m}{hp} -= $v;
				$com.=qq|$m�͖ғłɂ�� <span class="damage">$v</span> �̃_���[�W���������I|;
				
				if ($ms{$m}{hp} <= 0) {
					$ms{$m}{hp} = 0;
					&reset_status($m);
					$com .= qq!<span class="die">$m�͓|�ꂽ�I</span>!;
					&defeat($m);
				}
			}
			if ($ms{$m}{tmp} eq '��' && $ms{$m}{hp} > 0) { # ������
				my $v = $ms{$m}{mhp} > 999 ? int(rand(100)) : int($ms{$m}{mhp} * (rand(0.1)+0.1));
				$ms{$m}{hp} += $v;
				$ms{$m}{hp} = $ms{$m}{mhp} if $ms{$m}{hp} > $ms{$m}{mhp};
				$com .= qq|<b>$m</b>��$e2j{mhp}�� <span class="heal">$v</span> �񕜂����I|;
			}
		}
	}

	$ms{$m}{time} = $time;
}

sub add_treasure {
	my $count = shift || $#partys;
	for my $name (@partys) {
		--$count if $ms{$name}{hp} <= 0;
	}

	# �󔠂̖��O��摜
	my @boxes = (
		{ name => "���ʂ̕�",		icon => "mon/900.gif", },
		{ name => "�傫����",		icon => "mon/901.gif", },
		{ name => "��������",		icon => "mon/902.gif", },
		{ name => "������",		icon => "mon/903.gif", },
		{ name => "����",		icon => "mon/904.gif", },
		{ name => "�Â���",		icon => "mon/905.gif", },
		{ name => "�ۂ���",		icon => "mon/906.gif", },
	);
	
	$npc_com .= "$p_name �͕󔠂𔭌������I";
	for my $i (0 .. $count) {
		my $no = int(rand(@boxes));
		my @alfas = ('A'..'Z'); # �������O�����ʂ��邽�߂ɖ��O�̌�ɂ������
		my $name = '@'.$boxes[$no]{name}.$alfas[$i];
		
		for my $k (@battle_datas) {
			$ms{$name}{$k} = defined $boxes[$no]{$k} ? $boxes[$no]{$k} : 0;
		}
		$ms{$name}{ten} = 1   unless $ms{$name}{ten};
		for my $k (qw/hp df/) {
			$ms{$name}{'m'.$k} = 1000;
			$ms{$name}{$k}     = 1000;
		}
		
		$ms{$name}{name}  = $name;
		$ms{$name}{color} = $npc_color;
		$ms{$name}{tmp} = '������';
		$ms{$name}{state} = '';
		
		# �j���ʂɵ��ނ�ǉ�(�j���ʂɂ����`���ꏊ�Œ�ɂ���ꍇ�́A���O�s�R�����g�A�E�g���āA./stage/**.cgi��@treasures�̓���ɵ��ނ�ǉ�)
		my @orbs = (int(rand(6)+60), 60..65); # ���j�̓����_��
		my $wday = (localtime($time))[6];
		push @{$treasures[2]}, $orbs[$wday];
		
		# ����o��m�����グ�� 1,2,3,3
		my $v = int(rand(4)) + 1;
		$v = 3 if $v > 3 || @{$treasures[$v-1]} <= 0;
		$ms{$name}{get_exp} = $v;
		$ms{$name}{get_money} = $treasures[$v-1][int(rand(@{ $treasures[$v-1] }))];
		
		push @members, $name;
	}
}

sub add_boss {
	for my $no (0 .. $#bosses) {
		my $name = '@'.$bosses[$no]{name};
		
		for my $k (@battle_datas) {
			$ms{$name}{$k} = defined $bosses[$no]{$k} ? $bosses[$no]{$k} : 0;
		}
		
		# �����f�[�^�Z�b�g(�ǂݍ��񂾃f�[�^�ɂ��łɒl������ꍇ�͂�������D��)
		$ms{$name}{hit} = 95 unless $ms{$name}{hit};
		$ms{$name}{ten} = 1   unless $ms{$name}{ten};
		for my $k (qw/hp mp at df ag/) {
			$ms{$name}{$k} = int($ms{$name}{$k} * (0.9 + rand(0.3) + (@partys - 2) * 0.1) ); # �p�[�e�B�[�l���ɂ�鋭���␳
			$ms{$name}{'m'.$k} = $ms{$name}{$k} unless $ms{$name}{'m'.$k};
		}
		$ms{$name}{name} = $name;
		$ms{$name}{color} = $npc_color;
		$ms{$name}{tmp}   ||= '';
		$ms{$name}{state} ||= '';
		
		$npc_com .= "$name,";
		push @members, $name;
	}
	chop $npc_com;
	$npc_com .= "�������ꂽ�I";
}
sub add_monster {
	my $c = shift || int(rand( 2.5 + @partys * 0.6 )); # �o����
	my $s = shift || 1; # �����␳
	my @alfas = ('A'..'H'); # �������O�̃����X�^�[�����ʂ��邽�߂ɖ��O�̌�ɂ������

	for my $i (0 .. $c) {
		my $no = @appears ? $appears[int(rand(@appears))] : int(rand(@monsters)); # �o�������X�^�[
		$no = 0 unless defined $monsters[$no]; # ���݂��Ȃ�No��������
		my $name = '@'.$monsters[$no]{name}.$alfas[$i];
		
		for my $k (@battle_datas) {
			$ms{$name}{$k} = defined $monsters[$no]{$k} ? $monsters[$no]{$k} : 0;
		}
		
		# �����f�[�^�Z�b�g(�ǂݍ��񂾃f�[�^�ɂ��łɒl������ꍇ�͂�������D��)
		for my $k (qw/hp mp at df ag/) {
			$ms{$name}{$k} = int( $ms{$name}{$k} * (0.9 + rand(0.3) + (@partys - 2) * 0.1) * $s ); # �p�[�e�B�[�l���ɂ�鋭���␳
			$ms{$name}{'m'.$k} ||= $ms{$name}{$k};
		}
		$ms{$name}{name}  = $name;
		$ms{$name}{color} = $npc_color;
		$ms{$name}{hit}   ||= 95;
		$ms{$name}{ten}   ||= 1;
		$ms{$name}{tmp}   ||= '';
		$ms{$name}{state} ||= '';
		
		$npc_com .= "$name,";
		push @members, $name;
	}
	chop $npc_com;
	$npc_com .= "�������ꂽ�I";
}



1; # �폜�s��
