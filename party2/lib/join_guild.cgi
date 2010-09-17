#=================================================
# �M���h�ݗ� Created by Merino
#=================================================
# �ꏊ��
$this_title = '�M���h';

# NPC��
$npc_name   = '@�x�z�l';

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$logdir/join_guild";

# �w�i�摜
$bgimg   = "$bgimgdir/join_guild.gif";

# �M���h�ݗ���
$make_money = 5000;

# �f�t�H���g�̃M���h�}�[�N�A�C�R��
$default_mark = "$icondir/mark/000.gif";

# �M���h�}�[�N�ύX����
$mark_money = 3000;

# �ő�M���h��������(���p)
$max_guild_name = 16;

# �M���h�����폜�B���̓����ԁu������ǁv�ɂ��o���肪�Ȃ��ꍇ�����폜(��)
$auto_delete_guild_day = 20;

#=================================================
# �͂Ȃ����t
#=================================================
@words = (
	"$auto_delete_guild_day ���ȏ�u������ǁv�ɂ��o���肪�Ȃ��ꍇ�́A�����I�ɍ폜�ƂȂ�܂�",
	"�M���h�Ƃ́A�C�����������o�[�̏W�܂�ł�",
	"�M���h���́A�r���ŕς��邱�Ƃ��ł��܂���̂ŁA��������l���Ă�������",
	"�M���}�X�Ƃ́A�M���h�}�X�^�[�̗��̂ł��B���̃M���h���ň�Ԃ̌���������܂�",
	"�M���}�X�́A�����o�[�ɖ�E�����������邱�Ƃ��ł���̂ł�",
	"�M���h�}�[�N��ǎ��́A������������܂������x�ł��ς��邱�Ƃ��\�ł�",
	"�M���h�Q���҂́A�M���h�킪�ł���悤�ɂȂ�܂�",
	"�M���h��V�������ɂ́A$make_money G�K�v�ł�",
	"�M���h�}�[�N��ύX����ɂ́A$mark_money G�K�v�ł�",
	"�M���h��ŗD������Ə������_�����M���h���ɏ����Ă����܂�",
);


#=================================================
# �ǉ��A�N�V����
#=================================================
push @actions, '����';
push @actions, '����';
push @actions, '�܁[��';
push @actions, '���ׂ���';
#push @actions, '�����߂�'; # �����Ɓ���#$actions{'�����߂�'}�̃R�����g���O���ƃM���h�������ł���B
push @actions, '��������';
push @actions, '��������';
$actions{'����'}   = sub{ &sanka }; 
$actions{'����'}   = sub{ &tsukuru }; 
$actions{'�܁[��'}   = sub{ &mark }; 
$actions{'���ׂ���'} = sub{ &kabegami }; 
#$actions{'�����߂�'} = sub{ &kaimei }; 
$actions{'��������'} = sub{ &dattai }; 
$actions{'��������'} = sub{ &kaisan }; 


sub header_html { 
	print qq|<div class="mes">�y$this_title�z $e2j{money} <b>$m{money}</b>G|;
	print qq| / �M���h�y$m{guild}�z| if $m{guild};
	print qq|</div>|;
}

#=================================================
# �����ׂ���
#=================================================
sub kabegami {
	my $target = shift;
	
	if ($target) {
		unless ($m{guild}) {
			$mes = "�M���h�ɏ������Ă��܂���";
			return;
		}

		my $gid = unpack 'H*', $m{guild};
		unless (-d "$guilddir/$gid") {
			$mes = "$m{guild}�M���h�����݂��܂���";
			$m{guild} = "";
			return;
		}
		unless (&is_guild_master($gid)) {
			$mes = "�ǎ���ύX�ł���̂́A�M���h�}�X�^�[�����ł�";
			return;
		}
		if (defined $kabes{$target} && $m{money} < $kabes{$target}) {
			$mes = "����������܂���";
			return;
		}
	}
	
	my $count = 0;
	my $p = qq|<table><tr>|;
	for my $k (sort { $kabes{$a} <=> $kabes{$b} } keys %kabes) {
		my $base_name = $k;
		$base_name =~ s/(.+)\..+/$1/; # ���h���������̂Ŋg���q������
		if ($base_name eq $target) {
			&regist_guild_data('bgimg', $k, $m{guild});

			$npc_com   = qq|$m{guild}�̕ǎ��� $base_name �ɕύX���܂���|;
			$m{money} -= $kabes{$k};
			return;
		}
		$p .= qq|<td valign="bottom" align="right"><span onclick="text_set('�����ׂ���>$base_name ')"><img src="$bgimgdir/$k" title="$k" /><br />$kabes{$k} G</span></td>|;
		$p .= qq|</tr><tr>| if ++$count % 10 == 0;
	}
	$p .= qq|</tr></table>|;

	$mes = qq|�ǂ̕ǎ��ɂ��܂����H<br />$p|;
	$act_time = 0;
}


#=================================================
# ���܁[��
#=================================================
sub mark {
	my $target = shift;
	
	if ($target) {
		unless ($m{guild}) {
			$mes = "�M���h�ɏ������Ă��܂���";
			return;
		}

		my $gid = unpack 'H*', $m{guild};
		unless (-d "$guilddir/$gid") {
			$mes = "$m{guild}�M���h�����݂��܂���";
			$m{guild} = "";
			return;
		}
		unless (&is_guild_master($gid)) {
			$mes = "�M���h�}�[�N��ύX�ł���̂́A�M���h�}�X�^�[�����ł�";
			return;
		}
		if ($m{money} < $mark_money) {
			$mes = "�M���h�}�[�N��ύX����̂� <b>$mark_money</b> G�K�v�ł�";
			return;
		}
	}
	
	my $p = '';
	opendir my $dh, "$icondir/mark" or &error("$icondir/mark�f�B���N�g�����J���܂���");
	while (my $file_name = readdir $dh) {
		next if $file_name =~ /^\./;

		my $no = $file_name;
		$no =~ s/[^0-9]//g;

		if ($m{guild} && $no eq $target) {
			my $gid = unpack 'H*', $m{guild};
			# �M���h�}�[�N�摜���R�s�[
			&copy("$icondir/mark/$file_name", "$guilddir/$gid/mark.gif");

			$npc_com   = qq|$m{guild}�̃M���h�}�[�N�� <img src="$icondir/mark/$file_name" /> �ɕύX���܂���|;
			$m{money} -= $mark_money;
			return;
		}
		$p .= qq|<span onclick="text_set('���܁[��>$no ')"><img src="$icondir/mark/$file_name" title="$no" /></span> |;
	}
	closedir $dh;

	$mes = qq|�M���h�}�[�N�̕ύX�ɂ� $mark_money G������܂��B�ǂ̃M���h�}�[�N�ɂ��܂����H<br />$p|;
	$act_time = 0;
}



#=================================================
# ������
#=================================================
sub sanka {
	my $target = shift;
	
	if ($m{guild}) {
		$mes = "$m{guild}�ɎQ�����Ă��܂��B���̃M���h�ɎQ���������ꍇ�́A���̃M���h��E�ނ��Ă��������B";
		return;
	}
	
	my $p = '';
	opendir my $dh, $guilddir or &error("$guilddir�f�B���N�g�����J���܂���");
	while (my $gid = readdir $dh) {
		next if $gid =~ /\./;
		my $gname = pack 'H*', $gid;
		
		if ($target eq $gname) {
			open my $fh, "+< $guilddir/$gid/member.cgi" or &error("$guilddir/$gid/member.cgi�t�@�C�����J���܂���");
			eval { flock $fh, 2; };
			my $head_line = <$fh>;
			my @lines = ($head_line);
			while ($line = <$fh>) {
				my($name, $position) = split /<>/, $line;
				if ($name eq $m) {
					$mes = "$target�ɂ͂��łɎQ���\\�����o���Ă��܂�";
					return;
				}
				push @lines, $line;
			}
			push @lines, "$m<>�Q���\\����<>\n";
			seek  $fh, 0, 0;
			truncate $fh, 0;
			print $fh @lines;
			close $fh;
			
			my($guild_master) = (split /<>/, $head_line)[0];
			&send_letter($guild_master, "�y�{�Q���\\���{�z$gname ���c��]�� $m");
			$npc_com = "$gname�̃M���}�X $guild_master �ɎQ���\\���̎莆�𑗂�܂����B�M���}�X����̕Ԏ���҂��܂��傤";
			return;
		}
		$p .= qq|<span onclick="text_set('������>$gname ')">$gname</span> / |;
	}
	closedir $dh;
	
	$mes = "�ǂ̃M���h�ɎQ�����܂����H<br />$p";
}

