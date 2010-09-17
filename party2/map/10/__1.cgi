# �_���W������
$d_name = "$dungeons[$stage]�R�K";

# �ő�^�[��
$max_round = 30;

# �}�b�v
@maps = (
	[2,3,4],
	[0,0,0],
	[0,C,0],
	[1,0,1],
	[1,0,1],
	[1,0,1],
	[1,0,1],
);


# �C�x���g
$map_imgs{2} = '��' if $event !~ /2/;
$map_imgs{3} = '��' if $event !~ /3/;
$map_imgs{4} = '��' if $event !~ /4/;
$map_imgs{C} = '��' if $event !~ /C/;
sub event_2 { for my $y (@partys) { $ms{$y}{state} = '�U��' }; return if $event =~ /2/; $event .= '2'; &_add_treasure; }
sub event_3 { for my $y (@partys) { $ms{$y}{state} = '�U��' }; return if $event =~ /3/; $event .= '3'; &_add_treasure; }
sub event_4 { for my $y (@partys) { $ms{$y}{state} = '�U��' }; return if $event =~ /4/; $event .= '4'; &_add_treasure; }
sub event_0 { for my $y (@partys) { $ms{$y}{state} = '�U��' }; return if rand(2) > 1; &_add_monster; } # ��
sub event_C { for my $y (@partys) { $ms{$y}{state} = '�U��' }; return if $event =~ /C/; $event .= 'C'; $npc_com.="�����Ȃ�ʋC�z��������c�B�ǂ����A���̃_���W�����̃{�X�̂悤���I<br />"; &add_boss; } # �{�X


# �G�ƕ�̐ݒ�
require "$mapdir/10/_data.cgi";

# �{�X
@bosses= (
	{
		name		=> '����',
		hp			=> 5000,
		at			=> 300,
		df			=> 200,
		ag			=> 800,
		get_exp		=> 500,
		get_money	=> 700,
		icon		=> 'mon/661.gif',
		job			=> 58, # �ް����
		sp			=> 999,
		old_job		=> 48, # �V�g
		old_sp		=> 160,
		mmp			=> 99999,
		mp			=> 9999,
	},
	{
		name		=> '����',
		hp			=> 8000,
		at			=> 400,
		df			=> 400,
		ag			=> 999,
		get_exp		=> 3000,
		get_money	=> 2500,
		icon		=> 'mon/660.gif',
		hit			=> 500, # ������p������
		job			=> 98, # �����@�^
		sp			=> 999,
		mmp			=> 99999,
		mp			=> 9999,
		tmp			=> '������',
	},
	{
		name		=> '����',
		hp			=> 5000,
		at			=> 300,
		df			=> 600,
		ag			=> 900,
		get_exp		=> 666,
		get_money	=> 666,
		icon		=> 'mon/697.gif',
		job			=> 95, # ����
		sp			=> 999,
		old_job		=> 31, # �����m
		old_sp		=> 999,
		mmp			=> 99999,
		mp			=> 9999,
	},
);


1; # �폜�s��
