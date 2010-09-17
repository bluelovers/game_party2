my @orbs = split //, $m{orb};
#=================================================
# 復活の祭壇 Created by Merino
#=================================================
# 場所名
$this_title = "復活の祭壇";

# NPC名
$npc_name   = '@巫女';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/reborn";

# 背景画像
$bgimg   = "$bgimgdir/reborn.gif";

# 
@sales = (66..69);

# オーブのフォントカラー
%colors = (
	'G' => 'gold',
	's' => 'silver',
	'r' => 'red',
	'b' => 'blue',
	'g' => 'green',
	'y' => 'yellow',
	'p' => 'purple',
);



#=================================================
# はなす言葉
#=================================================
if (@orbs >= 6) {
	@words = (
		"私達。私達。この日をどんなに。この日をどんなに。待ちわびたことでしょう",
		"さぁ、祈りましょう。さぁ、祈りましょう",
	);
}
else {
	@words = (
		"私達は。私達は。卵を守っています。卵を守っています",
		"世界中にちらばる６つのオーブをささげたとき....",
		"伝説の不死鳥ラーミァはよみがえりましょう",
		"手に入れられるオーブは曜日によって変わるようです",
	);
}


if ($m{orb} =~ /G/) {
	# 追加アクション
	push @actions, 'ねがう';
	$actions{ 'ねがう' } = sub{ &negau };
	
	@words = (
		"このアイテムを冒険中に使えば、今まで見たことのない世界へと行くことができます",
		"未知の世界に連れて行くことができるのは、アイテムを使った一回だけです",
		"未知の世界にへは、その場にいた仲間と一緒に行くことができます",
	);
}
else {
	# 追加アクション
	push @actions, 'いのる';
	$actions{ 'いのる' } = sub{ &inoru };
}

#=================================================
# ステータス表示
#=================================================
sub header_html {
	my $orbs = '';
	for my $orb (@orbs) {
		$orbs .= qq|<font color="$colors{$orb}">●</font>|;
	}
	print qq|<div class="mes">【$this_title】$orbs</div>|;
}

#=================================================
# ＠いのる
#=================================================
sub inoru {
	if (@orbs < 6) {
		$mes = "オーブが足りません。オーブが足りません。オーブを６つ集めてください";
	}
	elsif (@orbs >= 6) {
		my $r_time = $time + 1800;
		open my $fh, ">> ${this_file}_member.cgi" or &error("${this_file}_member.cgiファイルが開けません");
		print $fh "$r_time<>0<>ﾗｰﾐｧ@<>0<>chr/051.gif<>$npc_color<>\n";
		close $fh;
		$npc_com .= "時は来たれり。今こそ目覚める時。大空はお前のもの。舞い上がれ空高く！";
		$m{orb} = 'G';
	}
}


#=================================================
# ＠ねがう
#=================================================
sub negau {
	return if $m{orb} !~ /G/;
	
	my $target = shift;
	
	my $p = qq|<table class="table1">|;
	for my $i (@sales) {
		if ($ites[$i][1] eq $target) {
			if ($m{ite}) {
				&send_item($m, 3, $i);
				$npc_com = "$ites[$i][1] を$mの預かり所に送っておきました。冒険中に使うことで未知の世界へと行くことができるでしょう";
			}
			else {
				$m{ite} = $i;
				$npc_com = "$ites[$i][1] ですね。冒険中に使うことで未知の世界へと行くことができるでしょう";
				require "./lib/_add_collection.cgi";
				&add_collection;
			}
			$m{orb} = '';
			return;
		}
		$p .= qq|<tr onclick="text_set('＠ねがう>$ites[$i][1] ')"><td>$ites[$i][1]</td></tr>|;
	}
	$p  .= qq|</table>|;

	$mes = qq|ﾗｰﾐｧ「ふむ。$mというのか…。我をよみがえらせてくれた礼として、<br />わが力が宿ったアイテムを１つだけあたえよう…」<br />$p|;
	$act_time = 0;
}


1; # 削除不可
