my $yid = unpack 'H*', $m{home};
if (!$m{home} || !-d "$userdir/$yid") { my $yhome = $m{home}; $m{home} = $m; &write_user; &error("$yhome�Ƃ����Ƃ͌�����܂���"); }
#=================================================
# �z�[�� Created by Merino
#=================================================
# �莆�A�莆����A�A�C�e���g�p ����

# �ꏊ��
$this_title = "$m{home}�̉�";

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$userdir/$yid/home";

# �w�i�摜
$bgimg   = "$userdir/$yid/bgimg.gif";

$max_monster_word = 120;

#=================================================
# ���l�̉ƂȂ炱���܂�
unless ($m eq $m{home}) {
	push @actions, '�˂�';
	push @actions, '�����Ăނ�����';
	push @actions, '���񂷂��[�Ԃ���';
	push @actions, '����Ԃ܂����[';
	push @actions, '�Ղ�ӂ��[��';
	$actions{'�˂�'}             = sub{ &neru };
	$actions{'�����Ăނ�����'}   = sub{ &aitemuzukan  };
	$actions{'���񂷂��[�Ԃ���'} = sub{ &monster_book };
	$actions{'����Ԃ܂����['}   = sub{ &job_master   };
	$actions{'�Ղ�ӂ��[��'}     = sub{ &profile      };
	return 1;
}

#=================================================

#=================================================
# �ȉ��A�����̉ƂȂ�
#=================================================
if (-f "$userdir/$yid/letter_flag.cgi") {
	print qq|<div class="get">�莆���͂��Ă��܂�</div>|;
	unlink "$userdir/$yid/letter_flag.cgi" or &error("$userdir/$yid/letter_flag.cgi�t�@�C�����폜�ł��܂���");
}
if (-f "$userdir/$yid/money_flag.cgi") {
	print qq|<div class="get">�������a���菊�ɓ͂��Ă��܂�</div>|;
	unlink "$userdir/$yid/money_flag.cgi" or &error("$userdir/$yid/money_flag.cgi�t�@�C�����폜�ł��܂���");
}
if (-s "$userdir/$yid/send_item_mes.cgi") {
	open my $fh, "+< $userdir/$yid/send_item_mes.cgi" or &error("$userdir/$yid/send_item_mes.cgi�t�@�C�����J���܂���");
	while (my $send_message = <$fh>) {
		print qq|<div class="get">$send_message</div>|;
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	close $fh;
}


#=================================================
# �ǉ��A�N�V����
#=================================================
push @actions, '�˂�';
push @actions, '�����Ăނ�����';
push @actions, '���񂷂��[�Ԃ���';
push @actions, '����Ԃ܂����[';
push @actions, '�Ղ�ӂ��[��';
push @actions, 'br';
push @actions, '����';
push @actions, '�Ă��݂�����';
push @actions, '�Ă��݂����';
push @actions, '����[';
push @actions, '���Ƃ΂���������';
$actions{'�˂�'}         = sub{ &neru };
$actions{'�����Ăނ�����'}   = sub{ &aitemuzukan };
$actions{'���񂷂��[�Ԃ���'} = sub{ &monster_book };
$actions{'����Ԃ܂����['}   = sub{ &job_master   };
$actions{'�Ղ�ӂ��[��'}     = sub{ &profile      };
$actions{'����'}       = sub{ &thukau };
$actions{'�Ă��݂�����'} = sub{ &tegamiwokaku };
$actions{'�Ă��݂����'} = sub{ &tegamiwoyomu };
$actions{'����['}       = sub{ &color };
$actions{'���Ƃ΂���������'} = sub{ &kotobawooshieru };
#=================================================
# ��ʈ�ԏ�ɕ\��(�ꏊ�̖��O�A�X�e�[�^�X�Ȃ�)
#=================================================
sub header_html { 
	if ($m{home} eq $m) {
		my $next_lv = $m{lv} * $m{lv} * 10;
		print qq|<div class="mes">�y$this_title�z $e2j{lv}<b>$m{lv}</b> / $e2j{exp}<b>$m{exp}</b>Exp / ����$e2j{lv}<b>$next_lv</b>Exp / �]�E��<b>$m{job_lv}</b>�� / $e2j{money}<b>$m{money}</b>G / ��J�x<b>$m{tired}</b>��|;
		print qq|<span onclick="text_set('������>$weas[$m{wea}][1] ')"> / E�F$weas[$m{wea}][1]</span>| if $m{wea};
		print qq|<span onclick="text_set('������>$arms[$m{arm}][1] ')"> / E�F$arms[$m{arm}][1]</span>| if $m{arm};
		print qq|<span onclick="text_set('������>$ites[$m{ite}][1] ')"> / E�F$ites[$m{ite}][1]</span>| if $m{ite};
		print qq|</div>|
	}
	else {
		print qq|<div class="mes">�y$this_title�z</div>|;
	}
}

#=================================================
# �����񂷂��[�Ԃ���
#=================================================
sub monster_book {
	$mes = qq|<form action="$userdir/$yid/monster_book.html" target="_blank"><input type="submit" value="$m{home}�̃����X�^�[�u�b�N" /></form>|;
}

#=================================================
# �������Ăނ�����
#=================================================
sub aitemuzukan {
	$mes = "$m{home}�̃A�C�e���}��";
	$m{lib} = 'collection';
	&auto_reload;
}
#=================================================
# ������Ԃ܂����[
#=================================================
sub job_master {
	$mes = "$m{home}�̃W���u�}�X�^�[";
	$m{lib} = 'job_master';
	&auto_reload;
}
#=================================================
# ���Ղ�ӂ��[��
#=================================================
sub profile {
	$mes = "$m{home}�̃v���t�B�[��";
	$m{lib} = 'profile';
	&auto_reload;
}

#=================================================
# ���˂�
#=================================================
sub neru {
	my($login_list, $login_count) = &get_login_member;
	
	$m{sleep} = $login_count >= 30 ? $sleep_time * 60 * 3
			  : $login_count >= 20 ? $sleep_time * 60 * 2
			  : 				     $sleep_time * 60;
	$com .= qq|$m�̓x�b�h�ɂ����肱�񂾁I|;
	
	$m{recipe} =~ s/^0/1/o;
}


#=================================================
# ������[
#=================================================
sub color {
	$target = shift;
	
	if ($target =~ /(#[0-9a-fA-F]{6})/) {
		$com .= qq|�J���[��<font color="$1">$1</font>�ɕύX���܂���|;
		$m{color} = $1;
		return;
	}
	else {
		my %sample_colors = (
			'���b�h'		=> '#FF3333',
			'�s���N'		=> '#FF33CC',
			'�I�����W'		=> '#FF9933',
			'�C�G���['		=> '#FFFF33',
			'�O���[��'		=> '#33FF33',
			'�A�N�A'		=> '#33CCFF',
			'�u���['		=> '#6666FF',
			'�p�[�v��'		=> '#CC66FF',
			'�O���C'		=> '#CCCCFF',
			'�z���C�g'		=> '#FFFFFF',
			'�G�������h'	=> '#33FF99',
		);
		
		$mes  = qq|#����n�܂�(16�i����)�J���[�R�[�h���L�����Ă�������<br />�T���v����|;
		
		while (my($name, $c_code) = each %sample_colors) {
			$mes .= qq|<span onclick="text_set('������[>$c_code ')" style="color: $c_code;">$name</span> |;
		}
		return;
	}
}


#=================================================
# ������
#=================================================
sub thukau {
	my $target = shift;

	unless ($target) {
		$mes .= qq|<span onclick="text_set('������>$weas[$m{wea}][1] ')">$weas[$m{wea}][1]</span> / | if $m{wea};
		$mes .= qq|<span onclick="text_set('������>$arms[$m{arm}][1] ')">$arms[$m{arm}][1]</span> / | if $m{arm};
		$mes .= qq|<span onclick="text_set('������>$ites[$m{ite}][1] ')">$ites[$m{ite}][1]</span> / | if $m{ite};
		
		$mes .= qq|<br />|;
		open my $fh, "< $userdir/$id/depot.cgi" or &error("$userdir/$id/depot.cgi�t�@�C�����J���܂���");
		while (my $line = <$fh>) {
			my($kind, $no) = split /<>/, $line;
			if    ($kind eq '1') {
				$mes .= qq|<span onclick="text_set('������>$weas[$no][1] ')">$weas[$no][1]</span> / |;
			}
			elsif ($kind eq '2') {
				$mes .= qq|<span onclick="text_set('������>$arms[$no][1] ')">$arms[$no][1]</span> / |;
			}
			elsif ($kind eq '3') {
				$mes .= qq|<span onclick="text_set('������>$ites[$no][1] ')">$ites[$no][1]</span> / |;
			}
		}
		close $fh;
		
		return;
	}
	
	if    ($target eq $weas[$m{wea}][1]) {
		$mes = qq|���햼�F$weas[$m{wea}][1] / �����F<b>$weas[$m{wea}][3]</b> / �d���F<b>$weas[$m{wea}][4]</b> / ���i�F<b>$weas[$m{wea}][2]</b>G|;
	}
	elsif ($target eq $arms[$m{arm}][1]) {
		$mes = qq|�h��F$arms[$m{arm}][1] / �����F<b>$arms[$m{arm}][3]</b> / �d���F<b>$arms[$m{arm}][4]</b> / ���i�F<b>$arms[$m{arm}][2]</b>G|;
	}
	elsif ($target eq $ites[$m{ite}][1]) {
		if ($ites[$m{ite}][3] eq '1') {
			$mes = "$ites[$m{ite}][1]�͐퓬���ł����g���܂���";
		}
		elsif ($ites[$m{ite}][3] eq '2') {
			$com .= "$ites[$m{ite}][1]���������I";
			&{ $ites[$m{ite}][4] };
			return if $mes;
			$m{ite} = 0;
		}
		else {
			$mes = "$ites[$m{ite}][1]�͂����ł͎g���܂���";
		}
	}
	else {
		my $is_lost = 0;
		my @lines = ();
		open my $fh, "+< $userdir/$id/depot.cgi" or &error("$userdir/$id/depot.cgi�t�@�C�����J���܂���");
		eval { flock $fh, 2; };
		while (my $line = <$fh>) {
			my($kind, $no) = split /<>/, $line;

			if ($is_lost) {
				push @lines, $line;
				next;
			}
			elsif ($kind eq '1' && $weas[$no][1] eq $target) {
				$mes = qq|���햼�F$weas[$no][1] / �����F<b>$weas[$no][3]</b> / �d���F<b>$weas[$no][4]</b> / ���i�F<b>$weas[$no][2]</b>G|;
				last;
			}
			elsif ($kind eq '2' && $arms[$no][1] eq $target) {
				$mes = qq|�h��F$arms[$no][1] / �����F<b>$arms[$no][3]</b> / �d���F<b>$arms[$no][4]</b> / ���i�F<b>$arms[$no][2]</b>G|;
				last;
			}
			elsif ($kind eq '3' && $ites[$no][1] eq $target) {
				if ($ites[$no][3] eq '2') {
					$com .= "$ites[$no][1]���������I";
					&{ $ites[$no][4] };
					return if $mes;
					$is_lost = 1;
					next;
				}
				else {
					$mes = "$ites[$no][1]�͂����ł͎g���܂���";
					last;
				}
			}
			push @lines, $line;
		}
		if ($is_lost) {
			seek  $fh, 0, 0;
			truncate $fh, 0;
			print $fh @lines;
			&get_depot_c; # ���t���ǂ����`�F�b�N
		}
		close $fh;
	}
}

#=================================================
# ���Ă��݂�����
#=================================================
sub tegamiwokaku {
	my $y = shift;

	$this_file = "$userdir/$id/letter_log";
	if ($y) {
		&send_letter($y, $com);
		return if $mes;
		$mes = "$y�Ɏ莆�𑗂�܂���";
		
		my $new_line = "$time<>$date<>$m<>$addr<>$m{color}<>$com<><>\n";
		# �����p�̑��M���O
		my @lines = ();
		open my $fh, "+< $userdir/$id/letter_log.cgi" or &error("$userdir/$id/letter_log.cgi�t�@�C�����J���܂���");
		eval { flock $fh, 2; };
		while (my $line = <$fh>) {
			push @lines, $line;
			last if @lines+1 >= $max_log;
		}
		unshift @lines, $new_line;
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
		close $fh;
	}
	else {
		$mes = qq|<span onclick="text_set('���Ă��݂�����')">�w���������Ă��݂�����>�������x�������ɑ��肽�������������ɑ����̖��O�������Ă��������B</span><br />�����M�ς݂̎莆|;
	}
}

#=================================================
# ���Ă��݂����
#=================================================
sub tegamiwoyomu {
	$this_file = "$userdir/$id/letter";
	$mes = "$m�̎󂯎�����莆";
}


#================================================
# ���͂Ȃ�
#================================================
sub hanasu {
	if (@members <= 1) {
		$mes = "�������A�N�����Ȃ������c" ;
		return;
	}
	
	my $line;
	open my $fh, "< $userdir/$yid/hanasu.cgi" or &error("$userdir/$yid/hanasu.cgi�t�@�C�����ǂݍ��߂܂���");
	rand($.) < 1 and $line = $_ while <$fh>;
	close $fh;
	$line =~ tr/\x0D\x0A//d; # ���s�폜

	$npc_name = $members[int(rand(@members))];
	$npc_name = $members[0] unless $ms{$npc_name}{color} eq $npc_color;
	$npc_com  = $line;
}

#================================================
# �����Ƃ΂���������
#================================================
sub kotobawooshieru {
	my $target = shift;
	
	unless ($target) {
		$mes = qq|<span onclick="text_set('�����Ƃ΂���������> ')">�����Ƃ΂���������>������ �ŉƂɂ��郂���X�^�[�����͂Ȃ��Řb���悤�ɂȂ�܂�|;
		return;
	}
	
	if (@members <= 1) {
		$mes = "�����鑊�肪���܂���";
	}
	elsif (length $target > $max_monster_word) {
		$mes = "���t���������܂�(���p$max_monster_word�����܂�)";
	}
	else {
		$npc_name = $members[int(rand(@members))];
		$npc_name = $members[0] unless $ms{$npc_name}{color} eq $npc_color;
		$npc_com  = $target;

		my @lines = ();
		open my $fh, "+< $userdir/$id/hanasu.cgi" or &error("$userdir/$id/hanasu.cgi�t�@�C�����J���܂���");
		eval { flock $fh, 2; };
		while (my $line = <$fh>) {
			push @lines, $line;
			last if @lines >= $max_log-1;
		}
		unshift @lines, "$target\n";
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
		close $fh;
	}
}

#================================================
# ���V�s�g�p
#================================================
sub learn_recipe {
	my @learns = @_;

	# ���V�s�ꗗ�ǂݍ���
	require './lib/_alchemy_recipe.cgi';

	# ���������Ă��郌�V�s������
	my @lines = ();
	open my $fh, "+< $userdir/$id/recipe.cgi" or &errror("$userdir/$id/recipe.cgi�t�@�C�����ǂݍ��߂܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		push @lines, $line;
		my($base, $sozai) = (split /<>/, $line)[1,2];
		delete($recipes{$base}{$sozai});
	}

	my %new_recipes = ();
	if (@learns) { # �K���ł��郌�V�s����
		for my $learn (@learns) {
			$new_recipes{$learn} = $recipes{$learn} if defined($recipes{$learn}) && values %{ $recipes{$learn} };
		}
	}
	else { # �S���K���\(�_�̃��V�s)
		for my $k (keys %recipes) {
			$new_recipes{$k} = $recipes{$k} if values %{ $recipes{$k} };
		}
	}
	
	my @bases = keys %new_recipes;
	if (@bases) {
		# ���K���̃��V�s�������_���Ŏ擾
		my $base = $bases[int rand @bases];
		my @sozais = keys %{ $recipes{$base} };
		my $sozai = $sozais[int rand @sozais];
		my $mix = $recipes{$base}{$sozai};

		push @lines, "0<>$base<>$sozai<>$mix<>\n";
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
		
		$com = "$m �͘B�����V�s��ǂ񂾁I�y$base �~ $sozai �� �H�H�H�z�̘B�����@���K�������I";

	}
	else {
		$com = "���̘B�����V�s���炱��ȏ�K���ł���B�����@�͂Ȃ��悤���c";
	}

	close $fh;
}


1; # �폜�s��
