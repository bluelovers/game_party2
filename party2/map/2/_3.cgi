# �_���W������
$d_name = "$dungeons[$stage]�Q�K";

# �ő�^�[��
$max_round = 40;

# �}�b�v
@maps = (
	[0,0,0],
	[1,1,0],
	[0,0,0],
	[0,1,T],
	[0,8,F],
);

# �C�x���g
$map_imgs{F} = '��';
sub event_F { $map="__1"; $npc_com.="$p_name�͎��̊K�ւƐi�񂾁c"; }
sub event_2 { return if $event =~ /2/; $event .= '2'; &_add_treasure; }
sub event_8 { return if $event =~ /8/; $event .= '8'; require "$stagedir/4.cgi"; $npc_com.="�����Ȃ�ʋC�z��������c�B�ǂ����A���̃t���A�̃{�X�̂悤���I<br />"; &add_boss } # �{�X
sub event_T { $map= int(rand(3)+1); $npc_com.= "<b>�I�I�I�I�H</b>���Ƃ������I$leader�����͌��ɗ����Ă��܂����I"; &_trap_d(30); }


# �G�ƕ�̐ݒ�
my $_s = int(rand(3)+3);
require "$stagedir/$_s.cgi";



1; # �폜�s��
