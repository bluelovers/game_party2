# �ő�^�[��
$max_round = 50;

# �}�b�v
@maps = (
	[2,A,0,0,D,0,0,0,0,A,3],
	[A,0,0,0,0,0,0,W,0,D,0],
	[0,0,0,0,0,0,0,0,0,0,B],
	[0,0,0,0,W,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,C],
	[0,0,0,0,0,0,0,0,0,0,0],
	[B,0,0,W,0,S,0,0,0,0,0],
	[0,0,0,0,0,W,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,C,0,0,0,0,0,0,0,0,0],
	[D,0,3,0,0,0,0,0,0,B,0],
	[0,0,0,0,0,C,0,0,0,4,0],
);

# �C�x���g
$map_imgs{1} = '��';
sub event_W { $py=int(rand(5)+3); $px=int(rand(5)+3); }
sub event_1 { $py=int(rand(5)+3); $px=int(rand(5)+3); }
sub event_2 { return if $event =~ /2/; $event .= '2'; &_add_treasure; }
sub event_3 { return if $event =~ /3/; $event .= '3'; &_add_treasure; }
sub event_4 { return if $event =~ /4/; $event .= '4'; &_add_treasure; }
sub event_A { return if $event =~ /A/; $event .= 'A'; $npc_com.="�����Ȃ�ʋC�z��������c�B�ǂ����A���̃_���W�����̃{�X�̂悤���I<br />"; &add_boss } # �{�X
sub event_C { return if $event =~ /C/; $event .= 'C'; $npc_com.="�����Ȃ�ʋC�z��������c�B�ǂ����A���̃_���W�����̃{�X�̂悤���I<br />"; &add_boss } # �{�X
sub event_D { return if $event =~ /D/; $event .= 'D'; $npc_com.="�����Ȃ�ʋC�z��������c�B�ǂ����A���̃_���W�����̃{�X�̂悤���I<br />"; &add_boss } # �{�X

# �G�ƕ�̐ݒ�
my $_s = int(rand(5)+10);
require "$stagedir/$_s.cgi";



1; # �폜�s��
