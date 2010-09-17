#!/usr/local/bin/perl
require 'config.cgi';
#================================================
# ﾜﾝｸｯｼｮﾝﾘﾝｸ Created by Merino
#================================================
# 直ﾘﾝするとIDとﾊﾟｽがﾘﾌｧﾗｰなどに洩れてしまうため。

&header;
&run;
&footer;
exit;

#================================================

sub run {
	my $url = $ENV{'QUERY_STRING'};

	$url =~ s/&#44;/,/g;
	$url =~ s/&lt;/</g;
	$url =~ s/&gt;/>/g;
	$url =~ s/&quot;/"/g;
	$url =~ s/&amp;/&amp/g;
	$url =~ s/&#59;/;/g;
	$url =~ s/&amp/&/g;
	print qq|<div class="mes">下記のページにジャンプしようとしています。問題ない場合はクリックしてください。<p><a href="$url">$url</a></p><br /></div>|;
}

