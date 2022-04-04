# 硬幣及紙鈔的數量
tp = [100,50,10,5,1]
a = 0
money = int(input("請輸入金額 : "))

for i in range(len(tp)):
    a += money // tp[i]
    money = money % tp[i]

print(a)
