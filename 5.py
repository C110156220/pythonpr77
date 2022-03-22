# 階層判斷
M = int(input("請輸入階層值 : "))
i,N = 1,1
while True :
    if M < N : 
        print("超過M為",M,"的最小階層N值為",i)
        break
    i = i + 1    
    N = N * i
    
    
