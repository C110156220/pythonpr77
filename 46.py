# 運動會獎牌及獎牌數(使用字典方式)
n = int(input("請輸入比數(輸入4將輸出各類獎牌數，其餘為輸入獎牌)"))
data = {"金":4,"銀":4,"銅":4,"優":4}

if n == 4:
    for i in data:
        print(i+"牌得到共"+str(data[i])+"面")
else:
    print("獎牌種類 :金、銀、銅、優")
    for j in range(4):
        medal,Q = input("請輸入哪類型獎牌及數量(以空白隔開)").split()
        Q = int(Q)
        data[medal] = Q
    print('更新後')
    for i in data:
        print(i+"牌得到共"+str(data[i])+"面")
