#=================================================
# �R���N�V�����ǉ� Created by Merino
# collction.cgi,depot.cgi,weapon.cgi,armor.cgi,item.cgi�Ŏg�p
#=================================================
# �g����:�R���N�V�����ɒǉ��������^�C�~���O�ŉ���s
# require './lib/_add_collection.cgi';
# &add_collection;

#================================================
# �����̃R���N�V�����f�[�^�擾 + ���������̕����R���N�V�����ɂȂ��Ȃ�ǉ�
#=================================================
sub add_collection {
	my @kinds = ('', 'wea', 'arm', 'ite');
	my $kind = 1;
	my $is_rewrite = 0;
	my @lines = ();
	
	open my $fh, "+< $userdir/$id/collection.cgi" or &error("�R���N�V�����t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		$line =~ tr/\x0D\x0A//d; # \n���s�폜
		
		# �ǉ�
		if ($m{ $kinds[$kind] } && $line !~ /,$m{ $kinds[$kind] },/) {
			$is_rewrite = 1;
			$line .= "$m{ $kinds[$kind] },";
			$npc_com .= "<br />" if $npc_com;
			$npc_com .= $kind eq '1' ? "<b>$weas[$m{wea}][1]"
					  : $kind eq '2' ? "<b>$arms[$m{arm}][1]"
					  :                "<b>$ites[$m{ite}][1]"
					  ;
			$npc_com .= '���V�����A�C�e���}�ӂɓo�^����܂���</b>';
			
			# sort
			$line  = join ",", sort { $a <=> $b } split /,/, $line;
			$line .= ",";
		}
		
		push @lines, "$line\n";
		++$kind;
	}
	if ($is_rewrite) {
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
	}
	close $fh;
	
	return @lines;
}

#================================================
# �ǂݍ��݂̂�(����̃R���N�V�����f�[�^������Ƃ��Ȃ�)
#=================================================
sub read_collection {
	my $yid = shift || $id;
	
	my @lines = ();
	open my $fh, "< $userdir/$yid/collection.cgi" or &error("$userdir/$yid/collection.cgi�t�@�C�����ǂݍ��߂܂���");
	while (my $line = <$fh>) {
		push @lines, $line;
	}
	close $fh;
	return @lines;
}



1; # �폜�s��
