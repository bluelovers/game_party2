#=================================================
# ジョブマスター Created by Merino
#=================================================
$m{lib} = 'home'; # 戻るボタンを押したら強制的に家に戻る

sub read_member { return }
sub set_action  { return }

#=================================================
sub html {
	print qq|<form method="$method" action="$script">|;
	print qq|<input type="hidden" name="id" value="$id" /><input type="hidden" name="pass" value="$pass" />|;
	print qq|<input type="submit" value="戻る" /></form>|;
	
	my $yid = unpack 'H*', $m{home};
	my %jobs_data = ();
	my $count = 0;
	open my $fh, "< $userdir/$yid/job_master.cgi" or &error("$userdir/$yid/job_master.cgiファイルが読み込めません");
	while (my $line = <$fh>) {
		my($job_no, $job_sex, $job_point, $is_master) = split /<>/, $line;
		$jobs_data{$job_no} = [$job_sex, $job_point, $is_master];
		$count += $is_master ? 1 : 0.5;
	}
	close $fh;
	
	my $comp_par = int($count / $#jobs * 100);
	$comp_par = 100 if $comp_par > 100;

	print qq|<h2>$m{home}のジョブマスター率《<b>$comp_par</b>％》</h2><table class="table1"><tr>|;
	for my $i (1..$#jobs) {
		if (defined $jobs_data{$i}) {
			print qq|<td align="center">|;
			print $jobs_data{$i}[2] ? qq|<div style="color: #FF0;">★SP$jobs_data{$i}[1]</div>| : qq|<br />|;
			print qq|<img src="$icondir/job/${i}_$jobs_data{$i}[0].gif" alt="$jobs[$i][1]" /><br />$jobs[$i][1]</td>|;
		}
		else {
			print qq|<td align="center" style="color: #666;"><br /><img src="$icondir/chr/098.gif" /><br />$jobs[$i][1]</td>|;
		}
		print qq|</tr><tr>| if $i % 10 == 0;
	}
	
	my $mod = int(10 - $#jobs % 10);
	print qq|<td>　</td>| for (1..$mod);
	print qq|</tr></table>|;
}


1; # 削除不可
