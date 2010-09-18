# ダンジョン名
$d_name = "$dungeons[$stage]１階";

# 最大ターン
$max_round = 30;

# マップ
@maps = (
	[F,7,0],
	[1,1,0],
	[0,0,0],
	[0,1,1],
	[0,0,S],
);

# イベント
$map_imgs{F} = '凸';
sub event_F { my $v = int(rand(3)+1); $map="_$v"; $npc_com.="$p_nameは次の階へと進んだ…"; }
sub event_7 { return if $event =~ /7/; $event .= '7'; require "$stagedir/3.cgi"; $npc_com.="ただならぬ気配を感じる…。どうやら、このフロアのボスのようだ！<br />"; &add_boss } # ボス

# 敵と宝の設定
my $_s = int(rand(3)+2);
require "$stagedir/$_s.cgi";



1; # 削除不可
