# �_���W������
$d_name = "$dungeons[$stage]�R�K";

# �ő�^�[��
$max_round = 50;

# �}�b�v
@maps = (
	[1,F,1],
	[0,B,0],
	[Q,T,Q],
	[0,0,0],
	[0,0,0],
);

# �C�x���g
$map_imgs{Q} = '�@';
$map_imgs{T} = '�@';
$map_imgs{B} = '��' if $event !~ /B/;;
$map_imgs{F} = '��';
sub event_Q {}
sub event_F { my $v = int(rand(3)+1); $map="___$v"; $npc_com.="$p_name�͎��̊K�ւƐi�񂾁c"; }
sub event_T { $map = '_'.int(rand(4)+1); $npc_com.= "<b>�I�I�I�I�H</b>���Ƃ������I$leader�����͌��ɗ����Ă��܂����I"; &_trap_d(70); }


# �G�ƕ�̐ݒ�
my $_s = int(rand(3)+4);
require "$stagedir/$_s.cgi";




1; # �폜�s��
