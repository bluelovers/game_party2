#=================================================
# �v���t�B�[�� Created by Merino
#=================================================
# ���ǉ�/�폜/�ύX/���ёւ���
# �v���t�B�[���\��������́B���̉p���͓�������Ȃ���Ή��ł��ǂ�
@profiles = (
	['name',		'���O'],
	['sex',			'����'],
	['blood',		'���t�^'],
	['birthday',	'�a����'],
	['age',			'�N��'],
	['job',			'�E��'],
	['address',		'�Z��ł��鏊'],
	['hobby',		'�'],
	['boom',		'�}�C�u�[��'],
	['site',		'�I�X�X���T�C�g'],
	['dream',		'��/�ڕW'],
	['character',	'���i�E����'],
	['like',		'�D���Ȃ���'],
	['dislike',		'�����Ȃ���'],
	['like_food',	'�D���ȐH�ו�'],
	['dislike_food','�����ȐH�ו�'],
	['goal',		'���̃Q�[���̖ڕW'],
	['login',		'���O�C������'],
	['boast',		'����'],
	['reference',	'���̃T�C�g��m������������'],
	['message',		'�����ꌾ'],
);

#=================================================

$yid = unpack 'H*', $m{home};
$this_file = "$userdir/$yid/profile.cgi";
$com = '';

sub read_member { return }
sub set_action  { return }

#=================================================
sub html {
	if ($m eq $m{home}) {
		$in{mode} eq 'write_exe' ? &write_exe : &write_form;
	}
	else {
		&view_profile;
	}
}

sub view_profile {
	unless ($is_top_profile) {
		$m{lib} = 'home'; # �߂�{�^�����������狭���I�ɉƂɖ߂�
		print qq|<form method="$method" action="$script">|;
		print qq|<input type="hidden" name="id" value="$id" /><input type="hidden" name="pass" value="$pass" />|;
		print qq|<input type="submit" value="�߂�" /></form>|;
	}

	open my $fh, "< $this_file" or &error("$this_file�t�@�C�����ǂݍ��߂܂���");
	my $line = <$fh>;
	close $fh;
	
	my %datas = ();
	for my $hash (split /<>/, $line) {
		my($k, $v) = split /;/, $hash;
		$datas{$k} = $v;
	}
	
	print qq|<h2>$m{home}�̃v���t�B�[��</h2><table class="table2" cellpadding="3" width="440">|;
	for my $profile (@profiles) {
		next if $datas{$profile->[0]} eq '';
		
		# http://�Ȃ�I�[�g�����N
		$datas{$profile->[0]} =~ s/([^=^\"]|^)(https?\:[\w\.\~\-\/\?\&\=\@\;\#\:\%]+)/$1<a href=\"link.cgi?$2\" target=\"_blank\">$2<\/a>/g;
		
		print qq|<tr><th align="left">$profile->[1]</th></tr><tr><td>$datas{$profile->[0]}</td></tr>|;
	}
	print qq|</table>|;
}


#================================================
sub write_form {
	my %datas = ();
	open my $fh, "< $this_file" or &error("$this_file�t�@�C�����ǂݍ��߂܂���");
	my $line = <$fh>;
	close $fh;
	for my $hash (split /<>/, $line) {
		my($k, $v) = split /;/, $hash;
		$datas{$k} = $v;
	}

	print qq|$m�̃v���t�B�[���F�S�p80����(���p160)�܂�<br />|;
	print qq|<form method="$method" action="$script"><input type="hidden" name="mode" value="write_exe">|;
	print qq|<table class="table2" cellpadding="3" width="440">|;
	for my $profile (@profiles) {
		print qq|<tr><th align="left">$profile->[1]</th></tr><tr><td><input type="text" name="$profile->[0]" value="$datas{$profile->[0]}" class="text_box_b"></td></tr>|; 
	}
	print qq|</table><input type="hidden" name="id" value="$id"><input type="hidden" name="pass" value="$pass">|;
	print qq|<p><input type="submit" value="�ύX����" class="button1"></p></form>|;
}

sub write_exe {
	my %datas = ();
	open my $fh, "+< $this_file" or &error("$this_file�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	my $line = <$fh>;
	for my $hash (split /<>/, $line) {
		my($k, $v) = split /;/, $hash;
		$datas{$k} = $v;
	}
	
	my $is_rewrite = 0;
	for my $profile (@profiles) {
		unless ($in{$profile->[0]} eq $datas{$profile->[0]}) {
			&error("$profile->[1] �ɕs���ȕ���( \;<> )���܂܂�Ă��܂�")	if $in{$profile->[0]} =~ /[;<>]/;
			&error("$profile->[1] �͑S�p80(���p160)�����ȓ��ł�")			if length($in{$profile->[0]}) > 160;
			$datas{$profile->[0]} = $in{$profile->[0]};
			$is_rewrite = 1;
		}
	}
	if ($is_rewrite) {
		my $new_line = '';
		while ( my($k, $v) = each %datas ) {
			$new_line .= "$k;$v<>";
		}
		
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh $new_line;
		close $fh;
		
		print '�v���t�B�[����ύX���܂���';
	}
	else {
		close $fh;
	}
	
	&view_profile;
}


1; # �폜�s��
