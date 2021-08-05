# 時分秒を出力する

import datetime

d = datetime.datetime.now() # <- 変数dに現在時刻のデータを代入
print(d.hour)   # <- 時
print(d.minute) # <- 分
print(d.second) # <- 秒

print(d.year)   # <- 年
print(d.month)  # <- 月
print(d.day)    # <- 日
