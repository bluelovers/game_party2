# _W¼
$d_name = "$dungeons[$stage]PK";

# Åå^[
$max_round = 30;

# }bv
@maps = (
	[0,F,0],
	[0,0,0],
	[0,A,0],
	[1,0,1],
	[1,0,1],
	[1,0,1],
	[1,S,1],
);


# Cxg
$map_imgs{F} = 'Ê';
$map_imgs{A} = '' if $event !~ /A/;
sub event_F { for my $y (@partys) { $ms{$y}{state} = 'U' }; $map="_1"; $npc_com.="$p_nameÍÌKÖÆiñ¾c"; }
sub event_0 { for my $y (@partys) { $ms{$y}{state} = 'U' }; return if rand(2) > 1; &add_monster; } # ¹
sub event_A { for my $y (@partys) { $ms{$y}{state} = 'U' }; return if $event =~ /A/; $event .= 'A'; &add_boss; } # {X


# GÆóÌÝè
require "$mapdir/10/_data.cgi";

# {X
@bosses= (
	{
		name		=> 'ÅÌpm',
		hp			=> 8000,
		at			=> 300,
		df			=> 100,
		ag			=> 400,
		get_exp		=> 750,
		get_money	=> 250,
		icon		=> 'mon/510.gif',
		job			=> 40, # Ê¸ÞÚÒÀÙ~
		sp			=> 50,
		old_job		=> 58, # ÀÞ°¸´ÙÌ
		old_sp		=> 999,
		mmp			=> 9999,
		mp			=> 999,
		tmp			=> 'zû',
	},
	{
		name		=> '@g¢',
		hp			=> 1200,
		at			=> 250,
		df			=> 80,
		ag			=> 210,
		get_exp		=> 150,
		get_money	=> 30,
		icon		=> 'mon/061.gif',
		job			=> 6, # @g¢
		sp			=> 999,
		old_job		=> 48, # ÂVg
		old_sp		=> 160,
		mp			=> 542,
	},
	{
		name		=> '½×²ÑÜÇ¤',
		hp			=> 1300,
		at			=> 220,
		df			=> 50,
		ag			=> 300,
		get_exp		=> 160,
		get_money	=> 25,
		icon		=> 'mon/013.gif',
		job			=> 19, # Å¹m
		sp			=> 999,
		old_job		=> 40, # Ê¸ÞÚÒÀÙ
		old_sp		=> 999,
		mp			=> 384,
	},
);


1; # ísÂ
