#=================================================
# 交流広場 Created by Merino
#=================================================
# 場所名
$this_title = '闇市場';

# NPC名
$npc_name   = '@闇商人';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/black_market";

# 背景画像
$bgimg   = "$bgimgdir/black_market.gif";

# レアアイテム
@rare_items = (
[29,30,33..40],
[35..40],
[28,29,40,57..71,87,104..107,109],
);


# 交換対象
@prizes = (
# [道具No, レアポイント],
[87, 1],
[57, 4],
[60, 2],
[61, 2],
[62, 2],
[63, 2],
[64, 2],
[65, 2],
);

#=================================================
# はなす言葉
#=================================================
@words = (
	"よく来たな…。ここは闇市場だ…",
	"表\の世界では手に入れられない物を取引している…",
	"物の取引は金では買えないもの…。つまり、魂…ゴホッゴホッ…ではなく、レアアイテムだ…",
	"お前の魂…ではなく、お前が装備しているレアアイテムをささげろ…",
	"レアアイテムをささげることによって…お前のレアポイントが増える…",
	"レアポイントにより取引できるアイテムが違う…",
);

#=================================================
# ＠しらべる>NPC
#=================================================
sub shiraberu_npc {
	$mes = "…お前の魂で取引したいのか？";
}

#=================================================
# 追加アクション
#=================================================
push @actions, 'ささげる';
push @actions, 'とりひき';
$actions{'ささげる'} = sub{ &sasageru }; 
$actions{'とりひき'} = sub{ &torihiki }; 


#=================================================
# ステータス表示
#=================================================
sub header_html {
	print qq!<div class="mes">【$this_title】 レアポイント <b>$m{rare}</b>ポイント!;
	print qq| E：$weas[$m{wea}][1]| if $m{wea};
	print qq| E：$arms[$m{arm}][1]| if $m{arm};
	print qq| E：$ites[$m{ite}][1]| if $m{ite};
	print qq|</div>|;
}

#=================================================
# ＠とりひき
#=================================================
sub torihiki {
	my $target = shift;
	
	my $p = qq|<table class="table1"><tr><th>商品</th><th>レアポイント</th></tr>|;
	for my $i (0 .. $#prizes) {
		if ($ites[ $prizes[$i][0] ][1] eq $target) {
			if ($m{rare} >= $prizes[$i][1]) {
				&send_item($m, 3, $prizes[$i][0]);
				$npc_com = "取引成立だ…。$ites[ $prizes[$i][0] ][1] はお前の預かり所に送っておいた…";
				$m{rare} -= $prizes[$i][1];
			}
			else {
				$mes = "レアポイント不足だ…";
			}
			return;
		}
	
		$p .= qq|<tr onclick="text_set('＠とりひき>$ites[ $prizes[$i][0] ][1] ')"><td>$ites[ $prizes[$i][0] ][1]</td><td align="right">$prizes[$i][1] Pt</td></tr>|;
	}
	$p  .= qq|</table>|;
	$mes = qq|どれと取引するんだ…？<br />$p|;
	$act_time = 0;
}



#=================================================
# ＠ささげる
#=================================================
sub sasageru {
	my $target = shift;

	unless ($target) {
		$mes .= qq|<span onclick="text_set('＠ささげる>$weas[$m{wea}][1] ')">$weas[$m{wea}][1]</span> / | if $m{wea};
		$mes .= qq|<span onclick="text_set('＠ささげる>$arms[$m{arm}][1] ')">$arms[$m{arm}][1]</span> / | if $m{arm};
		$mes .= qq|<span onclick="text_set('＠ささげる>$ites[$m{ite}][1] ')">$ites[$m{ite}][1]</span> / | if $m{ite};
		$mes = 'ささげるものを装備して来い…' unless $mes;
		return;
	}
	
	if ($weas[$m{wea}][1] eq $target) {
		for my $rare_item (@{ $rare_items[0] }) {
			if ($m{wea} eq $rare_item) {
				$m{wea} = 0;
				$npc_com.="…$target…か…。レアだな…。いいだろう…。お前のレアポイントを加算しておこう…";
				$m{rare} += 1;
				return;
			}
		}
		$npc_com.="…$target…か…。ダメだな…。そのアイテムは…めずらしくない…";
	}
	elsif ($arms[$m{arm}][1] eq $target) {
		for my $rare_item (@{ $rare_items[1] }) {
			if ($m{arm} eq $rare_item) {
				$m{arm} = 0;
				$npc_com.="…$target…か…。レアだな…。いいだろう…。お前のレアポイントを加算しておこう…";
				$m{rare} += 1;
				return;
			}
		}
		$npc_com.="…$target…か…。ダメだな…。そのアイテムは…めずらしくない…";
	}
	elsif ($ites[$m{ite}][1] eq $target) {
		for my $rare_item (@{ $rare_items[2] }) {
			if ($m{ite} eq $rare_item) {
				$m{ite} = 0;
				$npc_com.="…$target…か…。レアだな…。いいだろう…。お前のレアポイントを加算しておこう…";
				$m{rare} += 1;
				return;
			}
		}
		$npc_com.="…$target…か…。ダメだな…。そのアイテムは…めずらしくない…";
	}
	else {
		$mes = 'ささげるものを装備して来い…';
	}
}




1; # 削除不可
