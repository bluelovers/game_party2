#=================================================
# コレクション追加 Created by Merino
# collction.cgi,depot.cgi,weapon.cgi,armor.cgi,item.cgiで使用
#=================================================
# 使い方:コレクションに追加したいタイミングで下二行
# require './lib/_add_collection.cgi';
# &add_collection;

#================================================
# 自分のコレクションデータ取得 + 今装備中の物がコレクションにないなら追加
#=================================================
sub add_collection {
	my @kinds = ('', 'wea', 'arm', 'ite');
	my $kind = 1;
	my $is_rewrite = 0;
	my @lines = ();
	
	open my $fh, "+< $userdir/$id/collection.cgi" or &error("コレクションファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		$line =~ tr/\x0D\x0A//d; # \n改行削除
		
		# 追加
		if ($m{ $kinds[$kind] } && $line !~ /,$m{ $kinds[$kind] },/) {
			$is_rewrite = 1;
			$line .= "$m{ $kinds[$kind] },";
			$npc_com .= "<br />" if $npc_com;
			$npc_com .= $kind eq '1' ? "<b>$weas[$m{wea}][1]"
					  : $kind eq '2' ? "<b>$arms[$m{arm}][1]"
					  :                "<b>$ites[$m{ite}][1]"
					  ;
			$npc_com .= 'が新しくアイテム図鑑に登録されました</b>';
			
			# sort
			$line  = join ",", sort { $a <=> $b } split /,/, $line;
			$line .= ",";
		}
		
		push @lines, "$line\n";
		++$kind;
	}
	if ($is_rewrite) {
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
	}
	close $fh;
	
	return @lines;
}

#================================================
# 読み込みのみ(相手のコレクションデータを見るときなど)
#=================================================
sub read_collection {
	my $yid = shift || $id;
	
	my @lines = ();
	open my $fh, "< $userdir/$yid/collection.cgi" or &error("$userdir/$yid/collection.cgiファイルが読み込めません");
	while (my $line = <$fh>) {
		push @lines, $line;
	}
	close $fh;
	return @lines;
}



1; # 削除不可
