#=================================================
# �a���菊 Created by Merino
#=================================================
# �ꏊ��
$this_title = '�t�H�g�R�����';

# NPC��
$npc_name   = '@ܺ��';

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$logdir/photo";

# �w�i�摜
$bgimg   = "$bgimgdir/photo.gif";

# �A���G���g���[(0:�s�\[���R���e�X�g�ɃG���g���[���Ă���ꍇ�́A����̃R���e�X�g�ɎQ���ł��Ȃ�],1:�\)
$is_renzoku_entry_contest = 0;


#=================================================
# ���͂Ȃ��̉�b
#=================================================
@words = (
	"�t�H�g�R���e�X�g�̉��A�����ăt�H�g�R�����ւ悤�����B������Î҂̃��R�[�����܂�",
	"�����ł́A$m���B�����X�N���[���V���b�g����������A�R���e�X�g�ɉ��債����ł��邴�܂�",
	"�R���e�X�g��ʓ��܎҂ɂ́A�S�[���h�Əܕi�����^����邴�܂�",
	"�R���e�X�g�P�ʂ̍�i�ɓ��[�����Q���҂ɂ������ȃ��_�����z���邴�܂�",
	"�t�H�g�R���ŏd�v�Ȃ̂́A�����ʂ��Ă��邩�͂������B�^�C�g����R�����g�Ȃǂ��d�v�ȃ|�C���g���܂�",
	"�����ŎB�����X�N���[���V���b�g��������������Ƃ��ł��邴�܂�",
	"�����B�邾���ł͂Ȃ��A�R�X�v��������F�X�ƍH�v���邱�Ƃ��厖���܂�",
	"�X�N���[���V���b�g�͍ő�$max_screen_shot���܂ŏ������邱�Ƃ��ł��邴�܂��B����ȏ�́A�������K�v�����邴�܂�",
);

#=================================================
# �ǉ��A�N�V����
#=================================================
push @actions, '�݂�';
push @actions, '����';
push @actions, '�Ƃ��Ђ傤';
push @actions, '����Ƃ�[';
$actions{'�݂�'}       = sub{ &miru }; 
$actions{'����'}       = sub{ &kesu }; 
$actions{'�Ƃ��Ђ傤'} = sub{ &touhyou }; 
$actions{'����Ƃ�['} = sub{ &entori  }; 


#=================================================
# ���݂�
#=================================================
sub miru {
	$mes = qq|<form action="screen_shot.cgi"><input type="hidden" name="path" value="$userdir/$id" /><input type="hidden" name="id" value="$id" /><input type="hidden" name="pass" value="$pass" /><input type="submit" value="$m�̃X�N���[���V���b�g" /></form>|;
}

#=================================================
# ������
#=================================================
sub kesu {
	my $target = shift;
	my $count = 0;
	my @lines = ();
	my $p = '';
	open my $fh, "+< $userdir/$id/screen_shot.cgi" or &error("$userdir/$id/screen_shot.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while ($line = <$fh>) {
		++$count;
		if ($target eq "$count����") {
			$mes = "$count���ڂ̃X�N���[���V���b�g���폜���܂������";
		}
		else {
			push @lines, $line;
			$p .= qq|<span onclick="text_set('������>$count���� ')">$count����<br>$line</span>|;
		}
	}
	if ($mes) {
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
		close $fh;
		return;
	}
	close $fh;

	$mes = qq|�ǂ̃X�N���[���V���b�g�������܂����H<br><div class="view" style="font-weight: normal; color: #FFF;">$p</div>|;
}

#=================================================
# ������Ƃ�[
#=================================================
sub entori {
	my $target = shift;
	my($photo, $ptitle) = split /�������߂�&gt;/, $target;
	
	if (!$is_renzoku_entry_contest && &is_entry_contest) {
		$mes = "�A���ŃR���e�X�g�ɃG���g���[���邱�Ƃ͂ł��܂���<br />����̃R���e�X�g�܂ł��҂���������";
		return;
	}
	
	my $entry_photo = '';
	my $count = 0;
	open my $fh2, "< $userdir/$id/screen_shot.cgi" or &error("$userdir/$id/screen_shot.cgi�t�@�C�����J���܂���");
	while ($line2 = <$fh2>) {
		$line2 =~ tr/\x0D\x0A//d;
		++$count;
		if ($photo eq "$count����") {
			$entry_photo = $line2;
			last;
		}
		$p .= qq|<span onclick="text_set('������Ƃ�[>$count���ځ������߂�>')">$count����<br>$line2</span>|;
	}
	close $fh2;
	
	unless ($entry_photo) {
		$mes = qq|�ǂ̍�i���G���g���[���܂����H<br><div class="view" style="font-weight: normal; color: #FFF;">$p</div>|;
		return;
	}

	$mes = "�薼�ɕs���ȋ󔒂��܂܂�Ă��܂�"					if $ptitle =~ /�@|\s/;
	$mes = "�薼�ɕs���ȕ���( ,;\"\'&<>\@ )���܂܂�Ă��܂�" 	if $ptitle =~ /[,;\"\'&<>\@]/;
	$mes = "�薼�ɕs���ȕ���( �� )���܂܂�Ă��܂�" 			if $ptitle =~ /��/;
	$mes = "�薼�͑S�p20����[���p40����]�܂łł�"				if length($ptitle) > 40;
	$mes = "�薼���L�����Ă�������"								unless $ptitle;
	return if $mes;

	open my $fh, "+< $logdir/contest_prepare.cgi" or &error("$logdir/contest_prepare.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	my $head_line = <$fh>;
	my($etime, $round) = split /<>/, $head_line;
	my @lines = ($head_line);
	while ($line = <$fh>) {
		my($stitle, $name, $guild, $vote, $comment, $vote_names, $content) = split /<>/, $line;
		
		if ($name eq $m) {
			$mes = "�y$stitle�z�Ƃ�����i�ŁA���łɃG���g���[�ς݂ł�";
			return;
		}
		elsif ($ptitle eq $stitle) {
			$mes = "�����^�C�g���̍�i�����łɃG���g���[����Ă��܂�";
			return;
		}
		push @lines, $line;
	}
	push @lines, "$ptitle<>$m<>$m{guild}<>0<><><>$entry_photo<>\n";
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;

	$npc_com .= "��$round��t�H�g�R���e�X�g�Ɂw$ptitle�x�Ƃ����薼�ŃG���g���[���܂���";
}
sub is_entry_contest {
	open my $fh, "< $logdir/contest_entry.cgi" or &error("$logdir/contest_entry.cgi�t�@�C�����ǂݍ��߂܂���");
	my $head_line = <$fh>;
	while (my $line = <$fh>) {
		my($stitle, $name, $guild, $vote, $comment, $vote_names, $content) = split /<>/, $line;
		return 1 if $name eq $m;
	}
	close $fh;
	return 0;
}


#=================================================
# ���Ƃ��Ђ傤
#=================================================
sub touhyou {
	my $target = shift;
	my($ptitle, $pcom) = split /�����߂��&gt;/, $target;

	my $count = 0;
	my $p = '';
	open my $fh, "+< $logdir/contest_entry.cgi" or &error("$logdir/contest_entry.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	my $head_line = <$fh>;
	my($etime, $round) = split /<>/, $head_line;
	my @lines = ($head_line);
	while ($line = <$fh>) {
		my($stitle, $name, $guild, $vote, $comment, $vote_names, $content) = split /<>/, $line;
		
		if ($ptitle eq $stitle) {
			if (&add_vote_name) {
				$mes = "��$round��̃t�H�g�R���e�X�g�ɂ́A���łɓ��[�ς݂ł�";
				return;
			}
			else {
				++$vote;
				$vote_names .= "$m,";
				$comment .= "$m�w$pcom�x," if $pcom;
				$mes = "$stitle�ɓ��[���܂���";
			}
		}
		else {
			++$count;
			$p .= qq|<hr color="#CCCC00"/><span onclick="text_set('���Ƃ��Ђ傤>$stitle�����߂��>')"><span class="strong">��iNo.$count�w$stitle�x</span><br>$content</span>|;
		}
		push @lines, "$stitle<>$name<>$guild<>$vote<>$comment<>$vote_names<>$content<>\n";
	}
	if ($mes) {
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
		close $fh;
		return;
	}
	close $fh;

	$mes = qq|�ǂ̍�i�ɓ��[���܂����H<br><div class="view" style="font-weight: normal; color: #FFF;">$p</div>|;
}
# ------------------
sub add_vote_name {
	open my $fh, "+< $logdir/contest_vote_name.cgi" or &error("$logdir/contest_vote_name.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	my $line = <$fh>;
	$line =~ tr/\x0D\x0A//d;
	if ($line =~ /,\Q$m{name}\E,/) {
		close $fh;
		return 1;
	}
	$line .= "$m{name},";
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh $line;
	close $fh;
	return 0;
}


1; # �폜�s��
