#=================================================
# SP交換 Created by Merino
#=================================================
# 場所名
$this_title = '願いの泉';

# NPC名
$npc_name   = '@女神';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/sp_change";

# 背景画像
$bgimg   = "$bgimgdir/sp_change.gif";


#=================================================
# はなす言葉
#=================================================
@words = (
	"スキルポイントはレベルが上がるごとに１ポイント増えていくのです",
	"スキルポイントを早く上げるコツは、何度も同じ職業に転職することです",
	"$mのスキルポイントは現在 $m{sp} ポイントです",
	"スキル習得を目指している場合は、ささげずにとっておくのですよ",
	"スキルポイントをささげるのです",
	"スキルポイントのお礼に、$mのステータスを上げてあげましょう",
	"一度ささげたスキルポイントを戻すことはできません",
	"スキルポイントは、その職業のスキルを習得するのに必要です",
);


#=================================================
# 追加アクション
#=================================================
push @actions, $e2j{mhp};
push @actions, $e2j{mmp};
push @actions, $e2j{at};
push @actions, $e2j{df};
push @actions, $e2j{ag};
$actions{ $e2j{mhp} } = sub{ &mhp }; 
$actions{ $e2j{mmp} } = sub{ &mmp }; 
$actions{ $e2j{at}  } = sub{ &at }; 
$actions{ $e2j{df}  } = sub{ &df }; 
$actions{ $e2j{ag}  } = sub{ &ag }; 


#=================================================
# ヘッダー表示
#=================================================
sub header_html {
	print qq|<div class="mes">【$this_title】 $jobs[$m{job}][1] $e2j{sp}<b>$m{sp}</b>|;
	for my $k (qw/lv mhp mmp at df ag/) {
		print qq| $e2j{$k}<b>$m{$k}</b>|;
	}
	print qq|</div>|;
}

sub mhp { &_chang_sp(shift, 2, 'mhp') }
sub mmp { &_chang_sp(shift, 2, 'mmp') }
sub at  { &_chang_sp(shift, 1, 'at') }
sub df  { &_chang_sp(shift, 1, 'df') }
sub ag  { &_chang_sp(shift, 1, 'ag') }
sub _chang_sp {
	my($sp, $up, $k) = @_;
	
	if ($sp < 1 || $sp =~ /[^0-9]/) {
		$mes = "$e2j{sp}をいくつささげますか？例＞『＠$e2j{hp}>1』SPを１ささげＨＰを上げる";
		return;
	}
	elsif ($sp > $m{sp}) {
		$mes = "ささげる$e2j{sp}が足りません";
		return;
	}
	
	my $v = $sp * $up;
	$m{sp} -= $sp;
	$m{$k} += $v;
	$npc_com = "$e2j{sp} $sp のかわりに $e2j{$k} を $v あたえましょう";
}



1; # 削除不可
