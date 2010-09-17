#=================================================
# �𗬍L�� Created by Merino
#=================================================
# �ꏊ��
$this_title = '�Ŏs��';

# NPC��
$npc_name   = '@�ŏ��l';

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$logdir/black_market";

# �w�i�摜
$bgimg   = "$bgimgdir/black_market.gif";

# ���A�A�C�e��
@rare_items = (
[29,30,33..40],
[35..40],
[28,29,40,57..71,87,104..107,109],
);


# �����Ώ�
@prizes = (
# [����No, ���A�|�C���g],
[87, 1],
[57, 4],
[60, 2],
[61, 2],
[62, 2],
[63, 2],
[64, 2],
[65, 2],
);

#=================================================
# �͂Ȃ����t
#=================================================
@words = (
	"�悭�����ȁc�B�����͈Ŏs�ꂾ�c",
	"�\\�̐��E�ł͎�ɓ�����Ȃ�����������Ă���c",
	"���̎���͋��ł͔����Ȃ����́c�B�܂�A���c��ί��ί�c�ł͂Ȃ��A���A�A�C�e�����c",
	"���O�̍��c�ł͂Ȃ��A���O���������Ă��郌�A�A�C�e������������c",
	"���A�A�C�e�����������邱�Ƃɂ���āc���O�̃��A�|�C���g��������c",
	"���A�|�C���g�ɂ�����ł���A�C�e�����Ⴄ�c",
);

#=================================================
# ������ׂ�>NPC
#=================================================
sub shiraberu_npc {
	$mes = "�c���O�̍��Ŏ���������̂��H";
}

#=================================================
# �ǉ��A�N�V����
#=================================================
push @actions, '��������';
push @actions, '�Ƃ�Ђ�';
$actions{'��������'} = sub{ &sasageru }; 
$actions{'�Ƃ�Ђ�'} = sub{ &torihiki }; 


#=================================================
# �X�e�[�^�X�\��
#=================================================
sub header_html {
	print qq!<div class="mes">�y$this_title�z ���A�|�C���g <b>$m{rare}</b>�|�C���g!;
	print qq| E�F$weas[$m{wea}][1]| if $m{wea};
	print qq| E�F$arms[$m{arm}][1]| if $m{arm};
	print qq| E�F$ites[$m{ite}][1]| if $m{ite};
	print qq|</div>|;
}

#=================================================
# ���Ƃ�Ђ�
#=================================================
sub torihiki {
	my $target = shift;
	
	my $p = qq|<table class="table1"><tr><th>���i</th><th>ڱ�߲��</th></tr>|;
	for my $i (0 .. $#prizes) {
		if ($ites[ $prizes[$i][0] ][1] eq $target) {
			if ($m{rare} >= $prizes[$i][1]) {
				&send_item($m, 3, $prizes[$i][0]);
				$npc_com = "����������c�B$ites[ $prizes[$i][0] ][1] �͂��O�̗a���菊�ɑ����Ă������c";
				$m{rare} -= $prizes[$i][1];
			}
			else {
				$mes = "���A�|�C���g�s�����c";
			}
			return;
		}
	
		$p .= qq|<tr onclick="text_set('���Ƃ�Ђ�>$ites[ $prizes[$i][0] ][1] ')"><td>$ites[ $prizes[$i][0] ][1]</td><td align="right">$prizes[$i][1] Pt</td></tr>|;
	}
	$p  .= qq|</table>|;
	$mes = qq|�ǂ�Ǝ������񂾁c�H<br />$p|;
	$act_time = 0;
}



#=================================================
# ����������
#=================================================
sub sasageru {
	my $target = shift;

	unless ($target) {
		$mes .= qq|<span onclick="text_set('����������>$weas[$m{wea}][1] ')">$weas[$m{wea}][1]</span> / | if $m{wea};
		$mes .= qq|<span onclick="text_set('����������>$arms[$m{arm}][1] ')">$arms[$m{arm}][1]</span> / | if $m{arm};
		$mes .= qq|<span onclick="text_set('����������>$ites[$m{ite}][1] ')">$ites[$m{ite}][1]</span> / | if $m{ite};
		$mes = '����������̂𑕔����ė����c' unless $mes;
		return;
	}
	
	if ($weas[$m{wea}][1] eq $target) {
		for my $rare_item (@{ $rare_items[0] }) {
			if ($m{wea} eq $rare_item) {
				$m{wea} = 0;
				$npc_com.="�c$target�c���c�B���A���ȁc�B�������낤�c�B���O�̃��A�|�C���g�����Z���Ă������c";
				$m{rare} += 1;
				return;
			}
		}
		$npc_com.="�c$target�c���c�B�_�����ȁc�B���̃A�C�e���́c�߂��炵���Ȃ��c";
	}
	elsif ($arms[$m{arm}][1] eq $target) {
		for my $rare_item (@{ $rare_items[1] }) {
			if ($m{arm} eq $rare_item) {
				$m{arm} = 0;
				$npc_com.="�c$target�c���c�B���A���ȁc�B�������낤�c�B���O�̃��A�|�C���g�����Z���Ă������c";
				$m{rare} += 1;
				return;
			}
		}
		$npc_com.="�c$target�c���c�B�_�����ȁc�B���̃A�C�e���́c�߂��炵���Ȃ��c";
	}
	elsif ($ites[$m{ite}][1] eq $target) {
		for my $rare_item (@{ $rare_items[2] }) {
			if ($m{ite} eq $rare_item) {
				$m{ite} = 0;
				$npc_com.="�c$target�c���c�B���A���ȁc�B�������낤�c�B���O�̃��A�|�C���g�����Z���Ă������c";
				$m{rare} += 1;
				return;
			}
		}
		$npc_com.="�c$target�c���c�B�_�����ȁc�B���̃A�C�e���́c�߂��炵���Ȃ��c";
	}
	else {
		$mes = '����������̂𑕔����ė����c';
	}
}




1; # �폜�s��
