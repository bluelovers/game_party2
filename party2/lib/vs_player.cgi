require "./lib/_battle.cgi";
$is_npc_action = 0;
#=================================================
# �p�[�e�B�[�� Created by Merino
#=================================================
# �����J�E���g���v�Z
# �܋��v�Z

# �p�[�e�B�[�J���[(NPC�J���[�ƃf�t�H���g�J���[�͎g������~)
%colors = (
	'#FF3333'	=> '���b�h',
	'#FF33CC'	=> '�s���N',
	'#FF9933'	=> '�I�����W',
	'#FFFF33'	=> '�C�G���[',
	'#33FF33'	=> '�O���[��',
	'#33CCFF'	=> '�A�N�A',
	'#6666FF'	=> '�u���[',
	'#CC66FF'	=> '�p�[�v��',
	'#CCCCCC'	=> '�O���C',
);

#=================================================
# �^�C�g���A�w�i�摜
#=================================================
sub get_header_data {
	$bgimg = "$bgimgdir/stage$stage.gif";
	$this_title = "$p_name(<b>$win</b>�揟) <b>$round</b>����";
}
#=================================================
# �ǉ��A�N�V����
#=================================================
sub add_battle_action {
	if ($round <= 0) {
		push @actions, '����ׂ�';
		push @actions, '�ρ[�Ă��[';
		$actions{'����ׂ�'}   = [0,	sub{ &shiraberu }];
		$actions{'�ρ[�Ă��['} = [0,	sub{ &party }];
	}

	push @actions, '������';
	$actions{'������'}     = [0,	sub{ &kaishi }];
}


#=================================================
# ���ρ[�Ă��[
#=================================================
sub party {
	$target = shift;
	
	if ($round > 0) {
		$mes = "�퓬�̓r���ŕύX���邱�Ƃ͂ł��܂���";
		return;
	}
	
	my %r_colors = reverse %colors;
	if (defined $r_colors{$target}) {
		$ms{$m}{color} = $r_colors{$target};
		$com.=qq|<font color="$r_colors{$target}">$target</font>�p�[�e�B�[�ɓ���܂����I|;
		return;
	}
	
	my $p = '';
	for my $k (keys %colors) {
		$p .= qq|<span onclick="text_set('���ρ[�Ă��[>$colors{$k} ')" style="color: $k;">$colors{$k}</span> / |;
	}
	$mes = "�ǂ̃p�[�e�B�[�ɓ���܂����H<br />$p";
}

#=================================================
# ��������
#=================================================
sub kaishi {
	# �퓬�J�n�O
	if ($round < 1) {
		my %teams = ();
		for my $name (@members) {
			$mes .= "$name," if !$ms{$name}{color} || $ms{$name}{color} eq $default_color;
			++$teams{ $ms{$name}{color} } unless $teams{ $ms{$name}{color} };
		}
		if (keys %teams <= 1) {
			$mes = "�ΐ킷��p�[�e�B�[�����܂���";
			return;
		}
		elsif ($mes) {
			$mes .= "�̃v���C���[���A�܂��p�[�e�B�[�����߂Ă��܂���";
			return;
		}
		elsif ($leader ne $m) {
			$mes = "��Ԏn�߂� �������� �����邱�Ƃ��ł���̂̓��[�_�[�݂̂ł�";
			return;
		}
	}
	else {
		# �܋��z��I���B
		unless (-s "$questdir/$m{quest}/bet.cgi") {
			$mes .= "���N�G�X�g�͏I�����܂����B���ɂ���ŉ��U���Ă�������";
			return;
		}
		# �Ȃ��Ȃ����������Ȃ��ꍇ�B�����I��
		if ($round > 10) {
			$mes = "$round ���E���h�܂Ō��������܂���ł����B���ɂ���ŉ��U���Ă�������";
			return;
		}

		my $win_color    = '';
		my $alive_team_c = 0;
		
		for my $name (@members) {
			next if $ms{$name}{hp} < 1;
			unless ($win_color eq $ms{$name}{color}) {
				$win_color = $ms{$name}{color};
				++$alive_team_c;
			}
		}
		
		# ������
		if ($alive_team_c eq '0') {
			$npc_com = "�� $round ���E���h�̏����̌��ʂ� �u���������I�v<br />";
		}
		# �P�p�[�e�B�[�̂ݎc���Ă�����
		elsif ($alive_team_c eq '1') {
			my $winner = '';
			my %win_c = ();

			open my $fh, "+< $questdir/$m{quest}/win.cgi" or &error("$questdir/$m{quest}/win.cgi�t�@�C�����J���܂���");
			eval { flock $fh, 2; };
			my $line = <$fh>;
			$line =~ tr/\x0D\x0A//d;
			$line .= "$win_color,";
			for my $c (split /,/, $line) {
				if (++$win_c{$c} >= $win) {
					$winner = $c;
					last;
				}
			}
			seek  $fh, 0, 0;
			truncate $fh, 0;
			print $fh $line;
			close $fh;
			
			# �D���p�[�e�B�[����
			if ($winner) {
				&give_bet($winner);
				return;
			}
			# �Ȃ��Ȃ����������Ȃ��ꍇ�B�����I��
			elsif ($round > 10) {
				$mes = "$round ���E���h�܂Ō��������܂���ł����B���ɂ���ŉ��U���Ă�������";
				return;
			}
			
			# ���݂̓r���o��
			for my $c (sort { $b <=> $a } keys %win_c) {
				$npc_com .= qq|<font color="$c">$colors{$c} $win_c{$c}��</font> / |;
			}
		}
		# �c��P�p�[�e�B�[�ɂȂ�܂�
		else {
			$mes .= "���������Ă��܂���";
			return;
		}
	}
	
	&reset_status_all;

	# ���т�F���ƂɃV���b�t��
	&shuffle;

	for my $name (@members) {
		# ���E���h���ɑS�v���C���[��HP��
		$ms{$name}{hp} = $ms{$name}{mhp};
		
		# �J�n�O�̑ҋ@���Ԃ����ꂼ��^����
		next if $m eq $name;
		&regist_you_data($name, 'wt', int($time + $speed * 2 + rand(4)) );
	}
	$act_time = $speed * 2; # ���J�n�����l�p

	++$round;
	$npc_com .= "�� $round ���E���h�����J�n�I";
	&auto_reload;
}

sub give_bet {
	my $winner = shift;
	
	my @win_members = ();
	for my $name (@members) {
		next unless $ms{$name}{color} eq $winner;
		push @win_members, $name;
	}
	
	open my $fh, "+< $questdir/$m{quest}/bet.cgi" or &error("$questdir/$m{quest}/bet.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	my $prize_money = <$fh>;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	close $fh;
	$prize_money =~ tr/\x0D\x0A//d;
	
	if (@win_members <= 0) {
		$npc_com .= "�D���p�[�e�B�[�����Ȃ��悤�ł��c";
		return;
	}
	
	my $p_money = int($prize_money / @win_members);
	
	for my $name (@win_members) {
		&send_money($name, $p_money, "$p_name�̓��Z��̏܋�");
		$names .= "$name,";
	}
	chop $names;
	$npc_com .= "�D���p�[�e�B�[��$names�� <b>$p_money</b> G�������܂����I";
}


sub npc_turn { return } # �O�̂��߃n�}���h�~


1; # �폜�s��
