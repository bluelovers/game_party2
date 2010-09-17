require "./lib/_skill.cgi";
#=================================================
# �퓬���� Created by Merino
# vs_player.cgi,vs_monster.cgi,vs_guild.cgi���ʃT�u���[�`�� 
#=================================================
# ���O�Ɏg���t�@�C��(.cgi����)
$this_file = "$questdir/$m{quest}/log";


#=================================================
# �|�����Ƃ��̏���
#=================================================
sub defeat {
	my $y = shift;
	
	# �����̏��
	if ($ms{$y}{tmp} eq '����') {
		$ms{$y}{tmp} = '';
		$ms{$y}{hp}  = int($ms{$y}{mhp} * (rand(0.1)+0.1));
		$com.=qq|<span class="revive">$y�͕m���ł�݂��������I</span>|;
		&reset_status($y);
		return;
	}
	
	# ��ԂȂǏ�����
	$ms{$y}{hp} = 0;
	&reset_status($y);
	
	# NPC���v���C���[��|�������B�܂��͎���
	return if $ms{$m}{color} eq $npc_color || $m eq $y;

	$com .= qq|<br /><span class="get">$m�����͂��ꂼ�� $ms{$y}{get_exp} ��$e2j{exp}�� $ms{$y}{get_money} G����ɓ��ꂽ�I</span>|;
	
	for my $name (@partys) {
		next if $ms{$name}{hp} <= 0;
		if ($name eq $m) { # �|�����l
			$m{exp}   += $ms{$y}{get_exp};
			$m{money} += $ms{$y}{get_money};
			
			my $par = 2; # ���ԂɂȂ�m��(�������ア)
			if ( &is_strong(%{ $ms{$y} }) ) { # ������苭������
				$win ? $m{kill_p}++ : $m{kill_m}++;
				$par = 1 unless $ms{$m}{job} eq '12'; # ���ԂɂȂ�m��(������苭��)�B�������A�����g���Ȃ�m�������炸�B
			}
			$par += 2 if $m{ite} eq '77'; # �����̴�
			
			if (!$win && $ms{$y}{color} eq $npc_color && rand(200) < $par) { # �����X�^�[�Q�b�g
				my $base_name = $y;
				$base_name =~ s/^\@//; # �퓬��@������
				$base_name =~ s/[A-Z]$//; # ������A�`Z������
				$npc_name = $base_name; 
				$npc_com .= "<br />" if $npc_com;
				$npc_com .= qq|�Ȃ��<img src="$icondir/$ms{$y}{icon}" />$base_name ���N���オ�肱��������Ă���B|;
				if ( &is_full_monster($id) ) {
					$npc_com .= "�������A$m�̃����X�^�[�a���菊�͂����ς��������B$base_name�͔߂������ɋ����Ă������c";
				}
				else {
					$npc_com .= "$base_name�͂��ꂵ������$m�̃����X�^�[�a���菊�Ɍ�������";
					
					open my $fh, ">> $userdir/$id/monster.cgi";
					print $fh "$base_name<>$ms{$y}{icon}<>\n";
					close $fh;
					
					require "./lib/_add_monster_book.cgi";
					&add_monster_book($y);
				}
			}
		}
		else { # ���ԃ����o�[�̂��ꂼ��̃t�@�C�����J���ăv���X����
			my $yid = unpack 'H*', $name;
			next unless -f "$userdir/$yid/user.cgi";
			open my $fh, ">> $userdir/$yid/stock.cgi" or &error("$userdir/$yid/stock.cgi�t�@�C�����J���܂���");
			print $fh "$ms{$y}{get_exp}<>$ms{$y}{get_money}<>\n";
			close $fh;
		}
	}
}

#=================================================
# ���x���A�b�v
#=================================================
sub lv_up {
	++$m{lv};
	++$m{sp};
	++$ms{$m}{sp};
	$npc_com .= "<br />" if $npc_com;
	$npc_com .= qq|<span class="lv_up">$m�̃��x�����オ������$e2j{lv}$m{lv}�ɂȂ����I|;

	my $i = 2;
	for my $k (qw/hp mp at df ag/) {
		my $v = int(rand($jobs[$m{job}][$i]+1));
		$v = int(rand(9)+1) if $v > 9;
		if ($k eq 'hp') {
			++$v;
			$m{'m'.$k} += $v;
		}
		elsif ($k eq 'mp')  {
			$m{'m'.$k} += $v;
		}
		else {
			$m{$k} += $v;
		}
		$ms{$m}{'m'.$k} += $v;
		$npc_com .= "$e2j{$k}�{$v ";
		++$i;
	}
	
	my @skills = &{ 'skill_'.$ms{$m}{job} };
	for my $i (0..$#skills) {
		if ($skills[$i][0] eq $m{sp}) {
			$npc_com .= qq|<br /><b>$m�͐V���� $skills[$i][2] ���o�����I</b>|;
		}
	}
	$npc_com .= qq|</span>|;
}

#=================================================
# �X�e�[�^�X�\��
#=================================================
sub header_html {
	print qq|<div class="mes">�y$this_title�z|;
	print qq| $e2j{mhp}<b>$ms{$m}{hp}</b>/<b>$ms{$m}{mhp}</b> $e2j{mmp}<b>$ms{$m}{mp}</b>/<b>$ms{$m}{mmp}</b>|;
	print qq| $e2j{at}<b>$ms{$m}{at}</b> $e2j{df}<b>$ms{$m}{df}</b> $e2j{ag}<b>$ms{$m}{ag}</b> $jobs[$m{job}][1](<b>$m{sp}</b>)|;
	print qq| $jobs[$m{old_job}][1](<b>$m{old_sp}</b>)| if $m{old_job};
	print qq| E�F$ites[$m{ite}][1]| if $m{ite};
	print qq|</div>|;
}

#=================================================
# �����o�[�o��
#=================================================
sub member_html {
	my $member_html = '';
	$member_html .= qq|<div style="background: url($bgimg) #333 repeat-x center bottom;"><table><tr>|;
	for my $name (@members) {
		next if $ms{$name}{hp} <= 0 && ($ms{$m}{color} ne $ms{$name}{color} || $name =~ /^@/); # ���ꂽ�G��g���������
		my $par = int($ms{$name}{hp} / $ms{$name}{mhp} * 100);
		my $_mhp = $ms{$name}{mhp} > 999 ? '???' : $ms{$name}{mhp};
		my $_hp  = $ms{$name}{hp}  > 999 ? '???' : $ms{$name}{hp};
		$member_html .= qq|<td onclick="text_set('>$name ')" align="center" valign="bottom"><div class="battle-disp" style="color: $ms{$name}{color};">|;
		$member_html .= $ms{$name}{tmp} || $ms{$name}{state} ? qq|<span class="state">$ms{$name}{state}</span><span class="tmp">$ms{$name}{tmp}</span>| : defined($ten_names{ $ms{$name}{ten} }) ? $ten_names{ $ms{$name}{ten} } : q{};
		$member_html .= qq|<br />$_hp <span style="color: #99C;">/</span> $_mhp<div class="gage_back2"><img src="$htmldir/space.gif" width="$par%" class="gage_bar2" /></div>$name<br /></div>|;
		$member_html .= $ms{$name}{hp} <= 0 ? qq|<img src="$icondir/chr/099.gif" alt="$name" /></td>| : qq|<img src="$icondir/$ms{$name}{icon}" alt="$name" /></td>|;
	}
	$member_html .= qq|</tr></table></div>|;
	return $member_html;
}


# $FH �r����������邽�߂̃O���[�o���ϐ�(���̃t�@�C���̂�)�B�����̃v���C���[�������t�@�C�������L���邽�߁B
my $FH;
#=================================================
# �����o�[�ǂݍ���
#=================================================
sub read_member {
	@members = ();
	@enemys = ();
	@partys = ();
	%ms = (); # Members

	my $count = 0;
	open $FH, "+< $questdir/$m{quest}/member.cgi" or do{ $m{lib} = ''; $m{quest} = ''; &write_user; &error("���łɃp�[�e�B�[�����U���Ă��܂����悤�ł�"); };
	eval { flock $FH, 2; };
	my $head_line = <$FH>;
	($speed,$stage,$round,$leader,$p_name,$p_pass,$p_join,$win,$bet,$is_visit,$need_join,$type,$map,$py,$px,$event) = split /<>/, $head_line;
	$act_time = $speed;
	while (my $line = <$FH>) {
		my @datas = split /<>/, $line;
		my $name  = $datas[0];
		my $i = 0;
		for my $k (@battle_datas) {
			$ms{$name}{$k} = $datas[$i];
			++$i;
		}
		# �����`�F�b�N(���肦�Ȃ��f�[�^)�B�����N�G�X�g�폜�B
		if (!defined($ms{$name}{mhp}) || $ms{$name}{mhp} <= 0) {
			close $FH;
			&delete_directory("$questdir/$m{quest}");
			&error("�f�[�^�����Ă��܂��B�N�G�X�g�������I�����܂�");
		}
		push @members, $name;
	}
	
	for my $name (@members) {
		if (defined($ms{$m}{name}) && $ms{$m}{color} eq $ms{$name}{color}) {
			push @partys, $name;
		}
		else {
			next if $ms{$name}{hp} <= 0;
			push @enemys, $name;
		}
	}
}


#=================================================
# �����o�[��������
#=================================================
sub write_member {
	return unless -d "$questdir/$m{quest}";
	
	my $head_line = "$speed<>$stage<>$round<>$leader<>$p_name<>$p_pass<>$p_join<>$win<>$bet<>$is_visit<>$need_join<>$type<>$map<>$py<>$px<>$event<>\n";
	my @lines = ($head_line);
	for my $name (@members) {
		next if $name =~ /^@/ && $ms{$name}{hp} <= 0; # ���ꂽNPC��g���������
		my $line = '';
		for my $k (@battle_datas) {
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
	return unless defined $actions{$action}[1];
	if ($time - $ms{$m}{time} < $act_time) {
		$mes = "�܂��s�����邱�Ƃ͂ł��܂���";
		return;
	}
	
	if ($action eq '�����₫') {
		&sasayaki($target);
		return;
	}
	elsif ($action eq '��������') {
		&sukusho($target);
		return;
	}
	elsif (!defined($ms{$m}{name}) || $ms{$m}{hp} <= 0) {
		if ($action eq '�ɂ���') {
			&nigeru;
		}
		elsif ($win && $action eq '������') { # �������̎��p
			&kaishi;
			&write_member;
		}
		else {
			$mes = '�퓬�s�\�ɂ��s���ł��܂���';
		}
		return;
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
			if (rand(5) < 1) {
				$com .="$m�͍������Ȃ���܂����I";
				$ms{$m}{state} = '';
			}
			else {
				$com .= "$m�͍������Ă���I";
			}
		}
		
		$ms{$m}{tmp} = '' if $ms{$m}{tmp} =~ /�h��|����/ || rand(3) < 1; # �h��Ɣ����ȊO�͐��^�[���c��
		&{ $actions{$action}[1] }($target);
		return if $mes;
		
		$ms{$m}{mp} -= $actions{$action}[0];
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
	&get_stock if -s "$userdir/$id/stock.cgi"; # �擾�o���l�A�������f�[�^�ɔ��f
	if ($m{lv} < 99 && $m{exp} >= $m{lv} * $m{lv} * 10) {
		&lv_up;
	}
	elsif ($is_npc_action && @enemys > 0 && !$npc_com) {
		&npc_turn;
	}
	
	$m{wt}  = $time + $act_time;
	$nokori = $act_time;
	$ms{$m}{time} = $time;
	&write_member;
}


#=================================================
# ���ɂ���
#=================================================
sub nigeru {
	$is_npc_action = 0;
	$m{lib} = 'quest';

	# �N�G�X�g�̃����o�[���X�g���珜��
	my $is_join = 0;
	my @new_members = ();
	my @dummy_members = ();
	for my $name (@members) {
		if ($m eq $name) {
			$is_join = 1;
			next;
		}
		$name =~ /^@/ ? push @dummy_members, $name : push @new_members, $name;
	}
	@members = @new_members;

	# ���w�҂͂��̂܂܋A��
	unless ($is_join) {
		$mes ="$p_name�̌��w���瓦���o���܂���";
		&reload("$p_name�̌��w���瓦���o���܂���");
		return;
	}
	
	&get_stock if -s "$userdir/$id/stock.cgi"; # �擾�o���l�A�������f�[�^�ɔ��f
	
	# ��J�x�v���X
	$m{tired} += $round * 3 + 1;
	$m{is_eat} = 0;
	$m{hp} = $ms{$m}{hp};
	$m{mp} = $ms{$m}{mp};
	$m{hp} = $m{mhp} if $m{hp} > $m{mhp};
	$m{mp} = $m{mmp} if $m{mp} > $m{mmp};
	$m{exp}   += $round * 20 if $m{ite} eq '105'; # �K���̂���
	$m{money} += int($round * rand(77)) if $m{ite} eq '106'; # ���̌{
	
	if ($round <= 0 && $win > 0) {
		# ���Z��ŊJ�n�O�ɔ������ꍇ�B�ԋ�
		if ($type eq '4') {
			$m{money} += $bet;
			&add_bet($m{quest}, "-$bet");
			&reload("�퓬���瓦���o���܂���<br />�q������ $bet G���ԋ�����܂���");
		}
		# �M���h��Ŕ������ꍇ�B�D���M���h�|�C���g��
		elsif($type eq '5') {
			&add_bet($m{quest}, "-2");
			&reload("�퓬���瓦���o���܂���");
		}
		else {
			&reload("�퓬���瓦���o���܂���");
		}
	}
	else {
		&reload("�퓬���瓦���o���܂���");
	}

	# �N�����Ȃ��Ȃ�����N�G�X�g���폜
	if (@members < 1 && ($type ne '6' || ($type eq '6' && $ms{$leader}{hp} <= 0)) ) { # ����킶��Ȃ����Ńv���C���[���O�l���A�����Ń{�X�̂g�o���O�ȉ�
		&write_member;
		$this_file = "$logdir/quest";
		&delete_directory("$questdir/$m{quest}");
		$mes = "�퓬���瓦���o���܂���";
	}
	else {
		# ذ�ް�������ꍇذ�ް���
		if ($leader eq $m) {
			$leader = $members[0];
			$npc_com = "$p_name�̃��[�_�[��$leader�ɂȂ�܂���";
		}
		push @members, @dummy_members;
		&write_member;
	}
}

# �����v�Z
sub strong {
	my %p = @_;	
	return int($p{mhp} + $p{mmp} + $p{at} + $p{df} * 0.5 + $p{ag});
}
sub is_strong {
	my %p = @_;
	&strong(%p) > &strong(%m) * 0.5 ? return 1 : return 0;
}

# ��ԂȂǂ̒l���f�t�H���g�ɖ߂�
sub reset_status {
	my $y = shift;
	$ms{$y}{state} = '';
	$ms{$y}{tmp} = '';
	$ms{$y}{ten} = 1;
	$ms{$y}{hit} = 95;
	$ms{$y}{at} = $ms{$y}{mat} + $weas[$ms{$y}{wea}][3];
	$ms{$y}{df} = $ms{$y}{mdf} + $arms[$ms{$y}{arm}][3];
	$ms{$y}{ag} = $ms{$y}{mag} - $weas[$ms{$y}{wea}][4] - $arms[$ms{$y}{arm}][4];
	&{ $ites[$ms{$y}{ite}][4] }($y) if $ites[$ms{$y}{ite}][3] eq '3'; # �����i(�퓬�J�n���A���S���A���Ă��͂ǂ��Ȃ� &reset_status�̎�)
	$ms{$y}{ag} = 0 if $ms{$y}{ag} < 0;
}
sub reset_status_all {
	for my $name (@members) {
		&reset_status($name);
	}
}



# ���я���F���ƂɃV���b�t��
sub shuffle {
	# �S�F�擾
	my %teams = ();
	for my $name (@members) {
		++$teams{ $ms{$name}{color} };
	}
	
	# �F���V���b�t��
	my @new_team_colors = ();
	my(@team_colors) = keys %teams;
	while (@team_colors) {
		push( @new_team_colors, splice(@team_colors, rand @team_colors, 1) );
	}
	
	# �F���Ƀ����o�[����ъ���
	my @new_members = ();
	for my $new_team_color (@new_team_colors) {
		for my $name (@members) {
			if ($new_team_color eq $ms{$name}{color}) {
				push @new_members, $name;
			}
		}
	}
	@members = @new_members;
}

sub get_stock {
	open my $fh, "+< $userdir/$id/stock.cgi" or &error("$userdir/$id/stock.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($exp, $money) = split /<>/, $line;
		$m{exp} += $exp;
		$m{money} += $money;
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	close $fh;
}


1; # �폜�s��
