# �ő�^�[��
$max_round = 70;

# �}�b�v
@maps = (
	[S,M,0,0,0,0,1,4,3,2,B],
	[1,1,0,1,1,0,1,1,1,1,b],
	[0,0,0,1,0,0,1,0,H,1,0],
	[0,1,1,1,0,1,1,0,1,1,0],
	[0,0,0,1,0,H,1,0,0,0,0],
	[1,1,0,1,1,1,1,1,1,1,0],
	[0,0,0,0,0,0,0,0,1,0,0],
	[0,1,1,0,1,1,1,H,1,0,1],
	[0,1,1,1,1,0,1,1,1,0,1],
	[0,0,0,0,0,0,0,0,0,0,0],
);

# �C�x���g
$map_imgs{B} = '��' if $event !~ /B/;
$map_imgs{b} = '��' if $event !~ /b/;
$map_imgs{2} = '��' if $event !~ /2/;
$map_imgs{3} = '��' if $event !~ /3/;
$map_imgs{4} = '��' if $event !~ /4/;
sub event_0 { $ms{$m}{hp}-=int($ms{$m}{mhp}*0.02+0.5); if ($ms{$m}{hp} <= 0) { $ms{$m}{hp}=0; $npc_com .= qq!<span class="die">$m�͓|�ꂽ�I</span>!; } } # ��
sub event_2 { return if $event =~ /2/; $event .= '2'; &_add_treasure; }
sub event_3 { return if $event =~ /3/; $event .= '3'; &_add_treasure; }
sub event_4 { return if $event =~ /4/; $event .= '4'; &_add_treasure; }
sub event_M { return if $event =~ /M/; $event .= 'M'; $npc_com.=qq|<br /><span class="strong">�R�R�n���m����H�@���L�e�A�b�^�҃n�@�N���C�i�C�c<br />�@���P�f�n�i�C�@�G�n�o�i�C�K�@�P���i���S�g�j�@���K�탉���e�C�N�_���E�c</span>|; }
sub event_b { return if $event =~ /b/; $event .= 'b'; $npc_com.="�����Ȃ�ʋC�z��������c�B�ǂ����A���̃_���W�����̃{�X�̂悤���I<br />"; &add_boss } # �{�X
sub event_H { return if $event =~ /H/; $event .= 'H'; $npc_com.=qq|<br /><span class="strong">�c�O�@���O�@�s�L�~�}��<br />�@�V�J�V�@�`���b�g�_�P�T�[�r�X</span><br />|; rand(2)<1 ? &_heal(shift, 40, '��') : &_mp_h(shift, 40, '��'); }

# �G�ƕ�̐ݒ�
my $_s = int(rand(5)+4);
require "$stagedir/$_s.cgi";



1; # �폜�s��
