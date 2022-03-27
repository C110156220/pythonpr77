# 販賣機

have = int(input("請輸入小名現在擁有多少錢"))
type = int(input("請輸入販賣機有幾種飲料"))
price = []
can = 0
for i in range(type):
    price.append(int(input("請輸入第"+str(i+1)+"種飲料的價錢")))
    if price[i] <= have :
        can += 1

print("小名可以買",can,"種飲料")
    
