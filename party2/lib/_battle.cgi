require "./lib/_skill.cgi";
#=================================================
# 戦闘処理 Created by Merino
# vs_player.cgi,vs_monster.cgi,vs_guild.cgi共通サブルーチン 
#=================================================
# ログに使うファイル(.cgi抜き)
$this_file = "$questdir/$m{quest}/log";


#=================================================
# 倒したときの処理
#=================================================
sub defeat {
	my $y = shift;
	
	# 復活の状態
	if ($ms{$y}{tmp} eq '復活') {
		$ms{$y}{tmp} = '';
		$ms{$y}{hp}  = int($ms{$y}{mhp} * (rand(0.1)+0.1));
		$com.=qq|<span class="revive">$yは瀕死でよみがえった！</span>|;
		&reset_status($y);
		return;
	}
	
	# 状態など初期化
	$ms{$y}{hp} = 0;
	&reset_status($y);
	
	# NPCがプレイヤーを倒した時。または自爆
	return if $ms{$m}{color} eq $npc_color || $m eq $y;

	$com .= qq|<br /><span class="get">$mたちはそれぞれ $ms{$y}{get_exp} の$e2j{exp}と $ms{$y}{get_money} Gを手に入れた！</span>|;
	
	for my $name (@partys) {
		next if $ms{$name}{hp} <= 0;
		if ($name eq $m) { # 倒した人
			$m{exp}   += $ms{$y}{get_exp};
			$m{money} += $ms{$y}{get_money};
			
			my $par = 2; # 仲間になる確率(自分より弱い)
			if ( &is_strong(%{ $ms{$y} }) ) { # 自分より強い判定
				$win ? $m{kill_p}++ : $m{kill_m}++;
				$par = 1 unless $ms{$m}{job} eq '12'; # 仲間になる確率(自分より強い)。ただし、魔物使いなら確率下がらず。
			}
			$par += 2 if $m{ite} eq '77'; # 魔物のｴｻ
			
			if (!$win && $ms{$y}{color} eq $npc_color && rand(200) < $par) { # モンスターゲット
				my $base_name = $y;
				$base_name =~ s/^\@//; # 戦闘の@を除く
				$base_name =~ s/[A-Z]$//; # 末尾のA～Zを除く
				$npc_name = $base_name; 
				$npc_com .= "<br />" if $npc_com;
				$npc_com .= qq|なんと<img src="$icondir/$ms{$y}{icon}" />$base_name が起き上がりこちらを見ている。|;
				if ( &is_full_monster($id) ) {
					$npc_com .= "しかし、$mのモンスター預かり所はいっぱいだった。$base_nameは悲しそうに去っていった…";
				}
				else {
					$npc_com .= "$base_nameはうれしそうに$mのモンスター預かり所に向かった";
					
					open my $fh, ">> $userdir/$id/monster.cgi";
					print $fh "$base_name<>$ms{$y}{icon}<>\n";
					close $fh;
					
					require "./lib/_add_monster_book.cgi";
					&add_monster_book($y);
				}
			}
		}
		else { # 仲間メンバーのそれぞれのファイルを開いてプラス処理
			my $yid = unpack 'H*', $name;
			next unless -f "$userdir/$yid/user.cgi";
			open my $fh, ">> $userdir/$yid/stock.cgi" or &error("$userdir/$yid/stock.cgiファイルが開けません");
			print $fh "$ms{$y}{get_exp}<>$ms{$y}{get_money}<>\n";
			close $fh;
		}
	}
}

#=================================================
# レベルアップ
#=================================================
sub lv_up {
	++$m{lv};
	++$m{sp};
	++$ms{$m}{sp};
	$npc_com .= "<br />" if $npc_com;
	$npc_com .= qq|<span class="lv_up">$mのレベルが上がった♪$e2j{lv}$m{lv}になった！|;

	my $i = 2;
	for my $k (qw/hp mp at df ag/) {
		my $v = int(rand($jobs[$m{job}][$i]+1));
		$v = int(rand(9)+1) if $v > 9;
		if ($k eq 'hp') {
			++$v;
			$m{'m'.$k} += $v;
		}
		elsif ($k eq 'mp')  {
			$m{'m'.$k} += $v;
		}
		else {
			$m{$k} += $v;
		}
		$ms{$m}{'m'.$k} += $v;
		$npc_com .= "$e2j{$k}＋$v ";
		++$i;
	}
	
	my @skills = &{ 'skill_'.$ms{$m}{job} };
	for my $i (0..$#skills) {
		if ($skills[$i][0] eq $m{sp}) {
			$npc_com .= qq|<br /><b>$mは新しく $skills[$i][2] を覚えた！</b>|;
		}
	}
	$npc_com .= qq|</span>|;
}

#=================================================
# ステータス表示
#=================================================
sub header_html {
	print qq|<div class="mes">【$this_title】|;
	print qq| $e2j{mhp}<b>$ms{$m}{hp}</b>/<b>$ms{$m}{mhp}</b> $e2j{mmp}<b>$ms{$m}{mp}</b>/<b>$ms{$m}{mmp}</b>|;
	print qq| $e2j{at}<b>$ms{$m}{at}</b> $e2j{df}<b>$ms{$m}{df}</b> $e2j{ag}<b>$ms{$m}{ag}</b> $jobs[$m{job}][1](<b>$m{sp}</b>)|;
	print qq| $jobs[$m{old_job}][1](<b>$m{old_sp}</b>)| if $m{old_job};
	print qq| E：$ites[$m{ite}][1]| if $m{ite};
	print qq|</div>|;
}

#=================================================
# メンバー出力
#=================================================
sub member_html {
	my $member_html = '';
	$member_html .= qq|<div style="background: url($bgimg) #333 repeat-x center bottom;"><table><tr>|;
	for my $name (@members) {
		next if $ms{$name}{hp} <= 0 && ($ms{$m}{color} ne $ms{$name}{color} || $name =~ /^@/); # やられた敵や身代わりを除く
		my $par = int($ms{$name}{hp} / $ms{$name}{mhp} * 100);
		my $_mhp = $ms{$name}{mhp} > 999 ? '???' : $ms{$name}{mhp};
		my $_hp  = $ms{$name}{hp}  > 999 ? '???' : $ms{$name}{hp};
		$member_html .= qq|<td onclick="text_set('>$name ')" align="center" valign="bottom"><div class="battle-disp" style="color: $ms{$name}{color};">|;
		$member_html .= $ms{$name}{tmp} || $ms{$name}{state} ? qq|<span class="state">$ms{$name}{state}</span><span class="tmp">$ms{$name}{tmp}</span>| : defined($ten_names{ $ms{$name}{ten} }) ? $ten_names{ $ms{$name}{ten} } : q{};
		$member_html .= qq|<br />$_hp <span style="color: #99C;">/</span> $_mhp<div class="gage_back2"><img src="$htmldir/space.gif" width="$par%" class="gage_bar2" /></div>$name<br /></div>|;
		$member_html .= $ms{$name}{hp} <= 0 ? qq|<img src="$icondir/chr/099.gif" alt="$name" /></td>| : qq|<img src="$icondir/$ms{$name}{icon}" alt="$name" /></td>|;
	}
	$member_html .= qq|</tr></table></div>|;
	return $member_html;
}


# $FH 排他制御をするためのグローバル変数(このファイルのみ)。複数のプレイヤーが同じファイルを共有するため。
my $FH;
#=================================================
# メンバー読み込み
#=================================================
sub read_member {
	@members = ();
	@enemys = ();
	@partys = ();
	%ms = (); # Members

	my $count = 0;
	open $FH, "+< $questdir/$m{quest}/member.cgi" or do{ $m{lib} = ''; $m{quest} = ''; &write_user; &error("すでにパーティーが解散してしまったようです"); };
	eval { flock $FH, 2; };
	my $head_line = <$FH>;
	($speed,$stage,$round,$leader,$p_name,$p_pass,$p_join,$win,$bet,$is_visit,$need_join,$type,$map,$py,$px,$event) = split /<>/, $head_line;
	$act_time = $speed;
	while (my $line = <$FH>) {
		my @datas = split /<>/, $line;
		my $name  = $datas[0];
		my $i = 0;
		for my $k (@battle_datas) {
			$ms{$name}{$k} = $datas[$i];
			++$i;
		}
		# 汚染チェック(ありえないデータ)。強制クエスト削除。
		if (!defined($ms{$name}{mhp}) || $ms{$name}{mhp} <= 0) {
			close $FH;
			&delete_directory("$questdir/$m{quest}");
			&error("データが壊れています。クエストを強制終了します");
		}
		push @members, $name;
	}
	
	for my $name (@members) {
		if (defined($ms{$m}{name}) && $ms{$m}{color} eq $ms{$name}{color}) {
			push @partys, $name;
		}
		else {
			next if $ms{$name}{hp} <= 0;
			push @enemys, $name;
		}
	}
}


#=================================================
# メンバー書き込み
#=================================================
sub write_member {
	return unless -d "$questdir/$m{quest}";
	
	my $head_line = "$speed<>$stage<>$round<>$leader<>$p_name<>$p_pass<>$p_join<>$win<>$bet<>$is_visit<>$need_join<>$type<>$map<>$py<>$px<>$event<>\n";
	my @lines = ($head_line);
	for my $name (@members) {
		next if $name =~ /^@/ && $ms{$name}{hp} <= 0; # やられたNPCや身代わりを除く
		my $line = '';
		for my $k (@battle_datas) {
			$line .= "$ms{$name}{$k}<>";
		}
		push @lines, "$line\n";
	}
	
	seek  $FH, 0, 0;
	truncate $FH, 0;
	print $FH @lines;
	close $FH;
}

#=================================================
# 戦闘アクション
#=================================================
sub action {
	$com .= "\x20";
	$com =~ /＠(.+?)(?:(?:\x20|　)?&gt;(.+?)(?:\x20|　)|\x20|　)/;
	my $action = $1;
	my $target = $2 ? $2 : '';
	return unless defined $actions{$action}[1];
	if ($time - $ms{$m}{time} < $act_time) {
		$mes = "まだ行動することはできません";
		return;
	}
	
	if ($action eq 'ささやき') {
		&sasayaki($target);
		return;
	}
	elsif ($action eq 'すくしょ') {
		&sukusho($target);
		return;
	}
	elsif (!defined($ms{$m}{name}) || $ms{$m}{hp} <= 0) {
		if ($action eq 'にげる') {
			&nigeru;
		}
		elsif ($win && $action eq 'かいし') { # 引分けの時用
			&kaishi;
			&write_member;
		}
		else {
			$mes = '戦闘不能により行動できません';
		}
		return;
	}
	
	# 状態異常
	if ($ms{$m}{state} eq '動封') {
		$ms{$m}{state} = '';
		$com .="しかし、$mは動くことができない！";
	}
	elsif ($ms{$m}{state} eq '麻痺') {
		if (rand(3) < 1) {
			$com .="$mのしびれがなくなりました！";
			$ms{$m}{state} = '';
		}
		else {
			$com .= "$mはしびれて動くことができない！";
		}
	}
	elsif ($ms{$m}{state} eq '眠り') {
		if (rand(3) < 1) {
			$com .="$mは眠りからさめました！";
			$ms{$m}{state} = '';
		}
		else {
			$com .= "$mは眠っている！";
		}
	}
	else { # 正常
		if ($ms{$m}{state} eq '混乱') {
			if (rand(5) < 1) {
				$com .="$mは混乱がなおりました！";
				$ms{$m}{state} = '';
			}
			else {
				$com .= "$mは混乱している！";
			}
		}
		
		$ms{$m}{tmp} = '' if $ms{$m}{tmp} =~ /防御|反撃/ || rand(3) < 1; # 防御と反撃以外は数ターン残る
		&{ $actions{$action}[1] }($target);
		return if $mes;
		
		$ms{$m}{mp} -= $actions{$action}[0];
		$ms{$m}{mp}  = 0 if $ms{$m}{mp} < 0;
		
		if ($ms{$m}{hp} > 0) {
			if ($ms{$m}{state} eq '猛毒') {
				my $v = int($ms{$m}{mhp}*0.1);
				$v = int(rand(100)+950) if $v > 999;
				$ms{$m}{hp} -= $v;
				$com.=qq|$mは猛毒により <span class="damage">$v</span> のダメージをうけた！|;
				
				if ($ms{$m}{hp} <= 0) {
					$ms{$m}{hp} = 0;
					&reset_status($m);
					$com .= qq!<span class="die">$mは倒れた！</span>!;
					&defeat($m);
				}
			}
			if ($ms{$m}{tmp} eq '回復' && $ms{$m}{hp} > 0) { # 自動回復
				my $v = $ms{$m}{mhp} > 999 ? int(rand(100)) : int($ms{$m}{mhp} * (rand(0.1)+0.1));
				$ms{$m}{hp} += $v;
				$ms{$m}{hp} = $ms{$m}{mhp} if $ms{$m}{hp} > $ms{$m}{mhp};
				$com .= qq|<b>$m</b>の$e2j{mhp}が <span class="heal">$v</span> 回復した！|;
			}
		}
	}
	&get_stock if -s "$userdir/$id/stock.cgi"; # 取得経験値、お金をデータに反映
	if ($m{lv} < 99 && $m{exp} >= $m{lv} * $m{lv} * 10) {
		&lv_up;
	}
	elsif ($is_npc_action && @enemys > 0 && !$npc_com) {
		&npc_turn;
	}
	
	$m{wt}  = $time + $act_time;
	$nokori = $act_time;
	$ms{$m}{time} = $time;
	&write_member;
}


#=================================================
# ＠にげる
#=================================================
sub nigeru {
	$is_npc_action = 0;
	$m{lib} = 'quest';

	# クエストのメンバーリストから除く
	my $is_join = 0;
	my @new_members = ();
	my @dummy_members = ();
	for my $name (@members) {
		if ($m eq $name) {
			$is_join = 1;
			next;
		}
		$name =~ /^@/ ? push @dummy_members, $name : push @new_members, $name;
	}
	@members = @new_members;

	# 見学者はそのまま帰す
	unless ($is_join) {
		$mes ="$p_nameの見学から逃げ出しました";
		&reload("$p_nameの見学から逃げ出しました");
		return;
	}
	
	&get_stock if -s "$userdir/$id/stock.cgi"; # 取得経験値、お金をデータに反映
	
	# 疲労度プラス
	$m{tired} += $round * 3 + 1;
	$m{is_eat} = 0;
	$m{hp} = $ms{$m}{hp};
	$m{mp} = $ms{$m}{mp};
	$m{hp} = $m{mhp} if $m{hp} > $m{mhp};
	$m{mp} = $m{mmp} if $m{mp} > $m{mmp};
	$m{exp}   += $round * 20 if $m{ite} eq '105'; # 幸せのくつ
	$m{money} += int($round * rand(77)) if $m{ite} eq '106'; # 金の鶏
	
	if ($round <= 0 && $win > 0) {
		# 闘技場で開始前に抜けた場合。返金
		if ($type eq '4') {
			$m{money} += $bet;
			&add_bet($m{quest}, "-$bet");
			&reload("戦闘から逃げ出しました<br />賭け金の $bet Gが返金されました");
		}
		# ギルド戦で抜けた場合。優勝ギルドポイント減
		elsif($type eq '5') {
			&add_bet($m{quest}, "-2");
			&reload("戦闘から逃げ出しました");
		}
		else {
			&reload("戦闘から逃げ出しました");
		}
	}
	else {
		&reload("戦闘から逃げ出しました");
	}

	# 誰もいなくなったらクエストを削除
	if (@members < 1 && ($type ne '6' || ($type eq '6' && $ms{$leader}{hp} <= 0)) ) { # 封印戦じゃない時でプレイヤーが０人か、封印戦でボスのＨＰが０以下
		&write_member;
		$this_file = "$logdir/quest";
		&delete_directory("$questdir/$m{quest}");
		$mes = "戦闘から逃げ出しました";
	}
	else {
		# ﾘｰﾀﾞｰだった場合ﾘｰﾀﾞｰ交代
		if ($leader eq $m) {
			$leader = $members[0];
			$npc_com = "$p_nameのリーダーが$leaderになりました";
		}
		push @members, @dummy_members;
		&write_member;
	}
}

# 強さ計算
sub strong {
	my %p = @_;	
	return int($p{mhp} + $p{mmp} + $p{at} + $p{df} * 0.5 + $p{ag});
}
sub is_strong {
	my %p = @_;
	&strong(%p) > &strong(%m) * 0.5 ? return 1 : return 0;
}

# 状態などの値をデフォルトに戻す
sub reset_status {
	my $y = shift;
	$ms{$y}{state} = '';
	$ms{$y}{tmp} = '';
	$ms{$y}{ten} = 1;
	$ms{$y}{hit} = 95;
	$ms{$y}{at} = $ms{$y}{mat} + $weas[$ms{$y}{wea}][3];
	$ms{$y}{df} = $ms{$y}{mdf} + $arms[$ms{$y}{arm}][3];
	$ms{$y}{ag} = $ms{$y}{mag} - $weas[$ms{$y}{wea}][4] - $arms[$ms{$y}{arm}][4];
	&{ $ites[$ms{$y}{ite}][4] }($y) if $ites[$ms{$y}{ite}][3] eq '3'; # 装飾品(戦闘開始時、死亡時、いてつくはどうなど &reset_statusの時)
	$ms{$y}{ag} = 0 if $ms{$y}{ag} < 0;
}
sub reset_status_all {
	for my $name (@members) {
		&reset_status($name);
	}
}



# 並び順を色ごとにシャッフル
sub shuffle {
	# 全色取得
	my %teams = ();
	for my $name (@members) {
		++$teams{ $ms{$name}{color} };
	}
	
	# 色をシャッフル
	my @new_team_colors = ();
	my(@team_colors) = keys %teams;
	while (@team_colors) {
		push( @new_team_colors, splice(@team_colors, rand @team_colors, 1) );
	}
	
	# 色順にメンバーを並び換え
	my @new_members = ();
	for my $new_team_color (@new_team_colors) {
		for my $name (@members) {
			if ($new_team_color eq $ms{$name}{color}) {
				push @new_members, $name;
			}
		}
	}
	@members = @new_members;
}

sub get_stock {
	open my $fh, "+< $userdir/$id/stock.cgi" or &error("$userdir/$id/stock.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($exp, $money) = split /<>/, $line;
		$m{exp} += $exp;
		$m{money} += $money;
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	close $fh;
}


1; # 削除不可
