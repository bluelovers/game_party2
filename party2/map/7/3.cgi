# 最大ターン
$max_round = 60;

# マップ
@maps = (
	[0,1,0,1,4],
	[t,0,T,1,0],
	[1,0,1,1,D],
	[0,0,0,0,0],
	[0,1,0,1,B],
	[0,1,S,1,2],
	[0,1,0,1,1],
	[0,0,0,0,1],
	[0,1,1,0,1],
	[A,1,b,0,t],
	[3,1,K,1,0],
);

# イベント
$map_imgs{K} = '★' if $event !~ /D|K/;
$map_imgs{D} = '岩' if $event !~ /D|K/;
sub event_2 { return if $event =~ /2/; $event .= '2'; &_add_treasure; }
sub event_3 { return if $event =~ /3/; $event .= '3'; &_add_treasure; }
sub event_4 { return if $event =~ /4/; $event .= '4'; &_add_treasure; }
sub event_T { $npc_com.= "<b>！！！！？</b>しびれるようなガスが$mたちをつつみこんだ！"; for my $y (@partys) { $ms{$y}{state} = '麻痺'; }; &_add_monster; }
sub event_t { $npc_com.= "<b>！！！！？</b>高熱のガスがふきだしてきた！"; &_trap_d(140); }
sub event_A { return if $event =~ /A/; $event .= 'A'; $npc_com.="ただならぬ気配を感じる…。どうやら、このダンジョンのボスのようだ！<br />"; &add_boss } # ボス
sub event_b { return if $event =~ /b/; $event .= 'b'; $npc_com.="ただならぬ気配を感じる…。どうやら、このダンジョンのボスのようだ！<br />"; &add_boss } # ボス
sub event_K { return if $event =~ /D|K/; $event .= 'K'; $npc_com.="$mは何かスイッチのようなものを踏んでしまった！…ドゴオォォォォンッ！！…何かが壊れた音がした！";  }
sub event_D {
	return if $event =~ /D|K/;
	if ($m{job} eq '4' || $m{job} eq '25') {
		$com .= "<br />$m{mes}" if $m{mes};
		$npc_com .= "$mは全身の気を拳に集中させた…ドゴオォォォォォォォンッ！！！岩を破壊した！";
		$event .= 'D';
	}
	else {
		$npc_com .= "大きな岩で道がふさがれている！";
		++$py;
	}
}


# 敵と宝の設定
require "$mapdir/7/_data.cgi";



1; # 削除不可
