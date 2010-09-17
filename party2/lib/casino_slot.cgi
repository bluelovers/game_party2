#=================================================
# 武器屋 Created by Merino
#=================================================
# 場所名
$this_title = 'カジノ';

# NPC名
$npc_name = '@ﾊﾞﾆｰ';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/casino_slot";

# 背景画像
$bgimg = "$bgimgdir/casino.gif";


# 交換リスト
my @prizes = (
# 種類 1=武器,2=防具,3=道具 
#*交換は必要枚数で判断しているので、同じ枚数が複数はダメ
#  [0]*必要枚数,[1]種類,[2]No
	[0,			0,		0,	],
	[100,		3,		4,	],
	[300,		3,		12,	],
	[700,		3,		6,	],
	[2000,		3,		32,	],
	[4000,		3,		38,	],
	[5000,		3,		39,	],
	[8000,		2,		34,	],
	[30000,		1,		31,	],
	[70000,		1,		40,	],
	[80000,		1,		38,	],
);

#=================================================
# ヘッダー表示
#=================================================
sub header_html {
	print qq|<div class="mes">【$this_title】 コイン<b>$m{coin}</b>枚 / ゴールド<b>$m{money}</b>G</div>|;
}


#=================================================
# はなす言葉
#=================================================
@words = (
	"コインは１枚20Gです☆",
	"ゴールドをコインに両替してね☆",
	"賞品は他ではなかなか手に入れることができないレアなアイテムばかりよ☆",
	"スロットの絵柄を３つそろえるとコインが増えて幸せになれるわよ☆",
	"ゆっくりしていってね☆",
);

sub shiraberu_npc {
	$mes = "$npc_name「きゃぁッ☆エッチィ～☆」";
}

#=================================================
# 追加アクション
#=================================================
push @actions, ('＄1すろっと', '＄10すろっと', '＄50すろっと','＄100すろっと', 'こうかん', 'りょうがえ',);
$actions{'＄1すろっと'}   = sub{ &slot_1   }; 
$actions{'＄10すろっと'}  = sub{ &slot_10  }; 
$actions{'＄50すろっと'}  = sub{ &slot_50  }; 
$actions{'＄100すろっと'} = sub{ &slot_100 }; 
$actions{'こうかん'}      = sub{ &koukan  }; 
$actions{'りょうがえ'}    = sub{ &ryougae }; 

#=================================================
# ＠すろっと
#=================================================
sub slot_1   { &_slot(1) }
sub slot_10  { &_slot(10) }
sub slot_50  { &_slot(50) }
sub slot_100 { &_slot(100) }
sub _slot {
	my $bet = shift;
	
	if ($m{tired} >= 100) {
		$mes = qq|<span onclick="text_set('＠ほーむ ')">$e2j{tired}がたまっています。「＠ほーむ」で家に帰り「＠ねる」で休んでください</span>|;
		return;
	}
	if ($m{coin} < $bet) {
		$mes = qq|<span onclick="text_set('＠りょうがえ ')">＄$betスロットをするコインが足りません。「＠りょうがえ」でコインを両替してください</span>|;
		return;
	}
	
	my @m = ('∞','♪','†','★','７');
	my @o = (3,10, 20,  50,  70,  100); # オッズ 一番左はチェリーが2つそろいのとき
	my @s = ();
	$s[$_] = int(rand(@m)) for (0 .. 2);
	$mes .= qq|<span onclick="text_set('＠＄$betすろっと')">|;
	$mes .= "\$$betスロット<br />";
	$mes .= "【$m[$s[0]]】【$m[$s[1]]】【$m[$s[2]]】<br />";
	$m{coin} -= $bet;

	# 連打防止策
	$act_time *= 0.5;
	$m{wt}  = $time + $act_time;
	$nokori = $act_time;

	if ($s[0] == $s[1]) { # 1つ目と2つ目
		if ($s[1] == $s[2]) { # 2つ目と3つ目
			my $v = $bet * $o[$s[0]+1]; # +1 = チェリー2そろい
			$m{coin} += $v;
			$mes .= "なんと!! $m[$s[0]] が3つそろいました!!<br />";
			$mes .= "おめでとうございます!!<br />";
			$mes .= "***** コイン $v 枚 GET !! *****<br />";
		}
		elsif ($s[0] == 0) { # チェリーのみ1つ目と2つ目がそろえばよい
			my $v = $bet * $o[0];
			$m{coin} += $v;
			$mes .= "チェリーが2つそろいました♪<br />";
			$mes .= "コイン $v 枚Up♪<br />";
		}
		else {
			$mes .= "ハズレ<br />";
			$m{tired} += 1;
		}
	}
	else {
		$mes .= "ハズレ<br />";
		$m{tired} += 1;
	}
	$mes .= "</span>";
}


#=================================================
# ＠こうかん
#=================================================
sub koukan {
	my $target = shift;
	
	my $p = qq|<table class="table1"><tr><th>賞品</th><th>ｺｲﾝ</th></tr>|;
	for my $i (1 .. $#prizes) {
		if ("$prizes[$i][0]枚" eq $target) {
			if ($m{coin} >= $prizes[$i][0]) {
				if ($prizes[$i][1] eq '1') {
					&send_item($m, $prizes[$i][1], $prizes[$i][2]);
					$npc_com = "コイン$targetの賞品と交換ですね！$weas[ $prizes[$i][2] ][1]は$mの預かり所に送っておきました";
				}
				elsif ($prizes[$i][1] eq '2') {
					&send_item($m, $prizes[$i][1], $prizes[$i][2]);
					$npc_com = "コイン$targetの賞品と交換ですね！$arms[ $prizes[$i][2] ][1]は$mの預かり所に送っておきました";
				}
				else {
					&send_item($m, $prizes[$i][1], $prizes[$i][2]);
					$npc_com = "コイン$targetの賞品と交換ですね！$ites[ $prizes[$i][2] ][1]は$mの預かり所に送っておきました";
				}
				$m{coin} -= $prizes[$i][0];
			}
			else {
				$mes = "コイン$targetの賞品と交換するのにコインが足りません";
			}
			return;
		}
	
		$p .= qq|<tr onclick="text_set('＠こうかん>$prizes[$i][0]枚 ')"><td>|;
		$p .= $prizes[$i][1] eq '1' ? $weas[$prizes[$i][2]][1]
		    : $prizes[$i][1] eq '2' ? $arms[$prizes[$i][2]][1]
		    :                         $ites[$prizes[$i][2]][1]
		    ;
		$p .= qq|</td><td align="right">$prizes[$i][0]枚</td></tr>|;
	}
	$p  .= qq|</table>|;
	$mes = qq|どれと交換しますか？<br />$p|;
	$act_time = 0;
}

#=================================================
# ＠りょうがえ
#=================================================
sub ryougae {
	my $target = shift;
	$target =~ s/枚//;

	if ($target < 1 || $target =~ /[^0-9]/) {
		$mes = qq|<span onclick="text_set('＠りょうがえ>')">コイン１枚 20 Gです。いくら両替しますか？</span>|;
		return;
	}

	my $need_money = $target * 20;
	if ($need_money > $m{money}) {
		$mes = "ゴールドが足りません。コイン$target枚を両替するには $need_money G必要です";
		return;
	}
	
	$m{coin}  += $target;
	$m{money} -= $need_money;
	$npc_com = "$target枚のコインと両替しました";
}


1; # 削除不可
