#=================================================
# �J�W�m���ʏ��� Created by Merino
#=================================================
# ���O�Ɏg���t�@�C��(.cgi����)
$this_file = "$casinodir/$m{quest}/log";

#=================================================
# �퓬�p�A�N�V�����Z�b�g(�v���C���[�p)
#=================================================
sub set_action {
	unless (defined $ms{$m}{name}) {
		push @actions, ('�ɂ���','��������');
		$actions{'�ɂ���'}   = sub{ &nigeru  };
		$actions{'��������'} = sub{ &sukusho };
		return;
	}

	&add_casino_action;
	push @actions, ('�ɂ���','��������');
	$actions{'�ɂ���'}   = sub{ &nigeru   };
	$actions{'��������'} = sub{ &sukusho  };
	return unless defined $ms{$m}{name};

	if ($round == 0) { # �J�n�O
		push @actions, ('������','������');
		$actions{'������'} = sub{ &kaishi };
		$actions{'������'}  = sub{ &sasou  };
		if ($m eq $leader) { # ذ�ް�̂�
			push @actions, ('������');
			$actions{'������'} = sub{ &kick };
		}
	}
}

#=================================================
# ��ʃw�b�_�[
#=================================================
sub header_html {
	print qq|<div class="mes">�y$this_title�z �R�C��<b>$m{coin}</b>��</div>|;
}


# $FH �r����������邽�߂̃O���[�o���ϐ�(���̃t�@�C���̂�)�B�����̃v���C���[�������t�@�C�������L���邽�߁B
my $FH;
#=================================================
# �����o�[�ǂݍ���
#=================================================
sub read_member {
	@members = ();
	%ms = (); # Members

	my $count = 0;
	open $FH, "+< $casinodir/$m{quest}/member.cgi" or do{ $m{lib} = ''; $m{quest} = ''; &write_user; &error("���łɃp�[�e�B�[�����U���Ă��܂����悤�ł�"); };
	eval { flock $FH, 2; };
	my $head_line = <$FH>;
	($speed,$stage,$round,$leader,$p_name,$p_pass,$p_join,$win,$bet,$is_visit,$now_bet,$max_bet) = split /<>/, $head_line;
	$act_time = $speed;
	while (my $line = <$FH>) {
		my @datas = split /<>/, $line;
		my $name  = $datas[0];
		my $i = 0;
		for my $k (@casino_datas) {
			$ms{$name}{$k} = $datas[$i];
			++$i;
		}
		push @members, $name;
	}
	
	$this_title = $stage eq '�h�b�y��' ? "$p_name �q�����<b>$bet</b>��"
				: "$p_name �����[�g<b>$bet</b>�� �����݂̃��[�g<b>$now_bet</b>�� ���ő僌�[�g<b>$max_bet</b>��";
	$bgimg = "$bgimgdir/casino.gif"; # �w�i�摜
}


#=================================================
# �����o�[��������
#=================================================
sub write_member {
	return unless -d "$casinodir/$m{quest}";
	
	my $head_line = "$speed<>$stage<>$round<>$leader<>$p_name<>$p_pass<>$p_join<>$win<>$bet<>$is_visit<>$now_bet<>$max_bet<>\n";
	my @lines = ($head_line);
	for my $name (@members) {
		my $line = '';
		for my $k (@casino_datas) {
			$line .= "$ms{$name}{$k}<>";
		}
		push @lines, "$line\n";
	}
	
	seek  $FH, 0, 0;
	truncate $FH, 0;
	print $FH @lines;
	close $FH;
}

#=================================================
# �퓬�A�N�V����
#=================================================
sub action {
	$com .= "\x20";
	$com =~ /��(.+?)(?:(?:\x20|�@)?&gt;(.+?)(?:\x20|�@)|\x20|�@)/;
	my $action = $1;
	my $target = $2 ? $2 : '';
	return unless defined $actions{$action};
 	if ($nokori > 0) {
		$mes = "�܂��s�����邱�Ƃ͂ł��܂���";
		return;
	}
	
	&{ $actions{$action} }($target);
	return if $mes;

	$m{wt}  = $time + $act_time;
	$nokori = $act_time;
	$ms{$m}{time} = $time;
	&write_member;
}


#=================================================
# ��������
#=================================================
sub sasou {
	my $y = shift;

	$act_time = 0;
	$this_file = "$logdir/casino";

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
			open my $fh, "+< $logdir/casino.cgi" or &error("$logdir/casino.cgi�t�@�C�����J���܂���");
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
# ���ɂ���
#=================================================
sub nigeru {
	$m{lib} = 'casino';

	# �N�G�X�g�̃����o�[���X�g���珜��
	my $is_join = 0;
	my @new_members = ();
	for my $name (@members) {
		if ($m eq $name) {
			$is_join = 1;
			next;
		}
		push @new_members, $name;
	}
	@members = @new_members;


	# ���w�҂͂��̂܂܋A��
	unless ($is_join) {
		$mes ="$p_name�̌��w���瓦���o���܂���";
		&reload("$p_name�̌��w���瓦���o���܂���");
		return;
	}
	
	# ��J�x�v���X
	$m{tired} += 1;
	$m{is_eat} = 0;
	
	&reload("�������瓦���o���܂���");

	# �N�����Ȃ��Ȃ�����N�G�X�g���폜
	if (@members < 1) {
		&write_member;
		$this_file = "$logdir/casino";
		&delete_directory("$casinodir/$m{quest}");
		$mes = "�������瓦���o���܂���";
	}
	else {
		&next_round;

		# ذ�ް�������ꍇذ�ް���
		if ($leader eq $m) {
			$leader = $members[0];
			$npc_com = "$p_name�̃��[�_�[��$leader�ɂȂ�܂���";
		}
		&write_member;
	}
}


#================================================
# ���Z��A�M���h��̃S�[���h�A�M���h�|�C���g�̑���
#================================================
sub add_bet {
	my($quest_id, $add_bet) = @_;

	open my $fh, "+< $casinodir/$quest_id/bet.cgi" or &error("$casinodir/$quest_id/bet.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	my $bet = <$fh>;
	$bet =~ tr/\x0D\x0A//d;
	$bet += $add_bet;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh $bet;
	close $fh;
}



# ��ݎx����
sub give_coin {
	my $give_coin = shift || $now_bet;
	$m{coin} -= $give_coin;
	&add_bet($m{quest}, $give_coin);
	$com.=qq|<span class="st_down">���ɺ�݂� <b>$give_coin</b>�� �x�����܂���</span>|;
}


# ��݂��Ȃ��l�����ޏ�
sub reload_member {
	my $winner = shift;
	my @new_members = ();
	for my $name (@members) {
		my %p = &get_you_datas($name);
		if ($p{coin} <= 0) {
			$npc_com .= qq|<span class="die">$name�ͺ�݂��Ȃ��Ȃ����I</span><br />|;
			&regist_you_data($name, 'lib', 'casino');

			# ذ�ް�������ꍇذ�ް���
			if ($leader eq $name && $winner) {
				$leader = $winner;
				$npc_com .= "$p_name�̃��[�_�[��$leader�ɂȂ�܂���";
			}
		}
		else {
			$ms{$name}{action} = '�ҋ@��' unless $stage eq '�n�C���E';
			push @new_members, $name;
		}
	}
	@members = @new_members;
}

# �܋�
sub get_coin {
	open my $fh, "+< $casinodir/$m{quest}/bet.cgi" or &error("$casinodir/$m{quest}/bet.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	my $get_coin = <$fh>;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh 0;
	close $fh;
	$get_coin =~ tr/\x0D\x0A//d;
	return $get_coin;
}

1; # �폜�s��
