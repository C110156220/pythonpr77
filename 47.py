# 運動會獎牌及獎牌數(使用串列方式)a

data =[[],[]]
n = int(input("請輸入比數n : "))
for i in range(n):
    medal,Q=input("請輸入獎牌類型及數量(並以空白隔開) :").split()
    data[0].append(medal),data[1].append(Q)
for j in range(len(data[0])):
    print(data[0][j]+"牌共拿到了"+data[1][j]+"個")
