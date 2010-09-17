#!/usr/local/bin/perl
require 'config.cgi';
require '_side_menu.cgi';
#================================================
# �R���e�X�g Created by Merino
# past �ߋ�, prepare �G���g���[��t(���̃R���e�X�g), entry ���R���e�X�g
#================================================
# �R���e�X�g���{����(��)
$contest_cycle_day = 10;

# �Œገ�s�l��(�l)
$min_entry_contest = 5;

# �R���e�X�g�̏܋�
@prizes = (
# ���������ف@�܋��@�M���h�|�C���g
	[10,	15000,	700],
	[6,		 7000,	300],
	[3,		 3000,	100],
);

#================================================
&decode;
&header;
&header_contest;
if    ($in{mode} eq 'past')   { &past }
elsif ($in{mode} eq 'legend') { &legend }
else { &now_contest }
&side_menu($contents);
&footer;
exit;
#================================================
# �R���e�X�g�pheader
#================================================
sub header_contest {
	$contents .= '<p>';
	$contents .= $in{mode} eq 'legend' ? qq|<a href="contest.cgi">���݂̃R���e�X�g</a> / <a href="contest.cgi?mode=past">�O��̃R���e�X�g</a> / �a������|
			   : $in{mode} eq 'past'   ? qq|<a href="contest.cgi">���݂̃R���e�X�g</a> / �O��̃R���e�X�g / <a href="contest.cgi?mode=legend">�a������</a>|
			   :                         qq|���݂̃R���e�X�g / <a href="contest.cgi?mode=past">�O��̃R���e�X�g</a> / <a href="contest.cgi?mode=legend">�a������</a>|
			   ;
	$contents .= '</p>';
}

#================================================
# �a������
#================================================
sub legend {
	$contents .= qq|<h2>�a������</h2><hr />|;
	open my $fh, "< $logdir/contest_legend.cgi" or &error("$logdir/contest_legend.cgi�t�@�C�����ǂݍ��߂܂���");
	while (my $line = <$fh>) {
		my($round, $stitle, $name, $guild, $vote, $ldate, $photo) = split /<>/, $line;
		$name .= "��$guild" if $guild;
		$contents .= qq|<h3>��$round��D�G��i�w$stitle�x <b>$vote</b>�[ ��F$name <span class="text_small">($ldate)</span></h3>$photo<br />|;
	}
	close $fh;
}

#================================================
# �O��̃R���e�X�g����
#================================================
sub past {
	if (-s "$logdir/contest_past.cgi") {
		my $count = 1;
		open my $fh, "< $logdir/contest_past.cgi" or &error("$logdir/contest_past.cgi�t�@�C�����ǂݍ��߂܂���");
		my $head_line = <$fh>;
		my($etime, $round) = split /<>/, $head_line;
		$contents .= qq|<h2>��$round�񌋉ʔ��\\</h2> ���P�ʂ̍�i�ɓ��[���ꂽ�l�ɂ͏����ȃ��_���������܂�<hr />|;
		while (my $line = <$fh>) {
			my($stitle, $name, $guild, $vote, $comment, $vote_names, $photo) = split /<>/, $line;
			$name .= "��$guild" if $guild;
			$comment  .= qq|<hr />| if $comment;
			$contents .= qq|<h3>$count�� <b>$vote</b>�[ �薼�w$stitle�x ��:$name</h3>$photo$comment<br />\n|;
			++$count;
		}
		close $fh;
	}
	else {
		$contents .= qq|<p>�O��̃R���e�X�g�͊J�Â���Ă��܂���</p>|;
	}
}

#================================================
# ���݂̃R���e�X�g
#================================================
sub now_contest {
	my $count = 0;
	my $sub_mes = '';
	open my $fh, "< $logdir/contest_entry.cgi" or &error("$logdir/contest_entry.cgi�t�@�C�����ǂݍ��߂܂���");
	my $head_line = <$fh>;
	my($etime, $round) = split /<>/, $head_line;
	while (my $line = <$fh>) {
		my($stitle, $name, $guild, $vote, $comment, $vote_names, $photo) = split /<>/, $line;
		$sub_mes .= qq|<h3>�薼�w$stitle�x</h3>$photo<br />\n|;
		++$count;
	}
	close $fh;
	my($min,$hour,$day,$month) = (localtime($etime))[1..4];
	++$month;
	
	# �ߋ��R���e�X�g�폜�����R���e�X�g���ߋ��R���e�X�g�����R���e�X�g�����R���e�X�g�ɂ��鏈��
	if ($time > $etime) {
		$contents .= qq|<h2>��$round��t�H�g�R���e�X�g</h2>|;
		$contents .= qq|<p>�c�W�v�������c</p>|;

		if ($count > 0) {
			&_send_goods_to_creaters if -s "$logdir/contest_past.cgi";
			&_result_contest;
		}
		&_start_contest;
	}
	elsif ($min_entry_contest > $count) {
		$contents .= qq|<h2>��$round��t�H�g�R���e�X�g</h2>|;
		$contents .= qq|�y���[�I�����E����R���e�X�g $month��$day��$hour��$min���z<hr />|;
		$contents .= qq|���e��i���W�܂��Ă��Ȃ����ߊJ�É������ł�<br />|;
	}
	else {
		$contents .= qq|<h2>��$round��t�H�g�R���e�X�g</h2>|;
		$contents .= qq|�y���[�I�����E����R���e�X�g $month��$day��$hour��$min���z<hr />|;
		$contents .= $sub_mes;
	}
}


# ------------------
# �ߋ��̃R���e�X�g��i����҂ɕԕi���t�@�C���E�t�H���_�폜
sub _send_goods_to_creaters {
	my $count = 0;
	open my $fh, "+< $logdir/contest_past.cgi" or &error("$logdir/contest_past.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	my $head_line = <$fh>;
	my($etime, $round) = split /<>/, $head_line;
	while (my $line = <$fh>) {
		my($stitle, $name, $guild, $vote, $comment, $vote_names, $content) = split /<>/, $line;
		++$count;
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	close $fh;
}
# ------------------
# ���ʂ��W�v���ĉߋ��R���e�X�g�Ƀ��l�[��
sub _result_contest {
	my @lines = ();
	open my $fh, "+< $logdir/contest_entry.cgi" or &error("$logdir/contest_entry.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	my $head_line = <$fh>;
	while (my $line = <$fh>) {
		push @lines, $line;
	}
	
	# ��������sort
	@lines = map { $_->[0] } sort { $b->[4] <=> $a->[4] } map { [$_, split/<>/] } @lines;
	
	unshift @lines, $head_line;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	rename "$logdir/contest_entry.cgi", "$logdir/contest_past.cgi" or &error("Cannot rename $logdir/contest_entry.cgi to $logdir/contest_past.cgi");
	
	# ��i���R�s�[���ēa������
	&__copy_goods_to_legend($head_line, $lines[1]) if @lines > $min_entry_contest;
	
	&__send_prize(@lines);
}

# ��ʂɏܕi����
sub __send_prize {
	my @lines = @_;

	my $head_line = shift @lines;
	my($etime, $round) = split /<>/, $head_line;
	
	my $count = 1;
	for my $line (@lines) {
		my($stitle, $name, $guild, $vote, $comment, $vote_names, $content) = split /<>/, $line;
		
		if ($count eq '1') {
			for my $vname (split /,/, $vote_names) {
				next unless $vname;
				&send_item($vname, 3, 23, '�t�H�g�R���e�X�g');
			}
		}
		
		my $send_id = unpack 'H*', $name;
		if (-f "$userdir/$send_id/depot.cgi") {
			open my $fh, ">> $userdir/$send_id/depot.cgi";
			for my $i (1..$prizes[$count-1][0]-1) {
				print $fh "3<>23<>\n";
			}
			close $fh;
			
			&send_item($vname, 3, 23, '�t�H�g�R���e�X�g')
		}
		&send_money($name, $prizes[$count-1][1], "��$round��t�H�g�R���e�X�g$count�ʂ̏܋�");
		&write_memory("����$round��t�H�g�R���e�X�g$count�ʓ��܁�", $name);
		&regist_guild_data('point', $prizes[$count-1][2], $guild) if $guild;
		&write_news(qq|<span class="comp">����$round��t�H�g�R���e�X�g$count�� $name��</span>|);
		last if ++$count > @prizes;
	}
}

sub __copy_goods_to_legend {
	my($head_line, $line) = @_;
	my($etime, $round) = split /<>/, $head_line;
	my($stitle, $name, $guild, $vote, $comment, $vote_names, $content) = split /<>/, $line;
	
	my @lines = ();
	open my $fh, "+< $logdir/contest_legend.cgi" or &error("$logdir/contest_legend.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		push @lines, $line;
		last if @lines > $max_log - 1;
	}
	unshift @lines, "$round<>$stitle<>$name<>$guild<>$vote<>$date<>$content<>\n";
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}

# ------------------
# ���R���e�X�g�����R���e�X�g�Ƀ��l�[��
sub _start_contest {
	my $end_time = $time + 24 * 60 * 60 * $contest_cycle_day;

	my @lines = ();
	open my $fh, "+< $logdir/contest_prepare.cgi" or &error("$logdir/contest_prepare.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	my $head_line = <$fh>;
	my($etime, $round) = split /<>/, $head_line;
	push @lines, "$end_time<>$round<>\n";
	while (my $line = <$fh>) {
		push @lines, $line;
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;

	# �G���g���[�����Œ�G���g���[���𒴂����ꍇ�͊J��
	if ( @lines > $min_entry_contest ) {
		rename "$logdir/contest_prepare.cgi", "$logdir/contest_entry.cgi" or &error("Cannot rename $logdir/contest_prepare.cgi to $logdir/contest_entry.cgi");
		
		# ���[/�����[���ʃt�@�C����������
		open my $fh3, "> $logdir/contest_vote_name.cgi" or &error("$logdir/contest_vote_name.cgi�t�@�C�������܂���");
		print $fh3 ",";
		close $fh3;
		
		# ���R���e�X�g��������
		++$round;
	 	open my $fh2, "> $logdir/contest_prepare.cgi" or &error("$logdir/contest_prepare.cgi�t�@�C�����J���܂���");
		print $fh2 "$end_time<>$round<>\n";
		close $fh2;
		chmod $chmod, "$logdir/contest_prepare.cgi";
	}
	else {
		# ���Ԃ�����
	 	open my $fh2, "> $logdir/contest_entry.cgi" or &error("$logdir/contest_entry.cgi�t�@�C�����J���܂���");
		print $fh2 "$end_time<>$round<>\n";
		close $fh2;
		chmod $chmod, "$logdir/contest_entry.cgi";
	}
}


