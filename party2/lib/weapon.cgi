#=================================================
# ���퉮 Created by Merino
#=================================================
# �ꏊ��
$this_title = '���퉮';

# NPC��
$npc_name = '@�ޯ��';

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$logdir/weapon";

# �w�i�摜
$bgimg = "$bgimgdir/weapon.gif";


# �����Ă��镐��(No)
@sales = $m{job_lv} > 11 ? (1..5,43,6..16) : (1..5,43,6+$m{job_lv});


#=================================================
# �͂Ȃ����t
#=================================================
@words = (
	"�����͕��퉮���I�킢�ɕ���͕K�{�����I",
	"$m�ɂ�$weas[$sales[int(rand(@sales))]][1]�Ȃ񂩗ǂ��񂶂�˂����H",
	"$m�ɂ�$weas[$sales[int(rand(@sales))]][1]���I�X�X�����I",
	"���̌��͂ǂ��̌��H",
	"�悧�I���������Ă����̂��H",
	"�f�����������Ɖ�S�̈ꌂ���𗦂��オ�邼�I",
	"$e2j{at}���������A�d�����d���Ȃ�$e2j{ag}��������B�܂�A�����ɍ�����������������Ă��Ƃ��I",
	"���̐��E�̂ǂ����ɁA�����̋����ɂ�蕐��̋������ς�镐�킪����炵�����I",
	"�����X�^�[�ɂ��ꂽ�Ƃ��Ă������������ɂȂ邱�Ƃ͂Ȃ����I",
	"$m��$e2j{at}��$m{at}���c�B$e2j{lv}$m{lv}�ɂ��Ă͂Ȃ��Ȃ����ȁI",
	"$m�̓]�E�񐔂�$m{job_lv}�񂩁I�]�E�񐔂�������Ώn���҂ƌ��Ȃ��A�����Ƌ�������𔄂��Ă�邺�I",
);

sub shiraberu_npc {
	$mes = "$npc_name�u���������A���͕��킶��˂����v";
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
	
	my $h_no = &get_helper_item(1);
	
	my $p = qq|<table class="table1"><tr><th>���O</th><th>�l�i</th><th>����</th><th>�d��</th></tr>|;
	for my $i (@sales) {
		next if $h_no =~ /,$i,/; # �菕���N�G�X�g�ň˗�����Ă���A�C�e���͏���
		$weas[$i][2] *= 2; # �B���ł���̂łQ�{
		if ($weas[$i][1] eq $target) {
			if ($m{money} >= $weas[$i][2]) {
				if ($m{wea}) {
					&send_item($m, 1, $i);
					$npc_com = "�܂��ǁI$weas[$i][1]��$m�̗a���菊�ɑ����Ă��������I";
				}
				else {
					$m{wea} = $i;
					$npc_com = "�܂��ǁI$weas[$i][1]���I�󂯂Ƃ��Ă���I";
					require "./lib/_add_collection.cgi";
					&add_collection;
				}
				$m{money} -= $weas[$i][2];
			}
			else {
				$mes = "����������Ȃ��݂�������";
			}
			return;
		}
		$p .= qq|<tr onclick="text_set('������>$weas[$i][1] ')"><td>$weas[$i][1]</td><td align="right">$weas[$i][2] G</td><td align="right">$weas[$i][3]</td><td align="right">$weas[$i][4]</td></tr>|;
	}
	$p  .= qq|</table>|;
	$mes = qq|���𔃂��񂾂��H<br />$p|;
	$act_time = 0;
}

#=================================================
# ������
#=================================================
sub uru {
	my $target = shift;
	
	unless ($m{wea}) {
		$mes = "������ĉ��𔄂�C���H$m�͕���������Ă��Ȃ��悤����";
		return;
	}
	
	# ������z
	my $buy_price = int($weas[$m{wea}][2] * 0.5);
	
	if ($weas[$m{wea}][1] eq $target) {
		$npc_com = "$weas[$m{wea}][1] �̔����� $buy_price G���I";
		$m{money} += $buy_price;
		$m{wea} = 0;
		return;
	}

	$mes = qq|<span onclick="text_set('������>$weas[$m{wea}][1] ')">$weas[$m{wea}][1]�Ȃ� $buy_price G�Ŕ�����邺�I</span>|;
	$act_time = 0;
}


1; # �폜�s��
