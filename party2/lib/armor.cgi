#=================================================
# 防具屋 Created by Merino
#=================================================
# 場所名
$this_title = '防具屋';

# NPC名
$npc_name = '@ｱﾏﾉ';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/armor";

# 背景画像
$bgimg = "$bgimgdir/armor.gif";

# 売っている防具(No)
@sales = $m{job_lv} > 11 ? (1..16) : (1..5+$m{job_lv});


#=================================================
# はなす言葉
#=================================================
@words = (
	"ここは防具屋ッス！防具を装備すればダメージを減らすことができるッス！",
	"$e2j{ag}がないと攻撃をかわすことができないッス！",
	"$e2j{ag}に自信がない場合は、ステテコパンツがオススメッス！",
	"強さや重さは１回の戦闘ごとで変わるッス！",
	"$mさんは$arms[$sales[int(rand(@sales))]][1]なんて似合いそうッスね！",
	"重い鎧でガチガチに固めるか、ヒラヒラの服で回避率を上げるのか、どちらが好きッスか？",
	"いつかあっしもあぶない水着を着るのが夢ッス",
	"$mさんの転職回数は$m{job_lv}回ッスね！転職回数が多いと熟練者と見なし売れる物が増えるッス！",
	"$mさんの$e2j{df}は$m{df}ッスね！。なかなかの固さッスね！",
);

sub shiraberu_npc {
	$mes = "$npc_name「な、な、何を見ているッスか！？」";
}

#=================================================
# 追加アクション
#=================================================
push @actions, ('かう', 'うる');
$actions{'かう'} = sub{ &kau }; 
$actions{'うる'} = sub{ &uru }; 


#=================================================
# ＠かう
#=================================================
sub kau {
	my $target = shift;
	
	my $p = qq|<table class="table1"><tr><th>名前</th><th>値段</th><th>強さ</th><th>重さ</th></tr>|;
	for my $i (@sales) {
		if ($arms[$i][1] eq $target) {
			if ($m{money} >= $arms[$i][2]) {
				if ($m{arm}) {
					&send_item($m, 2, $i);
					$npc_com = "お買い上げありがとうッス！$arms[$i][1]は$mさんの預かり所に送っておいたッス！";
				}
				else {
					$m{arm} = $i;
					$npc_com = "お買い上げありがとうッス！$arms[$i][1]どうぞ着てくださいッス";
					require "./lib/_add_collection.cgi";
					&add_collection;
				}
				$m{money} -= $arms[$i][2];
			}
			else {
				$mes = "残念ながら、お金が足りないッス";
			}
			return;
		}
		$p .= qq|<tr onclick="text_set('＠かう>$arms[$i][1] ')"><td>$arms[$i][1]</td><td align="right">$arms[$i][2] G</td><td align="right">$arms[$i][3]</td><td align="right">$arms[$i][4]</td></tr>|;
	}
	$p  .= qq|</table>|;
	$mes = qq|どれを買うッスか？<br />$p|;
	$act_time = 0;
}

#=================================================
# ＠うる
#=================================================
sub uru {
	my $target = shift;
	
	unless ($m{arm}) {
		$mes = "売りたい防具がある場合は、装備してきて欲しいッス！";
		return;
	}
	
	# 買取金額
	my $buy_price = int($arms[$m{arm}][2] * 0.5);
	
	if ($arms[$m{arm}][1] eq $target) {
		$npc_com = "$arms[$m{arm}][1] の買取代の $buy_price Gッス！";
		$m{money} += $buy_price;
		$m{arm} = 0;
		return;
	}

	$mes = qq|<span onclick="text_set('＠うる>$arms[$m{arm}][1] ')">$arms[$m{arm}][1]なら $buy_price Gで買い取るッス！</span>|;
	$act_time = 0;
}


1; # 削除不可
