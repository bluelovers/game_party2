# �_���W������
$d_name = "$dungeons[$stage]�P�K";

# �ő�^�[��
$max_round = 30;

# �}�b�v
@maps = (
	[F,7,0],
	[1,1,0],
	[0,0,0],
	[0,1,1],
	[0,0,S],
);

# �C�x���g
$map_imgs{F} = '��';
sub event_F { my $v = int(rand(3)+1); $map="_$v"; $npc_com.="$p_name�͎��̊K�ւƐi�񂾁c"; }
sub event_7 { return if $event =~ /7/; $event .= '7'; require "$stagedir/3.cgi"; $npc_com.="�����Ȃ�ʋC�z��������c�B�ǂ����A���̃t���A�̃{�X�̂悤���I<br />"; &add_boss } # �{�X

# �G�ƕ�̐ݒ�
my $_s = int(rand(3)+2);
require "$stagedir/$_s.cgi";



1; # �폜�s��
