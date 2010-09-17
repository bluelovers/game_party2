#=================================================
# イベント広場 Created by Merino
# プレイヤー数により商人出現
#=================================================
# 場所名
$this_title = 'イベント広場';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/event";

# 背景画像
$bgimg = "$bgimgdir/event.gif";


sub _get_count {
	open my $fh, "< ${this_file}_member.cgi" or &error("${this_file}_member.cgiファイルが読み込めません");
	my @lines = <$fh>;
	close $fh;
	
	my $count = @lines;
	return $count;
}

my $c_member = &_get_count;

if ($c_member < 10) { # 10人未満ならイベント起こらず
	return 1;
}
elsif ($c_member >= 30) {
	# 売っている道具(No)
	@sales = (90..100,108);
	$bgimg = "$bgimgdir/event3.gif";
}
elsif ($c_member >= 20) {
	# 売っている道具(No)
	@sales = (73,74,77,5,75,85);
	$bgimg = "$bgimgdir/event2.gif";
}
else {
	# 売っている道具(No)
	@sales = (72,81,82,83,84,86);
	$bgimg = "$bgimgdir/event1.gif";
}

$npc_name = '@旅の商人';
sub _add_akindo {
	open my $fh, ">> ${this_file}_member.cgi" or &error("${this_file}_member.cgiファイルが開けません");
	print $fh "$time<>0<>@旅の商人<>0<>chr/024.gif<>$npc_color<>\n";
	close $fh;
}

&_add_akindo;

#=================================================
# はなす言葉
#=================================================
@words = (
	"おや、たくさんの人が集まって何かあるんですか？",
	"バザーでもやるんですかねぇ",
	"たくさん人がいて、にぎやかですね",
	"では、商売でもさせてもらいましょうか",
);

#=================================================
# ＠しらべる>NPC
#=================================================
sub shiraberu_npc {
	$mes = "なんと、薬草を見つけた！…が人の物を盗ってはいけない…";
}

#=================================================
# 追加アクション
#=================================================
push @actions, ('かう');
$actions{'かう'} = sub{ &kau }; 

#=================================================
# ＠かう
#=================================================
sub kau {
	my $target = shift;
	
	my $p = qq|<table class="table1"><tr><th>名前</th><th>値段</th></tr>|;
	for my $i (@sales) {
		$ites[$i][2] *= 3; # 特別なので3倍の値段
		if ($ites[$i][1] eq $target) {
			if ($m{money} >= $ites[$i][2]) {
				if ($m{ite}) {
					&send_item($m, 3, $i);
					$npc_com = "$ites[$i][1]は$mさんの預かり所に送っておきましたよ";
				}
				else {
					$m{ite} = $i;
					$npc_com = "はい、$ites[$i][1]です";
					require "./lib/_add_collection.cgi";
					&add_collection;
				}
				$m{money} -= $ites[$i][2];
			}
			else {
				$mes = "お金が足らないようですが…";
			}
			return;
		}
		$p .= qq|<tr onclick="text_set('＠かう>$ites[$i][1] ')"><td>$ites[$i][1]</td><td align="right">$ites[$i][2] G</td></tr>|;
	}
	$p  .= qq|</table>|;
	$mes = qq|では商売をさせてもらいましょう<br />$p|;
	$act_time = 0;
}



1; # 削除不可
