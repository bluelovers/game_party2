my $yid = unpack 'H*', $m{home};
if (!$m{home} || !-d "$userdir/$yid") { my $yhome = $m{home}; $m{home} = $m; &write_user; &error("$yhome�Ƃ����Ƃ͌�����܂���"); }
#=================================================
# ������ Created by Merino
#=================================================
# �ꏊ��
$this_title = "$m{home}�̉�";

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$userdir/$yid/home";

# �w�i�摜
$bgimg  = "";


#=================================================
# �w�b�_�[�\��
#=================================================
$m{sleep} -= int($time - $m{ltime}) if $m{sleep} > 0;
sub header_html {
	if ($m{sleep} > 0) {
		my $wake_time  = sprintf("%d��%02d�b", int($m{sleep} / 60), int($m{sleep} % 60) );
		my $wake_html .= qq|<span id="wake_time">$wake_time</span>\n|;
		$wake_html    .= qq|<script type="text/javascript"><!--\n wake_time($m{sleep});\n// --></script>\n|;
		$wake_html    .= qq|<noscript>$wake_up_nokori</noscript>\n|;

		print qq|<form method="$method" action="$script_index"><input type="submit" value="�����O�A�E�g" class="button_s" /></form>|;
		print qq|<div class="mes">�y$this_title�z ���x�ݒ��uZzz...�v �ڊo�߂�܂� $wake_html</div>|;
	}
	else { # �ڊo��
		$m{tired} = 0;
		$m{hp} = $m{mhp};
		$m{mp} = $m{mmp};
		$m{is_eat} = 0;
		$m{icon}   = "job/$m{job}_$m{sex}.gif";

		print qq|<div class="mes">�y$this_title�z $m��$e2j{hp}$e2j{mp}$e2j{tired}���񕜂����I</div>|;
	}
}

# �s���͂ł��Ȃ�
sub set_action { return }


1; # �폜�s��
