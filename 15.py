# 數字加密
a = list(input("請輸入一組四位數字"))

if len(a) == 4 :
    for i in range(len(a)):
       a[i]=  (int(a[i])+7) % 10
    
    b = a[2]
    a[2] = a[0]
    a[0] = b

    c = a[1]
    a[1] = a[3]
    a[3] = c

    d =""
    for i in range(len(a)):
        d += str(a[i])

    print("輸出加密後的數字為",d)
else:
    print("並非輸入4位數字")