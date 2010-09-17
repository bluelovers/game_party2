require "./lib/_battle.cgi";
$is_npc_action = 0;
#=================================================
# �M���h�� Created by Merino
#=================================================
# �O���[�h�A�b�v�ɕK�v�Ȗ���
my $need_medal = 5;

# �������_��
my @win_medals = (
	# ���O		./icon/����̉摜�ւ̃p�X
	['������',	'etc/win_medal1.gif'], # 0
	['������',	'etc/win_medal2.gif'], # 5
	['������',	'etc/win_medal3.gif'], # 25
	['�M��',	'etc/win_medal4.gif'], # 125
	['��̨�',	'etc/win_medal5.gif'], # 625
	['�D���t',	'etc/win_medal6.gif'], # 3125
	['���Ҕt',	'etc/win_medal7.gif'], # 15625
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
		$actions{'����ׂ�'}   = [0,	sub{ &shiraberu }];
	}

	push @actions, '������';
	$actions{'������'}     = [0,	sub{ &kaishi }];
}

#=================================================
# ��������
#=================================================
sub kaishi {
	# �퓬�J�n�O
	if ($round < 1) {
		my %teams = ();
		for my $name (@members) {
			++$teams{ $ms{$name}{color} } unless $teams{ $ms{$name}{color} };
		}
		if (keys %teams <= 1) {
			$mes = "�ΐ킷��M���h�����܂���";
			return;
		}
		elsif ($leader ne $m) {
			$mes = "��Ԏn�߂� �������� �����邱�Ƃ��ł���̂̓��[�_�[�݂̂ł�";
			return;
		}
	}
	else {
		# �f�o���Z��
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
			
			my %guilds = &get_guilds;
			
			&regist_guild_data('point', 3, $guilds{$win_color});
			
			# ���݂̓r���o��
			for my $c (sort { $b <=> $a } keys %win_c) {
				$npc_com .= qq|<font color="$c">$guilds{$c} $win_c{$c}��</font> / |;
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

# �M���h���ƃM���h�F���n�b�V���ɃZ�b�g
sub get_guilds {
	my %guilds = ();
	open my $fh, "< $questdir/$m{quest}/guild.cgi" or &error("$questdir/$m{quest}/guild.cgi�t�@�C�����ǂݍ��߂܂���");
	while (my $line = <$fh>) {
		my($gcolor, $gname) = split /<>/, $line;
		$guilds{$gcolor} = $gname;
	}
	close $fh;

	return %guilds;
}

# �D���M���h�ɃM���h�|�C���g����������
sub give_bet {
	my $winner = shift;
	
	my %guilds = &get_guilds;

	open my $fh, "+< $questdir/$m{quest}/bet.cgi" or &error("$questdir/$m{quest}/bet.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	my $prize_money = <$fh>;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	close $fh;
	$prize_money =~ tr/\x0D\x0A//d;

	&regist_guild_data('point', $prize_money, $guilds{$winner});

	my $names = '';
	for my $name (@members) {
		&regist_guild_data('point', 4, $guilds{ $ms{$name}{color} });
		$names .= "$name," if $ms{$name}{color} eq $winner;
	}
	chop $names;
	$npc_com .= qq|�D����$names���������� <b style="color: $winner;">*+.$guilds{$winner}�M���h.+*</b> �ł��I|;

	&give_medal($guilds{$winner});
}

# �����M���h�ɏ������_������������
sub give_medal {
	my $gname = shift;
	
	my $gid = unpack 'H*', $gname;
	return unless -f "$guilddir/$gid/log_member.cgi"; # �M���h���U���Ă����ꍇ

	my %counts = ();
	my @lines = ();
	open my $fh, "+< $guilddir/$gid/log_member.cgi" or &error("$guilddir/$gid/log_member.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($ltime, $is_npc, $name, $laddr, $icon, $color) = split /<>/, $line;
		$counts{$icon}++ if $is_npc;
		push @lines, $line;
	}
	$counts{$win_medals[0][1]}++;
	push @lines, "$time<>1<>$win_medals[0][0]$counts{$win_medals[0][1]}<>0<>$win_medals[0][1]<>$npc_color<>\n";
	
	# �������_���̃O���[�h�A�b�v����
	for my $i (0 .. $#win_medals-1) {
		next unless defined($counts{$win_medals[$i][1]});  # %win_medals�ɂȂ�����
		last if $counts{$win_medals[$i][1]} < $need_medal; # �K�v�����ɓ��B���Ă��Ȃ�

		# �K�v���_�����ɂȂ������̂������ăO���[�h�A�b�v������
		my @new_lines = ();
		for my $line (@lines) {
			my($ltime, $is_npc, $name, $laddr, $icon, $color) = split /<>/, $line;
			next if $icon eq $win_medals[$i][1];
			push @new_lines, $line;
		}
		$counts{$win_medals[$i+1][1]}++;
		push @new_lines, "$time<>1<>$win_medals[$i+1][0]$counts{$win_medals[$i+1][1]}<>0<>$win_medals[$i+1][1]<>$npc_color<>\n";
		@lines = @new_lines;
	}
	
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}

sub npc_turn { return } # �O�̂��߃n�}���h�~

1; # �폜�s��
