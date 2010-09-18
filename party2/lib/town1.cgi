require './lib/_town.cgi';
#=================================================
# 町１ Created by Merino
#=================================================
# 場所名
$this_title = $towns[0][0];

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/$towns[0][1]";

# 背景画像
$bgimg = "$bgimgdir/stage8.gif";

# 家の値段
$price = 500;

# 家の所有日数(日)
$cycle_house_day = 5;

# 最大建設数
$max_house = 10;

# 建設できる家(./icon/houseの中のファイル名)
@houses = ('001.gif','002.gif','003.gif','004.gif');



1; # 削除不可
