#=================================================
# ���퉮 Created by Merino
#=================================================
# �ꏊ��
$this_title = '�J�W�m';

# NPC��
$npc_name = '@��ư';

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$logdir/casino_slot";

# �w�i�摜
$bgimg = "$bgimgdir/casino.gif";


# �������X�g
my @prizes = (
# ��� 1=����,2=�h��,3=���� 
#*�����͕K�v�����Ŕ��f���Ă���̂ŁA���������������̓_��
#  [0]*�K�v����,[1]���,[2]No
	[0,			0,		0,	],
	[100,		3,		4,	],
	[300,		3,		12,	],
	[700,		3,		6,	],
	[2000,		3,		32,	],
	[4000,		3,		38,	],
	[5000,		3,		39,	],
	[8000,		2,		34,	],
	[30000,		1,		31,	],
	[70000,		1,		40,	],
	[80000,		1,		38,	],
);

#=================================================
# �w�b�_�[�\��
#=================================================
sub header_html {
	print qq|<div class="mes">�y$this_title�z �R�C��<b>$m{coin}</b>�� / �S�[���h<b>$m{money}</b>G</div>|;
}


#=================================================
# �͂Ȃ����t
#=================================================
@words = (
	"�R�C���͂P��20G�ł���",
	"�S�[���h���R�C���ɗ��ւ��Ăˁ�",
	"�ܕi�͑��ł͂Ȃ��Ȃ���ɓ���邱�Ƃ��ł��Ȃ����A�ȃA�C�e���΂���恙",
	"�X���b�g�̊G�����R���낦��ƃR�C���������čK���ɂȂ���恙",
	"������肵�Ă����Ăˁ�",
);

sub shiraberu_npc {
	$mes = "$npc_name�u���႟�b���G�b�`�B�`���v";
}

#=================================================
# �ǉ��A�N�V����
#=================================================
push @actions, ('��1�������', '��10�������', '��50�������','��100�������', '��������', '��傤����',);
$actions{'��1�������'}   = sub{ &slot_1   }; 
$actions{'��10�������'}  = sub{ &slot_10  }; 
$actions{'��50�������'}  = sub{ &slot_50  }; 
$actions{'��100�������'} = sub{ &slot_100 }; 
$actions{'��������'}      = sub{ &koukan  }; 
$actions{'��傤����'}    = sub{ &ryougae }; 

#=================================================
# ���������
#=================================================
sub slot_1   { &_slot(1) }
sub slot_10  { &_slot(10) }
sub slot_50  { &_slot(50) }
sub slot_100 { &_slot(100) }
sub _slot {
	my $bet = shift;
	
	if ($m{tired} >= 100) {
		$mes = qq|<span onclick="text_set('���ف[�� ')">$e2j{tired}�����܂��Ă��܂��B�u���ف[�ށv�ŉƂɋA��u���˂�v�ŋx��ł�������</span>|;
		return;
	}
	if ($m{coin} < $bet) {
		$mes = qq|<span onclick="text_set('����傤���� ')">��$bet�X���b�g������R�C��������܂���B�u����傤�����v�ŃR�C���𗼑ւ��Ă�������</span>|;
		return;
	}
	
	my @m = ('��','��','��','��','�V');
	my @o = (3,10, 20,  50,  70,  100); # �I�b�Y ��ԍ��̓`�F���[��2���낢�̂Ƃ�
	my @s = ();
	$s[$_] = int(rand(@m)) for (0 .. 2);
	$mes .= qq|<span onclick="text_set('����$bet�������')">|;
	$mes .= "\$$bet�X���b�g<br />";
	$mes .= "�y$m[$s[0]]�z�y$m[$s[1]]�z�y$m[$s[2]]�z<br />";
	$m{coin} -= $bet;

	# �A�Ŗh�~��
	$act_time *= 0.5;
	$m{wt}  = $time + $act_time;
	$nokori = $act_time;

	if ($s[0] == $s[1]) { # 1�ڂ�2��
		if ($s[1] == $s[2]) { # 2�ڂ�3��
			my $v = $bet * $o[$s[0]+1]; # +1 = �`�F���[2���낢
			$m{coin} += $v;
			$mes .= "�Ȃ��!! $m[$s[0]] ��3���낢�܂���!!<br />";
			$mes .= "���߂łƂ��������܂�!!<br />";
			$mes .= "***** �R�C�� $v �� GET !! *****<br />";
		}
		elsif ($s[0] == 0) { # �`�F���[�̂�1�ڂ�2�ڂ����낦�΂悢
			my $v = $bet * $o[0];
			$m{coin} += $v;
			$mes .= "�`�F���[��2���낢�܂�����<br />";
			$mes .= "�R�C�� $v ��Up��<br />";
		}
		else {
			$mes .= "�n�Y��<br />";
			$m{tired} += 1;
		}
	}
	else {
		$mes .= "�n�Y��<br />";
		$m{tired} += 1;
	}
	$mes .= "</span>";
}


#=================================================
# ����������
#=================================================
sub koukan {
	my $target = shift;
	
	my $p = qq|<table class="table1"><tr><th>�ܕi</th><th>���</th></tr>|;
	for my $i (1 .. $#prizes) {
		if ("$prizes[$i][0]��" eq $target) {
			if ($m{coin} >= $prizes[$i][0]) {
				if ($prizes[$i][1] eq '1') {
					&send_item($m, $prizes[$i][1], $prizes[$i][2]);
					$npc_com = "�R�C��$target�̏ܕi�ƌ����ł��ˁI$weas[ $prizes[$i][2] ][1]��$m�̗a���菊�ɑ����Ă����܂���";
				}
				elsif ($prizes[$i][1] eq '2') {
					&send_item($m, $prizes[$i][1], $prizes[$i][2]);
					$npc_com = "�R�C��$target�̏ܕi�ƌ����ł��ˁI$arms[ $prizes[$i][2] ][1]��$m�̗a���菊�ɑ����Ă����܂���";
				}
				else {
					&send_item($m, $prizes[$i][1], $prizes[$i][2]);
					$npc_com = "�R�C��$target�̏ܕi�ƌ����ł��ˁI$ites[ $prizes[$i][2] ][1]��$m�̗a���菊�ɑ����Ă����܂���";
				}
				$m{coin} -= $prizes[$i][0];
			}
			else {
				$mes = "�R�C��$target�̏ܕi�ƌ�������̂ɃR�C��������܂���";
			}
			return;
		}
	
		$p .= qq|<tr onclick="text_set('����������>$prizes[$i][0]�� ')"><td>|;
		$p .= $prizes[$i][1] eq '1' ? $weas[$prizes[$i][2]][1]
		    : $prizes[$i][1] eq '2' ? $arms[$prizes[$i][2]][1]
		    :                         $ites[$prizes[$i][2]][1]
		    ;
		$p .= qq|</td><td align="right">$prizes[$i][0]��</td></tr>|;
	}
	$p  .= qq|</table>|;
	$mes = qq|�ǂ�ƌ������܂����H<br />$p|;
	$act_time = 0;
}

#=================================================
# ����傤����
#=================================================
sub ryougae {
	my $target = shift;
	$target =~ s/��//;

	if ($target < 1 || $target =~ /[^0-9]/) {
		$mes = qq|<span onclick="text_set('����傤����>')">�R�C���P�� 20 G�ł��B�����痼�ւ��܂����H</span>|;
		return;
	}

	my $need_money = $target * 20;
	if ($need_money > $m{money}) {
		$mes = "�S�[���h������܂���B�R�C��$target���𗼑ւ���ɂ� $need_money G�K�v�ł�";
		return;
	}
	
	$m{coin}  += $target;
	$m{money} -= $need_money;
	$npc_com = "$target���̃R�C���Ɨ��ւ��܂���";
}


1; # �폜�s��
