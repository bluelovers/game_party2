# �ő�^�[��
$max_round = 20;

# �}�b�v
@maps = (
	[0,I,0,0,2],
	[0,1,B,1,1],
	[0,I,0,0,0],
	[0,1,1,1,0],
	[0,0,S,0,0],
);

# �C�x���g
$map_imgs{I} = '��';
sub event_I { $npc_com .= "�Ȃ�ƁI�ǂł͂Ȃ��B���ʘH�ɂȂ��Ă����I"; }
sub event_2 { return if $event =~ /2/; $event .= '2'; &_add_treasure; }

# �G�ƕ�̐ݒ�
my $_s = int(rand(2));
require "$stagedir/$_s.cgi";



1; # �폜�s��
