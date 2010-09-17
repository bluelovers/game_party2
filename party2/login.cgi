#!/usr/local/bin/perl
require 'config.cgi';
#================================================
# �v���C���[�ꗗHTML�쐬 + �����؂�v���C���[�폜
# & Cookie�Z�b�g Created by Merino
#================================================
# �v���C���[�ꗗHTML�X�V����(��) 1���`
my $update_cycle_day = 1;

# Cookie�ۑ�����(��)
my $limit_cookie_day = 30;

# ���b�Z�[�W�̍ő啶����(���p)
my $max_login_message = 60;

$htmldir = './html';


#================================================
&decode;
&error("���b�Z�[�W�ɕs���ȕ���( ,;\"\'&<> )���܂܂�Ă��܂�",1)	if $in{login_message} =~ /[,;\"\'&<>]/;
&error("���b�Z�[�W�ɕs���ȋ󔒂��܂܂�Ă��܂�",1)					if $in{login_message} =~ /�@|\s/;
&error("���b�Z�[�W���������܂�(���p$max_login_message�����܂�)",1)	if length $in{login_message} > $max_login_message; # �ő啶��������
$in{is_cookie} ? &set_cookie($in{login_name},$in{pass},$in{login_message}) : &del_cookie;
# �X�V�A�ł��Ă����ꍇ�̃y�i���e�B
&read_user(1);
if (-s "$userdir/$id/reload.cgi") {
	open my $fh, "+< $userdir/$id/reload.cgi" or &error("$userdir/$id/reload.cgi�t�@�C�����J���܂���", 1);
	my $line = <$fh>;
	my @lines = split /<>/, $line;
	seek  $fh, 0, 0;
	truncate $fh, 0;
	close $fh;
	
	if    (@lines > 30) {
#		&add_black_list($addr);
#		&delete_guild_member($m{guild}, $m{name}) if $m{guild};
#		&delete_directory("$userdir/$id");
#		&error(qq|<span class="die">�O��̃v���C���ɍX�V�A�ł�30��𒴂��Ă����̂ŁA�폜�ƂȂ�܂�</span>|, 1);
		$sleep_time = 7 * 24 * 60;
		$m{sleep} = $m{sleep} > 0 ? $m{sleep} + $sleep_time * 60 : $sleep_time * 60;
		&write_user;
		&error(qq|<span class="die">�O��̃v���C���ɍX�V�A�ł�30��𒴂��Ă����̂ŁA$sleep_time���Ԑ�����ԂƂȂ�܂�</span>|, 1);
	}
	elsif (@lines > 25) {
#		&add_black_list($addr);
#		&error(qq|<span class="die">�O��̃v���C���ɍX�V�A�ł�25��𒴂��Ă����̂ŁA�u���b�N���X�g�ǉ��ƂȂ�$sleep_time���Ԑ�����ԂƂȂ�܂�</span>|, 1);
		$sleep_time = 3 * 24 * 60;
		$m{sleep} = $m{sleep} > 0 ? $m{sleep} + $sleep_time * 60 : $sleep_time * 60;
		&write_user;
		&error(qq|<span class="die">�O��̃v���C���ɍX�V�A�ł�25��𒴂��Ă����̂ŁA$sleep_time���Ԑ�����ԂƂȂ�܂�</span>|, 1);
	}
	elsif (@lines > 20) {
		$sleep_time = 24 * 60;
		$m{sleep} = $m{sleep} > 0 ? $m{sleep} + $sleep_time * 60 : $sleep_time * 60;
		&write_user;
		&error(qq|<span class="die">�O��̃v���C���ɍX�V�A�ł�20��𒴂��Ă����̂ŁA$sleep_time���Ԑ�����ԂƂȂ�܂�</span>|, 1);
	}
	elsif (@lines > 15) {
		$sleep_time = 6 * 60;
		$m{sleep} = $m{sleep} > 0 ? $m{sleep} + $sleep_time * 60 : $sleep_time * 60;
		&write_user;
		&error(qq|<span class="die">�O��̃v���C���ɍX�V�A�ł�15��𒴂��Ă����̂ŁA$sleep_time���Ԑ�����ԂƂȂ�܂�</span>|, 1);
	}
	elsif (@lines > 10) {
		$sleep_time = 60;
		$m{sleep} = $m{sleep} > 0 ? $m{sleep} + $sleep_time * 60 : $sleep_time * 60;
		&write_user;
		&error(qq|<span class="die">�O��̃v���C���ɍX�V�A�ł�10��𒴂��Ă����̂ŁA$sleep_time���Ԑ�����ԂƂȂ�܂�</span>|, 1);
	}
}

require 'party.cgi';
$m{mes} = $in{login_message};
&write_user;
&write_top_message;

if    (-M "$htmldir/player_list.html" >= $update_cycle_day) {
	&write_player_list_html;
}
elsif (-M "$logdir/guild_list.cgi"  >= $update_cycle_day) {
	&write_guild_list_html;
}
exit;

# ------------------

sub write_top_message {
	my @lines = ();
	open my $fh, "+< $logdir/login.cgi" or &error("$logdir/login.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	push @lines, $_ while <$fh>;
	unshift @lines, "$time<>$m{name}<>$m{color}<>$m{guild}<>$m{mes}<>$m{icon}<>\n";
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}


#=================================================
# �N�b�L�[�Z�b�g
#=================================================
sub set_cookie {
	my @cooks = @_;

	local($csec,$cmin,$chour,$cmday,$cmon,$cyear,$cwday) = gmtime(time + $limit_cookie_day * 24 * 60 * 60); # 60�� 24���� * 60�� * 60�b
	local @mons = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec');
	local @week = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat');

	local $expirese_time = sprintf("%s, %02d-%s-%04d %02d:%02d:%02d GMT",
			$week[$cwday],$cmday,$mons[$cmon],$cyear+1900,$chour,$cmin,$csec);

	for my $c (@cooks) {
		$c =~ s/(\W)/sprintf("%%%02X", unpack "C", $1)/eg;
		$cook .= "$c<>";
	}

	print "Set-Cookie: party=$cook; expires=$expirese_time\n";
}
# ------------------
# �N�b�L�[�폜
sub del_cookie {
	my $expires_time = 'Thu, 01-Jan-1970 00:00:00 GMT';
	print "Set-Cookie: party=dummy; expires=$expires_time\n";
}

#=================================================
# �v���C���[�ꗗ�쐬
#=================================================
sub write_player_list_html {
	my $count = 0;
	my $html = qq|<table class="tablesorter"><thead><tr>|;
	for my $k (qw/���O ���� �M���h Lv �]�E �E�� �O�E�� �g�o �l�o �U�� ��� �f�� �ް��� ��� ���� ���� �h�� ���� �ݽ������ ��ڲ԰���� ���� ��� ���� �ŏI���O�C��/) {
		$html .= qq|<th>$k</th>|;
	}
	$html .= qq|</tr></thead><tbody>\n|;
	
	my @datas = ();
	opendir my $dh, $userdir or &error("$userdir�f�B���N�g�����J���܂���");
	while (my $dir_name = readdir $dh) {
		next if $dir_name =~ /\./;
		my %p = &get_you_datas($dir_name, 1);
		
		# �����폜����
		if ( ($time > $p{ltime} + $auto_delete_day * 3600 * 24)
			|| ($p{job_lv} <= 0 && $p{lv} <= 2 && $time > $p{ltime} + 7 * 3600 * 24) ) { # �]�E�񐔂O�Ń��x��2�ȉ��͂V���ō폜
				&delete_guild_member($p{guild}, $p{name}) if $p{guild};
				&delete_directory("$userdir/$dir_name");
				next;
		}
		++$count;
		push @datas, [$p{name},$p{guild},$p{color},$p{icon},$p{mes},$p{kill_p},$p{kill_m},$p{cas_c},$p{mao_c},$p{hero_c}];
		$html .= qq|<tr><td style="color: $p{color};"><img src="../$icondir/$p{icon}" /><a href="../player.cgi?id=$dir_name">$p{name}</a></td><td>$e2j{$p{sex}}</td><td>$p{guild}</td><td align="right">$p{lv}</td><td align="right">$p{job_lv}</td><td>$jobs[$p{job}][1]($p{sp})</td><td>$jobs[$p{old_job}][1]($p{old_sp})</td><td align="right">$p{mhp}</td><td align="right">$p{mmp}</td><td align="right">$p{at}</td><td align="right">$p{df}</td><td align="right">$p{ag}</td><td align="right">$p{money}</td><td align="right">$p{coin}</td><td align="right">$p{medal}</td><td>$weas[$p{wea}][1]</td><td>$arms[$p{arm}][1]</td><td>$ites[$p{ite}][1]</td><td align="right">$p{kill_m}</td><td align="right">$p{kill_p}</td><td align="right">$p{hero_c}</td><td align="right">$p{mao_c}</td><td align="right">$p{cas_c}</td><td>$p{ldate}</td></tr>\n|; 
	}
	closedir $dh;
	
	$html .= qq|\n</tbody></table>\n|;
	
	open my $fh, "> $htmldir/player_list.html" or &error("$htmldir/player_list.html�t�@�C�����J���܂���");
	print $fh &html_player_header;
	print $fh $html;
	print $fh &html_player_footer;
	close $fh;

	# �o�^�l���␳
	open my $fh2, "> $logdir/entry.cgi" or &error("$logdir/entry.cgi�t�@�C�����ǂݍ��߂܂���");
	print $fh2 "$count<><>";
	close $fh2;
	
	&write_ranking(@datas);
}
#=================================================
# ���ҁE�p�Y�̃f�[�^�쐬
#=================================================
sub write_ranking {
	my @datas = @_;
	my @kills_ps = sort { $b->[5] <=> $a->[5] } @datas;
	my @kills_ms = sort { $b->[6] <=> $a->[6] } @datas;
	my @cas_cs   = sort { $b->[7] <=> $a->[7] } @datas;
	my @mao_cs   = sort { $b->[8] <=> $a->[8] } @datas;
	my @hero_cs  = sort { $b->[9] <=> $a->[9] } @datas;
	
	# ���҃��X�g
	my %sames = ();
	my $count = 0;
	my $line  = '';
	for my $ref (@kills_ps) {
		++$sames{ $ref->[0] };
		$line .= "$ref->[0]<>$ref->[1]<>$ref->[2]<>$ref->[3]<>$ref->[4]<>$ref->[5]<>\n";
		last if ++$count >= 10;
	}
	open my $fh, "> $logdir/kill_p.cgi" or &error("$logdir/kill_p.cgi�t�@�C�����J���܂���");
	print $fh $line;
	close $fh;
	
	# �p�Y���X�g
	$count = 0;
	$line  = '';
	for my $ref (@kills_ms) {
		next if $sames{ $ref->[0] }; # ���҃����L���O�҂͔r��
		$line .= "$ref->[0]<>$ref->[1]<>$ref->[2]<>$ref->[3]<>$ref->[4]<>$ref->[6]<>\n";
		last if ++$count >= 10;
	}
	open my $fh2, "> $logdir/kill_m.cgi" or &error("$logdir/kill_m.cgi�t�@�C�����J���܂���");
	print $fh2 $line;
	close $fh2;

	# �������X�g
	%sames = ();
	$count = 0;
	$line  = '';
	for my $ref (@mao_cs) {
		++$sames{ $ref->[0] };
		$line .= "$ref->[0]<>$ref->[1]<>$ref->[2]<>$ref->[3]<>$ref->[4]<>$ref->[8]<>\n";
		last if ++$count >= 10;
	}
	open my $fh3, "> $logdir/mao_c.cgi" or &error("$logdir/mao_c.cgi�t�@�C�����J���܂���");
	print $fh3 $line;
	close $fh3;

	# �E�҃��X�g
	$count = 0;
	$line  = '';
	for my $ref (@hero_cs) {
		next if $sames{ $ref->[0] }; # ���������L���O�҂͔r��
		$line .= "$ref->[0]<>$ref->[1]<>$ref->[2]<>$ref->[3]<>$ref->[4]<>$ref->[9]<>\n";
		last if ++$count >= 10;
	}
	open my $fh4, "> $logdir/hero_c.cgi" or &error("$logdir/hero_c.cgi�t�@�C�����J���܂���");
	print $fh4 $line;
	close $fh4;

	# �J�W�m���҃��X�g
	$count = 0;
	$line  = '';
	for my $ref (@cas_cs) {
		$line .= "$ref->[0]<>$ref->[1]<>$ref->[2]<>$ref->[3]<>$ref->[4]<>$ref->[7]<>\n";
		last if ++$count >= 10;
	}
	open my $fh5, "> $logdir/cas_c.cgi" or &error("$logdir/cas_c.cgi�t�@�C�����J���܂���");
	print $fh5 $line;
	close $fh5;
}


# ------------------
# �v���C���[�ꗗ�̃w�b�_�[
sub html_player_header {
	return <<"EOM";
<html>
<head>
<title>$title / �v���C���[�ꗗ</title>
<link rel="stylesheet" type="text/css" href="party.css">
<link rel="stylesheet" type="text/css" href="./jQuery/themes/green/style.css">
<script type="text/javascript" src="./jQuery/jquery-latest.js"></script>
<script type="text/javascript" src="./jQuery/jquery.tablesorter.js"></script>
<script type="text/javascript" src="./jQuery/jquery.tablesorter.pager.js"></script>
<script type="text/javascript">
<!--
\$(document).ready(function() {
	\$(".tablesorter")
		.tablesorter({
			widgets: ['zebra'],
			sortList: [[4,1],[3,1]]
		})
		.tablesorterPager({
			size: 50,
			positionFixed: false,
			container: \$("#pager")
		});
});
-->
</script>
</head>
<body>
<form action="../index.cgi"><input type="submit" value="�s�n�o�֖߂�" /></form>
<p>�X�V���� $date</p>
<div id="pager" class="pager">
	<form>
		<img src="./jQuery/addons/pager/icons/first.png" class="first" />
		<img src="./jQuery/addons/pager/icons/prev.png" class="prev" />
		<input type="text" class="pagedisplay" />
		<img src="./jQuery/addons/pager/icons/next.png" class="next" />
		<img src="./jQuery/addons/pager/icons/last.png" class="last" />
		<select class="pagesize">
			<option value="30">30</option>
			<option value="50" selected="selected">50</option>
			<option value="100">100</option>
		</select>
	</form>
</div>
EOM
}

# ------------------
# �v���C���[�ꗗ�̃t�b�^�[
sub html_player_footer {
	return <<"EOM";
<br />
<div align="right" style="font-size:11px">
���p�[�e�B�[II Ver$VERSION<br /><a href="http://cgi-sweets.com/" target="_blank">CGI-Sweets</a><br /><a href="http://amaraku.net/" target="_blank">Ama�y.net</a><br />
$copyright
</div>
</body>
</html>
EOM
}


#=================================================
# �M���h���͍쐬
#=================================================
sub write_guild_list_html {
	my @guild_list = ();
	opendir my $dh, $guilddir or &error("$guilddir�f�B���N�g�����J���܂���");
	while (my $dir_name = readdir $dh) {
		next if $dir_name =~ /\./;
		
		open my $fh, "+< $guilddir/$dir_name/data.cgi" or &error("$guilddir/$dir_name/data.cgi");
		eval { flock $fh, 2; };
		my $line = <$fh>;
		my($gname,$gmaster,$gcolor,$gbgimg,$gmes,$gpoint) = split /<>/, $line;
		$gpoint = int($gpoint * 0.8); # �M���h�|�C���g���P����
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh "$gname<>$gmaster<>$gcolor<>$gbgimg<>$gmes<>$gpoint<>";
		close $fh;
		
		my $gmembers = '';
		my $gcount = 0;
		open my $fh2, "< $guilddir/$dir_name/member.cgi" or &error("$guilddir/$dir_name/member.cgi�t�@�C�����ǂݍ��߂܂���");
		while (my $line2 = <$fh2>) {
			my($name, $position) = split /<>/, $line2;
			next if $position eq '�Q���\����';
			$gmembers .= "$name��$position<>";
			++$gcount;
		}
		close $fh2;
		
		push @guild_list, "$gname<>$gcount<>$gcolor<>$gmes<>$gpoint<>$gmembers\n";
	}
	closedir $dh;
	
	# �M���h�|�C���g�A�l�����������Ƀ\�[�g
	@guild_list = map { $_->[0] } sort { $b->[5] <=> $a->[5] || $b->[2] <=> $a->[2] } map { [$_, split /<>/] } @guild_list;
	
	open my $fh3, "> $logdir/guild_list.cgi";
	print $fh3 @guild_list;
	close $fh3;
}


