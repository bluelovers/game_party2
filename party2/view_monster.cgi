#!/usr/local/bin/perl
require 'config.cgi';
require './lib/_data.cgi';
#================================================
# 出現モンスターを確認するためのもの(管理用)
# http://自分のURL/party/_view_monster.cgi?pass=管理者パスワード
# ※「自分のURL」とはこのCGIを設置した場所までのアドレス
#================================================

#=================================================
# メイン処理
#=================================================
&header;
&decode;
&error("パスワードが違います") unless $in{pass} eq $admin_pass;
&run;
&footer;
exit;

#=================================================
sub run {
	opendir my $dh, "./stage";
	while (my $file_name = readdir $dh) {
		next if $file_name =~ /^\./;
		next if $file_name =~ /sample/;
		require "./stage/$file_name";
		
		print "『$file_name』<br>";
		for my $no (0 .. $#bosses) {
			print qq|$bosses[$no]{name} <img src="./icon/$bosses[$no]{icon}">|;
			print qq| $jobs[$bosses[$no]{job}][1] SP $bosses[$no]{sp}| if $bosses[$no]{sp};
			print qq| $jobs[$bosses[$no]{old_job}][1] SP $bosses[$no]{old_sp}| if $bosses[$no]{old_sp};
			print qq|<br>|;
		}
		print qq|<hr>|;
		
		for my $no (0 .. $#monsters) {
			print qq|$monsters[$no]{name} <img src="./icon/$monsters[$no]{icon}">|;
			print qq| $jobs[$monsters[$no]{job}][1]     SP $monsters[$no]{sp}| if $monsters[$no]{sp};
			print qq| $jobs[$monsters[$no]{old_job}][1] SP $monsters[$no]{old_sp}| if $monsters[$no]{old_sp};
			print qq|<br>|;
		}
		print qq|<hr>|;
	}
	closedir $dh;
}

