# �f�t�H���g
my $_s = int(rand(5)+7);
require "$stagedir/$_s.cgi";

# �Œ�{�X
sub event_X {
	return if $event =~ /X/;
	$event .= 'X';
	$npc_com.="�����Ȃ�ʋC�z��������c�B�ǂ����A���̃_���W�����̃{�X�̂悤���I<br />";

	@bosses= (
		{
			name		=> '�ꌫ��',
			hp			=> 2000,
			at			=> 200,
			df			=> 60,
			ag			=> 200,
			get_exp		=> 600,
			get_money	=> 200,
			icon		=> 'mon/508.gif',

			job			=> 51, # �������m�܂Ԃ����Ђ���Ђ���݂̂��т����₵�̂Ђ��肠�₵���Ђ���
			sp			=> 80,
			old_job		=> 16, # �������m
			old_sp		=> 999,
			mp			=> 999,
			tmp			=> '������',
		},
		{
			name		=> '�񌫎�',
			hp			=> 2000,
			at			=> 200,
			df			=> 60,
			ag			=> 200,
			get_exp		=> 600,
			get_money	=> 200,
			icon		=> 'mon/507.gif',
			
			job			=> 15, # �������m
			sp			=> 80,
			old_job		=> 40, # ʸ�����
			old_sp		=> 50,
			mp			=> 999,
			tmp			=> '���z��',
		},
		{
			name		=> '�O����',
			hp			=> 2000,
			at			=> 200,
			df			=> 60,
			ag			=> 200,
			get_exp		=> 600,
			get_money	=> 200,
			icon		=> 'mon/509.gif',
			
			job			=> 6, # ���@�g��
			sp			=> 999,
			old_job		=> 19, # �Ŗ����m
			old_sp		=> 70,
			mp			=> 999,
			tmp			=> '������',
		},
	);

	&add_boss;
}



1; # �폜�s��
