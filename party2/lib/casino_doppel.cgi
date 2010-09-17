require "./lib/_casino.cgi";
#=================================================
# �h�b�y�� Created by Merino
#=================================================

@cards = ('��','��','��','��','��','��','��','��');

#=================================================
# �퓬�p�A�N�V�����Z�b�g(�v���C���[�p)
#=================================================
sub add_casino_action {
	return if $ms{$m}{action};
	for my $i (0..$now_bet) {
		push @actions, $cards[$i];
		$actions{$cards[$i]} = sub{ &mark($cards[$i]) };
		last if $i >= $#cards;
	}
}

#=================================================
# �����o�[�o��
#=================================================
sub member_html {
	my $member_html = '';
	$member_html .= qq|<div style="background: url($bgimg) #333 repeat-x left bottom;"><table><tr>|;
	for my $name (@members) {
		$member_html .= qq|<td onclick="text_set('>$name ')" align="center" valign="bottom"><span style="color: $ms{$name}{color}; font-size: 11px; background-color: #333;">|;
		$member_html .= qq|$ms{$name}{action}<br />| if $ms{$name}{action};
		$member_html .= $round <= 0 || $m eq $name ? qq|$ms{$name}{card}| : qq|�H| if $ms{$name}{card};
		$member_html .= qq|<br />|;
		$member_html .= qq|<img src="$icondir/etc/mark_leader.gif" />| if $leader eq $name;
		$member_html .= qq|$name</span><br /><img src="$icondir/$ms{$name}{icon}" alt="$name" /></td>|;
	}
	$member_html .=  qq|</tr></table></div>|;
	return $member_html;
}

#=================================================
# �����`��
#=================================================
sub mark {
	return if $ms{$m}{action};
	my $mark = shift or return;
	
	$com =~ s/��.+?(\x20|�@)//g; # �}�[�N���폜
	if ($ms{$m}{card}) {
		$com.=qq|<span class="st_up">$m���J�[�h��ς��܂����I</span>|;
	}
	else {
		$com.=qq|<span class="st_up">$m���J�[�h�����߂܂����I</span>|;
		&give_coin($bet);
	}
	$ms{$m}{card} = $mark;
	&next_round;
}

#=================================================
# ��������
#=================================================
sub kaishi {
	if (@members <= 1) {
		$mes = "�ΐ킷�鑊�肪���܂���";
		return;
	}
	elsif ($leader ne $m) {
		$mes = "�������� �����邱�Ƃ��ł���̂̓��[�_�[�݂̂ł�";
		return;
	}
	
	# ������
	for my $name (@members) {
		$ms{$name}{action} = '';
		$ms{$name}{card}   = '';
	}
	
	$now_bet = @members; # �l���ɂ���đI�ׂ�J�[�h�����ς��
	++$round;
	$npc_com .= "<b>�Q�[���J�n�I�I</b>";
	&auto_reload;
}

#=================================================
# �S���̃A�N�V�������`�F�b�N
#=================================================
sub next_round {
	return if $round <= 0;

	# �S���J�[�h�����܂�����
	&battle if &is_all_select;
}
# ------------------
# �S���s���ς݁H
sub is_all_select {
	for my $name (@members) {
		next if $ms{$name}{action};
		return 0 if $ms{$name}{card} eq '';
	}
	return 1;
}

#=================================================
# ����
#=================================================
sub battle {
	# �܋�
	my $get_coin = &get_coin;
	return if $get_coin <= 0;

	my @winners = ();
	for my $name (@members) {
		next if $ms{$name}{action}; # �ҋ@���̐l�̓X���[
		next if $leader eq $name; # �e�̓X���[
		next if $ms{$leader}{card} ne $ms{$name}{card}; # �Ⴄ�J�[�h�̐l�̓X���[
		push @winners, $name;
	}
	if (@winners >= 1) { # �q�̏���
		my $s_coin = int($get_coin / @winners);
		for my $winner (@winners) {
			my %p = &get_you_datas($winner);
			&regist_you_data($winner, 'cas_c', ++$p{cas_c});
			&regist_you_data($winner, 'coin', $p{coin}+$s_coin);
		}
		
		if (@winners > 1) {
			my $winners = join "�A", @winners;
			$npc_com .= qq|�h�b�y���I�I�c$leader�̃J�[�h�́y$ms{$leader}{card}�z�����J�[�h�̐l�� $winners�I����āA<span class="get">���҂� $winners �������ꂼ��ɶ��ɺ�� <span class="damage">$s_coin</span> �����������܂�</span><br />|;
		}
		else {
			$npc_com .= qq|�h�b�y���I�I�c$leader�̃J�[�h�́y$ms{$leader}{card}�z�����J�[�h�̐l�� <b>$winners[0]</b>�I����āA<span class="get">���҂� <b>$winners[0]</b> �ɶ��ɺ�� <span class="damage">$s_coin</span> �����������܂�</span><br />|;
		}
		
		&reload_member();
		$leader = $winners[int rand @winners];
		$npc_com .= "$p_name�̃��[�_�[��$leader�ɂȂ�܂���";
	}
	else { # �e�̏���
		my %p = &get_you_datas($leader);
		&regist_you_data($winner, 'cas_c', $p{cas_c}++);
		&regist_you_data($leader, 'coin', $p{coin}+$get_coin);

		$npc_com .= qq|�h�b�y���I�I�c$leader�̃J�[�h�́y$ms{$leader}{card}�z�����J�[�h�̐l�͂��܂���I����āA<span class="get">���҂� <b>$leader</b> �ɶ��ɺ�� <span class="damage">$get_coin</span> �����������܂�</span>|;
		&reload_member($leader);
	}
	
	$round = 0;
}


1; # �폜�s��
