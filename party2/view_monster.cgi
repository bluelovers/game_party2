#!/usr/local/bin/perl
require 'config.cgi';
require './lib/_data.cgi';
#================================================
# �o�������X�^�[���m�F���邽�߂̂���(�Ǘ��p)
# http://������URL/party/_view_monster.cgi?pass=�Ǘ��҃p�X���[�h
# ���u������URL�v�Ƃ͂���CGI��ݒu�����ꏊ�܂ł̃A�h���X
#================================================

#=================================================
# ���C������
#=================================================
&header;
&decode;
&error("�p�X���[�h���Ⴂ�܂�") unless $in{pass} eq $admin_pass;
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
		
		print "�w$file_name�x<br>";
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

