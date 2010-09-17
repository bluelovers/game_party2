# •ó‚Ì’†g
@treasures = (
[1..39], # •ŠíNo
[1..39], # –h‹ïNo
[1..109,125..126,130..134], # “¹‹ïNo
);

# ƒ{ƒX
@bosses= (
	{
		name		=> 'lH‚¢” ',
		hp			=> 1000,
		at			=> 350,
		df			=> 50,
		ag			=> 400,
		get_exp		=> 200,
		get_money	=> 400,
		icon		=> 'mon/090.gif',
		
		old_sp		=> 20,
		job			=> 92, # –°‚èŒn
		sp			=> 999,
		mp			=> 500,
		tmp			=> '‚Q”{', 
	},
	{
		name		=> 'ÐÐ¯¸',
		hp			=> 1500,
		at			=> 360,
		df			=> 100,
		ag			=> 700,
		get_exp		=> 400,
		get_money	=> 800,
		icon		=> 'mon/091.gif',
		
		hit			=> 150, # ’·Šúí—p–½’†—¦150%
		old_sp		=> 20,
		job			=> 93, # ‘¦Ž€
		sp			=> 999,
		mp			=> 500,
		tmp			=> '‚Q”{', 
	},
	{
		name		=> 'ÊßÝÄÞ×ÎÞ¯¸½',
		hp			=> 2000,
		at			=> 370,
		df			=> 150,
		ag			=> 800,
		get_exp		=> 600,
		get_money	=> 1000,
		icon		=> 'mon/092.gif',
		
		hit			=> 150, # ’·Šúí—p–½’†—¦150%
		old_sp		=> 20,
		job			=> 93, # ‘¦Ž€
		sp			=> 999,
		mp			=> 999,
		tmp			=> '‚Q”{', 
	},
	{
		name		=> 'Ä×¯ÌßÎÞ¯¸½',
		hp			=> 2500,
		at			=> 380,
		df			=> 200,
		ag			=> 900,
		get_exp		=> 800,
		get_money	=> 2000,
		icon		=> 'mon/575.gif',

		hit			=> 200, # ’·Šúí—p–½’†—¦150%
		job			=> 19, # ˆÅ–‚“¹Žm
		sp			=> 999,
		old_job		=> 93, # ‘¦Ž€
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '‚Q”{', 
	},
);

# oŒ»—¦(@monsters‚Ì”z—ñ”Ô†‚ª‘½‚¯‚ê‚Î‘½‚¢‚Ù‚ÇoŒ»B‹Ï“™‚ÈoŒ»—¦‚Ìê‡‚ÍA‚©‚çw()x)
@appears = ();


# ƒ‚ƒ“ƒXƒ^[
@monsters = (
	{ # 0
		hit			=> 70,
		name		=> 'ºÛË°Û°',
		hp			=> 270,
		at			=> 300,
		df			=> 150,
		ag			=> 150,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/100.gif',

		old_sp		=> 20,
		job			=> 34, # —EŽÒ
		sp			=> 999,
		mp			=> 200,
	},
	{ # 1
		hit			=> 70,
		name		=> 'ºÛÌ§²À°',
		hp			=> 280,
		at			=> 320,
		df			=> 250,
		ag			=> 50,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/101.gif',

		old_sp		=> 20,
		job			=> 1, # íŽm
		sp			=> 999,
		mp			=> 100,
	},
	{ # 2
		hit			=> 70,
		name		=> 'ºÛÏ°¼Þ',
		hp			=> 240,
		at			=> 150,
		df			=> 100,
		ag			=> 300,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/102.gif',

		job			=> 6, # –‚–@Žg‚¢
		sp			=> 999,
		mp			=> 400,
	},
	{ # 3
		hit			=> 70,
		name		=> 'ºÛÌßØ°½Ä',
		hp			=> 250,
		at			=> 200,
		df			=> 150,
		ag			=> 200,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/103.gif',

		job			=> 5, # ‘m—µ
		sp			=> 999,
		mp			=> 300,
	},
	{ # 4
		name		=> 'ÌßÁË°Û°',
		hp			=> 320,
		at			=> 280,
		df			=> 150,
		ag			=> 150,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/105.gif',

		old_sp		=> 20,
		job			=> 34, # —EŽÒ
		sp			=> 999,
		mp			=> 250,
	},
	{ # 5
		name		=> 'ÌßÁÌ§²À°',
		hp			=> 340,
		at			=> 320,
		df			=> 250,
		ag			=> 50,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/106.gif',

		old_sp		=> 20,
		job			=> 1, # íŽm
		sp			=> 999,
		mp			=> 150,
	},
	{ # 6
		name		=> 'ÌßÁÏ°¼Þ',
		hp			=> 250,
		at			=> 150,
		df			=> 100,
		ag			=> 300,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/107.gif',

		job			=> 6, # –‚–@Žg‚¢
		sp			=> 999,
		mp			=> 300,
	},
	{ # 7
		name		=> 'ÌßÁÌßØ°½Ä',
		hp			=> 270,
		at			=> 200,
		df			=> 150,
		ag			=> 200,
		get_exp		=> 99,
		get_money	=> 50,
		icon		=> 'mon/108.gif',

		job			=> 5, # ‘m—µ
		sp			=> 999,
		mp			=> 250,
	},
);



1;
