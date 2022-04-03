# 電梯費用

a = int(input("請輸入搭了幾次電梯 : "))
now = "1"
price = 0

for i in range(a):
    next = int(input("請輸入到達哪一樓層"))
    if int(now) < next :
        price += (next - int(now))*20
        now = str(next) 
        

    elif int(now) > next : 
        price += (int(now) - next)*10
        now = str(next)
        

    else :
        price += 0

print("需支付",price,"元")

