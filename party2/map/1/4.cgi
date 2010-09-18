# 最大ターン
$max_round = 50;

# マップ
@maps = (
	[3,1,0,0,0,0,0,I,3],
	[I,1,0,1,D,1,0,1,1],
	[0,0,0,1,B,1,0,0,0],
	[0,1,1,1,2,1,1,1,0],
	[0,0,0,1,1,1,0,0,0],
	[0,1,0,0,S,0,0,1,1],
	[0,1,0,1,0,1,1,1,K],
	[0,1,0,1,0,0,0,1,0],
	[K,1,0,0,0,1,0,0,0],
);

# イベント
sub event_2 { return if $event =~ /2/; $event .= '2'; &_add_treasure; }
sub event_3 { return if $event =~ /3/; $event .= '3'; &_add_treasure; }
$map_imgs{I} = '■';
$map_imgs{K} = '★' if $event !~ /K/;
$map_imgs{D} = '扉' if $event !~ /D/;
sub event_I { $npc_com .= "なんと！壁ではなく隠し通路になっていた！"; }
sub event_K { return if $event =~ /K/; $event .= 'K'; $npc_com.="扉の鍵を拾った！";  }
sub event_D {
	return if $event =~ /D/;
	if ($m{job} eq '9') {
		$com .= "<br />$m{mes}" if $m{mes};
		$npc_com .= "$mは細いナイフと針金のようなもので、扉のカギ穴をガチャガチャした！…ガチャンッ！なんと、扉が開いたようだ！";
		$event .= 'D';
	}
	elsif ($event =~ /K/) {
		$npc_com .= "$mは拾ったカギをトビラ扉に差し込んでみた！…ゴゴゴゴゴ…重い音をたてて扉が開いていく！";
		$event .= 'D';
	}
	else {
		$npc_com .= "$mは扉を押したり引いたりしてみたが、ビクともしない…";
		--$py;
	}
}

require "$stagedir/2.cgi";



1; # 削除不可
