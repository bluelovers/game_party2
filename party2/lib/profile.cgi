#=================================================
# プロフィール Created by Merino
#=================================================
# ◎追加/削除/変更/並び替え可
# プロフィール表示するもの。左の英字は同じじゃなければ何でも良い
@profiles = (
	['name',		'名前'],
	['sex',			'性別'],
	['blood',		'血液型'],
	['birthday',	'誕生日'],
	['age',			'年齢'],
	['job',			'職業'],
	['address',		'住んでいる所'],
	['hobby',		'趣味'],
	['boom',		'マイブーム'],
	['site',		'オススメサイト'],
	['dream',		'夢/目標'],
	['character',	'性格・特徴'],
	['like',		'好きなもの'],
	['dislike',		'嫌いなもの'],
	['like_food',	'好きな食べ物'],
	['dislike_food','嫌いな食べ物'],
	['goal',		'このゲームの目標'],
	['login',		'ログイン時間'],
	['boast',		'自慢'],
	['reference',	'このサイトを知ったきっかけ'],
	['message',		'何か一言'],
);

#=================================================

$yid = unpack 'H*', $m{home};
$this_file = "$userdir/$yid/profile.cgi";
$com = '';

sub read_member { return }
sub set_action  { return }

#=================================================
sub html {
	if ($m eq $m{home}) {
		$in{mode} eq 'write_exe' ? &write_exe : &write_form;
	}
	else {
		&view_profile;
	}
}

sub view_profile {
	unless ($is_top_profile) {
		$m{lib} = 'home'; # 戻るボタンを押したら強制的に家に戻る
		print qq|<form method="$method" action="$script">|;
		print qq|<input type="hidden" name="id" value="$id" /><input type="hidden" name="pass" value="$pass" />|;
		print qq|<input type="submit" value="戻る" /></form>|;
	}

	open my $fh, "< $this_file" or &error("$this_fileファイルが読み込めません");
	my $line = <$fh>;
	close $fh;
	
	my %datas = ();
	for my $hash (split /<>/, $line) {
		my($k, $v) = split /;/, $hash;
		$datas{$k} = $v;
	}
	
	print qq|<h2>$m{home}のプロフィール</h2><table class="table2" cellpadding="3" width="440">|;
	for my $profile (@profiles) {
		next if $datas{$profile->[0]} eq '';
		
		# http://ならオートリンク
		$datas{$profile->[0]} =~ s/([^=^\"]|^)(https?\:[\w\.\~\-\/\?\&\=\@\;\#\:\%]+)/$1<a href=\"link.cgi?$2\" target=\"_blank\">$2<\/a>/g;
		
		print qq|<tr><th align="left">$profile->[1]</th></tr><tr><td>$datas{$profile->[0]}</td></tr>|;
	}
	print qq|</table>|;
}


#================================================
sub write_form {
	my %datas = ();
	open my $fh, "< $this_file" or &error("$this_fileファイルが読み込めません");
	my $line = <$fh>;
	close $fh;
	for my $hash (split /<>/, $line) {
		my($k, $v) = split /;/, $hash;
		$datas{$k} = $v;
	}

	print qq|$mのプロフィール：全角80文字(半角160)まで<br />|;
	print qq|<form method="$method" action="$script"><input type="hidden" name="mode" value="write_exe">|;
	print qq|<table class="table2" cellpadding="3" width="440">|;
	for my $profile (@profiles) {
		print qq|<tr><th align="left">$profile->[1]</th></tr><tr><td><input type="text" name="$profile->[0]" value="$datas{$profile->[0]}" class="text_box_b"></td></tr>|; 
	}
	print qq|</table><input type="hidden" name="id" value="$id"><input type="hidden" name="pass" value="$pass">|;
	print qq|<p><input type="submit" value="変更する" class="button1"></p></form>|;
}

sub write_exe {
	my %datas = ();
	open my $fh, "+< $this_file" or &error("$this_fileファイルが開けません");
	eval { flock $fh, 2; };
	my $line = <$fh>;
	for my $hash (split /<>/, $line) {
		my($k, $v) = split /;/, $hash;
		$datas{$k} = $v;
	}
	
	my $is_rewrite = 0;
	for my $profile (@profiles) {
		unless ($in{$profile->[0]} eq $datas{$profile->[0]}) {
			&error("$profile->[1] に不正な文字( \;<> )が含まれています")	if $in{$profile->[0]} =~ /[;<>]/;
			&error("$profile->[1] は全角80(半角160)文字以内です")			if length($in{$profile->[0]}) > 160;
			$datas{$profile->[0]} = $in{$profile->[0]};
			$is_rewrite = 1;
		}
	}
	if ($is_rewrite) {
		my $new_line = '';
		while ( my($k, $v) = each %datas ) {
			$new_line .= "$k;$v<>";
		}
		
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh $new_line;
		close $fh;
		
		print 'プロフィールを変更しました';
	}
	else {
		close $fh;
	}
	
	&view_profile;
}


1; # 削除不可
