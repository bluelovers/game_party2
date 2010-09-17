# 最大ターン
$max_round = 60;

# マップ
@maps = (
	[3,0,0,0,0,t,0,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,S,0,0,0,0,1,0,0,0],
	[L,1,0,1,1,1,0,0,0,1,T],
	[0,1,0,1,0,0,0,I,0,0,0],
	[0,t,0,1,0,1,1,4,1,T,1],
	[0,1,0,1,0,H,1,1,1,1,1],
	[0,1,0,1,t,1,1,0,I,I,1],
	[0,T,0,0,0,0,0,0,1,B,2],
);

# イベント
$map_imgs{L} = '★';
$map_imgs{I} = $event =~ /L/ ? '□' : '■'; # レバーひかれたら道表示
sub event_I { return if $event =~ /L/; $npc_com .= "なんと！壁ではなく隠し通路になっていた！"; }
sub event_2 { return if $event =~ /2/; $event .= '2'; &_add_treasure; }
sub event_3 { return if $event =~ /3/; $event .= '3'; &_add_treasure; }
sub event_4 { return if $event =~ /4/; $event .= '4'; &_add_treasure; }
sub event_T { $npc_com.= "<b>！！！！？</b>周りの壁から毒ガスがふきだしてきた！"; for my $y (@partys) { $ms{$y}{state} = '猛毒'; }; &add_monster; }
sub event_t { $npc_com.= "<b>！！！！？</b>頭上から矢の雨がふりそそいできた！"; &_trap_d(80); }
sub event_H {
	return if $event =~ /H/;
	$npc_com.="テーブルの上に何やらあやしげな薬や高度な医学書が散らばっている…";
	if ($m{job} eq '43') {
		$event .= 'H';
		$npc_com.="$mは本に書いてあることを解読し回復薬を作り出した！全員のＨＰとＭＰが回復した！";
		for my $y (@partys) {
			$ms{$y}{hp} = $ms{$y}{mhp};
			$ms{$y}{mp} = $ms{$y}{mmp};
		}
	}
}
sub event_L {
	if ($event =~ /L/) {
		$npc_com.= rand(4) > 1 ? "レバーはすでに引かれている…" : rand(2) > 1 ? "$mの嫌いな食べ物はレバー…" : "$mの大好物はレバー…(￣￢￣)ｼﾞｭﾙﾘ…";
		return;
	}
	$event .= 'L';
	$npc_com.="$mはあやしげなレバーを引いてみた！…ｺﾞｺﾞｺﾞｺﾞｺﾞｺﾞｺﾞ…どこかの壁がくずれる音がした！<br />";
	$npc_com.="なんと、レバーのうしろの壁が崩れ、モンスターがおそいかかってきた！<br />";
	&add_boss;
}

# 敵と宝の設定
my $_s = int(rand(4)+5);
require "$stagedir/$_s.cgi";



1; # 削除不可
