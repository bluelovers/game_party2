#=================================================
# �菕���N�G�X�g Created by Merino
#=================================================
# �ꏊ��
$this_title = '�菕���N�G�X�g';

# NPC��
$npc_name = '@د�';

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$logdir/helper";

# �w�i�摜
$bgimg = "$bgimgdir/helper.gif";

# ����(��) ���̊��Ԃ𒴂��Ă��N���B�����Ȃ������ꍇ�̓N�G�X�g��ύX
$limit_day = 6;

# ����@ ����A�h��A����K�v �����X�^�[���K�v�@�ʋ����ʁA�M���h��p �M���h�����҂Ȃ� GP up ����N���A���V����쐬���撅�N���A

# �C�x���g�N���A�ɕK�v�ȃA�C�e��No
@clear_items = (
	[1..27], # ����No
	[1..27], # �h��No
	[1..27,30..43,60..65,72..103,108], # ����No
	['004'..'120',198..260], # ����No
	['001'..'003'], # ���̖��������Ԃ������Ƃ��̖���No
);
# ��V(����No)
@pays = (128,128,128,130..134,134);


# ���A�N�G�C�x���g�N���A�ɕK�v�ȃA�C�e��No
@rare_items = (
	[28..40], # ����No
	[28..40], # �h��No
	[28,29,40,58..59,66..71,104..107,109], # ����No
	[500..579], # ����No
	[160..165], # ���̖��������Ԃ������Ƃ��̖���No
);
# ���A�N�G��V(����No)
@rare_pays = (129,129,129,135..137);


#=================================================
# �͂Ȃ����t
#=================================================
@words = (
	"�����͍����Ă���l�B�������鉽�ł�����",
	"�A�C�e���⃂���X�^�[���˗���̑���ɒT���Ă��Ăق�����",
	"��V�͘B���ɕK�v�ƂȂ�f�ނȂǁA���ł͎�ɓ���Ȃ��A�C�e����",
	"���܂Ƀ��A�N�G�X�g�Ƃ����āA�����𖞂����̂�����˗�������́B�ł��A���̎��̕�V�͑��ł͎�ɓ���邱�Ƃ��ł��Ȃ����̂�",
	"�N���������邱�Ƃ��ł��Ȃ��˗��͂��΂炭����ƈႤ�˗��ɕς���",
);


#=================================================
# �ǉ��A�N�V����
#=================================================
push @actions, ('�݂�', '��������');
$actions{'�݂�'}     = sub{ &miru }; 
$actions{'��������'} = sub{ &kaiketsu }; 


#=================================================
# ���݂� # 1,2,3:�q�ɂ����� 4:�q�������
#=================================================
sub miru {
	my $target = shift;

	my $p = qq|<table class="table1"><tr><th>�˗���</th><th>�N���A����</th><th>��V</th><th>����</th></tr>|;

	open my $fh, "< $logdir/helper_quest.cgi" or &error("$logdir/helper_quest.cgi�t�@�C�����J���܂���");
	while (my $line = <$fh>) {
		my($limit_time,$limit_date,$name,$is_guild,$pay,$kind,$no,$need_c) = split /<>/, $line;
		my $detail = $kind eq '1' ? "$weas[$no][1] <b>$need_c</b> �{"
				   : $kind eq '2' ? "$arms[$no][1] <b>$need_c</b> ��"
				   : $kind eq '3' ? "$ites[$no][1] <b>$need_c</b> ��"
				   :             qq|<img src="$icondir/mon/$no.gif" /> <b>$need_c</b> �C|;
		my $g_mark = $is_guild ? qq|<img src="$icondir/etc/mark_guild.gif" alt="�M���h��p" />| : '';
		$p .= qq|<tr><td>�w$name�x</td><td>�y$g_mark $detail�z</td><td>��$ites[$pay][1]</td><td>�Y$limit_date�܂�</td></tr>|;
	}
	close $fh;

	$mes = qq|�菕���N�G�X�g�ꗗ<br />$p</table>|;
	$act_time = 0;
}

#=================================================
# ���������� # 1,2,3:�q�ɂ����� 4:�q�������
#=================================================
sub kaiketsu {
	my $target = shift;

	my $p = qq|<table class="table1"><tr><th>�˗���</th><th>�N���A����</th><th>��V</th><th>����</th></tr>|;

	my @lines = ();
	open my $fh, "+< $logdir/helper_quest.cgi" or &error("$logdir/helper_quest.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($limit_time,$limit_date,$name,$is_guild,$pay,$kind,$no,$need_c) = split /<>/, $line;
	
		my $detail = $kind eq '1' ? "$weas[$no][1] <b>$need_c</b> �{"
				   : $kind eq '2' ? "$arms[$no][1] <b>$need_c</b> ��"
				   : $kind eq '3' ? "$ites[$no][1] <b>$need_c</b> ��"
				   :             qq|<img src="$icondir/mon/$no.gif" /> <b>$need_c</b> �C|;

		if ($name eq $target) {
			if ($is_guild && $m{guild} eq '') {
				$mes = "$name�̓M���h��p�̃N�G�X�g��B�M���h�ɉ������Ă��Ȃ��ƈ˗����󂯂邱�Ƃ��ł��Ȃ���";
				return;
			}
			my $is_clear = $kind eq '4' ? &check_farm($no,$need_c) : &check_depot($kind, $no, $need_c);
			if ($is_clear) {
				&send_item($m, 3, $pay);
				$npc_com .= "<br />" if $npc_com;
				$npc_com .= " $detail �������Ɏ󂯎��܂����B�����炪��V�� $ites[$pay][1] �ɂȂ�܂��I$m����̗a�菊�ɑ����Ă����܂��ˁI";
				$line = &create_helper_line();
				
				&regist_guild_data('point', 100) if $is_guild && $m{guild};
				++$m{help_c};
			}
			else {
				$mes = "$detail �̏����𖞂����ĂȂ��悤�ł�";
				return;
			}
		}
		elsif ($time > $limit_time) {
			$line = &create_helper_line();
			$npc_com .= "<br />" if $npc_com;
			$npc_com .= "�w$name�x�͒N�������ł������ɂȂ��̂ŁA�V�����˗������܂����I";
		}

		$p .= qq|<tr onclick="text_set('����������>$name ')"><td>�w$name�x</td><td>�y$detail�z</td><td>��$ites[$pay][1]</td><td>�Y$limit_date�܂�</td></tr>|;
		push @lines, $line;
	}
	if ($npc_com) {
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
		close $fh;
		return;
	}
	close $fh;

	$p  .= qq|</table>|;
	$mes = qq|�菕���N�G�X�g�ꗗ<br />$p|;
	$act_time = 0;
}

#=================================================
# �N�G�X�g�쐬
#=================================================
sub create_helper_line {
	# �^�C�v[1:����,2:�h��,3:����,4:����]
	my $kind = int(rand(4)+1);

	my $no = 0;
	my $pay;
	if (rand(14) < 1) { # 1/14�̊m���Ń��A�N�G
		my @items = @{ $rare_items[$kind-1] };
		$no  = $items[int rand @items];
		$pay = $rare_pays[int rand @rare_pays];

		# �����X�^�[No�����Ԃ������ꍇ
		if ($kind eq '4' && !-f "$icondir/mon/$no.gif") {
			@items = @{ $rare_items[$kind] };
			$no = $items[int rand @items];
		}
	}
	else { # �ʏ�N�G�X�g
		my @items = @{ $clear_items[$kind-1] };
		$no  = $items[int rand @items];
		$pay = $pays[int rand @pays];

		# �����X�^�[No�����Ԃ������ꍇ
		if ($kind eq '4' && !-f "$icondir/mon/$no.gif") {
			@items = @{ $clear_items[$kind] };
			$no = $items[int rand @items];
		}
	}

	# �K�v�� $kind eq '4':�����W��
	my $need_c = $kind eq '4' ? int(rand(2)+1) : int(rand(3)+2);

	# 1/15�̊m���ŃM���h��p
	my $is_guild = 0;
	if (rand(15) < 1) {
		$is_guild = 1;
		$need_c *= 2; # �K�v���Q�{
		$pay = 126; # �K����
	}

	# �N�G�X�g��(���Ȃ��悤��int(rand(999)) )
	my @names = $kind eq '1' ? ('�X���n�߂����̂�','�����Ȃ肽����','�킢�p��','���C�o���ɏ���������','���Ă݂���','���','�ƕ�ɂ�����','�T���Ă��܂�') # ����
			  : $kind eq '2' ? ('�R���v���[�g�̂��߂�','�J�b�R�ǂ��Ȃ肽��','�I�V�����ɂȂ肽����','��������̕�','�v���[���g�p��','���Ă݂���','�W�߂���','���s�Ȃ̂�') # �h��
			  : $kind eq '3' ? ('�R���N�V�����p','�a�C���������߂�','���p��','�K�v�Ȃ�ł�','��D���Ȃ̂�','�C�ɂȂ�̂�','�����p�ɗ~����','�p�r�͔閧�ł�') # ����
			  :                ('���킢���̂�','�y�b�g�ق���','���ǂ��Ȃ肽��','�v�j�v�j������','���₳�ꂽ��','�G���Ă݂���','�w���ɏ���Ă݂���','�K���ɂȂ邽�߂�','��������邽�߂�'); # ����
	my $name = $names[int(rand(@names))] . '����' . int(rand(999)+1);

	# ����
	my $limit_time = $time + $limit_day * 24 * 60 * 60;
	my($min,$hour,$mday,$mon,$year) = (localtime($limit_time))[1..4];
	my $limit_date = sprintf("%d/%d %02d:%02d", $mon+1,$mday,$hour,$min);

	return "$limit_time<>$limit_date<>$name<>$is_guild<>$pay<>$kind<>$no<>$need_c<>\n";
}

#=================================================
# �q�Ƀ`�F�b�N�B�����N���A�Ȃ�Y���̃A�C�e�������炷
#=================================================
sub check_depot {
	my($p_kind, $p_no, $need_c) = @_;

	my $c = 0;
	my @lines = ();
	open my $fh, "+< $userdir/$id/depot.cgi" or &error("$userdir/$id/depot.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($kind, $no) = split /<>/, $line;
		
		# �Y�����J�E���g(�X�g�b�N���Ȃ�)�A��Y�����X�g�b�N
		$kind eq $p_kind && $no eq $p_no && $c < $need_c ? ++$c : push @lines, $line;
	}
	if ($c >= $need_c) { # ���������N���A���Ă���㏑��
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
		close $fh;
		return 1;
	}
	close $fh;
	
	return 0;
}
#=================================================
# �q��`�F�b�N�B�����N���A�Ȃ�Y���̖��������炷
#=================================================
sub check_farm {
	my($p_no, $need_c) = @_;
	
	my $c = 0;
	my @lines = ();
	open my $fh, "+< $userdir/$id/monster.cgi" or &error("$userdir/$id/monster.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($name, $icon) = split /<>/, $line;
		
		$icon eq "mon/$p_no.gif" && $c < $need_c ? ++$c : push @lines, $line;
	}
	if ($c >= $need_c) {
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
		close $fh;
		return 1;
	}
	close $fh;
	
	return 0;
}


1; # �폜�s��
