#!/usr/local/bin/perl
require 'config.cgi';
require './lib/_data.cgi';
my $this_script = 'admin.cgi';
#=================================================
# �v���C���[�Ǘ� Created by Merino
#=================================================
# ���я���
my %e2j_sorts = (
	name	=> '���O��',
	ldate	=> '�X�V������',
	addr	=> 'Host/IP��',
);

# �f�t�H���g�̕��я�
$in{sort} ||= 'addr';

#=================================================
# ���C������
#=================================================
&header;
&decode;
&error("�p�X���[�h���Ⴂ�܂�") unless $in{pass} eq $admin_pass;
if ($in{mode} eq 'admin_delete_user') { &admin_delete_user; }
&top;
&footer;
exit;

#=================================================
# top
#=================================================
sub top {
	print qq|<table><tr>|;
	print qq|<td><form action="$script_index"><input type="submit" value="�s�n�o" class="button_s" /></form></td>|;
	while (my($k,$v) = each %e2j_sorts) {
		next if $in{sort} eq $k;
		print qq|<td><form method="$method" action="$this_script"><input type="hidden" name="pass" value="$in{pass}" />\n|;
		print qq|<input type="hidden" name="sort" value="$k" /><input type="submit" value="$v" class="button_s" /></form></td>\n|;
	}
	print qq|</tr></table>|;
	
	print qq|<div class="mes">$mes</div><br />| if $mes;
	
	print qq|<form method="$method" action="$this_script">|;
	print qq|<input type="hidden" name="mode" value="admin_delete_user" /><input type="hidden" name="pass" value="$in{pass}" />|;
	print qq|<input type="hidden" name="sort" value="$in{sort}" />|;
	print qq|�~�o�́A��ʂɉ����\\������Ȃ��Ȃ�����A���[�v�ɂ͂܂�����ԂȂǂ��C�����܂��B<br />|;
	print qq|<table class="table2"><tr>|;

	for my $k (qw/�폜 ���O�C�� ���O �t�H���_ ���Z�b�g IP�A�h���X �z�X�g�� �X�V����/) {
		print qq|<th>$k</th>|;
	}
	print qq|</tr>|;
	
	# �v���C���[�����擾
	my @lines = &get_all_users;

	my $b_host = '';
	my $b_addr = '';
	my $count = 0;
	for my $line (@lines) {
		my($id, $name, $pass, $addr, $host, $ldate) = split /<>/, $line;
		
		# ����HostIP�������Ȃ�ԕ\��
		if ($host eq $b_host && $b_addr eq $addr) {
			print qq|<tr class="stripe2">|;
		}
		else {
			print ++$count % 2 == 0 ? qq|<tr class="stripe1">| : qq|<tr>|;
		}
		$b_host = $host;
		$b_addr = $addr;
		
		print qq|<td><input type="checkbox" name="delete" value="$id" /></td>|;
		print qq|<td><input type="button" class="button_s" value="���O�C��" onclick="location.href='$script?id=$id&pass=$pass';" /></td>|;
		print qq|<td>$name</td>|;
		print qq|<td>$id</td>|;
		print qq|<td><input type="button" class="button_s" value="�~�o" onclick="location.href='?mode=admin_refresh&pass=$in{pass}&id=$id&sort=$in{sort}';" /></td>|;
		print qq|<td>$addr</td>|;
		print qq|<td>$host</td>|;
		print qq|<td>$ldate</td></tr>|;
	}
	print qq|</table><br /><input type="checkbox" name="is_add_bl" value="1" checked="checked" />�u���b�N���X�g�ɒǉ�|;
	print qq|<p style="color: #F00">�v���C���[���폜����<br /><input type="submit" value="�폜" class="button_s" /></p></form>|;
}

#=================================================
# �폜����
#=================================================
sub admin_delete_user {
	return unless @delfiles;

	for my $delfile (@delfiles) {
		my %datas = &get_you_datas($delfile, 1);
		# �ᔽ�҃��X�g�ɒǉ�
		&add_black_list($datas{host}) if $in{is_add_bl};

		&delete_guild_member($datas{guild}, $datas{name}) if $datas{guild};
		&delete_directory("$userdir/$delfile");
		$mes .= "$datas{name}���폜���܂���<br />";
	}
	
	my $count = @delfiles;
	&minus_entry_count($count);
}

#=================================================
# ���Z�b�g�����F��ʐ^�����@�n�}�����ꍇ�Ɏg�p(��������ُ̈�G���[)
#=================================================
sub admin_refresh {
	return unless $in{id};
	
	local %m = &get_you_datas($in{id}, 1);
	$m{lib} = '';
	$m{wt} = $m{tp} = 0;
	$id = $in{id};
	&write_user;
	
	$mes .= "$m{name}���~�o���������܂���<br />";
}

#=================================================
# �S���[�U�[�̃f�[�^���擾
#=================================================
sub get_all_users {
	my @lines = ();
	opendir my $dh, "$userdir" or &error("$userdir�f�B���N�g�����J���܂���");
	while (my $id = readdir $dh) {
		next if $id =~ /\./;
		
		my %m = &get_you_datas($id, 1);

		my $line = "$id<>";
		for my $k (qw/name pass addr host ldate/) {
			$line .= "$m{$k}<>";
		}
		push @lines, "$line\n";
		
#		for my $k (qw/recipe/) {
#			unless (-f "$userdir/$id/$k.cgi") {
#				open my $fh, "> $userdir/$id/$k.cgi";
#				close $fh;
#				chmod $chmod, "$userdir/$id/$k.cgi";
#			}
#		}
	}
	closedir $dh;
	
	if    ($in{sort} eq 'name')    { @lines = map { $_->[0] } sort { $a->[2] cmp $b->[2] } map { [$_, split /<>/] } @lines; }
	elsif ($in{sort} eq 'addr')    { @lines = map { $_->[0] } sort { $a->[5] cmp $b->[5] || $a->[4] cmp $b->[4] } map { [$_, split /<>/] } @lines; }
	elsif ($in{sort} eq 'ldate')   { @lines = map { $_->[0] } sort { $b->[6] cmp $a->[6] } map { [$_, split /<>/] } @lines; }
	
	return @lines;
}

