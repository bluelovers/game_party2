#=================================================
# 手助けクエスト Created by Merino
#=================================================
# 場所名
$this_title = '手助けクエスト';

# NPC名
$npc_name = '@ﾘｯｶ';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/helper";

# 背景画像
$bgimg = "$bgimgdir/helper.gif";

# 期限(日) この期間を超えても誰も達成しなかった場合はクエストを変更
$limit_day = 6;

# お題　 武器、防具、道具が必要 モンスターが必要　個別強さ別、ギルド専用 ギルド加入者なら GP up お題クリア→新お題作成→先着クリア

# イベントクリアに必要なアイテムNo
@clear_items = (
	[1..27], # 武器No
	[1..27], # 防具No
	[1..27,30..43,60..65,72..103,108], # 道具No
	['004'..'120',198..260], # 魔物No
	['001'..'003'], # ↑の魔物が欠番だったときの魔物No
);
# 報酬(道具No)
@pays = (128,128,128,130..134,134);


# レアクエイベントクリアに必要なアイテムNo
@rare_items = (
	[28..40], # 武器No
	[28..40], # 防具No
	[28,29,40,58..59,66..71,104..107,109], # 道具No
	[500..579], # 魔物No
	[160..165], # ↑の魔物が欠番だったときの魔物No
);
# レアクエ報酬(道具No)
@rare_pays = (129,129,129,135..137);


#=================================================
# はなす言葉
#=================================================
@words = (
	"ここは困っている人達を助ける何でも屋よ",
	"アイテムやモンスターを依頼主の代わりに探してきてほしいの",
	"報酬は錬金に必要となる素材など、他では手に入らないアイテムよ",
	"たまにレアクエストといって、条件を満たすのが難しい依頼がくるの。でも、その時の報酬は他では手に入れることができないものよ",
	"誰も解決することができない依頼はしばらくすると違う依頼に変わるわ",
);


#=================================================
# 追加アクション
#=================================================
push @actions, ('みる', 'かいけつ');
$actions{'みる'}     = sub{ &miru }; 
$actions{'かいけつ'} = sub{ &kaiketsu }; 


#=================================================
# ＠みる # 1,2,3:倉庫を検索 4:牧場を検索
#=================================================
sub miru {
	my $target = shift;

	my $p = qq|<table class="table1"><tr><th>依頼名</th><th>クリア条件</th><th>報酬</th><th>期限</th></tr>|;

	open my $fh, "< $logdir/helper_quest.cgi" or &error("$logdir/helper_quest.cgiファイルが開けません");
	while (my $line = <$fh>) {
		my($limit_time,$limit_date,$name,$is_guild,$pay,$kind,$no,$need_c) = split /<>/, $line;
		my $detail = $kind eq '1' ? "$weas[$no][1] <b>$need_c</b> 本"
				   : $kind eq '2' ? "$arms[$no][1] <b>$need_c</b> 着"
				   : $kind eq '3' ? "$ites[$no][1] <b>$need_c</b> 個"
				   :             qq|<img src="$icondir/mon/$no.gif" /> <b>$need_c</b> 匹|;
		my $g_mark = $is_guild ? qq|<img src="$icondir/etc/mark_guild.gif" alt="ギルド専用" />| : '';
		$p .= qq|<tr><td>『$name』</td><td>【$g_mark $detail】</td><td>★$ites[$pay][1]</td><td>〆$limit_dateまで</td></tr>|;
	}
	close $fh;

	$mes = qq|手助けクエスト一覧<br />$p</table>|;
	$act_time = 0;
}

#=================================================
# ＠かいけつ # 1,2,3:倉庫を検索 4:牧場を検索
#=================================================
sub kaiketsu {
	my $target = shift;

	my $p = qq|<table class="table1"><tr><th>依頼名</th><th>クリア条件</th><th>報酬</th><th>期限</th></tr>|;

	my @lines = ();
	open my $fh, "+< $logdir/helper_quest.cgi" or &error("$logdir/helper_quest.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($limit_time,$limit_date,$name,$is_guild,$pay,$kind,$no,$need_c) = split /<>/, $line;
	
		my $detail = $kind eq '1' ? "$weas[$no][1] <b>$need_c</b> 本"
				   : $kind eq '2' ? "$arms[$no][1] <b>$need_c</b> 着"
				   : $kind eq '3' ? "$ites[$no][1] <b>$need_c</b> 個"
				   :             qq|<img src="$icondir/mon/$no.gif" /> <b>$need_c</b> 匹|;

		if ($name eq $target) {
			if ($is_guild && $m{guild} eq '') {
				$mes = "$nameはギルド専用のクエストよ。ギルドに加入していないと依頼を受けることができないわ";
				return;
			}
			my $is_clear = $kind eq '4' ? &check_farm($no,$need_c) : &check_depot($kind, $no, $need_c);
			if ($is_clear) {
				&send_item($m, 3, $pay);
				$npc_com .= "<br />" if $npc_com;
				$npc_com .= " $detail たしかに受け取りました。こちらが報酬の $ites[$pay][1] になります！$mさんの預り所に送っておきますね！";
				$line = &create_helper_line();
				
				&regist_guild_data('point', 100) if $is_guild && $m{guild};
				++$m{help_c};
			}
			else {
				$mes = "$detail の条件を満たしてないようです";
				return;
			}
		}
		elsif ($time > $limit_time) {
			$line = &create_helper_line();
			$npc_com .= "<br />" if $npc_com;
			$npc_com .= "『$name』は誰も解決できそうにないので、新しい依頼がきました！";
		}

		$p .= qq|<tr onclick="text_set('＠かいけつ>$name ')"><td>『$name』</td><td>【$detail】</td><td>★$ites[$pay][1]</td><td>〆$limit_dateまで</td></tr>|;
		push @lines, $line;
	}
	if ($npc_com) {
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
		close $fh;
		return;
	}
	close $fh;

	$p  .= qq|</table>|;
	$mes = qq|手助けクエスト一覧<br />$p|;
	$act_time = 0;
}

#=================================================
# クエスト作成
#=================================================
sub create_helper_line {
	# タイプ[1:武器,2:防具,3:道具,4:魔物]
	my $kind = int(rand(4)+1);

	my $no = 0;
	my $pay;
	if (rand(14) < 1) { # 1/14の確率でレアクエ
		my @items = @{ $rare_items[$kind-1] };
		$no  = $items[int rand @items];
		$pay = $rare_pays[int rand @rare_pays];

		# モンスターNoが欠番だった場合
		if ($kind eq '4' && !-f "$icondir/mon/$no.gif") {
			@items = @{ $rare_items[$kind] };
			$no = $items[int rand @items];
		}
	}
	else { # 通常クエスト
		my @items = @{ $clear_items[$kind-1] };
		$no  = $items[int rand @items];
		$pay = $pays[int rand @pays];

		# モンスターNoが欠番だった場合
		if ($kind eq '4' && !-f "$icondir/mon/$no.gif") {
			@items = @{ $clear_items[$kind] };
			$no = $items[int rand @items];
		}
	}

	# 必要個数 $kind eq '4':魔物集め
	my $need_c = $kind eq '4' ? int(rand(2)+1) : int(rand(3)+2);

	# 1/15の確率でギルド専用
	my $is_guild = 0;
	if (rand(15) < 1) {
		$is_guild = 1;
		$need_c *= 2; # 必要数２倍
		$pay = 126; # 幸福袋
	}

	# クエスト名(被らないようにint(rand(999)) )
	my @names = $kind eq '1' ? ('店を始めたいので','強くなりたくて','戦い用に','ライバルに勝ちたくて','見てみたい','趣味で','家宝にしたい','探しています') # 武器
			  : $kind eq '2' ? ('コンプリートのために','カッコ良くなりたい','オシャレになりたくて','あこがれの服','プレゼント用に','着てみたい','集めたい','流行なので') # 防具
			  : $kind eq '3' ? ('コレクション用','病気を治すために','非常用に','必要なんです','大好物なので','気になるので','自分用に欲しい','用途は秘密です') # 道具
			  :                ('かわいいので','ペットほしい','仲良くなりたい','プニプニしたい','いやされたい','触ってみたい','背中に乗ってみたい','幸せになるために','王国を作るために'); # 魔物
	my $name = $names[int(rand(@names))] . 'その' . int(rand(999)+1);

	# 期限
	my $limit_time = $time + $limit_day * 24 * 60 * 60;
	my($min,$hour,$mday,$mon,$year) = (localtime($limit_time))[1..4];
	my $limit_date = sprintf("%d/%d %02d:%02d", $mon+1,$mday,$hour,$min);

	return "$limit_time<>$limit_date<>$name<>$is_guild<>$pay<>$kind<>$no<>$need_c<>\n";
}

#=================================================
# 倉庫チェック。条件クリアなら該当のアイテムを減らす
#=================================================
sub check_depot {
	my($p_kind, $p_no, $need_c) = @_;

	my $c = 0;
	my @lines = ();
	open my $fh, "+< $userdir/$id/depot.cgi" or &error("$userdir/$id/depot.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($kind, $no) = split /<>/, $line;
		
		# 該当→カウント(ストックしない)、非該当→ストック
		$kind eq $p_kind && $no eq $p_no && $c < $need_c ? ++$c : push @lines, $line;
	}
	if ($c >= $need_c) { # 条件数をクリアしてたら上書き
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
# 牧場チェック。条件クリアなら該当の魔物を減らす
#=================================================
sub check_farm {
	my($p_no, $need_c) = @_;
	
	my $c = 0;
	my @lines = ();
	open my $fh, "+< $userdir/$id/monster.cgi" or &error("$userdir/$id/monster.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($name, $icon) = split /<>/, $line;
		
		$icon eq "mon/$p_no.gif" && $c < $need_c ? ++$c : push @lines, $line;
	}
	if ($c >= $need_c) {
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
		close $fh;
		return 1;
	}
	close $fh;
	
	return 0;
}


1; # 削除不可
