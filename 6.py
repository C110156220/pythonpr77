# 兩數差值

listx = list(input("請輸入0~9的值，並以逗號隔開 : ").split(","))
M =""
m =""
for i in range(len(listx)):
    listx[i] = int(listx[i])
listx.sort()
for i in range(len(listx)):
    m += str(listx[i])
listx.reverse()
for i in range(len(listx)):
    M += str(listx[i])

print("最大值數列與最小值數列的差值為 : ",int(M)-int(m))