# �f�t�H���g
my $_s = int(rand(4)+8);
require "$stagedir/$_s.cgi";

# �m���ɂ��Œ�{�X
if (rand(3)<1) {
@bosses= (
	{
		name		=> '��ذ�',
		hp			=> 7000,
		at			=> 360,
		df			=> 140,
		ag			=> 300,
		get_exp		=> 1500,
		get_money	=> 300,
		icon		=> 'mon/555.gif',
		
		hit			=> 500, # ������p������
		job			=> 70, # �V���l�߂������h���S���p���[�M�K�f�C��
		sp			=> 150,
		old_job		=> 52, # ���l
		old_sp		=> 999,
		mmp			=> 99999,
		mp			=> 4999,
		tmp			=> '�U����',
	},
	{
		name		=> 'گ�޽İ�',
		hp			=> 10,
		at			=> 200,
		df			=> 6000,
		ag			=> 1000,
		get_exp		=> 70,
		get_money	=> 500,
		icon		=> 'mon/190.gif',
		
		job			=> 12, # �����g��
		sp			=> 999,
		old_job		=> 90, # �ғŌn
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '������',
	},
);
}


1; # �폜�s��
