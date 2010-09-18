#=================================================
# ルイーダの酒場 Created by Merino
#=================================================
# 場所名
$this_title = 'ルイーダの酒場';

# NPC名
$npc_name   = '@ルイーダ';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/bar";

# 背景画像
$bgimg   = "$bgimgdir/bar.gif";



# メニュー
@foods = (
	# 名前,				値段,		HP回復,	MP回復,		福引券
	['アモールの水',		20,			40,			0,		1,	],
	['オレンジジュース',		50,			0,			30,		1,	],
	['トマトジュース',		100,		10,			80,		2,	],
	['コーヒー',			200,		0,			250,	3,	],
	['ハーブティー',			500,		0,			500,	5,	],
	['アイスクリーム',			100,		30,			30,		2,	],
	['プリン',			200,		60,			60,		3,	],
	['パフェ',			300,		100,		100,	4,	],
	['カレーライス',			400,		250,		0,		5,	],
	['スパゲティ',			600,		300,		50,		6,	],
	['オムライス',			750,		500,		100,	7,	],
	['ハンバーグ',			900,		800,		0,		8,	],
	['ステーキ',			1000,		999,		0,		10,	],
	['フルコース',			3000,		999,		999,	15,	],
);


#=================================================
# はなす言葉
#=================================================
@words = (
	"いらっしゃい。何か食べてく？",
	"$mさんは$foods[int(rand(@foods))][0]は好きかしら？",
	"食材にＭＰを回復させる魔法の聖水やＨＰを回復させる薬草がふくまれているのよ",
	"ＨＰを回復させたいならデザートやご飯物を食べていくといいわ",
	"ＭＰを回復させたいならドリンクを飲んでいくといいわ",
	"食べたり飲んだりした後は、運動しなきゃね",
	"お酒は大人になってからね",
);

#=================================================
# 画面ヘッダー
#=================================================
sub header_html {
	print qq|<div class="mes">【$this_title】$e2j{money}：<b>$m{money}</b>G $e2j{hp}：<b>$m{hp}</b>/<b>$m{mhp}</b>  $e2j{mp}：<b>$m{mp}</b>/<b>$m{mmp}</b></div>|;
}

#=================================================
# 追加アクション
#=================================================
push @actions, 'ちゅうもん';
$actions{'ちゅうもん'} = sub{ &chuumon }; 

#=================================================
# ＠ちゅうもん
#=================================================
sub chuumon {
	my $target = shift;
	
	if ($m{is_eat}) {
		$npc_com = "そんなに飲み食いするとお腹がこわれちゃうわよ？";
		return;
	}
	

	my $like_food;
	if (-s "$userdir/$id/profile.cgi") {
		open my $fh, "< $userdir/$id/profile.cgi";
		my $line = <$fh>;
		close $fh;
		($like_food) = ($line =~ /<>like_food;(.*?)<>/);
	}
	$foods[-1][0] = $like_food if $like_food;
	
	my $p = qq|<table class="table1"><tr><th>名前</th><th>値段</th></tr>|;
	for my $i (0 .. $#foods) {
		if ($foods[$i][0] eq $target) {
			if ($m{money} >= $foods[$i][1]) {
				$npc_com = "おまたせ、$foods[$i][0]よ♪";
				
				if ($foods[$i][2]) {
					$npc_com .= "$mの$e2j{hp}が回復した！";
					$m{hp} += $foods[$i][2];
					$m{hp} = $m{mhp} if $m{hp} > $m{mhp};
				}
				if ($foods[$i][3]) {
					$npc_com .= "$mの$e2j{mp}が回復した！";
					$m{mp} += $foods[$i][3];
					$m{mp} = $m{mmp} if $m{mp} > $m{mmp};
				}
				
				$npc_com .= "福引券を$foods[$i][4]枚もらった！";
				
				$m{is_eat} = 1;
				$m{money} -= $foods[$i][1];
				$m{coupon} += $foods[$i][4];
				&regist_guild_data('point', 2, $m{guild}) if $m{guild};
			}
			else {
				$mes = "お金が足りないみたいね";
			}
			return;
		}
		$p .= qq|<tr onclick="text_set('＠ちゅうもん>$foods[$i][0] ')"><td>$foods[$i][0]</td><td align="right">$foods[$i][1] G</td></tr>|;
	}
	$mes = qq|注文は何にするのかしら？<br />$p</table>|;
	$act_time = 0;
}



1; # 削除不可
