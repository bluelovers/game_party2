# �_���W������
$d_name = "$dungeons[$stage]�S�K[�󕨌�]";

# �ő�^�[��
$max_round = 50;

# �}�b�v
@maps = (
	[1,0,1],
	[0,0,0],
	[0,T,0],
	[0,2,0],
	[3,0,4],
);

# �C�x���g
$map_imgs{2} = '��' if $event !~ /2/;
$map_imgs{3} = '��' if $event !~ /3/;;
$map_imgs{4} = '��' if $event !~ /4/;;
sub event_2 { return if $event =~ /2/; $event .= '2'; &_add_treasure; }
sub event_3 { return if $event =~ /3/; $event .= '3'; &_add_treasure; }
sub event_4 { return if $event =~ /4/; $event .= '4'; &_add_treasure; }
sub event_T { $map = '__1'; $npc_com.= "<b>�I�I�I�I�H</b>���Ƃ������I$leader�����͌��ɗ����Ă��܂����I"; &_trap_d(40); }


# �G�ƕ�̐ݒ�
my $_s = int(rand(4)+3);
require "$stagedir/$_s.cgi";




1; # �폜�s��
