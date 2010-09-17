# 最大ターン
$max_round = 60;

# マップ
@maps = (
	[4,1,0,0,0,1,0],
	[0,1,0,2,0,1,0],
	[0,1,0,0,0,1,0],
	[0,1,1,A,1,1,0],
	[0,0,0,0,0,0,0],
	[1,1,1,1,1,0,1],
	[0,3,0,1,0,0,0],
	[0,0,0,1,0,0,0],
	[0,B,0,1,0,C,0],
	[1,0,1,1,1,0,1],
	[0,0,0,S,0,0,0],
);


# イベント
$map_imgs{2} = '宝' if $event !~ /2/;
$map_imgs{3} = '宝' if $event !~ /3/;
$map_imgs{4} = '宝' if $event !~ /4/;
$map_imgs{A} = '◎' if $event !~ /A/;
$map_imgs{B} = '◎' if $event !~ /B/;
$map_imgs{C} = '◎' if $event !~ /C/;
sub event_0 { for my $y (@partys) { $ms{$y}{state} = '魔封' }; return if rand(2) > 1; &_add_monster; } # 道
sub event_2 { for my $y (@partys) { $ms{$y}{state} = '魔封' }; return if $event =~ /2/; $event .= '2'; &_add_treasure; }
sub event_3 { for my $y (@partys) { $ms{$y}{state} = '魔封' }; return if $event =~ /3/; $event .= '3'; &_add_treasure; }
sub event_4 { for my $y (@partys) { $ms{$y}{state} = '魔封' }; return if $event =~ /4/; $event .= '4'; &_add_treasure; }
sub event_A { for my $y (@partys) { $ms{$y}{state} = '魔封' }; return if $event =~ /A/; $event .= 'A'; $npc_com.="ただならぬ気配を感じる…。どうやら、このダンジョンのボスのようだ！<br />"; &add_boss } # ボス
sub event_B { for my $y (@partys) { $ms{$y}{state} = '魔封' }; return if $event =~ /B/; $event .= 'B'; my $_s = int(rand(5)+8); require "$stagedir/$_s.cgi"; &add_boss; } # ボス
sub event_C { for my $y (@partys) { $ms{$y}{state} = '魔封' }; return if $event =~ /C/; $event .= 'C'; my $_s = int(rand(5)+8); require "$stagedir/$_s.cgi"; &add_boss; } # ボス



# 敵と宝の設定
require "$mapdir/9/_data.cgi";


1; # 削除不可
