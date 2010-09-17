#=================================================
# SP���� Created by Merino
#=================================================
# �ꏊ��
$this_title = '�肢�̐�';

# NPC��
$npc_name   = '@���_';

# ���O�Ɏg���t�@�C��(.cgi����)
$this_file  = "$logdir/sp_change";

# �w�i�摜
$bgimg   = "$bgimgdir/sp_change.gif";


#=================================================
# �͂Ȃ����t
#=================================================
@words = (
	"�X�L���|�C���g�̓��x�����オ�邲�ƂɂP�|�C���g�����Ă����̂ł�",
	"�X�L���|�C���g�𑁂��グ��R�c�́A���x�������E�Ƃɓ]�E���邱�Ƃł�",
	"$m�̃X�L���|�C���g�͌��� $m{sp} �|�C���g�ł�",
	"�X�L���K����ڎw���Ă���ꍇ�́A���������ɂƂ��Ă����̂ł���",
	"�X�L���|�C���g����������̂ł�",
	"�X�L���|�C���g�̂���ɁA$m�̃X�e�[�^�X���グ�Ă����܂��傤",
	"��x���������X�L���|�C���g��߂����Ƃ͂ł��܂���",
	"�X�L���|�C���g�́A���̐E�Ƃ̃X�L�����K������̂ɕK�v�ł�",
);


#=================================================
# �ǉ��A�N�V����
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
# �w�b�_�[�\��
#=================================================
sub header_html {
	print qq|<div class="mes">�y$this_title�z $jobs[$m{job}][1] $e2j{sp}<b>$m{sp}</b>|;
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
		$mes = "$e2j{sp}�������������܂����H�၄�w��$e2j{hp}>1�xSP���P�������g�o���グ��";
		return;
	}
	elsif ($sp > $m{sp}) {
		$mes = "��������$e2j{sp}������܂���";
		return;
	}
	
	my $v = $sp * $up;
	$m{sp} -= $sp;
	$m{$k} += $v;
	$npc_com = "$e2j{sp} $sp �̂����� $e2j{$k} �� $v �������܂��傤";
}



1; # �폜�s��
