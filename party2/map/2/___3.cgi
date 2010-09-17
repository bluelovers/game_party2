# ダンジョン名
$d_name = "$dungeons[$stage]４階[宝物庫]";

# 最大ターン
$max_round = 50;

# マップ
@maps = (
	[1,0,1],
	[0,0,0],
	[0,T,0],
	[0,2,0],
	[3,0,4],
);

# イベント
$map_imgs{2} = '宝' if $event !~ /2/;
$map_imgs{3} = '宝' if $event !~ /3/;;
$map_imgs{4} = '宝' if $event !~ /4/;;
sub event_2 { return if $event =~ /2/; $event .= '2'; &_add_treasure; }
sub event_3 { return if $event =~ /3/; $event .= '3'; &_add_treasure; }
sub event_4 { return if $event =~ /4/; $event .= '4'; &_add_treasure; }
sub event_T { $map = '__1'; $npc_com.= "<b>！！！！？</b>落とし穴だ！$leaderたちは穴に落ちてしまった！"; &_trap_d(40); }


# 敵と宝の設定
my $_s = int(rand(4)+3);
require "$stagedir/$_s.cgi";




1; # 削除不可
