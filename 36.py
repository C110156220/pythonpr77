# 等比或等差數列的判斷

times = int(input("請輸入總共有幾個測試資料"))
for i in range(times):
    a = int(input("請輸入幾個數字"))
    aa = []
    for j in range(a):
        aa.append(int(input("請輸入第"+str(j+1)+"個數字 : ")))
    aa.sort()
    kk = aa[1] - aa[0]
    muli=aa[1] / aa[0]
    pa1 = 0 ; pa2 = 0
    for i in range(len(aa)-1):
        if aa[i]+kk == aa[i+1]:
            pa1 += 1
        elif aa[i]*muli == aa[i+1]:
            pa2 += 1
    if pa1 == len(aa)-1:
        print(aa)
        print()
        print("是等差數列")
    elif pa2 == len(aa)-1:
        print(aa)
        print()
        print("是等比數列")
    else:
        print("不是等差數列也不是等比數列")

        
        