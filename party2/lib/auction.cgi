#=================================================
# �a���菊 Created by Merino
#=================================================
# �ꏊ��
$this_title = '�I�[�N�V�������';

# NPC��
$npc_name   = '@ܲ���';

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$logdir/auction";

# �w�i�摜
$bgimg   = "$bgimgdir/auction.gif";

# ����̋֎~�A�C�e��(�၄'wea' => [1,2,3,4,5],)
%taboo_items = (
	'wea' => [], # ����No
	'arm' => [], # �h��No
	'ite' => [], # ����No
);

#=================================================
# ���͂Ȃ��̉�b
#=================================================
@words = (
	"������$this_title�ł��B���̃v���C���[�ƃA�C�e��������A�C�e������������ꏊ�ł��B",
	"���D��o�i�̂悤�ȃV�X�e���͂Ȃ��ł��B���R�ɋ�������Ă��������B",
	"���肪���ۂɂ��̃A�C�e���◎�D���������Ă���̂��u������ׂ�v�Ō��邱�Ƃ��ł��܂��B",
);


#=================================================
# �ǉ��A�N�V����
#=================================================
push @actions, '������';
$actions{'������'} = sub{ &okuru }; 

#=================================================
# ��������
#=================================================
sub okuru {
	my $target = shift;
	my($send, $name) = split /��������&gt;/, $target;
	
#	if ($m{job_lv} < 1) {
#		$mes = "���]�E�̕��́A���邱�Ƃ͂ł��܂���";
#		return;
#	}

	if ($name) {
		my $yid = unpack 'H*', $name;
		unless (-d "$userdir/$yid") {
			$mes = "$name�Ƃ����v���C���[�͑��݂��܂���";
			return;
		}
		my %p = &get_you_datas($yid, 1);
		if ($p{is_full}) {
			$mes = "$name�̗a���菊�������ς��ł�";
			return
		}
		
		if ($send =~ /^([0-9]+)\x20?G?$/) {
			my $send_money = int($1);
			if ($send_money > $m{money}) {
				$mes = "����Ȃɂ����������Ă��܂���";
				return;
			}
			elsif ($send_money <= 0) {
				$mes = "�����͍Œ�ł� 1 G�ȏ�ł�";
				return;
			}
			
			$m{money} -= $send_money;
			&send_money($name, $send_money, "$m����̑���");
			$npc_com = "$send_money G�� $name �ɑ���܂���";
			return;
		}
		elsif ($m{wea} && $weas[$m{wea}][1] eq $send) {
			for my $taboo_item (@{ $taboo_items{wea} }) {
				if ($weas[$taboo_item][1] eq $weas[$m{wea}][1]) {
					$mes = "$weas[$m{wea}][1]�͑��邱�Ƃ��ł��܂���";
					return;
				}
			}
			$npc_com = "$weas[$m{wea}][1]��$name�ɑ���܂���";
			&send_item($name, 1, $m{wea}, $m);
			$m{wea} = 0;
		}
		elsif ($m{arm} && $arms[$m{arm}][1] eq $send) {
			for my $taboo_item (@{ $taboo_items{arm} }) {
				if ($arms[$taboo_item][1] eq $arms[$m{arm}][1]) {
					$mes = "$arms[$m{arm}][1]�͑��邱�Ƃ��ł��܂���";
					return;
				}
			}
			$npc_com = "$arms[$m{arm}][1]��$name�ɑ���܂���";
			&send_item($name, 2, $m{arm}, $m);
			$m{arm} = 0;
		}
		elsif ($m{ite} && $ites[$m{ite}][1] eq $send) {
			for my $taboo_item (@{ $taboo_items{ite} }) {
				if ($ites[$taboo_item][1] eq $ites[$m{ite}][1]) {
					$mes = "$ites[$m{ite}][1]�͑��邱�Ƃ��ł��܂���";
					return;
				}
			}
			$npc_com = "$ites[$m{ite}][1]��$name�ɑ���܂���";
			&send_item($name, 3, $m{ite}, $m);
			$m{ite} = 0;
		}
		
		&get_depot_c;
		return;
	}
	
	$mes  = qq|�ǂ��N�ɑ���܂����H<br />$p|;
	$mes .= qq|<span onclick="text_set('��������>$weas[$m{wea}][1]��������')">$weas[$m{wea}][1]</span> / | if $m{wea};
	$mes .= qq|<span onclick="text_set('��������>$arms[$m{arm}][1]��������')">$arms[$m{arm}][1]</span> / | if $m{arm};
	$mes .= qq|<span onclick="text_set('��������>$ites[$m{ite}][1]��������')">$ites[$m{ite}][1]</span> / | if $m{ite};
	$mes .= qq|<span onclick="text_set('��������>$m{money}G��������')">$m{money}G</span> / |;
	$act_time = 0;
}



1; # �폜�s��
