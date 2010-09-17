require './lib/_add_collection.cgi';
#=================================================
# アイテム図鑑 Created by Merino
#=================================================
my @collections = (
# タイトル,ファイル名
	['武器図鑑', 'comp_wea', 'Weapon'],
	['防具図鑑', 'comp_arm', 'Armor'],
	['道具図鑑', 'comp_ite', 'Item'],
);

#=================================================
$m{lib} = 'home'; # 更新したら強制的に家に戻る

sub read_member { return }
sub set_action  { return }

#=================================================
sub html {
	print qq|<form method="$method" action="$script">|;
	print qq|<input type="hidden" name="id" value="$id" /><input type="hidden" name="pass" value="$pass" />|;
	print qq|<input type="submit" value="戻る" /></form>|;
	print qq|<h2>$m{home}のアイテム図鑑</h2>|;
	
	my $yid = unpack 'H*', $m{home};
	unless (-f "$userdir/$yid/collection.cgi") {
		print qq|<div class="strong">$m{home}のアイテム図鑑が見つかりません</div>|;
		return;
	}
	
	my @lines = $m{home} eq $m ? &add_collection : &read_collection($yid);
	my $kind = 1;
	for my $line (@lines) {
		$line =~ tr/\x0D\x0A//d;
		
		my $count = 0;
		my $sub_mes = '';
		for my $no (split /,/, $line) {
			next if $no eq ''; # 先頭の空
			++$count;
			next unless $no;
			if    ($kind eq '1') { $sub_mes .= qq|<tr><td>$weas[$no][1]</td><td align="right">$weas[$no][3]</td><td align="right">$weas[$no][4]</td><td align="right">$weas[$no][2] G</td></tr>|; }
			elsif ($kind eq '2') { $sub_mes .= qq|<tr><td>$arms[$no][1]</td><td align="right">$arms[$no][3]</td><td align="right">$arms[$no][4]</td><td align="right">$arms[$no][2] G</td></tr>|; }
			elsif ($kind eq '3') { $sub_mes .= qq|<tr><td>$ites[$no][1]</td><td align="right">$ites[$no][2] G</td></tr>|; }
		}
		
		my $comp_par = 0;
		if ($kind eq '1') {
			$comp_par = int($count / $#weas * 100);
			&write_comp_legend($kind) if $m{home} eq $m && $count eq $#weas;
			$sub_mes = qq|<table class="table1">\n<tr><th>名前</th><th>強さ</th><th>重さ</th><th>価格</th></tr>\n$sub_mes\n</table>\n|;
		}
		elsif ($kind eq '2') {
			$comp_par = int($count / $#arms * 100);
			&write_comp_legend($kind) if $m{home} eq $m && $count eq $#arms;
			$sub_mes = qq|<table class="table1">\n<tr><th>名前</th><th>強さ</th><th>重さ</th><th>価格</th></tr>\n$sub_mes\n</table>\n|;
		}
		elsif ($kind eq '3') {
			$comp_par = int($count / $#ites * 100);
			&write_comp_legend($kind) if $m{home} eq $m && $count eq $#ites;
			$sub_mes = qq|<table class="table1">\n<tr><th>名前</th><th>価格</th></tr>\n$sub_mes\n</table>\n|;
		}
		$comp_par = 100 if $comp_par > 100;
		
		print qq|<h2>$collections[$kind-1][0] 《コンプリート率 <b>$comp_par</b>％》</h2>\n|;
		print $sub_mes;
		
		++$kind;
	}
}

#=================================================
# コンプリート処理
#=================================================
sub write_comp_legend {
	my $kind = shift;
	
	&write_legend($collections[$kind-1][1]);
	&write_memory(qq|<span class="comp">$collections[$kind-1][2] Complete!!</span>|);
	&write_news(qq|<span class="comp">$mが$collections[$kind-1][2]をコンプリートする！</span>|);
	print qq|<div class="comp">$collections[$kind-1][0] Complete!!</div>|;
	
	$kind--;
	# 0 を追加することで 100%を超えることになる
	my @lines = ();
	open my $fh, "+< $userdir/$id/collection.cgi" or &error("コレクションファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		if ($kind eq @lines) {
			$line =~ tr/\x0D\x0A//d; # \n改行削除
			$line .= "0,\n";
		}
		push @lines, $line;
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}


1; # 削除不可
