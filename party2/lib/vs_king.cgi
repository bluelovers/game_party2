require "./lib/_battle.cgi";
require "./lib/_npc_action.cgi";
#=================================================
# ����� Created by Merino
#=================================================

@npc_skills = (
	[0,	0,	'��������',		sub{ &kougeki	}],
	[0,	0,	'�f�W����',		sub{ &dejon		}],
);

#=================================================
# �^�C�g���A�w�i�摜
#=================================================
sub get_header_data {
	$bgimg = "$bgimgdir/stage19.gif";
	$this_title = "$p_name";
}
#=================================================
# �ǉ��A�N�V����
#=================================================
sub add_battle_action {
	if ($round eq '2') {
		$is_npc_action = 0;
		push @actions, '����ׂ�';
		$actions{'����ׂ�'} = [0,	sub{ &shiraberu }];
	}
	elsif (@enemys <= 0) {
		push @actions, '�ӂ�����';
		$actions{'�ӂ�����'} = [0,	sub{ &fuuin }];
	}
}

#=================================================
# ���ӂ�����
#=================================================
sub fuuin {
	return if @enemys;
	$is_npc_action = 0;
	if (@enemys > 0) {
		$mes .= "���S�Ă̓G��|���Ȃ��ƕ��󂷂邱�Ƃ͂ł��܂���";
		return;
	}
	elsif ($round >= 2) {
		$mes .= "���łɕ���ς݂ł��B���ɂ���ŉ��U���Ă�������<br />";
		return;
	}
	
	++$round;

	&error("$stagedir/$stage.cgi�����X�^�[�f�[�^�t�@�C��������܂���") unless -f "$stagedir/$stage.cgi";
	require "$stagedir/$stage.cgi";
	
	$npc_com .= "$p_name���Ăѕ��󂷂邱�Ƃɐ������܂����I�C�x���g�L��ŏj���J�Â���܂��I<br />";
	my $hero_name = join "�A", @partys;
	&write_news(qq|<span class="tenshon">�E��$hero_name��$p_name�𕕈󂷂�</span>|);

	for my $name (@partys) {
		next if $name =~ /^@/;
		my %p = &get_you_datas($name);
		&regist_you_data($name, 'hero_c', $p{hero_c}+1);
	}

	&add_treasure();

	# �C�x���g�L��ŏj���̐l������ǉ�
	require "./lib/_win_vs_king.cgi";
}

#=============================
# ���f�W���� ���ꂽ�l�������ޏ�
#=============================
sub dejon {
	my @new_members;
	for my $name (@members) {
		if ($ms{$name}{hp} <= 0) {
			my $yid = unpack 'H*', $name;
			if (-f "$userdir/$yid/user.cgi") {
				my %p = &get_you_datas($yid, 1);
				&regist_you_data($name, 'lib', '');
				&regist_you_data($name, 'tired', $p{tired}+30);
			}
			$ms{$name}{color} = $npc_color;
			$com.="$name���ً�ԂւƋz�����܂ꂽ�I";
		}
		else {
			push @new_members, $name;
		}
	}
	@members = @new_members;
}


1; # �폜�s��
