# 最大ターン
$max_round = 70;

# マップ
@maps = (
	[S,M,0,0,0,0,1,4,3,2,B],
	[1,1,0,1,1,0,1,1,1,1,b],
	[0,0,0,1,0,0,1,0,H,1,0],
	[0,1,1,1,0,1,1,0,1,1,0],
	[0,0,0,1,0,H,1,0,0,0,0],
	[1,1,0,1,1,1,1,1,1,1,0],
	[0,0,0,0,0,0,0,0,1,0,0],
	[0,1,1,0,1,1,1,H,1,0,1],
	[0,1,1,1,1,0,1,1,1,0,1],
	[0,0,0,0,0,0,0,0,0,0,0],
);

# イベント
$map_imgs{B} = '◎' if $event !~ /B/;
$map_imgs{b} = '◎' if $event !~ /b/;
$map_imgs{2} = '宝' if $event !~ /2/;
$map_imgs{3} = '宝' if $event !~ /3/;
$map_imgs{4} = '宝' if $event !~ /4/;
sub event_0 { $ms{$m}{hp}-=int($ms{$m}{mhp}*0.02+0.5); if ($ms{$m}{hp} <= 0) { $ms{$m}{hp}=0; $npc_com .= qq!<span class="die">$mは倒れた！</span>!; } } # 道
sub event_2 { return if $event =~ /2/; $event .= '2'; &_add_treasure; }
sub event_3 { return if $event =~ /3/; $event .= '3'; &_add_treasure; }
sub event_4 { return if $event =~ /4/; $event .= '4'; &_add_treasure; }
sub event_M { return if $event =~ /M/; $event .= 'M'; $npc_com.=qq|<br /><span class="strong">ココハ死ノ大迷路　生キテ帰ッタ者ハ　誰モイナイ…<br />　ワケデハナイ　敵ハ出ナイガ　１歩進ムゴトニ　命ガ削ラレテイクダロウ…</span>|; }
sub event_b { return if $event =~ /b/; $event .= 'b'; $npc_com.="ただならぬ気配を感じる…。どうやら、このダンジョンのボスのようだ！<br />"; &add_boss } # ボス
sub event_H { return if $event =~ /H/; $event .= 'H'; $npc_com.=qq|<br /><span class="strong">残念　無念　行キ止マリ<br />　シカシ　チョットダケサービス</span><br />|; rand(2)<1 ? &_heal(shift, 40, '無') : &_mp_h(shift, 40, '無'); }

# 敵と宝の設定
my $_s = int(rand(5)+4);
require "$stagedir/$_s.cgi";



1; # 削除不可
