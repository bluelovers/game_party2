&get_date; # ���ԂƓ��t�͏펞�K�v�Ȃ̂ŏ�Ɏ擾 Get $time,$date
#================================================
# �T�u���[�`���W(�悭�g������) Created by Merino
#================================================
# ��{�A�N�V�����R�}���h
sub set_action {
	push @actions, ('br','���ǂ�', '�܂�', '�ف[��');
	if ($m{guild}) {
		push @actions, '�����';
		$actions{'�����'} = sub{ &girudo }
	}
	push @actions, ('�����₫', '�͂Ȃ�', '����ׂ�', '�낮������', '��������');
	$actions{'���ǂ�'}   = sub{ &idou };
	$actions{'�܂�'}     = sub{ &machi };
	$actions{'�ف[��'}   = sub{ &homu };
	$actions{'�͂Ȃ�'}   = sub{ &hanasu };
	$actions{'����ׂ�'} = sub{ &shiraberu };
	$actions{'�����₫'} = sub{ &sasayaki };
	$actions{'�낮������'} = sub{ &roguauto };
	$actions{'��������'} = sub{ &sukusho }; 
}

#================================================
# �v���C���[�f�[�^��������
#================================================
sub write_user {
	&error("�v���C���[�f�[�^�̏������݂Ɏ��s���܂���") if !$id || !$m{name};

	# -------------------
	# top��۸޲�ؽĂɕ\��
	if ($time > $m{login_time} + $login_time * 60) {
		$m{login_time} = $time;
		
		open my $fh2, ">> $logdir/login.cgi";
		print $fh2 "$time<>$m{name}<>$m{color}<>$m{guild}<>$m{mes}<>$m{icon}<>\n";
		close $fh2;
	}

	$m{addr}  = $addr;
	$m{host}  = $host;
	$m{ltime} = $time;
	$m{ldate} = $date;
	# -------------------
	# �ð���̍ő�l
	for my $k (qw/mhp hp mmp mp/) {
		$m{$k} = 999 if $m{$k} > 999;
	}
	for my $k (qw/at df ag/) {
		$m{$k} = 255 if $m{$k} > 255;
	}
	$m{coin}   = 0 if $m{coin} <= 0;
	$m{money}  = 999999 if $m{money} > 999999;
	
	# -------------------
	# �ϐ��ǉ�����ꍇ�͔��p��߰������s�����Ēǉ�(���s���A���בւ���(login_time�ȊO))
	my @keys = (qw/
		login_time ldate name pass addr host lib wt sleep
		ltime quest home guild job_lv lv exp money medal coin coupon rare
		tired sex icon color job sp old_job old_sp mhp hp mmp mp at df ag wea arm ite
		orb is_full is_get is_eat kill_p kill_m cas_c hero_c mao_c alc_c help_c event recipe mes
	/);
	# ۸޲݂������ԁ@�ŏI۸޲ݓ��@���O�@�߽ܰ�ށ@IP�@Host�@lib�@�҂����ԁ@�S������
	# �ŏI۸޲ݎ��ԁ@�Q�����ā@�؍݉Ɓ@����ށ@�]�E�񐔁@���x���o���l�@�����@�����ȃ��_���@�������@���A�|�C���g
	# ��J�x�@���ʁ@���݁@�F�@�E�Ɓ@�r�o�@�O�E�Ɓ@�r�o�@�ő�HP�@HP�@�ő�MP�@MP�@�U�@��@�f�@����@�h��@����
	# ���ށ@�a���菊���t�׸ށ@��擾�׸ށ@���H�׸ށ@��ڲ԰���ސ��@�ݽ�����ސ��@�J�W�m�n���x�@�E�ҏn���x�@�����n���x�@�B�����@�菕�����@�_���W�����C�x���g�@�B�����V�s�@ү����
	
	my $line;
	for my $k (@keys) {
		$line .= "$k;$m{$k}<>";
	}
	open my $fh, "> $userdir/$id/user.cgi";
	print $fh "$line\n";
	close $fh;
}

#================================================
# �v���C���[�f�[�^�ǂݍ���
#================================================
sub read_user { # Get %m
	my $is_header = shift || 0;
	$id ||= unpack 'H*', $in{login_name};

	open my $fh, "< $userdir/$id/user.cgi" or &error("���̂悤�Ȗ��O$in{login_name}�̃v���C���[�����݂��܂���", $is_header);
	my $line = <$fh>;
	close $fh;
	
	%m = ();
	for my $hash (split /<>/, $line) {
		my($k, $v) = split /;/, $hash;
		$m{$k} = $v;
	}
	&error("�p�X���[�h���Ⴂ�܂�", $is_header) unless $m{pass} eq $pass;
	
	if ($m{ltime} + $wait_time > $time && !$in{is_auto}) {
		open my $fh2, ">> $userdir/$id/reload.cgi";
		print $fh2 "1<>";
		close $fh2;
		&error("�X�V�̘A�ł͋֎~���Ă��܂��B�Œ�ł� $wait_time �b�͑҂��Ă�������<br>���ߓx�ȍX�V�A�ł͎����폜�̑ΏۂƂȂ�܂�", $is_header);
	}

	$m      = $m{name}; # ���O���悭�g���̂� $m �Əȗ�
	$nokori = int($m{wt} - $time);
}

#=================================================
# ����������
#=================================================
sub sukusho {
	my $target = shift || $this_title;
	
	my @lines = ();
	open my $fh, "+< $userdir/$id/screen_shot.cgi" or &error("$userdir/$id/screen_shot.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		push @lines, $line;
	}
	if (@lines >= $max_screen_shot) {
		$mes = qq|����ȏ�X�N���[���V���b�g���B�邱�Ƃ��ł��܂���B�t�H�g�R�����Łu�������v���Ă�������</span>|;
		return;
	}
	my $new_line;
	$new_line .= qq|<div class="mes">�y$target�z</div>|;
	$new_line .= &member_html;
	$new_line .= &_sukusho_mes;
	unshift @lines, "$new_line\n";
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	&write_top_screen_shot($new_line);
	
	$mes = "�X�N���[���V���b�g���Ƃ�܂���";
}
sub _sukusho_mes { # �R�����g�O�s�擾
	my $count = 0;
	my $data = qq|<hr size="1" />|;
	open my $fh, "< $this_file.cgi" or &error("$this_file.cgi �t�@�C�����J���܂���");
	while (my $line = <$fh>) {
		my($btime,$bdate,$bname,$baddr,$bcolor,$bcomment,$bto_name) = split /<>/, $line;
		next if $bto_name;
		$data .= qq|<font color="$bcolor">$bname</font>�F $bcomment <font size="1">($bdate)</font><hr size="1" />|;
		last if ++$count >= 3;
	}
	close $fh;
	return $data;
}
sub write_top_screen_shot { # �g�b�v�ɕ\������X�N�V���̃��O�ɏ�������
	my $new_line = shift;
	my @lines = ();
	open my $fh, "+< $logdir/screen_shot.cgi" or &error("$logdir/screen_shot.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		push @lines, $line;
		last if @lines >= $max_log-1;
	}
	unshift @lines, "$new_line\n";
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}

#================================================
# �������
#================================================
sub girudo {
	$m{lib} = 'guild';
	$mes = "��$m{guild}�Ɉړ����܂�";
	&auto_reload;
	&leave_member($m)
}

#================================================
# ���͂Ȃ�
#================================================
sub hanasu {
	unless (@words) {
		$mes = "�Ԏ����Ȃ��A�����̂����΂˂̂悤���c" ;
		return;
	}
	$npc_com = $words[int(rand(@words))];
}
#================================================
# �������₫
#================================================
sub sasayaki {
	$to_name = shift;
	if ($to_name) {
		my $yid = unpack 'H*', $to_name;
		unless (-f "$userdir/$yid/user.cgi") {
			$mes = "$to_name�Ƃ����v���C���[�����݂��܂���";
			return;
		}
	}
	$is_npc_action = 0;
	$act_time = 0;
}
#================================================
# �����ǂ�
#================================================
sub idou {
	my $target = shift;
	my $p = '';
	my $count = 0;
	for my $i (0 .. $#places) {
		if ($places[$i][0] eq $target) {
			if ($m{lib} eq $places[$i][1]) {
				$mes = "������$places[$i][0]�ł�";
			}
			else {
				$m{lib} = $places[$i][1];
				$mes = "$places[$i][0]�Ɉړ����܂�";
				&auto_reload;
				&leave_member($m);
			}
			return;
		}
		$p .= qq|<span onclick="text_set('�����ǂ�>$places[$i][0] ')">$places[$i][0] </span>/ |;
		$p .= qq|<br />| if ++$count % 7 == 0;
	}
	$mes = qq|�ǂ��Ɉړ����܂����H<br />$p|;
	$act_time = 0;
}
#================================================
# ���܂�
#================================================
sub machi {
	my $target = shift;
	my $p = '';
	@towns = reverse @towns; # ������������\��
	for my $i (0 .. $#towns) {
		if ($towns[$i][0] eq $target) {
			if ($m{lib} eq $towns[$i][1]) {
				$mes = "������$towns[$i][0]�ł�";
			}
			else {
				$m{lib} = $towns[$i][1];
				$mes = "$towns[$i][0]�Ɉړ����܂�";
				&auto_reload;
				&leave_member($m);
			}
			return;
		}
		$p .= qq|<span onclick="text_set('���܂�>$towns[$i][0] ')">$towns[$i][0] </span>/ |;
	}
	$mes = qq|�ǂ̒��ɍs���܂����H<br />$p|;
	$act_time = 0;
}
#================================================
# ������ׂ�
#================================================
sub shiraberu {
	my $target = shift;
	
	if ($target eq $npc_name) {
		&shiraberu_npc;
		return;
	}
	
	my $yid = unpack 'H*', $target;
	
	if (-f "$userdir/$yid/user.cgi") { # ����̃X�e�[�^�X
		my %p = &get_you_datas($yid, 1);
		
		if ($time > $p{login_time} + $login_time * 60) {
			$mes .= "$target�̓��O�C�����Ă��܂���";
		}
		elsif ($p{lib} eq 'home') {
			$mes .= "$target��$p{home}�̉Ƃɂ��܂�";
		}
		elsif ($p{lib} =~ /^vs_/) {
			$mes .= "$target�̓N�G�X�g���ł�";
		}
		else {
			for my $i (0..$#places) {
				if ($p{lib} eq $places[$i][1]) {
					$mes .= "$target��$places[$i][0]�ɂ��܂�";
					last;
				}
			}
		}
		
		$mes .= " �ŏI�X�V���� $p{ldate}<br />";
		if ($p{guild}) {
			my $gid = unpack 'H*', $p{guild};
			$mes .= qq|<img src="$guilddir/$gid/mark.gif" alt="�M���h�}�[�N" />| if -f "$guilddir/$gid/mark.gif";
			$mes .= qq|$p{guild} |;
		}
		$mes .= qq|<img src="$icondir/$p{icon}" />$p{name} $e2j{$p{sex}} $e2j{lv}$p{lv} $jobs[$p{job}][1](Sp $p{sp})/$jobs[$p{old_job}][1](Sp $p{old_sp})<br />|;
		$mes .= qq|$e2j{tired}�F$p{tired}�� $e2j{mhp}�F$p{mhp} $e2j{mmp}�F$p{mmp} $e2j{at}�F$p{at} $e2j{df}�F$p{df} $e2j{ag}�F$p{ag}<br />|;
		$mes .= qq| ����F$weas[$p{wea}][1]| if $p{wea};
		$mes .= qq| �h��F$arms[$p{arm}][1]| if $p{arm};
		$mes .= qq| ����F$ites[$p{ite}][1]| if $p{ite};
		$mes .= qq|<br />���w$p{mes}�x| if $p{mes};
	}
	else { # �����̃X�e�[�^�X
		if ($m{guild}) {
			my $gid = unpack 'H*', $m{guild};
			$mes .= qq|<img src="$guilddir/$gid/mark.gif" alt="�M���h�}�[�N" />| if -f "$guilddir/$gid/mark.gif";
			$mes .= qq|$m{guild} |;
		}
		my $next_lv = $m{lv} * $m{lv} * 10 - $m{exp};
		$mes .= qq|<img src="$icondir/$m{icon}" />$m $e2j{$m{sex}} / $e2j{lv}$m{lv} ���̃��x������${next_lv}Exp / $e2j{tired}$m{tired}�� / �]�E$m{job_lv}��<br />$jobs[$m{job}][1](Sp $m{sp})/$jobs[$m{old_job}][1](Sp $m{old_sp}) / $m{money}�f / $m{coin}�R�C�� / �����ȃ��_��$m{medal}�� <br />|;
		$mes .= qq|$e2j{tired}�F$m{tired}�� $e2j{mhp}�F$m{mhp} $e2j{mmp}�F$m{mmp} $e2j{at}�F$m{at} $e2j{df}�F$m{df} $e2j{ag}�F$m{ag}<br />|;
		$mes .= qq| ����F$weas[$m{wea}][1]| if $m{wea};
		$mes .= qq| �h��F$arms[$m{arm}][1]| if $m{arm};
		$mes .= qq| ����F$ites[$m{ite}][1]| if $m{ite};
	}
}
sub shiraberu_npc { $mes = "����������������Ȃ������c"; }
#================================================
# ���ف[��
#================================================
sub homu {
	my $target = shift;
	my $yid = unpack 'H*', $target;
	$m{lib} = 'home';
	
	if (-f "$userdir/$yid/home.cgi") {
		$m{home} = $target;
	}
	else {
		$m{home} = $m;
	}
	$mes = "�����̉ƂɋA��܂�";
	&auto_reload;
	&leave_member($m);
}

#================================================
# ��ʐ؂�ւ����̂P
# ���b�Z�[�W��\�����Ď蓮�ōX�V�{�^��
#================================================
sub reload { # Manual Reaload
	my $message = shift;
	$m{wt}  = $time + $act_time;
	
	print <<"EOM";
<div class="strong">$message</div>
<form method="$method" action="$script">
	<input type="hidden" name="id" value="$id" />
	<input type="hidden" name="pass" value="$pass" />
	<input type="submit" value="[> Next" class="button_s" />
</form>
EOM
}
#================================================
# ��ʐ؂�ւ����̂Q
# JavaScript�ɂ�鋭�������[�h�Ńy�[�W�𓮓I�ɕς���
#================================================
sub auto_reload { # Auto Reload
	$m{wt}  = $time + $act_time;
	print <<"EOM";
<script type="text/javascript"><!--
location.href="$script?id=$id&pass=$pass&is_auto=1&reload_time=$in{reload_time}";
// --></script>
<noscript>
	<form method="$method" action="$script">
		<input type="hidden" name="id" value="$id" />
		<input type="hidden" name="pass" value="$pass" />
		<input type="submit" value="[> Next" class="button_s" />
	</form>
</noscript>
EOM
}

#=================================================
# �����o�[�擾
#=================================================
sub read_member {
	%ms = ();
	my @lines   = ();
	my %sames   = ();
	my $is_find = 0;
	@members = ();
	open my $fh, "+< ${this_file}_member.cgi" or &error("${this_file}_member.cgi�t�@�C�����J���܂���"); 
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($ltime, $is_npc, $name, $laddr, $icon, $color) = split /<>/, $line;
		if (!$is_npc) {
			next if $time - $limit_member_time > $ltime;
			next if $sames{$name}++; # �����l�Ȃ玟
		}
		
		if ($is_npc) {
			$name =~ /^@/ ?
				push @lines, "$time<>1<>$npc_name<>0<>$icon<>$npc_color<>\n":
				push @lines, "$time<>1<>$name<>0<>$icon<>$npc_color<>\n";
		}
		elsif ($name eq $m) {
			$is_find = 1;
			push @lines, "$time<>0<>$m<>$addr<>$m{icon}<>$m{color}<>\n";
		}
		else {
			push @lines, $line;
		}
		push @members, $name;
		$ms{$name}{icon}  = $icon;
		$ms{$name}{color} = $color;
	}
	unless ($is_find) {
		push @members, $m;
		$ms{$m}{icon}     = $m{icon};
		$ms{$m}{color}    = $m{color};
		push @lines, "$time<>0<>$m<>$addr<>$m{icon}<>$m{color}<>\n";
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}

#=================================================
# ��ʈ�ԏ�ɕ\��(�ꏊ�̖��O�A�X�e�[�^�X�Ȃ�)
#=================================================
sub header_html {
	my $my_at = $m{at} + $weas[$m{wea}][3];
	my $my_df = $m{df} + $arms[$m{arm}][3];
	my $my_ag = $m{ag} - $weas[$m{wea}][4] - $arms[$m{arm}][4];
	$my_ag = 0 if $my_ag < 0;
	print qq|<div class="mes">�y$this_title�z $e2j{money} <b>$m{money}</b>G|;
	print qq| / $e2j{at} <b>$my_at</b> / $e2j{df} <b>$my_df</b> / $e2j{ag} <b>$my_ag</b> /|;
	print qq| E�F$weas[$m{wea}][1]| if $m{wea};
	print qq| E�F$arms[$m{arm}][1]| if $m{arm};
	print qq| E�F$ites[$m{ite}][1]| if $m{ite};
	print qq|</div>|;
}
#=================================================
# �����o�[�\��
#=================================================
sub member_html {
	my $member_html = '';
	$member_html .= qq|<div style="background: url($bgimg) #333 repeat-x left bottom;"><table><tr>|;
	for my $name (@members) {
		$member_html .= qq|<td onclick="text_set('>$name ')" align="center" valign="bottom"><span style="color: $ms{$name}{color}; font-size: 11px; background-color: #333;">$name</span><br /><img src="$icondir/$ms{$name}{icon}" alt="$name" /></td>|;
	}
	$member_html .=  qq|</tr></table></div>|;
	return $member_html;
}
#=================================================
# ��ʕ\��
#=================================================
sub html {
	&header_html;
	print &member_html;
	print qq|<form method="$method" action="$script" name="form" id="form">\n<input type="hidden" name="reload_time" value="$in{reload_time}" />\n|;
	print qq|<input type="hidden" name="id" value="$id" />\n<input type="hidden" name="pass" value="$pass" />|;
	print qq|<input type="text"  name="comment" class="text_box_b" />\n<input type="submit" value="����" class="button_s" />\n|;
	print qq| <input type="reset" value="�ر" /> |;
	print qq|<select name="reload_time"><option value="0">�Ȃ�</option>\n|;
	for my $i (1 .. $#reload_times) {
		print $in{reload_time} eq $i ? qq|<option value="$i" selected="selected">$reload_times[$i]�b</option>\n| : qq|<option value="$i">$reload_times[$i]�b</option>\n|;
	}
	print qq|</select>\n|;
	print qq|�X�V <span id="nokori_auto_time"></span>�b<script type="text/javascript"><!--\n count_down($reload_times[$in{reload_time}]);\n// --></script>\n| if $in{reload_time} > 0;
	print qq|<br />\n|;

	for my $action (@actions) {
		print $action eq 'br' ? qq|<br />| : qq|<span onclick="text_set('��$action ')">��$action</span> �@|;
	}
	print qq|</form>\n|;

	print qq|<font size="1">���̍s��</font><div id="gage_back1" style="width: $gage_width"><img src="$htmldir/space.gif" width="0%" class="gage_bar1" /></div><br />\n|;
	print qq|<script type="text/javascript"><!--\n active_gage($nokori, $act_time);\n// --></script></form>\n|;
	print qq|<div class="strong">$mes</div>\n| if $mes;
	print qq|<hr size="1" />\n|;
	
	# ���O�o��
	open my $fh, "< $this_file.cgi" or &error("$this_file.cgi �t�@�C�����J���܂���");
	while (my $line = <$fh>) {
		my($btime,$bdate,$bname,$baddr,$bcolor,$bcomment,$bto_name) = split /<>/, $line;
		if ($bto_name) { # �����₫
			if ($m eq $bto_name || $m eq $bname) {
				print qq|<span class="whisper">$bname�F $bcomment <font size="1">($bdate)</font></span><hr size="1" />\n|;
			}
		}
		else {
			print qq|<font color="$bcolor">$bname</font>�F $bcomment <font size="1">($bdate)</font><hr size="1" />\n|;
		}
	}
	close $fh;
}

#=================================================
# �����E�A�N�V����
#=================================================
sub action {
	$com .= "\x20";
	$com =~ /��(.+?)(?:(?:\x20|�@)?&gt;(.+?)(?:\x20|�@)|\x20|�@)/;
	my $action = $1;
	my $target = $2 ? $2 : '';
	return unless defined $actions{$action};
 	if ($nokori > 0) {
		$mes = "�܂��s�����邱�Ƃ͂ł��܂���";
		return;
	}
	
	&{ $actions{$action} }($target);
	return if $mes;
	
	$m{wt}  = $time + $act_time;
	$nokori = $act_time;
}

#=================================================
# ���O�������ݏ���
#=================================================
sub write_comment {
	my @lines = ();
	open my $fh, "+< $this_file.cgi" or &error("$this_file.cgi �t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		push @lines, $line;
		last if @lines >= $max_log-1;
	}
	unshift @lines, "$time<>$date<>$m{name}<>$addr<>$m{color}<>$com<>$to_name<>\n";
	unshift @lines, "$time<>$date<>$npc_name<>NPC<>$npc_color<>$npc_com<>$to_name<>\n" if $npc_com;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}

#================================================
# �f�R�[�h
#================================================
sub decode {
	local ($k,$v,$buf);

	if ($ENV{REQUEST_METHOD} eq 'POST') {
		&error('���e�ʂ��傫�����܂�',1) if $ENV{CONTENT_LENGTH} > 51200;
		read STDIN, $buf, $ENV{CONTENT_LENGTH};
	}
	else {
		&error('���e�ʂ��傫�����܂�',1) if length $ENV{QUERY_STRING} > 51200;
		$buf = $ENV{QUERY_STRING};
	}
	
	for my $pair (split /&/, $buf) {
		($k,$v) = split /=/, $pair;
		$v =~ tr/+/ /;
		$v =~ s/%([0-9A-Fa-f][0-9A-Fa-f])/pack 'H2', $1/eg;

		# �L���u����
		$v =~ s/&/&amp/g;
		$v =~ s/;/&#59;/g;
		$v =~ s/&amp/&amp;/g;
		$v =~ s/,/&#44;/g;
		$v =~ s/</&lt;/g;
		$v =~ s/>/&gt;/g;
		$v =~ s/"/&quot;/g;
		$v =~ tr/\x0D\x0A//d; # ���s�폜

		$in{$k} = $v;
		push @delfiles, $v if $k eq 'delete';
	}
	
	# �悭�g���̂ŊȒP�ȕϐ��ɑ��
	$com  = $in{comment};
	$id   = $in{id};
	$pass = $in{pass};
	&error("�{�����������܂�(���p$max_comment�����܂�)",1) if length $com > $max_comment; # �ő啶��������
}

#================================================
# �A�N�Z�X�`�F�b�N Get $addr $host $agent
#================================================
sub access_check {
	$addr = $ENV{REMOTE_ADDR};
	$host = $ENV{REMOTE_HOST};
	$host = $addr if $host eq '';

	for my $deny (@deny_lists) {
		$deny =~ s/\./\\\./g;
		$deny =~ s/\*/\.\*/g;
		&error($deny_message, 1) if $addr =~ /^$deny$/i;
		&error($deny_message, 1) if $host =~ /^$deny$/i;
	}
}

#================================================
# ���Ԏ擾 Get $time $date
#================================================
sub get_date {
	$time = time();
	my($min,$hour,$mday,$mon,$year) = (localtime($time))[1..4];
	$date = sprintf("%d/%d %02d:%02d", $mon+1,$mday,$hour,$min);
}

#================================================
# header
#================================================
sub header {
	print "Content-type: text/html; charset=Shift_JIS\n";
	if ($gzip ne '' && $ENV{HTTP_ACCEPT_ENCODING} =~ /gzip/){  
		if ($ENV{HTTP_ACCEPT_ENCODING} =~ /x-gzip/) {
			print "Content-encoding: x-gzip\n\n";
		}
		else{
			print "Content-encoding: gzip\n\n";
		}
		open STDOUT, "| $gzip -1 -c";
	}
	else {
		print "\n";
	}
	
	my $meta_refresh = $in{reload_time} ? qq|<meta http-equiv="refresh" content="$reload_times[$in{reload_time}];URL=$script?id=$id&pass=$pass&is_auto=1&reload_time=$in{reload_time}" />| : '';

	print <<"EOM";
<html>
<head>
<meta http-equiv="Cache-Control" content="no-cache" />
<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS" />
$meta_refresh
<link rel="shortcut icon" href="$htmldir/favicon.ico" />
<link rel="stylesheet" type="text/css" href="$htmldir/party.css" />
<title>$title</title>
<script type="text/javascript" src="$htmldir/party.js"></script>
</head>
<body onLoad="text_focus()">
EOM
}
#================================================
# footer
#================================================
sub footer {
	print qq|<div id="footer">|;
	print qq|+ ���p�[�e�B�[II Ver$VERSION <a href="http://cgi-sweets.com/" target="_blank">CGI-Sweets</a> <a href="http://amaraku.net/" target="_blank">Ama�y.net</a>|; # ����\��:�폜�E��\�� �֎~!!
	print qq|$copyright +</div></body></html>|;
}

#==========================================================
# �G���[��ʕ\��
#==========================================================
sub error {
	my($error_mes, $is_need_header) = @_;
	
	&header if $is_need_header;
	print qq|<br /><div class="mes">$error_mes<br /><br /></div>\n|;
	print qq|<form action="$script_index"><p><input type="submit" value="�s�n�o" /></p></form>|;
	&footer;
	exit;
}

#================================================
# �A�C�e���𑗂�
#================================================
sub send_item {
	my($send_name, $kind, $no, $send_from) = @_;
	my $send_id = unpack 'H*', $send_name;
	
	if (-f "$userdir/$send_id/depot.cgi") {
		open my $fh, ">> $userdir/$send_id/depot.cgi";
		print $fh "$kind<>$no<>\n";
		close $fh;
		
		if ($send_from) {
			my $item_name = $kind eq '1' ? $weas[$no][1]
						  : $kind eq '2' ? $arms[$no][1]
						  :				   $ites[$no][1]
						  ;
			open my $fh2, ">> $userdir/$send_id/send_item_mes.cgi";
			print $fh2 "�a���菊��$send_from����$item_name���͂��Ă��܂�\n";
			close $fh2; 
		}
	}
}

#================================================
# ���v���C���[�ɂ����𑗋�
#================================================
sub send_money {
	my($send_name, $money, $message) = @_;
	my $send_id = unpack 'H*', $send_name;
	$message ||= "$send_name����̑���";

	if (-f "$userdir/$send_id/money.cgi") {
		open my $fh, ">> $userdir/$send_id/money.cgi";
		print $fh "$money<>$message<>\n";
		close $fh;

		open my $fh2, "> $userdir/$send_id/money_flag.cgi";
		close $fh2; 
	}
}

#================================================
# �����ް��ύX
#================================================
# �g����: &regist_you_data('����̖��O', '�ύX�������ϐ�', '�l');
sub regist_you_data {
	my($name, $k, $v) = @_;
	return if $name eq '' || $k eq '';
	
	if ($m eq $name) {
		$m{$k} = $v;
	}
	else {
		my $y_id = unpack 'H*', $name;
		return unless -f "$userdir/$y_id/user.cgi";
		
		open my $fh, "+< $userdir/$y_id/user.cgi" or &error("$userdir/$y_id/user.cgi�t�@�C�����J���܂���");
		eval { flock $fh, 2; };
		my $line = <$fh>;
		if ($line) {
			$line =~ s/<>($k;).*?<>/<>$1$v<>/;
			seek  $fh, 0, 0;
			truncate $fh, 0;
			print $fh $line;
		}
		close $fh;
	}
}

#================================================
# �����ް���Get �߂�l�̓n�b�V��
#================================================
# �g����: &get_you_datas('����̖��O');
sub get_you_datas {
	my($name, $is_unpack) = @_;
	
	my $y_id = '';
	if ($is_unpack) {
		return %m if $id eq $name;
		$y_id = $name;
	}
	else {
		return %m if $m eq $name;
		$y_id = unpack 'H*', $name;
	}
	
	open my $fh, "< $userdir/$y_id/user.cgi" or &error("$name���̂悤�ȃv���C���[�͑��݂��܂���");
	my $line = <$fh>;
	close $fh;
	
	%you_datas = ();
	for my $hash (split /<>/, $line) {
		my($k, $v) = split /;/, $hash;
		$you_datas{$k} = $v;
	}

	return %you_datas;
}

#=================================================
# �f�B���N�g�����ƍ폜
#=================================================
sub delete_directory {
	my $dir_name = shift;
	
	opendir my $dh, "$dir_name" or &error("$dir_name�f�B���N�g�����J���܂���");
	while (my $file_name = readdir $dh) {
		next if $file_name =~ /^\./;
		unlink "$dir_name/$file_name" or &error("$dir_name/$file_name�t�@�C�����폜�ł��܂���");
	}
	closedir $dh;
	rmdir "$dir_name";
}

#=================================================
# ���낮������
#=================================================
sub roguauto {
	$mes = "���O�A�E�g���܂����H";
	&leave_member($m);

	print <<"EOM";
<script type="text/javascript"><!--
	location.href="$script_index";
// --></script>
<noscript>
	<div>���O�A�E�g���܂����H</div>
	<form method="$method" action="$script_index">
		<input type="submit" value="�����O�A�E�g" class="button_s" />
	</form>
</noscript>
EOM
}

#=================================================
# �����o�[���珜��
#=================================================
sub leave_member {
	my $y = shift;
	
	my @lines = ();
	open my $fh, "+< ${this_file}_member.cgi" or &error("${this_file}_member.cgi�t�@�C�������J���܂���"); 
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($ltime, $is_npc, $name, $laddr, $icon, $color, $guild) = split /<>/, $line;
		next if !$is_npc && $name eq $y;
		push @lines, $line;
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}

#================================================
# �o�^�Ґ�
#================================================
sub get_entry_count {
	open my $fh, "< $logdir/entry.cgi" or &error("$logdir/entry.cgi�t�@�C�����ǂݍ��߂܂���");
	my $line = <$fh>;
	close $fh;
	my($entry_count) = (split /<>/, $line)[0];
	return $entry_count;
}

#================================================
# �o�^�Ґ��}�C�i�X
#================================================
sub minus_entry_count {
	my $count = shift || 1;

	open my $fh, "+< $logdir/entry.cgi" or &error("$logdir/entry.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	my $line = <$fh>;
	my($entry_count, $last_addr) = split /<>/, $line;
	$entry_count -= $count;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh "$entry_count<>$last_addr<>";
	close $fh;
}

#================================================
# �u���b�N���X�g�ɒǉ�
#================================================
sub add_black_list {
	my $baddr = shift;
	open my $fh, ">> $logdir/black_list.cgi" or &error("$logdir/black_list.cgi�t�@�C�����J���܂���");
	print $fh "$baddr,";
	close $fh;
}

#================================================
# �Ǖ��\���ǉ�
#================================================
sub add_exile {
	my($bad_name, $because) = @_;
	
	my $is_find = 0;
	my @lines = ();
	open my $fh, "+< $logdir/violator.cgi" or &error("$logdir/violator.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($name, $violator, $message, $yess, $noss) = split /<>/, $line;
		
		# �Ǖ��\�����o�Ă��Ă���Ɉᔽ�s�ׂ������ꍇ�{�P�[
		if ($bad_name eq $violator) {
			$line = "$name<>$violator<>$message<>$yess,@�Ǖ��R�m<>$noss<>\n";
			$is_find = 1;
		}
		push @lines, $line;
	}
	push @lines, "@�Ǖ��R�m<>$bad_name<>$because<>@�Ǖ��R�m<><>\n" unless $is_find;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}

#================================================
# �莆�𑗂�
#================================================
sub send_letter {
	my($send_name, $send_message) = @_;

	my $yid = unpack 'H*', $send_name;
	unless (-f "$userdir/$yid/letter.cgi") {
		$mes = "$send_name�Ƃ����v���C���[�����݂��܂���";
		return;
	}

	my $new_line = "$time<>$date<>$m<>$addr<>$m{color}<>$send_message<><>\n";
	my @lines = ();
	open my $fh, "+< $userdir/$yid/letter.cgi" or &error("$userdir/$yid/letter.cgi�t�@�C�����ǂݍ��߂܂���");
	eval { flock $fh, 2; };
	my $head_line = <$fh>;
	my($ltime, $name) = (split /<>/, $head_line)[0,2];
	if ($name eq $m && $ltime + $bad_time > $time) {
		$mes = "�A���Ŏ莆�𑗂邱�Ƃ͂ł��܂���B���΂炭���Ă��瑗���Ă�������";
		return;
	}
	push @lines, $head_line;
	while (my $line = <$fh>) {
		push @lines, $line;
		last if @lines+1 >= $max_log;
	}
	unshift @lines, $new_line;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	open my $fh3, "> $userdir/$yid/letter_flag.cgi";
	close $fh3; 
}

#================================================
# �M���h�f�[�^��ҏW
#================================================
sub regist_guild_data {
	my($k, $v, $guild_name) = @_;
	
	$guild_name ||= $m{guild};
	return unless $guild_name;
	my $gid = unpack 'H*', $guild_name;
	unless (-f "$guilddir/$gid/data.cgi") {
		$mes = "$guild_name�M���h�����݂��܂���";
		return;
	}

	open my $fh, "+< $guilddir/$gid/data.cgi" or &error("$guilddir/$gid/data.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	my $line = <$fh>;
	my($gname,$gmaster,$gcolor,$gbgimg,$gmes,$gpoint) = split /<>/, $line;
	if    ($k eq 'master') { $gmaster = $v }
	elsif ($k eq 'color')  { $gcolor  = $v }
	elsif ($k eq 'bgimg')  { $gbgimg  = $v }
	elsif ($k eq 'mes')    { $gmes    = $v }
	elsif ($k eq 'point')  { $gpoint += $v }
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh "$gname<>$gmaster<>$gcolor<>$gbgimg<>$gmes<>$gpoint<>";
	close $fh;
}


#=================================================
# �M���h�����o�[����폜
#=================================================
sub delete_guild_member {
	my($gname, $delete_name) = @_;
	
	my $gid = unpack 'H*', $gname;
	return unless -f "$guilddir/$gid/member.cgi";
	
	my @lines = ();
	open my $fh, "< $guilddir/$gid/member.cgi" or &error("$guilddir/$gid/member.cgi�t�@�C�����ǂݍ��߂܂���");
	while (my $line = <$fh>) {
		push @lines, $line;
	}
	close $fh;
	
	# �Ō�̂P�l�̏ꍇ�̓M���h�폜
	if (@lines <= 1) {
		&delete_directory("$guilddir/$gid");
		&write_news(qq|<span class="die">$gname �M���h�����U���܂���</span>|);
	}
	else {
		my($guild_master) = (split /<>/, $lines[0])[0];
		
		# �M���}�X���E��
		if ($delete_name eq $guild_master) {
			shift @lines;
			
			# �M���}�X����T��(��E��[�M���}�X]���܂܂�Ă���l�B���Ȃ���΂Q�ԖڂɃ����o�[�ɂȂ����l)
			my $is_find = 0;
			for my $i (0 .. $#lines) {
				my($name, $position) = split /<>/, $lines[$i];
				if ($position =~ /�M���}�X/) {
					$is_find = 1;
					splice(@lines, $i, 1);
					unshift @lines, "$name<>�M���}�X<>\n";
					&regist_guild_data('master', $name, $gname);
					last;
				}
			}
			
			# �Q�Ԗڂ̐l
			unless ($is_find) {
				my($name, $position) = split /<>/, $lines[0];
				$lines[0] = "$name<>�M���}�X<>\n";
				&regist_guild_data('master', $name, $gname);
			}
		}
		else {
			for my $i (0 .. $#lines) {
				my($name, $position) = split /<>/, $lines[$i];
				if ($delete_name eq $name) {
					splice(@lines, $i, 1);
					last;
				}
			}
		}
		open my $fh2, "> $guilddir/$gid/member.cgi";
		print $fh2 @lines;
		close $fh2;
	}
}

#================================================
# �����̃M���h�f�[�^�擾
#================================================
sub read_guild_data {
	unless ($m{guild}) {
		$m{lib}='';
		&write_user;
		&error("�M���h�ɎQ�����Ă��܂���");
	}
	
	my $g_id = unpack 'H*', $m{guild};
	unless (-f "$guilddir/$g_id/data.cgi") {
		my $name  = $m{guild};
		$m{guild} = $m{lib} = '';
		&write_user;
		&error("$name�͉��U���Ă��܂����悤�ł�");
	}

	open my $fh, "< $guilddir/$g_id/data.cgi" or &error("$guilddir/$g_id/data.cgi�t�@�C�����J���܂���");
	my $line = <$fh>;
	close $fh;
	
	return $g_id, split /<>/, $line;
}

#================================================
# �R�s�[�B�g�����F&copy('�R�s�[����Path', '�R�s�[���Path');
#================================================
sub copy {
	my($from, $to) = @_;
	
	open my $in, "< $from" or &error("�R�s�[��$from�t�@�C�����ǂݍ��߂܂���");
	binmode $in;
	my @datas = <$in>;
	close $in;

	open my $out, "> $to" or &error("$from����$to�ɃR�s�[����̂����s���܂���");
	binmode $out;
	print $out @datas;
	close $out;
}

#================================================
# �O�Ղ̏������݁��v���C���[�����Ȃ��ꍇ�͎������g�B
# �g�����F&write_memory('���b�Z�[�W', '�v���C���[��');
#================================================
sub write_memory {
	my($message, $memory_name) = @_;
	my $yid;
	my %p;

	if ($memory_name) {
		$yid = unpack 'H*', $memory_name;
		return unless -f "$userdir/$yid/memory.cgi";
		%p = &get_you_datas($yid, 1);
	}
	else {
		$yid = $id;
		%p = %m;
	}
	
	my @lines = ();
	open my $fh, "+< $userdir/$yid/memory.cgi" or &error("$userdir/$yid/memory.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		push @lines, $line;
		last if @lines >= $max_log-1;
	}
	my $name = $p{guild} ? "$p{name}��$p{guild}" : "$p{name}";
	unshift @lines, qq|<span color="$p{color}"><img src="$icondir/$p{icon}" />$name�F $e2j{lv}$p{lv} $jobs[$p{job}][1]($p{sp}) $message <font size="1">($date)</font></span>\n|;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}

#=================================================
# ���݂̗a���Ă����
#=================================================
sub get_depot_c {
	# �ő�a���菊�ł̕ۑ���
	my $max_depot = $m{job_lv} >= 20 ? 100 : $m{job_lv} * 5 + 5;

	my $count = 0;
	open my $fh, "< $userdir/$id/depot.cgi" or &error("$userdir/$id/depot.cgi�t�@�C�����ǂݍ��߂܂���");
	++$count while <$fh>;
	close $fh;
	$m{is_full} = $count >= $max_depot ? 1 : 0;	
	return $count, $max_depot;
}
#================================================
# �a���Ă��郂���X�^�[�����t���̃`�F�b�N(�f�t�H���g�F50)
# ����������ꍇ�́wreturn $count >= 50 ? 1 : 0;�x��30�̕�����ύX
#================================================
sub is_full_monster {
	my $yid = shift;
	my $count = 0;
	open my $fh, "< $userdir/$yid/monster.cgi" or &error("$userdir/$yid/monster.cgi�t�@�C�����ǂݍ��߂܂���");
	++$count while <$fh>;
	close $fh;
	return $count >= 50 ? 1 : 0;
}

#================================================
# �`���̃v���C���[��������
#================================================
sub write_legend {
	my $file = shift;
	
	my @lines = ();
	open my $fh, "+< $logdir/$file.cgi" or &error("$logdir/$file.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		push @lines, $line;
		last if @lines >= $max_log-1;
	}
	unshift @lines, "$m{name}<>$m{guild}<>$m{color}<>$m{icon}<>$m{mes}<>$date<>\n";;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}

#================================================
# ���Z��A�M���h��̃S�[���h�A�M���h�|�C���g�̑���
#================================================
sub add_bet {
	my($quest_id, $add_bet, $is_casino) = @_;

	open my $fh, "+< $questdir/$quest_id/bet.cgi" or &error("$questdir/$quest_id/bet.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	my $bet = <$fh>;
	$bet =~ tr/\x0D\x0A//d;
	$bet += $add_bet;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh $bet;
	close $fh;
}

#================================================
# �ŋ߂̑傫�ȏo����
#================================================
sub write_news {
	my $message = shift;

	my @lines = ();
	open my $fh, "+< $logdir/news.cgi" or &error("$logdir/news.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		push @lines, $line;
		last if @lines >= $max_log-1;
	}
	unshift @lines, qq|$message <font size="1">($date)</font>\n|;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}


#=========================================================
# ���O�C�������o�[�擾
#=========================================================
sub get_login_member {
	my @lines = ();
	my %sames = ();
	my $list  = '';
	open my $fh, "+< $logdir/login.cgi" or &error("$logdir/login.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($ltime, $name, $color, $guild, $message, $icon) = split /<>/, $line;
		next if $time > $ltime + $login_time * 60;
		next if ++$sames{$name} > 1;
		
		my $yid = unpack 'H*', $name;
		$list .= qq|<div style="color: $color;"><a href="player.cgi?id=$yid" style="color: $color; text-decoration: none;" target="_blank"><img src="$icondir/$icon" />$name</a>|;
		$list .= qq|��$guild| if $guild;
		$list .= qq|��$message</div>\n|;
		
		++$count;
		push @lines, $line;
	}
	seek $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	my $login_count = @lines;
	return ($list, $login_count);
}
sub get_header_data { return }

#=========================================================
# �菕���N�G�X�g�ň˗�����Ă���A�C�e��No�̎擾 weapon.cgi, armor.cgi, item.cgi, secret.cgi
#=========================================================
sub get_helper_item {
	my $gkind = shift;

	my $gno = ',';
	open my $fh, "< $logdir/helper_quest.cgi" or &error("$logdir/helper_quest.cgi�t�@�C�����J���܂���");
	while (my $line = <$fh>) {
		my($limit_time,$limit_date,$name,$is_guild,$pay,$kind,$no,$need_c) = split /<>/, $line;
		$gno .= "$no," if $gkind eq $kind;
	}
	close $fh;
	return $gno;
}

sub get_header_data { return }


1; # �폜�s��
