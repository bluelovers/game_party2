#=================================================
# �����ʏ��� Created by Merino
#=================================================


#=================================================
# �ǉ��A�N�V����
#=================================================
push @actions, '���Ă�';
push @actions, '��������';
$actions{'���Ă�'}   = sub{ &tateru }; 
$actions{'��������'} = sub{ &chekku }; 

#=================================================
# ����������
#=================================================
sub chekku {
	my $target = shift;
	
	unless ($target) {
		$mes = qq|<span onclick="text_set('����������')">����������>������ �̉ƂŁA���̉Ƃ̏��L���Ԃ𒲂ׂ邱�Ƃ��ł��܂�</span>|;
		return;
	}
	
	$target .= ' �̉�';
	open my $fh, "< ${this_file}_member.cgi" or &error("${this_file}_member.cgi�t�@�C�����ǂݍ��߂܂���");
	while (my $line = <$fh>) {
		my($ltime, $is_npc, $name, $laddr, $icon, $color) = split /<>/, $line;
		if ($target eq $name) {
			my($hour,$mday,$mon) = (localtime($ltime))[2..4];
			my $c_date = sprintf("%d��%d��%d��", $mon+1,$mday,$hour);
			$npc_com = "<b>$name</b>�̏��L���Ԃ� $c_date �܂łł�";
			return;
		}
	}
	close $fh;

	$mes = qq|<span onclick="text_set('����������')">����������>������ �̉ƂŁA���̉Ƃ̏��L���Ԃ𒲂ׂ邱�Ƃ��ł��܂�</span>|;
}

#=================================================
# �����Ă�
#=================================================
sub tateru {
	my $target = shift;
	
	my $p = '';
	for my $house (@houses) {
		my $no = $house;
		$no =~ s/(.+)\..+/$1/; # ���h���������̂Ŋg���q������
		if ($no eq $target) {
			if ($m{money} < $price) {
				$mes = "�Ƃ����Ă邨��������܂���";
			}
			elsif (&is_max_house) {
				$mes = "$this_title �ɂ� �ő� $max_house ���܂ł������Ă邱�Ƃ��ł��܂���<br />�Ƃ��Ȃ��Ȃ�܂ł��΂炭���҂���������";
			}
			elsif (&is_build_house) {
				$mes = "$m �͂��łɉƂ������Ă��܂�";
			}
			else {
				my $c_time = $time + $cycle_house_day * 24 * 60 * 60;
				open my $fh, ">> ${this_file}_member.cgi" or &error("${this_file}_member.cgi�t�@�C�����J���܂���");
				print $fh "$c_time<>0<>$m �̉�<>0<>house/$house<>$npc_color<>\n";
				close $fh;
				
				my($hour,$mday,$mon) = (localtime($c_time))[2..4];
				my $c_date = sprintf("%d��%d��%d��", $mon+1,$mday,$hour);
				$npc_com = "$m �̉Ƃ����Ă܂����I�Ƃ̏��L���Ԃ� $c_date �܂łł�";
				$m{money} -= $price;
				&regist_guild_data('point', $cycle_house_day * 10, $m{guild}) if $m{guild};
			}
			return;
		}
		$p .= qq|<span onclick="text_set('�����Ă�>$no ')"><img src="$icondir/house/$house" /></span> |;
	}
	$mes = qq|�y$this_title�z �Ƃ̒l�i $price G / �ő匚�ݐ� $max_house �� / ���L���� $cycle_house_day ��<br />�ǂ̉Ƃ����Ă܂����H<br />$p|;
	$act_time = 0;
}


# ���łɉƂ����ĂĂ��邩�ǂ���
sub is_build_house {
	for my $i (0..$#towns) {
		open my $fh, "< $logdir/${towns[$i][1]}_member.cgi" or &error("$logdir/${towns[$i][1]}_member.cgi�t�@�C�����ǂݍ��߂܂���");
		while (my $line = <$fh>) {
			my($ltime, $is_npc, $name, $laddr, $icon, $color) = split /<>/, $line;
			return 1 if $name eq "$m �̉�";
		}
		close $fh;
	}
	return 0;
}


# �ő吔�𒴂��Ă��邩�ǂ���
sub is_max_house {
	my $count = 0;
	for my $name (@members) {
		++$count if $ms{$name}{color} eq $npc_color;
	}
	return $count >= $max_house ? 1 : 0;
}





1; # �폜�s��
