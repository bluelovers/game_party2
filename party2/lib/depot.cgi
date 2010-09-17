#=================================================
# �a���菊 Created by Merino
#=================================================
# �ꏊ��
$this_title = '�a���菊';

# NPC��
$npc_name   = '@Ʒ��';

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$logdir/depot";

# �w�i�摜
$bgimg   = "$bgimgdir/depot.gif";

# ����̋֎~�A�C�e��(�၄'wea' => [1,2,3,4,5],)
%taboo_items = (
	'wea' => [], # ����
	'arm' => [], # �h��
	'ite' => [], # ����
);


#=================================================
# ���͂Ȃ��̉�b
#=================================================
my($my_depot, $max_depot) = &get_depot_c;
@words = (
	"������$this_title�����ǁA�����p�����H",
	"$m�́A�ő�$max_depot�܂ŗa���邱�Ƃ��ł��邺",
	"�]�E�񐔂������邲�Ƃɗa��������������Ă�����",
	"�������鎞�́A����A�C�e���Ƒ���̖��O�������Ă����",
	"�������Ƃ񂷂�ƁA����A�h��A����̏��ɐ��ڂł��邺",
	"�a���菊���܂�ς񂾂ƁA���肩��̃A�C�e�����󂯎��Ȃ���",
	"�a���菊���܂�ς񂾂ƁA�N�G�X�g�ł̕󕨂���ɓ���邱�Ƃ��ł��Ȃ���",
	"�����Ŕ���̂����X�Ŕ���̂����l�͕ς��Ȃ���",
);


#=================================================
# �ǉ��A�N�V����
#=================================================
push @actions, '����';
push @actions, '��������';
push @actions, '�Ђ�����';
push @actions, '�����Ƃ�';
push @actions, '������';
$actions{'����'}     = sub{ &uru      }; 
$actions{'��������'} = sub{ &azukeru  }; 
$actions{'�Ђ�����'} = sub{ &hikidasu }; 
$actions{'�����Ƃ�'} = sub{ &seiton   }; 
$actions{'������'  } = sub{ &okuru    }; 


#=================================================
# �w�b�_�[�\��
#=================================================
sub header_html {
	my $my_at = $m{at} + $weas[$m{wea}][3];
	my $my_df = $m{df} + $arms[$m{arm}][3];
	my $my_ag = $m{ag} - $weas[$m{wea}][4] - $arms[$m{arm}][4];
	$my_ag = 0 if $my_ag < 0;
	print qq|<div class="mes">�y$this_title�z �q�ɁF<b>$my_depot</b>/<b>$max_depot</b>�� / $e2j{money} <b>$m{money}</b>G|;
	print qq| / $e2j{at} <b>$my_at</b> / $e2j{df} <b>$my_df</b> / $e2j{ag} <b>$my_ag</b> /|;
	print qq| E�F$weas[$m{wea}][1]| if $m{wea};
	print qq| E�F$arms[$m{arm}][1]| if $m{arm};
	print qq| E�F$ites[$m{ite}][1]| if $m{ite};
	print qq|</div>|;
}

#=================================================
# ������
#=================================================
sub uru {
	my $target = shift;
	
	my $is_find = 0;
	my $p = '';
	my @lines = ();
	open my $fh, "+< $userdir/$id/depot.cgi" or &error("$userdir/$id/depot.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($kind, $no) = split /<>/, $line;
		if ($kind eq '1') { # ����
			my $buy_price = int($weas[$no][2] * 0.5);
			if (!$is_find && $weas[$no][1] eq $target) {
				$is_find = 1;
				$npc_com = "$weas[$no][1] �̔����� $buy_price G�ł��I";
				$m{money} += $buy_price;
			}
			else {
				$p .= qq|<span onclick="text_set('������>$weas[$no][1] ')">$weas[$no][1] $buy_price G</span> / |;
				push @lines, $line;
			}
		}
		elsif ($kind eq '2') { # �h��
			my $buy_price = int($arms[$no][2] * 0.5);
			if (!$is_find && $arms[$no][1] eq $target) {
				$is_find = 1;
				$npc_com = "$arms[$no][1] �̔����� $buy_price G�ł��I";
				$m{money} += $buy_price;
			}
			else {
				$p .= qq|<span onclick="text_set('������>$arms[$no][1] ')">$arms[$no][1] $buy_price G</span> / |;
				push @lines, $line;
			}
		}
		elsif ($kind eq '3') { # ����
			my $buy_price = int($ites[$no][2] * 0.5);
			if (!$is_find && $ites[$no][1] eq $target) {
				$is_find = 1;
				$npc_com = "$ites[$no][1] �̔����� $buy_price G�ł��I";
				$m{money} += $buy_price;
			}
			else {
				$p .= qq|<span onclick="text_set('������>$ites[$no][1] ')">$ites[$no][1] $buy_price G</span> / |;
				push @lines, $line;
			}
		}
	}
	if ($npc_com) {
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
		close $fh;
		&get_depot_c;
		return;
	}
	close $fh;
	
	$mes = qq|�ǂ�𔄂�܂����H<br />$p|;
	$act_time = 0;
}

#=================================================
# ����������
#=================================================
sub azukeru {
	my $target = shift;
	
	if ($m{is_full}) {
		$mes = "$max_depot�܂ł����a���邱�Ƃ͂ł��Ȃ�";
		return;
	}
	
	if ($weas[$m{wea}][1] eq $target) {
		$npc_com = "$weas[$m{wea}][1]�����a���肵�܂���";
		&send_item($m, 1, $m{wea});
		$m{wea} = 0;
	}
	elsif ($arms[$m{arm}][1] eq $target) {
		$npc_com = "$arms[$m{arm}][1]�����a���肵�܂���";
		&send_item($m, 2, $m{arm});
		$m{arm} = 0;
	}
	elsif ($ites[$m{ite}][1] eq $target) {
		$npc_com = "$ites[$m{ite}][1]�����a���肵�܂���";
		&send_item($m, 3, $m{ite});
		$m{ite} = 0;
	}
	
	if ($npc_com) {
		&get_depot_c;
		return;
	}
	
	$mes = qq|�ǂ��a����H<br />|;
	$mes .= qq|<span onclick="text_set('����������>$weas[$m{wea}][1] ')">$weas[$m{wea}][1]</span> / | if $m{wea};
	$mes .= qq|<span onclick="text_set('����������>$arms[$m{arm}][1] ')">$arms[$m{arm}][1]</span> / | if $m{arm};
	$mes .= qq|<span onclick="text_set('����������>$ites[$m{ite}][1] ')">$ites[$m{ite}][1]</span> / | if $m{ite};
	$act_time = 0;
}

#=================================================
# ���Ђ�����
#=================================================
sub hikidasu {
	my $target = shift;
	
	# ����������΍ŏ��Ɏ󂯎��
	if (-s "$userdir/$id/money.cgi") {
		&_get_money;
		return;
	}
	
	my $is_find = 0;
	my $p = '';
	my @lines = ();
	open my $fh, "+< $userdir/$id/depot.cgi" or &error("$userdir/$id/depot.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($kind, $no) = split /<>/, $line;
		if ($kind eq '1') { # ����
			if (!$is_find && $weas[$no][1] eq $target) { # ����
				$is_find = 1;
				if ($m{wea}) {
					$npc_com .= "$weas[$m{wea}][1]�����a���肵�܂����B";
					push @lines, "1<>$m{wea}<>\n";
				}
				$m{wea} = $no;
				$npc_com .= "$weas[$m{wea}][1]�����Ԃ����܂�";
			}
			else {
				$p .= qq|<span onclick="text_set('���Ђ�����>$weas[$no][1] ')">$weas[$no][1]</span> / |;
				push @lines, $line;
			}
		}
		elsif ($kind eq '2') { # �h��
			if (!$is_find && $arms[$no][1] eq $target) { # ����
				$is_find = 1;
				if ($m{arm}) {
					$npc_com .= "$arms[$m{arm}][1]�����a���肵�܂����B";
					push @lines, "2<>$m{arm}<>\n";
				}
				$m{arm} = $no;
				$npc_com .= "$arms[$m{arm}][1]�����Ԃ����܂�";
			}
			else {
				$p .= qq|<span onclick="text_set('���Ђ�����>$arms[$no][1] ')">$arms[$no][1]</span> / |;
				push @lines, $line;
			}
		}
		elsif ($kind eq '3') { # ����
			if (!$is_find && $ites[$no][1] eq $target) { # ����
				$is_find = 1;
				if ($m{ite}) {
					$npc_com .= "$ites[$m{ite}][1]�����a���肵�܂����B";
					push @lines, "3<>$m{ite}<>\n";
				}
				$m{ite} = $no;
				$npc_com .= "$ites[$m{ite}][1]�����Ԃ����܂�";
			}
			else {
				$p .= qq|<span onclick="text_set('���Ђ�����>$ites[$no][1] ')">$ites[$no][1]</span> / |;
				push @lines, $line;
			}
		}
	}
	if ($npc_com) {
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
		close $fh;
		
		require "./lib/_add_collection.cgi";
		&add_collection;
		return;
	}
	close $fh;
	
	$mes = qq|�ǂ���Ђ������H<br />$p|;
	$act_time = 0;
}
# ------------------
# �S�[���h���󂯂Ƃ�
sub _get_money {
	open my $fh, "+< $userdir/$id/money.cgi" or &error("$userdir/$id/money.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($money, $message) = split /<>/, $line;
		$m{money} += $money;
		if ($money >= 0) {
			$mes.="$message �Ƃ��� $money G���󂯎��܂���<br />";
		}
		else {
			$money *= -1;
			$mes.="$message �Ƃ��� $money G���x�����܂���<br />";
		}
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	close $fh;
}


#=================================================
# �������Ƃ�
#=================================================
sub seiton {
	my @lines = ();
	open my $fh, "+< $userdir/$id/depot.cgi" or &error("$userdir/$id/depot.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	push @lines, $_ while <$fh>;
	@lines = map { $_->[0] }
				sort { $a->[1] <=> $b->[1] || $a->[2] <=> $b->[2] }
					map { [$_, split /<>/ ] } @lines;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	$npc_com = "�a�����Ă���A�C�e���������Ƃ񂵂�";
}



#=================================================
# ��������
#=================================================
sub okuru {
	my $target = shift;
	my($send, $name) = split /��������&gt;/, $target;
	
#	if ($m{job_lv} < 1) {
#		$mes = "���]�E�̕��́A���邱�Ƃ͂ł��܂���B";
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
	
	$mes  = qq|�ǂ������ɑ���H<br />$p|;
	$mes .= qq|<span onclick="text_set('��������>$weas[$m{wea}][1]��������')">$weas[$m{wea}][1]</span> / | if $m{wea};
	$mes .= qq|<span onclick="text_set('��������>$arms[$m{arm}][1]��������')">$arms[$m{arm}][1]</span> / | if $m{arm};
	$mes .= qq|<span onclick="text_set('��������>$ites[$m{ite}][1]��������')">$ites[$m{ite}][1]</span> / | if $m{ite};
	$mes .= qq|<span onclick="text_set('��������>$m{money}G��������')">$m{money}G</span> / |;
	$act_time = 0;
}



1; # �폜�s��
