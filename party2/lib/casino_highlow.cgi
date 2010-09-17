require "./lib/_casino.cgi";
#=================================================
# �n�C���E Created by Merino
#=================================================
# �J�[�h���`��(�ǉ�/�ύX/�폜�\)
@cards = ('�`','�Q','�R','�S','�T','�U','�V','�W','�X','10','�i','�p','�j');

#=================================================
# �A�N�V�������[�h
#=================================================
sub add_casino_action {
	return if $round <= 0;
	if ($now_bet < $max_bet && $m{coin} >= $now_bet) {
		push @actions, ('�Â���');
		$actions{'�Â���'} = sub{ &tsuzukeru };
	}

	push @actions, '�n�C';
	$actions{'�n�C'} = sub{ &high };

	if (@members > 2) {
		push @actions, '���E';
		$actions{'���E'} = sub{ &low };
	}
	
	push @actions, '�����';
	$actions{'�����'}  = sub{ &oriru };
}

#=================================================
# �����o�[�o��
#=================================================
sub member_html {
	my $member_html = '';
	$member_html .= qq|<div style="background: url($bgimg) #333 repeat-x left bottom;"><table><tr>|;
	for my $name (@members) {
		$member_html .= qq|<td onclick="text_set('>$name ')" align="center" valign="bottom"><span style="color: $ms{$name}{color}; font-size: 11px; background-color: #333;">|;
		if ($round < 1) {
			$member_html .= qq|$ms{$name}{action}<br />$cards[$ms{$name}{card}]|;
		}
		else {
			$member_html .= $ms{$name}{action} =~ /�Â���|�ҋ@��/ || $m eq $name ? qq|$ms{$name}{action}| : qq|�H�H�H| if $ms{$name}{action};
			$member_html .= qq|<br />|;
			$member_html .= $ms{$name}{action} =~ /�ҋ@��/ || $m eq $name ? qq|$cards[$ms{$name}{card}]| : qq|�H|;
		}
		$member_html .= qq|<br />$name</span><br /><img src="$icondir/$ms{$name}{icon}" alt="$name" /></td>|;
	}
	$member_html .=  qq|</tr></table></div>|;
	return $member_html;
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
	
	my $max_card = $#cards;
	my @card_nos = (0..$max_card);
	
	# �J�[�h��z��
	for my $name (@members) {
		$ms{$name}{action} = '';
		$ms{$name}{card} = splice(@card_nos, int rand @card_nos, 1);
	}

	++$round;
	$npc_com .= "�Q�[���J�n�I�I";
	&auto_reload;
}

#=================================================
# ���Â���
#=================================================
sub tsuzukeru {
	if ($ms{$m}{action}) {
		$mes = "���łɁu��$ms{$m}{action}�v��錾���Ă��܂�";
		return;
	}

	$ms{$m}{action} = '�Â���';
	&give_coin($now_bet);
	&next_round;
}
#=================================================
# ���n�C�����E
#=================================================
sub high { &_call('�n�C'); }
sub low  { &_call('���E'); }	
sub _call {
	my $call = shift;

	if ($ms{$m}{action}) {
		$mes = "���łɁu��$ms{$m}{action}�v��錾���Ă��܂�";
		return;
	}

	$com =~ s/��(.+?)(\x20|�@)/���H�H�H$2/; # �}�[�N���폜
	$ms{$m}{action} = $call;
	&give_coin($now_bet);
	&next_round;
}

#=================================================
# �������
#=================================================
sub oriru {
	if ($ms{$m}{action}) {
		$mes = "���łɁu��$ms{$m}{action}�v��錾���Ă��܂�";
		return;
	}

	$com =~ s/��(.+?)(\x20|�@)/���H�H�H$2/; # �}�[�N���폜
	$ms{$m}{action} = '�����';
	&give_coin($now_bet);
	&next_round;
}


#=================================================
# �S���̃A�N�V�������`�F�b�N���āA���������̃��E���h��
#=================================================
sub next_round {
	return if $round <= 0;
	my %as = (
		'�n�C'		=> 0,
		'���E'		=> 0,
		'�Â���'	=> 0,
		'�����'	=> 0,
	);

	my $count = 0;
	for my $name (@members) {
		next if $ms{$name}{action} eq '';
		++$as{$ms{$name}{action}};
		++$count;
	}

	if ($count eq @members) { # �S���A�N�V�����ς�
		if ($m{coin} <= 0 || $now_bet >= $max_bet || ($as{'�n�C'} + $as{'���E'}) >= (@members - $as{'�����'}) * 0.5) { # �R�C�����Ȃ��Ȃ��� or �ő僌�[�g or ��������
			&battle;
		}
		else { # ���̃��E���h��
			for my $name (@members) {
				next if $ms{$name}{action} eq '�����';
				next if $ms{$name}{action} eq '�ҋ@��';
				$ms{$name}{action} = '';
			}
			$round++;
			$now_bet += $bet;
			$npc_com.=qq|<span class="lv_up">���Q�[�����s�����[�g���オ��܂����􌻍݂̃��[�g�� <span class="damage">$now_bet</span> ���ł�</span>|;
		}
	}
}


#=================================================
# ����
#=================================================
sub battle {
	# �܋�
	my $get_coin = &get_coin;
	return if $get_coin <= 0;

	# �n�C�̐l�ƃ��E�̐l�̃O���[�v�����ŏ��s
	my $higher   = '';
	my $lowher   = '';
	my $max_card = -1;
	my $min_card = $#cards+1;
	for my $name (@members) {
		if ($ms{$name}{action} eq '�n�C') {
			if ($ms{$name}{card} > $max_card) {
				$higher   = $name;
				$max_card = $ms{$name}{card};
			}
		}
		elsif ($ms{$name}{action} eq '���E') {
			if ($ms{$name}{card} < $min_card) {
				$lower    = $name;
				$min_card = $ms{$name}{card};
			}
		}
	}
	
	my @winners = ($higher, $lower);
	if (@members > 2 && $higher && $lower) { # �Q�l�ȏ� �܋��Q����
		$get_coin = int($get_coin * 0.5);
		@winners = ($higher, $lower);
		$npc_com .= qq|�n�C��錾�����J�[�h�̒��ň�ԋ����J�[�h�́y$cards[$max_card]�z�I����āA<span class="get">���҂� $higher �ɶ��ɺ�� <span class="damage">$get_coin</span> �����������܂�</span>|;
		$npc_com .= qq|<br />���E��錾�����J�[�h�̒��ň�Ԏア�J�[�h�́y$cards[$min_card]�z�I����āA<span class="get">���҂� $lower �ɶ��ɺ�� <span class="damage">$get_coin</span> �����������܂�</span>|;
	}
	elsif ($higher) {
		@winners = ($higher);
		$npc_com .= qq|�n�C��錾�����J�[�h�̒��ň�ԋ����J�[�h�́y$cards[$max_card]�z�I����āA<span class="get">���҂� $higher �ɶ��ɺ�� <span class="damage">$get_coin</span> �����������܂�</span>|;
	}
	elsif ($lower) {
		@winners = ($lower);
		$npc_com .= qq|���E��錾�����J�[�h�̒��ň�Ԏア�J�[�h�́y$cards[$min_card]�z�I����āA<span class="get">���҂� $lower �ɶ��ɺ�� <span class="damage">$get_coin</span> �����������܂�</span>|;
	}
	else {
		$npc_com .= qq|�S������Ă��܂����̂Łc����̃Q�[���͂�����ƂȂ�܂�|;
		&reload_member($winners[0]);
	}
	
	for my $winner (@winners) {
		my $yid = unpack 'H*', $winner;
		if (-f "$userdir/$yid/user.cgi") {
			my %p = &get_you_datas($yid, 1);
			&regist_you_data($winner, 'cas_c', ++$p{cas_c});
			&regist_you_data($winner, 'coin', $p{coin}+$get_coin);
		}
	}

	$round   = 0;
	$now_bet = $bet;
	&reload_member($winners[0]);
}



1; # �폜�s��
