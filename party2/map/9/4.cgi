# �ő�^�[��
$max_round = 60;

# �}�b�v
@maps = (
	[4,1,0,0,0,1,0],
	[0,1,0,2,0,1,0],
	[0,1,0,0,0,1,0],
	[0,1,1,A,1,1,0],
	[0,0,0,0,0,0,0],
	[1,1,1,1,1,0,1],
	[0,3,0,1,0,0,0],
	[0,0,0,1,0,0,0],
	[0,B,0,1,0,C,0],
	[1,0,1,1,1,0,1],
	[0,0,0,S,0,0,0],
);


# �C�x���g
$map_imgs{2} = '��' if $event !~ /2/;
$map_imgs{3} = '��' if $event !~ /3/;
$map_imgs{4} = '��' if $event !~ /4/;
$map_imgs{A} = '��' if $event !~ /A/;
$map_imgs{B} = '��' if $event !~ /B/;
$map_imgs{C} = '��' if $event !~ /C/;
sub event_0 { for my $y (@partys) { $ms{$y}{state} = '����' }; return if rand(2) > 1; &_add_monster; } # ��
sub event_2 { for my $y (@partys) { $ms{$y}{state} = '����' }; return if $event =~ /2/; $event .= '2'; &_add_treasure; }
sub event_3 { for my $y (@partys) { $ms{$y}{state} = '����' }; return if $event =~ /3/; $event .= '3'; &_add_treasure; }
sub event_4 { for my $y (@partys) { $ms{$y}{state} = '����' }; return if $event =~ /4/; $event .= '4'; &_add_treasure; }
sub event_A { for my $y (@partys) { $ms{$y}{state} = '����' }; return if $event =~ /A/; $event .= 'A'; $npc_com.="�����Ȃ�ʋC�z��������c�B�ǂ����A���̃_���W�����̃{�X�̂悤���I<br />"; &add_boss } # �{�X
sub event_B { for my $y (@partys) { $ms{$y}{state} = '����' }; return if $event =~ /B/; $event .= 'B'; my $_s = int(rand(5)+8); require "$stagedir/$_s.cgi"; &add_boss; } # �{�X
sub event_C { for my $y (@partys) { $ms{$y}{state} = '����' }; return if $event =~ /C/; $event .= 'C'; my $_s = int(rand(5)+8); require "$stagedir/$_s.cgi"; &add_boss; } # �{�X



# �G�ƕ�̐ݒ�
require "$mapdir/9/_data.cgi";


1; # �폜�s��
