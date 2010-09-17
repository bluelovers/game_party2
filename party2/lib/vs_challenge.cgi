require "./lib/_battle.cgi";
require "./lib/_npc_action.cgi";
#=================================================
# �`�������W���[�h Created by Merino
#=================================================
@npc_skills = (
	[0,	0,	'��������',		sub{ &kougeki	}],
#	[0,	0,	'�ڂ�����',		sub{ $ms{$m}{tmp} = '�h��'; $com.="$m�͐g���ł߂Ă���";	}],
);

#=================================================
# �^�C�g���A�w�i�摜
#=================================================
sub get_header_data {
	$bgimg = "$bgimgdir/challenge$stage.gif";
	$this_title = "$challenges[$stage] Lv.<b>$round</b>";
}
#=================================================
# �ǉ��A�N�V����
#=================================================
sub add_battle_action {
	if (defined $enemys[0] && $enemys[0] =~ /��.$/) {
		$is_npc_action = 0;
		push @actions, '����ׂ�';
		$actions{'����ׂ�'} = [0,	sub{ &shiraberu }];
	}

	return if @enemys;
	push @actions, '������';
	$actions{'������'} = [0,	sub{ &susumu }];
}

#=================================================
# ��������
#=================================================
sub susumu {
	$is_npc_action = 0;
	if (@enemys > 0) {
		$mes .= "���G��S�ē|���܂ŁA����Lv.�ɐi�ނ��Ƃ͂ł��܂���";
		return;
	}
	elsif ($round < 1 && $leader ne $m) {
		$mes = "��Ԏn�߂� �������� �����邱�Ƃ��ł���̂̓��[�_�[�݂̂ł�";
		return;
	}

	&update_record() if $round > $win; # �ō��L�^�𒴂��Ă�����L�^�X�V����
	&reset_status_all;

	++$round;
	$npc_com .= "$p_name�� $challenges[$stage] Lv.$round �ɒ���I<br />";
	&set_monster();
	&auto_reload;
}
# ------------------
# �퓬�����o�[��NPC�����X�^�[��ǉ�����
sub set_monster {
	&error("$challengedir/$stage.cgi�����X�^�[�f�[�^�t�@�C��������܂���") unless -f "$challengedir/$stage.cgi";
	require "$challengedir/$stage.cgi";

	@members = @partys;
	
	if (!$m{is_get} && $round >= $tresure_round && rand(10) < 1) { # ����(���擾�ŁA$tresure_round�ȏ�̊K�ŁA1/10�̊m��)
		&add_treasure();
	}
	else {
		&add_monster(0, 1 + 0.1 * $round );
	}
}

# �L�^�X�V
sub update_record {
	open my $fh, "+< $logdir/challenge$stage.cgi" or &error("$logdir/challenge$stage.cgi�t�@�C�����J���܂���");;
	eval { flock $fh, 2; };
	my $line = <$fh>;
	my($max_round) = (split /<>/, $line)[0];

	if ($round > $max_round) { # �����ōX�V����Ă���ꍇ������̂ōĊm�F
		my @lines = ("$round<>$date<>$p_name<>$ms{$m}{color}<>\n");
		for my $y (@partys) { # �L�^�\���Ɏg�������f�[�^��������
			my $icon = $ms{$y}{hp} <= 0 ? 'chr/099.gif' : $ms{$y}{icon};
			push @lines, "$y<>$icon<>$ms{$y}{job}<>$ms{$y}{old_job}<>$ms{$y}{hp}<>$ms{$y}{mp}<>$ms{$y}{at}<>$ms{$y}{df}<>$ms{$y}{ag}<>\n";
		}
		
		$win = $round;
		$npc_com .= qq|<span class="lv_up">$challenges[$stage]�̋L�^���X�V���܂����I�yLv.<b>$round</b>�N���A�z</span><br />|;
		seek $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
	}
	close $fh;
}


1; # �폜�s��
