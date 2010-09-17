#=================================================
# �B���p Created by Merino
#=================================================
# �ꏊ��
$this_title = '�B����';

# NPC��
$npc_name = '@����';

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$logdir/alchemy";

# �w�i�摜
$bgimg = "$bgimgdir/alchemy.gif";



# �����t���O���������犮��������
&finish() if $m{recipe} =~ /^1/;


#=================================================
# �͂Ȃ����t
#=================================================
@words = (
	"�Q�̃A�C�e����B�����邱�ƂŐV���ȃA�C�e������邱�Ƃ��ł��邼��",
	"�B��ڼ�߂��g�����ƂŘB�����邱�Ƃ��\\�ɂȂ邼��",
	"�B�������A�C�e���̊����́A���傪�Q�ċN�������̓��ɂ͊������Ă��邶��낤",
	"�B���ō�邱�Ƃł�����ɓ���Ȃ������h����邻������E�E�E",
	"�B��ڼ�߂͏K���ς݈ȊO�̂��̂��K�����邱�Ƃ��ł��邼��",
);

#=================================================
# ������ׂ�>NPC
#=================================================
sub shiraberu_npc {
	$mes = qq|$npc_name�u�����B�ǂ���������Ƃ�񂶂���I�v|;
}

#=================================================
# �ǉ��A�N�V����
#=================================================
push @actions, '�ꂵ��';
push @actions, '��񂫂�';
$actions{'�ꂵ��'}   = sub{ &reshipi }; 
$actions{'��񂫂�'} = sub{ &renkin }; 

#=================================================
# ���ꂵ��
#=================================================
sub reshipi {
	# ���V�s�ꗗ�ǂݍ���
	require './lib/_alchemy_recipe.cgi';
	my $all_c = map { keys %{ $recipes{$_} } } keys %recipes;

	my $c = 0;
	my $comp_c = 0;
	my $p = qq|<table><tr><td><table class="table1">|;
	open my $fh, "< $userdir/$id/recipe.cgi" or &errror("$userdir/$id/recipe.cgi�t�@�C�����ǂݍ��߂܂���");
	while (my $line = <$fh>) {
		my($is_make, $base, $sozai, $mix) = split /<>/, $line;
		
		if ($is_make) {
			++$comp_c;
		}
		else {
			$mix = '�H�H�H';
		}
		$p .= qq|<tr onclick="text_set('����񂫂�>$base��������>$sozai ')"><td>$base</td><td>�~$sozai</td><td>��$mix</td></tr>|;
		$p .= qq|</td></tr></table></td><td><table class="table1"><tr><td>| if ++$c % 40 == 0;
	}
	close $fh;

	my $comp_par = int($comp_c / $all_c * 100);
	if ($comp_par >= 100) {
		unless (-f "$userdir/$id/comp_alc_flag.cgi") {
			open my $fh2, "> $userdir/$id/comp_alc_flag.cgi" or &error("$userdir/$id/comp_alc_flag.cgi�t�@�C�����J���܂���");
			close $fh2;
			
			&write_legend('comp_alc');
			&write_memory(qq|<span class="comp">Alchemy Complete!!</span>|);
			&write_news(qq|<span class="comp">$m���B�����V�s���R���v���[�g����I</span>|);
			$npc_com .= qq|<span class="comp">$m�� <b>�B�����V�s</b> ���R���v���[�g���܂����I</span>�̂���|;
		}
		
		$comp_par = 100;
	}

	$mes = qq|$m�̘B�����V�s�@�R���v���[�g���s<b>$comp_par</b>���t<br />$p</td></tr></table></td></tr></table>|;
	$act_time = 0;
}


#=================================================
# ����񂫂�
#=================================================
sub renkin {
	my $target = shift;
	my($base_t, $sozai_t) = split /��������&gt;/, $target;

	if ($m{recipe}) {
		$mes = "��������܂ł��΂��҂����";
		return;
	}

	my $c = 0;
	my $p = qq|<table><tr><td><table class="table1">|;
	open my $fh, "< $userdir/$id/recipe.cgi" or &error("$userdir/$id/recipe.cgi�t�@�C�����ǂݍ��߂܂���");
	while (my $line = <$fh>) {
		my($is_make, $base, $sozai, $mix) = split /<>/, $line;
		
		if ($base_t eq $base && $sozai_t eq $sozai) {
			my $is_clear = &check_depot($base, $sozai);

			if ($is_clear) {
				$m{recipe} = "0,${is_make},${base},${sozai},${mix}";
				$npc_com = $is_make
					? "$base �� $sozai ����ȁI�ӂށA���̑g�ݍ��킹�Ȃ� $mix ���ł��邼�I�������鍠�ɂ܂����邪�悢"
					: "$base �� $sozai ����ȁI�����A�B���\\�Ȃ悤����I�����o���邩�y���݂���ȁI��ӂ��ĂΊ������邶��낤�B�������鍠�ɂ܂����邪�悢";
			}
			else {
				$npc_com = "�c�O�Ȃ��� $base �� $sozai �̍ޗ����a�菊�ɂȂ��悤����";
			}
			last;
		}
		else {
			$mix = '�H�H�H' unless $is_make;
			$p .= qq|<tr onclick="text_set('����񂫂�>$base��������>$sozai ')"><td>$base</td><td>�~$sozai</td><td>��$mix</td></tr>|;
		}
		$p .= qq|</td></tr></table></td><td><table class="table1"><tr><td>| if ++$c % 40 == 0;
	}
	close $fh;
	
	$npc_com = "�B��ڼ�߂ŏK���������̂����B�����邱�Ƃ͂ł���" if !$npc_com && $base_t && $sozai_t;
	return if $npc_com;
	$mes = qq|$m�̘B�����V�s<br />$p</td></tr></table></td></tr></table>|;
	$act_time = 0;
}
#-------------------
# �q�Ƀ`�F�b�N�B�����N���A�Ȃ�Y���̃A�C�e�������炷
sub check_depot {
	my($base, $sozai) = @_;

	my $has_base = 0;
	my $has_sozai = 0;
	my @lines = ();
	open my $fh, "+< $userdir/$id/depot.cgi" or &error("$userdir/$id/depot.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($kind, $no) = split /<>/, $line;
		my $name = $kind eq '1' ? $weas[$no][1]
				 : $kind eq '2' ? $arms[$no][1]
				 :                $ites[$no][1];
		if    (!$has_base  && $name eq $base)  { $has_base  = 1 }
		elsif (!$has_sozai && $name eq $sozai) { $has_sozai = 1 }
		else                                   { push @lines, $line }
	}
	if ($has_base && $has_sozai) { # ���������N���A���Ă���㏑��
		seek  $fh, 0, 0;
		truncate $fh, 0;
		print $fh @lines;
		close $fh;

		return 1;
	}
	close $fh;

	return 0;
}

#=================================================
# ����
#=================================================
sub finish {
	my($is_finish, $is_make, $base, $sozai, $mix) = split /,/, $m{recipe};
	$com = "����񂫂�ł��񂹂��������̂������Ƃ�";
	$npc_com = "�܂��Ă��������I$base��$sozai��B������ <b>$mix</b> ���������������I�o���オ�����A�C�e���͗a���菊�̕��ɑ����Ă����������I";
	$m{recipe} = '';
	++$m{alc_c};

	my($kind, $no) = &get_item_no($mix);
	if ($kind eq '0') { # ���ݒ�̑��݂��Ȃ��A�C�e�����������ꍇ(config.cgi�ɒǉ����Y��)
		$npc_com .= qq|<b style="color: #F00">$mix �Ƃ����A�C�e�����ݒ肳��Ă����悤����c�B�����̊Ǘ��҂ɓ`����񂶂�I</b>|;
	}
	else {
		&send_item($m, $kind, $no);
	}
	
	# ���쐬�Ȃ烌�V�s�ɍ쐬�����t���O�����Ă�
	&finished_recipe($base, $sozai, $mix) unless $is_make;
}
#-------------------
# �A�C�e��������A�C�e����ނ�No���擾
sub get_item_no {
	my $name = shift;
	for my $i (1..$#weas) { return 1, $i if $weas[$i][1] eq $name; }
	for my $i (1..$#arms) { return 2, $i if $arms[$i][1] eq $name; }
	for my $i (1..$#ites) { return 3, $i if $ites[$i][1] eq $name; }
	return 0;
}
#-------------------
# ���V�s�ɍ쐬�����t���O�����Ă�
sub finished_recipe {
	my($new_base, $new_sozai, $new_mix) = @_;

	my @lines = ();
	open my $fh, "+< $userdir/$id/recipe.cgi" or &errror("$userdir/$id/recipe.cgi�t�@�C�����J���܂���");
	eval { flock $fh, 2; };
	while (my $line = <$fh>) {
		my($is_make, $base, $sozai, $mix) = split /<>/, $line;
		
		if ($new_base eq $base && $new_sozai eq $sozai && $new_mix eq $mix) {
			$line = "1<>$base<>$sozai<>$mix<>\n";
		}
		push @lines, $line;
	}
	seek  $fh, 0, 0;
	truncate $fh, 0;
	print $fh @lines;
	close $fh;
}




1; # �폜�s��
