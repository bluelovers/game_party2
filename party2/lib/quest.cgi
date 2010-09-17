#=================================================
# 冒険準備・作成 Created by Merino
# type: 1:通常,2:ダンジョン,3:チャレンジ,4:闘技場,5:ギルド戦,6:封印戦
#=================================================
# 場所名
$this_title = '冒険中のパーティー';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/quest";

# 背景画像
$bgimg   = "$bgimgdir/quest.gif";

# パーティー名、闘技場名の最大文字数(半角)
$max_title = 50;

# 最大パーティー人数
$max_party = 4;

# 闘技場最大参加人数
$max_colosseum = 8;

# 闘技場最低賭け金(G)
$min_bet = 10;

# 進行スピード
%speeds = (
#	秒数	=> ['セレクト名', "画像ファイル"],
	12		=> ['さくさく', "$icondir/etc/speed_sakusaku.gif"],
	18		=> ['まったり', "$icondir/etc/speed_mattari.gif"],
	25		=> ['じっくり', "$icondir/etc/speed_jikkuri.gif"],
);


# 放置クエスト(ログの更新なし)の自動削除時間(秒)
$auto_delete_quest_time = 1800;


#=================================================
# 画面ヘッダー
#=================================================
sub header_html {
	my $my_at = $m{at} + $weas[$m{wea}][3];
	my $my_df = $m{df} + $arms[$m{arm}][3];
	my $my_ag = $m{ag} - $weas[$m{wea}][4] - $arms[$m{arm}][4];
	$my_ag = 0 if $my_ag < 0;
	print qq|<div class="mes">【$this_title】 $e2j{tired}：<b>$m{tired}</b>％ ゴールド：<b>$m{money}</b>G / $e2j{mhp}：<b>$m{hp}</b>/<b>$m{mhp}</b> / $e2j{mmp}：<b>$m{mp}</b>/<b>$m{mmp}</b>|;
	print qq| / $e2j{at}：<b>$my_at</b> / $e2j{df}：<b>$my_df</b> / $e2j{ag}：<b>$my_ag</b> /|;
	print qq| E：$weas[$m{wea}][1]| if $m{wea};
	print qq| E：$arms[$m{arm}][1]| if $m{arm};
	print qq| E：$ites[$m{ite}][1]| if $m{ite};
	print qq|</div>|;
	print qq|<div class="view">|;
	&quest_html;
	print qq|</div>|;
}

#=================================================
# クエスト(パーティー)一覧
#=================================================
sub quest_html {
	opendir my $dh, "$questdir" or &error("$questdirディレクトリが開けません");
	while (my $dir_name = readdir $dh) {
		next if $dir_name =~ /\./;
		
		# 放置クエスト削除(30分以上ログの更新なし)
		my($mtime) = (stat("$questdir/$dir_name/log.cgi"))[9];
		if ($time > $mtime + $auto_delete_quest_time) {
			&auto_delete_quest($dir_name);
			next;
		}

		open my $fh, "< $questdir/$dir_name/member.cgi";
		my $head_line = <$fh>;
		my($speed,$stage,$round,$leader,$p_name,$p_pass,$p_join,$win,$bet,$is_visit,$need_join,$type,$map,$py,$px,$event) = split /<>/, $head_line;
		my $count = 1;
		my $p = qq| <span onclick="text_set('＠しらべる>$leader ')"><img src="$icondir/etc/mark_leader.gif" alt="リーダー" />$leader</span> / |;
		while (my $line = <$fh>) {
			my($name,$laddr,$color) = split /<>/, $line;
			next if $name =~ /^@/;
			next if $leader eq $name;
			$p .= qq|<span onclick="text_set('＠しらべる>$name ')">$name</span> / |;
			++$count;
		}
		close $fh;
		
		my $party_data = qq|$p_name <img src="$speeds{$speed}[1]" alt="$speeds{$speed}[0]" /> |;
		$party_data .= $type eq '1' ? qq|$stages[$stage]|
					:  $type eq '2' ? qq|<img src="$icondir/etc/mark_dungeon.gif" alt="ダンジョン" />$dungeons[$stage]|
					:  $type eq '3' ? qq|<img src="$icondir/etc/mark_challenge.gif" alt="チャレンジ" />$challenges[$stage]|
					:  $type eq '4' ? qq|<img src="$icondir/etc/mark_arena.gif" alt="闘技場" /> 賭け金 <b>$bet</b>Ｇ|
					:  $type eq '5' ? qq|<img src="$icondir/etc/mark_guild.gif" alt="ギルド戦" />|
					:  '' ;
		$party_data .= qq| 【<b>$count</b>/<b>$p_join</b>】|;
		
		if ($need_join) {
			my($need_k, $need_v, $need_uo) = split /_/, $need_join;
			if ($need_k eq 'hp') {
				$party_data .= $need_uo eq 'u' ? "☆$e2j{hp}$need_v未満☆" : "★$e2j{hp}$need_v以上★";
			}
			elsif ($need_k eq 'joblv')  {
				if ($need_uo eq 'u') {
					if    ($need_v <= 3) { $party_data .= '☆初心者歓迎☆';   }
				}
				else {
					if    ($need_v >= 3)  { $party_data .= '★初心者お断り！★'; }
					elsif ($need_v >= 10) { $party_data .= '★熟練者のみ！★'; }
				}
			}
		}
		my $aikotoba = $p_pass ? '＠あいことば>' : ' ';
		if ($type eq '6') {
			print $count >= $p_join || $round > 1
				? qq|<span onclick="text_set('＠けんがく>$p_name')"><img src="$icondir/etc/vs_king.gif" alt="封印戦" /> $party_data</span>$p<hr size="1" />|
				: qq|<span onclick="text_set('＠さんか>$p_name')"><img src="$icondir/etc/vs_king.gif" alt="封印戦" /> $party_data</span>$p<hr size="1" />|;
		}
		elsif ($round > 0) {
			print !$is_visit
				? qq|<img src="$icondir/etc/playing.gif" alt="クエスト中" /> $party_data 見学× $p<hr size="1" />|
				: qq|<span onclick="text_set('＠けんがく>$p_name$aikotoba')"><img src="$icondir/etc/playing.gif" alt="クエスト中" /> $party_data</span>$p<hr size="1" />|;
		}
		elsif ($count >= $p_join) {
			print !$is_visit
				? qq|<img src="$icondir/etc/full.gif" alt="まんいん" /> $party_data 見学× $p<hr size="1" />|
				: qq|<span onclick="text_set('＠けんがく>$p_name$aikotoba')"><img src="$icondir/etc/full.gif" alt="まんいん" /> $party_data</span>$p<hr size="1" />|;
		}
		else {
			print qq|<span onclick="text_set('＠さんか>$p_name$aikotoba')"><img src="$icondir/etc/waitting.gif" alt="たいき中" /> $party_data</span>$p<hr size="1" />|;
		}
	}
	closedir $dh;
}
sub auto_delete_quest { # 放置自動削除
	my $dir_name = shift;
	open my $fh, "< $questdir/$dir_name/member.cgi";
	my $head_line = <$fh>;
	while (my $line = <$fh>) {
		my($name,$color) = (split /<>/, $line)[0,2];
		next if $color eq $npc_color;
		&regist_you_data($name, 'lib', '');
		&regist_you_data($name, 'sleep', 3600);
	}
	close $fh;
	&delete_directory("$questdir/$dir_name");
}

#=================================================
# 追加アクション
#=================================================
push @actions, 'つくる';
push @actions, 'さんか';
push @actions, 'けんがく';
$actions{'つくる'}   = sub{ &tsukuru }; 
$actions{'さんか'}   = sub{ &sanka }; 
$actions{'けんがく'} = sub{ &kengaku }; 
$actions{'パーティー'}   = sub{ &party }; 
$actions{'とうぎじょう'} = sub{ &tougijyou }; 
$actions{'ギルドバトル'} = sub{ &girudobatoru }; 
$actions{'ダンジョン'}   = sub{ &dungeon }; 
$actions{'チャレンジ'}   = sub{ &challenge }; 


#=================================================
# ＠つくる
#=================================================
sub tsukuru {
	# ステージ
	my $stage_select = qq|<select name="stage" class="select1">|;
	for my $i (0 .. 14) {
		$stage_select .= qq|<option value="$i">$stages[$i]</option>|;
		last if $i > $m{job_lv}+1;
	}
	$stage_select .= qq|</select>|;

	# ダンジョン
	my $dungeon_select = qq|<select name="stage" class="select1">|;
	for my $i (0 .. $#dungeons) {
		$dungeon_select .= qq|<option value="$i">$dungeons[$i]</option>|;
		last if ($i+1) * 2 >= $m{job_lv};
	}
	$dungeon_select .= qq|</select>|;
	
	# チャレンジ
	my $challenge_select = qq|<select name="stage" class="select1">|;
	for my $i (0 .. $#challenges) {
		$challenge_select .= qq|<option value="$i">$challenges[$i]</option>|;
		last if ($i+1) * 3 >= $m{job_lv};
	}
	$challenge_select .= qq|</select>|;

	# 対戦数(闘技場用)
	my $round_select = qq|<select name="win" class="select1">|;
	for my $i (1 .. 3) {
		$round_select .= qq|<option value="$i">$i回先勝</option>|;
	}
	$round_select .= qq|</select>|;
	
	# 冒険参加人数
	my $join_select = qq|<select name="p_join" class="select1">|;
	for my $i (1 .. $max_party-1) {
		$join_select .= qq|<option value="$i">$i人</option>|;
	}
	$join_select .= qq|<option value="$max_party" selected="selected">$max_party人</option>|;
	$join_select .= qq|</select>|;

	# 闘技場参加人数
	my $join_select2 = qq|<select name="p_join" class="select1">|;
	for my $i (2 .. $max_colosseum-1) {
		$join_select2 .= qq|<option value="$i">$i人</option>|;
	}
	$join_select2 .= qq|<option value="$max_colosseum" selected="selected">$max_colosseum人</option>|;
	$join_select2 .= qq|</select>|;

	# 進行速度
	my $speed_select = qq|<select name="speed" class="select1">|;
	for my $k (sort { $a <=> $b } keys %speeds) {
		$speed_select .= qq|<option value="$k">$speeds{$k}[0]</option>|;
	}
	$speed_select .= qq|</select>|;
	
	# 参加条件
	my $need_join = <<"EOM";
	<select name="need_join" class="select1">
		<option value="0">なし</option>
		<option value="joblv_3_u">初心者</option>
		<option value="joblv_3_o">中級者以上</option>
		<option value="joblv_10_o">上級者以上</option>
		<option value="hp_100_u">ＨＰ100未満</option>
		<option value="hp_100_o">ＨＰ100以上</option>
		<option value="hp_200_u">ＨＰ200未満</option>
		<option value="hp_200_o">ＨＰ200以上</option>
		<option value="hp_300_u">ＨＰ300未満</option>
		<option value="hp_300_o">ＨＰ300以上</option>
		<option value="hp_400_u">ＨＰ400未満</option>
		<option value="hp_400_o">ＨＰ400以上</option>
	</select>
EOM
	
	
	$mes = <<"EOM";
<table><tr><td valign="top">
<form method="$method" action="$script">
	<input type="hidden" name="comment" value="＠パーティー" />
	<input type="hidden" name="id" value="$id" /><input type="hidden" name="pass" value="$pass" />
	<table class="table1">
		<tr><td>パーティー名：</td><td><input type="text" name="p_name" class="text_box1" /></td></tr>
		<tr><td>進行速度：</td><td>$speed_select</td></tr>
		<tr><td>参加人数：</td><td>$join_select</td></tr>
		<tr><td>冒険場所：</td><td>$stage_select</td></tr>
		<tr><td>参加条件：</td><td>$need_join</td></tr>
		<tr><td>合言葉：</td><td><input type="text" name="p_pass" class="text_box_s" />　</td></tr>
		<tr><td>見学可：<input type="checkbox" name="is_visit" value="1" checked="checked"></td><td><input type="submit" value="＠パーティー" /></td></tr>
	</table>
</form>
EOM
	if ($m{job_lv} > 0) {
		$mes .= <<"EOM";
</td><td valign="top">
<form method="$method" action="$script">
	<input type="hidden" name="comment" value="＠ダンジョン" />
	<input type="hidden" name="id" value="$id" /><input type="hidden" name="pass" value="$pass" />
	<table class="table1">
		<tr><td>パーティー名：</td><td><input type="text" name="p_name" class="text_box1" /></td></tr>
		<tr><td>進行速度：</td><td>$speed_select</td></tr>
		<tr><td>参加人数：</td><td>$join_select</td></tr>
		<tr><td>冒険場所：</td><td>$dungeon_select</td></tr>
		<tr><td>参加条件：</td><td>$need_join</td></tr>
		<tr><td>合言葉：</td><td><input type="text" name="p_pass" class="text_box_s" />　</td></tr>
		<tr><td>見学可：<input type="checkbox" name="is_visit" value="1" checked="checked"></td><td><input type="submit" value="＠ダンジョン" /></td></tr>
	</table>
</form>
</td></tr><tr><td valign="top">
<form method="$method" action="$script">
	<input type="hidden" name="comment" value="＠チャレンジ" />
	<input type="hidden" name="id" value="$id"><input type="hidden" name="pass" value="$pass" />
	<table class="table1">
		<tr><td>チャレンジ名：</td><td><input type="text" name="p_name" class="text_box1" /></td></tr>
		<tr><td>進行速度：</td><td>$speed_select</td></tr>
		<tr><td>挑戦場所：</td><td>$challenge_select</td></tr>
		<tr><td>合言葉：</td><td><input type="text" name="p_pass" class="text_box_s" /></td></tr>
		<tr><td>見学可：<input type="checkbox" name="is_visit" value="1" checked="checked"></td><td><input type="submit" value="＠チャレンジ" /></td></tr>
	</table>
</form>
EOM
}
	$mes .= <<"EOM";
</td><td valign="top">
<form method="$method" action="$script">
	<input type="hidden" name="comment" value="＠とうぎじょう" />
	<input type="hidden" name="id" value="$id"><input type="hidden" name="pass" value="$pass" />
	<table class="table1">
		<tr><td>闘技場名：</td><td><input type="text" name="p_name" class="text_box1" /></td></tr>
		<tr><td>進行速度：</td><td>$speed_select</td></tr>
		<tr><td>参加人数：</td><td>$join_select2</td></tr>
		<tr><td>対戦場所：</td><td>$stage_select</td></tr>
		<tr><td>賭け金：</td><td><input type="text" name="bet" class="text_box_s" style="text-align: right;" value="$min_bet" />G</td></tr>
		<tr><td>対戦回数：</td><td>$round_select</td></tr>
		<tr><td>参加条件：</td><td>$need_join</td></tr>
		<tr><td>合言葉：</td><td><input type="text" name="p_pass" class="text_box_s" /></td></tr>
		<tr><td>見学可：<input type="checkbox" name="is_visit" value="1" checked="checked"></td><td><input type="submit" value="＠闘技場" /></td></tr>
	</table>
</form>
EOM
	if ($m{guild}) {
		$mes .= <<"EOM";
</td><td valign="top">
<form method="$method" action="$script">
	<input type="hidden" name="comment" value="＠ギルドバトル" />
	<input type="hidden" name="id" value="$id"><input type="hidden" name="pass" value="$pass" />
	<table class="table1">
		<tr><td>ギルド戦名：</td><td><input type="text" name="p_name" class="text_box1" /></td></tr>
		<tr><td>進行速度：</td><td>$speed_select</td></tr>
		<tr><td>参加人数：</td><td>$join_select2</td></tr>
		<tr><td>対戦場所：</td><td>$stage_select</td></tr>
		<tr><td>対戦回数：</td><td>$round_select</td></tr>
		<tr><td>参加条件：</td><td>$need_join</td></tr>
		<tr><td>合言葉：</td><td><input type="text" name="p_pass" class="text_box_s" /></td></tr>
		<tr><td>見学可：<input type="checkbox" name="is_visit" value="1" checked="checked"></td><td><input type="submit" value="＠ギルド戦" /></td></tr>
	</table>
</form>
EOM
	}
	$mes .= "</td></tr></table>";
}
#=================================================
# 入力チェック
#=================================================
sub check_create_quest {
	my($p_name) = @_;

	$mes = qq|<span onclick="text_set('＠ほーむ ')">$e2j{hp}を回復してください。「＠ほーむ」で家に帰り「＠ねる」で休んでください</span>|	if $m{hp} <= 0;
	$mes = qq|<span onclick="text_set('＠ほーむ ')">$e2j{tired}がたまっています。「＠ほーむ」で家に帰り「＠ねる」で休んでください</span>|	if $m{tired} >= 100;
	return if $mes;

	if ($p_name eq '闘技場') {
		$mes = "賭け金は最低でも $min_bet G必要です"	if $in{bet} < $min_bet;
		$mes = "賭け金は最低でも 1 G必要です"			if $in{bet} < 1;
		$mes = "賭け金が足りません"						if $in{bet} > $m{money};
		$mes = "賭け金が異常です"						if $in{bet} =~ /[^0-9]/;
		$in{bet} = int($in{bet});
	}
	elsif ($p_name eq 'ギルド戦') {
		if ($m{guild}) {
			my($gid,$gname,$gmaster,$gcolor,$gbgimg,$gmes,$gpoint) = &read_guild_data;
			$mes = "仲良しギルドはギルド戦をすることはできません" if $gcolor eq $default_color;
		}
		else {
			$mes = "ギルドに参加していません";
		}
	}
	return if $mes;
	
	# 参加条件	
	if ($in{need_join}) {
		my($need_key, $need_value, $need_uo) = split /_/, $in{need_join};
		$mes = "参加条件『ＨＰが$need_value未満』を満たしていません"		if $need_key eq 'hp'    && $need_uo eq 'u' && $m{mhp}    >= $need_value;
		$mes = "参加条件『ＨＰが$need_value以上』を満たしていません"		if $need_key eq 'hp'    && $need_uo eq 'o' && $m{mhp}    <  $need_value;
		$mes = "参加条件『転職回数が$need_value回未満』を満たしていません"	if $need_key eq 'joblv' && $need_uo eq 'u' && $m{job_lv} >= $need_value;
		$mes = "参加条件『転職回数が$need_value回以上』を満たしていません"	if $need_key eq 'joblv' && $need_uo eq 'o' && $m{job_lv} <  $need_value;
		return if $mes;
	}
	
	if ($p_name eq 'パーティー') {
		$mes = "参加人数が異常です"		if $in{p_join} < 1 || $in{p_join} > $max_party;
		$mes = "冒険場所が異常です"		if $in{stage}  < 0 || $in{stage} > $#stages || $in{stage} > $m{job_lv}+2;
	}
	elsif ($p_name eq 'ダンジョン') {
		$mes = "参加人数が異常です"		if $in{p_join} < 1 || $in{p_join} > $max_party;
		$mes = "冒険場所が異常です"		if $in{stage}  < 0 || $in{stage} > $#dungeons || $in{stage} * 2 > $m{job_lv}+1;
	}
	elsif ($p_name eq 'チャレンジ') {

	}
	else {
		$mes = "参加人数が異常です"		if $in{p_join} < 2 || $in{p_join} > $max_colosseum;
		$mes = "対戦回数が異常です"		if $in{win}    < 1 || $in{win} > 4;
		$mes = "対戦場所が異常です"		if $in{stage}  < 0 || $in{stage} > $#stages || $in{stage} > $m{job_lv}+2;
	}
	return if $mes;

	$in{is_visit} = 1 if $in{is_visit} =~ /[^01]/;
	$mes = "進行速度が異常です"		unless defined $speeds{$in{speed}};
	$mes = "$p_name名は半角$max_title文字までです"						if length($in{p_name}) > $max_title;
	$mes = "$p_name名に不正な空白が含まれています"						if $in{p_name} =~ /　|\s/;
	$mes = "$p_name名に不正な文字( ,;\"\'&<>\\\/@ )が含まれています"	if $in{p_name} =~ /[,;\"\'&<>\\\/@]/;
	$mes = "$p_name名に不正な文字( ＠ )が含まれています"				if $in{p_name} =~ /＠/;
	$mes = "$p_name名を決めてください"	unless $in{p_name};
}
#=================================================
# ＠パーティー
#=================================================
sub party {
	&check_create_quest('パーティー');
	return if $mes;

	my $quest_id = unpack 'H*', $in{p_name};
	$mes = "同じクエスト名($in{p_name})がすでに存在します" if -d "$questdir/$quest_id";
	return if $mes;
	
	# 新規パーティー作成
	mkdir "$questdir/$quest_id", $mkdir or &error("$questdir/$quest_idディレクトリが作成できません");
	open my $fh, "> $questdir/$quest_id/member.cgi" or &error("$questdir/$quest_id/member.cgiファイルが作成できません");
	print $fh "$in{speed}<>$in{stage}<>0<>$m<>$in{p_name}<>$in{p_pass}<>$in{p_join}<>0<>0<>$in{is_visit}<>$in{need_join}<>1<><>0<>0<><>\n";
	my $new_line = &get_battle_line($m{color},0);
	print $fh "$new_line\n";
	close $fh;
	chmod $chmod, "$questdir/$quest_id/member.cgi";
	
	open my $fh2, "> $questdir/$quest_id/log.cgi" or &error("$questdir/$quest_id/log.cgiファイルが作成できません");
	close $fh2;
	chmod $chmod, "$questdir/$quest_id/log.cgi";
	
	$m{lib}   = 'vs_monster';
	$m{quest} = $quest_id;
	
	$com = "<b>＠パーティー>$in{p_name}＠冒険場所>$stages[$in{stage}]＠参加人数>$in{p_join}人＠$speeds{$in{speed}}[0]";
 	if ($in{p_pass}) {
		$com .= "＠合言葉>必要";
	}
	else {
		$in{p_pass} = 'なし' ;
	}
	$com .= "</b>";
	&reload("$in{p_name}パーティーを作りました！<br />冒険場所：$stages[$in{stage}]，$speeds{$in{speed}}[0]，合言葉：$in{p_pass}，参加人数：$in{p_join}人");
	&leave_member($m);
}
#=================================================
# ＠ダンジョン
#=================================================
sub dungeon {
	&check_create_quest('ダンジョン');
	return if $mes;

	my $quest_id = unpack 'H*', $in{p_name};
	$mes = "同じクエスト名($in{p_name})がすでに存在します" if -d "$questdir/$quest_id";
	return if $mes;
	
	&get_dungeon_data;
	# 新規パーティー作成
	mkdir "$questdir/$quest_id", $mkdir or &error("$questdir/$quest_idディレクトリが作成できません");
	open my $fh, "> $questdir/$quest_id/member.cgi" or &error("$questdir/$quest_id/member.cgiファイルが作成できません");
	print $fh "$in{speed}<>$in{stage}<>0<>$m<>$in{p_name}<>$in{p_pass}<>$in{p_join}<>0<>0<>$in{is_visit}<>$in{need_join}<>2<>$in{map}<>$in{py}<>$in{px}<>S<>\n";
	my $new_line = &get_battle_line($m{color},0);
	print $fh "$new_line\n";
	close $fh;
	chmod $chmod, "$questdir/$quest_id/member.cgi";
	
	open my $fh2, "> $questdir/$quest_id/log.cgi" or &error("$questdir/$quest_id/log.cgiファイルが作成できません");
	close $fh2;
	chmod $chmod, "$questdir/$quest_id/log.cgi";
	
	$m{lib}   = 'vs_dungeon';
	$m{quest} = $quest_id;
	
	$com = "<b>＠ダンジョン>$in{p_name}＠冒険場所>$dungeons[$in{stage}]＠参加人数>$in{p_join}人＠$speeds{$in{speed}}[0]";
 	if ($in{p_pass}) {
		$com .= "＠合言葉>必要";
	}
	else {
		$in{p_pass} = 'なし' ;
	}
	$com .= "</b>";
	&reload("$in{p_name}パーティーを作りました！<br />冒険場所：$dungeons[$in{stage}]，$speeds{$in{speed}}[0]，合言葉：$in{p_pass}，参加人数：$in{p_join}人");
	&leave_member($m);
}
sub get_dungeon_data {
	# 冒険するマップをランダムで選択
	my @random_maps = ();
	opendir my $dh, "$mapdir/$in{stage}" or &error("$mapdir/$in{stage}ディレクトリが開けません");
	while (my $file_name = readdir $dh) {
		next if $file_name =~ /^\./;
		next if $file_name =~ /_/;
		push @random_maps, $file_name;
	}
	closedir $dh;
	
	$in{map} = $random_maps[int rand @random_maps];
	$in{map} =~ s/^(.+)\..+$/$1/; # 拡張子を除く
	
	&error("$mapdir/$in{stage}/$in{map}.cgiダンジョンデータファイルが見つかりません") unless -f "$mapdir/$in{stage}/$in{map}.cgi";
	require "$mapdir/$in{stage}/$in{map}.cgi";
	for my $y (0..$#maps) {
		for my $x (0..$#maps) {
			if ($maps[$y][$x] eq 'S') {
				$in{py} = $y;
				$in{px} = $x;
				return;
			}
		}
	}
	
	&error("$in{map} スタート地点が見つかりません");
}

#=================================================
# ＠チャレンジ
#=================================================
sub challenge {
	$mes = "冒険場所が異常です"		if $in{stage}  < 0 || $in{stage} > $#challenges || $in{stage} * 2 > $m{job_lv}+1;
	$mes = "レベルアップをストックした状態で挑戦することはできません" if $m{lv} < 99 && $m{exp} >= $m{lv} * $m{lv} * 10;
	return if $mes;

	require "$challengedir/$in{stage}.cgi";

	$in{p_join}    = $k{p_join};
	$in{need_join} = $k{need_join};

	&check_create_quest('チャレンジ');
	return if $mes;

	my $quest_id = unpack 'H*', $in{p_name};
	$mes = "同じクエスト名($in{p_name})がすでに存在します" if -d "$questdir/$quest_id";
	return if $mes;
	
	# 最高記録を取得
	my $max_round = &get_max_round($in{stage});

	# 新規パーティー作成
	mkdir "$questdir/$quest_id", $mkdir or &error("$questdir/$quest_idディレクトリが作成できません");
	open my $fh, "> $questdir/$quest_id/member.cgi" or &error("$questdir/$quest_id/member.cgiファイルが作成できません");
	print $fh "$in{speed}<>$in{stage}<>0<>$m<>$in{p_name}<>$in{p_pass}<>$in{p_join}<>$max_round<>0<>$in{is_visit}<>$in{need_join}<>3<><>0<>0<><>\n";
	my $new_line = &get_battle_line($m{color},0);
	print $fh "$new_line\n";
	close $fh;
	chmod $chmod, "$questdir/$quest_id/member.cgi";
	
	open my $fh2, "> $questdir/$quest_id/log.cgi" or &error("$questdir/$quest_id/log.cgiファイルが作成できません");
	close $fh2;
	chmod $chmod, "$questdir/$quest_id/log.cgi";
	
	$m{lib}   = 'vs_challenge';
	$m{quest} = $quest_id;
	
	$com = "<b>＠チャレンジ>$in{p_name}＠冒険場所>$challenges[$in{stage}]＠参加人数>$in{p_join}人＠$speeds{$in{speed}}[0]";
 	if ($in{p_pass}) {
		$com .= "＠合言葉>必要";
	}
	else {
		$in{p_pass} = 'なし' ;
	}
	$com .= "</b>";
	&reload("$challenges[$in{stage}] に挑戦します！<br />$speeds{$in{speed}}[0]，合言葉：$in{p_pass}，参加人数：$in{p_join}人");
	&leave_member($m);
}
sub get_max_round {
	my $stage = shift;
	
	open my $fh, "< $logdir/challenge$stage.cgi" or &error("$logdir/challenge$stage.cgiファイルが読み込めません");
	my $line = <$fh>;
	close $fh;
	my($max_round) = (split /<>/, $line)[0];

	return $max_round;
}

#=================================================
# ＠とうぎじょう
#=================================================
sub tougijyou {
	&check_create_quest('闘技場');
	return if $mes;

	my $quest_id = unpack 'H*', $in{p_name};
	$mes = "同じクエスト名($in{p_name})がすでに存在します" if -d "$questdir/$quest_id";
	return if $mes;
	
	# 新規闘技場作成
	mkdir "$questdir/$quest_id", $mkdir or &error("$questdir/$quest_idディレクトリが作成できません");
	open my $fh, "> $questdir/$quest_id/member.cgi" or &error("$questdir/$quest_id/member.cgiファイルが作成できません");
	print $fh "$in{speed}<>$in{stage}<>0<>$m<>$in{p_name}<>$in{p_pass}<>$in{p_join}<>$in{win}<>$in{bet}<>$in{is_visit}<>$in{need_join}<>4<><>0<>0<><>\n";
	my $new_line = &get_battle_line($default_color, 1);
	print $fh "$new_line\n";
	close $fh;
	chmod $chmod, "$questdir/$quest_id/member.cgi";
	
	for my $k (qw/log bet win/) {
		open my $fh2, "> $questdir/$quest_id/$k.cgi" or &error("$questdir/$quest_id/$k.cgiファイルが作成できません");
		close $fh2;
		chmod $chmod, "$questdir/$quest_id/$k.cgi";
	}
	&add_bet($quest_id, $in{bet});
	
	$m{money} -= $in{bet};
	$m{lib}   = 'vs_player';
	$m{quest} = $quest_id;
	
	$com = "<b>＠闘技場>$in{p_name}＠対戦場所>$stages[$in{stage}]＠賭け金>$in{bet} G＠参加人数>$in{p_join}人＠$speeds{$in{speed}}[0]";
 	if ($in{p_pass}) {
		$com .= "＠あいことば>必要";
	}
	else {
		$in{p_pass} = 'なし' ;
	}
	$com .= "</b>";
	&reload("闘技場「$in{p_name}」を作りました！<br />対戦場所：$stages[$in{stage}]，賭け金：$in{bet} G，$speeds{$in{speed}}[0]，合言葉：$in{p_pass}，参加人数：$in{p_join}人");
	&leave_member($m);
}
#=================================================
# ＠ギルドバトル
#=================================================
sub girudobatoru {
	&check_create_quest('ギルド戦');
	return if $mes;
	
	my $quest_id = unpack 'H*', $in{p_name};
	$mes = "同じクエスト名($in{p_name})がすでに存在します" if -d "$questdir/$quest_id";
	return if $mes;

	my($gid,$gname,$gmaster,$gcolor,$gbgimg,$gmes,$gpoint) = &read_guild_data;
	# 新規闘技場作成
	mkdir "$questdir/$quest_id", $mkdir or &error("$questdir/$quest_idディレクトリが作成できません");
	open my $fh, "> $questdir/$quest_id/member.cgi" or &error("$questdir/$quest_id/member.cgiファイルが作成できません");
	print $fh "$in{speed}<>$in{stage}<>0<>$m<>$in{p_name}<>$in{p_pass}<>$in{p_join}<>$in{win}<>0<>$in{is_visit}<>$in{need_join}<>5<><>0<>0<><>\n";
	my $new_line = &get_battle_line($gcolor, 1);
	print $fh "$new_line\n";
	close $fh;
	chmod $chmod, "$questdir/$quest_id/member.cgi";
	
	for my $k (qw/log bet win guild/) {
		open my $fh2, "> $questdir/$quest_id/$k.cgi" or &error("$questdir/$quest_id/$k.cgiファイルが作成できません");
		close $fh2;
		chmod $chmod, "$questdir/$quest_id/$k.cgi";
	}
	&add_bet($quest_id, 2);
	
	open my $fh3, "> $questdir/$quest_id/guild.cgi" or &error("$questdir/$quest_id/guild.cgiファイルが作成できません");
	print $fh3 "$gcolor<>$m{guild}<>\n";
	close $fh3;
	chmod $chmod, "$questdir/$quest_id/guild.cgi";
	
	$m{lib}   = 'vs_guild';
	$m{quest} = $quest_id;
	
	$com = "<b>＠ギルド戦>$in{p_name}＠対戦場所>$stages[$in{stage}]＠参加人数>$in{p_join}人＠$speeds{$in{speed}}[0]";
 	if ($in{p_pass}) {
		$com .= "＠あいことば>必要";
	}
	else {
		$in{p_pass} = 'なし' ;
	}
	$com .= "</b>";
	&reload("ギルド戦「$in{p_name}」を作りました！<br />対戦場所：$stages[$in{stage}]，$speeds{$in{speed}}[0]，合言葉：$in{p_pass}，参加人数：$in{p_join}人");
	&leave_member($m);
}
#=================================================
# ＠さんか
#=================================================
sub sanka {
	my $target = shift;

	$mes = qq|<span onclick="text_set('＠ほーむ ')">$e2j{hp}を回復してください。「＠ほーむ」で家に帰り「＠ねる」で休んでください</span>|	if $m{hp} <= 0;
	$mes = qq|<span onclick="text_set('＠ほーむ ')">$e2j{tired}がたまっています。「＠ほーむ」で家に帰り「＠ねる」で休んでください</span>|	if $m{tired} >= 100;
	return if $mes;

	unless ($target) {
		$mes = "どのクエストに参加しますか？";
		return;
	}
	
	my($p_name, $join_pass) = split /＠あいことば&gt;/, $target;
	my $quest_id = unpack 'H*', $p_name;
	$com =~ s/(.+)＠あいことば&gt;(.+)/$1/; # 発言した＠あいことば～を削除

	if ($p_name && -d "$questdir/$quest_id") {
		&add_member($quest_id,$join_pass);
	}
	else {
		$mes = "参加しようとしたクエストは、解散してしまったようです";
	}
}

#=================================================
# ＠さんか処理
#=================================================
sub add_member {
	my($quest_id,$join_pass) = @_;
	
	my @lines = ();
	open my $fh, "+< $questdir/$quest_id/member.cgi" or &error("$questdir/$quest_id/member.cgiファイルが作成できません");
	eval { flock $fh, 2; };
	my $head_line = <$fh>;
	my($speed,$stage,$round,$leader,$p_name,$p_pass,$p_join,$win,$bet,$is_visit,$need_join,$type,$map,$py,$px,$event) = split /<>/, $head_line;
	$mes = "$p_nameに参加するための賭け金が足りません"	if $bet > $m{money};
	$mes = "$p_nameに参加するための合言葉が違います"	if $p_pass ne '' && $p_pass ne $join_pass;
	$mes = "クエスト途中から参加することはできません"	if $round > 1 || ($round > 0 && $type ne '6'); # 封印戦以外
	return if $mes;
	
	if ($need_join) {
		my($need_key, $need_value, $need_uo) = split /_/, $need_join;
		$mes = "参加条件『ＨＰが$need_value未満』を満たしていません"		if $need_key eq 'hp'    && $need_uo eq 'u' && $m{mhp}    >= $need_value;
		$mes = "参加条件『ＨＰが$need_value以上』を満たしていません"		if $need_key eq 'hp'    && $need_uo eq 'o' && $m{mhp}    <  $need_value;
		$mes = "参加条件『転職回数が$need_value回未満』を満たしていません"	if $need_key eq 'joblv' && $need_uo eq 'u' && $m{job_lv} >= $need_value;
		$mes = "参加条件『転職回数が$need_value回以上』を満たしていません"	if $need_key eq 'joblv' && $need_uo eq 'o' && $m{job_lv} <  $need_value;
		return if $mes;
	}

	my $color = '';
	if ($type eq '5') { # ギルド戦
		$color = &_check_guild_battle($quest_id);
		return if $mes || !$color;
	}
	elsif ($type eq '3' && $m{lv} < 99 && $m{exp} >= $m{lv} * $m{lv} * 10) { # チャレンジ
		$mes = "レベルアップをストックした状態で参加することはできません";
		return;
	}
	
	push @lines, $head_line;

	my $count = $type eq '6' ? 1 : 0; # 封印戦？
	my %same_colors = ();
	while (my $line = <$fh>) {
		my($name,$laddr,$gcolor) = (split /<>/, $line)[0..2];
		if ($name eq $m) {
			$mes = "同じ名前のプレイヤーがすでに参加しています";
			return;
		}
		elsif ($addr eq $laddr) {
			$mes = "ＩＰアドレスが同じプレイヤーがすでに参加しています。";
#			$mes .= "<br />多重登録容疑で追放騎士団に追加申\請されました。";
#			&write_news(qq|<span class="damage">$nameと$mが多重登録の疑いで追放申\請されました</span>|);
#			$m{wt} = $time;
#			&add_exile($m,    "【多重登録容疑】$nameと同じIPアドレス");
#			&add_exile($name, "【多重登録容疑】$mと同じIPアドレス");
			return;
		}
		++$same_colors{$gcolor};
		++$count unless $name =~ /^@/;
		push @lines, $line;
	}
	if ($count >= $p_join) {
		$mes = "$p_nameは定員がいっぱいで参加することができません";
		return;
	}
	elsif ($type eq '5' && $same_colors{ $color } >= 4) { # ギルド戦
		$mes = "同じギルドメンバー５人以上は参加することができません";
		return;
	}
	
	# 参加条件OK
	($color) ||= (split /<>/, $lines[1])[2];
	my $new_line = &get_battle_line($color,$type);
	push @lines, "$new_line\n";
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	if    ($type eq '1') {
		$m{lib} = 'vs_monster';
		&reload("$p_nameのパーティーに参加します");
	}
	elsif ($type eq '2') {
		$m{lib} = 'vs_dungeon';
		&reload("$p_nameのパーティーに参加します");
	}
	elsif ($type eq '3') {
		$m{lib} = 'vs_challenge';
		&reload("$p_nameに参加します");
	}
	elsif ($type eq '4') { # 闘技場
		&add_bet($quest_id, $bet);
		$m{money} -= $bet;
		$m{lib}    = 'vs_player';
		$com      .="賭け金 $bet Gを支払いました";
		&reload("賭け金 $bet Gを支払い $p_nameの闘技場に参加します");
	}
	elsif ($type eq '5') { # ギルド戦
		&add_bet($quest_id, 1);
		$m{lib}    = 'vs_guild';
		&reload("$p_nameのギルド戦に参加します");
	}
	elsif ($type eq '6') { # 封印戦
		$m{lib} = 'vs_king';
		$m{tired} += 20;
		&reload("$p_nameの封印戦に参加します");
	}
	$m{quest} = $quest_id;
	&leave_member($m);
}
# ギルド戦参加条件チェック
sub _check_guild_battle {
	my $quest_id = shift;
	
	if ($m{guild}) {
		my($gid,$gname,$gmaster,$gcolor,$gbgimg,$gmes,$gpoint) = &read_guild_data;
		if ($gcolor eq $default_color) {
			$mes = "仲良しギルドはギルド戦をすることはできません";
		}
		else {
			open my $fh, ">> $questdir/$quest_id/guild.cgi" or &error("$questdir/$quest_id/guild.cgiファイルが開けません");
			print $fh "$gcolor<>$m{guild}<>\n";
			close $fh;
			return $gcolor;
		}
	}
	else {
		$mes = "ギルドに参加していません";
	}
	
	return;
}

#=================================================
# ＠けんがく
#=================================================
sub kengaku {
	my $target = shift;

	unless ($target) {
		$mes = "どのクエストを見学しますか？";
		return;
	}
	
	my($p_name, $join_pass) = split /＠あいことば&gt;/, $target;
	my $quest_id = unpack 'H*', $p_name;
	$com =~ s/(.+)＠あいことば&gt;(.+)/$1/; # 発言した＠あいことば～を削除

	if ($p_name && -d "$questdir/$quest_id") {
		open my $fh, "< $questdir/$quest_id/member.cgi" or &error("$questdir/$quest_id/member.cgiファイルが読み込めません");
		my $head_line = <$fh>;
		close $fh;

		my($speed,$stage,$round,$leader,$p_name,$p_pass,$p_join,$win,$bet,$is_visit,$need_join,$type,$map,$py,$px,$event) = split /<>/, $head_line;
		if (!$is_visit) {
			$mes = "$p_nameの見学はできません";
			return;
		}
		elsif ($p_pass ne '' && $p_pass ne $join_pass) {
			$mes = "$p_nameを見学するための合言葉が違います";
			return;
		}
		
		$m{lib} = $type eq '1' ? 'vs_monster'
				: $type eq '2' ? 'vs_dungeon'
				: $type eq '3' ? 'vs_challenge'
				: $type eq '4' ? 'vs_player'
				: $type eq '5' ? 'vs_guild'
				: $type eq '6' ? 'vs_king'
				: '';
		$m{quest} = $quest_id;
		$mes = "$p_nameを見学します";
		&reload("$p_nameを見学します");
		&leave_member($m);
	}
	else {
		$mes = "見学しようとしたクエストは、解散してしまったようです";
	}
}


#=================================================
# バトル用データ作成 @battle_datasの値をセット
#=================================================
sub get_battle_line {
	my($color,$type) = @_;
	my %p = %m;
	
	$m{is_get} = 0;  # 宝取得フラグをリセット
	$m{event}  = ''; # イベントフラグをリセット
	$p{color} = $type eq '4' || !defined($color) || $color eq $npc_color ? $default_color : $color; # 闘技場かカラー未定義か敵色か
	
	# %mにはないKey
	$p{get_exp}   = $m{lv} + $m{job_lv};
	$p{get_money} = int($m{lv} * 0.5);
	$p{ten} = 1;
	$p{hit} = 95;
	
	$p{mat} = $m{at};
	$p{mdf} = $m{df};
	$p{mag} = $m{ag};
	$p{at}  = $m{at} + $weas[$m{wea}][3];
	$p{df}  = $m{df} + $arms[$m{arm}][3];
	$p{ag}  = $m{ag} - $weas[$m{wea}][4] - $arms[$m{arm}][4];
	%p = &{ $ites[$p{ite}][4] }(%p) if $ites[$p{ite}][3] eq '4'; # 装飾品(戦闘開始時、死亡時、いてつくはどうなど &reset_statusの時)

	my $line = '';
	for my $k (@battle_datas) {
		$line .= "$p{$k}<>";
	}
	return $line;
}


1; # 削除不可
