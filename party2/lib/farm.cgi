#=================================================
# �����X�^�[�������� Created by Merino
#=================================================
# �ꏊ��
$this_title = '�����X�^�[��������';

# NPC��
$npc_name   = '@�ݼި';

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$logdir/farm";

# �w�i�摜
$bgimg   = "$bgimgdir/farm.gif";

# �ƂɘA��čs���鐔
$max_monster = 8;

#=================================================
# ���͂Ȃ��̉�b
#=================================================
@words = (
	"�킵���L����$npc_name����B�����X�^�[�̂��ƂȂ牽�ł������Ă��ꂢ",
	"���x�������X�^�[��|���Ă���ƁA�Ȃ��Ă��郂���X�^�[������̂���",
	"�l�Ԃ��D�ރ����X�^�[������Ƃ������Ƃ���",
	"$m�̏����ȋ����Ƀ����X�^�[�͂Ђ�������̂���",
	"�����̉Ƃɂ�$max_monster�C�܂Ńy�b�g��A��čs�����Ƃ��ł��邼��",
	"�����X�^�[�͍ő�30�C�܂ŗa�����Ă����邼���B����ȏ�́A�c�O���Ⴊ���킩��邵���Ȃ��̂��c",
	"�����X�^�[�a���菊���܂�ς�̏�Ԃ��ƁA�����X�^�[�͒��ԂɂȂ�񂩂璍�ӂ���",
	"�����������苭���������ԂɂȂ�₷������",
	"�ӂ��ӂ��ӂ��ӂ��ӂ��ӂ��ӂ�",
);

#=================================================
# �ǉ��A�N�V����
#=================================================
push @actions, '��Ă�';
push @actions, '�ȂÂ���';
push @actions, '��������';
push @actions, '������';
push @actions, '�킩���';
$actions{'��Ă�'} = sub{ &tureteku }; 
$actions{'�ȂÂ���'} = sub{ &nazukeru }; 
$actions{'��������'} = sub{ &azukeru }; 
$actions{'������'}   = sub{ &okuru }; 
$actions{'�킩���'} = sub{ &wakareru }; 

#=================================================
# ��������
#=================================================
sub okuru {
	my $target = shift;
	my($pet, $yname) = split /��������&gt;/, $target;
	
	if ($yname) {
		my $yid = unpack 'H*', $yname;
		unless (-f "$userdir/$yid/user.cgi") {
			$mes = "$yname�Ƃ����v���C���[�͑��݂��܂���";
			return;
		}

		if ( &is_full_monster($yid) ) {
			$mes = "$name�̃����X�^�[�a���菊�������ς��ł�";
			return
		}
	}

	my $p = '';
	my @lines = ();
	open my $fh, "+< $userdir/$id/monster.cgi" or &error("$userdir/$id/monster.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($mname, $micon) = split /<>/, $line;
		if ($yname && !$npc_com && $pet eq $mname) {
			my $yid = unpack 'H*', $yname;
			open my $fh2, ">> $userdir/$yid/monster.cgi" or &error("$userdir/$yid/monster.cgi�t�@�C�����J���܂���");
			print $fh2 "$mname<>$micon<>\n";
			close $fh2;
			$npc_com .= "$mname��$yname�̃����X�^�[�a���菊�ɑ����Ă�������";
		}
		else {
			push @lines, $line;
			$p .= qq|<span onclick="text_set('��������>$mname��������')"><img src="$icondir/$micon" />$mname</span> |;
		}
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	return if $npc_com;
	$mes = qq|�ǂ̃����X�^�[��N�ɑ���̂���H<br />$p|;
	$act_time = 0;
}
#=================================================
# ���킩���
#=================================================
sub wakareru {
	$y = shift;
	
	my $p = '';
	my @lines = ();
	open my $fh, "+< $userdir/$id/monster.cgi" or &error("$userdir/$id/monster.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($name, $icon) = split /<>/, $line;
		if (!$npc_com && $y eq $name) {
			$npc_com = "$name��쐶�ɋA���Ƃ�����";
		}
		else {
			push @lines, $line;
			$p .= qq|<span onclick="text_set('���킩���>$name ')"><img src="$icondir/$icon" />$name</span> |;
		}
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	return if $npc_com;
	$mes = qq|�ǂ̃����X�^�[�ƕʂ��̂���H<br />$p|;
	$act_time = 0;
}

#=================================================
# ����Ă�
#=================================================
sub tureteku {
	my $y = shift;
	
	my $p = '';
	my @lines = ();
	open my $fh, "+< $userdir/$id/monster.cgi" or &error("$userdir/$id/monster.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($name, $icon) = split /<>/, $line;
		if (!$npc_com && $y eq $name) {
			&_add_home_member($name, $icon);
			return if $mes;
			$npc_com = "$name��$m�̉Ƃɑ����Ă�������";
		}
		else {
			push @lines, $line;
			$p .= qq|<span onclick="text_set('����Ă�>$name ')"><img src="$icondir/$icon" />$name</span> |;
		}
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;

	return if $npc_com;
	$mes = qq|�ǂ̃����X�^�[��A��čs���̂���H<br />$p|;
	$act_time = 0;
}
sub _add_home_member {
	my($add_name, $add_icon) = @_;

	my $count = 0;
	open my $fh, "< $userdir/$id/home_member.cgi" or &error("$userdir/$id/home_member.cgi�t�@�C�����ǂݍ��߂܂���");
	while (my $line = <$fh>) {
		my($ltime, $is_npc, $name, $laddr, $icon, $color) = split /<>/, $line;
		next unless $is_npc;
		if ($add_name eq $name) {
			$mes = qq|<span onclick="text_set('���ȂÂ���>$add_name���Ȃ܂�>')">$m�̉Ƃɓ������O�̃����X�^�[�����܂��B�u���ȂÂ���v�Ŗ��O��ς��Ă�������</span>|;
			return;
		}
		++$count;
	}
	close $fh;

	if ($count >= $max_monster) {
		$mes = "����ȏ�A�����X�^�[���ƂɘA��čs�����Ƃ͂ł��܂���";
		return;
	}
	else {
		open my $fh2, ">> $userdir/$id/home_member.cgi" or &error("$userdir/$id/home_member.cgi�t�@�C�����J���܂���");
		print $fh2 "$time<>1<>$add_name<>0<>$add_icon<>$npc_color<>\n";
		close $fh2;
	}
}

#=================================================
# ����������
#=================================================
sub azukeru {
	my $y = shift;
	
	if ( &is_full_monster($id) ) {
		$mes = "����ȏ�A�����X�^�[��a���邱�Ƃ͂ł���";
		return;
	}
	
	my $p = '';
	my @lines = ();
	open my $fh, "+< $userdir/$id/home_member.cgi" or &error("$userdir/$id/home_member.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($ltime, $is_npc, $name, $laddr, $icon, $color) = split /<>/, $line;
		unless ($is_npc) {
			push @lines, $line;
			next;
		}
		if (!$npc_com && $y eq $name) {
			open my $fh2, ">> $userdir/$id/monster.cgi" or &error("$userdir/$id/monster.cgi�t�@�C�����J���܂���");
			print $fh2 "$name<>$icon<>\n";
			close $fh2;
			$npc_com = "$name��a�����Ă�����";
		}
		else {
			push @lines, $line;
			$p .= qq|<span onclick="text_set('����������>$name ')"><img src="$icondir/$icon" />$name</span> |;
		}
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;

	return if $npc_com;
	$mes = qq|�ǂ̃����X�^�[��a����̂���H<br />$p|;
	$act_time = 0;
}


#=================================================
# ���ȂÂ���
#=================================================
sub nazukeru {
	my $target = shift;
	
	my($y, $new_name) = split /���Ȃ܂�&gt;/, $target;
	
	if ($y && $new_name) {
		$mes = qq|<span onclick="text_set('���ȂÂ���>$y���Ȃ܂�>')">�����X�^�[���ɕs���ȋ󔒂��܂܂�Ă��܂�</span>|					if $new_name =~ /�@|\s/;
		$mes = qq|<span onclick="text_set('���ȂÂ���>$y���Ȃ܂�>')">�����X�^�[���ɕs���ȕ���( ,;\"\'&<> )���܂܂�Ă��܂�</span>| 	    if $new_name =~ /[,;\"\'&<>]/;
		$mes = qq|<span onclick="text_set('���ȂÂ���>$y���Ȃ܂�>')">�����X�^�[���ɕs���ȕ���( �� )���܂܂�Ă��܂�</span>| 			if $new_name =~ /��/;
		$mes = qq|<span onclick="text_set('���ȂÂ���>$y���Ȃ܂�>')">�����X�^�[���͑S�p�S����[���p�W����]�܂łł�</span>|				if length($new_name) > 8;
		return if $mes;
	}

	my @lines = ();
	my $p = '';
	open my $fh, "+< $userdir/$id/monster.cgi" or &error("$userdir/$id/monster.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($name, $icon) = split /<>/, $line;
		if (!$npc_com && $new_name && $y eq $name) {
			push @lines, "$new_name<>$icon<>\n";
			$npc_com = "$y��$new_name�Ɩ��Â�����";
		}
		else {
			push @lines, $line;
		}
		$p .= qq|<span onclick="text_set('���ȂÂ���>$name���Ȃ܂�>')"><img src="$icondir/$icon" />$name</span> |;
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	return if $npc_com;
	$mes = qq|�ǂ̃����X�^�[�ɉ��Ɩ��Â���̂���H<br />$p|;
	$act_time = 0;
}


1; # �폜�s��
