require './lib/_town.cgi';
#=================================================
# 町２ Created by Merino
#=================================================
# 場所名
$this_title = $towns[1][0];

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/$towns[1][1]";

# 背景画像
$bgimg = "$bgimgdir/park.gif";

# 家の値段
$price = 1500;

# 家の所有日数(日)
$cycle_house_day = 10;

# 最大建設数
$max_house = 10;

# 建設できる家(./icon/houseの中のファイル名)
@houses = ('005.gif','006.gif','007.gif','008.gif','009.gif','010.gif','011.gif','012.gif');



1; # 削除不可
