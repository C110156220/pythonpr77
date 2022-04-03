# 占卜運勢
m = int(input("請輸入月份"))
d = int(input("請輸入日期"))
deal = (m*2+d)%3
if deal == 0:
    print("普通")
elif deal == 1:
    print("吉")
elif deal == 2:
    print("大吉")
else:
    print("大凶")
