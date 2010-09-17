#!/usr/local/bin/perl
require 'config.cgi';
#================================================
# メインCGI Created by Merino
#================================================
&decode;
&access_check;
&header;
&read_user;
&error("現在メンテナンス中です。しばらくお待ちください(約 $mente_min 分間)") if $mente_min;
require './lib/_data.cgi';
if    ($m{sleep} > 0)          { require "./lib/sleep.cgi";   } # 拘束時間
#elsif (-f "./lib/$m{lib}.cgi") { require "./lib/$m{lib}.cgi"; }
elsif ($m{lib})                { require "./lib/$m{lib}.cgi"; }
else                           { require './lib/park.cgi';    } # デフォルト場所
&read_member;
&set_action;
if ($com) {
	&action;
	&write_comment unless $mes;
}
&html;
&write_user;
&footer;


1; # login.cgiで読み込んでいるため1
