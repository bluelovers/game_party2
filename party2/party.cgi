#!/usr/local/bin/perl
require 'config.cgi';
#================================================
# ���C��CGI Created by Merino
#================================================
&decode;
&access_check;
&header;
&read_user;
&error("���݃����e�i���X���ł��B���΂炭���҂���������(�� $mente_min ����)") if $mente_min;
require './lib/_data.cgi';
if    ($m{sleep} > 0)          { require "./lib/sleep.cgi";   } # �S������
#elsif (-f "./lib/$m{lib}.cgi") { require "./lib/$m{lib}.cgi"; }
elsif ($m{lib})                { require "./lib/$m{lib}.cgi"; }
else                           { require './lib/park.cgi';    } # �f�t�H���g�ꏊ
&read_member;
&set_action;
if ($com) {
	&action;
	&write_comment unless $mes;
}
&html;
&write_user;
&footer;


1; # login.cgi�œǂݍ���ł��邽��1
