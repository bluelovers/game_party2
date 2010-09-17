# �ő�^�[��
$max_round = 30;

# �}�b�v
@maps = (
	[0,2,0],
	[1,X,1],
	[1,0,1],
	[0,0,0],
	[A,1,B],
	[0,5,0],
	[1,0,1],
	[1,0,1],
	[0,0,0],
	[C,1,D],
	[0,6,0],
	[1,0,1],
	[1,0,1],
	[0,0,0],
	[E,1,F],
	[0,7,0],
	[1,0,1],
	[1,S,1],
);

# �C�x���g
$map_imgs{X} = '��' if $event !~ /X/;
$map_imgs{2} = '��' if $event !~ /2/;
$map_imgs{3} = '��' if $event !~ /3/;
sub event_X { return if $event =~ /X/; $event .= 'X'; $npc_com.="�����Ȃ�ʋC�z��������c�B�ǂ����A���̃_���W�����̃{�X�̂悤���I<br />"; &add_boss } # �{�X
sub event_2 { return if $event =~ /2/; $event .= '2'; &_add_treasure; }
sub event_3 { return if $event =~ /3/; $event .= '3'; &_add_treasure; }

sub event_5 { return if $event =~ /5/; $event .= '5'; $npc_com.=qq|<br /><span class="strong">��Yes�y���������傫�����������zNo��</span>|; }
sub event_A { return if $event =~ /A|B/; $event .= 'A'; if (rand(3)<1) { &get_monster_data1; &_add_monster; } else { &get_monster_data2; &_add_monster; };  }
sub event_B { return if $event =~ /A|B/; $event .= 'B'; if (rand(7)<1) { &get_monster_data3; &_add_monster; } else { &get_monster_data4; &_add_monster; };  }

sub event_6 { return if $event =~ /6/; $event .= '6'; $npc_com.=qq|<br /><span class="strong">��Yes�y����肨�����厖�zNo��</span>|; }
sub event_C { return if $event =~ /C|D/; $event .= 'C'; if (rand(2)<1) { &_trap_d(rand(200));       } else { my $v = int(rand(2000)); $m{money}+=$v; $npc_com.="$m�� ${v}G �E�����I"; };  }
sub event_D { return if $event =~ /C|D/; $event .= 'D'; if (rand(2)<1) {  &_heals(rand(100), '��'); } else { my $v = int(rand(2000)); $m{money}-=$v; $npc_com.="$m�� ${v}G ���Ƃ��Ă��܂����I"; $m{money}-=0 if $m{money} < 0; };  }

sub event_7 { return if $event =~ /7/; $event .= '7'; $npc_com.=qq|<br /><span class="strong">��Yes�y���i�͑匙�����zNo��</span>|; }
sub event_E { return if $event =~ /E|F/; $event .= 'E'; if (rand(3)<1) { &add_boss; } else { &_add_monster; }; }
sub event_F { return if $event =~ /E|F/; $event .= 'F'; if (rand(3)<1) { $npc_com.= "<b>�I�I�I�I�H</b>��׶�׶�ׯ�I���ォ��傫�Ȋ₪�����Ă����I"; &_trap_d(120); } else { $npc_com.= "<b>�I�I�I�I�H</b>��׶�׶�ׯ�I���ォ��傫�Ȋ₪�����Ă����I�c�������A$m�����͂��炩���ߗ\\�z���Ă����̂ł��킷���Ƃ��ł����I"; };		 }


# �G�ƕ�̐ݒ�
require "$mapdir/6/_data.cgi";

sub get_monster_data1 {
	@monsters = (
		{
			name		=> '��ٽײ�',
			hp			=> 8,
			at			=> 70,
			df			=> 2500,
			ag			=> 1500,
			get_exp		=> 250,
			get_money	=> 10,
			icon		=> 'mon/004.gif',
			job			=> 39, # �X���C���M��
			sp			=> 3,
			old_job		=> 99, # ������
			old_sp		=> 0,
			mp			=> 31,
			tmp			=> '������',
		},
	);
}
sub get_monster_data2 {
	@monsters = (
		{
			name		=> '�ײ�',
			hp			=> 500,
			at			=> 200,
			df			=> 100,
			ag			=> 500,
			get_exp		=> 50,
			get_money	=> 30,
			icon		=> 'mon/002.gif',
			job			=> 40, # ʸ�����
			sp			=> 999,
			old_sp		=> 20,
			mp			=> 149,
		},
	);
}
sub get_monster_data3 {
	@monsters = (
		{
			name		=> '��ٷݸ�',
			hp			=> 25,
			at			=> 200,
			df			=> 6000,
			ag			=> 2000,
			get_exp		=> 4000,
			get_money	=> 100,
			icon		=> 'mon/517.gif',
			job			=> 40, # ʸ�����
			sp			=> 999,
			old_job		=> 99, # ������
			old_sp		=> 0,
			mp			=> 299,
			tmp			=> '������',
		},
	);
}
sub get_monster_data4 {
	@monsters = (
		{
			name		=> '�ݸ޽ײ�',
			hp			=> 2000,
			at			=> 250,
			df			=> 150,
			ag			=> 120,
			get_exp		=> 200,
			get_money	=> 200,
			icon		=> 'mon/516.gif',
			old_sp		=> 20,
			hit			=> 150, # ������p������150%
			job			=> 21, # ����m����������
			sp			=> 5,
			mp			=> 400,
			tmp			=> '�U����',
		},
	);
}




1; # �폜�s��
