# �ő�^�[��
$max_round = 60;

# �}�b�v
@maps = (
	[3,0,0,0,0,t,0,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,0],
	[0,1,S,0,0,0,0,1,0,0,0],
	[L,1,0,1,1,1,0,0,0,1,T],
	[0,1,0,1,0,0,0,I,0,0,0],
	[0,t,0,1,0,1,1,4,1,T,1],
	[0,1,0,1,0,H,1,1,1,1,1],
	[0,1,0,1,t,1,1,0,I,I,1],
	[0,T,0,0,0,0,0,0,1,B,2],
);

# �C�x���g
$map_imgs{L} = '��';
$map_imgs{I} = $event =~ /L/ ? '��' : '��'; # ���o�[�Ђ��ꂽ�瓹�\��
sub event_I { return if $event =~ /L/; $npc_com .= "�Ȃ�ƁI�ǂł͂Ȃ��B���ʘH�ɂȂ��Ă����I"; }
sub event_2 { return if $event =~ /2/; $event .= '2'; &_add_treasure; }
sub event_3 { return if $event =~ /3/; $event .= '3'; &_add_treasure; }
sub event_4 { return if $event =~ /4/; $event .= '4'; &_add_treasure; }
sub event_T { $npc_com.= "<b>�I�I�I�I�H</b>����̕ǂ���ŃK�X���ӂ������Ă����I"; for my $y (@partys) { $ms{$y}{state} = '�ғ�'; }; &add_monster; }
sub event_t { $npc_com.= "<b>�I�I�I�I�H</b>���ォ���̉J���ӂ肻�����ł����I"; &_trap_d(80); }
sub event_H {
	return if $event =~ /H/;
	$npc_com.="�e�[�u���̏�ɉ���炠�₵���Ȗ�⍂�x�Ȉ�w�����U��΂��Ă���c";
	if ($m{job} eq '43') {
		$event .= 'H';
		$npc_com.="$m�͖{�ɏ����Ă��邱�Ƃ���ǂ��񕜖�����o�����I�S���̂g�o�Ƃl�o���񕜂����I";
		for my $y (@partys) {
			$ms{$y}{hp} = $ms{$y}{mhp};
			$ms{$y}{mp} = $ms{$y}{mmp};
		}
	}
}
sub event_L {
	if ($event =~ /L/) {
		$npc_com.= rand(4) > 1 ? "���o�[�͂��łɈ�����Ă���c" : rand(2) > 1 ? "$m�̌����ȐH�ו��̓��o�[�c" : "$m�̑�D���̓��o�[�c(�P�ʁP)�ޭ�؁c";
		return;
	}
	$event .= 'L';
	$npc_com.="$m�͂��₵���ȃ��o�[�������Ă݂��I�c�޺޺޺޺޺޺ށc�ǂ����̕ǂ�������鉹�������I<br />";
	$npc_com.="�Ȃ�ƁA���o�[�̂�����̕ǂ�����A�����X�^�[���������������Ă����I<br />";
	&add_boss;
}

# �G�ƕ�̐ݒ�
my $_s = int(rand(4)+5);
require "$stagedir/$_s.cgi";



1; # �폜�s��
