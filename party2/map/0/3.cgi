# 最大ターン
$max_round = 20;

# マップ
@maps = (
	[0,I,0,0,2],
	[0,1,B,1,1],
	[0,I,0,0,0],
	[0,1,1,1,0],
	[0,0,S,0,0],
);

# イベント
$map_imgs{I} = '■';
sub event_I { $npc_com .= "なんと！壁ではなく隠し通路になっていた！"; }
sub event_2 { return if $event =~ /2/; $event .= '2'; &_add_treasure; }

# 敵と宝の設定
my $_s = int(rand(2));
require "$stagedir/$_s.cgi";



1; # 削除不可
