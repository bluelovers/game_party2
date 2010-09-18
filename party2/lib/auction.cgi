#=================================================
# 預かり所 Created by Merino
#=================================================
# 場所名
$this_title = 'オークション会場';

# NPC名
$npc_name   = '@ワイルド';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/auction";

# 背景画像
$bgimg   = "$bgimgdir/auction.gif";

# 送るの禁止アイテム(例＞'wea' => [1,2,3,4,5],)
%taboo_items = (
	'wea' => [], # 武器No
	'arm' => [], # 防具No
	'ite' => [], # 道具No
);

#=================================================
# ＠はなすの会話
#=================================================
@words = (
	"ここは$this_titleです。他のプレイヤーとアイテム交換やアイテム売買をする場所です。",
	"入札や出品のようなシステムはないです。自由に競りをしてください。",
	"相手が実際にそのアイテムや落札金を持っているのか「＠しらべる」で見ることができます。",
);


#=================================================
# 追加アクション
#=================================================
push @actions, 'おくる';
$actions{'おくる'} = sub{ &okuru }; 

#=================================================
# ＠おくる
#=================================================
sub okuru {
	my $target = shift;
	my($send, $name) = split /＠あいて&gt;/, $target;
	
#	if ($m{job_lv} < 1) {
#		$mes = "未転職の方は、送ることはできません";
#		return;
#	}

	if ($name) {
		my $yid = unpack 'H*', $name;
		unless (-d "$userdir/$yid") {
			$mes = "$nameというプレイヤーは存在しません";
			return;
		}
		my %p = &get_you_datas($yid, 1);
		if ($p{is_full}) {
			$mes = "$nameの預かり所がいっぱいです";
			return
		}
		
		if ($send =~ /^([0-9]+)\x20?G?$/) {
			my $send_money = int($1);
			if ($send_money > $m{money}) {
				$mes = "そんなにお金をもっていません";
				return;
			}
			elsif ($send_money <= 0) {
				$mes = "送金は最低でも 1 G以上です";
				return;
			}
			
			$m{money} -= $send_money;
			&send_money($name, $send_money, "$mからの送金");
			$npc_com = "$send_money Gを $name に送りました";
			return;
		}
		elsif ($m{wea} && $weas[$m{wea}][1] eq $send) {
			for my $taboo_item (@{ $taboo_items{wea} }) {
				if ($weas[$taboo_item][1] eq $weas[$m{wea}][1]) {
					$mes = "$weas[$m{wea}][1]は送ることができません";
					return;
				}
			}
			$npc_com = "$weas[$m{wea}][1]を$nameに送りました";
			&send_item($name, 1, $m{wea}, $m);
			$m{wea} = 0;
		}
		elsif ($m{arm} && $arms[$m{arm}][1] eq $send) {
			for my $taboo_item (@{ $taboo_items{arm} }) {
				if ($arms[$taboo_item][1] eq $arms[$m{arm}][1]) {
					$mes = "$arms[$m{arm}][1]は送ることができません";
					return;
				}
			}
			$npc_com = "$arms[$m{arm}][1]を$nameに送りました";
			&send_item($name, 2, $m{arm}, $m);
			$m{arm} = 0;
		}
		elsif ($m{ite} && $ites[$m{ite}][1] eq $send) {
			for my $taboo_item (@{ $taboo_items{ite} }) {
				if ($ites[$taboo_item][1] eq $ites[$m{ite}][1]) {
					$mes = "$ites[$m{ite}][1]は送ることができません";
					return;
				}
			}
			$npc_com = "$ites[$m{ite}][1]を$nameに送りました";
			&send_item($name, 3, $m{ite}, $m);
			$m{ite} = 0;
		}
		
		&get_depot_c;
		return;
	}
	
	$mes  = qq|どれを誰に送りますか？<br />$p|;
	$mes .= qq|<span onclick="text_set('＠おくる>$weas[$m{wea}][1]＠あいて')">$weas[$m{wea}][1]</span> / | if $m{wea};
	$mes .= qq|<span onclick="text_set('＠おくる>$arms[$m{arm}][1]＠あいて')">$arms[$m{arm}][1]</span> / | if $m{arm};
	$mes .= qq|<span onclick="text_set('＠おくる>$ites[$m{ite}][1]＠あいて')">$ites[$m{ite}][1]</span> / | if $m{ite};
	$mes .= qq|<span onclick="text_set('＠おくる>$m{money}G＠あいて')">$m{money}G</span> / |;
	$act_time = 0;
}



1; # 削除不可
