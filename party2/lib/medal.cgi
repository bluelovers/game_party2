#=================================================
# 交流広場 Created by Merino
#=================================================
# 場所名
$this_title = 'メダル王の城';

# NPC名
$npc_name   = '@メダル王';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/medal";

# 背景画像
$bgimg   = "$bgimgdir/medal.gif";


# 交換リスト
my @prizes = (
# 種類 1=武器,2=防具,3=道具 
# [0]*必要枚数,[1]種類,[2]No
#*交換は必要枚数で判断しているので、同じ枚数が複数はダメ
	[0,		0,		0,	],
	[3,		2,		32,	],
	[5,		3,		13,	],
	[8,		2,		33,	],
	[10,	1,		32,	],
	[15,	3,		36,	],
	[20,	3,		35,	],
	[25,	3,		37,	],
	[30,	3,		34,	],
	[35,	3,		89,	],
	[40,	1,		30,	],
	[45,	2,		35,	],
	[50,	2,		40,	],
	[60,	3,		109,],
	[77,	3,		107,],
	[100,	3,		59,	],
);

#=================================================
# はなす言葉
#=================================================
@words = (
	"わしはメダル王じゃ、小さなメダルを集めておる",
	"小さなメダルを持ってきたら代わりに褒美をやろう",
	"世界中の小さなメダルはわしのもんじゃ！",
	"わしの夢は小さなメダルを山ほど集めてだな…ムニャムニャ…",
	"小さなメダルをよこさんかい！",
	"自分の家で小さなメダルを使うと、わしの所にメダルが届けられるのじゃ",
	"小さなメダルはモンスターの住処の奥深くにあるらしいのじゃ",
	"$mからは小さなメダルを$m{medal}枚あずかっておるぞ",
);


#=================================================
# 追加アクション
#=================================================
push @actions, 'こうかん';
$actions{'こうかん'} = sub{ &koukan; }; 


#=================================================
# ステータス表示
#=================================================
sub header_html {
	print qq|<div class="mes">【$this_title】 メダル <b>$m{medal}</b>枚</div>|;
}

#=================================================
# ＠こうかん
#=================================================
sub koukan {
	my $target = shift;
	
	my $p = qq|<table class="table1"><tr><th>賞品</th><th>メダル</th></tr>|;
	for my $i (1 .. $#prizes) {
		if ("$prizes[$i][0]枚" eq $target) {
			if ($m{medal} >= $prizes[$i][0]) {
				if ($prizes[$i][1] eq '1') {
					&send_item($m, $prizes[$i][1], $prizes[$i][2]);
					$npc_com = "メダル$targetの賞品と交換するのじゃな！$weas[ $prizes[$i][2] ][1]は$mの預かり所に送っておいたぞ！";
				}
				elsif ($prizes[$i][1] eq '2') {
					&send_item($m, $prizes[$i][1], $prizes[$i][2]);
					$npc_com = "メダル$targetの賞品と交換するのじゃな！$arms[ $prizes[$i][2] ][1]は$mの預かり所に送っておいたぞ！";
				}
				else {
					&send_item($m, $prizes[$i][1], $prizes[$i][2]);
					$npc_com = "メダル$targetの賞品と交換するのじゃな！$ites[ $prizes[$i][2] ][1]は$mの預かり所に送っておいたぞ！";
				}
				$m{medal} -= $prizes[$i][0];
			}
			else {
				$mes = "小さなメダル$targetの賞品と交換するにはメダルが足りないぞ";
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
	$mes = qq|どれと交換するんじゃ？<br />$p|;
	$act_time = 0;
}


1; # 削除不可
