#=================================================
# 名前変更 Created by Merino
#=================================================
# 場所名
$this_title = '命名の館';

# NPC名
$npc_name   = '@ﾏﾘﾅﾝ';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/name_change";

# 背景画像
$bgimg   = "$bgimgdir/name_change.gif";

# 名前の変更にかかるお金
$need_money_name = 300000;

# 性別の変更にかかるお金
$need_money_sex  = 10000;


#=================================================
# はなす言葉
#=================================================
@words = (
	"ここは$this_titleじゃ。ここではお主の名前やパスワード、性別を変えることができのじゃ",
	"名前を変えるということは運命を変えるということじゃ。とても大きなことなのじゃ",
	"命名神の怒りに触れる名前にすると、存在が消されるらしいから気をつけることじゃ",
	"料金は以下の通りとなっておる。<br />名前変更 $need_money_name G<br />パスワード変更 無料<br />性別変更$need_money_sex G",
	"ギルドに参加している場合は、名前を変更することができんぞ",
);


#=================================================
# 追加アクション
#=================================================
push @actions, 'なまえ';
push @actions, 'ぱすわーど';
push @actions, 'せいてんかん';
$actions{'なまえ'} = sub{ &namae }; 
$actions{'ぱすわーど'} = sub{ &pasuwado }; 
$actions{'せいてんかん'} = sub{ &seitenkan }; 

#=================================================
# ＠せいてんかん
#=================================================
sub seitenkan {
	my $target = shift;
	
	if ($target eq '男') {
		if ($m{sex} eq 'm') {
			$mes = "$npc_name「すでに$mは男じゃぞ」";
		}
		elsif ($m{money} < $need_money_sex) {
			$mes = "$npc_name「男に性転換するためのお金が足りぬぞ」";
		}
		elsif (!-f "$icondir/job/$m{job}_m.gif") {
			$mes = "$npc_name「職業が $jobs[$m{job}][1] は性転換することはできぬぞ」";
		}
		else {
			$m{sex}    = "m";
			$m{icon}   = "job/$m{job}_m.gif";
			$m{money} -= $need_money_sex;
			$npc_com   = "女をやめて男として生きていくのだな。それでは…カッ！！<br />$mは今から男としての人生の始まりじゃ";
			&write_memory("女をやめて男として生まれ変わる");
		}
	}
	elsif ($target eq '女') {
		if ($m{sex} eq 'f') {
			$mes = "$npc_name「すでに$mは女じゃぞ」";
		}
		elsif ($m{money} < $need_money_sex) {
			$mes = "$npc_name「女に性転換するためのお金が足りぬぞ」";
		}
		elsif (!-f "$icondir/job/$m{job}_f.gif") {
			$mes = "$npc_name「職業が $jobs[$m{job}][1] は性転換することはできぬぞ」";
		}
		else {
			$m{sex}    = "f";
			$m{icon}   = "job/$m{job}_f.gif";
			$m{money} -= $need_money_sex;
			$npc_com   = "男をやめて女として生きていくのだな。それでは…カッ！！<br />$mは今から女としての人生の始まりじゃ";
			&write_memory("男をやめて女として生まれ変わる");
		}
	}
	else {
		$mes = $m{sex} eq 'm'
			? qq|<span onclick="text_set('＠せいてんかん>女')">＠せいてんかん>女<br />女に性転換するには $need_money_sex G必要じゃ</span>|
			: qq|<span onclick="text_set('＠せいてんかん>男')">＠せいてんかん>男<br />男に性転換するには $need_money_sex G必要じゃ</span>|
			;
	}
}

#=================================================
# ＠なまえ
#=================================================
sub namae {
	my $y = shift;
	
	unless ($y) {
		$mes = qq|<span onclick="text_set('＠なまえ>')">名前の変更には $need_money_name G必要じゃ<br />『＠なまえ>○○○』 ○○○に新しい名前を記入するのだ</span>|;
		return;
	}
	if ($m{money} < $need_money_name) {
		$mes = qq|名前の変更には $need_money_name G必要じゃ|;
		return;
	}
	elsif ($m{guild}) {
		$mes = qq|名前を変更するには、一度ギルドを脱退する必要があるぞ|;
		return;
	}

	my $new_id = unpack 'H*', $y;
	$mes = "プレイヤー名に不正な文字( ,;\"\'&<>\\\/@ )が含まれています"	if $y =~ /[,;\"\'&<>\\\/@]/;
	$mes = "プレイヤー名に不正な文字( ＠ )が含まれています"				if $y =~ /＠/;
	$mes = "プレイヤー名に不正な空白が含まれています"					if $y =~ /　|\s/;
	$mes = "プレイヤー名は全角４(半角８)文字以内です"					if length($y) > 8;
	$mes = "プレイヤー名とパスワードが同一文字列です"					if $y eq $pass;
	$mes = "すでに同じ名前のプレイヤーが存在します"						if -f "$userdir/$new_id";
	return if $mes;
	
	rename "$userdir/$id", "$userdir/$new_id" or &error("名前の変更に失敗しました");
	
	$com .= "$mは $need_money_name Gをささげました";
	$npc_com = "今から $m は $y と名乗るがよい<br />ログインするときのプレイヤー名も変わったから注意するんじゃぞ！<br />念のため、一度ログアウトしてログインしたほうがよいぞ";
	$id = $new_id;
	$m{name} = $y;
	$m{money} -= $need_money_name;
	
	&write_memory("<b>$y</b> に名前を変更する");
	&write_news("$mが <b>$y</b> と名前を変更する");
	&leave_member($m);
}

#=================================================
# ＠ぱすわーど
#=================================================
sub pasuwado {
	my $y = shift;
	unless ($y) {
		$mes = qq|<span onclick="text_set('＠ぱすわーど>')">『＠ぱすわーど>○○○』 ○○○に新しいパスワードを記入するのだ|;
		return;
	}

	$mes = "パスワードは半角英数字で入力して下さい"		if $y =~ m/[^0-9a-zA-Z]/;
	$mes = "パスワードは半角英数字４～12文字です"		if length $y < 4 || length $y > 12;
	$mes = "プレイヤー名とパスワードが同一文字列です"	if $y eq $m;
	return if $mes;
	
	$npc_com = "ログインするときのパスワードを新しいものに変更したぞ<br />念のため、一度ログアウトしてログインしたほうがよいぞ";
	$to_name = $m;
	$pass = $m{pass} = $y;
}


1; # 削除不可
