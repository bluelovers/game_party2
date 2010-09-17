#=================================================
# 家具屋 Created by Merino
#=================================================
# 場所名
$this_title = 'オラクル屋';

# NPC名
$npc_name = '@ﾗｸﾙ';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/goods";

# 背景画像
$bgimg = "$bgimgdir/goods.gif";

# 売っている道具(No)
@sales = $m{job_lv} > 10  ? (44..56) : (44..45+$m{job_lv});
push @sales, (138..141) if $m{job_lv} > 15;

#=================================================
# はなす言葉
#=================================================
@words = (
	"おっ！久しぶりのお客だ！よく来たよく来た！ここは$this_titleだよ",
	"＠かべがみでそなたの家をオシャレにすることができるよん",
	"壁紙は買ってしばらくしたら、こちらで勝手に張り替えておくよん。すぐ確認したい人は自分の家で更新ボタンを押すといいよ",
	"衣装は着た時からその日限りのレンタルだよ、次の日には返してもらうよ",
	"衣装は転職するときにも返してもらうよ",
);

#=================================================
# ＠しらべる>NPC
#=================================================
sub shiraberu_npc {
	$mes = qq|<span onclick="text_set('＠やみいちば に行きたい')">$npc_name「おっ？なんじゃなんじゃ？わしゃ何も知らんよ」</span>|;
}

#=================================================
# 追加アクション
#=================================================
push @actions, 'かう';
push @actions, 'かべがみ';
$actions{'かう'}     = sub{ &kau }; 
$actions{'かべがみ'} = sub{ &kabegami }; 
$actions{'やみいちば'} = sub{ &yamiichiba };

#=================================================
# ＠やみいちば
#=================================================
sub yamiichiba {
	return if $m{job_lv} < 15;
	$mes = "闇市場を見つけました！";
	$m{lib} = 'black_market';
	&auto_reload;
}

#=================================================
# ＠かう
#=================================================
sub kau {
	my $target = shift;
	
	my $h_no = &get_helper_item(3);

	my $p = qq|<table class="table1"><tr><th>名前</th><th>値段</th></tr>|;
	for my $i (@sales) {
		next if $h_no =~ /,$i,/; # 手助けクエストで依頼されているアイテムは除く
		if ($ites[$i][1] eq $target) {
			if ($m{money} >= $ites[$i][2]) {
				if ($m{ite}) {
					&send_item($m, 3, $i);
					$npc_com = "$ites[$i][1]は$mの預かり所に送っておいたよん";
				}
				else {
					$m{ite} = $i;
					$npc_com = "$ites[$i][1]だな。ほい、どうぞ";
					require "./lib/_add_collection.cgi";
					&add_collection;
				}
				$m{money} -= $ites[$i][2];
			}
			else {
				$mes = "$mよ…ゴールドが足らん";
			}
			return;
		}
		$p .= qq|<tr onclick="text_set('＠かう>$ites[$i][1] ')"><td>$ites[$i][1]</td><td align="right">$ites[$i][2] G</td></tr>|;
	}
	$p  .= qq|</table>|;
	$mes = qq|どれを買うのだ？<br />$p|;
	$act_time = 0;
}

#=================================================
# ＠かべがみ
#=================================================
sub kabegami {
	my $target = shift;
	
	my $count = 0;
	my $p = qq|<table><tr>|;
	for my $k (sort { $kabes{$a} <=> $kabes{$b} } keys %kabes) {
		my $base_name = $k;
		$base_name =~ s/(.+)\..+/$1/; # 見栄えが悪いので拡張子を除く
		
		if ($base_name eq $target) {
			if ($m{money} >= $kabes{$k}) {
				&copy("$bgimgdir/$k", "$userdir/$id/bgimg.gif");
				$npc_com   = qq|$mの家の壁紙を $base_name に、張り替えておいたよん|;
				$m{money} -= $kabes{$k};
			}
			else {
				$mes = "$mよ…ゴールドが足らん";
			}
			return;
		}
		$p .= qq|<td valign="bottom"><span onclick="text_set('＠かべがみ>$base_name ')"><img src="$bgimgdir/$k" title="$base_name" /><br />$kabes{$k} G</span></td>|;
		$p .= qq|</tr><tr>| if ++$count % 10 == 0;
	}
	$p .= qq|</tr></table>|;

	$mes = qq|どの壁紙にするのだ？<br />$p|;
	$act_time = 0;
}


1; # 削除不可
