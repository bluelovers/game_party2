#=================================================
# �C�x���g�L�� Created by Merino
# �v���C���[���ɂ�菤�l�o��
#=================================================
# �ꏊ��
$this_title = '�C�x���g�L��';

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$logdir/event";

# �w�i�摜
$bgimg = "$bgimgdir/event.gif";


sub _get_count {
	open my $fh, "< ${this_file}_member.cgi" or &error("${this_file}_member.cgi�t�@�C�����ǂݍ��߂܂���");
	my @lines = <$fh>;
	close $fh;
	
	my $count = @lines;
	return $count;
}

my $c_member = &_get_count;

if ($c_member < 10) { # 10�l�����Ȃ�C�x���g�N���炸
	return 1;
}
elsif ($c_member >= 30) {
	# �����Ă��铹��(No)
	@sales = (90..100,108);
	$bgimg = "$bgimgdir/event3.gif";
}
elsif ($c_member >= 20) {
	# �����Ă��铹��(No)
	@sales = (73,74,77,5,75,85);
	$bgimg = "$bgimgdir/event2.gif";
}
else {
	# �����Ă��铹��(No)
	@sales = (72,81,82,83,84,86);
	$bgimg = "$bgimgdir/event1.gif";
}

$npc_name = '@���̏��l';
sub _add_akindo {
	open my $fh, ">> ${this_file}_member.cgi" or &error("${this_file}_member.cgi�t�@�C�����J���܂���");
	print $fh "$time<>0<>@���̏��l<>0<>chr/024.gif<>$npc_color<>\n";
	close $fh;
}

&_add_akindo;

#=================================================
# �͂Ȃ����t
#=================================================
@words = (
	"����A��������̐l���W�܂��ĉ��������ł����H",
	"�o�U�[�ł�����ł����˂�",
	"��������l�����āA�ɂ��₩�ł���",
	"�ł́A�����ł������Ă��炢�܂��傤��",
);

#=================================================
# ������ׂ�>NPC
#=================================================
sub shiraberu_npc {
	$mes = "�Ȃ�ƁA�򑐂��������I�c���l�̕��𓐂��Ă͂����Ȃ��c";
}

#=================================================
# �ǉ��A�N�V����
#=================================================
push @actions, ('����');
$actions{'����'} = sub{ &kau }; 

#=================================================
# ������
#=================================================
sub kau {
	my $target = shift;
	
	my $p = qq|<table class="table1"><tr><th>���O</th><th>�l�i</th></tr>|;
	for my $i (@sales) {
		$ites[$i][2] *= 3; # ���ʂȂ̂�3�{�̒l�i
		if ($ites[$i][1] eq $target) {
			if ($m{money} >= $ites[$i][2]) {
				if ($m{ite}) {
					&send_item($m, 3, $i);
					$npc_com = "$ites[$i][1]��$m����̗a���菊�ɑ����Ă����܂�����";
				}
				else {
					$m{ite} = $i;
					$npc_com = "�͂��A$ites[$i][1]�ł�";
					require "./lib/_add_collection.cgi";
					&add_collection;
				}
				$m{money} -= $ites[$i][2];
			}
			else {
				$mes = "����������Ȃ��悤�ł����c";
			}
			return;
		}
		$p .= qq|<tr onclick="text_set('������>$ites[$i][1] ')"><td>$ites[$i][1]</td><td align="right">$ites[$i][2] G</td></tr>|;
	}
	$p  .= qq|</table>|;
	$mes = qq|�ł͏����������Ă��炢�܂��傤<br />$p|;
	$act_time = 0;
}



1; # �폜�s��
