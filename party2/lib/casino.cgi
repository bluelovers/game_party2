#=================================================
# �`�������E�쐬 Created by Merino
#=================================================
# �ꏊ��
$this_title = '�J�W�m';

# NPC��
$npc_name = '@��ư';

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$logdir/casino";

# �w�i�摜
$bgimg   = "$bgimgdir/casino.gif";

# �������̍ő啶����(���p)
$max_title = 50;

# �ő�Q���l��
$max_party = 8;

# �Œ�q�����
$min_bet   = 10;

# �q�����[�g
@rates = (1, 5, 10, 20, 50, 100, 500, 1000, 5000);

# �i�s�X�s�[�h
%speeds = (
#	�b��	=> ['�Z���N�g��', "�摜�t�@�C��"],
	12		=> ['��������', "$icondir/etc/speed_sakusaku.gif"],
	18		=> ['�܂�����', "$icondir/etc/speed_mattari.gif"],
	28		=> ['��������', "$icondir/etc/speed_jikkuri.gif"],
);


# ���u����(���O�̍X�V�Ȃ�)�̎����폜����(�b)
$auto_delete_casino_time = 1800;

# �������X�g
my @prizes = (
# ��� 1=����,2=�h��,3=���� 
#*�����͕K�v�����Ŕ��f���Ă���̂ŁA���������������̓_��
#  [0]*�K�v����,[1]���,[2]No
	[0,			0,		0,	],
	[100,		3,		4,	],
	[300,		3,		12,	],
	[700,		3,		6,	],
	[2000,		3,		32,	],
	[4000,		3,		38,	],
	[5000,		3,		39,	],
	[8000,		2,		34,	],
	[30000,		1,		31,	],
	[70000,		1,		40,	],
	[80000,		1,		38,	],
	[180000,	3,		106,],
	[200000,	3,		105,],
);


#=================================================
# ��ʃw�b�_�[
#=================================================
sub header_html {
	print qq|<div class="mes">�y$this_title�z �R�C��<b>$m{coin}</b>�� / �S�[���h<b>$m{money}</b>G</div>|;
	print qq|<div class="view">|;
	&casino_html;
	print qq|</div>|;
}


#=================================================
# �͂Ȃ����t
#=================================================
@words = (
	"�R�C���͂P��20G�ł���",
	"�S�[���h���R�C���ɗ��ւ��Ăˁ�",
	"�ܕi�͑��ł͂Ȃ��Ȃ���ɓ���邱�Ƃ��ł��Ȃ����A�ȃA�C�e���΂���恙",
	"�X���b�g�̊G�����R���낦��ƃR�C���������čK���ɂȂ���恙",
	"������肵�Ă����Ăˁ�",
);

sub shiraberu_npc {
	$mes = "$npc_name�u���႟�b���G�b�`�B�`���v";
}


#=================================================
# �ǉ��A�N�V����
#=================================================
push @actions, '����';
push @actions, '����';
push @actions, '���񂪂�';
push @actions, ('��1�������', '��10�������', '��50�������','��100�������', '��������', '��傤����',);
$actions{'����'}   = sub{ &tsukuru }; 
$actions{'����'}   = sub{ &sanka }; 
$actions{'���񂪂�'} = sub{ &kengaku }; 
$actions{'�h�b�y��'} = sub{ &doppel }; 
$actions{'�n�C���E'} = sub{ &highlow }; 
$actions{'�C���f�B�A��'} = sub{ &indian }; 
$actions{'��1�������'}   = sub{ &slot_1   }; 
$actions{'��10�������'}  = sub{ &slot_10  }; 
$actions{'��50�������'}  = sub{ &slot_50  }; 
$actions{'��100�������'} = sub{ &slot_100 }; 
$actions{'��������'}      = sub{ &koukan  }; 
$actions{'��傤����'}    = sub{ &ryougae }; 

#=================================================
# �����ꗗ
#=================================================
sub casino_html {
	opendir my $dh, "$casinodir" or &error("$casinodir�f�B���N�g�����J���܂���");
	while (my $dir_name = readdir $dh) {
		next if $dir_name =~ /\./;
		
		# ���u�����폜(30���ȏネ�O�̍X�V�Ȃ�)
		my($mtime) = (stat("$casinodir/$dir_name/log.cgi"))[9];
		if ($time > $mtime + $auto_delete_casino_time) {
			&auto_delete_casino($dir_name);
			next;
		}

		open my $fh, "< $casinodir/$dir_name/member.cgi";
		my $head_line = <$fh>;
		my($speed,$stage,$round,$leader,$p_name,$p_pass,$p_join,$win,$bet,$is_visit,$now_bet,$max_bet) = split /<>/, $head_line;
		my $count = 1;
		my $p = qq| <span onclick="text_set('������ׂ�>$leader ')"><img src="$icondir/etc/mark_leader.gif" alt="���[�_�[" />$leader</span> / |;
		while (my $line = <$fh>) {
			my($name,$laddr,$color) = split /<>/, $line;
			next if $leader eq $name;
			$p .= qq|<span onclick="text_set('������ׂ�>$name ')">$name</span> / |;
			++$count;
		}
		close $fh;
		my $bet_name = $stage eq '�h�b�y��' ? "�q�����<b>$bet</b>��" : "���[�g<b>$bet</b>";
		my $party_data = qq|$p_name�y$stage�z<img src="$speeds{$speed}[1]" alt="$speeds{$speed}[0]" /> <span class="">$bet_name</span> �y<b>$count</b>/<b>$p_join</b>�z|;
		my $aikotoba = $p_pass ? '���������Ƃ�>' : ' ';
		if ($round > 0) {
			if ($count >= $p_join) {
				print !$is_visit ? qq|<img src="$icondir/etc/full.gif" alt="�ΐ풆" /> $party_data ���w�~ $p<hr size="1" />|
					: qq|<span onclick="text_set('�����񂪂�>$p_name$aikotoba')"><img src="$icondir/etc/playing.gif" alt="�ΐ풆" /> $party_data</span>$p<hr size="1" />|;
			}
			else {
				print !$is_visit ? qq|<img src="$icondir/etc/playing.gif" alt="�ΐ풆" /> $party_data ���w�~ $p<hr size="1" />|
					: qq|<span onclick="text_set('������>$p_name$aikotoba')"><img src="$icondir/etc/playing.gif" alt="�ΐ풆" /> $party_data</span>$p<hr size="1" />|;
			}
		}
		elsif ($count >= $p_join) {
			print !$is_visit ? qq|<img src="$icondir/etc/full.gif" alt="�܂񂢂�" /> $party_data ���w�~ $p<hr size="1" />|
				: qq|<span onclick="text_set('�����񂪂�>$p_name$aikotoba')"><img src="$icondir/etc/full.gif" alt="�܂񂢂�" /> $party_data</span>$p<hr size="1" />|;
		}
		else {
			print qq|<span onclick="text_set('������>$p_name$aikotoba')"><img src="$icondir/etc/waitting.gif" alt="��������" /> $party_data</span>$p<hr size="1" />|;
		}
	}
	closedir $dh;
}
sub auto_delete_casino { # ���u�����폜
	my $dir_name = shift;
	open my $fh, "< $casinodir/$dir_name/member.cgi";
	my $head_line = <$fh>;
	while (my $line = <$fh>) {
		my($name,$color) = (split /<>/, $line)[0,2];
		next if $color eq $npc_color;
		&regist_you_data($name, 'lib', '');
		&regist_you_data($name, 'sleep', 3600);
	}
	close $fh;
	&delete_directory("$casinodir/$dir_name");
}

#=================================================
# ������
#=================================================
sub tsukuru {
	# �Q���l��
	my $join_select = qq|<select name="p_join" class="select1">|;
	for my $i (2 .. $max_party-1) {
		$join_select .= qq|<option value="$i">$i�l</option>|;
	}
	$join_select .= qq|<option value="$max_party" selected="selected">$max_party�l</option>|;
	$join_select .= qq|</select>|;

	# ���[�g
	my $rate_select = qq|<select name="bet" class="select1">|;
	for my $i (0..$#rates) {
		$rate_select .= qq|<option value="$i">$rates[$i]</option>|;
	}
	$rate_select .= qq|</select>|;

	# �i�s���x
	my $speed_select = qq|<select name="speed" class="select1">|;
	for my $k (sort { $a <=> $b } keys %speeds) {
		$speed_select .= qq|<option value="$k">$speeds{$k}[0]</option>|;
	}
	$speed_select .= qq|</select>|;
	
	$mes = <<"EOM";
<table><tr><td>
<form method="$method" action="$script">
	<input type="hidden" name="comment" value="���C���f�B�A��" />
	<input type="hidden" name="id" value="$id" /><input type="hidden" name="pass" value="$pass" />
	<table class="table1">
		<tr><th>���C���f�B�A��</th></tr>
		<tr><td>�������F</td><td><input type="text" name="p_name" class="text_box1" /></td></tr>
		<tr><td>�i�s���x�F</td><td>$speed_select</td></tr>
		<tr><td>�Q���l���F</td><td>$join_select</td></tr>
		<tr><td>���[�g�F</td><td>$rate_select</td></tr>
		<tr><td>�����t�F</td><td><input type="text" name="p_pass" class="text_box_s" />�@</td></tr>
		<tr><td>���w�F<input type="checkbox" name="is_visit" value="1" checked="checked"></td><td><input type="submit" value="���C���f�B�A��" /></td></tr>
	</table>
</form>
</td><td>
<form method="$method" action="$script">
	<input type="hidden" name="comment" value="���n�C���E" />
	<input type="hidden" name="id" value="$id" /><input type="hidden" name="pass" value="$pass" />
	<table class="table1">
		<tr><th>���n�C���E</th></tr>
		<tr><td>�������F</td><td><input type="text" name="p_name" class="text_box1" /></td></tr>
		<tr><td>�i�s���x�F</td><td>$speed_select</td></tr>
		<tr><td>�Q���l���F</td><td>$join_select</td></tr>
		<tr><td>���[�g�F</td><td>$rate_select</td></tr>
		<tr><td>�����t�F</td><td><input type="text" name="p_pass" class="text_box_s" />�@</td></tr>
		<tr><td>���w�F<input type="checkbox" name="is_visit" value="1" checked="checked"></td><td><input type="submit" value="���n�C���E" /></td></tr>
	</table>
</form>
</td><td>
<form method="$method" action="$script">
	<input type="hidden" name="comment" value="���h�b�y��" />
	<input type="hidden" name="id" value="$id" /><input type="hidden" name="pass" value="$pass" />
	<table class="table1">
		<tr><th>���h�b�y��</th></tr>
		<tr><td>�������F</td><td><input type="text" name="p_name" class="text_box1" /></td></tr>
		<tr><td>�i�s���x�F</td><td>$speed_select</td></tr>
		<tr><td>�Q���l���F</td><td>$join_select</td></tr>
		<tr><td>�q����݁F</td><td><input type="text" name="bet" class="text_box_s" style="text-align: right;" value="$min_bet" />��</td></tr>
		<tr><td>�����t�F</td><td><input type="text" name="p_pass" class="text_box_s" />�@</td></tr>
		<tr><td>���w�F<input type="checkbox" name="is_visit" value="1" checked="checked"></td><td><input type="submit" value="���h�b�y��" /></td></tr>
	</table>
</form>
</td></tr></table>
EOM
}
#=================================================
# ���̓`�F�b�N
#=================================================
sub check_create_casino {
	my($p_name) = @_;
	
	if ($p_name eq '�h�b�y��') {
		$mes = "�q����݂͍Œ�ł� $min_bet ���K�v�ł�"	if $in{bet} < $min_bet;
		$mes = "�q����݂͍Œ�ł� 1 ���K�v�ł�"			if $in{bet} < 1;
		$mes = "�q����݂�����܂���"					if $in{bet} > $m{coin};
	}
	else {
		$mes = "���[�g���ُ�ł�"							if $in{bet} < 0 || $in{bet} > @rates;
		$in{bet} = $rates[$in{bet}];
		$mes = "���[�g$in{bet}�ŗV�Ԃ��߂̺�݂�����܂���"	if $m{coin} < $in{bet} * 5;
	}
	$mes = "�Q���l�����ُ�ł�"		if $in{p_join} < 2 || $in{p_join} > $max_party;
	return if $mes;

	$in{is_visit} = 1 if $in{is_visit} =~ /[^01]/;
	$mes = "�i�s���x���ُ�ł�"		unless defined $speeds{$in{speed}};
	$mes = "�������͔��p$max_title�����܂łł�"						if length($in{p_name}) > $max_title;
	$mes = "�������ɕs���ȋ󔒂��܂܂�Ă��܂�"						if $in{p_name} =~ /�@|\s/;
	$mes = "�������ɕs���ȕ���( ,;\"\'&<>\\\/@ )���܂܂�Ă��܂�"	if $in{p_name} =~ /[,;\"\'&<>\\\/@]/;
	$mes = "�������ɕs���ȕ���( �� )���܂܂�Ă��܂�"				if $in{p_name} =~ /��/;
	$mes = "�����������߂Ă�������"	unless $in{p_name};
}
#=================================================
# ���C���f�B�A��
#=================================================
sub indian {
	&check_create_casino('�C���f�B�A��');
	return if $mes;
	$in{stage} = '�C���f�B�A��';
	$in{now_bet} = $in{bet};
	&_create_room;
	$m{lib} = 'casino_indian';
}
#=================================================
# ���n�C���E
#=================================================
sub highlow {
	&check_create_casino('�n�C���E');
	return if $mes;
	$in{stage} = '�n�C���E';
	$in{now_bet} = $in{bet};
	&_create_room;
	$m{lib} = 'casino_highlow';
}
#=================================================
# ���h�b�y��
#=================================================
sub doppel {
	&check_create_casino('�h�b�y��');
	return if $mes;
	$in{stage} = '�h�b�y��';
	$in{now_bet} = 1;
	&_create_room;
	$m{lib} = 'casino_doppel';
}



# �V�K�����쐬
sub _create_room {
	my $casino_id = unpack 'H*', $in{p_name};
	$mes = "����������($in{p_name})�����łɑ��݂��܂�" if -d "$casinodir/$casino_id";
	return if $mes;

	my $bet_name = $in{stage} eq '�h�b�y��' ? "�q�����$in{bet}��" : "���[�g$in{bet}";

	my $max_bet = $in{bet} * 5;
	mkdir "$casinodir/$casino_id", $mkdir or &error("$casinodir/$casino_id�f�B���N�g�����쐬�ł��܂���");
	open my $fh, "> $casinodir/$casino_id/member.cgi" or &error("$casinodir/$casino_id/member.cgi�t�@�C�����쐬�ł��܂���");
	print $fh "$in{speed}<>$in{stage}<>0<>$m<>$in{p_name}<>$in{p_pass}<>$in{p_join}<>0<>$in{bet}<>$in{is_visit}<>$in{now_bet}<>$max_bet<>\n";
	my $new_line = &get_battle_line($m{color},0);
	print $fh "$new_line\n";
	close $fh;
	chmod $chmod, "$casinodir/$casino_id/member.cgi";
	
	for my $k (qw/log bet win/) {
		open my $fh2, "> $casinodir/$casino_id/$k.cgi" or &error("$casinodir/$casino_id/$k.cgi�t�@�C�����쐬�ł��܂���");
		close $fh2;
		chmod $chmod, "$casinodir/$casino_id/$k.cgi";
	}
	
	$com = "<b>��$in{stage}>$in{p_name}��$bet_name���Q���l��>$in{p_join}�l��$speeds{$in{speed}}[0]";
 	if ($in{p_pass}) {
		$com .= "�������t>�K�v";
	}
	else {
		$in{p_pass} = '�Ȃ�' ;
	}
	$com .= "</b>";

	$m{quest} = $casino_id;
	&reload("$in{p_name}�����y$in{stage}�z�����܂����I<br />$bet_name, $speeds{$in{speed}}[0]�C�����t�F$in{p_pass}�C�Q���l���F$in{p_join}�l");
	&leave_member($m);
}
#=================================================
# ������
#=================================================
sub sanka {
	my $target = shift;

	$mes = qq|<span onclick="text_set('���ف[�� ')">$e2j{tired}�����܂��Ă��܂��B�u���ف[�ށv�ŉƂɋA��u���˂�v�ŋx��ł�������</span>|	if $m{tired} >= 100;
	return if $mes;

	unless ($target) {
		$mes = "�ǂ̕����ɎQ�����܂����H";
		return;
	}
	
	my($p_name, $join_pass) = split /���������Ƃ�&gt;/, $target;
	my $casino_id = unpack 'H*', $p_name;
	$com =~ s/(.+)���������Ƃ�&gt;(.+)/$1/; # �����������������Ƃ΁`���폜

	if ($p_name && -d "$casinodir/$casino_id") {
		&add_member($casino_id,$join_pass);
	}
	else {
		$mes = "�Q�����悤�Ƃ��������́A���U���Ă��܂����悤�ł�";
	}
}

#=================================================
# �����񂩏���
#=================================================
sub add_member {
	my($casino_id,$join_pass) = @_;
	
	my @lines = ();
	open my $fh, "+< $casinodir/$casino_id/member.cgi" or &error("$casinodir/$casino_id/member.cgi�t�@�C�����쐬�ł��܂���");
	eval { flock $fh, 2; };
	my $head_line = <$fh>;
	my($speed,$stage,$round,$leader,$p_name,$p_pass,$p_join,$win,$bet,$is_visit) = split /<>/, $head_line;
	
	$mes = "$p_name�ɎQ�����邽�߂̺�݂�����܂���"		if $bet > $m{coin};
	$mes = "$p_name�ɎQ�����邽�߂̍����t���Ⴂ�܂�"	if $p_pass ne '' && $p_pass ne $join_pass;
#	$mes = "�ΐ�r������Q�����邱�Ƃ͂ł��܂���"		if $round > 0;
	return if $mes;
	
	push @lines, $head_line;

	while (my $line = <$fh>) {
		my($name,$laddr,$gcolor) = (split /<>/, $line)[0..2];
		if ($name eq $m) {
			$mes = "�������O�̃v���C���[�����łɎQ�����Ă��܂�";
			return;
		}
		elsif ($addr eq $laddr) {
			$mes = "�h�o�A�h���X�������v���C���[�����łɎQ�����Ă��܂��B";
#			$mes .= "<br />���d�o�^�e�^�ŒǕ��R�m�c�ɒǉ��\\������܂����B";
#			$m{wt} = $time;
#			&add_exile($m,    "�y���d�o�^�e�^�z$name�Ɠ���IP�A�h���X");
#			&add_exile($name, "�y���d�o�^�e�^�z$m�Ɠ���IP�A�h���X");
			return;
		}
		push @lines, $line;
	}
	if (@lines-1 >= $p_join) {
		$mes = "$p_name�͒���������ς��ŎQ�����邱�Ƃ��ł��܂���";
		return;
	}
	
	# �Q������OK
	my($color) ||= (split /<>/, $lines[1])[2];
	my $new_line = &get_battle_line($color,$type);
	push @lines, "$new_line\n";
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	$m{lib} = $stage eq '�h�b�y��' ? 'casino_doppel'
			: $stage eq '�n�C���E' ? 'casino_highlow'
			:                        'casino_indian';
	$m{quest} = $casino_id;
	&reload("$p_name�ɎQ�����܂�");

	&leave_member($m);
}

#=================================================
# �����񂪂�
#=================================================
sub kengaku {
	my $target = shift;

	unless ($target) {
		$mes = "�ǂ̕��������w���܂����H";
		return;
	}
	
	my($p_name, $join_pass) = split /���������Ƃ�&gt;/, $target;
	my $casino_id = unpack 'H*', $p_name;
	$com =~ s/(.+)���������Ƃ�&gt;(.+)/$1/; # �����������������Ƃ΁`���폜

	if ($p_name && -d "$casinodir/$casino_id") {
		open my $fh, "< $casinodir/$casino_id/member.cgi" or &error("$casinodir/$casino_id/member.cgi�t�@�C�����ǂݍ��߂܂���");
		my $head_line = <$fh>;
		close $fh;

		my($speed,$stage,$round,$leader,$p_name,$p_pass,$p_join,$win,$bet,$is_visit) = split /<>/, $head_line;
		if (!$is_visit) {
			$mes = "$p_name�̌��w�͂ł��܂���";
			return;
		}
		elsif ($p_pass ne '' && $p_pass ne $join_pass) {
			$mes = "$p_name�����w���邽�߂̍����t���Ⴂ�܂�";
			return;
		}
		
		$m{lib} = $stage eq '�h�b�y��' ? 'casino_doppel'
				: $stage eq '�n�C���E' ? 'casino_highlow'
				:                        'casino_indian';
		$m{quest} = $casino_id;
		$mes = "$p_name�����w���܂�";
		&reload("$p_name�����w���܂�");
		&leave_member($m);
	}
	else {
		$mes = "���w���悤�Ƃ��������́A���U���Ă��܂����悤�ł�";
	}
}


#=================================================
# ���������
#=================================================
sub slot_1   { &_slot(1) }
sub slot_10  { &_slot(10) }
sub slot_50  { &_slot(50) }
sub slot_100 { &_slot(100) }
sub _slot {
	my $bet = shift;
	
	if ($m{tired} >= 100) {
		$mes = qq|<span onclick="text_set('���ف[�� ')">$e2j{tired}�����܂��Ă��܂��B�u���ف[�ށv�ŉƂɋA��u���˂�v�ŋx��ł�������</span>|;
		return;
	}
	if ($m{coin} < $bet) {
		$mes = qq|<span onclick="text_set('����傤���� ')">��$bet�X���b�g������R�C��������܂���B�u����傤�����v�ŃR�C���𗼑ւ��Ă�������</span>|;
		return;
	}
	
	my @m = ('��','��','��','��','�V');
	my @o = (3,10, 20,  50,  70,  100); # �I�b�Y ��ԍ��̓`�F���[��2���낢�̂Ƃ�
	my @s = ();
	$s[$_] = int(rand(@m)) for (0 .. 2);
	$mes .= qq|<span onclick="text_set('����$bet�������')">|;
	$mes .= "\$$bet�X���b�g<br />";
	$mes .= "�y$m[$s[0]]�z�y$m[$s[1]]�z�y$m[$s[2]]�z<br />";
	$m{coin} -= $bet;

	# �A�Ŗh�~��
	$act_time *= 0.5;
	$m{wt}  = $time + $act_time;
	$nokori = $act_time;

	if ($s[0] == $s[1]) { # 1�ڂ�2��
		if ($s[1] == $s[2]) { # 2�ڂ�3��
			my $v = $bet * $o[$s[0]+1]; # +1 = �`�F���[2���낢
			$m{coin} += $v;
			$mes .= "�Ȃ��!! $m[$s[0]] ��3���낢�܂���!!<br />";
			$mes .= "���߂łƂ��������܂�!!<br />";
			$mes .= "***** �R�C�� $v �� GET !! *****<br />";
		}
		elsif ($s[0] == 0) { # �`�F���[�̂�1�ڂ�2�ڂ����낦�΂悢
			my $v = $bet * $o[0];
			$m{coin} += $v;
			$mes .= "�`�F���[��2���낢�܂�����<br />";
			$mes .= "�R�C�� $v ��Up��<br />";
		}
		else {
			$mes .= "�n�Y��<br />";
			$m{tired} += 1;
		}
	}
	else {
		$mes .= "�n�Y��<br />";
		$m{tired} += 1;
	}
	$mes .= "</span>";
}


#=================================================
# ����������
#=================================================
sub koukan {
	my $target = shift;
	
	my $p = qq|<table class="table1"><tr><th>�ܕi</th><th>���</th></tr>|;
	for my $i (1 .. $#prizes) {
		if ("$prizes[$i][0]��" eq $target) {
			if ($m{coin} >= $prizes[$i][0]) {
				if ($prizes[$i][1] eq '1') {
					&send_item($m, $prizes[$i][1], $prizes[$i][2]);
					$npc_com = "�R�C��$target�̏ܕi�ƌ����ł��ˁI$weas[ $prizes[$i][2] ][1]��$m�̗a���菊�ɑ����Ă����܂���";
				}
				elsif ($prizes[$i][1] eq '2') {
					&send_item($m, $prizes[$i][1], $prizes[$i][2]);
					$npc_com = "�R�C��$target�̏ܕi�ƌ����ł��ˁI$arms[ $prizes[$i][2] ][1]��$m�̗a���菊�ɑ����Ă����܂���";
				}
				else {
					&send_item($m, $prizes[$i][1], $prizes[$i][2]);
					$npc_com = "�R�C��$target�̏ܕi�ƌ����ł��ˁI$ites[ $prizes[$i][2] ][1]��$m�̗a���菊�ɑ����Ă����܂���";
				}
				$m{coin} -= $prizes[$i][0];
			}
			else {
				$mes = "�R�C��$target�̏ܕi�ƌ�������̂ɃR�C��������܂���";
			}
			return;
		}
	
		$p .= qq|<tr onclick="text_set('����������>$prizes[$i][0]�� ')"><td>|;
		$p .= $prizes[$i][1] eq '1' ? $weas[$prizes[$i][2]][1]
		    : $prizes[$i][1] eq '2' ? $arms[$prizes[$i][2]][1]
		    :                         $ites[$prizes[$i][2]][1]
		    ;
		$p .= qq|</td><td align="right">$prizes[$i][0]��</td></tr>|;
	}
	$p  .= qq|</table>|;
	$mes = qq|�ǂ�ƌ������܂����H<br />$p|;
	$act_time = 0;
}


#=================================================
# ����傤����
#=================================================
sub ryougae {
	my $target = shift;
	$target =~ s/��//;

	if ($target < 1 || $target =~ /[^0-9]/) {
		$mes = qq|<span onclick="text_set('����傤����>')">�R�C���P�� 20 G�ł��B�����痼�ւ��܂����H</span>|;
		return;
	}

	my $need_money = $target * 20;
	if ($need_money > $m{money}) {
		$mes = "�S�[���h������܂���B�R�C��$target���𗼑ւ���ɂ� $need_money G�K�v�ł�";
		return;
	}
	
	$m{coin}  += $target;
	$m{money} -= $need_money;
	$npc_com = "$target���̃R�C���Ɨ��ւ��܂���";
}


#=================================================
# �o�g���p�f�[�^�쐬 @casino_datas�̒l���Z�b�g
#=================================================
sub get_battle_line {
	my $color = shift;
	my %p = %m;
	
	$p{card}   = 0;
	$p{action} = '�ҋ@��';
	
	my $line = '';
	for my $k (@casino_datas) {
		$line .= "$p{$k}<>";
	}
	return $line;
}


1; # �폜�s��
