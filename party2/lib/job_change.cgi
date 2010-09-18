#=================================================
# 転職所 Created by Merino
#=================================================
# 場所名
$this_title = 'ダーマの神殿';

# NPC名
$npc_name   = '@神官';

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/job_change";

# 背景画像
$bgimg   = "$bgimgdir/job_change.gif";

# 道具を消費することで転職可能な職業(ここに記入されていない場合は道具を消費しない)
%lost_item_jobs = (
	'賢者'			=> 1,
	'勇者'			=> 1,
	'魔王'			=> 1,
	'ものまね士'	=> 1,
	'結界士'		=> 1,
	'バンパイア'		=> 1,
	'スライム'			=> 1,
	'ハグレメタル'		=> 1,
	'ドラゴン'		=> 1,
	'アサシン'			=> 1,
	'チョコボ'			=> 1,
	'モーグリ'			=> 1,
	'ギャンブラー'		=> 1,
	'ソルジャー'		=> 1,
	'堕天使'		=> 1,
	'魔銃士'		=> 1,
	'妖精'			=> 1,
	'ミニデーモン'		=> 1,
	'エルフ'			=> 1,
	'ダークエルフ'		=> 1,
	'スライムライダー'		=> 1,
	'ドラゴンライダー'	=> 1,
	'ネクロマンサー'		=> 1,
	'バットマスター'		=> 1,
	'キノコマスター'		=> 1,
	'オバケマスター'		=> 1,
	'ケモノマスター'		=> 1,
	'ドクロマスター'		=> 1,
	'バブルマスター'		=> 1,
	'コロヒーロー'		=> 1,
	'プチヒーロー'		=> 1,
	'チョコボライダー'	=> 1,
	'算術士'		=> 1,
);

#=================================================
# ＠はなすの会話
#=================================================
@words = (
	"よくきた！このダーマ神殿ではお主の職業を変えることができるぞ",
	"ふむふむ。どの職業にしようかまよっているのじゃな",
	"転職をすると今のステータスが半分になってしまうぞ",
	"職業は重要じゃからよーく考えるのじゃよ",
	"転職アイテムを持っていれば、特別な職業に転職することができるぞ",
	"$mは男前だから剣士なんかどうじゃろ？",
	"$mはお金が欲しいと思っているな？それなら商人になりなさい",
	"$mはモンスターと仲良くなりたいと思っているな？それなら魔物使いになりなさい",
	"$mは癒し系になりたいと思っているな？それなら僧侶になりなさい",
	"$mは相手やお宝が気になっているな？それなら盗賊になりなさい",
	"$mは誰かにイタズラしたいと思っているな？それなら遊び人になりなさい",
	"$mはモコモコしたものが好きじゃな？それなら羊飼いになりなさい",
	"$mは最終的に$jobs[int(rand(@jobs))+1][1]を目指すと良いじゃろぉ",
	"$mに一番しっくりくるのは$jobs[int(rand(@jobs))+1][1]じゃな",
	"転職条件が厳しいからといって強いとは限らんぞ",
	"どんなにスキルを覚えても使いこなせなきゃ意味がないぞ",
	"スキルを早く覚えたい場合は早期転職をオススメしておる",
	"ステータスを上げたい場合は、成長率の高い職業を選び、なるべく遅く転職するのがコツじゃ",
	"今の職業のスキルを全てマスターしてから転職しても、おそくはないはずじゃ",
	"$mの今の転職回数は…$m{job_lv}回。ふむ、なかなかじゃのぉ",
	"転職回数は冒険者の熟練度でもある。３回転職をすると初心者卒業レベルかのぉ",
	"転職回数は冒険者の熟練度でもある。10回以上の転職者は、この世界を熟知しているベテランじゃのぉ",
);

sub shiraberu_npc {
	$mes = "モンスター撃退数 $m{kill_m}回<br />プレイヤー撃退数 $m{kill_p}回<br />封印解いた回数 $m{mao_c}回<br />封印した回数 $m{hero_c}回<br />カジノ勝利数 $m{cas_c}回";
}


#=================================================
# 画面一番上に表示
#=================================================
sub header_html {
	print qq|<div class="mes">【$this_title】 $jobs[$m{job}][1] $e2j{sp} <b>$m{sp}</b>|;
	print qq| / $jobs[$m{old_job}][1] $e2j{sp} <b>$m{old_sp}</b>| if $m{old_job};
	for my $k (qw/lv mhp mmp at df ag/) {
		print qq| / $e2j{$k} <b>$m{$k}</b>|;
	}
	print qq| / E：$ites[$m{ite}][1]| if $m{ite};
	print qq|</div>|;
}

#=================================================
# 追加アクション
#=================================================
push @actions, 'てんしょく';
$actions{'てんしょく'} = sub{ &tensyoku }; 

#=================================================
# ＠てんしょく
#=================================================
sub tensyoku {
	my $target = shift;
	
	if ($m{lv} < 20) {
		$mes = "転職するにはレベルが２０以上必要じゃ";
		return;
	}
	
	my $p = '';
	for my $i (0 .. $#jobs) {
		next unless &{ $jobs[$i][7] }; # 転職条件がある場合、満たしているか
		if ($target eq $jobs[$i][1]) {
			# 道具消費転職(賢者だけ特別処理)
			if (defined $lost_item_jobs{$target}) {
				# アイテム消費しない条件
				unless (&_is_need_job($i) || (($target eq '賢者' || $target eq 'ギャンブラー') && ($jobs[$m{job}][1] eq '遊び人' || $jobs[$m{old_job}][1] eq '遊び人' )) ) {
					$npc_com .= "$ites[$m{ite}][1]を使いました！ ";
					$m{ite} = 0;
				}
			}
			
			&write_memory("$jobs[$m{job}][1]から$jobs[$i][1]に転職");
			&job_change($i);

			$npc_com .= "$mよ！$targetとなり新たな道を歩むが良い";
			&regist_guild_data('point', 50) if $m{guild};
			return;
		}

		$p .= qq|<span onclick="text_set('＠てんしょく>$jobs[$i][1] ')">$jobs[$i][1]</span> / |;
	}
	$mes = qq|どの職業に転職するのじゃ？<br />$p|;
	$act_time = 0;
}
# ------------------
# 転職処理
sub job_change {
	my $job = shift;
	
	&add_all_job_master;
	my $mastered_point = &add_job_master($job);
	
	# 違う職業に転職した場合の処理(同じ職業に転職した場合は、レベルとステータスを下げるだけ)
	unless ($m{job} eq $job) {
		my $buf_sp  = $m{old_sp};
		$m{old_sp}  = $m{sp};
		$m{sp}      = $job eq $m{old_job} ? $buf_sp : $mastered_point; # 前職業に転職する場合は前職業のSP
		$m{old_job} = $m{job};
		$m{job}     = $job;
		$m{icon}    = "job/$m{job}_$m{sex}.gif";
	}
	
	# ステータスダウン
	for my $k (qw/mhp mmp at df ag/) {
		$m{$k} = int($m{$k} * 0.5); 
		$m{$k} = 10 if $m{$k} < 10;
	}
	
	$m{hp} = $m{mhp};
	$m{mp} = $m{mmp};
	$m{lv}  = 1;
	$m{exp} = 0;
	$m{job_lv}++;
	
}

# 習得ジョブ
sub add_job_master {
	my $job = shift;

	require "./lib/_skill.cgi";
	my @skills = &{ 'skill_'.$m{job} };

	my $mastered_job_sp = 0;
	my $mastered_count = 0;
	my $is_find = 0;
	my @lines = ();
	open my $fh, "+< $userdir/$id/job_master.cgi" or &error("$userdir/$id/job_master.cgiファイルが開けません");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($job_no, $job_sex, $job_point, $is_master) = split /<>/, $line;

		if ($m{job} eq $job_no) {
			$is_find = 1;
			if (!$is_master && $m{sp} >= $skills[-1][0]) {
				$is_master = 1;
				$com .= qq|<span class="comp">$mは <b>$jobs[$m{job}][1]</b> をマスターしました！</span>|;
				&write_memory("<b>★ $jobs[$m{job}][1] Job Master! ★</b>");
			}
			push @lines, "$m{job}<>$m{sex}<>$m{sp}<>$is_master<>\n";
		}
		elsif ($job eq $job_no && $is_master) {
			$mastered_job_sp = $job_point;
			push @lines, $line;
		}
		else {
			push @lines, $line;
		}
		$mastered_count++ if $is_master;
	}
	unless ($is_find) {
		my $is_master = 0;
		
		if ($m{sp} >= $skills[-1][0]) {
			$is_master = 1;
			$com .= qq|<span class="comp">$mは <b>$jobs[$m{job}][1]</b> をマスターしました！</span>|;
			&write_memory("<b>★ $jobs[$m{job}][1] Job Master! ★</b>");
		}
		push @lines, "$m{job}<>$m{sex}<>$m{sp}<>$is_master<>\n";
	}
	@lines = map { $_->[0] } sort { $a->[1] <=> $b->[1] } map { [$_, split /<>/] } @lines;
	
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
	
	# 全ジョブコンプリート
	if ($mastered_count eq $#jobs-1 && !-f "$userdir/$id/comp_job_flag.cgi") { 
		open my $fh2, "> $userdir/$id/comp_job_flag.cgi" or &error("$userdir/$id/comp_job_flag.cgiファイルが開けません");
		close $fh2;
		
		&write_legend('comp_job');
		&write_memory(qq|<span class="comp">All Job Complete!!</span>|);
		&write_news(qq|<span class="comp">$mが全ての職業をマスターしました！</span>|);
		$com .= qq|<div class="comp">$mは <b>全ジョブ</b> をコンプリートしました！</div>|;
	}
	
	return $mastered_job_sp;
}

# 全体の転職の傾向
sub add_all_job_master {
	my $is_find = 0;
	
	my $add_point = int($m{lv} * 0.5);
	
	my @lines = ();
	open my $fh, "+< $logdir/job_ranking.cgi" or &error("$logdir/job_ranking.cgiファイルが開けません");
	eval { flock $fh, 2; };
	my $totale_point = <$fh>;
	$totale_point =~ tr/\x0D\x0A//d;
	$totale_point += $add_point;
	while (my $line = <$fh>) {
		my($job_no, $men_point, $female_point, $job_point) = split /<>/, $line;
		if ($m{job} eq $job_no) {
			$is_find = 1;
			
			if ($m{sex} eq 'm') {
				$men_point += $add_point;
			}
			else {
				$female_point += $add_point;
			}
			$job_point += $add_point;
		}
		push @lines, "$job_no<>$men_point<>$female_point<>$job_point<>\n";
	}
	unless ($is_find) {
		my $job_sex = $m{sex} eq 'm' ? "$add_point<>0" : "0<>$add_point";
		push @lines, "$m{job}<>$job_sex<>$add_point<>\n";
	}

	@lines = map { $_->[0] } sort { $b->[4] <=> $a->[4] } map { [$_, split /<>/] } @lines;
	unshift @lines, "$totale_point\n";
	
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}


1; # 削除不可
