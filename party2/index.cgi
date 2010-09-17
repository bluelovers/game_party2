#!/usr/local/bin/perl
require 'config.cgi';
require '_side_menu.cgi';
require './lib/_data.cgi';
#================================================
# Index Created by Merino
#================================================
&header;
&run;
&footer;
exit;
#=================================================
sub run {
	my($cookie_name, $cookie_pass, $cookie_mes) = &get_cookie;
	my $checked = $cookie_name ? 'checked="checked"' : '';
	my $entry_count = &get_entry_count;
	my($login_list, $login_count) = &get_login_member;

	my $contents = <<"EOM";
		<table><tr><td valign="top">
			<div class="login_list">$login_list</div>
			<div>���O�C���� $login_count �l</div>
			��ڲ԰�ۑ����� $auto_delete_day���i�]�E0�� $e2j{lv}2�ȉ��̏ꍇ��7���j<br />
			��� $entry_count / $max_entry�l
		</td><td valign="top">
EOM
	if ($login_count >= $max_login) {
		$contents .= qq|<table class="table1"><tr><th><p>�������܁A���O�C���K�����ł�</p><p>���O�C���l����$max_login�l�����ɂȂ�܂�<br />���΂炭���҂���������</p></th></tr></table>|;
	}
	else {
		$contents .= <<"EOM";
		<form method="$method" action="login.cgi">
			<table class="table1" style="margin: 0 0.5em; padding: 1em">
				<tr><th>���v���C���[��</th></tr><tr><td align="center"><input type="text" name="login_name" class="text_box1" value="$cookie_name" /></td></tr>
				<tr><th>���p�X���[�h��</th></tr><tr><td align="center"><input type="password" name="pass"   class="text_box1" value="$cookie_pass" /></td></tr>
				<tr><th>�����b�Z�[�W��</th></tr><tr><td align="center"><input type="text" name="login_message" class="text_box1" value="$cookie_mes" /></td></tr>
				<tr><th><input type="checkbox" name="is_cookie" $checked /> ���񂩂���͏ȗ�</th></tr>
				<tr><th><input type="submit" value="�����O�C��" /></th></tr>
			</table>
		</form>
EOM
	}
	$contents .= qq|</td></tr></table>|;
	
	open my $fh, "< $logdir/screen_shot.cgi" or &error("$logdir/screen_shot.cgi�t�@�C�����ǂݍ��߂܂���");
	my $line = <$fh>;
	close $fh;

	$contents .= <<"EOM";
<br>
<a href="screen_shot.cgi">�ŋ߂̃X�N���[���V���b�g</a><br /><div>$line</div>
EOM
	
	&side_menu($contents);
}


#=========================================================
# �N�b�L�[�擾
#=========================================================
sub get_cookie {
	my %cooks;
	my @cooks;

	for my $pair (split /;/, $ENV{HTTP_COOKIE}) {
		my($k, $v) = split /=/, $pair;
		$k =~ s/\s//g;
		$cook{$k} = $v;
	}
	for my $c (split /<>/, $cook{party}) {
		$c =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack 'H2', $1/eg;
		push @cooks, $c;
	}
	return @cooks;
}

