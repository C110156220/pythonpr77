




a = input("請輸入一個數字，判斷之中是否有最大質數:")
for i in range(1):
    for j in range(1):
        c = a[:]
        print(c)
        d = 0
        for k in range(1,int(c)+1):
            if int(c) % k == 0 :
                d += 1
        if d == 2 : 
            print("最高質數為",c)
            break
