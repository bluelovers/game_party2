my @orbs = split //, $m{orb};
#=================================================
# �����̍Ւd Created by Merino
#=================================================
# �ꏊ��
$this_title = "�����̍Ւd";

# NPC��
$npc_name   = '@�ޏ�';

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$logdir/reborn";

# �w�i�摜
$bgimg   = "$bgimgdir/reborn.gif";

# 
@sales = (66..69);

# �I�[�u�̃t�H���g�J���[
%colors = (
	'G' => 'gold',
	's' => 'silver',
	'r' => 'red',
	'b' => 'blue',
	'g' => 'green',
	'y' => 'yellow',
	'p' => 'purple',
);



#=================================================
# �͂Ȃ����t
#=================================================
if (@orbs >= 6) {
	@words = (
		"���B�B���B�B���̓����ǂ�ȂɁB���̓����ǂ�ȂɁB�҂���т����Ƃł��傤",
		"�����A�F��܂��傤�B�����A�F��܂��傤",
	);
}
else {
	@words = (
		"���B�́B���B�́B��������Ă��܂��B��������Ă��܂�",
		"���E���ɂ���΂�U�̃I�[�u�����������Ƃ�....",
		"�`���̕s�������[�~�@�͂�݂�����܂��傤",
		"��ɓ������I�[�u�͗j���ɂ���ĕς��悤�ł�",
	);
}


if ($m{orb} =~ /G/) {
	# �ǉ��A�N�V����
	push @actions, '�˂���';
	$actions{ '�˂���' } = sub{ &negau };
	
	@words = (
		"���̃A�C�e����`�����Ɏg���΁A���܂Ō������Ƃ̂Ȃ����E�ւƍs�����Ƃ��ł��܂�",
		"���m�̐��E�ɘA��čs�����Ƃ��ł���̂́A�A�C�e�����g������񂾂��ł�",
		"���m�̐��E�ɂւ́A���̏�ɂ������Ԃƈꏏ�ɍs�����Ƃ��ł��܂�",
	);
}
else {
	# �ǉ��A�N�V����
	push @actions, '���̂�';
	$actions{ '���̂�' } = sub{ &inoru };
}

#=================================================
# �X�e�[�^�X�\��
#=================================================
sub header_html {
	my $orbs = '';
	for my $orb (@orbs) {
		$orbs .= qq|<font color="$colors{$orb}">��</font>|;
	}
	print qq|<div class="mes">�y$this_title�z$orbs</div>|;
}

#=================================================
# �����̂�
#=================================================
sub inoru {
	if (@orbs < 6) {
		$mes = "�I�[�u������܂���B�I�[�u������܂���B�I�[�u���U�W�߂Ă�������";
	}
	elsif (@orbs >= 6) {
		my $r_time = $time + 1800;
		open my $fh, ">> ${this_file}_member.cgi" or &error("${this_file}_member.cgi�t�@�C�����J���܂���");
		print $fh "$r_time<>0<>װЧ@<>0<>chr/051.gif<>$npc_color<>\n";
		close $fh;
		$npc_com .= "���͗������B�������ڊo�߂鎞�B���͂��O�̂��́B�����オ��󍂂��I";
		$m{orb} = 'G';
	}
}


#=================================================
# ���˂���
#=================================================
sub negau {
	return if $m{orb} !~ /G/;
	
	my $target = shift;
	
	my $p = qq|<table class="table1">|;
	for my $i (@sales) {
		if ($ites[$i][1] eq $target) {
			if ($m{ite}) {
				&send_item($m, 3, $i);
				$npc_com = "$ites[$i][1] ��$m�̗a���菊�ɑ����Ă����܂����B�`�����Ɏg�����ƂŖ��m�̐��E�ւƍs�����Ƃ��ł���ł��傤";
			}
			else {
				$m{ite} = $i;
				$npc_com = "$ites[$i][1] �ł��ˁB�`�����Ɏg�����ƂŖ��m�̐��E�ւƍs�����Ƃ��ł���ł��傤";
				require "./lib/_add_collection.cgi";
				&add_collection;
			}
			$m{orb} = '';
			return;
		}
		$p .= qq|<tr onclick="text_set('���˂���>$ites[$i][1] ')"><td>$ites[$i][1]</td></tr>|;
	}
	$p  .= qq|</table>|;

	$mes = qq|װЧ�u�ӂށB$m�Ƃ����̂��c�B�����݂����点�Ă��ꂽ��Ƃ��āA<br />�킪�͂��h�����A�C�e�����P�����������悤�c�v<br />$p|;
	$act_time = 0;
}


1; # �폜�s��
