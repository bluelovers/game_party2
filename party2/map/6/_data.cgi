# デフォルト
my $_s = int(rand(5)+7);
require "$stagedir/$_s.cgi";

# 固定ボス
sub event_X {
	return if $event =~ /X/;
	$event .= 'X';
	$npc_com.="ただならぬ気配を感じる…。どうやら、このダンジョンのボスのようだ！<br />";

	@bosses= (
		{
			name		=> '一賢者',
			hp			=> 2000,
			at			=> 200,
			df			=> 60,
			ag			=> 200,
			get_exp		=> 600,
			get_money	=> 200,
			icon		=> 'mon/508.gif',

			job			=> 51, # 光魔道士まぶしいひかりひかりのみちびきいやしのひかりあやしいひかり
			sp			=> 80,
			old_job		=> 16, # 白魔道士
			old_sp		=> 999,
			mp			=> 999,
			tmp			=> '魔無効',
		},
		{
			name		=> '二賢者',
			hp			=> 2000,
			at			=> 200,
			df			=> 60,
			ag			=> 200,
			get_exp		=> 600,
			get_money	=> 200,
			icon		=> 'mon/507.gif',
			
			job			=> 15, # 黒魔道士
			sp			=> 80,
			old_job		=> 40, # ハグレメタル
			old_sp		=> 50,
			mp			=> 999,
			tmp			=> '魔吸収',
		},
		{
			name		=> '三賢者',
			hp			=> 2000,
			at			=> 200,
			df			=> 60,
			ag			=> 200,
			get_exp		=> 600,
			get_money	=> 200,
			icon		=> 'mon/509.gif',
			
			job			=> 6, # 魔法使い
			sp			=> 999,
			old_job		=> 19, # 闇魔道士
			old_sp		=> 70,
			mp			=> 999,
			tmp			=> '魔反撃',
		},
	);

	&add_boss;
}



1; # 削除不可
