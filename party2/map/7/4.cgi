# �ő�^�[��
$max_round = 60;

# �}�b�v
@maps = (
	[2,1,0,1,4],
	[B,0,T,1,0],
	[1,0,1,1,D],
	[0,0,0,0,0],
	[0,1,0,1,t],
	[0,1,S,1,0],
	[0,1,0,1,1],
	[0,0,0,0,1],
	[0,1,1,0,1],
	[b,1,A,0,t],
	[K,1,3,1,0],
);

# �C�x���g
$map_imgs{K} = '��' if $event !~ /D|K/;
$map_imgs{D} = '��' if $event !~ /D|K/;
sub event_2 { return if $event =~ /2/; $event .= '2'; &_add_treasure; }
sub event_3 { return if $event =~ /3/; $event .= '3'; &_add_treasure; }
sub event_4 { return if $event =~ /4/; $event .= '4'; &_add_treasure; }
sub event_T { $npc_com.= "<b>�I�I�I�I�H</b>���т��悤�ȃK�X��$m�������݂��񂾁I"; for my $y (@partys) { $ms{$y}{state} = '���'; }; &_add_monster; }
sub event_t { $npc_com.= "<b>�I�I�I�I�H</b>���M�̃K�X���ӂ������Ă����I"; &_trap_d(150); }
sub event_A { return if $event =~ /A/; $event .= 'A'; $npc_com.="�����Ȃ�ʋC�z��������c�B�ǂ����A���̃_���W�����̃{�X�̂悤���I<br />"; &add_boss } # �{�X
sub event_b { return if $event =~ /b/; $event .= 'b'; $npc_com.="�����Ȃ�ʋC�z��������c�B�ǂ����A���̃_���W�����̃{�X�̂悤���I<br />"; &add_boss } # �{�X
sub event_K { return if $event =~ /D|K/; $event .= 'K'; $npc_com.="$m�͉����X�C�b�`�̂悤�Ȃ��̂𓥂�ł��܂����I�c�޺޵����ݯ�I�I�c��������ꂽ���������I";  }
sub event_D {
	return if $event =~ /D|K/;
	if ($m{job} eq '4' || $m{job} eq '25') {
		$com .= "<br />$m{mes}" if $m{mes};
		$npc_com .= "$m�͑S�g�̋C�����ɏW���������c�޺޵�������ݯ�I�I�I���j�󂵂��I";
		$event .= 'D';
	}
	else {
		$npc_com .= "�傫�Ȋ�œ����ӂ�����Ă���I";
		++$py;
	}
}


# �G�ƕ�̐ݒ�
require "$mapdir/7/_data.cgi";



1; # �폜�s��
