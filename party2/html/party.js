// �����X�V�̃J�E���g�_�E���\��
function count_down(now_count) {
	if (now_count > 0) {
		now_count = ("00" + now_count).substr(("00" + now_count).length-2, 2);
		document.getElementById("nokori_auto_time").innerHTML = now_count;
		now_count = now_count - 1;
		setTimeout("count_down(" + now_count + ")",1000);
	}
	else {
		document.getElementById("nokori_auto_time").innerHTML = "00";
	}
}

// �A�N�e�B�u�Q�[�W�\��
function active_gage(now_time, act_time) {
	if (now_time > 0) {
		next_time = now_time - 1;
		gage_width = (act_time - now_time) / act_time * 100;
		document.getElementById("gage_back1").innerHTML = '<img src="./html/space.gif" width="' + gage_width + '%" class="gage_bar1" />';
		setTimeout("active_gage(" + next_time + "," + act_time + ")",1000);
	}
	else {
		document.getElementById("gage_back1").innerHTML = '<img src="./html/space.gif" width="100%" class="gage_bar1_full" />';
	}
}

// ���˂�F���ɍs���ł���܂ł̕\��
function wake_time(w_now_time) {
	if (w_now_time >= 0) {
		w_min  = Math.floor(w_now_time / 60);
		w_sec  = Math.floor(w_now_time % 60);
		w_sec  = ("00" + w_sec).substr(("00" + w_sec).length-2, 2);
		w_nokori = w_min + '��' + w_sec + '�b';
		document.getElementById("wake_time").innerHTML = w_nokori;
		w_next_time = w_now_time - 1;
		setTimeout("wake_time(w_next_time)",1000);
	}
}

// �R�����g�t�H�[���ɕ�����Z�b�g
function text_set(text){
	document.form.comment.value = document.form.comment.value + text;
	text_focus();
}

// �R�����g�t�H�[���Ɏ����t�H�[�J�X
function text_focus() {
	if (document.form) {
		document.form.comment.focus();
	}
}


