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
@c_randoms = (qw/ｱｲﾝ ﾍﾟｹ ﾎﾟｺ ﾎﾞﾌﾞ ｹｲﾝ ﾃｺﾃｺ ﾒｿ ｳﾙﾌ ｷﾞｬﾝｸﾞ ﾊﾞｰｲ ﾄｰｲ ｼｪﾘｰ ｲｱﾝ ｴﾄﾞｶﾞｰ ｴﾘｰ ﾄﾆｰ ﾋﾞﾘｰ ﾍﾞﾘｰ ﾎﾟｰﾙ ｴﾘｽ ｶｲﾝ ｹｲﾄ ｹﾘｰ ﾒﾘｰ ﾓﾘｽ ﾏﾘｽ ﾐﾘｰ ﾑｰｽ ﾓｰｽ ﾒｲ ﾒﾃﾞｨ ﾅｯﾊﾟ ﾊﾟｲﾝ ｽｰｽｰ ｸｩｸｩ ﾋﾞｰﾄﾙ ｱﾘｽ ｱｲｽ ｼｰｻﾞｰ ｶｯｺｴ ﾃﾞﾌｫ ｱｰｻｰ ﾖｳｽｹ ﾋﾟｯﾋﾟ ﾄﾛｰﾝ ﾄﾞﾛｰ ﾂｷﾞ ｻｷﾞ ﾄﾝﾇﾗ ﾎﾟﾎﾟﾛ ｸﾘｰﾑ ｸﾘｭｰ ｲｾｱ ﾈﾈｺ ﾄﾝﾄｺ ｹﾞﾚｹﾞﾚ ﾎﾞﾛﾝｺﾞ ﾁﾛﾙ ﾌﾟｯｸﾙ ﾄﾞﾝ ｼﾞｪｲ ｼﾞｬｯｸ ｼﾞｮﾝ ｼﾞｮﾆｰ ｼﾞｪｲ/);
@c_imgs    = (1..35);

# 名前と画像固定(置物系)
@c_fixeds  = (
	['ｽｰﾌﾟ',		'item/010.gif'],
	['ｺﾝｽｰﾌﾟ',		'item/010.gif'],
	['ｶﾎﾞﾁｬｽｰﾌﾟ',	'item/010.gif'],
	['ﾊｰﾌﾞﾃｨｰ',		'item/011.gif'],
	['ﾊﾝﾊﾞｰｸﾞ',		'item/020.gif'],
	['ﾊﾞﾝﾊﾞｰｸﾞ',	'item/020.gif'],
	['肉',			'item/020.gif'],
	['ｶﾚｰﾗｲｽ',		'item/023.gif'],
	['ｶﾘｰﾗｲｽ',		'item/023.gif'],
	['ﾗｲｽｶﾚｰ',		'item/023.gif'],
	['ｵﾑﾗｲｽ',		'item/021.gif'],
	['ｹﾁｬｯﾌﾟﾗｲｽ',	'item/021.gif'],
	['ｽﾊﾟｹﾞﾃｨ',		'item/022.gif'],
	['ｺﾞﾁｿｳ',		'item/021.gif'],
	['ﾚﾓﾝｽｶｯｼｭ',	'item/016.gif'],
	['ﾊﾁﾐﾂｼﾞｭｰｽ',	'item/016.gif'],
	['ｴﾙﾌの飲み薬',	'item/016.gif'],
	['ｱﾓｰﾙの水',	'item/015.gif'],
	['清酒',		'item/015.gif'],
	['祝酒',		'item/015.gif'],
	['ｸﾏﾁｬﾝ',		'chr/023.gif'],
	['ｸﾏﾀﾛｳ',		'chr/023.gif'],
	['ｸﾏｼﾞﾛｳ',		'chr/023.gif'],
	['ｸﾏｯｸｽ',		'chr/023.gif'],
	['ｸﾏﾁｬﾝ',		'chr/023.gif'],
	['ｶｴﾙ',			'chr/022.gif'],
	['ｹﾛｹﾛ',		'chr/022.gif'],
	['ｹﾛﾁｬ',		'chr/022.gif'],
	['ｹﾛｽｹ',		'chr/022.gif'],
	['ﾒｪﾒｪ',		'chr/019.gif'],
	['ﾋﾂｼﾞ',		'chr/019.gif'],
	['ｼｰﾌﾟ',		'chr/019.gif'],
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
