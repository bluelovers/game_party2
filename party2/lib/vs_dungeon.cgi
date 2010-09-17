require "./lib/_battle.cgi";
require "./lib/_npc_action.cgi";
#=================================================
# �`��(VS �����X�^�[) Created by Merino
#=================================================

%map_imgs = (
	0	=> '��', # ��
	1	=> '��', # ��
	'm'	=> '��', # ����
);

@npc_skills = (
	[0,	0,	'��������',		sub{ &kougeki	}],
#	[0,	0,	'�ڂ�����',		sub{ $ms{$m}{tmp} = '�h��'; $com.="$m�͐g���ł߂Ă���";	}],
);

#=================================================
# �^�C�g���A�w�i�摜
#=================================================
sub get_header_data {
	require "$mapdir/$stage/$map.cgi";
	$bgimg = "$bgimgdir/map$stage.gif"; # �w�i�摜
	$d_name ||= $dungeons[$stage];
	$this_title = "$d_name ���E�^�[�� <b>$round</b>/<b>$max_round</b>";
}
#=================================================
# �ǉ��A�N�V����
#=================================================
sub add_battle_action {
	if ($round eq '0') {
		push @actions, '������';
		$actions{'������'} = [0, sub{ &susumu }];
	}
	elsif (@enemys <= 0) {
		push @actions, ('�ɂ�','����','�݂Ȃ�','�Ђ���','����');
		$actions{'�ɂ�'}   = [0,	sub{ &nishi }];
		$actions{'����'}   = [0,	sub{ &kita }];
		$actions{'�݂Ȃ�'} = [0,	sub{ &minami }];
		$actions{'�Ђ���'} = [0,	sub{ &higashi }];
		$actions{'����'}   = [0,	sub{ $m{job} eq '9' || $m{job} eq '26' || $m{job} eq '27' ? &chizu(2) : &chizu(); }];
	}
	elsif ($enemys[0] =~ /^\@.+��.$/) {
		$is_npc_action = 0;
		push @actions, '����ׂ�';
		$actions{'����ׂ�'} = [0,	sub{ &shiraberu }];
	}
}
sub susumu {
	if ($round < 1 && $leader ne $m) {
		$mes = "��Ԏn�߂� �������� �����邱�Ƃ��ł���̂̓��[�_�[�݂̂ł�";
		return;
	}
	&reset_status_all;
	++$round;
	&auto_reload;
}

#=================================================
# ���ɂ����������݂Ȃ݁��Ђ���
#=================================================
sub kita    { &_susumu('�k', $py-1, $px)   }
sub minami  { &_susumu('��', $py+1, $px)   }
sub higashi { &_susumu('��', $py,   $px+1) }
sub nishi   { &_susumu('��', $py,   $px-1) }
sub _susumu {
	my($name, $y, $x) = @_;
	$is_npc_action = 0;
	if (@enemys > 0 && $event ne '��') {
		$mes .= "���G��S�ē|���܂ŁA��ɐi�ނ��Ƃ͂ł��܂���";
		return;
	}
	elsif ($round >= $max_round) {
		$mes .= "���s�����E�l�𒴂��܂����B����ȏ�͓����܂���B���ɂ���ŉ��U���Ă�������";
		return;
	}
	elsif ($y < 0 || $x < 0 || !defined $maps[$y][$x] || $maps[$y][$x] eq '1') {
		my @tekitos = ('����','��o��','��_��','��.��','�~_�~','�~o�~','�~.�~','�P���P;','�P���P;');
		my $face = $tekitos[int rand @tekitos];
		$com .= "$m �͕ǂɂԂ������I$face";
		$ms{$m}{state} = $face;
		&event_1;
		return;
	}
	&reset_status_all;
	++$round;
	$px = $x;
	$py = $y;

	$npc_com .= "$p_name�� $name�ւƐi�݂܂����c";
	&{'event_' .$maps[$py][$px] };
	&chizu();
	&auto_reload;
}

sub event_0 { return if rand(2) > 1; &add_monster(); } # ��
sub event_1 { return } # ��
sub event_S { return } # �X�^�[�g�n�_
sub event_B { return if $event =~ /B/; $event .= 'B'; $npc_com.="�����Ȃ�ʋC�z��������c�B�ǂ����A���̃_���W�����̃{�X�̂悤���I<br />"; &add_boss } # �{�X

#=================================================
# ������
#=================================================
sub chizu {
	my $v = shift || 1;
	$com .= '<br />';
	for my $y (-$v .. $v) {
		for my $x (-$v .. $v) {
			$com .= $y eq '0' && $x eq '0' ? $map_imgs{m} # �����̈ʒu 
				  : $py+$y < 0 || $px+$x < 0 || !defined $maps[$py+$y][$px+$x] ? $map_imgs{1} # Map�ɑ��݂��Ȃ������͕�
				  : !defined $map_imgs{$maps[$py+$y][$px+$x]} eq '1' ? $map_imgs{0} # MapImgs�ɑ��݂��Ȃ������͓�
				  :          $map_imgs{$maps[$py+$y][$px+$x]};
		}
		$com .= '<br />';
	}
}

# ���_���W�����p�̕�̐�
sub _add_treasure {
	&add_treasure();
}

# ���_���W�����p�̓G�̐�
sub _add_monster {
	&add_monster();
}


# �����S�̃��i�_���[�W
sub _trap_d {
	my $d = shift;
	for my $y (@partys) {
		my $v = int($d * (rand(0.3)+0.9));
		$npc_com .= qq|<b>$y</b>�� <span class="damage">$v</span> �̃_���[�W�I|;
		$ms{$y}{hp} -= $v;
		if ($ms{$y}{hp} <= 0) {
			$ms{$y}{hp} = 0;
			$npc_com .= qq!<span class="die">$y�͓|�ꂽ�I</span>!;
		}
	}
}


1; # �폜�s��
