#=================================================
# �`�������E�쐬 Created by Merino
# type: 1:�ʏ�,2:�_���W����,3:�`�������W,4:���Z��,5:�M���h��,6:�����
#=================================================
# �ꏊ��
$this_title = '�`�����̃p�[�e�B�[';

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$logdir/quest";

# �w�i�摜
$bgimg   = "$bgimgdir/quest.gif";

# �p�[�e�B�[���A���Z�ꖼ�̍ő啶����(���p)
$max_title = 50;

# �ő�p�[�e�B�[�l��
$max_party = 4;

# ���Z��ő�Q���l��
$max_colosseum = 8;

# ���Z��Œ�q����(G)
$min_bet = 10;

# �i�s�X�s�[�h
%speeds = (
#	�b��	=> ['�Z���N�g��', "�摜�t�@�C��"],
	12		=> ['��������', "$icondir/etc/speed_sakusaku.gif"],
	18		=> ['�܂�����', "$icondir/etc/speed_mattari.gif"],
	25		=> ['��������', "$icondir/etc/speed_jikkuri.gif"],
);


# ���u�N�G�X�g(���O�̍X�V�Ȃ�)�̎����폜����(�b)
$auto_delete_quest_time = 1800;


#=================================================
# ��ʃw�b�_�[
#=================================================
sub header_html {
	my $my_at = $m{at} + $weas[$m{wea}][3];
	my $my_df = $m{df} + $arms[$m{arm}][3];
	my $my_ag = $m{ag} - $weas[$m{wea}][4] - $arms[$m{arm}][4];
	$my_ag = 0 if $my_ag < 0;
	print qq|<div class="mes">�y$this_title�z $e2j{tired}�F<b>$m{tired}</b>�� �S�[���h�F<b>$m{money}</b>G / $e2j{mhp}�F<b>$m{hp}</b>/<b>$m{mhp}</b> / $e2j{mmp}�F<b>$m{mp}</b>/<b>$m{mmp}</b>|;
	print qq| / $e2j{at}�F<b>$my_at</b> / $e2j{df}�F<b>$my_df</b> / $e2j{ag}�F<b>$my_ag</b> /|;
	print qq| E�F$weas[$m{wea}][1]| if $m{wea};
	print qq| E�F$arms[$m{arm}][1]| if $m{arm};
	print qq| E�F$ites[$m{ite}][1]| if $m{ite};
	print qq|</div>|;
	print qq|<div class="view">|;
	&quest_html;
	print qq|</div>|;
}

#=================================================
# �N�G�X�g(�p�[�e�B�[)�ꗗ
#=================================================
sub quest_html {
	opendir my $dh, "$questdir" or &error("$questdir�f�B���N�g�����J���܂���");
	while (my $dir_name = readdir $dh) {
		next if $dir_name =~ /\./;
		
		# ���u�N�G�X�g�폜(30���ȏネ�O�̍X�V�Ȃ�)
		my($mtime) = (stat("$questdir/$dir_name/log.cgi"))[9];
		if ($time > $mtime + $auto_delete_quest_time) {
			&auto_delete_quest($dir_name);
			next;
		}

		open my $fh, "< $questdir/$dir_name/member.cgi";
		my $head_line = <$fh>;
		my($speed,$stage,$round,$leader,$p_name,$p_pass,$p_join,$win,$bet,$is_visit,$need_join,$type,$map,$py,$px,$event) = split /<>/, $head_line;
		my $count = 1;
		my $p = qq| <span onclick="text_set('������ׂ�>$leader ')"><img src="$icondir/etc/mark_leader.gif" alt="���[�_�[" />$leader</span> / |;
		while (my $line = <$fh>) {
			my($name,$laddr,$color) = split /<>/, $line;
			next if $name =~ /^@/;
			next if $leader eq $name;
			$p .= qq|<span onclick="text_set('������ׂ�>$name ')">$name</span> / |;
			++$count;
		}
		close $fh;
		
		my $party_data = qq|$p_name <img src="$speeds{$speed}[1]" alt="$speeds{$speed}[0]" /> |;
		$party_data .= $type eq '1' ? qq|$stages[$stage]|
					:  $type eq '2' ? qq|<img src="$icondir/etc/mark_dungeon.gif" alt="�_���W����" />$dungeons[$stage]|
					:  $type eq '3' ? qq|<img src="$icondir/etc/mark_challenge.gif" alt="�`�������W" />$challenges[$stage]|
					:  $type eq '4' ? qq|<img src="$icondir/etc/mark_arena.gif" alt="���Z��" /> �q���� <b>$bet</b>�f|
					:  $type eq '5' ? qq|<img src="$icondir/etc/mark_guild.gif" alt="�M���h��" />|
					:  '' ;
		$party_data .= qq| �y<b>$count</b>/<b>$p_join</b>�z|;
		
		if ($need_join) {
			my($need_k, $need_v, $need_uo) = split /_/, $need_join;
			if ($need_k eq 'hp') {
				$party_data .= $need_uo eq 'u' ? "��$e2j{hp}$need_v������" : "��$e2j{hp}$need_v�ȏず";
			}
			elsif ($need_k eq 'joblv')  {
				if ($need_uo eq 'u') {
					if    ($need_v <= 3) { $party_data .= '�����S�Ҋ��}��';   }
				}
				else {
					if    ($need_v >= 3)  { $party_data .= '�����S�҂��f��I��'; }
					elsif ($need_v >= 10) { $party_data .= '���n���҂̂݁I��'; }
				}
			}
		}
		my $aikotoba = $p_pass ? '���������Ƃ�>' : ' ';
		if ($type eq '6') {
			print $count >= $p_join || $round > 1
				? qq|<span onclick="text_set('�����񂪂�>$p_name')"><img src="$icondir/etc/vs_king.gif" alt="�����" /> $party_data</span>$p<hr size="1" />|
				: qq|<span onclick="text_set('������>$p_name')"><img src="$icondir/etc/vs_king.gif" alt="�����" /> $party_data</span>$p<hr size="1" />|;
		}
		elsif ($round > 0) {
			print !$is_visit
				? qq|<img src="$icondir/etc/playing.gif" alt="�N�G�X�g��" /> $party_data ���w�~ $p<hr size="1" />|
				: qq|<span onclick="text_set('�����񂪂�>$p_name$aikotoba')"><img src="$icondir/etc/playing.gif" alt="�N�G�X�g��" /> $party_data</span>$p<hr size="1" />|;
		}
		elsif ($count >= $p_join) {
			print !$is_visit
				? qq|<img src="$icondir/etc/full.gif" alt="�܂񂢂�" /> $party_data ���w�~ $p<hr size="1" />|
				: qq|<span onclick="text_set('�����񂪂�>$p_name$aikotoba')"><img src="$icondir/etc/full.gif" alt="�܂񂢂�" /> $party_data</span>$p<hr size="1" />|;
		}
		else {
			print qq|<span onclick="text_set('������>$p_name$aikotoba')"><img src="$icondir/etc/waitting.gif" alt="��������" /> $party_data</span>$p<hr size="1" />|;
		}
	}
	closedir $dh;
}
sub auto_delete_quest { # ���u�����폜
	my $dir_name = shift;
	open my $fh, "< $questdir/$dir_name/member.cgi";
	my $head_line = <$fh>;
	while (my $line = <$fh>) {
		my($name,$color) = (split /<>/, $line)[0,2];
		next if $color eq $npc_color;
		&regist_you_data($name, 'lib', '');
		&regist_you_data($name, 'sleep', 3600);
	}
	close $fh;
	&delete_directory("$questdir/$dir_name");
}

#=================================================
# �ǉ��A�N�V����
#=================================================
push @actions, '����';
push @actions, '����';
push @actions, '���񂪂�';
$actions{'����'}   = sub{ &tsukuru }; 
$actions{'����'}   = sub{ &sanka }; 
$actions{'���񂪂�'} = sub{ &kengaku }; 
$actions{'�p�[�e�B�['}   = sub{ &party }; 
$actions{'�Ƃ������傤'} = sub{ &tougijyou }; 
$actions{'�M���h�o�g��'} = sub{ &girudobatoru }; 
$actions{'�_���W����'}   = sub{ &dungeon }; 
$actions{'�`�������W'}   = sub{ &challenge }; 


#=================================================
# ������
#=================================================
sub tsukuru {
	# �X�e�[�W
	my $stage_select = qq|<select name="stage" class="select1">|;
	for my $i (0 .. 14) {
		$stage_select .= qq|<option value="$i">$stages[$i]</option>|;
		last if $i > $m{job_lv}+1;
	}
	$stage_select .= qq|</select>|;

	# �_���W����
	my $dungeon_select = qq|<select name="stage" class="select1">|;
	for my $i (0 .. $#dungeons) {
		$dungeon_select .= qq|<option value="$i">$dungeons[$i]</option>|;
		last if ($i+1) * 2 >= $m{job_lv};
	}
	$dungeon_select .= qq|</select>|;
	
	# �`�������W
	my $challenge_select = qq|<select name="stage" class="select1">|;
	for my $i (0 .. $#challenges) {
		$challenge_select .= qq|<option value="$i">$challenges[$i]</option>|;
		last if ($i+1) * 3 >= $m{job_lv};
	}
	$challenge_select .= qq|</select>|;

	# �ΐ퐔(���Z��p)
	my $round_select = qq|<select name="win" class="select1">|;
	for my $i (1 .. 3) {
		$round_select .= qq|<option value="$i">$i��揟</option>|;
	}
	$round_select .= qq|</select>|;
	
	# �`���Q���l��
	my $join_select = qq|<select name="p_join" class="select1">|;
	for my $i (1 .. $max_party-1) {
		$join_select .= qq|<option value="$i">$i�l</option>|;
	}
	$join_select .= qq|<option value="$max_party" selected="selected">$max_party�l</option>|;
	$join_select .= qq|</select>|;

	# ���Z��Q���l��
	my $join_select2 = qq|<select name="p_join" class="select1">|;
	for my $i (2 .. $max_colosseum-1) {
		$join_select2 .= qq|<option value="$i">$i�l</option>|;
	}
	$join_select2 .= qq|<option value="$max_colosseum" selected="selected">$max_colosseum�l</option>|;
	$join_select2 .= qq|</select>|;

	# �i�s���x
	my $speed_select = qq|<select name="speed" class="select1">|;
	for my $k (sort { $a <=> $b } keys %speeds) {
		$speed_select .= qq|<option value="$k">$speeds{$k}[0]</option>|;
	}
	$speed_select .= qq|</select>|;
	
	# �Q������
	my $need_join = <<"EOM";
	<select name="need_join" class="select1">
		<option value="0">�Ȃ�</option>
		<option value="joblv_3_u">���S��</option>
		<option value="joblv_3_o">�����҈ȏ�</option>
		<option value="joblv_10_o">�㋉�҈ȏ�</option>
		<option value="hp_100_u">�g�o100����</option>
		<option value="hp_100_o">�g�o100�ȏ�</option>
		<option value="hp_200_u">�g�o200����</option>
		<option value="hp_200_o">�g�o200�ȏ�</option>
		<option value="hp_300_u">�g�o300����</option>
		<option value="hp_300_o">�g�o300�ȏ�</option>
		<option value="hp_400_u">�g�o400����</option>
		<option value="hp_400_o">�g�o400�ȏ�</option>
	</select>
EOM
	
	
	$mes = <<"EOM";
<table><tr><td valign="top">
<form method="$method" action="$script">
	<input type="hidden" name="comment" value="���p�[�e�B�[" />
	<input type="hidden" name="id" value="$id" /><input type="hidden" name="pass" value="$pass" />
	<table class="table1">
		<tr><td>�p�[�e�B�[���F</td><td><input type="text" name="p_name" class="text_box1" /></td></tr>
		<tr><td>�i�s���x�F</td><td>$speed_select</td></tr>
		<tr><td>�Q���l���F</td><td>$join_select</td></tr>
		<tr><td>�`���ꏊ�F</td><td>$stage_select</td></tr>
		<tr><td>�Q�������F</td><td>$need_join</td></tr>
		<tr><td>�����t�F</td><td><input type="text" name="p_pass" class="text_box_s" />�@</td></tr>
		<tr><td>���w�F<input type="checkbox" name="is_visit" value="1" checked="checked"></td><td><input type="submit" value="���p�[�e�B�[" /></td></tr>
	</table>
</form>
EOM
	if ($m{job_lv} > 0) {
		$mes .= <<"EOM";
</td><td valign="top">
<form method="$method" action="$script">
	<input type="hidden" name="comment" value="���_���W����" />
	<input type="hidden" name="id" value="$id" /><input type="hidden" name="pass" value="$pass" />
	<table class="table1">
		<tr><td>�p�[�e�B�[���F</td><td><input type="text" name="p_name" class="text_box1" /></td></tr>
		<tr><td>�i�s���x�F</td><td>$speed_select</td></tr>
		<tr><td>�Q���l���F</td><td>$join_select</td></tr>
		<tr><td>�`���ꏊ�F</td><td>$dungeon_select</td></tr>
		<tr><td>�Q�������F</td><td>$need_join</td></tr>
		<tr><td>�����t�F</td><td><input type="text" name="p_pass" class="text_box_s" />�@</td></tr>
		<tr><td>���w�F<input type="checkbox" name="is_visit" value="1" checked="checked"></td><td><input type="submit" value="���_���W����" /></td></tr>
	</table>
</form>
</td></tr><tr><td valign="top">
<form method="$method" action="$script">
	<input type="hidden" name="comment" value="���`�������W" />
	<input type="hidden" name="id" value="$id"><input type="hidden" name="pass" value="$pass" />
	<table class="table1">
		<tr><td>�`�������W���F</td><td><input type="text" name="p_name" class="text_box1" /></td></tr>
		<tr><td>�i�s���x�F</td><td>$speed_select</td></tr>
		<tr><td>����ꏊ�F</td><td>$challenge_select</td></tr>
		<tr><td>�����t�F</td><td><input type="text" name="p_pass" class="text_box_s" /></td></tr>
		<tr><td>���w�F<input type="checkbox" name="is_visit" value="1" checked="checked"></td><td><input type="submit" value="���`�������W" /></td></tr>
	</table>
</form>
EOM
}
	$mes .= <<"EOM";
</td><td valign="top">
<form method="$method" action="$script">
	<input type="hidden" name="comment" value="���Ƃ������傤" />
	<input type="hidden" name="id" value="$id"><input type="hidden" name="pass" value="$pass" />
	<table class="table1">
		<tr><td>���Z�ꖼ�F</td><td><input type="text" name="p_name" class="text_box1" /></td></tr>
		<tr><td>�i�s���x�F</td><td>$speed_select</td></tr>
		<tr><td>�Q���l���F</td><td>$join_select2</td></tr>
		<tr><td>�ΐ�ꏊ�F</td><td>$stage_select</td></tr>
		<tr><td>�q�����F</td><td><input type="text" name="bet" class="text_box_s" style="text-align: right;" value="$min_bet" />G</td></tr>
		<tr><td>�ΐ�񐔁F</td><td>$round_select</td></tr>
		<tr><td>�Q�������F</td><td>$need_join</td></tr>
		<tr><td>�����t�F</td><td><input type="text" name="p_pass" class="text_box_s" /></td></tr>
		<tr><td>���w�F<input type="checkbox" name="is_visit" value="1" checked="checked"></td><td><input type="submit" value="�����Z��" /></td></tr>
	</table>
</form>
EOM
	if ($m{guild}) {
		$mes .= <<"EOM";
</td><td valign="top">
<form method="$method" action="$script">
	<input type="hidden" name="comment" value="���M���h�o�g��" />
	<input type="hidden" name="id" value="$id"><input type="hidden" name="pass" value="$pass" />
	<table class="table1">
		<tr><td>�M���h�햼�F</td><td><input type="text" name="p_name" class="text_box1" /></td></tr>
		<tr><td>�i�s���x�F</td><td>$speed_select</td></tr>
		<tr><td>�Q���l���F</td><td>$join_select2</td></tr>
		<tr><td>�ΐ�ꏊ�F</td><td>$stage_select</td></tr>
		<tr><td>�ΐ�񐔁F</td><td>$round_select</td></tr>
		<tr><td>�Q�������F</td><td>$need_join</td></tr>
		<tr><td>�����t�F</td><td><input type="text" name="p_pass" class="text_box_s" /></td></tr>
		<tr><td>���w�F<input type="checkbox" name="is_visit" value="1" checked="checked"></td><td><input type="submit" value="���M���h��" /></td></tr>
	</table>
</form>
EOM
	}
	$mes .= "</td></tr></table>";
}
#=================================================
# ���̓`�F�b�N
#=================================================
sub check_create_quest {
	my($p_name) = @_;

	$mes = qq|<span onclick="text_set('���ف[�� ')">$e2j{hp}���񕜂��Ă��������B�u���ف[�ށv�ŉƂɋA��u���˂�v�ŋx��ł�������</span>|	if $m{hp} <= 0;
	$mes = qq|<span onclick="text_set('���ف[�� ')">$e2j{tired}�����܂��Ă��܂��B�u���ف[�ށv�ŉƂɋA��u���˂�v�ŋx��ł�������</span>|	if $m{tired} >= 100;
	return if $mes;

	if ($p_name eq '���Z��') {
		$mes = "�q�����͍Œ�ł� $min_bet G�K�v�ł�"	if $in{bet} < $min_bet;
		$mes = "�q�����͍Œ�ł� 1 G�K�v�ł�"			if $in{bet} < 1;
		$mes = "�q����������܂���"						if $in{bet} > $m{money};
		$mes = "�q�������ُ�ł�"						if $in{bet} =~ /[^0-9]/;
		$in{bet} = int($in{bet});
	}
	elsif ($p_name eq '�M���h��') {
		if ($m{guild}) {
			my($gid,$gname,$gmaster,$gcolor,$gbgimg,$gmes,$gpoint) = &read_guild_data;
			$mes = "���ǂ��M���h�̓M���h������邱�Ƃ͂ł��܂���" if $gcolor eq $default_color;
		}
		else {
			$mes = "�M���h�ɎQ�����Ă��܂���";
		}
	}
	return if $mes;
	
	# �Q������	
	if ($in{need_join}) {
		my($need_key, $need_value, $need_uo) = split /_/, $in{need_join};
		$mes = "�Q�������w�g�o��$need_value�����x�𖞂����Ă��܂���"		if $need_key eq 'hp'    && $need_uo eq 'u' && $m{mhp}    >= $need_value;
		$mes = "�Q�������w�g�o��$need_value�ȏ�x�𖞂����Ă��܂���"		if $need_key eq 'hp'    && $need_uo eq 'o' && $m{mhp}    <  $need_value;
		$mes = "�Q�������w�]�E�񐔂�$need_value�񖢖��x�𖞂����Ă��܂���"	if $need_key eq 'joblv' && $need_uo eq 'u' && $m{job_lv} >= $need_value;
		$mes = "�Q�������w�]�E�񐔂�$need_value��ȏ�x�𖞂����Ă��܂���"	if $need_key eq 'joblv' && $need_uo eq 'o' && $m{job_lv} <  $need_value;
		return if $mes;
	}
	
	if ($p_name eq '�p�[�e�B�[') {
		$mes = "�Q���l�����ُ�ł�"		if $in{p_join} < 1 || $in{p_join} > $max_party;
		$mes = "�`���ꏊ���ُ�ł�"		if $in{stage}  < 0 || $in{stage} > $#stages || $in{stage} > $m{job_lv}+2;
	}
	elsif ($p_name eq '�_���W����') {
		$mes = "�Q���l�����ُ�ł�"		if $in{p_join} < 1 || $in{p_join} > $max_party;
		$mes = "�`���ꏊ���ُ�ł�"		if $in{stage}  < 0 || $in{stage} > $#dungeons || $in{stage} * 2 > $m{job_lv}+1;
	}
	elsif ($p_name eq '�`�������W') {

	}
	else {
		$mes = "�Q���l�����ُ�ł�"		if $in{p_join} < 2 || $in{p_join} > $max_colosseum;
		$mes = "�ΐ�񐔂��ُ�ł�"		if $in{win}    < 1 || $in{win} > 4;
		$mes = "�ΐ�ꏊ���ُ�ł�"		if $in{stage}  < 0 || $in{stage} > $#stages || $in{stage} > $m{job_lv}+2;
	}
	return if $mes;

	$in{is_visit} = 1 if $in{is_visit} =~ /[^01]/;
	$mes = "�i�s���x���ُ�ł�"		unless defined $speeds{$in{speed}};
	$mes = "$p_name���͔��p$max_title�����܂łł�"						if length($in{p_name}) > $max_title;
	$mes = "$p_name���ɕs���ȋ󔒂��܂܂�Ă��܂�"						if $in{p_name} =~ /�@|\s/;
	$mes = "$p_name���ɕs���ȕ���( ,;\"\'&<>\\\/@ )���܂܂�Ă��܂�"	if $in{p_name} =~ /[,;\"\'&<>\\\/@]/;
	$mes = "$p_name���ɕs���ȕ���( �� )���܂܂�Ă��܂�"				if $in{p_name} =~ /��/;
	$mes = "$p_name�������߂Ă�������"	unless $in{p_name};
}
#=================================================
# ���p�[�e�B�[
#=================================================
sub party {
	&check_create_quest('�p�[�e�B�[');
	return if $mes;

	my $quest_id = unpack 'H*', $in{p_name};
	$mes = "�����N�G�X�g��($in{p_name})�����łɑ��݂��܂�" if -d "$questdir/$quest_id";
	return if $mes;
	
	# �V�K�p�[�e�B�[�쐬
	mkdir "$questdir/$quest_id", $mkdir or &error("$questdir/$quest_id�f�B���N�g�����쐬�ł��܂���");
	open my $fh, "> $questdir/$quest_id/member.cgi" or &error("$questdir/$quest_id/member.cgi�t�@�C�����쐬�ł��܂���");
	print $fh "$in{speed}<>$in{stage}<>0<>$m<>$in{p_name}<>$in{p_pass}<>$in{p_join}<>0<>0<>$in{is_visit}<>$in{need_join}<>1<><>0<>0<><>\n";
	my $new_line = &get_battle_line($m{color},0);
	print $fh "$new_line\n";
	close $fh;
	chmod $chmod, "$questdir/$quest_id/member.cgi";
	
	open my $fh2, "> $questdir/$quest_id/log.cgi" or &error("$questdir/$quest_id/log.cgi�t�@�C�����쐬�ł��܂���");
	close $fh2;
	chmod $chmod, "$questdir/$quest_id/log.cgi";
	
	$m{lib}   = 'vs_monster';
	$m{quest} = $quest_id;
	
	$com = "<b>���p�[�e�B�[>$in{p_name}���`���ꏊ>$stages[$in{stage}]���Q���l��>$in{p_join}�l��$speeds{$in{speed}}[0]";
 	if ($in{p_pass}) {
		$com .= "�������t>�K�v";
	}
	else {
		$in{p_pass} = '�Ȃ�' ;
	}
	$com .= "</b>";
	&reload("$in{p_name}�p�[�e�B�[�����܂����I<br />�`���ꏊ�F$stages[$in{stage}]�C$speeds{$in{speed}}[0]�C�����t�F$in{p_pass}�C�Q���l���F$in{p_join}�l");
	&leave_member($m);
}
#=================================================
# ���_���W����
#=================================================
sub dungeon {
	&check_create_quest('�_���W����');
	return if $mes;

	my $quest_id = unpack 'H*', $in{p_name};
	$mes = "�����N�G�X�g��($in{p_name})�����łɑ��݂��܂�" if -d "$questdir/$quest_id";
	return if $mes;
	
	&get_dungeon_data;
	# �V�K�p�[�e�B�[�쐬
	mkdir "$questdir/$quest_id", $mkdir or &error("$questdir/$quest_id�f�B���N�g�����쐬�ł��܂���");
	open my $fh, "> $questdir/$quest_id/member.cgi" or &error("$questdir/$quest_id/member.cgi�t�@�C�����쐬�ł��܂���");
	print $fh "$in{speed}<>$in{stage}<>0<>$m<>$in{p_name}<>$in{p_pass}<>$in{p_join}<>0<>0<>$in{is_visit}<>$in{need_join}<>2<>$in{map}<>$in{py}<>$in{px}<>S<>\n";
	my $new_line = &get_battle_line($m{color},0);
	print $fh "$new_line\n";
	close $fh;
	chmod $chmod, "$questdir/$quest_id/member.cgi";
	
	open my $fh2, "> $questdir/$quest_id/log.cgi" or &error("$questdir/$quest_id/log.cgi�t�@�C�����쐬�ł��܂���");
	close $fh2;
	chmod $chmod, "$questdir/$quest_id/log.cgi";
	
	$m{lib}   = 'vs_dungeon';
	$m{quest} = $quest_id;
	
	$com = "<b>���_���W����>$in{p_name}���`���ꏊ>$dungeons[$in{stage}]���Q���l��>$in{p_join}�l��$speeds{$in{speed}}[0]";
 	if ($in{p_pass}) {
		$com .= "�������t>�K�v";
	}
	else {
		$in{p_pass} = '�Ȃ�' ;
	}
	$com .= "</b>";
	&reload("$in{p_name}�p�[�e�B�[�����܂����I<br />�`���ꏊ�F$dungeons[$in{stage}]�C$speeds{$in{speed}}[0]�C�����t�F$in{p_pass}�C�Q���l���F$in{p_join}�l");
	&leave_member($m);
}
sub get_dungeon_data {
	# �`������}�b�v�������_���őI��
	my @random_maps = ();
	opendir my $dh, "$mapdir/$in{stage}" or &error("$mapdir/$in{stage}�f�B���N�g�����J���܂���");
	while (my $file_name = readdir $dh) {
		next if $file_name =~ /^\./;
		next if $file_name =~ /_/;
		push @random_maps, $file_name;
	}
	closedir $dh;
	
	$in{map} = $random_maps[int rand @random_maps];
	$in{map} =~ s/^(.+)\..+$/$1/; # �g���q������
	
	&error("$mapdir/$in{stage}/$in{map}.cgi�_���W�����f�[�^�t�@�C����������܂���") unless -f "$mapdir/$in{stage}/$in{map}.cgi";
	require "$mapdir/$in{stage}/$in{map}.cgi";
	for my $y (0..$#maps) {
		for my $x (0..$#maps) {
			if ($maps[$y][$x] eq 'S') {
				$in{py} = $y;
				$in{px} = $x;
				return;
			}
		}
	}
	
	&error("$in{map} �X�^�[�g�n�_��������܂���");
}

#=================================================
# ���`�������W
#=================================================
sub challenge {
	$mes = "�`���ꏊ���ُ�ł�"		if $in{stage}  < 0 || $in{stage} > $#challenges || $in{stage} * 2 > $m{job_lv}+1;
	$mes = "���x���A�b�v���X�g�b�N������ԂŒ��킷�邱�Ƃ͂ł��܂���" if $m{lv} < 99 && $m{exp} >= $m{lv} * $m{lv} * 10;
	return if $mes;

	require "$challengedir/$in{stage}.cgi";

	$in{p_join}    = $k{p_join};
	$in{need_join} = $k{need_join};

	&check_create_quest('�`�������W');
	return if $mes;

	my $quest_id = unpack 'H*', $in{p_name};
	$mes = "�����N�G�X�g��($in{p_name})�����łɑ��݂��܂�" if -d "$questdir/$quest_id";
	return if $mes;
	
	# �ō��L�^���擾
	my $max_round = &get_max_round($in{stage});

	# �V�K�p�[�e�B�[�쐬
	mkdir "$questdir/$quest_id", $mkdir or &error("$questdir/$quest_id�f�B���N�g�����쐬�ł��܂���");
	open my $fh, "> $questdir/$quest_id/member.cgi" or &error("$questdir/$quest_id/member.cgi�t�@�C�����쐬�ł��܂���");
	print $fh "$in{speed}<>$in{stage}<>0<>$m<>$in{p_name}<>$in{p_pass}<>$in{p_join}<>$max_round<>0<>$in{is_visit}<>$in{need_join}<>3<><>0<>0<><>\n";
	my $new_line = &get_battle_line($m{color},0);
	print $fh "$new_line\n";
	close $fh;
	chmod $chmod, "$questdir/$quest_id/member.cgi";
	
	open my $fh2, "> $questdir/$quest_id/log.cgi" or &error("$questdir/$quest_id/log.cgi�t�@�C�����쐬�ł��܂���");
	close $fh2;
	chmod $chmod, "$questdir/$quest_id/log.cgi";
	
	$m{lib}   = 'vs_challenge';
	$m{quest} = $quest_id;
	
	$com = "<b>���`�������W>$in{p_name}���`���ꏊ>$challenges[$in{stage}]���Q���l��>$in{p_join}�l��$speeds{$in{speed}}[0]";
 	if ($in{p_pass}) {
		$com .= "�������t>�K�v";
	}
	else {
		$in{p_pass} = '�Ȃ�' ;
	}
	$com .= "</b>";
	&reload("$challenges[$in{stage}] �ɒ��킵�܂��I<br />$speeds{$in{speed}}[0]�C�����t�F$in{p_pass}�C�Q���l���F$in{p_join}�l");
	&leave_member($m);
}
sub get_max_round {
	my $stage = shift;
	
	open my $fh, "< $logdir/challenge$stage.cgi" or &error("$logdir/challenge$stage.cgi�t�@�C�����ǂݍ��߂܂���");
	my $line = <$fh>;
	close $fh;
	my($max_round) = (split /<>/, $line)[0];

	return $max_round;
}

#=================================================
# ���Ƃ������傤
#=================================================
sub tougijyou {
	&check_create_quest('���Z��');
	return if $mes;

	my $quest_id = unpack 'H*', $in{p_name};
	$mes = "�����N�G�X�g��($in{p_name})�����łɑ��݂��܂�" if -d "$questdir/$quest_id";
	return if $mes;
	
	# �V�K���Z��쐬
	mkdir "$questdir/$quest_id", $mkdir or &error("$questdir/$quest_id�f�B���N�g�����쐬�ł��܂���");
	open my $fh, "> $questdir/$quest_id/member.cgi" or &error("$questdir/$quest_id/member.cgi�t�@�C�����쐬�ł��܂���");
	print $fh "$in{speed}<>$in{stage}<>0<>$m<>$in{p_name}<>$in{p_pass}<>$in{p_join}<>$in{win}<>$in{bet}<>$in{is_visit}<>$in{need_join}<>4<><>0<>0<><>\n";
	my $new_line = &get_battle_line($default_color, 1);
	print $fh "$new_line\n";
	close $fh;
	chmod $chmod, "$questdir/$quest_id/member.cgi";
	
	for my $k (qw/log bet win/) {
		open my $fh2, "> $questdir/$quest_id/$k.cgi" or &error("$questdir/$quest_id/$k.cgi�t�@�C�����쐬�ł��܂���");
		close $fh2;
		chmod $chmod, "$questdir/$quest_id/$k.cgi";
	}
	&add_bet($quest_id, $in{bet});
	
	$m{money} -= $in{bet};
	$m{lib}   = 'vs_player';
	$m{quest} = $quest_id;
	
	$com = "<b>�����Z��>$in{p_name}���ΐ�ꏊ>$stages[$in{stage}]���q����>$in{bet} G���Q���l��>$in{p_join}�l��$speeds{$in{speed}}[0]";
 	if ($in{p_pass}) {
		$com .= "���������Ƃ�>�K�v";
	}
	else {
		$in{p_pass} = '�Ȃ�' ;
	}
	$com .= "</b>";
	&reload("���Z��u$in{p_name}�v�����܂����I<br />�ΐ�ꏊ�F$stages[$in{stage}]�C�q�����F$in{bet} G�C$speeds{$in{speed}}[0]�C�����t�F$in{p_pass}�C�Q���l���F$in{p_join}�l");
	&leave_member($m);
}
#=================================================
# ���M���h�o�g��
#=================================================
sub girudobatoru {
	&check_create_quest('�M���h��');
	return if $mes;
	
	my $quest_id = unpack 'H*', $in{p_name};
	$mes = "�����N�G�X�g��($in{p_name})�����łɑ��݂��܂�" if -d "$questdir/$quest_id";
	return if $mes;

	my($gid,$gname,$gmaster,$gcolor,$gbgimg,$gmes,$gpoint) = &read_guild_data;
	# �V�K���Z��쐬
	mkdir "$questdir/$quest_id", $mkdir or &error("$questdir/$quest_id�f�B���N�g�����쐬�ł��܂���");
	open my $fh, "> $questdir/$quest_id/member.cgi" or &error("$questdir/$quest_id/member.cgi�t�@�C�����쐬�ł��܂���");
	print $fh "$in{speed}<>$in{stage}<>0<>$m<>$in{p_name}<>$in{p_pass}<>$in{p_join}<>$in{win}<>0<>$in{is_visit}<>$in{need_join}<>5<><>0<>0<><>\n";
	my $new_line = &get_battle_line($gcolor, 1);
	print $fh "$new_line\n";
	close $fh;
	chmod $chmod, "$questdir/$quest_id/member.cgi";
	
	for my $k (qw/log bet win guild/) {
		open my $fh2, "> $questdir/$quest_id/$k.cgi" or &error("$questdir/$quest_id/$k.cgi�t�@�C�����쐬�ł��܂���");
		close $fh2;
		chmod $chmod, "$questdir/$quest_id/$k.cgi";
	}
	&add_bet($quest_id, 2);
	
	open my $fh3, "> $questdir/$quest_id/guild.cgi" or &error("$questdir/$quest_id/guild.cgi�t�@�C�����쐬�ł��܂���");
	print $fh3 "$gcolor<>$m{guild}<>\n";
	close $fh3;
	chmod $chmod, "$questdir/$quest_id/guild.cgi";
	
	$m{lib}   = 'vs_guild';
	$m{quest} = $quest_id;
	
	$com = "<b>���M���h��>$in{p_name}���ΐ�ꏊ>$stages[$in{stage}]���Q���l��>$in{p_join}�l��$speeds{$in{speed}}[0]";
 	if ($in{p_pass}) {
		$com .= "���������Ƃ�>�K�v";
	}
	else {
		$in{p_pass} = '�Ȃ�' ;
	}
	$com .= "</b>";
	&reload("�M���h��u$in{p_name}�v�����܂����I<br />�ΐ�ꏊ�F$stages[$in{stage}]�C$speeds{$in{speed}}[0]�C�����t�F$in{p_pass}�C�Q���l���F$in{p_join}�l");
	&leave_member($m);
}
#=================================================
# ������
#=================================================
sub sanka {
	my $target = shift;

	$mes = qq|<span onclick="text_set('���ف[�� ')">$e2j{hp}���񕜂��Ă��������B�u���ف[�ށv�ŉƂɋA��u���˂�v�ŋx��ł�������</span>|	if $m{hp} <= 0;
	$mes = qq|<span onclick="text_set('���ف[�� ')">$e2j{tired}�����܂��Ă��܂��B�u���ف[�ށv�ŉƂɋA��u���˂�v�ŋx��ł�������</span>|	if $m{tired} >= 100;
	return if $mes;

	unless ($target) {
		$mes = "�ǂ̃N�G�X�g�ɎQ�����܂����H";
		return;
	}
	
	my($p_name, $join_pass) = split /���������Ƃ�&gt;/, $target;
	my $quest_id = unpack 'H*', $p_name;
	$com =~ s/(.+)���������Ƃ�&gt;(.+)/$1/; # �����������������Ƃ΁`���폜

	if ($p_name && -d "$questdir/$quest_id") {
		&add_member($quest_id,$join_pass);
	}
	else {
		$mes = "�Q�����悤�Ƃ����N�G�X�g�́A���U���Ă��܂����悤�ł�";
	}
}

#=================================================
# �����񂩏���
#=================================================
sub add_member {
	my($quest_id,$join_pass) = @_;
	
	my @lines = ();
	open my $fh, "+< $questdir/$quest_id/member.cgi" or &error("$questdir/$quest_id/member.cgi�t�@�C�����쐬�ł��܂���");
	eval { flock $fh, 2; };
	my $head_line = <$fh>;
	my($speed,$stage,$round,$leader,$p_name,$p_pass,$p_join,$win,$bet,$is_visit,$need_join,$type,$map,$py,$px,$event) = split /<>/, $head_line;
	$mes = "$p_name�ɎQ�����邽�߂̓q����������܂���"	if $bet > $m{money};
	$mes = "$p_name�ɎQ�����邽�߂̍����t���Ⴂ�܂�"	if $p_pass ne '' && $p_pass ne $join_pass;
	$mes = "�N�G�X�g�r������Q�����邱�Ƃ͂ł��܂���"	if $round > 1 || ($round > 0 && $type ne '6'); # �����ȊO
	return if $mes;
	
	if ($need_join) {
		my($need_key, $need_value, $need_uo) = split /_/, $need_join;
		$mes = "�Q�������w�g�o��$need_value�����x�𖞂����Ă��܂���"		if $need_key eq 'hp'    && $need_uo eq 'u' && $m{mhp}    >= $need_value;
		$mes = "�Q�������w�g�o��$need_value�ȏ�x�𖞂����Ă��܂���"		if $need_key eq 'hp'    && $need_uo eq 'o' && $m{mhp}    <  $need_value;
		$mes = "�Q�������w�]�E�񐔂�$need_value�񖢖��x�𖞂����Ă��܂���"	if $need_key eq 'joblv' && $need_uo eq 'u' && $m{job_lv} >= $need_value;
		$mes = "�Q�������w�]�E�񐔂�$need_value��ȏ�x�𖞂����Ă��܂���"	if $need_key eq 'joblv' && $need_uo eq 'o' && $m{job_lv} <  $need_value;
		return if $mes;
	}

	my $color = '';
	if ($type eq '5') { # �M���h��
		$color = &_check_guild_battle($quest_id);
		return if $mes || !$color;
	}
	elsif ($type eq '3' && $m{lv} < 99 && $m{exp} >= $m{lv} * $m{lv} * 10) { # �`�������W
		$mes = "���x���A�b�v���X�g�b�N������ԂŎQ�����邱�Ƃ͂ł��܂���";
		return;
	}
	
	push @lines, $head_line;

	my $count = $type eq '6' ? 1 : 0; # �����H
	my %same_colors = ();
	while (my $line = <$fh>) {
		my($name,$laddr,$gcolor) = (split /<>/, $line)[0..2];
		if ($name eq $m) {
			$mes = "�������O�̃v���C���[�����łɎQ�����Ă��܂�";
			return;
		}
		elsif ($addr eq $laddr) {
			$mes = "�h�o�A�h���X�������v���C���[�����łɎQ�����Ă��܂��B";
#			$mes .= "<br />���d�o�^�e�^�ŒǕ��R�m�c�ɒǉ��\\������܂����B";
#			&write_news(qq|<span class="damage">$name��$m�����d�o�^�̋^���ŒǕ��\\������܂���</span>|);
#			$m{wt} = $time;
#			&add_exile($m,    "�y���d�o�^�e�^�z$name�Ɠ���IP�A�h���X");
#			&add_exile($name, "�y���d�o�^�e�^�z$m�Ɠ���IP�A�h���X");
			return;
		}
		++$same_colors{$gcolor};
		++$count unless $name =~ /^@/;
		push @lines, $line;
	}
	if ($count >= $p_join) {
		$mes = "$p_name�͒���������ς��ŎQ�����邱�Ƃ��ł��܂���";
		return;
	}
	elsif ($type eq '5' && $same_colors{ $color } >= 4) { # �M���h��
		$mes = "�����M���h�����o�[�T�l�ȏ�͎Q�����邱�Ƃ��ł��܂���";
		return;
	}
	
	# �Q������OK
	($color) ||= (split /<>/, $lines[1])[2];
	my $new_line = &get_battle_line($color,$type);
	push @lines, "$new_line\n";
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	if    ($type eq '1') {
		$m{lib} = 'vs_monster';
		&reload("$p_name�̃p�[�e�B�[�ɎQ�����܂�");
	}
	elsif ($type eq '2') {
		$m{lib} = 'vs_dungeon';
		&reload("$p_name�̃p�[�e�B�[�ɎQ�����܂�");
	}
	elsif ($type eq '3') {
		$m{lib} = 'vs_challenge';
		&reload("$p_name�ɎQ�����܂�");
	}
	elsif ($type eq '4') { # ���Z��
		&add_bet($quest_id, $bet);
		$m{money} -= $bet;
		$m{lib}    = 'vs_player';
		$com      .="�q���� $bet G���x�����܂���";
		&reload("�q���� $bet G���x���� $p_name�̓��Z��ɎQ�����܂�");
	}
	elsif ($type eq '5') { # �M���h��
		&add_bet($quest_id, 1);
		$m{lib}    = 'vs_guild';
		&reload("$p_name�̃M���h��ɎQ�����܂�");
	}
	elsif ($type eq '6') { # �����
		$m{lib} = 'vs_king';
		$m{tired} += 20;
		&reload("$p_name�̕����ɎQ�����܂�");
	}
	$m{quest} = $quest_id;
	&leave_member($m);
}
# �M���h��Q�������`�F�b�N
sub _check_guild_battle {
	my $quest_id = shift;
	
	if ($m{guild}) {
		my($gid,$gname,$gmaster,$gcolor,$gbgimg,$gmes,$gpoint) = &read_guild_data;
		if ($gcolor eq $default_color) {
			$mes = "���ǂ��M���h�̓M���h������邱�Ƃ͂ł��܂���";
		}
		else {
			open my $fh, ">> $questdir/$quest_id/guild.cgi" or &error("$questdir/$quest_id/guild.cgi�t�@�C�����J���܂���");
			print $fh "$gcolor<>$m{guild}<>\n";
			close $fh;
			return $gcolor;
		}
	}
	else {
		$mes = "�M���h�ɎQ�����Ă��܂���";
	}
	
	return;
}

#=================================================
# �����񂪂�
#=================================================
sub kengaku {
	my $target = shift;

	unless ($target) {
		$mes = "�ǂ̃N�G�X�g�����w���܂����H";
		return;
	}
	
	my($p_name, $join_pass) = split /���������Ƃ�&gt;/, $target;
	my $quest_id = unpack 'H*', $p_name;
	$com =~ s/(.+)���������Ƃ�&gt;(.+)/$1/; # �����������������Ƃ΁`���폜

	if ($p_name && -d "$questdir/$quest_id") {
		open my $fh, "< $questdir/$quest_id/member.cgi" or &error("$questdir/$quest_id/member.cgi�t�@�C�����ǂݍ��߂܂���");
		my $head_line = <$fh>;
		close $fh;

		my($speed,$stage,$round,$leader,$p_name,$p_pass,$p_join,$win,$bet,$is_visit,$need_join,$type,$map,$py,$px,$event) = split /<>/, $head_line;
		if (!$is_visit) {
			$mes = "$p_name�̌��w�͂ł��܂���";
			return;
		}
		elsif ($p_pass ne '' && $p_pass ne $join_pass) {
			$mes = "$p_name�����w���邽�߂̍����t���Ⴂ�܂�";
			return;
		}
		
		$m{lib} = $type eq '1' ? 'vs_monster'
				: $type eq '2' ? 'vs_dungeon'
				: $type eq '3' ? 'vs_challenge'
				: $type eq '4' ? 'vs_player'
				: $type eq '5' ? 'vs_guild'
				: $type eq '6' ? 'vs_king'
				: '';
		$m{quest} = $quest_id;
		$mes = "$p_name�����w���܂�";
		&reload("$p_name�����w���܂�");
		&leave_member($m);
	}
	else {
		$mes = "���w���悤�Ƃ����N�G�X�g�́A���U���Ă��܂����悤�ł�";
	}
}


#=================================================
# �o�g���p�f�[�^�쐬 @battle_datas�̒l���Z�b�g
#=================================================
sub get_battle_line {
	my($color,$type) = @_;
	my %p = %m;
	
	$m{is_get} = 0;  # ��擾�t���O�����Z�b�g
	$m{event}  = ''; # �C�x���g�t���O�����Z�b�g
	$p{color} = $type eq '4' || !defined($color) || $color eq $npc_color ? $default_color : $color; # ���Z�ꂩ�J���[����`���G�F��
	
	# %m�ɂ͂Ȃ�Key
	$p{get_exp}   = $m{lv} + $m{job_lv};
	$p{get_money} = int($m{lv} * 0.5);
	$p{ten} = 1;
	$p{hit} = 95;
	
	$p{mat} = $m{at};
	$p{mdf} = $m{df};
	$p{mag} = $m{ag};
	$p{at}  = $m{at} + $weas[$m{wea}][3];
	$p{df}  = $m{df} + $arms[$m{arm}][3];
	$p{ag}  = $m{ag} - $weas[$m{wea}][4] - $arms[$m{arm}][4];
	%p = &{ $ites[$p{ite}][4] }(%p) if $ites[$p{ite}][3] eq '4'; # �����i(�퓬�J�n���A���S���A���Ă��͂ǂ��Ȃ� &reset_status�̎�)

	my $line = '';
	for my $k (@battle_datas) {
		$line .= "$p{$k}<>";
	}
	return $line;
}


1; # �폜�s��
