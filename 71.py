# 轉換成三進位


a1 = int(input("請輸入十進位的正整數 : "));a = a1
res = [] ; res1 =""
while True :

    b = a % 3 
    a = a // 3 
    res.append(b)
    if a == 0:
        break
res.reverse()
for i in range(len(res)):
    res1 += str(res[i])
print(str(a1)+"的三進位為",str(res1)) ;
    

 