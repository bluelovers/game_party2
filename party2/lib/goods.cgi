#=================================================
# �Ƌ Created by Merino
#=================================================
# �ꏊ��
$this_title = '�I���N����';

# NPC��
$npc_name = '@׸�';

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$logdir/goods";

# �w�i�摜
$bgimg = "$bgimgdir/goods.gif";

# �����Ă��铹��(No)
@sales = $m{job_lv} > 10  ? (44..56) : (44..45+$m{job_lv});
push @sales, (138..141) if $m{job_lv} > 15;

#=================================================
# �͂Ȃ����t
#=================================================
@words = (
	"�����I�v���Ԃ�̂��q���I�悭�����悭�����I������$this_title����",
	"�����ׂ��݂ł��Ȃ��̉Ƃ��I�V�����ɂ��邱�Ƃ��ł�����",
	"�ǎ��͔����Ă��΂炭������A������ŏ���ɒ���ւ��Ă������B�����m�F�������l�͎����̉ƂōX�V�{�^���������Ƃ�����",
	"�ߑ��͒��������炻�̓�����̃����^������A���̓��ɂ͕Ԃ��Ă��炤��",
	"�ߑ��͓]�E����Ƃ��ɂ��Ԃ��Ă��炤��",
);

#=================================================
# ������ׂ�>NPC
#=================================================
sub shiraberu_npc {
	$mes = qq|<span onclick="text_set('����݂����� �ɍs������')">$npc_name�u�����H�Ȃ񂶂�Ȃ񂶂�H�킵�ች���m����v</span>|;
}

#=================================================
# �ǉ��A�N�V����
#=================================================
push @actions, '����';
push @actions, '���ׂ���';
$actions{'����'}     = sub{ &kau }; 
$actions{'���ׂ���'} = sub{ &kabegami }; 
$actions{'��݂�����'} = sub{ &yamiichiba };

#=================================================
# ����݂�����
#=================================================
sub yamiichiba {
	return if $m{job_lv} < 15;
	$mes = "�Ŏs��������܂����I";
	$m{lib} = 'black_market';
	&auto_reload;
}

#=================================================
# ������
#=================================================
sub kau {
	my $target = shift;
	
	my $h_no = &get_helper_item(3);

	my $p = qq|<table class="table1"><tr><th>���O</th><th>�l�i</th></tr>|;
	for my $i (@sales) {
		next if $h_no =~ /,$i,/; # �菕���N�G�X�g�ň˗�����Ă���A�C�e���͏���
		if ($ites[$i][1] eq $target) {
			if ($m{money} >= $ites[$i][2]) {
				if ($m{ite}) {
					&send_item($m, 3, $i);
					$npc_com = "$ites[$i][1]��$m�̗a���菊�ɑ����Ă��������";
				}
				else {
					$m{ite} = $i;
					$npc_com = "$ites[$i][1]���ȁB�ق��A�ǂ���";
					require "./lib/_add_collection.cgi";
					&add_collection;
				}
				$m{money} -= $ites[$i][2];
			}
			else {
				$mes = "$m��c�S�[���h�������";
			}
			return;
		}
		$p .= qq|<tr onclick="text_set('������>$ites[$i][1] ')"><td>$ites[$i][1]</td><td align="right">$ites[$i][2] G</td></tr>|;
	}
	$p  .= qq|</table>|;
	$mes = qq|�ǂ�𔃂��̂��H<br />$p|;
	$act_time = 0;
}

#=================================================
# �����ׂ���
#=================================================
sub kabegami {
	my $target = shift;
	
	my $count = 0;
	my $p = qq|<table><tr>|;
	for my $k (sort { $kabes{$a} <=> $kabes{$b} } keys %kabes) {
		my $base_name = $k;
		$base_name =~ s/(.+)\..+/$1/; # ���h���������̂Ŋg���q������
		
		if ($base_name eq $target) {
			if ($m{money} >= $kabes{$k}) {
				&copy("$bgimgdir/$k", "$userdir/$id/bgimg.gif");
				$npc_com   = qq|$m�̉Ƃ̕ǎ��� $base_name �ɁA����ւ��Ă��������|;
				$m{money} -= $kabes{$k};
			}
			else {
				$mes = "$m��c�S�[���h�������";
			}
			return;
		}
		$p .= qq|<td valign="bottom"><span onclick="text_set('�����ׂ���>$base_name ')"><img src="$bgimgdir/$k" title="$base_name" /><br />$kabes{$k} G</span></td>|;
		$p .= qq|</tr><tr>| if ++$count % 10 == 0;
	}
	$p .= qq|</tr></table>|;

	$mes = qq|�ǂ̕ǎ��ɂ���̂��H<br />$p|;
	$act_time = 0;
}


1; # �폜�s��
