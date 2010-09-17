#================================================
# �T�C�h���j���[�E�w�b�_�[�E�t�b�^�[ Created by Merino
#================================================
sub side_menu {
	my($contents) = shift;

	my $yid = $ENV{'QUERY_STRING'} ? '?'.$ENV{'QUERY_STRING'} : '';
	my $title_line = $title_img ? qq|<img src="$title_img" alt="$title">| : $title;
	
	print <<"EOM";
<div align="center">
<div id="page">
	<div id="header">
		<table width="100%">
		<tr><td>
		<h1><a href="$script_index">$title_line</a></h1>
		<script type="text/javascript" src="$htmldir/random_icons.js"></script>
		</td><td align="right" valign="bottom">
		</td></tr></table>
	</div>
	<div id="navigation">
		<div class="menu_button"><a href="$script_index$yid">���g�b�v<div class="text_small">�g�b�v�y�[�W</div></a></div>
		<div class="menu_button"><a href="new_entry.cgi$yid">���V�K�o�^<div class="text_small">�������̏��S����ڲ���ĕK��</div></a></div>
		<div class="menu_button"><a href="http://www19.atwiki.jp/atparty2/">��������<div class="text_small">���p�[�e�B�[II�ɂ���</div></a></div>
		<div class="menu_button"><a href="news.cgi$yid">���j���[�X<div class="text_small">�ŋ߂̏o����</div></a></div>
		<div class="menu_button"><a href="contest.cgi$yid">���t�H�g�R��<div class="text_small">�݂�Ȃ��B��������߉f��</div></a></div>
		<div class="menu_button"><a href="$htmldir/player_list.html">����ڲ԰�ꗗ<div class="text_small">�]�E�񐔁A���x����</div></a></div>
		<div class="menu_button"><a href="guild_list.cgi$yid">���M���h����<div class="text_small">�e�M���h�Ƃ��̃����o�[</div></a></div>
		<div class="menu_button"><a href="challenge.cgi$yid">�����E�L�^<div class="text_small">���`�������W�̍ō��L�^�ێ���</div></a></div>
		<div class="menu_button"><a href="ranking.cgi$yid">�������L���O<div class="text_small">���􂵂Ă���g�b�v�v���C���[</div></a></div>
		<div class="menu_button"><a href="legend.cgi$yid">���`������ڲ԰<div class="text_small">�R���v���[�g�v���C���[</div></a></div>
		<div class="menu_button"><a href="job_ranking.cgi$yid">���E�ƃ����L���O<div class="text_small">�l�C�̐E�Ƃ́I�H</div></a></div>
		<div class="menu_button"><a href="rescue.cgi$yid">���~�o����<div class="text_small">�o�O�~�o</div></a></div>
		<!-- div class="menu_button"><a href="delete.cgi$yid">���폜����<div class="text_small">�f�[�^�폜</div></a></div -->
		<div class="menu_button"><a href="$home">���g�n�l�d<div class="text_small">�z�[���y�[�W��</div></a></div>
	</div>
	<div id="contents">
		$contents
	</div>
EOM
}


#================================================
# footer
#================================================
sub footer {
	print qq|<div id="footer">|;
	print qq|+ ���p�[�e�B�[II Ver$VERSION <a href="http://cgi-sweets.com/" target="_blank">CGI-Sweets</a> <a href="http://amaraku.net/" target="_blank">Ama�y.net</a>|; # ����\��:�폜�E��\�� �֎~!!
	print qq|$copyright +</div></div></div></body></html>|;
}

1;
