#!/usr/local/bin/perl
require 'config.cgi';
require '_side_menu.cgi';
#================================================
# 王者・英雄 Created by Merino
#================================================
my @files = (
#	[ 'タイトル', 'ログファイル名'],
	['王者ランキング',	'kill_p'],
	['英雄ランキング',	'kill_m'],
	['魔王ランキング',	'mao_c'],
	['勇者ランキング',	'hero_c'],
	['勝負師ランキング','cas_c'],
	['手助けランキング','help_c'],
	['錬金ランキング',	'alc_c'],
);

#================================================
&decode;
&header;
&run;
&footer;
exit;
#================================================
sub run {
	my @nos = ();
	my $contents = '<p>';
	for my $i (0 .. $#files) {
		next unless -s "$logdir/$files[$i][1].cgi";
		$contents .= $i eq $in{no} ? qq|$files[$i][0] / | : qq|<a href="ranking.cgi?no=$i">$files[$i][0]</a> / |;
		push @nos, $i;
	}
	$in{no} ||= $nos[0] || 0;
	$in{no} = 0 if $in{no} >= @files;

	$contents .= qq!</p><h2>$files[$in{no}][0]</h2><table class="table1"><tr><th>ランク</th><th>ポイント</th><th>名前＠ギルド</th><th>コメント</th></tr>!;
	my $count = 1;
	open my $fh, "< $logdir/$files[$in{no}][1].cgi" or &error("$logdir/$files[$in{no}][1]ファイルが読み込めません");
	while (my $line = <$fh>) {
		my($name, $guild, $color, $icon, $message, $point) = split /<>/, $line;
		$name .= "＠$guild" if $guild;
		$contents .= qq|<tr><td align="center">$count位</td><td align="center"><b>$point</b></td><td style="color: $color;"><img src="$icondir/$icon">$name</td><td>$message</td></tr>\n|;
		++$count;
	}
	close $fh;
	
	$contents .= qq|</table>|;
	&side_menu($contents);
}

