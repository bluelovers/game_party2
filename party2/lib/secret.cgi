#=================================================
# �閧�̓X Created by Merino
#=================================================
# �ꏊ��
$this_title = '�閧�̓X';

# NPC��
$npc_name = '@��¼�';

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$logdir/secret";

# �w�i�摜
$bgimg = "$bgimgdir/item.gif";

# �����Ă��铹��(No)
@sales = (10,15,80,78,43,27,30,31);


#=================================================
# �͂Ȃ����t
#=================================================
@words = (
	"�o������������F�`�B���̐l�ɂ͔閧�����F�`�B",
	"�l�i�͍������F�`����ǁA���ł͎�ɓ���Ȃ����A���̂����F�`�B",
	"���F�`���F�`���F�`���F�`���F�`���F�`���F�`���F�`���F�`�B",
	"�x�F�`�x�F�`�x�F�`�x�F�`�x�F�`�x�F�`�x�F�`�x�F�`�x�F�`�B",
	"���ςӂςӂ̓T�[�r�X�����F�`�B",
);

sub shiraberu_npc {
	$mes = "$npc_name�u�I�C���͗r��$npc_name�����F�`�B�r�̍����痈����c�S�z�b�S�z�b�c�r�̍����痈�����F�`�v";
}

#=================================================
# �ǉ��A�N�V����
#=================================================
push @actions, '����';
push @actions, '�ςӂς�';
$actions{'����'} = sub{ &kau }; 
$actions{'�ςӂς�'} = sub{ &pafupafu }; 

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
					$npc_com = "$ites[$i][1]��$m���F�`�̗a���菊�̕��ɓ����܂������F�`";
				}
				else {
					$m{ite} = $i;
					$npc_com = "$ites[$i][1]���F�`�B�����Ă����F�`";
					require "./lib/_add_collection.cgi";
					&add_collection;
				}
				$m{money} -= $ites[$i][2];
			}
			else {
				$mes = "���������烁�F�`";
			}
			return;
		}
		$p .= qq|<tr onclick="text_set('������>$ites[$i][1] ')"><td>$ites[$i][1]</td><td align="right">$ites[$i][2] G</td></tr>|;
	}
	$p  .= qq|</table>|;
	$mes = qq|�ǂ�𔃂����F�`�H<br />$p|;
	$act_time = 0;
}

sub pafupafu {
	$to_name  = $m;
	$npc_com  = qq|�p�t�p�t<font color="#FFB6C1">&hearts;</font> �p�t�p�t<font color="#FFB6C1">&hearts;</font> �p�t�p�t<font color="#FFB6C1">&hearts;</font>�c�c�c|;
	$npc_com .= qq|�ǂ��� $m �킵�̃p�t�p�t�͋C�����������낤|;
}


1; # �폜�s��
