# 最大公因數

a = list(input("請輸入超過兩個正整數").split(","))
rem = []
if len(a) > 1:
    pos = True
    for i in range(len(a)):
        a[i] = int(a[i])
        if a[i] < 0 :
            pos = False
    if pos == True:
        for j in a:
            for i in range(1,j):
                if j % i == 0:
                    rem.append(i)
        print(max(rem))

    else:
        print("輸入負數無法判斷")
else :
    print("並非輸入兩個正整數或輸入負數")
