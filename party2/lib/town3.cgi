require './lib/_town.cgi';
#=================================================
# 町３ Created by Merino
#=================================================
# 場所名
$this_title = $towns[2][0];

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/$towns[2][1]";

# 背景画像
$bgimg = "$bgimgdir/stage16.gif";

# 家の値段
$price = 3000;

# 家の所有日数(日)
$cycle_house_day = 15;

# 最大建設数
$max_house = 10;

# 建設できる家(./icon/houseの中のファイル名)
@houses = ('013.gif','014.gif','015.gif','016.gif','017.gif','018.gif','019.gif','020.gif');



1; # 削除不可
