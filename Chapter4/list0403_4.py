# 生まれたときから経過した日数
import datetime

today = datetime.date.today()
date_of_year = int(input("生まれた年を入力:"))
date_of_month = int(input("生まれた月を入力:"))
date_of_day = int(input("生まれた日を入力:"))

birth = datetime.date(date_of_year, date_of_month, date_of_day)
diff = today - birth
print("生まれてから今日までの経過日数は: ", diff)
