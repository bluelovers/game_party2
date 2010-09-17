#=================================================
# 秘密の店 Created by Merino
#=================================================
# 場所名
$this_title = '秘密の店';

# NPC名
$npc_name = '@ﾋﾐﾂｼﾞ';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/secret";

# 背景画像
$bgimg = "$bgimgdir/item.gif";

# 売っている道具(No)
@sales = (10,15,80,78,43,27,30,31);


#=================================================
# はなす言葉
#=================================================
@words = (
	"バレちゃったメェ～。他の人には秘密だメェ～。",
	"値段は高いメェ～けれど、他では手に入らないレアものだメェ～。",
	"メェ～メェ～メェ～メェ～メェ～メェ～メェ～メェ～メェ～。",
	"ベェ～ベェ～ベェ～ベェ～ベェ～ベェ～ベェ～ベェ～ベェ～。",
	"＠ぱふぱふはサービスだメェ～。",
);

sub shiraberu_npc {
	$mes = "$npc_name「オイラは羊の$npc_nameだメェ～。羊の国から来たよ…ゴホッゴホッ…羊の国から来たメェ～」";
}

#=================================================
# 追加アクション
#=================================================
push @actions, 'かう';
push @actions, 'ぱふぱふ';
$actions{'かう'} = sub{ &kau }; 
$actions{'ぱふぱふ'} = sub{ &pafupafu }; 

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
					$npc_com = "$ites[$i][1]は$mメェ～の預かり所の方に投げましたメェ～";
				}
				else {
					$m{ite} = $i;
					$npc_com = "$ites[$i][1]メェ～。持ってけメェ～";
					require "./lib/_add_collection.cgi";
					&add_collection;
				}
				$m{money} -= $ites[$i][2];
			}
			else {
				$mes = "お金が足らメェ～";
			}
			return;
		}
		$p .= qq|<tr onclick="text_set('＠かう>$ites[$i][1] ')"><td>$ites[$i][1]</td><td align="right">$ites[$i][2] G</td></tr>|;
	}
	$p  .= qq|</table>|;
	$mes = qq|どれを買うメェ～？<br />$p|;
	$act_time = 0;
}

sub pafupafu {
	$to_name  = $m;
	$npc_com  = qq|パフパフ<font color="#FFB6C1">&hearts;</font> パフパフ<font color="#FFB6C1">&hearts;</font> パフパフ<font color="#FFB6C1">&hearts;</font>………|;
	$npc_com .= qq|どうだ $m わしのパフパフは気持ちいいだろう|;
}


1; # 削除不可
