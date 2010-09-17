require "./lib/_casino.cgi";
#=================================================
# ドッペル Created by Merino
#=================================================

@cards = ('★','●','◆','♪','■','▲','†','▼');

#=================================================
# 戦闘用アクションセット(プレイヤー用)
#=================================================
sub add_casino_action {
	return if $ms{$m}{action};
	for my $i (0..$now_bet) {
		push @actions, $cards[$i];
		$actions{$cards[$i]} = sub{ &mark($cards[$i]) };
		last if $i >= $#cards;
	}
}

#=================================================
# メンバー出力
#=================================================
sub member_html {
	my $member_html = '';
	$member_html .= qq|<div style="background: url($bgimg) #333 repeat-x left bottom;"><table><tr>|;
	for my $name (@members) {
		$member_html .= qq|<td onclick="text_set('>$name ')" align="center" valign="bottom"><span style="color: $ms{$name}{color}; font-size: 11px; background-color: #333;">|;
		$member_html .= qq|$ms{$name}{action}<br />| if $ms{$name}{action};
		$member_html .= $round <= 0 || $m eq $name ? qq|$ms{$name}{card}| : qq|？| if $ms{$name}{card};
		$member_html .= qq|<br />|;
		$member_html .= qq|<img src="$icondir/etc/mark_leader.gif" />| if $leader eq $name;
		$member_html .= qq|$name</span><br /><img src="$icondir/$ms{$name}{icon}" alt="$name" /></td>|;
	}
	$member_html .=  qq|</tr></table></div>|;
	return $member_html;
}

#=================================================
# ＠★～▼
#=================================================
sub mark {
	return if $ms{$m}{action};
	my $mark = shift or return;
	
	$com =~ s/＠.+?(\x20|　)//g; # マークを削除
	if ($ms{$m}{card}) {
		$com.=qq|<span class="st_up">$mがカードを変えました！</span>|;
	}
	else {
		$com.=qq|<span class="st_up">$mがカードを決めました！</span>|;
		&give_coin($bet);
	}
	$ms{$m}{card} = $mark;
	&next_round;
}

#=================================================
# ＠かいし
#=================================================
sub kaishi {
	if (@members <= 1) {
		$mes = "対戦する相手がいません";
		return;
	}
	elsif ($leader ne $m) {
		$mes = "＠かいし をすることができるのはリーダーのみです";
		return;
	}
	
	# 初期化
	for my $name (@members) {
		$ms{$name}{action} = '';
		$ms{$name}{card}   = '';
	}
	
	$now_bet = @members; # 人数によって選べるカード数が変わる
	++$round;
	$npc_com .= "<b>ゲーム開始！！</b>";
	&auto_reload;
}

#=================================================
# 全員のアクションをチェック
#=================================================
sub next_round {
	return if $round <= 0;

	# 全員カードが決まったら
	&battle if &is_all_select;
}
# ------------------
# 全員行動済み？
sub is_all_select {
	for my $name (@members) {
		next if $ms{$name}{action};
		return 0 if $ms{$name}{card} eq '';
	}
	return 1;
}

#=================================================
# 勝負
#=================================================
sub battle {
	# 賞金
	my $get_coin = &get_coin;
	return if $get_coin <= 0;

	my @winners = ();
	for my $name (@members) {
		next if $ms{$name}{action}; # 待機中の人はスルー
		next if $leader eq $name; # 親はスルー
		next if $ms{$leader}{card} ne $ms{$name}{card}; # 違うカードの人はスルー
		push @winners, $name;
	}
	if (@winners >= 1) { # 子の勝ち
		my $s_coin = int($get_coin / @winners);
		for my $winner (@winners) {
			my %p = &get_you_datas($winner);
			&regist_you_data($winner, 'cas_c', ++$p{cas_c});
			&regist_you_data($winner, 'coin', $p{coin}+$s_coin);
		}
		
		if (@winners > 1) {
			my $winners = join "、", @winners;
			$npc_com .= qq|ドッペル！！…$leaderのカードは【$ms{$leader}{card}】同じカードの人は $winners！よって、<span class="get">勝者の $winners たちそれぞれにｶｼﾞﾉｺｲﾝ <span class="damage">$s_coin</span> 枚がおくられます</span><br />|;
		}
		else {
			$npc_com .= qq|ドッペル！！…$leaderのカードは【$ms{$leader}{card}】同じカードの人は <b>$winners[0]</b>！よって、<span class="get">勝者の <b>$winners[0]</b> にｶｼﾞﾉｺｲﾝ <span class="damage">$s_coin</span> 枚がおくられます</span><br />|;
		}
		
		&reload_member();
		$leader = $winners[int rand @winners];
		$npc_com .= "$p_nameのリーダーが$leaderになりました";
	}
	else { # 親の勝ち
		my %p = &get_you_datas($leader);
		&regist_you_data($winner, 'cas_c', $p{cas_c}++);
		&regist_you_data($leader, 'coin', $p{coin}+$get_coin);

		$npc_com .= qq|ドッペル！！…$leaderのカードは【$ms{$leader}{card}】同じカードの人はいません！よって、<span class="get">勝者の <b>$leader</b> にｶｼﾞﾉｺｲﾝ <span class="damage">$get_coin</span> 枚がおくられます</span>|;
		&reload_member($leader);
	}
	
	$round = 0;
}


1; # 削除不可
