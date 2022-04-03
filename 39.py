# 迴圈練習
n = int(input("請輸入層數以利輸出菱形"))
mid =int(round(n/2,0)) 
print(mid)
for i in range(n+1):
    if i <= mid :
        for j in range(mid-i):
            print(" " ,end="")
        for k in range(2*i-1):
            print("*" ,end="")
    else:
        for j in range(i - mid):
            print(" ",end="")
        for k in range(1,(n+3),i-mid):
            print("*",end="")
    print()
