#=================================================
# �]�E�� Created by Merino
#=================================================
# �ꏊ��
$this_title = '�_�[�}�̐_�a';

# NPC��
$npc_name   = '@�_��';

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$logdir/job_change";

# �w�i�摜
$bgimg   = "$bgimgdir/job_change.gif";

# ���������邱�Ƃœ]�E�\�ȐE��(�����ɋL������Ă��Ȃ��ꍇ�͓��������Ȃ�)
%lost_item_jobs = (
	'����'			=> 1,
	'�E��'			=> 1,
	'����'			=> 1,
	'���̂܂ˎm'	=> 1,
	'���E�m'		=> 1,
	'����߲�'		=> 1,
	'�ײ�'			=> 1,
	'ʸ�����'		=> 1,
	'��׺��'		=> 1,
	'����'			=> 1,
	'�����'			=> 1,
	'Ӱ���'			=> 1,
	'�ެ���װ'		=> 1,
	'�ټެ�'		=> 1,
	'�V�g'		=> 1,
	'���e�m'		=> 1,
	'�d��'			=> 1,
	'���ް��'		=> 1,
	'���'			=> 1,
	'�ް����'		=> 1,
	'�ײ�ײ�ް'		=> 1,
	'��׺��ײ�ް'	=> 1,
	'ȸ��ݻ�'		=> 1,
	'�ޯ�Ͻ��'		=> 1,
	'�ɺϽ��'		=> 1,
	'��޹Ͻ��'		=> 1,
	'���Ͻ��'		=> 1,
	'�޸�Ͻ��'		=> 1,
	'�����Ͻ��'		=> 1,
	'��˰۰'		=> 1,
	'���˰۰'		=> 1,
);

#=================================================
# ���͂Ȃ��̉�b
#=================================================
@words = (
	"�悭�����I���̃_�[�}�_�a�ł͂���̐E�Ƃ�ς��邱�Ƃ��ł��邼",
	"�ӂނӂށB�ǂ̐E�Ƃɂ��悤���܂���Ă���̂����",
	"�]�E������ƍ��̃X�e�[�^�X�������ɂȂ��Ă��܂���",
	"�E�Ƃ͏d�v���Ⴉ���[���l����̂����",
	"�]�E�A�C�e���������Ă���΁A���ʂȐE�Ƃɓ]�E���邱�Ƃ��ł��邼",
	"$m�͒j�O�����猕�m�Ȃ񂩂ǂ������H",
	"$m�͂������~�����Ǝv���Ă���ȁH����Ȃ珤�l�ɂȂ�Ȃ���",
	"$m�̓����X�^�[�ƒ��ǂ��Ȃ肽���Ǝv���Ă���ȁH����Ȃ疂���g���ɂȂ�Ȃ���",
	"$m�͖����n�ɂȂ肽���Ǝv���Ă���ȁH����Ȃ�m���ɂȂ�Ȃ���",
	"$m�͑���₨�󂪋C�ɂȂ��Ă���ȁH����Ȃ瓐���ɂȂ�Ȃ���",
	"$m�͒N���ɃC�^�Y���������Ǝv���Ă���ȁH����Ȃ�V�ѐl�ɂȂ�Ȃ���",
	"$m�̓��R���R�������̂��D������ȁH����Ȃ�r�����ɂȂ�Ȃ���",
	"$m�͍ŏI�I��$jobs[int(rand(@jobs))+1][1]��ڎw���Ɨǂ�����낧",
	"$m�Ɉ�Ԃ������肭��̂�$jobs[int(rand(@jobs))+1][1]�����",
	"�]�E����������������Ƃ����ċ����Ƃ͌����",
	"�ǂ�ȂɃX�L�����o���Ă��g�����Ȃ��Ȃ���Ӗ����Ȃ���",
	"�X�L���𑁂��o�������ꍇ�͑����]�E���I�X�X�����Ă���",
	"�X�e�[�^�X���グ�����ꍇ�́A�������̍����E�Ƃ�I�сA�Ȃ�ׂ��x���]�E����̂��R�c����",
	"���̐E�Ƃ̃X�L����S�ă}�X�^�[���Ă���]�E���Ă��A�������͂Ȃ��͂�����",
	"$m�̍��̓]�E�񐔂́c$m{job_lv}��B�ӂށA�Ȃ��Ȃ�����̂�",
	"�]�E�񐔂͖`���҂̏n���x�ł�����B�R��]�E������Ə��S�ґ��ƃ��x�����̂�",
	"�]�E�񐔂͖`���҂̏n���x�ł�����B10��ȏ�̓]�E�҂́A���̐��E���n�m���Ă���x�e��������̂�",
);

sub shiraberu_npc {
	$mes = "�����X�^�[���ސ� $m{kill_m}��<br />�v���C���[���ސ� $m{kill_p}��<br />����������� $m{mao_c}��<br />���󂵂��� $m{hero_c}��<br />�J�W�m������ $m{cas_c}��";
}


#=================================================
# ��ʈ�ԏ�ɕ\��
#=================================================
sub header_html {
	print qq|<div class="mes">�y$this_title�z $jobs[$m{job}][1] $e2j{sp} <b>$m{sp}</b>|;
	print qq| / $jobs[$m{old_job}][1] $e2j{sp} <b>$m{old_sp}</b>| if $m{old_job};
	for my $k (qw/lv mhp mmp at df ag/) {
		print qq| / $e2j{$k} <b>$m{$k}</b>|;
	}
	print qq| / E�F$ites[$m{ite}][1]| if $m{ite};
	print qq|</div>|;
}

#=================================================
# �ǉ��A�N�V����
#=================================================
push @actions, '�Ă񂵂傭';
$actions{'�Ă񂵂傭'} = sub{ &tensyoku }; 

#=================================================
# ���Ă񂵂傭
#=================================================
sub tensyoku {
	my $target = shift;
	
	if ($m{lv} < 20) {
		$mes = "�]�E����ɂ̓��x�����Q�O�ȏ�K�v����";
		return;
	}
	
	my $p = '';
	for my $i (0 .. $#jobs) {
		next unless &{ $jobs[$i][7] }; # �]�E����������ꍇ�A�������Ă��邩
		if ($target eq $jobs[$i][1]) {
			# �������]�E(���҂������ʏ���)
			if (defined $lost_item_jobs{$target}) {
				# �A�C�e������Ȃ�����
				unless (&_is_need_job($i) || (($target eq '����' || $target eq '�ެ���װ') && ($jobs[$m{job}][1] eq '�V�ѐl' || $jobs[$m{old_job}][1] eq '�V�ѐl' )) ) {
					$npc_com .= "$ites[$m{ite}][1]���g���܂����I ";
					$m{ite} = 0;
				}
			}
			
			&write_memory("$jobs[$m{job}][1]����$jobs[$i][1]�ɓ]�E");
			&job_change($i);

			$npc_com .= "$m��I$target�ƂȂ�V���ȓ�����ނ��ǂ�";
			&regist_guild_data('point', 50) if $m{guild};
			return;
		}

		$p .= qq|<span onclick="text_set('���Ă񂵂傭>$jobs[$i][1] ')">$jobs[$i][1]</span> / |;
	}
	$mes = qq|�ǂ̐E�Ƃɓ]�E����̂���H<br />$p|;
	$act_time = 0;
}
# ------------------
# �]�E����
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
	if ($mastered_count eq $#jobs && !-f "$userdir/$id/comp_job_flag.cgi") { 
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
