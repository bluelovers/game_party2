#=================================================
# �h� Created by Merino
#=================================================
# �ꏊ��
$this_title = '�h�';

# NPC��
$npc_name = '@���';

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$logdir/armor";

# �w�i�摜
$bgimg = "$bgimgdir/armor.gif";

# �����Ă���h��(No)
@sales = $m{job_lv} > 11 ? (1..16) : (1..5+$m{job_lv});


#=================================================
# �͂Ȃ����t
#=================================================
@words = (
	"�����͖h��b�X�I�h��𑕔�����΃_���[�W�����炷���Ƃ��ł���b�X�I",
	"$e2j{ag}���Ȃ��ƍU�������킷���Ƃ��ł��Ȃ��b�X�I",
	"$e2j{ag}�Ɏ��M���Ȃ��ꍇ�́A�X�e�e�R�p���c���I�X�X���b�X�I",
	"������d���͂P��̐퓬���Ƃŕς��b�X�I",
	"$m�����$arms[$sales[int(rand(@sales))]][1]�Ȃ�Ď����������b�X�ˁI",
	"�d���Z�ŃK�`�K�`�Ɍł߂邩�A�q���q���̕��ŉ�𗦂��グ��̂��A�ǂ��炪�D���b�X���H",
	"���������������ԂȂ������𒅂�̂����b�X",
	"$m����̓]�E�񐔂�$m{job_lv}��b�X�ˁI�]�E�񐔂������Ən���҂ƌ��Ȃ�����镨��������b�X�I",
	"$m�����$e2j{df}��$m{df}�b�X�ˁI�B�Ȃ��Ȃ��̌ł��b�X�ˁI",
);

sub shiraberu_npc {
	$mes = "$npc_name�u�ȁA�ȁA�������Ă���b�X���I�H�v";
}

#=================================================
# �ǉ��A�N�V����
#=================================================
push @actions, ('����', '����');
$actions{'����'} = sub{ &kau }; 
$actions{'����'} = sub{ &uru }; 


#=================================================
# ������
#=================================================
sub kau {
	my $target = shift;
	
	my $p = qq|<table class="table1"><tr><th>���O</th><th>�l�i</th><th>����</th><th>�d��</th></tr>|;
	for my $i (@sales) {
		if ($arms[$i][1] eq $target) {
			if ($m{money} >= $arms[$i][2]) {
				if ($m{arm}) {
					&send_item($m, 2, $i);
					$npc_com = "�������グ���肪�Ƃ��b�X�I$arms[$i][1]��$m����̗a���菊�ɑ����Ă������b�X�I";
				}
				else {
					$m{arm} = $i;
					$npc_com = "�������グ���肪�Ƃ��b�X�I$arms[$i][1]�ǂ������Ă��������b�X";
					require "./lib/_add_collection.cgi";
					&add_collection;
				}
				$m{money} -= $arms[$i][2];
			}
			else {
				$mes = "�c�O�Ȃ���A����������Ȃ��b�X";
			}
			return;
		}
		$p .= qq|<tr onclick="text_set('������>$arms[$i][1] ')"><td>$arms[$i][1]</td><td align="right">$arms[$i][2] G</td><td align="right">$arms[$i][3]</td><td align="right">$arms[$i][4]</td></tr>|;
	}
	$p  .= qq|</table>|;
	$mes = qq|�ǂ�𔃂��b�X���H<br />$p|;
	$act_time = 0;
}

#=================================================
# ������
#=================================================
sub uru {
	my $target = shift;
	
	unless ($m{arm}) {
		$mes = "���肽���h�����ꍇ�́A�������Ă��ė~�����b�X�I";
		return;
	}
	
	# ������z
	my $buy_price = int($arms[$m{arm}][2] * 0.5);
	
	if ($arms[$m{arm}][1] eq $target) {
		$npc_com = "$arms[$m{arm}][1] �̔����� $buy_price G�b�X�I";
		$m{money} += $buy_price;
		$m{arm} = 0;
		return;
	}

	$mes = qq|<span onclick="text_set('������>$arms[$m{arm}][1] ')">$arms[$m{arm}][1]�Ȃ� $buy_price G�Ŕ������b�X�I</span>|;
	$act_time = 0;
}


1; # �폜�s��
