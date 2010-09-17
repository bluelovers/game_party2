# 最大ターン
$max_round = 60;

# マップ
@maps = (
	[b,0,0,0,0,0,0,0,F],#0
	[0,1,0,1,0,1,0,1,0],#1
	[0,0,A,1,0,1,3,T,0],#2
	[0,1,1,1,0,1,1,1,0],#3
	[0,0,0,0,S,0,0,D,0],#4
	[0,1,1,1,0,1,1,1,0],#5
	[0,T,2,1,0,1,B,0,0],#6
	[0,1,0,1,E,1,0,1,0],#7
	[C,0,0,0,0,0,0,0,G],#8
	#0,1,2,3,4,5,6,7,8
);

# イベント
sub event_2 { return if $event =~ /2/; $event .= '2'; &_add_treasure; }
sub event_3 { return if $event =~ /3/; $event .= '3'; &_add_treasure; }
sub event_A { $py=8; $px=8; }
sub event_C { $py=2; $px=6; }
sub event_D { $py=4; $px=3; }
sub event_E { $py=3; $px=4; }
sub event_F { $py=6; $px=2; }
sub event_G { $py=2; $px=2; }
sub event_T { $npc_com.= "<b>！！！！？</b>幻覚の霧が$mたちをつつみこんだ！"; for my $y (@partys) { $ms{$y}{state} = '混乱'; }; &add_monster; }
sub event_b { return if $event =~ /b/; $event .= 'b'; $npc_com.="ただならぬ気配を感じる…。どうやら、このダンジョンのボスのようだ！<br />"; &add_boss } # ボス


# 敵と宝の設定
my $_s = int(rand(4)+5);
require "$stagedir/$_s.cgi";



1; # 削除不可