#=================================================
# ������
#=================================================
sub tsukuru {
	my $target = shift;
	
	if ($m{guild}) {
		$mes = "$m{guild}�ɎQ�����Ă��܂��B�V�K�ɃM���h��ݗ�����ꍇ�́A���̃M���h��E�ނ��Ă��������B";
		return;
	}
	
	my $max_guild_name_z = int($max_guild_name * 0.5);
	unless ($target) {
		$mes  = "�ݗ����Ƃ��� $make_money G������܂��B<br />";
		$mes .= "������>������ �������ɂ̓M���h��������Ă�������(�ő�S�p$max_guild_name_z����[���p$max_guild_name����]�܂�)";
		return;
	}
	$mes = "�M���h���ɕs���ȋ󔒂��܂܂�Ă��܂�"								if $target =~ /�@|\s/;
	$mes = "�M���h���ɕs���ȕ���( ,;\"\'&<>\@ )���܂܂�Ă��܂�"				if $target =~ /[,;\"\'&<>\@]/;
	$mes = "�M���h���ɕs���ȕ���( �� )���܂܂�Ă��܂�"							if $target =~ /��/;
	$mes = "�M���h����$max_guild_name_z����[���p$max_guild_name����]�܂łł�"	if length $target > $max_guild_name;
	$mes = "�M���h�ݗ����� $make_money G������܂���"							if $make_money > $m{money};
	return if $mes;
	
	my $gid = unpack 'H*', $target;
	if (-d "$guilddir/$gid") {
		$mes = "���łɓ������O�̃M���h�����݂��܂�";
		return;
	}
	
	# �V�K�M���h�쐬
	mkdir "$guilddir/$gid", $mkdir or &error("$guilddir/$gid�f�B���N�g�����쐬�ł��܂���");
	
	my %guild_dirs = (
		log			=> "$time<>$date<>$npc_name<><>$npc_color<>�M���h�̐ݗ��������܂����M���h>$target<><>\n",
#		log_member	=> "$time<>1<>$target<>0.0.0.0<>$m{color}<>\n",
		log_member	=> "",
		member		=> "$m<>�M���}�X<>\n",
		data		=> "$target<>$m<>$default_color<><>$date�ݗ�<>0<>"
	);
	for my $k (keys %guild_dirs) {
		open my $fh, "> $guilddir/$gid/$k.cgi" or &error("$guilddir/$gid/$k.cgi�t�@�C�������܂���");
		print $fh $guild_dirs{$k};
		close $fh;
		chmod $chmod, "$guilddir/$gid/$k.cgi";
	}
	
	# �摜���R�s�[
	&copy($default_mark, "$guilddir/$gid/mark.gif");
	$m{lib}    = 'guild';
	$m{guild}  = $target;
	$m{money} -= $make_money;
	
	$npc_com = qq|<span class="st_up">���V�M���h <b>$target</b>�̐ݗ��������܂��I</span>|;
	&write_memory(qq|<span class="st_up">�V�M���h<b>$target</b>��ݗ��I</span>|);
	&write_news(qq|<span class="st_up">$m���V����<b>$target</b>�M���h��ݗ����܂����I</span>|);
	
	&check_dead_guild;
}
#=================================================
# �������߂�
#=================================================
sub kaimei {
	my $target = shift;
	
	unless ($m{guild}) {
		$mes = "�M���h�ɏ������Ă��܂���";
		return;
	}

	my $old_gid = unpack 'H*', $m{guild};
	unless (-d "$guilddir/$old_gid") {
		$mes = "$m{guild}�M���h�����݂��܂���";
		$m{guild} = "";
		return;
	}
	unless (&is_guild_master($old_gid)) {
		$mes = "�M���h����ύX�ł���̂́A�M���h�}�X�^�[�����ł�";
		return;
	}

	$mes = "�M���h���ɕs���ȋ󔒂��܂܂�Ă��܂�"					if $target =~ /�@|\s/;
	$mes = "�M���h���ɕs���ȕ���( ,;\"\'&<>\@ )���܂܂�Ă��܂�"	if $target =~ /[,;\"\'&<>\@]/;
	$mes = "�M���h���ɕs���ȕ���( �� )���܂܂�Ă��܂�"				if $target =~ /��/;
	$mes = "�M���h���͔��p$max_guild_name�����܂łł�"				if length $target > $max_guild_name;
	$mes = "�M���h����ύX����̂� <b>$make_money</b> G�K�v�ł�"	if $make_money > $m{money};
	return if $mes;
	
	my $gid = unpack 'H*', $target;
	if (-d "$guilddir/$gid") {
		$mes = "���łɓ������O�̃M���h�����݂��܂�";
		return;
	}
	
	# �V�K�M���h�쐬�{�f�[�^�R�s�[
	mkdir "$guilddir/$gid", $mkdir or &error("$guilddir/$gid�f�B���N�g�����쐬�ł��܂���");
	opendir my $dh, "$guilddir/$old_gid" or &error("$guilddir/$old_gid�f�B���N�g�����J���܂���");
	while (my $file_name = readdir $dh) {
		next if $file =~ /^\./;
		&copy("$guilddir/$old_gid/$file", "$guildir/$gid/$file");
	}
	closedir $dh;
	
	# �������Ă��郁���o�[�̃M���h����ύX
	open my $fh, "< $guilddir/$dir_name/member.cgi" or &error("$guilddir/$dir_name/member.cgi�t�@�C�����ǂݍ��߂܂���");
	while (my $line = <$fh>) {
		my($name, $position) = split /<>/, $line;
		next if $position eq '�Q���\����';
		&regist_you_data($name, 'guild', $target);
	}
	close $fh;
	
	# ���M���h�̍폜
	&delete_directory("$guilddir/$old_gid");
	
	$npc_com = qq|<span class="st_up">���M���h����<b>$m{guild}</b>���炽��<b>$target</b>�M���h�ɉ������܂�</span>|;
	&write_memory(qq|<span class="st_up">�M���h����<b>$target</b>�ɕύX</span>|);
	&write_news(qq|<span class="st_up">$m�� $m{guild} �M���h�� <b>$target</b> �M���h�ɕύX���܂����I</span>|);

	$m{lib}    = 'guild';
	$m{guild}  = $target;
	$m{money} -= $make_money;
}


#=================================================
# ����������
#=================================================
sub dattai {
	unless ($m{guild}) {
		$mes = "�M���h�ɏ������Ă��܂���";
		return;
	}

	&delete_guild_member($m{guild}, $m);
	&write_memory("$m{guild}����E�ނ���");
	$npc_com .= "$m{guild}����E�ނ��܂���";
	$m{guild} = '';
}

#=================================================
# ����������
#=================================================
sub kaisan {
	unless ($m{guild}) {
		$mes = "�M���h�ɏ������Ă��܂���";
		return;
	}
	
	my $gid = unpack 'H*', $m{guild};
	unless (-d "$guilddir/$gid") {
		$mes = "$m{guild}�M���h�����݂��܂���";
		$m{guild} = "";
		return;
	}
	
	if (&is_guild_master($gid)) {
		&delete_directory("$guilddir/$gid");
		&write_memory("$m{guild}�����U������");
		$npc_com  = "$m{guild}�����U�����܂���";
		&write_news(qq|<span class="die">$m{guild} �M���h�����U���܂���</span>|);
		$m{guild} = "";
	}
	else {
		$mes = "���U�����邱�Ƃ��ł���̂̓M���}�X�����ł�";
	}
}

# ------------------
# �M���h�}�X�^�[���ǂ���
sub is_guild_master {
	my $gid = shift;

	open my $fh, "< $guilddir/$gid/member.cgi" or &error("$guilddir/$gid/member.cgi�t�@�C�����ǂݍ��߂܂���");
	my $line = <$fh>;
	close $fh;
	my($guild_master) = (split /<>/, $line)[0];
	
	$m{name} eq $guild_master ? return 1 : return 0;
}


# ------------------
# �����ȏ�N���o���肵�Ă��Ȃ��M���h�̎����폜
sub check_dead_guild {
	opendir my $dh, $guilddir or &error("$guilddir�f�B���N�g�����J���܂���");
	while (my $gid = readdir $dh) {
		next if $gid =~ /\./;
		my($mtime) = (stat("$guilddir/$gid/log_member.cgi"))[9];
		if ($time > $mtime + $auto_delete_guild_day * 3600 * 24) {
			&delete_directory("$guilddir/$gid");
			my $gname = pack 'H*', $gid;
			&write_news(qq|<span class="die">$gname �M���h�����U���܂���</span>|);
		}
	}
	closedir $dh;
}


1; # �폜�s��
