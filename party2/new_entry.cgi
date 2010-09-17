#!/usr/local/bin/perl
require 'config.cgi';
require '_side_menu.cgi';
require './lib/_data.cgi';
#================================================
# �V�K�o�^ Created by Merino
#================================================
# �����őI�ׂ�E��(No)
my @default_jobs = (1..12);


#================================================
&decode;
&access_check;
&header;
&error("���݃����e�i���X���ł��B���΂炭���҂���������(�� $mente_min ����)") if $mente_min;
$in{mode} eq 'new_entry' ? &new_entry : &new_form;
&footer;
exit;

#================================================
# �V�K�o�^�t�H�[��
#================================================
sub new_form {
	my $job_html = qq|<select class="select1" name="job">|;
	for my $i (@default_jobs) {
		$job_html .= qq|<option value="$i">$jobs[$i][1]</option>|;
	}
	$job_html .= qq|</select>|;
	
	my $yid = $ENV{'QUERY_STRING'};
	my $contents = <<"EOM";
<h2>�V�K�o�^</h2>

<form method="$method" action="new_entry.cgi">
	<input type="hidden" name="mode" value="new_entry" />
	<input type="hidden" name="yid" value="$yid" />
	<ul>
		<li>�L��(,;"'&<>\\/@)��󔒂͎g���܂���B</li>
		<li>�l�b�g�}�i�[������Ċy�����V�т܂��傤�B</li>
		<li><b>���l���s�����ɂȂ�悤�ȏ������݂⑽�d�o�^�͋֎~�ł��B��������폜���܂��B</b></li>
	</ul>
	<table class="table1">
		<tr><td>�v���C���[���F</td><td><input type="text" name="name" class="text_box1" /></td></th></tr>
		<tr><td>�@</td><td>�S�p�S(���p�W)�����܂�</td></tr>
		<tr><td>�p�X���[�h�F</td><td><input type="text" name="pass" class="text_box1" /></td></th></tr>
		<tr><td>�@</td><td>���p�p�����S�`12�����܂�</td></tr>
		<tr><td>�E�ƁF</td><td>$job_html</td></th></tr>
		<tr><td>�@</td><td>�E�Ƃ͏d�v�ł��B�������̓������悭�ǂ݁A�����ɍ������E�Ƃ�I�т܂��傤</td></tr>
		<tr><td>$e2j{sex}�F</td><td><input type="radio" name="sex" value="m" checked="checked" />�j�@<input type="radio" name="sex" value="f" />��</td></tr>
		<tr><td>�@</td><td>���ʂɂ���ē]�E�ł���E�Ƃ�A�C�R�����Ⴂ�܂�</td></tr>
	</table>
	<p><input type="submit" value="���o�^" /></p>
</form>
<br />
EOM

	&side_menu($contents);
}
#================================================
# �V�K�o�^�`�F�b�N����������
#================================================
sub new_entry {
	&check_black_list;
	&check_entry;
	&check_registered;
	&create_user;

	$contents = <<"EOM";
<p>�ȉ��̓��e�œo�^���܂���</p>

<p class="strong">���v���C���[���ƃp�X���[�h�̓��O�C������Ƃ��ɕK�v�Ȃ̂ŁA�Y��Ȃ��悤��!<p>
<table class="table1">
	<tr><th>�v���C���[</th><td>$m{name}</td>
	<tr><th>�p�X���[�h</th><td>$m{pass}</td>
	<tr><th>$e2j{sex}</th><td>$e2j{$m{sex}}</td>
	<tr><th>�E��</th><td>$jobs[$m{job}][1]</td>
	<tr><th>$e2j{hp}</th><td align="right">$m{hp}</td>
	<tr><th>$e2j{mp}</th><td align="right">$m{mp}</td>
	<tr><th>$e2j{at}</th><td align="right">$m{at}</td>
	<tr><th>$e2j{df}</th><td align="right">$m{df}</td>
	<tr><th>$e2j{ag}</th><td align="right">$m{ag}</td>
</table>
<div>
�������͓ǂ݂܂������H<br />
�킩��Ȃ����Ƃ�����ꍇ�́A�܂���������ǂ݂܂��傤�B
</div>
<form method="$method" action="login.cgi">
	<input type="hidden" name="is_cookie" value="1" />
	<input type="hidden" name="login_name" value="$in{name}" />
	<input type="hidden" name="pass" value="$in{pass}" />
	<input type="submit" value="���v���C" />
</form>
EOM
&side_menu($contents);
}

#================================================
# �o�^�`�F�b�N
#================================================
sub check_entry {
	&error("�s���ȓo�^�����ł�")				if $ENV{QUERY_STRING};
	&error("�v���C���[�������͂���Ă��܂���")	unless $in{name};
	&error("�p�X���[�h�����͂���Ă��܂���")	if $in{pass} eq '';
	&error("$e2j{sex}�����͂���Ă��܂���")		if $in{sex} eq '';

	&error("�v���C���[���ɕs���ȕ���( ,;\"\'&<>\@ )���܂܂�Ă��܂�")	if $in{name} =~ /[,;\"\'&<>\@]/;
	&error("�v���C���[���ɕs���ȕ���( �� )���܂܂�Ă��܂�")			if $in{name} =~ /��/;
	&error("�v���C���[���ɕs���ȋ󔒂��܂܂�Ă��܂�")					if $in{name} =~ /�@|\s/;
	&error("�v���C���[���͑S�p�S(���p�W)�����ȓ��ł�")					if length($in{name}) > 8;
	&error("�p�X���[�h�͔��p�p�����œ��͂��ĉ�����")					if $in{pass} =~ m/[^0-9a-zA-Z]/;
	&error("�p�X���[�h�͔��p�p�����S�`12�����ł�")						if length $in{pass} < 4 || length $in{pass} > 12;
	&error("�v���C���[���ƃp�X���[�h�����ꕶ����ł�")					if $in{name} eq $in{pass};
	&error("$e2j{sex}���ُ�ł�")										unless $in{sex} eq 'm' || $in{sex} eq 'f';

	my $is_ng_job = 1;
	for my $i (@default_jobs) {
		if ($i eq $in{job}) {
			$is_ng_job = 0;
			last;
		}
	}
	&error("�E�Ƃ��ُ�ł�") if $is_ng_job;
	
	$id = unpack 'H*', $in{name};
	&error("���̖��O�͂��łɓo�^����Ă��܂�") if -d "$userdir/$id";
	
	open my $fh, "< $logdir/entry.cgi" or &error("$logdir/entry.cgi�t�@�C�����ǂݍ��߂܂���");
	my $line = <$fh>;
	close $fh;
	my($entry_count, $last_addr) = split /<>/, $line;
	&error("���ݒ���̂��߁A�V�K�o�^�͎󂯕t���Ă���܂���") if $entry_count >= $max_entry;
	&error("���d�o�^�͋֎~���Ă��܂�") if $addr eq $last_addr;
}
#================================================
# �o�^����
#================================================
sub create_user {
	$id = unpack 'H*', $in{name};
	
	# �t�H���_�E�t�@�C���쐬
	mkdir "$userdir/$id", $mkdir or &error("���̖��O�͂��łɓo�^����Ă��܂�");
	for my $file_name (qw/collection depot hanasu home home_member item_send_mes job_master letter letter_log memory money monster monster_book profile recipe reload screen_shot send_item_mes stock user/) {
		my $output_file = "$userdir/$id/$file_name.cgi";
		open my $fh, "> $output_file" or &error("$output_file �t�@�C�������܂���ł���");
		close $fh;
		chmod $chmod, $output_file;
	}
	open my $fh2, ">> $userdir/$id/collection.cgi" or &error("$userdir/$id/collection.cgi�t�@�C�������܂���ł���");
	print $fh2 ",\n,\n,\n";
	close $fh2;
	
	%m = ();
	$m = $m{name} = $in{name};
	$m{pass} = $in{pass};
	$m{job}  = $in{job};
	$m{sex}  = $in{sex};
	$m{money} = 200;
	$m{mhp}  = int(rand(3)) + 30;
	$m{mmp}  = int(rand(3)) + 6;
	$m{at}   = int(rand(3)) + 6;
	$m{df}   = int(rand(3)) + 6;
	$m{ag}   = int(rand(3)) + 6;
	$m{hp}   = $m{mhp};
	$m{mp}   = $m{mmp};
	$m{lv}   = 1;
	$m{icon} = "job/$m{job}_$m{sex}.gif";
	$m{color} = $default_color;
	$m{home} = $m;

	for my $k (qw/sleep job_lv exp medal coin coupon rare tired sp old_job old_sp wea arm ite is_full is_get is_eat kill_p kill_m cas_c hero_c mao_c/) {
		$m{$k} = 0;
	}
	
	&write_user;
	&write_memory("�`���� <b>$m</b> �a���I");
	&write_news("<b>$m</b> �Ƃ����`���҂��Q�����܂���");

	require './lib/_add_monster_book.cgi';
	&write_monster_book;

	&plus_entry_count;
	&copy("$htmldir/space.gif", "$userdir/$id/bgimg.gif");
	
	# �Љ�ID�t�Ȃ�Љ�҂ɏ����ȃ��_�����M
	if ($in{yid}) {
		my $send_name = pack 'H*', $in{yid};
		&send_item($send_name, 3, 23, "$m{name}(�Љ����)");
	}
}


#================================================
# �o�^�Ґ��v���X
#================================================
sub plus_entry_count {
	open my $fh, "+< $logdir/entry.cgi" or &error("$logdir/entry.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	my $line = <$fh>;
	my($entry_count, $last_addr) = split /<>/, $line;
	++$entry_count;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh "$entry_count<>$addr<>";
	close $fh;
}

#================================================
# �u���b�N���X�g�̂h�o�Ɠ������`�F�b�N
#================================================
sub check_black_list {
	open my $fh, "< $logdir/black_list.cgi" or &error("$logdir/black_list.cgi�t�@�C�����ǂݍ��߂܂���");
	my $line = <$fh>;
	close $fh;
	&error("���Ȃ��̃z�X�g����͓o�^���邱�Ƃ��֎~����Ă��܂�") if $line =~ /,$host,/;
}

#================================================
# ���d�o�^�֎~�F�S���[�U�[�̂h�o�A�h���X�𒲂ׂ�
#================================================
sub check_registered {
	opendir my $dh, "$userdir" or &error("���[�U�[�f�B���N�g�����J���܂���");
	while (my $dir_name = readdir $dh) {
		next if $dir_name =~ /\./;
		
		my %datas = &get_you_datas($dir_name, 1);
		if ($addr eq $datas{addr}) {
#			&add_black_list($addr);
			&error("���d�o�^�͋֎~���Ă��܂�");
		}
	}
	closedir $dh;
}

