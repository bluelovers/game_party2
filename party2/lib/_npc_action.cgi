$is_npc_action = 1;

#=================================================
# ＠しらべる
#=================================================
sub shiraberu {
	my $y = shift;

	return unless defined $ms{$y}{name}; # 存在しない宝箱名
	return unless $ms{$y}{color} eq $npc_color;
	if ($ms{$y}{hp} <= 0) {
		$mes = "しかし、宝箱の中身はからっぽだった…";
		return;
	}
	elsif ($map) {
		if ($m{event} =~ /$maps[$py][$px]/) {
			$mes = "１人１個までしか開けることはできません";
			return;
		}
		$m{event} = $maps[$py][$px]; # １人１箱のための開けたかフラグ
	}
	else {
		if ($m{is_get}) {
			$mes = "１人１個までしか開けることはできません";
			return;
		}
		$m{is_get} = 1; # １人１箱のための開けたかフラグ
	}
	
	$ms{$y}{hp} = 0;
	
	if ($ms{$y}{get_exp} =~ /^[1-3]$/ && $ms{$y}{get_money}) {
		my $item_name = $ms{$y}{get_exp} eq '1' ? $weas[$ms{$y}{get_money}][1]
					  : $ms{$y}{get_exp} eq '2' ? $arms[$ms{$y}{get_money}][1]
					  :                           $ites[$ms{$y}{get_money}][1];

		$npc_com .= "宝箱の中身は… <b>$item_name</b> でした！";
		if ($ms{$y}{get_exp} eq '3' && !$m{ite}) {
			$npc_com .= "$item_nameを手に入れました！";
			$m{ite} = $ms{$y}{get_money};
			require "./lib/_add_collection.cgi";
			&add_collection;
		}
		elsif ($m{is_full}) {
			$npc_com .= "しかし、$mの預かり所はいっぱいだった…。$mは$item_nameをあきらめた";
		}
		else {
			$npc_com .= "$item_nameは預かり所に送られました";
			&send_item($m, $ms{$y}{get_exp}, $ms{$y}{get_money});
		}
	}
	else {
		$npc_com .= "しかし、宝箱の中身はからっぽだった…";
	}
}

#=================================================
# NPCの反撃(何度も同じNPCが攻撃しないように並び替える)
#=================================================
sub npc_turn {
	for my $y (@enemys) {
		next if $ms{$y}{hp} <= 0;
		next if $time - $ms{$y}{time} < $act_time;
		
		# 行動できるNPCがいた場合
		my $buf_m   = $m;
		my $buf_com = $com;
		$com = '';
		$npc_name = $y;
		$m = $y;
		$ms{$y}{time} = $time;
		$is_add_effect = 0;
		
		my @buf_ps = ();
		@buf_ps = @partys;
		@partys = @enemys;
		@enemys = ();
		for my $name (@buf_ps) {
			next if $ms{$name}{hp} <= 0;
			push @enemys, $name;
		}
		
		&npc_action if @enemys >= 1;

		@enemys = @partys;
		@partys = @buf_ps;
		$npc_com = $com;
		$m   = $buf_m;
		$com = $buf_com;
		
		# 行動したキャラを最後尾に並び替え
		my $name = shift @enemys;
		@members = (@partys,@enemys,$name);
		last;
	}
}
# ------------------
# NPCのアクション処理
sub npc_action {
	push @npc_skills, &{ 'skill_'.$ms{$m}{job}     };
	
	my @npc_actions = ();
	my %npc_actions = ();
	for my $i (0.. $#npc_skills) {
		next if $npc_skills[$i][0] > $ms{$m}{sp};
		next if $npc_skills[$i][1] > $ms{$m}{mp};
		push @npc_actions, "$npc_skills[$i][2]";
		$npc_actions{$npc_skills[$i][2]} = [ $npc_skills[$i][1], $npc_skills[$i][3] ];
	}
	@npc_skills = &{ 'skill_'.$ms{$m}{old_job} };
	for my $i (0.. $#npc_skills) {
		next if $npc_skills[$i][0] > $ms{$m}{old_sp};
		next if $npc_skills[$i][1] > $ms{$m}{mp};
		push @npc_actions, "$npc_skills[$i][2]";
		$npc_actions{$npc_skills[$i][2]} = [ $npc_skills[$i][1], $npc_skills[$i][3] ];
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
			if (rand(3) < 1) {
				$com .="$mは混乱がなおりました！";
				$ms{$m}{state} = '';
			}
			else {
				$com .= "$mは混乱している！";
			}
		}
		
		my $npc_action = $npc_actions[int(rand(@npc_actions))];
		$com .= "＠$npc_action ";
		$ms{$m}{tmp} = '' if $ms{$m}{tmp} =~ /防御|反撃/ || rand(3) < 1; # 防御と反撃以外は数ターン残る
		&{ $npc_actions{$npc_action}[1] };
		$ms{$m}{mp} -= $npc_actions{$npc_action}[0];
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

	$ms{$m}{time} = $time;
}

sub add_treasure {
	my $count = shift || $#partys;
	for my $name (@partys) {
		--$count if $ms{$name}{hp} <= 0;
	}

	# 宝箱の名前や画像
	my @boxes = (
		{ name => "普通の宝箱",		icon => "mon/900.gif", },
		{ name => "大きい宝箱",		icon => "mon/901.gif", },
		{ name => "小さい宝箱",		icon => "mon/902.gif", },
		{ name => "黒い宝箱",		icon => "mon/903.gif", },
		{ name => "青い宝箱",		icon => "mon/904.gif", },
		{ name => "古い宝箱",		icon => "mon/905.gif", },
		{ name => "丸い宝箱",		icon => "mon/906.gif", },
	);
	
	$npc_com .= "$p_name は宝箱を発見した！";
	for my $i (0 .. $count) {
		my $no = int(rand(@boxes));
		my @alfas = ('A'..'Z'); # 同じ名前を識別するために名前の後につけるもの
		my $name = '@'.$boxes[$no]{name}.$alfas[$i];
		
		for my $k (@battle_datas) {
			$ms{$name}{$k} = defined $boxes[$no]{$k} ? $boxes[$no]{$k} : 0;
		}
		$ms{$name}{ten} = 1   unless $ms{$name}{ten};
		for my $k (qw/hp df/) {
			$ms{$name}{'m'.$k} = 1000;
			$ms{$name}{$k}     = 1000;
		}
		
		$ms{$name}{name}  = $name;
		$ms{$name}{color} = $npc_color;
		$ms{$name}{tmp} = '魔無効';
		$ms{$name}{state} = '';
		
		# 曜日別にオーブを追加(曜日別にせず冒険場所固定にする場合は、↓三行コメントアウトして、./stage/**.cgiの@treasuresの道具にオーブを追加)
		my @orbs = (int(rand(6)+60), 60..65); # 日曜はランダム
		my $wday = (localtime($time))[6];
		push @{$treasures[2]}, $orbs[$wday];
		
		# 道具が出る確率を上げる 1,2,3,3
		my $v = int(rand(4)) + 1;
		$v = 3 if $v > 3 || @{$treasures[$v-1]} <= 0;
		$ms{$name}{get_exp} = $v;
		$ms{$name}{get_money} = $treasures[$v-1][int(rand(@{ $treasures[$v-1] }))];
		
		push @members, $name;
	}
}

sub add_boss {
	for my $no (0 .. $#bosses) {
		my $name = '@'.$bosses[$no]{name};
		
		for my $k (@battle_datas) {
			$ms{$name}{$k} = defined $bosses[$no]{$k} ? $bosses[$no]{$k} : 0;
		}
		
		# 初期データセット(読み込んだデータにすでに値がある場合はそっちを優先)
		$ms{$name}{hit} = 95 unless $ms{$name}{hit};
		$ms{$name}{ten} = 1   unless $ms{$name}{ten};
		for my $k (qw/hp mp at df ag/) {
			$ms{$name}{$k} = int($ms{$name}{$k} * (0.9 + rand(0.3) + (@partys - 2) * 0.1) ); # パーティー人数による強さ補正
			$ms{$name}{'m'.$k} = $ms{$name}{$k} unless $ms{$name}{'m'.$k};
		}
		$ms{$name}{name} = $name;
		$ms{$name}{color} = $npc_color;
		$ms{$name}{tmp}   ||= '';
		$ms{$name}{state} ||= '';
		
		$npc_com .= "$name,";
		push @members, $name;
	}
	chop $npc_com;
	$npc_com .= "があらわれた！";
}
sub add_monster {
	my $c = shift || int(rand( 2.5 + @partys * 0.6 )); # 出現数
	my $s = shift || 1; # 強さ補正
	my @alfas = ('A'..'H'); # 同じ名前のモンスターを識別するために名前の後につけるもの

	for my $i (0 .. $c) {
		my $no = @appears ? $appears[int(rand(@appears))] : int(rand(@monsters)); # 出現モンスター
		$no = 0 unless defined $monsters[$no]; # 存在しないNoだったら
		my $name = '@'.$monsters[$no]{name}.$alfas[$i];
		
		for my $k (@battle_datas) {
			$ms{$name}{$k} = defined $monsters[$no]{$k} ? $monsters[$no]{$k} : 0;
		}
		
		# 初期データセット(読み込んだデータにすでに値がある場合はそっちを優先)
		for my $k (qw/hp mp at df ag/) {
			$ms{$name}{$k} = int( $ms{$name}{$k} * (0.9 + rand(0.3) + (@partys - 2) * 0.1) * $s ); # パーティー人数による強さ補正
			$ms{$name}{'m'.$k} ||= $ms{$name}{$k};
		}
		$ms{$name}{name}  = $name;
		$ms{$name}{color} = $npc_color;
		$ms{$name}{hit}   ||= 95;
		$ms{$name}{ten}   ||= 1;
		$ms{$name}{tmp}   ||= '';
		$ms{$name}{state} ||= '';
		
		$npc_com .= "$name,";
		push @members, $name;
	}
	chop $npc_com;
	$npc_com .= "があらわれた！";
}



1; # 削除不可
