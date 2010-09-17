require "./lib/_casino.cgi";
#=================================================
# �C���f�B�A���|�[�J�[ Created by Merino
#=================================================

@cards = ('�`','�Q','�R','�S','�T','�U','�V','�W','�X','10','�i','�p','�j');

#=================================================
# �퓬�p�A�N�V�����Z�b�g(�v���C���[�p)
#=================================================
sub add_casino_action {
	return if $round <= 0;
	push @actions, ('�Â���','���傤��','�����',);
	$actions{'�Â���'} = sub{ &tsuzukeru };
	$actions{'���傤��'} = sub{ &shoubu };
	$actions{'�����'}   = sub{ &oriru };
}

#=================================================
# �����o�[�o��
#=================================================
sub member_html {
	my $member_html = '';
	$member_html .= qq|<div style="background: url($bgimg) #333 repeat-x left bottom;"><table><tr>|;
	for my $name (@members) {
		$member_html .= qq|<td onclick="text_set('>$name ')" align="center" valign="bottom"><span style="color: $ms{$name}{color}; font-size: 11px; background-color: #333;">|;
		$member_html .= qq|$ms{$name}{action}| if $ms{$name}{action};
		$member_html .= $m ne $name || $ms{$name}{action} =~ /^�����|�ҋ@��/ ? qq|<br />$cards[$ms{$name}{card}]<br />| : qq|<br />�H<br />|;
		$member_html .= qq|$name</span><br />|;
		$member_html .= $ms{$name}{action} =~ /^�����|�ҋ@��/ ? qq|<img src="$icondir/chr/099.gif" alt="$name" /></td>| : qq|<img src="$icondir/$ms{$name}{icon}" alt="$name" /></td>|;
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
	$npc_com .= "�C���f�B�A�`���|�J�[�I�I�J�n�I";
	&auto_reload;
}

#=================================================
# �����傤��
#=================================================
sub shoubu {
	if ($ms{$m}{action}) {
		$mes = "���łɁu��$ms{$m}{action}�v��錾���Ă��܂�";
		return;
	}
	$ms{$m}{action} = '���傤��';
	&give_coin($now_bet);
	&next_round;
}
#=================================================
# ���Â���
#=================================================
sub tsuzukeru {
	if ($ms{$m}{action}) {
		$mes = "���łɁu��$ms{$m}{action}�v��錾���Ă��܂�";
		return;
	}
	elsif ($m{coin} < $now_bet) { # ��݂�����Ȃ��ꍇ�͋�������
		&shoubu;
	}
	else {
		$ms{$m}{action} = '�Â���';
		&give_coin($now_bet);
		&next_round;
	}
}

#=================================================
# �������
#=================================================
sub oriru {
	if ($ms{$m}{action}) {
		$mes = "���łɁu��$ms{$m}{action}�v��錾���Ă��܂�";
		return;
	}
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
		'���傤��' => 0,
		'�Â���' => 0,
		'�����'   => 0,
	);

	my $count = 0;
	for my $name (@members) {
		next if $ms{$name}{action} eq '';
		++$as{$ms{$name}{action}};
		++$count;
	}

	if ($as{'�����'} eq @members-1) { # �P�l�ȊO�S������
		&battle;
	}
	elsif ($count eq @members) { # �S���A�N�V�����ς�
		if ($m{coin} <= 0 || $now_bet >= $max_bet || $as{'���傤��'} >= (@members - $as{'�����'}) * 0.5) { # �R�C�����Ȃ��Ȃ��� or �ő僌�[�g or �S������
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

	my $winner = '';
	my $max_card = -1;
	for my $name (@members) {
		next if $ms{$name}{action} eq '�����'; # ����Ă���l�̓X���[
		next if $ms{$name}{action} eq '�ҋ@��'; # �ҋ@���̐l�̓X���[
		if ($ms{$name}{card} > $max_card) {
			$winner = $name;
			$max_card = $ms{$name}{card};
		}
	}

	if ($winner) {
		my %p = &get_you_datas($winner);
		&regist_you_data($winner, 'cas_c', ++$p{cas_c});
		&regist_you_data($winner, 'coin', $p{coin}+$get_coin);
		$npc_com .= qq|�����I�c<span class="get">���҂� $winner ����ł��� ���ɺ�� <span class="damage">$get_coin</span> �����������܂�</span>|;
	}
	else { # �����ҒE��
		$npc_com .= qq|���҂͂��܂���ł����c|;
	}

	$round   = 0;
	$now_bet = $bet;
	&reload_member($winner);
}




1; # �폜�s��
