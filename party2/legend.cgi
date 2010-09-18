#!/usr/local/bin/perl
require 'config.cgi';
require '_side_menu.cgi';
#================================================
# 伝説 Created by Merino
#================================================
# 表示するもの　★追加削除並べ替え可能
my @files = (
#	['タイトル',			'ログファイル名'],
	['ジョブマスター',		'comp_job'	],
	['モンスターマスター',	'comp_mon'	],
	['ウェポンキラー',		'comp_wea'	],
	['アーマーキング',		'comp_arm'	],
	['アイテムニスト',		'comp_ite'	],
	['アルケミスト',		'comp_alc'	],
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
		$contents .= $i eq $in{no} ? qq|$files[$i][0] / | : qq|<a href="legend.cgi?no=$i">$files[$i][0]</a> / |;
		push @nos, $i;
	}
	$in{no} ||= $nos[0] || 0;
	$in{no} = 0 if $in{no} >= @files;

	$contents .= qq|</p><h2>$files[$in{no}][0]</h2><table class="table1"><tr><th>記念日</th><th>名前＠ギルド</th><th>コメント</th></tr>|;
	open my $fh, "< $logdir/$files[$in{no}][1].cgi" or &error("$logdir/$files[$in{no}][1]ファイルが読み込めません");
	while (my $line = <$fh>) {
		my($name, $guild, $color, $icon, $message, $ldate) = split /<>/, $line;
		$name .= "＠$guild" if $guild;
		$contents .= qq|<tr><td>$ldate</td><td style="color: $color;"><img src="$icondir/$icon">$name</td><td>$message</td></tr>\n|;
	}
	close $fh;
	
	$contents .= "</table>";
	&side_menu($contents);
}

