require "./lib/_casino.cgi";
#=================================================
# ハイロウ Created by Merino
#=================================================
# カード小～大(追加/変更/削除可能)
@cards = ('Ａ','２','３','４','５','６','７','８','９','10','Ｊ','Ｑ','Ｋ');

#=================================================
# アクションワード
#=================================================
sub add_casino_action {
	return if $round <= 0;
	if ($now_bet < $max_bet && $m{coin} >= $now_bet) {
		push @actions, ('つづける');
		$actions{'つづける'} = sub{ &tsuzukeru };
	}

	push @actions, 'ハイ';
	$actions{'ハイ'} = sub{ &high };

	if (@members > 2) {
		push @actions, 'ロウ';
		$actions{'ロウ'} = sub{ &low };
	}
	
	push @actions, 'おりる';
	$actions{'おりる'}  = sub{ &oriru };
}

#=================================================
# メンバー出力
#=================================================
sub member_html {
	my $member_html = '';
	$member_html .= qq|<div style="background: url($bgimg) #333 repeat-x left bottom;"><table><tr>|;
	for my $name (@members) {
		$member_html .= qq|<td onclick="text_set('>$name ')" align="center" valign="bottom"><span style="color: $ms{$name}{color}; font-size: 11px; background-color: #333;">|;
		if ($round < 1) {
			$member_html .= qq|$ms{$name}{action}<br />$cards[$ms{$name}{card}]|;
		}
		else {
			$member_html .= $ms{$name}{action} =~ /つづける|待機中/ || $m eq $name ? qq|$ms{$name}{action}| : qq|？？？| if $ms{$name}{action};
			$member_html .= qq|<br />|;
			$member_html .= $ms{$name}{action} =~ /待機中/ || $m eq $name ? qq|$cards[$ms{$name}{card}]| : qq|？|;
		}
		$member_html .= qq|<br />$name</span><br /><img src="$icondir/$ms{$name}{icon}" alt="$name" /></td>|;
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
	$npc_com .= "ゲーム開始！！";
	&auto_reload;
}

#=================================================
# ＠つづける
#=================================================
sub tsuzukeru {
	if ($ms{$m}{action}) {
		$mes = "すでに「＠$ms{$m}{action}」を宣言しています";
		return;
	}

	$ms{$m}{action} = 'つづける';
	&give_coin($now_bet);
	&next_round;
}
#=================================================
# ＠ハイ＠ロウ
#=================================================
sub high { &_call('ハイ'); }
sub low  { &_call('ロウ'); }	
sub _call {
	my $call = shift;

	if ($ms{$m}{action}) {
		$mes = "すでに「＠$ms{$m}{action}」を宣言しています";
		return;
	}

	$com =~ s/＠(.+?)(\x20|　)/＠？？？$2/; # マークを削除
	$ms{$m}{action} = $call;
	&give_coin($now_bet);
	&next_round;
}

#=================================================
# ＠おりる
#=================================================
sub oriru {
	if ($ms{$m}{action}) {
		$mes = "すでに「＠$ms{$m}{action}」を宣言しています";
		return;
	}

	$com =~ s/＠(.+?)(\x20|　)/＠？？？$2/; # マークを削除
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
		'ハイ'		=> 0,
		'ロウ'		=> 0,
		'つづける'	=> 0,
		'おりる'	=> 0,
	);

	my $count = 0;
	for my $name (@members) {
		next if $ms{$name}{action} eq '';
		++$as{$ms{$name}{action}};
		++$count;
	}

	if ($count eq @members) { # 全員アクション済み
		if ($m{coin} <= 0 || $now_bet >= $max_bet || ($as{'ハイ'} + $as{'ロウ'}) >= (@members - $as{'おりる'}) * 0.5) { # コインがなくなった or 最大レート or 半分勝負
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

	# ハイの人とロウの人のグループ分けで勝敗
	my $higher   = '';
	my $lowher   = '';
	my $max_card = -1;
	my $min_card = $#cards+1;
	for my $name (@members) {
		if ($ms{$name}{action} eq 'ハイ') {
			if ($ms{$name}{card} > $max_card) {
				$higher   = $name;
				$max_card = $ms{$name}{card};
			}
		}
		elsif ($ms{$name}{action} eq 'ロウ') {
			if ($ms{$name}{card} < $min_card) {
				$lower    = $name;
				$min_card = $ms{$name}{card};
			}
		}
	}
	
	my @winners = ($higher, $lower);
	if (@members > 2 && $higher && $lower) { # ２人以上 賞金２分割
		$get_coin = int($get_coin * 0.5);
		@winners = ($higher, $lower);
		$npc_com .= qq|ハイを宣言したカードの中で一番強いカードは【$cards[$max_card]】！よって、<span class="get">勝者の $higher にｶｼﾞﾉｺｲﾝ <span class="damage">$get_coin</span> 枚がおくられます</span>|;
		$npc_com .= qq|<br />ロウを宣言したカードの中で一番弱いカードは【$cards[$min_card]】！よって、<span class="get">勝者の $lower にｶｼﾞﾉｺｲﾝ <span class="damage">$get_coin</span> 枚がおくられます</span>|;
	}
	elsif ($higher) {
		@winners = ($higher);
		$npc_com .= qq|ハイを宣言したカードの中で一番強いカードは【$cards[$max_card]】！よって、<span class="get">勝者の $higher にｶｼﾞﾉｺｲﾝ <span class="damage">$get_coin</span> 枚がおくられます</span>|;
	}
	elsif ($lower) {
		@winners = ($lower);
		$npc_com .= qq|ロウを宣言したカードの中で一番弱いカードは【$cards[$min_card]】！よって、<span class="get">勝者の $lower にｶｼﾞﾉｺｲﾝ <span class="damage">$get_coin</span> 枚がおくられます</span>|;
	}
	else {
		$npc_com .= qq|全員おりてしまったので…今回のゲームはお流れとなります|;
		&reload_member($winners[0]);
	}
	
	for my $winner (@winners) {
		my $yid = unpack 'H*', $winner;
		if (-f "$userdir/$yid/user.cgi") {
			my %p = &get_you_datas($yid, 1);
			&regist_you_data($winner, 'cas_c', ++$p{cas_c});
			&regist_you_data($winner, 'coin', $p{coin}+$get_coin);
		}
	}

	$round   = 0;
	$now_bet = $bet;
	&reload_member($winners[0]);
}



1; # 削除不可
