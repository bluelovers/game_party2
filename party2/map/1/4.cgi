# �ő�^�[��
$max_round = 50;

# �}�b�v
@maps = (
	[3,1,0,0,0,0,0,I,3],
	[I,1,0,1,D,1,0,1,1],
	[0,0,0,1,B,1,0,0,0],
	[0,1,1,1,2,1,1,1,0],
	[0,0,0,1,1,1,0,0,0],
	[0,1,0,0,S,0,0,1,1],
	[0,1,0,1,0,1,1,1,K],
	[0,1,0,1,0,0,0,1,0],
	[K,1,0,0,0,1,0,0,0],
);

# �C�x���g
sub event_2 { return if $event =~ /2/; $event .= '2'; &_add_treasure; }
sub event_3 { return if $event =~ /3/; $event .= '3'; &_add_treasure; }
$map_imgs{I} = '��';
$map_imgs{K} = '��' if $event !~ /K/;
$map_imgs{D} = '��' if $event !~ /D/;
sub event_I { $npc_com .= "�Ȃ�ƁI�ǂł͂Ȃ��B���ʘH�ɂȂ��Ă����I"; }
sub event_K { return if $event =~ /K/; $event .= 'K'; $npc_com.="���̌����E�����I";  }
sub event_D {
	return if $event =~ /D/;
	if ($m{job} eq '9') {
		$com .= "<br />$m{mes}" if $m{mes};
		$npc_com .= "$m�ׂ͍��i�C�t�Ɛj���̂悤�Ȃ��̂ŁA���̃J�M����������������I�c����ݯ�I�Ȃ�ƁA�����J�����悤���I";
		$event .= 'D';
	}
	elsif ($event =~ /K/) {
		$npc_com .= "$m�͏E�����J�M���g�r�����ɍ�������ł݂��I�c�޺޺޺޺ށc�d���������ĂĔ����J���Ă����I";
		$event .= 'D';
	}
	else {
		$npc_com .= "$m�͔�����������������肵�Ă݂����A�r�N�Ƃ����Ȃ��c";
		--$py;
	}
}

require "$stagedir/2.cgi";



1; # �폜�s��
