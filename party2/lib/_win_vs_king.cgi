#=================================================
# 祝賀会データ Created by Merino
#=================================================
# 祝賀会の開催時間(時間)
$c_hour = 2;

# 封印戦１勝利につき何人集まる
$c_people = 2 + int(rand(4));

# 封印戦１勝利につき置物
$c_mono   = 1 + int(rand(2));

# 色
@c_colors = (qw/#FF33FF #FF3333 #33CCFF #FFCCCC #FF33CC #FF9933 #FFFF33 #33FF33 #33CCFF #6666FF #CC66FF #CCCCFF #FFFFFF #33FF99/);

# 名前と画像ランダム(人物系)
@c_randoms = (qw/アイン ペケ ポコ ボブ ケイン テコテコ メソ ウルフ ギャング バーイ トーイ シェリー イアン エドガー エリー トニー ビリー ベリー ポール エリス カイン ケイト ケリー メリー モリス マリス ミリー ムース モース メイ メディ ナッパ パイン スースー クゥクゥ ビートル アリス アイス シーザー カッコエ デフォ アーサー ヨウスケ ピッピ トローン ドロー ツギ サギ トンヌラ ポポロ クリーム クリュー イセア ネネコ トントコ ゲレゲレ ボロンゴ チロル プックル ドン ジェイ ジャック ジョン ジョニー ジェイ/);
@c_imgs    = (1..38);

# 名前と画像固定(置物系)
@c_fixeds  = (
	['スープ',		'item/010.gif'],
	['コンスープ',		'item/010.gif'],
	['カボチャスープ',	'item/010.gif'],
	['ハーブティー',		'item/011.gif'],
	['ハンバーグ',		'item/020.gif'],
	['バンバーグ',	'item/020.gif'],
	['肉',			'item/020.gif'],
	['カレーライス',		'item/023.gif'],
	['カリーライス',		'item/023.gif'],
	['ライスカレー',		'item/023.gif'],
	['オムライス',		'item/021.gif'],
	['ケチャップライス',	'item/021.gif'],
	['スパゲティ',		'item/022.gif'],
	['ゴチソウ',		'item/021.gif'],
	['レモンスカッシュ',	'item/016.gif'],
	['ハチミツジュース',	'item/016.gif'],
	['エルフの飲み薬',	'item/016.gif'],
	['アモールの水',	'item/015.gif'],
	['清酒',		'item/015.gif'],
	['祝酒',		'item/015.gif'],
	['クマチャン',		'chr/023.gif'],
	['クマタロウ',		'chr/023.gif'],
	['クマジロウ',		'chr/023.gif'],
	['クマックス',		'chr/023.gif'],
	['クマチャン',		'chr/023.gif'],
	['カエル',			'chr/022.gif'],
	['ケロケロ',		'chr/022.gif'],
	['ケロチャ',		'chr/022.gif'],
	['ケロスケ',		'chr/022.gif'],
	['メェメェ',		'chr/019.gif'],
	['ヒツジ',		'chr/019.gif'],
	['シープ',		'chr/019.gif'],
);

$c_hour--;
open my $fh, ">> $logdir/event_member.cgi" or &error("$logdir/event_member.cgiファイルが開けません");
for my $i (1..$c_people) {
	my $ran_time = $time + $c_hour * 3600 + int(rand(3600)); # rand(3600): 人がいなくなるのに時差をつける
	my $c_random = $c_randoms[int rand @c_randoms ];
	my $c_img    = sprintf("chr/%03d.gif", $c_imgs[int rand @c_imgs]);
	my $c_color  = $c_colors[ int rand @c_colors  ];
	print $fh "$ran_time<>0<>$c_random<>0<>$c_img<>$c_color<>\n";
}
for my $i (1..$c_mono) {
	my $ran_time = $time + $c_hour * 3600 + int(rand(3600)); # rand(3600): 人がいなくなるのに時差をつける
	my $j = int(rand(@c_fixeds));
	my $c_color  = $c_colors[ int rand @c_colors  ];
	print $fh "$ran_time<>0<>$c_fixeds[$j][0]<>0<>$c_fixeds[$j][1]<>$c_color<>\n",
}
close $fh;



1; # 削除不可
