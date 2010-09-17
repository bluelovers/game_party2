# •ó‚Ì’†g
@treasures = (
[35..40], # •ŠíNo
[35..40], # –h‹ïNo
[59,59,59,59,59], # “¹‹ïNo
);

# ƒ{ƒX
@bosses= (
	{
		name		=> '–‚‰¤',
		hp			=> 14000,
		at			=> 650,
		df			=> 350,
		ag			=> 200,
		get_exp		=> 2000,
		get_money	=> 1500,
		icon		=> 'mon/700.gif',
		
		hit			=> 250, # ’·Šúí—p–½’†—¦200%
		job			=> 35, # –‚‰¤
		sp			=> 999,
		old_job		=> 22, # ˆÃ•‹RŽm
		old_sp		=> 999,
		mmp			=> 10000,
		mp			=> 4000,
		tmp			=> 'U”½Œ‚',
	},
	{
		name		=> '¶À½ÄÛÌ¨°',
		hp			=> 15000,
		at			=> 750,
		df			=> 400,
		ag			=> 400,
		get_exp		=> 5000,
		get_money	=> 3000,
		icon		=> 'mon/801.gif',
		
		hit			=> 500, # ’·Šúí—p–½’†—¦500%
		job			=> 97, # ’´UŒ‚Œ^
		sp			=> 999,
		old_job		=> 47, # ¿Ù¼Þ¬°
		old_sp		=> 999,
		mmp			=> 30000,
		mp			=> 8000,
		ten			=> 8,
	},
	{
		name		=> 'Ž€_',
		hp			=> 14000,
		at			=> 600,
		df			=> 250,
		ag			=> 999,
		get_exp		=> 2000,
		get_money	=> 1500,
		icon		=> 'mon/702.gif',
		
		hit			=> 250, # ’·Šúí—p–½’†—¦200%
		job			=> 19, # ˆÅ–‚“¹Žm
		sp			=> 999,
		old_job		=> 46, # ·Þ¬ÝÌÞ×°
		old_sp		=> 999,
		mmp			=> 14000,
		mp			=> 5000,
		tmp			=> '–‚”½Œ‚',
	},
);

# oŒ»—¦(@monsters‚Ì”z—ñ”Ô†‚ª‘½‚¯‚ê‚Î‘½‚¢‚Ù‚ÇoŒ»B‹Ï“™‚ÈoŒ»—¦‚Ìê‡‚ÍA‚©‚çw()x)
@appears = ();


# ƒ‚ƒ“ƒXƒ^[
@monsters = (
	{
		name		=> 'ËÞ¯¸½×²Ñ',
		hp			=> 500,
		at			=> 500,
		df			=> 100,
		ag			=> 500,
		get_exp		=> 120,
		get_money	=> 50,
		icon		=> 'mon/006.gif',
		old_sp		=> 20,
		tmp			=> '‰ñ•œ',
	},
	{
		name		=> 'l–ÊŽ÷',
		hp			=> 700,
		at			=> 550,
		df			=> 200,
		ag			=> 250,
		get_exp		=> 170,
		get_money	=> 140,
		icon		=> 'mon/503.gif',
		old_sp		=> 20,
		job			=> 7, # ¤l
		sp			=> 999,
		mp			=> 263,
		tmp			=> '•œŠˆ',
	},
	{
		name		=> '–S—ìŒ•Žm',
		hp			=> 860,
		at			=> 650,
		df			=> 200,
		ag			=> 150,
		get_exp		=> 180,
		get_money	=> 80,
		icon		=> 'mon/500.gif',
		old_sp		=> 20,
		job			=> 2, # Œ•Žm
		sp			=> 999,
		mp			=> 343,
		tmp			=> 'U”½Œ‚',
	},
	{
		name		=> '·×°¼ªÙ',
		hp			=> 600,
		at			=> 700,
		df			=> 600,
		ag			=> 300,
		get_exp		=> 150,
		get_money	=> 300,
		icon		=> 'mon/215.gif',
		old_sp		=> 20,
		job			=> 1, # íŽm
		sp			=> 999,
		mp			=> 452,
		tmp			=> '–‚”½Œ‚',
	},
	{
		name		=> 'ÃÞËÞÙ¼ªÙ',
		hp			=> 1000,
		at			=> 500,
		df			=> 700,
		ag			=> 200,
		get_exp		=> 160,
		get_money	=> 500,
		icon		=> 'mon/506.gif',
		job			=> 5, # ‘m—µ
		old_sp		=> 30,
		sp			=> 999,
		mp			=> 600,
		tmp			=> '–‚”½Œ‚',
	},
	{
		name		=> 'ºÞ°ÚÑ',
		hp			=> 1200,
		at			=> 500,
		df			=> 700,
		ag			=> 150,
		get_exp		=> 250,
		get_money	=> 150,
		icon		=> 'mon/546.gif',
		old_sp		=> 30,
		job			=> 27, # •—…Žm
		sp			=> 999,
		mp			=> 777,
		tmp			=> 'UŒyŒ¸',
	},
	{
		name		=> 'ˆÅ‚Ì–‚pŽm',
		hp			=> 800,
		at			=> 450,
		df			=> 200,
		ag			=> 200,
		get_exp		=> 180,
		get_money	=> 260,
		icon		=> 'mon/510.gif',
		job			=> 40, # Ê¸ÞÚÒÀÙ
		sp			=> 999,
		mp			=> 300,
		tmp			=> '–‚‹zŽû',
	},
	{
		name		=> '·Þ¶ÞÝÃ½',
		hp			=> 909,
		at			=> 909,
		df			=> 100,
		ag			=> 100,
		get_exp		=> 200,
		get_money	=> 5,
		icon		=> 'mon/563.gif',
		old_sp		=> 20,
		job			=> 21, # ‹¶íŽm
		sp			=> 999,
		mp			=> 909,
		ten			=> 8,
	},
	{
		name		=> '‚Ð‚­‚¢‚Ç‚è',
		hp			=> 1100,
		at			=> 530,
		df			=> 270,
		ag			=> 380,
		get_exp		=> 180,
		get_money	=> 180,
		icon		=> 'mon/530.gif',
		job			=> 26, # ”EŽÒ
		sp			=> 999,
		old_job		=> 27, # •—…Žt
		old_sp		=> 999,
		mp			=> 997,
		tmp			=> '‘§ŒyŒ¸',
	},
	{
		name		=> 'ÍÞË°Ó½',
		hp			=> 909,
		at			=> 777,
		df			=> 255,
		ag			=> 555,
		get_exp		=> 211,
		get_money	=> 99,
		icon		=> 'mon/553.gif',
		job			=> 23, # —³‹RŽm
		sp			=> 999,
		old_job		=> 25, # ƒ‚ƒ“ƒN
		old_sp		=> 999,
		mp			=> 909,
		tmp			=> '‘å–hŒä',
	},
	{
		name		=> '·Ý¸Þ½×²Ñ',
		hp			=> 1200,
		at			=> 500,
		df			=> 300,
		ag			=> 500,
		get_exp		=> 200,
		get_money	=> 250,
		icon		=> 'mon/516.gif',
		old_sp		=> 20,
		job			=> 21, # ‹¶íŽm
		sp			=> 999,
		mp			=> 999,
		tmp			=> 'U–³Œø',
	},
	{
		name		=> 'Ž€—ì‚Ì‹RŽm',
		hp			=> 1200,
		at			=> 666,
		df			=> 280,
		ag			=> 280,
		get_exp		=> 240,
		get_money	=> 170,
		icon		=> 'mon/566.gif',
		job			=> 24, # –‚Œ•Žm
		sp			=> 999,
		old_job		=> 2, # Œ•Žm
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> 'Žó—¬‚µ',
	},
	{
		name		=> '—³‰¤',
		hp			=> 1500,
		at			=> 750,
		df			=> 440,
		ag			=> 200,
		get_exp		=> 250,
		get_money	=> 200,
		icon		=> 'mon/560.gif',
		job			=> 41, # ÄÞ×ºÞÝ
		sp			=> 999,
		old_job		=> 25, # ÓÝ¸A
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '‘§”½Œ‚',
	},
);



1;
