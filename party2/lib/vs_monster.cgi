require "./lib/_battle.cgi";
require "./lib/_npc_action.cgi";
#=================================================
# �`��(VS �����X�^�[) Created by Merino
#=================================================

# �{�X��̊K��(+1 ���󕔉��ƂȂ�)
$boss_round = 10;


@npc_skills = (
	[0,	0,	'��������',		sub{ &kougeki	}],
#	[0,	0,	'�ڂ�����',		sub{ $ms{$m}{tmp} = '�h��'; $com.="$m�͐g���ł߂Ă���";	}],
);

#=================================================
# �^�C�g���A�w�i�摜
#=================================================
sub get_header_data {
	$bgimg = "$bgimgdir/stage$stage.gif";
	$this_title = "$stages[$stage] <b>$round</b>�K";
}
#=================================================
# �ǉ��A�N�V����
#=================================================
sub add_battle_action {
	if ($round eq $boss_round+1) {
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
		$mes .= "���G��S�ē|���܂ŁA���̊K�ɐi�ނ��Ƃ͂ł��܂���";
		return;
	}
	elsif ($round < 1 && $leader ne $m) {
		$mes = "��Ԏn�߂� �������� �����邱�Ƃ��ł���̂̓��[�_�[�݂̂ł�";
		return;
	}
	elsif ($round >= $boss_round+1) {
		$mes .= "���N�G�X�g�͏I�����܂����B���ɂ���ŉ��U���Ă�������";
		return;
	}
	
	&reset_status_all;

	++$round;
	$npc_com .= "$p_name�� $stages[$stage] �̉��ւƐi�݂܂����c<br />";
	&set_monster();
	&auto_reload;
}
# ------------------
# �퓬�����o�[��NPC�����X�^�[��ǉ�����
sub set_monster {
	&error("$stagedir/$stage.cgi�����X�^�[�f�[�^�t�@�C��������܂���") unless -f "$stagedir/$stage.cgi";
	require "$stagedir/$stage.cgi";

	@members = @partys;
	
	if ($round eq $boss_round+1) { # ����(�f�t�H���g11�K)
		my $count = $stage eq '17' || $stage eq '20' || $stage eq '21' ? ($#partys+1) * 3 : $#partys;
		++$count if $m{job} eq '7'; # ���l�̏ꍇ+1
		&add_treasure($count);
		&make_vs_king if $stage eq '19';
	}
	elsif ($round eq $boss_round) { # �{�X��(�f�t�H���g10�K)
		&add_boss();
	}
	else {
		&add_monster();
	}
}
# ------------------
# �����쐬
sub make_vs_king {
	opendir my $dh, $stagedir or &error("$stagedir�f�B���N�g�����J���܂���");
	while (my $file_name = readdir $dh) {
		next if $file_name =~ /^\./;
		next if $file_name !~ /^king/;
		my($k_stage) = ($file_name =~ /^(.+)\.cgi$/);
		
		require "$stagedir/$file_name";
		my $quest_id = unpack 'H*', $k{p_name};
		next if -d "$questdir/$quest_id"; # �����N�G�X�g�����������ꍇ�͍��Ȃ�(���Ȃ�)

		$k{p_join}++; # �{�X��1�l����L���Ă��邽��
		my $boss_name = '@'.$k{p_leader};

		# �V�K�p�[�e�B�[�쐬
		mkdir "$questdir/$quest_id" or &error("$questdir/$quest_id�f�B���N�g�����쐬�ł��܂���");
		open my $fh, "> $questdir/$quest_id/member.cgi" or &error("$questdir/$quest_id/member.cgi�t�@�C�����쐬�ł��܂���");
		print $fh "$k{speed}<>$k_stage<>1<>$boss_name<>$k{p_name}<><>$k{p_join}<>0<>0<>1<>$k{need_join}<>6<><>0<>0<><>\n";
		
		my @lines = ();
		for my $no (0 .. $#bosses) {
			my %p = ();
			
			# �����f�[�^�Z�b�g(�ǂݍ��񂾃f�[�^�ɂ��łɒl������ꍇ�͂�������D��)
			$bosses[$no]{tmp}   ||= '';
			$bosses[$no]{state} ||= '';
			$bosses[$no]{hit}   ||= 95;
			$bosses[$no]{ten}   ||= 1;
			$bosses[$no]{name}  = '@'.$bosses[$no]{name};
			$bosses[$no]{color} = $npc_color;
			for my $k (qw/hp mp at df ag/) {
				$bosses[$no]{$k}       = $bosses[$no]{$k};
				$bosses[$no]{'m'.$k} ||= $bosses[$no]{$k};
			}
			
			my $line = '';
			for my $k (@battle_datas) {
				$line .= defined $bosses[$no]{$k} ? "$bosses[$no]{$k}<>" : "0<>";
			}
			push @lines, "$line\n";
		}

		print $fh @lines;
		close $fh;
		chmod $chmod, "$questdir/$quest_id/member.cgi";
		
		open my $fh2, "> $questdir/$quest_id/log.cgi" or &error("$questdir/$quest_id/log.cgi�t�@�C�����쐬�ł��܂���");
		close $fh2;
		chmod $chmod, "$questdir/$quest_id/log.cgi";
	}
	closedir $dh;
	
	for my $name (@partys) {
		next if $name =~ /^@/;
		my %p = &get_you_datas($name);
		&regist_you_data($name, 'mao_c', $p{mao_c}+1);
	}
	
	my $hero_name = join "�A", @partys;
	&write_news(qq|<span class="die">$p_name($hero_name) �ɂ���ĕ��󂳂ꂵ�ҒB�̕��󂪉�����܂����I</span>|);
	$npc_com .= "<br />$leader�����́A�����Ȃ�ʕ��͋C���������c�B�Ȃ�ƁI���E���������������A���E�͐^�����Ȉłɂ������Ă��܂����I";
}



1; # �폜�s��
