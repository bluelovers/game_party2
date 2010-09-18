#=================================================
# 錬金術 Created by Merino
#=================================================
# 場所名
$this_title = '錬金場';

# NPC名
$npc_name = '@トロデ';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/alchemy";

# 背景画像
$bgimg = "$bgimgdir/alchemy.gif";



# 完成フラグがあったら完成処理へ
&finish() if $m{recipe} =~ /^1/;


#=================================================
# はなす言葉
#=================================================
@words = (
	"２つのアイテムを錬金することで新たなアイテムを作ることができるぞい",
	"錬金レシピを使うことで錬金することが可能\になるぞい",
	"錬金したアイテムの完成は、お主が寝て起きた次の日には完成しているじゃろう",
	"錬金で作ることでしか手に入らない武器や防具があるそうじゃ・・・",
	"錬金レシピは習得済み以外のものを習得することができるぞい",
);

#=================================================
# ＠しらべる>NPC
#=================================================
sub shiraberu_npc {
	$mes = qq|$npc_name「いやん。どこをさわっとるんじゃっ！」|;
}

#=================================================
# 追加アクション
#=================================================
push @actions, 'れしぴ';
push @actions, 'れんきん';
$actions{'れしぴ'}   = sub{ &reshipi }; 
$actions{'れんきん'} = sub{ &renkin }; 

#=================================================
# ＠れしぴ
#=================================================
sub reshipi {
	# レシピ一覧読み込み
	require './lib/_alchemy_recipe.cgi';
	my $all_c = map { keys %{ $recipes{$_} } } keys %recipes;

	my $c = 0;
	my $comp_c = 0;
	my $p = qq|<table><tr><td><table class="table1">|;
	open my $fh, "< $userdir/$id/recipe.cgi" or &errror("$userdir/$id/recipe.cgiファイルが読み込めません");
	while (my $line = <$fh>) {
		my($is_make, $base, $sozai, $mix) = split /<>/, $line;
		
		if ($is_make) {
			++$comp_c;
		}
		else {
			$mix = '？？？';
		}
		$p .= qq|<tr onclick="text_set('＠れんきん>$base＠そざい>$sozai ')"><td>$base</td><td>×$sozai</td><td>＝$mix</td></tr>|;
		$p .= qq|</td></tr></table></td><td><table class="table1"><tr><td>| if ++$c % 40 == 0;
	}
	close $fh;

	my $comp_par = int($comp_c / $all_c * 100);
	if ($comp_par >= 100) {
		unless (-f "$userdir/$id/comp_alc_flag.cgi") {
			open my $fh2, "> $userdir/$id/comp_alc_flag.cgi" or &error("$userdir/$id/comp_alc_flag.cgiファイルが開けません");
			close $fh2;
			
			&write_legend('comp_alc');
			&write_memory(qq|<span class="comp">Alchemy Complete!!</span>|);
			&write_news(qq|<span class="comp">$mが錬金レシピをコンプリートする！</span>|);
			$npc_com .= qq|<span class="comp">$mは <b>錬金レシピ</b> をコンプリートしました！</span>のじゃ|;
		}
		
		$comp_par = 100;
	}

	$mes = qq|$mの錬金レシピ　コンプリート率《<b>$comp_par</b>％》<br />$p</td></tr></table></td></tr></table>|;
	$act_time = 0;
}


