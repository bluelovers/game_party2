require './lib/system.cgi';
#================================================
$VERSION = '1.30';
# �ݒ�t�@�C�� Created by Merino
#================================================
# �Ǘ���ʂ�URL
# http://������URL/party/admin.cgi?pass=�Ǘ��҃p�X���[�h
# ���u������URL�v�Ƃ͂���CGI��ݒu�����ꏊ�܂ł̃A�h���X
#================================================
# �����e�i���X�\��(��) �ʏ�ғ����́u0�v
$mente_min = 0;

# �Ǘ��p�X���[�h(�K���Ȕ��p�p�����ɕK���ύX���Ă�������)
$admin_pass = '0123';

# ���ɍs���ł���܂ł̑҂�����(�b)�B�퓬�p�̑҂����Ԃ́u./lib/quest.cgi��%speeds�v�Őݒ�
$act_time = 7;

# �҂����Ԃ̃Q�[�W�̉���(px)
$gage_width = 140;

# �������ԁu���˂�v�̍S������(��)
$sleep_time = 10;

# gzip���k�]��(�킩��Ȃ��E�g��Ȃ��ꍇ�͋� '' )
$gzip = '';

# ----------------------------
# �^�C�g��
$title = '���p�[�e�B�[II';

# �^�C�g���摜(�K�v�Ȃ��ꍇ�́u''�v)
$title_img = './icon/etc/title.png';

# �߂��URL
$home = 'http://tenaku.com/';

# �ݒuPath(/index.cgi��������http://�`��URL)�u���O�p�[�c�p�����N
$game_path = 'http://party.xii.jp';

# ----------------------------
# �ő�o�^�l��
$max_entry = 200;

# �ő働�O�C���l��
$max_login = 30;

# Top�̃��O�C�����X�g�ɕ\�����鎞��(��)
$login_time = 15;

# �����폜����(��)�B���̓��ɂ��𒴂��Ă����O�C�����Ȃ����[�U�[�͍폜
$auto_delete_day = 30;

# ----------------------------
# �E���ɕ\������钘��\���BHTML�^�O�g�p�\(�u$copyright = <<"EOM";�v�`�uEOM�v�̊ԂɋL�q)
$copyright = <<"EOM";
<!-- �������� -->



<!-- �����܂� -->
EOM

# ----------------------------
# �ő働�O�ۑ�����
$max_log     = 30;

# �ő�R�����g������(���p)
$max_comment = 500;

# ���v���C���[�ɂ��莆�̘A���������݋֎~����(�b)
$bad_time    = 30;

# �ő�X�N���[���V���b�g������
$max_screen_shot = 20;


# ----------------------------
# �����o�[�Ƃ��ĕ\������鎞��(�b)
$limit_member_time = 60 * 5;

# ���������[�h����(�b) ���ǉ�/�ύX/���ёւ����R
@reload_times = (0, 10, 15, 20, 30, 60, 90);

# �X�V(F5)�A�Ŗh�~�B���̕b���ԂɍX�V����ƃG���[(�b)
$wait_time = 1;


# ----------------------------
# �f�t�H���g�J���[
$default_color = '#FFFFFF';

# �f�t�H���g��NPC��
$npc_name  = '��',

# �f�t�H���g��NPC�J���[
$npc_color = '#FF69B4',


# ----------------------------
# �퓬�ɕK�v�ȕϐ�(�ǉ��\)
@battle_datas = (qw/name addr color time ten job sp old_job old_sp mhp hp mmp mp mat at mdf df mag ag hit state tmp get_exp get_money icon wea arm/);

# �J�W�m�ɕK�v�ȕϐ�(�ǉ��\)
@casino_datas = (qw/name addr color time icon action card/);


# �`���ꏊ(./stage/��.cgi�Ɗ֘A�Â��Ă���B���₷�ꍇ��./stage/��.cgi�����₷)
@stages = ('�v�j�v�j����','�L�m�R�̐X','�H���','�C�ӂ̓��A','�n���̍��l','���p�t�̓�','�r��̏b��','�}�O�}�R','�d���̐X','�X���C�������h','����̏��n','�h���S���̒J','�Í�����','���̑�n','���E',
#           0              1            2        3            4            5            6            7          8          9                10           11             12         13         14
           '���̐��E','�}�_���K�[�f��','���̔鋫','�ł̃����v','����̒n','�V���','�J�I�X�t�B�[���h',
#           15         16               17         18           19         20       21
);

# ���_���W����(./map/��/�Ɗ֘A�Â��Ă���B���₷�ꍇ��./map/��/�����₷)
@dungeons = ('�N���N�̓��A','���k�[����','�g�[�X��','�����̐X','���̑���H','���̐_�a','���҂̏���','���̓��A','��]�̍���','�͂̓��A','���@�̓�','�w�u���Y�h�A','�w���Y�Q�[�g');
#             0              1            2          3          4            5          6            7          8            9          10         11,            12 

# ���`�������W(./challenge/��/�Ɗ֘A�Â��Ă���B���₷�ꍇ��./challenge/��/�����₷)
@challenges = ('�Ŏ�t�P','�{�r�q��','���|�̎�','���o�ғ�','��������','�ԉΑ��','�S�Ǘv��','�ŋ�����',);
#               0          1          2          3          4          5          6          7

# ���܂�
@towns = (
	['���P���P��',		'town1'], # 0
	['�L�m�R��',		'town2'], # 1
	['�X���C����',		'town3'], # 2
	['�K�C�A��',		'town4'], # 3
);


# �����ǂ�
@places = (
	# �ꏊ��,				�g�p���郉�C�u����(./lib/******.cgi)
	['�`���ɏo��',			'quest'],
	['�J�W�m',				'casino'],
	['�a���菊',			'depot'],
	['���퉮',				'weapon'],
	['�h�',				'armor'],
	['���',				'item'],
	['���C�[�_�̎���',		'bar'],

	['������',				'lot'],
	['�����X�^�[��������',	'farm'],
	['�t�H�g�R�����',		'photo'],
	['�I���N����',			'goods'],
	['���_�����̏�',		'medal'],
	['�_�[�}�_�a',			'job_change'],
	['�𗬍L��',			'park'],

	['�I�[�N�V�������',	'auction'],
	['�C�x���g�L��',		'event'],
	['�肢�̐�',			'sp_change'],
	['�����̍Ւd',			'reborn'],
	['�M���h����',			'join_guild'],
	['�����̊�',			'name_change'],
	['�Ǖ��R�m�c',			'exile'],
);

#=================================================
# �l�̓��{��ǂ� ���ǉ�/�ύX/���ёւ����R
#=================================================
%e2j = ( # English to Japanese
	sex		=> '����',
	m		=> '�j',
	f		=> '��',
	mhp		=> '�g�o',
	mmp		=> '�l�o',
	hp		=> '�g�o',
	mp		=> '�l�o',
	at		=> '�U����',
	df		=> '�����',
	ag		=> '�f����',
	hit		=> '������',
	state	=> '���',
	sp		=> 'SP',
	lv		=> 'Lv.',
	exp		=> '�o���l',
	money	=> '�S�[���h',
	tired	=> '��J',
);



#================================================
# �X�p��/�r�炵�΍��ݒ�
#================================================
# �A�N�Z�X���ێ҂ւ̃��b�Z�[�W
$deny_message = '���Ȃ���IP�A�h���X�̓A�N�Z�X�������������Ă��܂�';

# �A�N�Z�X���ۃ��X�g�u '�֎~IP�A�h���X�܂��̓z�X�g��', �v
# �A�X�^���X�N(*)�őO����v(��> '*.proxy',)�A�����v(��> '127.0.0.*',)
@deny_lists = (
	'*.anonymizer.com',
);

#================================================
# �e�t�@�C���ݒ�
#================================================
$userdir  = './user';
$icondir  = './icon';
$bgimgdir = './bgimg';
$guilddir = './guild';
$logdir   = './log';
$questdir = './quest';
$casinodir = './casino';
$htmldir  = './html';
$stagedir = './stage';
$mapdir   = './map';
$challengedir = './challenge';
$script       = 'party.cgi';
$script_index = 'index.cgi';

$method = 'POST';
$chmod  = 0666;
$mkdir  = 0777;


1; # �폜�s��
