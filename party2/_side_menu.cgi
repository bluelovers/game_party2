#================================================
# サイドメニュー・ヘッダー・フッター Created by Merino
#================================================
sub side_menu {
	my($contents) = shift;

	my $yid = $ENV{'QUERY_STRING'} ? '?'.$ENV{'QUERY_STRING'} : '';
	my $title_line = $title_img ? qq|<img src="$title_img" alt="$title">| : $title;
	
	print <<"EOM";
<div align="center">
<div id="page">
	<div id="header">
		<table width="100%">
		<tr><td>
		<h1><a href="$script_index">$title_line</a></h1>
		<script type="text/javascript" src="$htmldir/random_icons.js"></script>
		</td><td align="right" valign="bottom">
		</td></tr></table>
	</div>
	<div id="navigation">
		<div class="menu_button"><a href="$script_index$yid">＠トップ<div class="text_small">トップページ</div></a></div>
		<div class="menu_button"><a href="new_entry.cgi$yid">＠新規登録<div class="text_small">説明書の初心者ﾌﾟﾚｲﾁｬｰﾄ必読</div></a></div>
		<div class="menu_button"><a href="http://www19.atwiki.jp/atparty2/">＠説明書<div class="text_small">＠パーティーIIについて</div></a></div>
		<div class="menu_button"><a href="news.cgi$yid">＠ニュース<div class="text_small">最近の出来事</div></a></div>
		<div class="menu_button"><a href="contest.cgi$yid">＠フォトコン<div class="text_small">みんなが撮ったｽｸｰﾌﾟ映像</div></a></div>
		<div class="menu_button"><a href="$htmldir/player_list.html">＠ﾌﾟﾚｲﾔｰ一覧<div class="text_small">転職回数、レベル順</div></a></div>
		<div class="menu_button"><a href="guild_list.cgi$yid">＠ギルド勢力<div class="text_small">各ギルドとそのメンバー</div></a></div>
		<div class="menu_button"><a href="challenge.cgi$yid">＠世界記録<div class="text_small">＠チャレンジの最高記録保持者</div></a></div>
		<div class="menu_button"><a href="ranking.cgi$yid">＠ランキング<div class="text_small">活躍しているトッププレイヤー</div></a></div>
		<div class="menu_button"><a href="legend.cgi$yid">＠伝説のﾌﾟﾚｲﾔｰ<div class="text_small">コンプリートプレイヤー</div></a></div>
		<div class="menu_button"><a href="job_ranking.cgi$yid">＠職業ランキング<div class="text_small">人気の職業は！？</div></a></div>
		<div class="menu_button"><a href="rescue.cgi$yid">＠救出処理<div class="text_small">バグ救出</div></a></div>
		<!-- div class="menu_button"><a href="delete.cgi$yid">＠削除処理<div class="text_small">データ削除</div></a></div -->
		<div class="menu_button"><a href="$home">＠ＨＯＭＥ<div class="text_small">ホームページへ</div></a></div>
	</div>
	<div id="contents">
		$contents
	</div>
EOM
}


#================================================
# footer
#================================================
sub footer {
	print qq|<div id="footer">|;
	print qq|+ ＠パーティーII Ver$VERSION <a href="http://cgi-sweets.com/" target="_blank">CGI-Sweets</a> <a href="http://amaraku.net/" target="_blank">Ama楽.net</a>|; # 著作表示:削除・非表示 禁止!!
	print qq|$copyright +</div></div></div></body></html>|;
}

1;
