# 計算車資
km = float(input("請輸入搭乘里程數(km) : "))

if km < 1.5 :
    print("所需車費:75元" )
else :
    bonus =(int(km*1000)-1500) / 250 
    if (int(km*1000)-1500) % 250 != 0 : bonus += 1 
    print("所需車費:%d元"%(75+bonus*5) )