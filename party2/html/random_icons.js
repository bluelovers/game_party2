var element = document.getElementById("header");
var h = (new Date()).getHours();
if (h >= 16 && h < 17) {
	element.style.backgroundImage = "url(./bgimg/top2.gif)";
}
else if(h >= 17 && h < 19) {
	element.style.backgroundImage = "url(./bgimg/top3.gif)";
}
else if(h >= 19 && h < 22) {
	element.style.backgroundImage = "url(./bgimg/top4.gif)";
}
else if((h >= 22 && h < 24) || (h >= 0 && h < 4)) {
	element.style.backgroundImage = "url(./bgimg/top5.gif)";
}
else if(h >= 4 && h < 6) {
	element.style.backgroundImage = "url(./bgimg/top6.gif)";
}
else if(h >= 6 && h < 9) {
	element.style.backgroundImage = "url(./bgimg/top7.gif)";
}


for (var i = 1; i <= 8; i++) {
	var n = Math.floor(Math.random() * 70) + 1;
	
	// ’j«ê—pE
	if (n == 13 || n == 15 || n == 17 || n == 19 || n == 47) {
		s = 'm';
	}
	// —«ê—pE
	else if (n == 14 || n == 16 || n == 18 || n == 20 || n == 48) {
		s = 'f';
	}
	else if (Math.floor(Math.random() * 2) == 0) {
		s = 'm';
	}
	else {
		s = 'f';
	}
	
	document.write('<img src="./icon/job/' + n + '_' + s + '.gif">');
}

