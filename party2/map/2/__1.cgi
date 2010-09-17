# ダンジョン名
$d_name = "$dungeons[$stage]３階";

# 最大ターン
$max_round = 50;

# マップ
@maps = (
	[1,F,1],
	[0,B,0],
	[Q,T,Q],
	[0,0,0],
	[0,0,0],
);

# イベント
$map_imgs{Q} = '　';
$map_imgs{T} = '　';
$map_imgs{B} = '◎' if $event !~ /B/;;
$map_imgs{F} = '凸';
sub event_Q {}
sub event_F { my $v = int(rand(3)+1); $map="___$v"; $npc_com.="$p_nameは次の階へと進んだ…"; }
sub event_T { $map = '_'.int(rand(4)+1); $npc_com.= "<b>！！！！？</b>落とし穴だ！$leaderたちは穴に落ちてしまった！"; &_trap_d(70); }


# 敵と宝の設定
my $_s = int(rand(3)+4);
require "$stagedir/$_s.cgi";




1; # 削除不可
