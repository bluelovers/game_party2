# 最大ターン
$max_round = 50;

# マップ
@maps = (
	[2,0,0,0,0,0,0,0,0,0,0],
	[0,C,0,0,0,W,0,0,0,2,A],
	[D,0,0,0,0,0,0,0,W,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,A,0,0,W,S,0,0,0,0,0],
	[0,0,0,0,0,W,0,0,0,0,0],
	[0,0,0,0,0,0,0,W,0,0,0],
	[W,0,A,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,D,0],
	[3,0,0,0,0,B,0,0,4,0,0],
);

# イベント
$map_imgs{1} = '□';
sub event_W { $py=int(rand(5)+3); $px=int(rand(5)+3); }
sub event_1 { $py=int(rand(5)+3); $px=int(rand(5)+3); }
sub event_2 { return if $event =~ /2/; $event .= '2'; &_add_treasure; }
sub event_3 { return if $event =~ /3/; $event .= '3'; &_add_treasure; }
sub event_4 { return if $event =~ /4/; $event .= '4'; &_add_treasure; }
sub event_A { return if $event =~ /A/; $event .= 'A'; $npc_com.="ただならぬ気配を感じる…。どうやら、このダンジョンのボスのようだ！<br />"; &add_boss } # ボス
sub event_C { return if $event =~ /C/; $event .= 'C'; $npc_com.="ただならぬ気配を感じる…。どうやら、このダンジョンのボスのようだ！<br />"; &add_boss } # ボス
sub event_D { return if $event =~ /D/; $event .= 'D'; $npc_com.="ただならぬ気配を感じる…。どうやら、このダンジョンのボスのようだ！<br />"; &add_boss } # ボス

# 敵と宝の設定
my $_s = int(rand(5)+10);
require "$stagedir/$_s.cgi";



1; # 削除不可
