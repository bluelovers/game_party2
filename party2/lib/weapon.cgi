#=================================================
# 武器屋 Created by Merino
#=================================================
# 場所名
$this_title = '武器屋';

# NPC名
$npc_name = '@ﾌﾞｯｷｰ';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/weapon";

# 背景画像
$bgimg = "$bgimgdir/weapon.gif";


# 売っている武器(No)
@sales = $m{job_lv} > 11 ? (1..5,43,6..16) : (1..5,43,6+$m{job_lv});


#=================================================
# はなす言葉
#=================================================
@words = (
	"ここは武器屋だ！戦いに武器は必須だぜ！",
	"$mには$weas[$sales[int(rand(@sales))]][1]なんか良いんじゃねぇか？",
	"$mには$weas[$sales[int(rand(@sales))]][1]がオススメだ！",
	"銅の剣はどぉの剣？",
	"よぉ！何か買っていくのか？",
	"素早さが高いと会心の一撃や回避率が上がるぞ！",
	"$e2j{at}が高い分、重さも重くなり$e2j{ag}が下がる。つまり、自分に合った装備をしろってことだ！",
	"この世界のどこかに、自分の強さにより武器の強さも変わる武器があるらしいぜ！",
	"モンスターにやられたとしてもお金が半分になることはないぜ！",
	"$mの$e2j{at}は$m{at}か…。$e2j{lv}$m{lv}にしてはなかなかだな！",
	"$mの転職回数は$m{job_lv}回か！転職回数が多ければ熟練者と見なし、もっと強い武器を売ってやるぜ！",
);

sub shiraberu_npc {
	$mes = "$npc_name「おいおい、俺は武器じゃねぇぜ」";
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
	
	my $h_no = &get_helper_item(1);
	
	my $p = qq|<table class="table1"><tr><th>名前</th><th>値段</th><th>強さ</th><th>重さ</th></tr>|;
	for my $i (@sales) {
		next if $h_no =~ /,$i,/; # 手助けクエストで依頼されているアイテムは除く
		$weas[$i][2] *= 2; # 錬金できるので２倍
		if ($weas[$i][1] eq $target) {
			if ($m{money} >= $weas[$i][2]) {
				if ($m{wea}) {
					&send_item($m, 1, $i);
					$npc_com = "まいど！$weas[$i][1]は$mの預かり所に送っておいたぜ！";
				}
				else {
					$m{wea} = $i;
					$npc_com = "まいど！$weas[$i][1]だ！受けとってくれ！";
					require "./lib/_add_collection.cgi";
					&add_collection;
				}
				$m{money} -= $weas[$i][2];
			}
			else {
				$mes = "お金が足りないみたいだぜ";
			}
			return;
		}
		$p .= qq|<tr onclick="text_set('＠かう>$weas[$i][1] ')"><td>$weas[$i][1]</td><td align="right">$weas[$i][2] G</td><td align="right">$weas[$i][3]</td><td align="right">$weas[$i][4]</td></tr>|;
	}
	$p  .= qq|</table>|;
	$mes = qq|何を買うんだい？<br />$p|;
	$act_time = 0;
}

#=================================================
# ＠うる
#=================================================
sub uru {
	my $target = shift;
	
	unless ($m{wea}) {
		$mes = "売るって何を売る気だ？$mは武器を持っていないようだが";
		return;
	}
	
	# 買取金額
	my $buy_price = int($weas[$m{wea}][2] * 0.5);
	
	if ($weas[$m{wea}][1] eq $target) {
		$npc_com = "$weas[$m{wea}][1] の買取代の $buy_price Gだ！";
		$m{money} += $buy_price;
		$m{wea} = 0;
		return;
	}

	$mes = qq|<span onclick="text_set('＠うる>$weas[$m{wea}][1] ')">$weas[$m{wea}][1]なら $buy_price Gで買い取るぜ！</span>|;
	$act_time = 0;
}


1; # 削除不可
