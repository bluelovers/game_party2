#=================================================
# 町共通処理 Created by Merino
#=================================================


#=================================================
# 追加アクション
#=================================================
push @actions, 'たてる';
push @actions, 'ちぇっく';
$actions{'たてる'}   = sub{ &tateru }; 
$actions{'ちぇっく'} = sub{ &chekku }; 

#=================================================
# ＠ちぇっく
#=================================================
sub chekku {
	my $target = shift;
	
	unless ($target) {
		$mes = qq|<span onclick="text_set('＠ちぇっく')">＠ちぇっく>○○○ の家で、その家の所有期間を調べることができます</span>|;
		return;
	}
	
	$target .= ' の家';
	open my $fh, "< ${this_file}_member.cgi" or &error("${this_file}_member.cgiファイルが読み込めません");
	while (my $line = <$fh>) {
		my($ltime, $is_npc, $name, $laddr, $icon, $color) = split /<>/, $line;
		if ($target eq $name) {
			my($hour,$mday,$mon) = (localtime($ltime))[2..4];
			my $c_date = sprintf("%d月%d日%d時", $mon+1,$mday,$hour);
			$npc_com = "<b>$name</b>の所有期間は $c_date までです";
			return;
		}
	}
	close $fh;

	$mes = qq|<span onclick="text_set('＠ちぇっく')">＠ちぇっく>○○○ の家で、その家の所有期間を調べることができます</span>|;
}

#=================================================
# ＠たてる
#=================================================
sub tateru {
	my $target = shift;
	
	my $p = '';
	for my $house (@houses) {
		my $no = $house;
		$no =~ s/(.+)\..+/$1/; # 見栄えが悪いので拡張子を除く
		if ($no eq $target) {
			if ($m{money} < $price) {
				$mes = "家を建てるお金が足りません";
			}
			elsif (&is_max_house) {
				$mes = "$this_title には 最大 $max_house 軒までしか建てることができません<br />家がなくなるまでしばらくお待ちください";
			}
			elsif (&is_build_house) {
				$mes = "$m はすでに家を持っています";
			}
			else {
				my $c_time = $time + $cycle_house_day * 24 * 60 * 60;
				open my $fh, ">> ${this_file}_member.cgi" or &error("${this_file}_member.cgiファイルが開けません");
				print $fh "$c_time<>0<>$m の家<>0<>house/$house<>$npc_color<>\n";
				close $fh;
				
				my($hour,$mday,$mon) = (localtime($c_time))[2..4];
				my $c_date = sprintf("%d月%d日%d時", $mon+1,$mday,$hour);
				$npc_com = "$m の家を建てました！家の所有期間は $c_date までです";
				$m{money} -= $price;
				&regist_guild_data('point', $cycle_house_day * 10, $m{guild}) if $m{guild};
			}
			return;
		}
		$p .= qq|<span onclick="text_set('＠たてる>$no ')"><img src="$icondir/house/$house" /></span> |;
	}
	$mes = qq|【$this_title】 家の値段 $price G / 最大建設数 $max_house 軒 / 所有日数 $cycle_house_day 日<br />どの家を建てますか？<br />$p|;
	$act_time = 0;
}


# すでに家を建てているかどうか
sub is_build_house {
	for my $i (0..$#towns) {
		open my $fh, "< $logdir/${towns[$i][1]}_member.cgi" or &error("$logdir/${towns[$i][1]}_member.cgiファイルが読み込めません");
		while (my $line = <$fh>) {
			my($ltime, $is_npc, $name, $laddr, $icon, $color) = split /<>/, $line;
			return 1 if $name eq "$m の家";
		}
		close $fh;
	}
	return 0;
}


# 最大数を超えているかどうか
sub is_max_house {
	my $count = 0;
	for my $name (@members) {
		++$count if $ms{$name}{color} eq $npc_color;
	}
	return $count >= $max_house ? 1 : 0;
}





1; # 削除不可
