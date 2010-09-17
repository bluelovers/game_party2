#=================================================
# �r�炵�Ǖ� Created by Merino
#=================================================
# �ꏊ��
$this_title = '�r�炵�Ǖ��R�m�c';

# NPC��
$npc_name   = '@�Ǖ��R�m';

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$logdir/exile";

# �w�i�摜
$bgimg   = "$bgimgdir/exile.gif";

# ��������f�������\���҂ւ̍S������(��)
$penalty_day = 25;

# �Ǖ��ɕK�v�ȕ[��
$need_vote = 40;

# 1�l���Ǖ��\���ł�����x(�\�����̂���������ƍēx�\���\)
$max_violator = 1;

# �\���������֎~����(��)�B�N�������[���s���Ă��炱�̎��Ԉȓ��͎������ł��Ȃ��B
$c_hour = 3;


#=================================================
# �͂Ȃ����t
#=================================================
@words = (
	"�����͍r�炵�Ǖ��R�m�c�I�r�炵��s���v���C���[�������܂��Ă���I",
	"�r�炵��s���v���C���[�Ȃǂ�Ǖ����āA�y����������낤�I",
	"�r�炵�����������炱���ŒǕ����[�����Ă���I�r�炵�̂��Ȃ��y�������͂��O�B�������Ă����̂��B",
	"�r�炵�̔����ɑ΂��Ĕ������Ă͂����Ȃ��B����̔������y���ނ̂��r�炵�Ȃ̂��B��������Ԍ��ʓI���B",
	"�r�炵�̕s���Ȍ��t�ɕs���Ȍ��t�ŕԂ��Ă��܂��̂́A�r�炵�ƈꏏ�ɍr�炵�Ă���̂Ɠ������Ƃ��B",
	"����I�ɂȂ��Ă���Ƃ��́A�N�[���ɂȂ�I��ÂȎ��������������f�����邱�Ƃ��ł���͂����B",
	"�Ȃ�ƂȂ����J���Ȃǂ̊���I�Ȕ��f�Ō�����Ǖ��\\���������ꍇ�A�\\���҂��t�ɔ����󂯂邱�ƂɂȂ邼�B",
	"�����ɕK�v�ȕ[����$need_vote�[�K�v���I",
	"���[�ł���̂́A�]�E�񐔂��P��ȏ�̃v���C���[�݂̂��I",
);


#=================================================
# �ǉ��A�N�V����
#=================================================
push @actions, '���ق�';
push @actions, '���񂹂�';
push @actions, '�͂񂽂�';
$actions{'���ق�'} = sub{ &tuihou; }; 
$actions{'���񂹂�'} = sub{ &sansei; }; 
$actions{'�͂񂽂�'} = sub{ &hantai; }; 


#=================================================
# �����ق�
#=================================================
sub tuihou {
	my $target = shift;
	my($bad_name, $because) = split /����䂤&gt;/, $target;

	if ($bad_name eq '' || $because eq '') {
		$mes = "�w�����ق�>����������䂤>�������x�������ɂ͍r�炵�̖��O�A�������ɂ͂Ȃ��Ǖ��������̂��̗��R�������Ă���";
		return;
	}

	if ($m{job_lv} < 1) {
		$mes = "���]�E�̕��́A�\\�����邱�Ƃ͂ł��܂���";
		return;
	}
	elsif ($bad_name eq $m) {
		$mes = "�������g��\\�����邱�Ƃ͂ł��܂���";
		return;
	}

	my $yid = unpack 'H*', $bad_name;
	if (!-d "$userdir/$yid") {
		$mes = "$bad_name�Ƃ����v���C���[�͑��݂��܂���";
		return;
	}
	
	my %sames = ();
	my @lines = ();
	open my $fh, "+< $logdir/violator.cgi" or &error("$logdir/violator.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($name, $violator, $message, $yess, $noss) = split /<>/, $line;
		if ($violator eq $bad_name) {
			$mes = "$bad_name�͂��łɒǕ��\\������Ă��܂�";
			return;
		}
		elsif (++$sames{$name} > $max_violator) {
			$mes = "�\\�������Ǖ��҂̔�����҂��Ă�������";
			return;
		}
		
		push @lines, $line;
	}
	push @lines, "$m<>$bad_name<>$because<>$m,<><>\n";
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	$npc_com = qq|<span class="damage">$bad_name��Ǖ��҃��X�g�ɒǉ����Ă��������B������������̂�҂āI</span>|;
	&write_news(qq|<span class="damage">$m��$bad_name��$because�̗��R�ŒǕ��\\�����܂���</span>|);
}

#=================================================
# �����񂹂����͂񂽂�
#=================================================
sub sansei { &vote('yes', shift); }
sub hantai { &vote('no',  shift); }
sub vote {
	my($vote, $target) = @_;
	
	if ($m{job_lv} < 1) {
		$mes = "���]�E�̕��́A���[���邱�Ƃ͂ł��܂���";
		return;
	}
	
	my @lines = ();
	my $p = '';
	open my $fh, "+< $logdir/violator.cgi" or &error("$logdir/violator.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($name, $violator, $message, $yess, $noss) = split /<>/, $line;
		my $y_c = split /,/, $yess;
		my $n_c = split /,/, $noss;
		$p .= qq|<hr>�\\���F$name / �Ǖ��F$violator / ���R�F$message<br /><span onclick="text_set('�����񂹂�>$violator ')">�^�� <b>$y_c</b> �[�F$yess</span>�@<span onclick="text_set('���͂񂽂�>$violator ')">���� <b>$n_c</b> �[�F$noss</span><br />\n|;
		next if $target eq '';

		# �Ǖ��\��������
		if ($name eq $m && $vote eq 'no') {
			my $ftime = (stat "$logdir/violator.cgi")[9];
			if ($ftime + $c_hour * 3600 > $time) {
				$mes = "���[�サ�΂炭�͎��������Ƃ͂ł��܂���";
				return;
			}
			else {
				$npc_com = "$violator�̒Ǖ��\\�����������܂���";
				&write_news(qq|<span class="revive">$m��$violator�̒Ǖ��\\�����������܂���</span>|);
				next;
			}
		}
		
		if ($target eq $violator) {
			if ($yess =~ /\Q$m,\E/ || $noss =~ /\Q$m,\E/) {
				$mes = "���łɒǕ����[�ɎQ�����Ă��܂�";
				return;
			}
			elsif ($violator eq $m) {
				$mes = "�\\������Ă���l�͓��[���邱�Ƃ͂ł��܂���";
				return;
			}
			my $yid = unpack 'H*', $violator;
			if (!-d "$userdir/$yid") {
				$npc_com = "$violator�Ƃ����v���C���[�͑��݂��܂���";
				next;
			}
			elsif ($vote eq 'yes') {
				++$y_c;
				# �Ǖ�
				if ($y_c >= $need_vote) {
					my %p = &get_you_datas($yid, 1);
					&add_black_list($p{host});
					&delete_guild_member($p{guild}, $p{name}) if $p{guild};
					&delete_directory("$userdir/$yid");
					&minus_entry_count;
					$npc_com = qq|<span class="die">�y�c���z�^�� $y_c �[ / ���� $n_c �[�B����� $violator�͗L�߁I�Ǖ��Ƃ���I�ȏ�I</span>|;
					&write_news(qq|<span class="die">�y�c���z�^�� $y_c �[ / ���� $n_c �[�B����� $violator�͗L�߂Ƃ��ĒǕ�����܂���</span>|);
				}
				else {
					push @lines, "$name<>$violator<>$message<>$m,$yess<>$noss<>\n";
					$npc_com = "$violator�̒Ǖ��F�^�� $y_c �[ / ���� $n_c �[";
				}
			}
			elsif ($vote eq 'no') {
				++$n_c;
				# �\���҂Ƀy�i���e�B
				if ($n_c >= $need_vote) {
					$pid = unpack 'H*', $name;
					&regist_you_data($name, 'sleep', $penalty_day * 24 * 3600) if -d "$userdir/$pid";
					$npc_com  = qq|<span class="revive">�y�c���z�^�� $y_c �[ / ���� $n_c�[�B����� $violator�͖��߁I</span>|;
					&write_news(qq|<span class="revive">�y�c���z�^�� $y_c �[ / ���� $n_c �[�B����� $violator�͖��߂ƂȂ�܂���</span>|);
					
					if ($name && $name !~ /^@/) {
						$npc_com .= qq|<span class="die">�\\���҂�$name�� $penalty_day���Ԃ̖���̌Y�Ƃ���I</span>|;
						&write_news(qq|<span class="die">�\\���҂�$name�� $penalty_day���Ԃ̖���̌Y�ƂȂ�܂���</span>|);
					}
					$npc_com .= "�ȏ�I</b>";
				}
				else {
					push @lines, "$name<>$violator<>$message<>$yess<>$m,$noss<>\n";
					$npc_com = "$violator�̒Ǖ��̎^�� $y_c �[ / ���� $n_c �[";
				}
			}
			else {
				push @lines, $line;
			}
		}
		else {
			push @lines, $line;
		}
	}
	if ($npc_com) {
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
	}
	else {
		$mes = qq|�Ǖ��Ґ\\�����X�g<br />$p|;
	}
	close $fh;
}




1; # �폜�s��
