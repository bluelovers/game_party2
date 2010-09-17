my($gid,$gname,$gmaster,$gcolor,$gbgimg,$gmes,$gpoint) = &read_guild_data;
#=================================================
# ギルド Created by Merino
#=================================================
# 場所名
$this_title = qq|<img src="$guilddir/$gid/mark.gif" alt="ギルドマーク" /><span style="color: $gcolor">$m{guild}</span>|;

# ログに使うファイル(.cgi抜き)
$this_file  = "$guilddir/$gid/log";

# 背景画像
$bgimg   = "$bgimgdir/$gbgimg";

# 最大ギルドメッセージ文字数(半角)
$max_guild_mes = 200;

#=================================================

#=================================================
# 追加アクション
#=================================================
push @actions, 'めんばー';
push @actions, 'よびかける';
$actions{'めんばー'} = sub{ &menba }; 
$actions{'よびかける'} = sub{ &yobikakeru }; 
if ($gmaster eq $m) {
	push @actions, 'からー';
	push @actions, 'めっせーじ';
	push @actions, 'あたえる';
	$actions{'からー'}     = sub{ &color }; 
	$actions{'めっせーじ'} = sub{ &message }; 
	$actions{'あたえる'}   = sub{ &ataeru }; 
}

#=================================================
# ＠よびかける
#=================================================
sub yobikakeru {
	my $target = shift;

	unless ($target) {
		$mes = qq|<span onclick="text_set('＠よびかける')">『＠よびかける>○○○』ギルドのメンバーに送りたい文を○○○に書いてください。</span>|;
		return;
	}
	
	$this_file = "$userdir/$id/letter_log";
	open my $fh, "< $guilddir/$gid/member.cgi" or &error("$guilddir/$gid/member.cgiファイルが読み込めません");
	while (my $line = <$fh>) {
		my($name, $position) = split /<>/, $line;
		&send_letter($name, $com);
		return if $mes;
	}
	close $fh;
	
	$this_file = "$guilddir/$gid/log";
	$npc_name  = '@'.$gname;
	$npc_com   = "$gnameのメンバー全員に手紙を送りました";
	&regist_guild_data('point', 1, $m{guild}) if $m{guild};
}

#=================================================
# ＠からー
#=================================================
sub color {
	$target = shift;
	
	if ($target =~ /(#[0-9a-fA-F]{6})/) {
		my $color = uc $1;
		if ($color ne $default_color && ($color eq $npc_color || &is_used_guild_color($color)) ){
			$mes = "すでに他のギルドでそのカラーは使われています";
		}
		else {
			&regist_guild_data('color', $color, $m{guild});
			$com .= qq|ギルドカラーを<font color="$color">$color</font>に変更しました|;
		}
		return;
	}
	else {
		my %sample_colors = (
			'レッド'		=> '#FF3333',
			'ピンク'		=> '#FF33CC',
			'オレンジ'		=> '#FF9933',
			'イエロー'		=> '#FFFF33',
			'グリーン'		=> '#33FF33',
			'アクア'		=> '#33CCFF',
			'ブルー'		=> '#3333FF',
			'パープル'		=> '#CC66FF',
			'グレイ'		=> '#CCCCCC',
			'ホワイト'		=> '#FFFFFF',
		);
		
		$mes  = qq|#から始まる(16進数の)カラーコードを記入してください。※ホワイトの場合はギルド戦はできません<br />サンプル＞|;
		
		while (my($name, $c_code) = each %sample_colors) {
			$mes .= qq|<span onclick="text_set('＠からー>$c_code ')" style="color: $c_code;">$name</span> |;
		}
		return;
	}
}
#=================================================
# ＠めっせーじ
#=================================================
sub message {
	$target = shift;
	
	unless ($target) {
		$mes = qq|<span onclick="text_set('＠めっせーじ>')">メッセージを記入してください</span>|;
		return;
	}
	
#	$mes = qq|<span onclick="text_set('＠めっせーじ>')">メッセージに不正な空白が含まれています</span>|						if $target =~ /　|\s/;
	$mes = qq|<span onclick="text_set('＠めっせーじ>')">メッセージに不正な文字( ,;\"\'&<> )が含まれています</span>| 	    if $target =~ /[,;\"\'&<>]/;
#	$mes = qq|<span onclick="text_set('＠めっせーじ>')">メッセージに不正な文字( ＠ )が含まれています</span>| 				if $target =~ /＠/;
	$mes = qq|<span onclick="text_set('＠めっせーじ>')">メッセージは半角$max_guild_mes文字までです</span>|					if length($target) > $max_guild_mes;
	return if $mes;
	
	&regist_guild_data('mes', $target, $m{guild});
	$com .= qq|ギルドメッセージを変更しました|;
}
#================================================
# ＠はなす
#================================================
sub hanasu { 
	if ($gmes) {
		$mes = $gmes;
	}
	else {
		&menba;
	}
}

#=================================================
# ＠めんばー
#=================================================
sub menba {
	$mes .= "$gmes<br />";
	open my $fh, "< $guilddir/$gid/member.cgi" or &error("$guilddir/$gid/member.cgiファイルが読み込めません");
	while (my $line = <$fh>) {
		my($name, $position) = split /<>/, $line;
		$mes .= qq|<span onclick="text_set('＠ほーむ>$name ')">$name＠$position</span>,|;
	}
	close $fh;
}


#=================================================
# ＠あたえる
#=================================================
sub ataeru {
	$npc_name = '@'.$gname;
	my $target = shift;
	my($yname, $new_position) = split /＠やくしょく&gt;/, $target;

	if ($yname) {
		$mes = "役職名に不正な空白が含まれています"						if $new_position =~ /　|\s/;
		$mes = "役職名に不正な文字( ,;\"\'&<>\@ )が含まれています" 		if $new_position =~ /[,;\"\'&<>\@]/;
		$mes = "役職名に不正な文字( ＠ )が含まれています" 				if $new_position =~ /＠/;
		$mes = "$new_positionという役職名はつけることができません"		if $new_position eq '参加申請中' || $new_position eq '参加申\請中' || $new_position eq 'ギルマス';
		$mes = "役職名は全角６文字[半角12文字]までです"					if length($new_position) > 12;
		$mes = "役職名を記入してください"								if $new_position eq '';
		return if $mes;
	}
	
	my $p = '';
	$p .= qq|<span onclick="text_set('＠あたえる>○○○＠やくしょく>△△△')">『＠あたえる>○○○＠やくしょく>△△△』</span>○○○には名前、△△△には役職名(全角６文字[半角12文字]まで)を記入。<br />|;
	$p .= qq|<span onclick="text_set('＠やくしょく>')">＠やくしょく</span>に<span onclick="text_set('追放')">『追放』</span>と記入すると追い出すことができます。<br />|;
	$p .= qq|『参加申\請中』のメンバーは何か役職をあたえることにより参加許可、<span onclick="text_set('追放')">『追放』</span>で参加拒否にできます。|;
	$p .= qq|誰の役職を変えますか？<br />|;
	
	my $is_find = 0;
	open my $fh, "+< $guilddir/$gid/member.cgi" or &error("$guilddir/$gid/member.cgiファイルが開けません");
	eval { flock $fh, 2; };
	my $head_line = <$fh>;
	my($guild_master) = (split /<>/, $head_line)[0];
	unless ($m eq $guild_master) {
		$mes = "役職をあたえることができる権限はギルマスだけです";
		return;
	}
	my @lines = ($head_line);
	while (my $line = <$fh>) {
		my($name, $position) = split /<>/, $line;
		$p .= qq|<span onclick="text_set('＠あたえる>$name＠やくしょく>')">$name＠$position</span>,|;
		if ($name eq $yname) {
			$is_find = 1;
			if ($position eq '参加申\請中') {
				my $yid = unpack 'H*', $name;
				# 削除などでいない
				unless (-f "$userdir/$yid/user.cgi") {
					$npc_com = "$nameというプレイヤーはいなくなってしまいました";
					next;
				}
				
				my %datas = &get_you_datas($yid, 1);
				# 申請中に他のギルドに入った場合
				if ($datas{guild}){
					$npc_com = "$nameは他のギルドに参加したようです";
					next;
				}

				# 参加拒否
				if ($new_position eq '追放') {
					$npc_com = "$nameの参加を拒否しました";
					&send_letter($name, "【＋不合格＋】残念ながら $m{guild} (ギルマス $m) から参加を拒否されました");
					next;
				}
				
				$npc_com = "$nameを$m{guild}に参加することを許可しました";
				&regist_you_data($name, 'guild', $m{guild});
				&send_letter($name, "【＋参加許可証＋】$m{guild} (ギルマス $m) から参加許可をもらいました");
				&write_memory("$m{guild}ギルドに加入", $name);
				$line = "$name<>$new_position<>\n";
			}
			elsif ($new_position eq '追放') {
				$npc_com = "$nameを$m{guild}から追放しました";
				&regist_you_data($name, 'guild', '');
				&send_letter($name, "【＋追放＋】$m{guild} (ギルマス $m) から追放されました");
				next;
			}
			else {
				$line = "$name<>$new_position<>\n";
			}
		}
		push @lines, $line;
	}
	if ($is_find) {
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
		close $fh;
	}
	else {
		close $fh;
		
		$mes = $p;
	}
}

sub is_used_guild_color {
	my $select_color = shift;
	
	opendir my $dh, $guilddir or &error("$guilddirディレクトリが開けません");
	while (my $dir_name = readdir $dh) {
		next if $dir_name =~ /^\./;
		open my $fh, "< $guilddir/$dir_name/data.cgi";
		my $line = <$fh>;
		close $fh;
		my($color) = (split /<>/, $line)[2];
		return 1 if $select_color eq $color;
	}
	closedir $dh;

	return 0;
}


1; # 削除不可
