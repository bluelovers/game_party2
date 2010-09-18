# デフォルト
my $_s = int(rand(4)+8);
require "$stagedir/$_s.cgi";

# 確率により固定ボス
if (rand(3)<1) {
@bosses= (
	{
		name		=> 'イフリート',
		hp			=> 7000,
		at			=> 360,
		df			=> 140,
		ag			=> 300,
		get_exp		=> 1500,
		get_money	=> 300,
		icon		=> 'mon/555.gif',
		
		hit			=> 500, # 長期戦用命中率
		job			=> 70, # 天竜人めいそうドラゴンパワーギガデイン
		sp			=> 150,
		old_job		=> 52, # 魔人
		old_sp		=> 999,
		mmp			=> 99999,
		mp			=> 4999,
		tmp			=> '攻無効',
	},
	{
		name		=> 'レッドストーン',
		hp			=> 10,
		at			=> 200,
		df			=> 6000,
		ag			=> 1000,
		get_exp		=> 70,
		get_money	=> 500,
		icon		=> 'mon/190.gif',
		
		job			=> 12, # 魔物使い
		sp			=> 999,
		old_job		=> 90, # 猛毒系
		old_sp		=> 999,
		mp			=> 999,
		tmp			=> '魔無効',
	},
);
}


1; # 削除不可
