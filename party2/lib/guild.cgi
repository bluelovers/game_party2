my($gid,$gname,$gmaster,$gcolor,$gbgimg,$gmes,$gpoint) = &read_guild_data;
#=================================================
# �M���h Created by Merino
#=================================================
# �ꏊ��
$this_title = qq|<img src="$guilddir/$gid/mark.gif" alt="�M���h�}�[�N" /><span style="color: $gcolor">$m{guild}</span>|;

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$guilddir/$gid/log";

# �w�i�摜
$bgimg   = "$bgimgdir/$gbgimg";

# �ő�M���h���b�Z�[�W������(���p)
$max_guild_mes = 200;

#=================================================

#=================================================
# �ǉ��A�N�V����
#=================================================
push @actions, '�߂�΁[';
push @actions, '��т�����';
$actions{'�߂�΁['} = sub{ &menba }; 
$actions{'��т�����'} = sub{ &yobikakeru }; 
if ($gmaster eq $m) {
	push @actions, '����[';
	push @actions, '�߂����[��';
	push @actions, '��������';
	$actions{'����['}     = sub{ &color }; 
	$actions{'�߂����[��'} = sub{ &message }; 
	$actions{'��������'}   = sub{ &ataeru }; 
}

#=================================================
# ����т�����
#=================================================
sub yobikakeru {
	my $target = shift;

	unless ($target) {
		$mes = qq|<span onclick="text_set('����т�����')">�w����т�����>�������x�M���h�̃����o�[�ɑ��肽�������������ɏ����Ă��������B</span>|;
		return;
	}
	
	$this_file = "$userdir/$id/letter_log";
	open my $fh, "< $guilddir/$gid/member.cgi" or &error("$guilddir/$gid/member.cgi�t�@�C�����ǂݍ��߂܂���");
	while (my $line = <$fh>) {
		my($name, $position) = split /<>/, $line;
		&send_letter($name, $com);
		return if $mes;
	}
	close $fh;
	
	$this_file = "$guilddir/$gid/log";
	$npc_name  = '@'.$gname;
	$npc_com   = "$gname�̃����o�[�S���Ɏ莆�𑗂�܂���";
	&regist_guild_data('point', 1, $m{guild}) if $m{guild};
}

#=================================================
# ������[
#=================================================
sub color {
	$target = shift;
	
	if ($target =~ /(#[0-9a-fA-F]{6})/) {
		my $color = uc $1;
		if ($color ne $default_color && ($color eq $npc_color || &is_used_guild_color($color)) ){
			$mes = "���łɑ��̃M���h�ł��̃J���[�͎g���Ă��܂�";
		}
		else {
			&regist_guild_data('color', $color, $m{guild});
			$com .= qq|�M���h�J���[��<font color="$color">$color</font>�ɕύX���܂���|;
		}
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
			'�u���['		=> '#3333FF',
			'�p�[�v��'		=> '#CC66FF',
			'�O���C'		=> '#CCCCCC',
			'�z���C�g'		=> '#FFFFFF',
		);
		
		$mes  = qq|#����n�܂�(16�i����)�J���[�R�[�h���L�����Ă��������B���z���C�g�̏ꍇ�̓M���h��͂ł��܂���<br />�T���v����|;
		
		while (my($name, $c_code) = each %sample_colors) {
			$mes .= qq|<span onclick="text_set('������[>$c_code ')" style="color: $c_code;">$name</span> |;
		}
		return;
	}
}
#=================================================
# ���߂����[��
#=================================================
sub message {
	$target = shift;
	
	unless ($target) {
		$mes = qq|<span onclick="text_set('���߂����[��>')">���b�Z�[�W���L�����Ă�������</span>|;
		return;
	}
	
#	$mes = qq|<span onclick="text_set('���߂����[��>')">���b�Z�[�W�ɕs���ȋ󔒂��܂܂�Ă��܂�</span>|						if $target =~ /�@|\s/;
	$mes = qq|<span onclick="text_set('���߂����[��>')">���b�Z�[�W�ɕs���ȕ���( ,;\"\'&<> )���܂܂�Ă��܂�</span>| 	    if $target =~ /[,;\"\'&<>]/;
#	$mes = qq|<span onclick="text_set('���߂����[��>')">���b�Z�[�W�ɕs���ȕ���( �� )���܂܂�Ă��܂�</span>| 				if $target =~ /��/;
	$mes = qq|<span onclick="text_set('���߂����[��>')">���b�Z�[�W�͔��p$max_guild_mes�����܂łł�</span>|					if length($target) > $max_guild_mes;
	return if $mes;
	
	&regist_guild_data('mes', $target, $m{guild});
	$com .= qq|�M���h���b�Z�[�W��ύX���܂���|;
}
#================================================
# ���͂Ȃ�
#================================================
sub hanasu { 
	if ($gmes) {
		$mes = $gmes;
	}
	else {
		&menba;
	}
}

#=================================================
# ���߂�΁[
#=================================================
sub menba {
	$mes .= "$gmes<br />";
	open my $fh, "< $guilddir/$gid/member.cgi" or &error("$guilddir/$gid/member.cgi�t�@�C�����ǂݍ��߂܂���");
	while (my $line = <$fh>) {
		my($name, $position) = split /<>/, $line;
		$mes .= qq|<span onclick="text_set('���ف[��>$name ')">$name��$position</span>,|;
	}
	close $fh;
}


#=================================================
# ����������
#=================================================
sub ataeru {
	$npc_name = '@'.$gname;
	my $target = shift;
	my($yname, $new_position) = split /���₭���傭&gt;/, $target;

	if ($yname) {
		$mes = "��E���ɕs���ȋ󔒂��܂܂�Ă��܂�"						if $new_position =~ /�@|\s/;
		$mes = "��E���ɕs���ȕ���( ,;\"\'&<>\@ )���܂܂�Ă��܂�" 		if $new_position =~ /[,;\"\'&<>\@]/;
		$mes = "��E���ɕs���ȕ���( �� )���܂܂�Ă��܂�" 				if $new_position =~ /��/;
		$mes = "$new_position�Ƃ�����E���͂��邱�Ƃ��ł��܂���"		if $new_position eq '�Q���\����' || $new_position eq '�Q���\\����' || $new_position eq '�M���}�X';
		$mes = "��E���͑S�p�U����[���p12����]�܂łł�"					if length($new_position) > 12;
		$mes = "��E�����L�����Ă�������"								if $new_position eq '';
		return if $mes;
	}
	
	my $p = '';
	$p .= qq|<span onclick="text_set('����������>���������₭���傭>������')">�w����������>���������₭���傭>�������x</span>�������ɂ͖��O�A�������ɂ͖�E��(�S�p�U����[���p12����]�܂�)���L���B<br />|;
	$p .= qq|<span onclick="text_set('���₭���傭>')">���₭���傭</span>��<span onclick="text_set('�Ǖ�')">�w�Ǖ��x</span>�ƋL������ƒǂ��o�����Ƃ��ł��܂��B<br />|;
	$p .= qq|�w�Q���\\�����x�̃����o�[�͉�����E���������邱�Ƃɂ��Q�����A<span onclick="text_set('�Ǖ�')">�w�Ǖ��x</span>�ŎQ�����ۂɂł��܂��B|;
	$p .= qq|�N�̖�E��ς��܂����H<br />|;
	
	my $is_find = 0;
	open my $fh, "+< $guilddir/$gid/member.cgi" or &error("$guilddir/$gid/member.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	my $head_line = <$fh>;
	my($guild_master) = (split /<>/, $head_line)[0];
	unless ($m eq $guild_master) {
		$mes = "��E���������邱�Ƃ��ł��錠���̓M���}�X�����ł�";
		return;
	}
	my @lines = ($head_line);
	while (my $line = <$fh>) {
		my($name, $position) = split /<>/, $line;
		$p .= qq|<span onclick="text_set('����������>$name���₭���傭>')">$name��$position</span>,|;
		if ($name eq $yname) {
			$is_find = 1;
			if ($position eq '�Q���\\����') {
				my $yid = unpack 'H*', $name;
				# �폜�Ȃǂł��Ȃ�
				unless (-f "$userdir/$yid/user.cgi") {
					$npc_com = "$name�Ƃ����v���C���[�͂��Ȃ��Ȃ��Ă��܂��܂���";
					next;
				}
				
				my %datas = &get_you_datas($yid, 1);
				# �\�����ɑ��̃M���h�ɓ������ꍇ
				if ($datas{guild}){
					$npc_com = "$name�͑��̃M���h�ɎQ�������悤�ł�";
					next;
				}

				# �Q������
				if ($new_position eq '�Ǖ�') {
					$npc_com = "$name�̎Q�������ۂ��܂���";
					&send_letter($name, "�y�{�s���i�{�z�c�O�Ȃ��� $m{guild} (�M���}�X $m) ����Q�������ۂ���܂���");
					next;
				}
				
				$npc_com = "$name��$m{guild}�ɎQ�����邱�Ƃ������܂���";
				&regist_you_data($name, 'guild', $m{guild});
				&send_letter($name, "�y�{�Q�����؁{�z$m{guild} (�M���}�X $m) ����Q���������炢�܂���");
				&write_memory("$m{guild}�M���h�ɉ���", $name);
				$line = "$name<>$new_position<>\n";
			}
			elsif ($new_position eq '�Ǖ�') {
				$npc_com = "$name��$m{guild}����Ǖ����܂���";
				&regist_you_data($name, 'guild', '');
				&send_letter($name, "�y�{�Ǖ��{�z$m{guild} (�M���}�X $m) ����Ǖ�����܂���");
				next;
			}
			else {
				$line = "$name<>$new_position<>\n";
			}
		}
		push @lines, $line;
	}
	if ($is_find) {
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
		close $fh;
	}
	else {
		close $fh;
		
		$mes = $p;
	}
}

sub is_used_guild_color {
	my $select_color = shift;
	
	opendir my $dh, $guilddir or &error("$guilddir�f�B���N�g�����J���܂���");
	while (my $dir_name = readdir $dh) {
		next if $dir_name =~ /^\./;
		open my $fh, "< $guilddir/$dir_name/data.cgi";
		my $line = <$fh>;
		close $fh;
		my($color) = (split /<>/, $line)[2];
		return 1 if $select_color eq $color;
	}
	closedir $dh;

	return 0;
}


1; # �폜�s��
