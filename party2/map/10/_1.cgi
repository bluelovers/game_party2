# �_���W������
$d_name = "$dungeons[$stage]�Q�K";

# �ő�^�[��
$max_round = 30;

# �}�b�v
@maps = (
	[1,0,1],
	[1,0,1],
	[1,0,1],
	[1,0,1],
	[0,B,0],
	[0,0,0],
	[0,F,0],
);


# �C�x���g
$map_imgs{F} = '��';
$map_imgs{B} = '��' if $event !~ /B/;
sub event_F { for my $y (@partys) { $ms{$y}{state} = '�U��' }; $map="__1"; $npc_com.="$p_name�͎��̊K�ւƐi�񂾁c"; }
sub event_0 { for my $y (@partys) { $ms{$y}{state} = '�U��' }; return if rand(2) > 1; &add_monster; } # ��
sub event_B { for my $y (@partys) { $ms{$y}{state} = '�U��' }; return if $event =~ /B/; $event .= 'B'; &add_boss; } # �{�X


# �G�ƕ�̐ݒ�
require "$mapdir/10/_data.cgi";

# �{�X
@bosses= (
	{
		name		=> '�ޯ�����A',
		hp			=> 1200,
		at			=> 450,
		df			=> 120,
		ag			=> 150,
		get_exp		=> 255,
		get_money	=> 50,
		icon		=> 'mon/577.gif',
		job			=> 31, # �����m���΂�
		sp			=> 20,
		mp			=> 142,
	},
	{
		name		=> '�Ђ����ǂ�',
		hp			=> 9800,
		at			=> 660,
		df			=> 210,
		ag			=> 310,
		get_exp		=> 1200,
		get_money	=> 300,
		icon		=> 'mon/530.gif',
		hit			=> 300, # ������p������
		job			=> 26, # �E��
		sp			=> 999,
		old_job		=> 27, # �����t
		old_sp		=> 999,
		mmp			=> 9999,
		mp			=> 797,
		tmp			=> '������',
	},
	{
		name		=> '�ޯ�����B',
		hp			=> 1200,
		at			=> 450,
		df			=> 120,
		ag			=> 150,
		get_exp		=> 255,
		get_money	=> 50,
		icon		=> 'mon/577.gif',
		job			=> 31, # �����m���΂�
		sp			=> 20,
		mp			=> 142,
	},
);


1; # �폜�s��
