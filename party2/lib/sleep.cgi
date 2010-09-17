my $yid = unpack 'H*', $m{home};
if (!$m{home} || !-d "$userdir/$yid") { my $yhome = $m{home}; $m{home} = $m; &write_user; &error("$yhomeという家は見つかりません"); }
#=================================================
# 睡眠中 Created by Merino
#=================================================
# 場所名
$this_title = "$m{home}の家";

# ログに使うファイル(.cgi抜き)
$this_file  = "$userdir/$yid/home";

# 背景画像
$bgimg  = "";


#=================================================
# ヘッダー表示
#=================================================
$m{sleep} -= int($time - $m{ltime}) if $m{sleep} > 0;
sub header_html {
	if ($m{sleep} > 0) {
		my $wake_time  = sprintf("%d分%02d秒", int($m{sleep} / 60), int($m{sleep} % 60) );
		my $wake_html .= qq|<span id="wake_time">$wake_time</span>\n|;
		$wake_html    .= qq|<script type="text/javascript"><!--\n wake_time($m{sleep});\n// --></script>\n|;
		$wake_html    .= qq|<noscript>$wake_up_nokori</noscript>\n|;

		print qq|<form method="$method" action="$script_index"><input type="submit" value="＠ログアウト" class="button_s" /></form>|;
		print qq|<div class="mes">【$this_title】 お休み中「Zzz...」 目覚めるまで $wake_html</div>|;
	}
	else { # 目覚め
		$m{tired} = 0;
		$m{hp} = $m{mhp};
		$m{mp} = $m{mmp};
		$m{is_eat} = 0;
		$m{icon}   = "job/$m{job}_$m{sex}.gif";

		print qq|<div class="mes">【$this_title】 $mの$e2j{hp}$e2j{mp}$e2j{tired}が回復した！</div>|;
	}
}

# 行動はできない
sub set_action { return }


1; # 削除不可
