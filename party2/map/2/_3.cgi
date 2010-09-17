# ダンジョン名
$d_name = "$dungeons[$stage]２階";

# 最大ターン
$max_round = 40;

# マップ
@maps = (
	[0,0,0],
	[1,1,0],
	[0,0,0],
	[0,1,T],
	[0,8,F],
);

# イベント
$map_imgs{F} = '凸';
sub event_F { $map="__1"; $npc_com.="$p_nameは次の階へと進んだ…"; }
sub event_2 { return if $event =~ /2/; $event .= '2'; &_add_treasure; }
sub event_8 { return if $event =~ /8/; $event .= '8'; require "$stagedir/4.cgi"; $npc_com.="ただならぬ気配を感じる…。どうやら、このフロアのボスのようだ！<br />"; &add_boss } # ボス
sub event_T { $map= int(rand(3)+1); $npc_com.= "<b>！！！！？</b>落とし穴だ！$leaderたちは穴に落ちてしまった！"; &_trap_d(30); }


# 敵と宝の設定
my $_s = int(rand(3)+3);
require "$stagedir/$_s.cgi";



1; # 削除不可
