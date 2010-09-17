# �ő�^�[��
$max_round = 30;

# �}�b�v
@maps = (
	[2,3,4],
	[1,0,1],
	[1,0,1],
	[0,A,0],
	[1,0,1],
	[1,0,1],
	[H,B,H],
	[1,0,1],
	[1,0,1],
	[H,C,H],
	[1,0,1],
	[1,0,1],
	[H,D,H],
	[1,0,1],
	[1,0,1],
	[H,E,H],
	[1,0,1],
	[1,0,1],
	[H,F,H],
	[1,0,1],
	[1,0,1],
	[1,S,1],
);

# �C�x���g
$map_imgs{2} = '��' if $event !~ /2/;
$map_imgs{3} = '��' if $event !~ /3/;;
$map_imgs{4} = '��' if $event !~ /4/;;
sub event_2 { return if $event =~ /2/; $event .= '2'; my $_s = int(rand(8)+14); require "$stagedir/$_s.cgi"; &_add_treasure; }
sub event_3 { return if $event =~ /3/; $event .= '3'; my $_s = int(rand(8)+14); require "$stagedir/$_s.cgi"; &_add_treasure; }
sub event_4 { return if $event =~ /4/; $event .= '4'; my $_s = int(rand(8)+14); require "$stagedir/$_s.cgi"; &_add_treasure; }

$map_imgs{A} = '��' if $event !~ /A/;
$map_imgs{B} = '��' if $event !~ /B/;
$map_imgs{C} = '��' if $event !~ /C/;
$map_imgs{D} = '��' if $event !~ /D/;
$map_imgs{E} = '��' if $event !~ /E/;
$map_imgs{F} = '��' if $event !~ /F/;
sub event_A { return if $event =~ /A/; $event .= 'A'; $npc_com.="�����قǂ�苭���p���[��������c�B<br />"; &get_boss_data2; &add_boss; }
sub event_B { return if $event =~ /B/; $event .= 'B'; $npc_com.="�����Ȃ�ʋC�z��������c�B�ǂ����A���̃_���W�����̃{�X�̂悤���I<br />"; &get_boss_data; &add_boss; }
sub event_C { return if $event =~ /C/; $event .= 'C'; require "$stagedir/13.cgi"; &add_boss; }
sub event_D { return if $event =~ /D/; $event .= 'D'; require "$stagedir/18.cgi"; &add_boss; }
sub event_E { return if $event =~ /E/; $event .= 'E'; require "$stagedir/12.cgi"; &add_boss; }
sub event_F { return if $event =~ /F/; $event .= 'F'; require "$stagedir/10.cgi"; &add_boss; }
sub event_H {
	return if $event =~ /H/;
	$npc_com.="�e�[�u���̏�ɉ���炠�₵���Ȗ�⍂�x�Ȉ�w�����U��΂��Ă���c";
	if ($m{job} eq '43') {
		$event .= 'H';
		$npc_com.="$m�͖{�ɏ����Ă��邱�Ƃ���ǂ��񕜖�����o�����I�S���̂g�o�Ƃl�o���񕜂����I";
		for my $y (@partys) {
			$ms{$y}{hp} = $ms{$y}{mhp};
			$ms{$y}{mp} = $ms{$y}{mmp};
		}
	}
}

sub get_boss_data {
	@bosses= (
		{
			name		=> '���̉E��',
			hp			=> 6000,
			at			=> 500,
			df			=> 400,
			ag			=> 900,
			get_exp		=> 300,
			get_money	=> 300,
			icon		=> 'mon/588.gif',
			
			job			=> 41, # ��׺��
			sp			=> 999,
			old_job		=> 90, # �ғŌn
			old_sp		=> 999,
			mp			=> 999,
			tmp			=> '�󗬂�',
		},
		{
			name		=> '�ި���۽',
			hp			=> 14000,
			at			=> 600,
			df			=> 200,
			ag			=> 200,
			get_exp		=> 2000,
			get_money	=> 500,
			icon		=> 'mon/650.gif',
			
			hit			=> 400, # ������p������400%
			job			=> 97, # ���U���^
			sp			=> 999,
			mmp			=> 30000,
			mp			=> 8000,
			tmp			=> '������',
		},
		{
			name		=> '���̍���',
			hp			=> 6000,
			at			=> 500,
			df			=> 400,
			ag			=> 900,
			get_exp		=> 300,
			get_money	=> 300,
			icon		=> 'mon/589.gif',
			
			job			=> 41, # ��׺��
			sp			=> 999,
			old_job		=> 91, # ��჌n
			old_sp		=> 999,
			mp			=> 999,
			tmp			=> '�󗬂�',
		},
	);
}
sub get_boss_data2 {
	@bosses= (
		{
			name		=> '�З��̓V�g',
			hp			=> 12000,
			at			=> 500,
			df			=> 300,
			ag			=> 300,
			get_exp		=> 3000,
			get_money	=> 2000,
			icon		=> 'mon/569.gif',
			
			hit			=> 500, # ������p������
			job			=> 98, # �����@�^
			sp			=> 999,
			old_job		=> 48, # �V�g
			old_sp		=> 999,
			mmp			=> 30000,
			mp			=> 8000,
			tmp			=> '������',
		},
		{
			name		=> '�ި���۽',
			hp			=> 15000,
			at			=> 750,
			df			=> 300,
			ag			=> 700,
			get_exp		=> 5000,
			get_money	=> 1000,
			icon		=> 'mon/651.gif',
			
			hit			=> 500, # ������p������
			job			=> 97, # ���U���^
			old_job		=> 38, # ����߲�
			old_sp		=> 999,
			sp			=> 999,
			mmp			=> 30000,
			mp			=> 8000,
			ten			=> 8,
		},
		{
			name		=> '��ϰ',
			hp			=> 9000,
			at			=> 600,
			df			=> 500,
			ag			=> 200,
			get_exp		=> 1000,
			get_money	=> 1,
			icon		=> 'mon/652.gif',
			
			hit			=> 500, # ������p������
			job			=> 95, # ����
			sp			=> 999,
			old_job		=> 8, # �V�ѐl
			old_sp		=> 999,
			mp			=> 999,
			state		=> '�唚��',
			tmp			=> '���邼',
		},
	);
}

# �����X�^�[
@appears = ();
@monsters = (
	{
		name		=> '���e��',
		hp			=> 300,
		at			=> 500,
		df			=> 400,
		ag			=> 50,
		get_exp		=> 150,
		get_money	=> 30,
		icon		=> 'mon/579.gif',

		job			=> 94, # �������K���e�A�˂�
		sp			=> 20,
		mp			=> 42,
	},
	{
		name		=> '�ޯ����',
		hp			=> 600,
		at			=> 400,
		df			=> 200,
		ag			=> 200,
		get_exp		=> 120,
		get_money	=> 50,
		icon		=> 'mon/577.gif',

		job			=> 31, # �����m���΂�
		sp			=> 20,
		mp			=> 42,
	},
	{
		name		=> '�װ���',
		hp			=> 250,
		at			=> 500,
		df			=> 250,
		ag			=> 100,
		get_exp		=> 110,
		get_money	=> 50,
		icon		=> 'mon/209.gif',

		job			=> 94, # �������K���e
		sp			=> 10,
		mp			=> 42,
	},
	{
		name		=> '������',
		hp			=> 100,
		at			=> 50,
		df			=> 600,
		ag			=> 900,
		get_exp		=> 50,
		get_money	=> 1,
		icon		=> 'mon/208.gif',

		job			=> 94, # �������K���e
		sp			=> 10,
		mp			=> 42,
		tmp			=> '������',
	},
	{
		name		=> '�����',
		hp			=> 300,
		at			=> 500,
		df			=> 200,
		ag			=> 200,
		get_exp		=> 180,
		get_money	=> 99,
		icon		=> 'mon/599.gif',

		job			=> 100, # �����
		sp			=> 999,
		mp			=> 161,
	},
);



1; # �폜�s��
