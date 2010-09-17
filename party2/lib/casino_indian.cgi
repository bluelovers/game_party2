require "./lib/_casino.cgi";
#=================================================
# インディアンポーカー Created by Merino
#=================================================

@cards = ('Ａ','２','３','４','５','６','７','８','９','10','Ｊ','Ｑ','Ｋ');

#=================================================
# 戦闘用アクションセット(プレイヤー用)
#=================================================
sub add_casino_action {
	return if $round <= 0;
	push @actions, ('つづける','しょうぶ','おりる',);
	$actions{'つづける'} = sub{ &tsuzukeru };
	$actions{'しょうぶ'} = sub{ &shoubu };
	$actions{'おりる'}   = sub{ &oriru };
}

#=================================================
# メンバー出力
#=================================================
sub member_html {
	my $member_html = '';
	$member_html .= qq|<div style="background: url($bgimg) #333 repeat-x left bottom;"><table><tr>|;
	for my $name (@members) {
		$member_html .= qq|<td onclick="text_set('>$name ')" align="center" valign="bottom"><span style="color: $ms{$name}{color}; font-size: 11px; background-color: #333;">|;
		$member_html .= qq|$ms{$name}{action}| if $ms{$name}{action};
		$member_html .= $m ne $name || $ms{$name}{action} =~ /^おりる|待機中/ ? qq|<br />$cards[$ms{$name}{card}]<br />| : qq|<br />？<br />|;
		$member_html .= qq|$name</span><br />|;
		$member_html .= $ms{$name}{action} =~ /^おりる|待機中/ ? qq|<img src="$icondir/chr/099.gif" alt="$name" /></td>| : qq|<img src="$icondir/$ms{$name}{icon}" alt="$name" /></td>|;
	}
	$member_html .=  qq|</tr></table></div>|;
	return $member_html;
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
	
	my $max_card = $#cards;
	my @card_nos = (0..$max_card);
	
	# カードを配る
	for my $name (@members) {
		$ms{$name}{action} = '';
		$ms{$name}{card} = splice(@card_nos, int rand @card_nos, 1);
	}

	++$round;
	$npc_com .= "インディア～ンポカー！！開始！";
	&auto_reload;
}

#=================================================
# ＠しょうぶ
#=================================================
sub shoubu {
	if ($ms{$m}{action}) {
		$mes = "すでに「＠$ms{$m}{action}」を宣言しています";
		return;
	}
	$ms{$m}{action} = 'しょうぶ';
	&give_coin($now_bet);
	&next_round;
}
#=================================================
# ＠つづける
#=================================================
sub tsuzukeru {
	if ($ms{$m}{action}) {
		$mes = "すでに「＠$ms{$m}{action}」を宣言しています";
		return;
	}
	elsif ($m{coin} < $now_bet) { # ｺｲﾝが足らない場合は強制勝負
		&shoubu;
	}
	else {
		$ms{$m}{action} = 'つづける';
		&give_coin($now_bet);
		&next_round;
	}
}

#=================================================
# ＠おりる
#=================================================
sub oriru {
	if ($ms{$m}{action}) {
		$mes = "すでに「＠$ms{$m}{action}」を宣言しています";
		return;
	}
	$ms{$m}{action} = 'おりる';
	&give_coin($now_bet);
	&next_round;
}

#=================================================
# 全員のアクションをチェックして、勝負か次のラウンドへ
#=================================================
sub next_round {
	return if $round <= 0;
	my %as = (
		'しょうぶ' => 0,
		'つづける' => 0,
		'おりる'   => 0,
	);

	my $count = 0;
	for my $name (@members) {
		next if $ms{$name}{action} eq '';
		++$as{$ms{$name}{action}};
		++$count;
	}

	if ($as{'おりる'} eq @members-1) { # １人以外全員おり
		&battle;
	}
	elsif ($count eq @members) { # 全員アクション済み
		if ($m{coin} <= 0 || $now_bet >= $max_bet || $as{'しょうぶ'} >= (@members - $as{'おりる'}) * 0.5) { # コインがなくなった or 最大レート or 全員勝負
			&battle;
		}
		else { # 次のラウンドへ
			for my $name (@members) {
				next if $ms{$name}{action} eq 'おりる';
				next if $ms{$name}{action} eq '待機中';
				$ms{$name}{action} = '';
			}
			$round++;
			$now_bet += $bet;
			$npc_com.=qq|<span class="lv_up">★ゲーム続行★レートが上がりました♪現在のレートは <span class="damage">$now_bet</span> 枚です</span>|;
		}
	}
}

#=================================================
# 勝負
#=================================================
sub battle {
	# 賞金
	my $get_coin = &get_coin;
	return if $get_coin <= 0;

	my $winner = '';
	my $max_card = -1;
	for my $name (@members) {
		next if $ms{$name}{action} eq 'おりる'; # おりている人はスルー
		next if $ms{$name}{action} eq '待機中'; # 待機中の人はスルー
		if ($ms{$name}{card} > $max_card) {
			$winner = $name;
			$max_card = $ms{$name}{card};
		}
	}

	if ($winner) {
		my %p = &get_you_datas($winner);
		&regist_you_data($winner, 'cas_c', ++$p{cas_c});
		&regist_you_data($winner, 'coin', $p{coin}+$get_coin);
		$npc_com .= qq|勝負！…<span class="get">勝者は $winner さんです★ ｶｼﾞﾉｺｲﾝ <span class="damage">$get_coin</span> 枚がおくられます</span>|;
	}
	else { # 勝利者脱走
		$npc_com .= qq|勝者はいませんでした…|;
	}

	$round   = 0;
	$now_bet = $bet;
	&reload_member($winner);
}




1; # 削除不可