#=================================================
# ＠れんきん
#=================================================
sub renkin {
	my $target = shift;
	my($base_t, $sozai_t) = split /＠そざい&gt;/, $target;

	if ($m{recipe}) {
		$mes = "完成するまでしばし待たれよ";
		return;
	}

	my $c = 0;
	my $p = qq|<table><tr><td><table class="table1">|;
	open my $fh, "< $userdir/$id/recipe.cgi" or &error("$userdir/$id/recipe.cgiファイルが読み込めません");
	while (my $line = <$fh>) {
		my($is_make, $base, $sozai, $mix) = split /<>/, $line;
		
		if ($base_t eq $base && $sozai_t eq $sozai) {
			my $is_clear = &check_depot($base, $sozai);

			if ($is_clear) {
				$m{recipe} = "0,${is_make},${base},${sozai},${mix}";
				$npc_com = $is_make
					? "$base と $sozai じゃな！ふむ、この組み合わせなら $mix ができるぞ！完成する頃にまた来るがよい"
					: "$base と $sozai じゃな！おお、錬金可能\なようじゃ！何が出来るか楽しみじゃな！一晩たてば完成するじゃろう。完成する頃にまた来るがよい";
			}
			else {
				$npc_com = "残念ながら $base と $sozai の材料が預り所にないようじゃ";
			}
			last;
		}
		else {
			$mix = '？？？' unless $is_make;
			$p .= qq|<tr onclick="text_set('＠れんきん>$base＠そざい>$sozai ')"><td>$base</td><td>×$sozai</td><td>＝$mix</td></tr>|;
		}
		$p .= qq|</td></tr></table></td><td><table class="table1"><tr><td>| if ++$c % 40 == 0;
	}
	close $fh;
	
	$npc_com = "錬金レシピで習得したものしか錬金することはできんぞ" if !$npc_com && $base_t && $sozai_t;
	return if $npc_com;
	$mes = qq|$mの錬金レシピ<br />$p</td></tr></table></td></tr></table>|;
	$act_time = 0;
}
#-------------------
# 倉庫チェック。条件クリアなら該当のアイテムを減らす
sub check_depot {
	my($base, $sozai) = @_;

	my $has_base = 0;
	my $has_sozai = 0;
	my @lines = ();
	open my $fh, "+< $userdir/$id/depot.cgi" or &error("$userdir/$id/depot.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($kind, $no) = split /<>/, $line;
		my $name = $kind eq '1' ? $weas[$no][1]
				 : $kind eq '2' ? $arms[$no][1]
				 :                $ites[$no][1];
		if    (!$has_base  && $name eq $base)  { $has_base  = 1 }
		elsif (!$has_sozai && $name eq $sozai) { $has_sozai = 1 }
		else                                   { push @lines, $line }
	}
	if ($has_base && $has_sozai) { # 条件数をクリアしてたら上書き
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
		close $fh;

		return 1;
	}
	close $fh;

	return 0;
}

#=================================================
# 完成
#=================================================
sub finish {
	my($is_finish, $is_make, $base, $sozai, $mix) = split /,/, $m{recipe};
	$com = "＠れんきんでかんせいしたものをうけとる";
	$npc_com = "まっておったぞ！$baseと$sozaiを錬金した <b>$mix</b> が完成したぞい！出来上がったアイテムは預かり所の方に送っておいたぞい！";
	$m{recipe} = '';
	++$m{alc_c};

	my($kind, $no) = &get_item_no($mix);
	if ($kind eq '0') { # 未設定の存在しないアイテム名だった場合(config.cgiに追加し忘れ)
		$npc_com .= qq|<b style="color: #F00">$mix というアイテムが設定されておらんようじゃ…。ここの管理者に伝えるんじゃ！</b>|;
	}
	else {
		&send_item($m, $kind, $no);
	}
	
	# 未作成ならレシピに作成したフラグをたてる
	&finished_recipe($base, $sozai, $mix) unless $is_make;
}
#-------------------
# アイテム名からアイテム種類とNoを取得
sub get_item_no {
	my $name = shift;
	for my $i (1..$#weas) { return 1, $i if $weas[$i][1] eq $name; }
	for my $i (1..$#arms) { return 2, $i if $arms[$i][1] eq $name; }
	for my $i (1..$#ites) { return 3, $i if $ites[$i][1] eq $name; }
	return 0;
}
#-------------------
# レシピに作成したフラグをたてる
sub finished_recipe {
	my($new_base, $new_sozai, $new_mix) = @_;

	my @lines = ();
	open my $fh, "+< $userdir/$id/recipe.cgi" or &errror("$userdir/$id/recipe.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($is_make, $base, $sozai, $mix) = split /<>/, $line;
		
		if ($new_base eq $base && $new_sozai eq $sozai && $new_mix eq $mix) {
			$line = "1<>$base<>$sozai<>$mix<>\n";
		}
		push @lines, $line;
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}




1; # 削除不可
