#=================================================
# �V�� Created by Merino
#=================================================
# �ꏊ��
$this_title = "�V�E";

# NPC��
$npc_name   = '@�_';

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$logdir/god";

# �w�i�摜
$bgimg   = "$bgimgdir/god.gif";

# �肢��
@prizes = (
# 	['�˂������Ɩ�',				'�⑫����',			sub{ ����($mes�ɉ�������������ƃL�����Z��)  }],	
	['�����Ȃ肽��',				'�S�ð�� 40 ����',	sub{ for my $k (qw/mhp mmp at df ag/) { $m{$k}+=40; };	}],
	['�X�L�����o������',			'Sp 50 ����',		sub{ $m{sp}     += 50;		}],
	['�������ق���',				'10 ��G',			sub{ $m{money}  += 100000;		}],
	['�J�W�m�R�C�����ق���',		'5 ����',			sub{ $m{coin}   += 50000;		}],
	['�����ȃ��_�����ق���',		'20 ��',			sub{ $m{medal}  += 20;		}],
	['���������ق���',				'1000 ��',			sub{ $m{coupon} += 1000;	}],
	['�M���h�����N����������',		'1000 �߲��',		sub{ return unless $m{guild}; &regist_guild_data('point', 1000, $m{guild});	}],
	['�M���h���S�[�W���X�ɂ�����',	'�M���h���c',		sub{ return unless $m{guild}; my $gid = unpack 'H*', $m{guild}; return unless -f "$guilddir/$gid/log_member.cgi"; open my $fh, ">> $guilddir/$gid/log_member.cgi" or &error("$guilddir/$gid/log_member.cgi�t�@�C�����J���܂���"); print $fh "$time<>1<>������<>0<>etc/win_medal3.gif<>$npc_color<>\n"; close $fh; &regist_guild_data('bgimg', 'god.gif', $m{guild});		}],
	['���C�����ς��ɂȂ肽��',		'��J�x -150 %',	sub{ $m{tired} -= 150;		}],
	['�V�����`���ꏊ�ɍs������',	'�S�I�[�u',			sub{ $m{orb}    = 'byrpgs';		}],
	['�V���l�ɂȂ肽��',			'�]�E',				sub{ if ($m{job} eq '70' || $m{old_job} eq '70') { $mes="�ӂށB���ł�$m�͓V���l�����c"; return; }; &job_change(70);		}],
	['�V���E�̐_�ɂȂ肽��',		'�����̉Ƃ��c',		sub{ $m{icon} = 'chr/052.gif'; &copy("$bgimgdir/god.gif", "$userdir/$id/bgimg.gif");		}],
	['�I���e�K�𐶂��Ԃ炵��',		'�����̉ƂɁc',		sub{ open my $fh, ">> $userdir/$id/home_member.cgi" or &error("$userdir/$id/home_member.cgi�t�@�C�����J���܂���"); print $fh "$time<>1<>��ö�<>0<>chr/029.gif<>$npc_color<>\n"; close $fh;		}],
	['�L����������',				'�����̉ƂɁc',		sub{ open my $fh, ">> $userdir/$id/home_member.cgi" or &error("$userdir/$id/home_member.cgi�t�@�C�����J���܂���"); if (rand(2) < 1) { print $fh "$time<>1<>���L<>0<>chr/030.gif<>$npc_color<>\n"; }else{ print $fh "$time<>1<>���L<>0<>chr/031.gif<>$npc_color<>\n"; }; close $fh;		}],
	['�G�b�`�Ȗ{���ق���',			'�A�C�e��',			sub{ &send_item($m, 3, 58);		}],
	['�B��ڼ�߂��ق���',			'�A�C�e��',			sub{ &send_item( $m, 3, int(rand(2)+128) );	}],
	['�f�G�ȗ��l���ق���',			'���l���c',			sub{ $mes = '����͖����Ȋ肢���c�B�A�h�o�C�X�Ƃ��Ă͐ϋɓI�ɃA�s�[������̂��c';		}],

	# �V�[�N���b�g
	['���C�h���ق�����',			'�����b�W',			sub{ open my $fh, ">> $userdir/$id/home_member.cgi" or &error("$userdir/$id/home_member.cgi�t�@�C�����J���܂���"); print $fh "$time<>1<>Ҳ��<>0<>chr/026.gif<>$npc_color<>\n"; close $fh;		}],
);

# �L����������
# װЧ����������
# �ς�

#=================================================
# ������ׂ�>NPC
#=================================================
sub shiraberu_npc {
	$mes = qq|<span onclick="text_set('���˂���>���C�h���ق�����')">$npc_name�u�{���̊肢�͎����̗͂Ŋ�����̂��c�v</span>|;
}

#=================================================
# �͂Ȃ����t
#=================================================
@words = (
	"$m��B�悭�������܂ł����B$m�̊肢������������Ă�낤",
);

#=================================================
# �ǉ��A�N�V����
#=================================================
push @actions, '�˂���';
$actions{ '�˂���' } = sub{ &negau };

#=================================================
# �X�e�[�^�X�\��
#=================================================
sub header_html {
	print qq|<div class="mes">�y$this_title�z</div>|;
}

#=================================================
# ���˂���
#=================================================
sub negau {
	my $target = shift;

	my $p = qq|<table class="table1">|;
	for my $i (0 .. $#prizes-1) {
		if ($prizes[$i][0] eq $target) {
			&{ $prizes[$i][2] };
			return if $mes;
			
			$npc_com = "�ӂށB$m�̊肢�́u$prizes[$i][0]�v���ȁB<br />$m�̊肢�����������c�B�@�����΂܂������邾�낤�c�B����΂��c";
			$m{lib} = 'home';
			&write_memory("$m�̊肢�w$prizes[$i][0]�x�������Ă��炤");
			return;
		}
		$p .= qq|<tr onclick="text_set('���˂���>$prizes[$i][0] ')"><td>$prizes[$i][0]($prizes[$i][1])</td></tr>|;
	}
	$p  .= qq|</table>|;
	$mes = qq|�肢������������Ă�낤�c<br />$p|;
	$act_time = 0;
}

# ------------------
# �]�E���� ./lib/job_change.cgi����R�s�[
sub job_change {
	my $job = shift;
	
	&add_all_job_master;
	my $mastered_point = &add_job_master($job);
	
	# �Ⴄ�E�Ƃɓ]�E�����ꍇ�̏���(�����E�Ƃɓ]�E�����ꍇ�́A���x���ƃX�e�[�^�X�������邾��)
	unless ($m{job} eq $job) {
		my $buf_sp  = $m{old_sp};
		$m{old_sp}  = $m{sp};
		$m{sp}      = $job eq $m{old_job} ? $buf_sp : $mastered_point; # �O�E�Ƃɓ]�E����ꍇ�͑O�E�Ƃ�SP
		$m{old_job} = $m{job};
		$m{job}     = $job;
		$m{icon}    = "job/$m{job}_$m{sex}.gif";
	}
	
	# �X�e�[�^�X�_�E��
	for my $k (qw/mhp mmp at df ag/) {
		$m{$k} = int($m{$k} * 0.5); 
		$m{$k} = 10 if $m{$k} < 10;
	}
	
	$m{hp} = $m{mhp};
	$m{mp} = $m{mmp};
	$m{lv}  = 1;
	$m{exp} = 0;
	$m{job_lv}++;
}

# �K���W���u
sub add_job_master {
	my $job = shift;

	require "./lib/_skill.cgi";
	my @skills = &{ 'skill_'.$m{job} };

	my $mastered_job_sp = 0;
	my $mastered_count = 0;
	my $is_find = 0;
	my @lines = ();
	open my $fh, "+< $userdir/$id/job_master.cgi" or &error("$userdir/$id/job_master.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($job_no, $job_sex, $job_point, $is_master) = split /<>/, $line;

		if ($m{job} eq $job_no) {
			$is_find = 1;
			if (!$is_master && $m{sp} >= $skills[-1][0]) {
				$is_master = 1;
				$com .= qq|<span class="comp">$m�� <b>$jobs[$m{job}][1]</b> ���}�X�^�[���܂����I</span>|;
				&write_memory("<b>�� $jobs[$m{job}][1] Job Master! ��</b>");
			}
			push @lines, "$m{job}<>$m{sex}<>$m{sp}<>$is_master<>\n";
		}
		elsif ($job eq $job_no && $is_master) {
			$mastered_job_sp = $job_point;
			push @lines, $line;
		}
		else {
			push @lines, $line;
		}
		$mastered_count++ if $is_master;
	}
	unless ($is_find) {
		my $is_master = 0;
		
		if ($m{sp} >= $skills[-1][0]) {
			$is_master = 1;
			$com .= qq|<span class="comp">$m�� <b>$jobs[$m{job}][1]</b> ���}�X�^�[���܂����I</span>|;
			&write_memory("<b>�� $jobs[$m{job}][1] Job Master! ��</b>");
		}
		push @lines, "$m{job}<>$m{sex}<>$m{sp}<>$is_master<>\n";
	}
	@lines = map { $_->[0] } sort { $a->[1] <=> $b->[1] } map { [$_, split /<>/] } @lines;
	
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	# �S�W���u�R���v���[�g
	if ($mastered_count eq $#jobs-1 && !-f "$userdir/$id/comp_job_flag.cgi") { 
		open my $fh2, "> $userdir/$id/comp_job_flag.cgi" or &error("$userdir/$id/comp_job_flag.cgi�t�@�C�����J���܂���");
		close $fh2;
		
		&write_legend('comp_job');
		&write_memory(qq|<span class="comp">All Job Complete!!</span>|);
		&write_news(qq|<span class="comp">$m���S�Ă̐E�Ƃ��}�X�^�[���܂����I</span>|);
		$com .= qq|<div class="comp">$m�� <b>�S�W���u</b> ���R���v���[�g���܂����I</div>|;
	}
	
	return $mastered_job_sp;
}

# �S�̂̓]�E�̌X��
sub add_all_job_master {
	my $is_find = 0;
	
	my $add_point = int($m{lv} * 0.5);
	
	my @lines = ();
	open my $fh, "+< $logdir/job_ranking.cgi" or &error("$logdir/job_ranking.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	my $totale_point = <$fh>;
	$totale_point =~ tr/\x0D\x0A//d;
	$totale_point += $add_point;
	while (my $line = <$fh>) {
		my($job_no, $men_point, $female_point, $job_point) = split /<>/, $line;
		if ($m{job} eq $job_no) {
			$is_find = 1;
			
			if ($m{sex} eq 'm') {
				$men_point += $add_point;
			}
			else {
				$female_point += $add_point;
			}
			$job_point += $add_point;
		}
		push @lines, "$job_no<>$men_point<>$female_point<>$job_point<>\n";
	}
	unless ($is_find) {
		my $job_sex = $m{sex} eq 'm' ? "$add_point<>0" : "0<>$add_point";
		push @lines, "$m{job}<>$job_sex<>$add_point<>\n";
	}

	@lines = map { $_->[0] } sort { $b->[4] <=> $a->[4] } map { [$_, split /<>/] } @lines;
	unshift @lines, "$totale_point\n";
	
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}

1; # �폜�s��
