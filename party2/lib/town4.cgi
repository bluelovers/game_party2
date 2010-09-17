require './lib/_town.cgi';
#=================================================
# 町４ Created by Merino
#=================================================
# 場所名
$this_title = $towns[3][0];

# ログに使うファイル(.cgi抜き)
$this_file  = "$logdir/$towns[3][1]";

# 背景画像
$bgimg = "$bgimgdir/quest.gif";

# 家の値段
$price = 5000;

# 家の所有日数(日)
$cycle_house_day = 20;

# 最大建設数
$max_house = 10;

# 建設できる家(./icon/houseの中のファイル名)
@houses = ('021.gif','022.gif','023.gif','024.gif','025.gif','026.gif','027.gif','028.gif');



1; # 削除不可
