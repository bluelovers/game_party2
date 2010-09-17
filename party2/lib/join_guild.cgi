#=================================================
# ギルド設立 Created by Merino
#=================================================
# 場所名
$this_title = 'ギルド';

# NPC名
$npc_name   = '@支配人';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/join_guild";

# 背景画像
$bgimg   = "$bgimgdir/join_guild.gif";

# ギルド設立金
$make_money = 5000;

# デフォルトのギルドマークアイコン
$default_mark = "$icondir/mark/000.gif";

# ギルドマーク変更料金
$mark_money = 3000;

# 最大ギルド名文字数(半角)
$max_guild_name = 16;

# ギルド自動削除。この日数間「＠ぎるど」による出入りがない場合自動削除(日)
$auto_delete_guild_day = 20;

#=================================================
# はなす言葉
#=================================================
@words = (
	"$auto_delete_guild_day 日以上「＠ぎるど」による出入りがない場合は、自動的に削除となります",
	"ギルドとは、気が合うメンバーの集まりです",
	"ギルド名は、途中で変えることができませんので、じっくり考えてください",
	"ギルマスとは、ギルドマスターの略称です。そのギルド内で一番の権限があります",
	"ギルマスは、メンバーに役職名をあたえることができるのです",
	"ギルドマークや壁紙は、お金がかかりますが何度でも変えることが可能です",
	"ギルド参加者は、ギルド戦ができるようになります",
	"ギルドを新しく作るには、$make_money G必要です",
	"ギルドマークを変更するには、$mark_money G必要です",
	"ギルド戦で優勝すると勝利メダルがギルド内に飾られていきます",
);


#=================================================
# 追加アクション
#=================================================
push @actions, 'さんか';
push @actions, 'つくる';
push @actions, 'まーく';
push @actions, 'かべがみ';
#push @actions, 'かいめい'; # ここと↓の#$actions{'かいめい'}のコメントを外すとギルドを改名できる。
push @actions, 'だったい';
push @actions, 'かいさん';
$actions{'さんか'}   = sub{ &sanka }; 
$actions{'つくる'}   = sub{ &tsukuru }; 
$actions{'まーく'}   = sub{ &mark }; 
$actions{'かべがみ'} = sub{ &kabegami }; 
#$actions{'かいめい'} = sub{ &kaimei }; 
$actions{'だったい'} = sub{ &dattai }; 
$actions{'かいさん'} = sub{ &kaisan }; 


sub header_html { 
	print qq|<div class="mes">【$this_title】 $e2j{money} <b>$m{money}</b>G|;
	print qq| / ギルド【$m{guild}】| if $m{guild};
	print qq|</div>|;
}

#=================================================
# ＠かべがみ
#=================================================
sub kabegami {
	my $target = shift;
	
	if ($target) {
		unless ($m{guild}) {
			$mes = "ギルドに所属していません";
			return;
		}

		my $gid = unpack 'H*', $m{guild};
		unless (-d "$guilddir/$gid") {
			$mes = "$m{guild}ギルドが存在しません";
			$m{guild} = "";
			return;
		}
		unless (&is_guild_master($gid)) {
			$mes = "壁紙を変更できるのは、ギルドマスターだけです";
			return;
		}
		if (defined $kabes{$target} && $m{money} < $kabes{$target}) {
			$mes = "お金が足りません";
			return;
		}
	}
	
	my $count = 0;
	my $p = qq|<table><tr>|;
	for my $k (sort { $kabes{$a} <=> $kabes{$b} } keys %kabes) {
		my $base_name = $k;
		$base_name =~ s/(.+)\..+/$1/; # 見栄えが悪いので拡張子を除く
		if ($base_name eq $target) {
			&regist_guild_data('bgimg', $k, $m{guild});

			$npc_com   = qq|$m{guild}の壁紙を $base_name に変更しました|;
			$m{money} -= $kabes{$k};
			return;
		}
		$p .= qq|<td valign="bottom" align="right"><span onclick="text_set('＠かべがみ>$base_name ')"><img src="$bgimgdir/$k" title="$k" /><br />$kabes{$k} G</span></td>|;
		$p .= qq|</tr><tr>| if ++$count % 10 == 0;
	}
	$p .= qq|</tr></table>|;

	$mes = qq|どの壁紙にしますか？<br />$p|;
	$act_time = 0;
}


#=================================================
# ＠まーく
#=================================================
sub mark {
	my $target = shift;
	
	if ($target) {
		unless ($m{guild}) {
			$mes = "ギルドに所属していません";
			return;
		}

		my $gid = unpack 'H*', $m{guild};
		unless (-d "$guilddir/$gid") {
			$mes = "$m{guild}ギルドが存在しません";
			$m{guild} = "";
			return;
		}
		unless (&is_guild_master($gid)) {
			$mes = "ギルドマークを変更できるのは、ギルドマスターだけです";
			return;
		}
		if ($m{money} < $mark_money) {
			$mes = "ギルドマークを変更するのに <b>$mark_money</b> G必要です";
			return;
		}
	}
	
	my $p = '';
	opendir my $dh, "$icondir/mark" or &error("$icondir/markディレクトリが開けません");
	while (my $file_name = readdir $dh) {
		next if $file_name =~ /^\./;

		my $no = $file_name;
		$no =~ s/[^0-9]//g;

		if ($m{guild} && $no eq $target) {
			my $gid = unpack 'H*', $m{guild};
			# ギルドマーク画像をコピー
			&copy("$icondir/mark/$file_name", "$guilddir/$gid/mark.gif");

			$npc_com   = qq|$m{guild}のギルドマークを <img src="$icondir/mark/$file_name" /> に変更しました|;
			$m{money} -= $mark_money;
			return;
		}
		$p .= qq|<span onclick="text_set('＠まーく>$no ')"><img src="$icondir/mark/$file_name" title="$no" /></span> |;
	}
	closedir $dh;

	$mes = qq|ギルドマークの変更には $mark_money Gかかります。どのギルドマークにしますか？<br />$p|;
	$act_time = 0;
}



#=================================================
# ＠さんか
#=================================================
sub sanka {
	my $target = shift;
	
	if ($m{guild}) {
		$mes = "$m{guild}に参加しています。他のギルドに参加したい場合は、今のギルドを脱退してください。";
		return;
	}
	
	my $p = '';
	opendir my $dh, $guilddir or &error("$guilddirディレクトリが開けません");
	while (my $gid = readdir $dh) {
		next if $gid =~ /\./;
		my $gname = pack 'H*', $gid;
		
		if ($target eq $gname) {
			open my $fh, "+< $guilddir/$gid/member.cgi" or &error("$guilddir/$gid/member.cgiファイルが開けません");
			eval { flock $fh, 2; };
			my $head_line = <$fh>;
			my @lines = ($head_line);
			while ($line = <$fh>) {
				my($name, $position) = split /<>/, $line;
				if ($name eq $m) {
					$mes = "$targetにはすでに参加申\請を出しています";
					return;
				}
				push @lines, $line;
			}
			push @lines, "$m<>参加申\請中<>\n";
			seek  $fh, 0, 0;
			truncate $fh, 0;
			print $fh @lines;
			close $fh;
			
			my($guild_master) = (split /<>/, $head_line)[0];
			&send_letter($guild_master, "【＋参加申\請＋】$gname 入団希望者 $m");
			$npc_com = "$gnameのギルマス $guild_master に参加申\請の手紙を送りました。ギルマスからの返事を待ちましょう";
			return;
		}
		$p .= qq|<span onclick="text_set('＠さんか>$gname ')">$gname</span> / |;
	}
	closedir $dh;
	
	$mes = "どのギルドに参加しますか？<br />$p";
}

#=================================================
# ＠つくる
#=================================================
sub tsukuru {
	my $target = shift;
	
	if ($m{guild}) {
		$mes = "$m{guild}に参加しています。新規にギルドを設立する場合は、今のギルドを脱退してください。";
		return;
	}
	
	my $max_guild_name_z = int($max_guild_name * 0.5);
	unless ($target) {
		$mes  = "設立金として $make_money Gかかります。<br />";
		$mes .= "＠つくる>○○○ ○○○にはギルド名をいれてください(最大全角$max_guild_name_z文字[半角$max_guild_name文字]まで)";
		return;
	}
	$mes = "ギルド名に不正な空白が含まれています"								if $target =~ /　|\s/;
	$mes = "ギルド名に不正な文字( ,;\"\'&<>\@ )が含まれています"				if $target =~ /[,;\"\'&<>\@]/;
	$mes = "ギルド名に不正な文字( ＠ )が含まれています"							if $target =~ /＠/;
	$mes = "ギルド名は$max_guild_name_z文字[半角$max_guild_name文字]までです"	if length $target > $max_guild_name;
	$mes = "ギルド設立金の $make_money Gが足りません"							if $make_money > $m{money};
	return if $mes;
	
	my $gid = unpack 'H*', $target;
	if (-d "$guilddir/$gid") {
		$mes = "すでに同じ名前のギルドが存在します";
		return;
	}
	
	# 新規ギルド作成
	mkdir "$guilddir/$gid", $mkdir or &error("$guilddir/$gidディレクトリが作成できません");
	
	my %guild_dirs = (
		log			=> "$time<>$date<>$npc_name<><>$npc_color<>ギルドの設立を許可します＠ギルド>$target<><>\n",
#		log_member	=> "$time<>1<>$target<>0.0.0.0<>$m{color}<>\n",
		log_member	=> "",
		member		=> "$m<>ギルマス<>\n",
		data		=> "$target<>$m<>$default_color<><>$date設立<>0<>"
	);
	for my $k (keys %guild_dirs) {
		open my $fh, "> $guilddir/$gid/$k.cgi" or &error("$guilddir/$gid/$k.cgiファイルが作れません");
		print $fh $guild_dirs{$k};
		close $fh;
		chmod $chmod, "$guilddir/$gid/$k.cgi";
	}
	
	# 画像をコピー
	&copy($default_mark, "$guilddir/$gid/mark.gif");
	$m{lib}    = 'guild';
	$m{guild}  = $target;
	$m{money} -= $make_money;
	
	$npc_com = qq|<span class="st_up">＠新ギルド <b>$target</b>の設立を許可します！</span>|;
	&write_memory(qq|<span class="st_up">新ギルド<b>$target</b>を設立！</span>|);
	&write_news(qq|<span class="st_up">$mが新しく<b>$target</b>ギルドを設立しました！</span>|);
	
	&check_dead_guild;
}
#=================================================
# ＠かいめい
#=================================================
sub kaimei {
	my $target = shift;
	
	unless ($m{guild}) {
		$mes = "ギルドに所属していません";
		return;
	}

	my $old_gid = unpack 'H*', $m{guild};
	unless (-d "$guilddir/$old_gid") {
		$mes = "$m{guild}ギルドが存在しません";
		$m{guild} = "";
		return;
	}
	unless (&is_guild_master($old_gid)) {
		$mes = "ギルド名を変更できるのは、ギルドマスターだけです";
		return;
	}

	$mes = "ギルド名に不正な空白が含まれています"					if $target =~ /　|\s/;
	$mes = "ギルド名に不正な文字( ,;\"\'&<>\@ )が含まれています"	if $target =~ /[,;\"\'&<>\@]/;
	$mes = "ギルド名に不正な文字( ＠ )が含まれています"				if $target =~ /＠/;
	$mes = "ギルド名は半角$max_guild_name文字までです"				if length $target > $max_guild_name;
	$mes = "ギルド名を変更するのに <b>$make_money</b> G必要です"	if $make_money > $m{money};
	return if $mes;
	
	my $gid = unpack 'H*', $target;
	if (-d "$guilddir/$gid") {
		$mes = "すでに同じ名前のギルドが存在します";
		return;
	}
	
	# 新規ギルド作成＋データコピー
	mkdir "$guilddir/$gid", $mkdir or &error("$guilddir/$gidディレクトリが作成できません");
	opendir my $dh, "$guilddir/$old_gid" or &error("$guilddir/$old_gidディレクトリが開けません");
	while (my $file_name = readdir $dh) {
		next if $file =~ /^\./;
		&copy("$guilddir/$old_gid/$file", "$guildir/$gid/$file");
	}
	closedir $dh;
	
	# 所属しているメンバーのギルド名を変更
	open my $fh, "< $guilddir/$dir_name/member.cgi" or &error("$guilddir/$dir_name/member.cgiファイルが読み込めません");
	while (my $line = <$fh>) {
		my($name, $position) = split /<>/, $line;
		next if $position eq '参加申請中';
		&regist_you_data($name, 'guild', $target);
	}
	close $fh;
	
	# 旧ギルドの削除
	&delete_directory("$guilddir/$old_gid");
	
	$npc_com = qq|<span class="st_up">＠ギルド改名<b>$m{guild}</b>あらため<b>$target</b>ギルドに改名します</span>|;
	&write_memory(qq|<span class="st_up">ギルド名を<b>$target</b>に変更</span>|);
	&write_news(qq|<span class="st_up">$mが $m{guild} ギルドを <b>$target</b> ギルドに変更しました！</span>|);

	$m{lib}    = 'guild';
	$m{guild}  = $target;
	$m{money} -= $make_money;
}


#=================================================
# ＠だったい
#=================================================
sub dattai {
	unless ($m{guild}) {
		$mes = "ギルドに所属していません";
		return;
	}

	&delete_guild_member($m{guild}, $m);
	&write_memory("$m{guild}から脱退する");
	$npc_com .= "$m{guild}から脱退しました";
	$m{guild} = '';
}

#=================================================
# ＠かいさん
#=================================================
sub kaisan {
	unless ($m{guild}) {
		$mes = "ギルドに所属していません";
		return;
	}
	
	my $gid = unpack 'H*', $m{guild};
	unless (-d "$guilddir/$gid") {
		$mes = "$m{guild}ギルドが存在しません";
		$m{guild} = "";
		return;
	}
	
	if (&is_guild_master($gid)) {
		&delete_directory("$guilddir/$gid");
		&write_memory("$m{guild}を解散させる");
		$npc_com  = "$m{guild}を解散させました";
		&write_news(qq|<span class="die">$m{guild} ギルドが解散しました</span>|);
		$m{guild} = "";
	}
	else {
		$mes = "解散させることができるのはギルマスだけです";
	}
}

# ------------------
# ギルドマスターかどうか
sub is_guild_master {
	my $gid = shift;

	open my $fh, "< $guilddir/$gid/member.cgi" or &error("$guilddir/$gid/member.cgiファイルが読み込めません");
	my $line = <$fh>;
	close $fh;
	my($guild_master) = (split /<>/, $line)[0];
	
	$m{name} eq $guild_master ? return 1 : return 0;
}


# ------------------
# 数日以上誰も出入りしていないギルドの自動削除
sub check_dead_guild {
	opendir my $dh, $guilddir or &error("$guilddirディレクトリが開けません");
	while (my $gid = readdir $dh) {
		next if $gid =~ /\./;
		my($mtime) = (stat("$guilddir/$gid/log_member.cgi"))[9];
		if ($time > $mtime + $auto_delete_guild_day * 3600 * 24) {
			&delete_directory("$guilddir/$gid");
			my $gname = pack 'H*', $gid;
			&write_news(qq|<span class="die">$gname ギルドが解散しました</span>|);
		}
	}
	closedir $dh;
}


1; # 削除不可
