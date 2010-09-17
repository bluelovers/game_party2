#!/usr/local/bin/perl
require 'config.cgi';
require './lib/_data.cgi';
my $this_script = 'admin.cgi';
#=================================================
# プレイヤー管理 Created by Merino
#=================================================
# 並び順名
my %e2j_sorts = (
	name	=> '名前順',
	ldate	=> '更新日時順',
	addr	=> 'Host/IP順',
);

# デフォルトの並び順
$in{sort} ||= 'addr';

#=================================================
# メイン処理
#=================================================
&header;
&decode;
&error("パスワードが違います") unless $in{pass} eq $admin_pass;
if ($in{mode} eq 'admin_delete_user') { &admin_delete_user; }
&top;
&footer;
exit;

#=================================================
# top
#=================================================
sub top {
	print qq|<table><tr>|;
	print qq|<td><form action="$script_index"><input type="submit" value="ＴＯＰ" class="button_s" /></form></td>|;
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
	print qq|救出は、画面に何も表\示されなくなったり、ループにはまった状態などを修正します。<br />|;
	print qq|<table class="table2"><tr>|;

	for my $k (qw/削除 ログイン 名前 フォルダ リセット IPアドレス ホスト名 更新時間/) {
		print qq|<th>$k</th>|;
	}
	print qq|</tr>|;
	
	# プレイヤー情報を取得
	my @lines = &get_all_users;

	my $b_host = '';
	my $b_addr = '';
	my $count = 0;
	for my $line (@lines) {
		my($id, $name, $pass, $addr, $host, $ldate) = split /<>/, $line;
		
		# もしHostIPが同じなら赤表示
		if ($host eq $b_host && $b_addr eq $addr) {
			print qq|<tr class="stripe2">|;
		}
		else {
			print ++$count % 2 == 0 ? qq|<tr class="stripe1">| : qq|<tr>|;
		}
		$b_host = $host;
		$b_addr = $addr;
		
		print qq|<td><input type="checkbox" name="delete" value="$id" /></td>|;
		print qq|<td><input type="button" class="button_s" value="ログイン" onclick="location.href='$script?id=$id&pass=$pass';" /></td>|;
		print qq|<td>$name</td>|;
		print qq|<td>$id</td>|;
		print qq|<td><input type="button" class="button_s" value="救出" onclick="location.href='?mode=admin_refresh&pass=$in{pass}&id=$id&sort=$in{sort}';" /></td>|;
		print qq|<td>$addr</td>|;
		print qq|<td>$host</td>|;
		print qq|<td>$ldate</td></tr>|;
	}
	print qq|</table><br /><input type="checkbox" name="is_add_bl" value="1" checked="checked" />ブラックリストに追加|;
	print qq|<p style="color: #F00">プレイヤーを削除する<br /><input type="submit" value="削除" class="button_s" /></p></form>|;
}

#=================================================
# 削除処理
#=================================================
sub admin_delete_user {
	return unless @delfiles;

	for my $delfile (@delfiles) {
		my %datas = &get_you_datas($delfile, 1);
		# 違反者リストに追加
		&add_black_list($datas{host}) if $in{is_add_bl};

		&delete_guild_member($datas{guild}, $datas{name}) if $datas{guild};
		&delete_directory("$userdir/$delfile");
		$mes .= "$datas{name}を削除しました<br />";
	}
	
	my $count = @delfiles;
	&minus_entry_count($count);
}

#=================================================
# リセット処理：画面真っ黒　ハマった場合に使用(何かしらの異常エラー)
#=================================================
sub admin_refresh {
	return unless $in{id};
	
	local %m = &get_you_datas($in{id}, 1);
	$m{lib} = '';
	$m{wt} = $m{tp} = 0;
	$id = $in{id};
	&write_user;
	
	$mes .= "$m{name}を救出処理をしました<br />";
}

#=================================================
# 全ユーザーのデータを取得
#=================================================
sub get_all_users {
	my @lines = ();
	opendir my $dh, "$userdir" or &error("$userdirディレクトリが開けません");
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

