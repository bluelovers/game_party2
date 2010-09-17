#=================================================
# モンスターブック Created by Merino
# _battle.cgiのsub defeatで使用
#=================================================
# コンプリートに必要な数
my $complete = 180;


#=================================================
# 追加
#=================================================
sub add_monster_book {
	my $y = shift or return;
	
	my $base_name = $y;
	$base_name =~ s/^\@//; # 戦闘の@を除く
	$base_name =~ s/[A-Z]$//; # 末尾のA～Zを除く

	my $new_no = $ms{$y}{icon};
	$new_no =~ s/[^0-9]//g;

	my @lines = ();
	open my $fh, "+< $userdir/$id/monster_book.cgi" or &error("$userdir/$id/monster_book.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($icon) = (split /<>/, $line)[2];
		return if $icon eq $ms{$y}{icon}; # すでに登録済みのモンスターなら更新しない
		push @lines, $line;
	}
	
	my $new_strong = &strong(%{ $ms{$y} });
	push @lines, "$new_no<>$base_name<>$ms{$y}{icon}<>$stage<>$new_strong<>$ms{$y}{mhp}<>$ms{$y}{mmp}<>$ms{$y}{mat}<>$ms{$y}{mdf}<>$ms{$y}{mag}<>$ms{$y}{get_exp}<>$ms{$y}{get_money}<>$date<>$map<>\n";
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;

	&write_monster_book(@lines);
	
	$npc_com .= "<br />" if $npc_com;
	$npc_com .= "<b>$base_nameのデータがモンスターブックに追加されました</b>";
}

#=================================================
# monster_book.html出力
#=================================================
sub write_monster_book {
	my @lines = @_;
	
	my $complete_par = int(@lines / $complete * 100);
	if ($complete_par >= 100) {
		unless (-f "$userdir/$id/comp_mon_flag.cgi") {
			open my $fh2, "> $userdir/$id/comp_mon_flag.cgi" or &error("$userdir/$id/comp_mon_flag.cgiファイルが開けません");
			close $fh2;
			
			&write_legend('comp_mon');
			&write_memory(qq|<span class="comp">MonsterBook Complete!!</span>|);
			&write_news(qq|<span class="comp">$mがモンスターブックをコンプリートしました！</span>|);
			$npc_com .= qq|<span class="comp">$mは <b>モンスターブック</b> をコンプリートしました！</span>|;
		}
		
		$complete_par = 100;
	}

	my $contents = '';
	for my $line (@lines) {
		$line =~ tr/\x0D\x0A//d; # 改行削除
		my($no, $name, $icon, $place, $strong, $hp, $mp, $at, $df, $ag, $exp, $money, $ldate, $dmap) = split /<>/, $line;
		my $stage_name = $place =~ /^king/ ? '封印戦' : defined($dmap) && $dmap ne '' ? $dungeons[$place] : $stages[$place];
		$contents .= qq|<tr><td>$no,</td><td><img src="../../$icondir/$icon" />$name</td><td>$stage_name</td><td align="right">$strong</td><td align="right">$hp</td><td align="right">$mp</td><td align="right">$at</td><td align="right">$df</td><td align="right">$ag</td><td align="right">$exp</td><td align="right">$money</td><td>$ldate</td></tr>\n|;
	}
	
	my $html = <<"EOM";
<html>
<head>
<title>$mのモンスターブック</title>
<link rel="stylesheet" type="text/css" href="../../$htmldir/party.css">
<link rel="stylesheet" type="text/css" href="../../$htmldir/jQuery/themes/green/style.css">
<script type="text/javascript" src="../../$htmldir/jQuery/jquery-latest.js"></script>
<script type="text/javascript" src="../../$htmldir/jQuery/jquery.tablesorter.js"></script>
<script type="text/javascript" src="../../$htmldir/jQuery/jquery.tablesorter.pager.js"></script>
<script type="text/javascript">
<!--
\$(document).ready(function() {
	\$(".tablesorter")
		.tablesorter({
			widgets: ['zebra'],
			sortList: [[0,0]]
		})
		.tablesorterPager({
			size: 50,
			positionFixed: false,
			container: \$("#pager")
		});
});
-->
</script>
</head>
<body>
<table><tr><td><form action="../../$script_index"><input type="submit" value="ＴＯＰへ戻る" /></form></td><td><form><input type="button" onclick="window.close(); return false;" value="閉じる"></form></td></tr></table>
<form action="../../player.cgi"><input type="hidden" name="id" value="$id"><input type="submit" value="$mの軌跡" /></form>

<h2>$mのモンスターブック　コンプリート率《<b>$complete_par</b>％》</h2>
<div id="pager" class="pager">
	<form>
		<img src="../../$htmldir/jQuery/addons/pager/icons/first.png" class="first" />
		<img src="../../$htmldir/jQuery/addons/pager/icons/prev.png" class="prev" />
		<input type="text" class="pagedisplay" />
		<img src="../../$htmldir/jQuery/addons/pager/icons/next.png" class="next" />
		<img src="../../$htmldir/jQuery/addons/pager/icons/last.png" class="last" />
		<select class="pagesize">
			<option value="30">30</option>
			<option value="50" selected="selected">50</option>
			<option value="100">100</option>
		</select>
	</form>
</div>
<table class="tablesorter">
<thead>
	<tr>
		<th>No</th>
		<th>名前</th>
		<th>生息地</th>
		<th>強さ</th>
		<th>ＨＰ</th>
		<th>ＭＰ</th>
		<th>攻撃</th>
		<th>守備</th>
		<th>素早</th>
		<th>経験値</th>
		<th>ゴールド</th>
		<th>登録日</th>
	</tr>
</thead>
<tbody>
	$contents
</tbody>
</table>
<br /><div align="right" style="font-size:11px">
＠パーティーII Ver$VERSION<br /><a href="http://cgi-sweets.com/" target="_blank">CGI-Sweets</a><br /><a href="http://amaraku.net/" target="_blank">Ama楽.net</a><br />
$copyright
</div>
</body>
</html>
EOM
	
	open my $fh, "> $userdir/$id/monster_book.html" or &error("$userdir/$id/monster_book.htmlファイルが開けません");
	print $fh $html;
	close $fh;
}


1; # 削除不可
