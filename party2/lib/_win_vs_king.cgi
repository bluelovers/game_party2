#=================================================
# �j���f�[�^ Created by Merino
#=================================================
# �j���̊J�Î���(����)
$c_hour = 2;

# �����P�����ɂ����l�W�܂�
$c_people = 2 + int(rand(4));

# �����P�����ɂ��u��
$c_mono   = 1 + int(rand(2));

# �F
@c_colors = (qw/#FF33FF #FF3333 #33CCFF #FFCCCC #FF33CC #FF9933 #FFFF33 #33FF33 #33CCFF #6666FF #CC66FF #CCCCFF #FFFFFF #33FF99/);

# ���O�Ɖ摜�����_��(�l���n)
@c_randoms = (qw/��� �߹ �ߺ ���� ��� úú ҿ ��� �ެݸ� �ް� İ� ��ذ ��� ��޶ް �ذ �ư ��ذ ��ذ �߰� �ؽ ��� ��� �ذ �ذ �ؽ �ؽ �ذ Ѱ� Ӱ� Ҳ ��ި ů�� �߲� ���� ���� �ް�� �ؽ ��� ���ް ���� ��̫ ���� ֳ�� �߯�� �۰� ��۰ ·� ��� ���� ����� �ذ� �ح� ��� �Ⱥ ��ĺ ��ڹ�� ���ݺ� ��� �߯�� ��� �ު� �ެ�� �ޮ� �ޮư �ު�/);
@c_imgs    = (1..35);

# ���O�Ɖ摜�Œ�(�u���n)
@c_fixeds  = (
	['����',		'item/010.gif'],
	['�ݽ���',		'item/010.gif'],
	['���������',	'item/010.gif'],
	['ʰ��è�',		'item/011.gif'],
	['���ް��',		'item/020.gif'],
	['����ް��',	'item/020.gif'],
	['��',			'item/020.gif'],
	['�ڰײ�',		'item/023.gif'],
	['�ذײ�',		'item/023.gif'],
	['ײ��ڰ',		'item/023.gif'],
	['��ײ�',		'item/021.gif'],
	['������ײ�',	'item/021.gif'],
	['��߹�è',		'item/022.gif'],
	['�����',		'item/021.gif'],
	['��ݽ����',	'item/016.gif'],
	['���¼ޭ��',	'item/016.gif'],
	['��̂̈��ݖ�',	'item/016.gif'],
	['�Ӱق̐�',	'item/015.gif'],
	['����',		'item/015.gif'],
	['�j��',		'item/015.gif'],
	['�����',		'chr/023.gif'],
	['���۳',		'chr/023.gif'],
	['�ϼ�۳',		'chr/023.gif'],
	['�ϯ��',		'chr/023.gif'],
	['�����',		'chr/023.gif'],
	['���',			'chr/022.gif'],
	['�۹�',		'chr/022.gif'],
	['����',		'chr/022.gif'],
	['�۽�',		'chr/022.gif'],
	['ҪҪ',		'chr/019.gif'],
	['�¼�',		'chr/019.gif'],
	['����',		'chr/019.gif'],
);

$c_hour--;
open my $fh, ">> $logdir/event_member.cgi" or &error("$logdir/event_member.cgi�t�@�C�����J���܂���");
for my $i (1..$c_people) {
	my $ran_time = $time + $c_hour * 3600 + int(rand(3600)); # rand(3600): �l�����Ȃ��Ȃ�̂Ɏ���������
	my $c_random = $c_randoms[int rand @c_randoms ];
	my $c_img    = sprintf("chr/%03d.gif", $c_imgs[int rand @c_imgs]);
	my $c_color  = $c_colors[ int rand @c_colors  ];
	print $fh "$ran_time<>0<>$c_random<>0<>$c_img<>$c_color<>\n";
}
for my $i (1..$c_mono) {
	my $ran_time = $time + $c_hour * 3600 + int(rand(3600)); # rand(3600): �l�����Ȃ��Ȃ�̂Ɏ���������
	my $j = int(rand(@c_fixeds));
	my $c_color  = $c_colors[ int rand @c_colors  ];
	print $fh "$ran_time<>0<>$c_fixeds[$j][0]<>0<>$c_fixeds[$j][1]<>$c_color<>\n",
}
close $fh;



1; # �폜�s��
