#!/usr/local/bin/perl
require './config.cgi';
require './lib/_data.cgi';
#================================================
# �u���O�p�[�c�Q Created by Merino
#================================================
print "Content-type: text/html; charset=Shift_JIS\n\n";
&run;
exit;

#================================================
sub run {
	my $yid = $ENV{'QUERY_STRING'};
	$yid =~ s/\W//g;
	
	if (-f "$userdir/$yid/user.cgi") {
		my %m = &get_you_datas($yid, 1);
		my $latest = $time < $m{login_time} + $login_time * 60 ? qq|<b style="color:#FF0;">���O�C����</b>| : qq|�ŏI�X�V��: $m{ldate}|;
		my $mes    = $m{mes} ? $m{mes} : $title;

		# ���͂Ȃ�
		my $hanasu;
		open my $fh2, "< $userdir/$yid/hanasu.cgi" or &error("$userdir/$yid/hanasu.cgi�t�@�C�����ǂݍ��߂܂���");
		rand($.) < 1 and $hanasu = $_ while <$fh2>;
		close $fh2;

		my $html;
		$html .= qq|<table style="width: 120px; background: #000; font-size: 11px; color: #FFF;"><tr><td style="border:1px solid #FFF; background-color:#336;">�y$m{name}�̉Ɓz</td></tr>|;
		$html .= qq|<tr><td><div style="background: url($game_path/$userdir/$yid/bgimg.gif) #333 repeat-x left bottom;"><table><tr>|;
		my $count = 0;
		open my $fh, "< $userdir/$yid/home_member.cgi" or &error("$userdir/$yid/home_member.cgi�t�@�C�����J���܂���"); 
		while (my $line = <$fh>) {
			my($ltime, $is_npc, $name, $laddr, $icon, $color) = split /<>/, $line;
			$html .= qq|<td align="center" valign="bottom"><span style="color: $color; font-size: 11px; background-color: #333;">$name</span><br /><img src="$game_path/$icondir/$icon" alt="$name" /></td>|;
			last if ++$count >= 3;
		}
		close $fh;
		$html .= qq|</tr></table></div><hr size="1" />|;
		$html .= qq|$hanasu<hr size="1" />| if $hanasu;
		$html .= qq|$latest<br /><a href="$game_path/index.cgi?$yid" style="color: #6CF;">$mes</a><hr size="1" /></td></tr></table>|;
		
		$html =~ tr/\x0D\x0A//d; # ���s�폜
		print qq|document.write('$html');|;
	}
	else {
		print qq|document.write("�v���C���[�f�[�^��������܂���");|;
	}
}
