# 走私的狗狗


n = int(input("請輸入整數n，代表狗狗可能跑到n個地方"))
k = []
for i in range(n):
    k.append(int(input("請輸入離家大概公里 ? ")))
er = 0
for j in range(len(k)):
    if k[j] % 7 == 0 or k[j] % 11 == 0 :
        print("第"+str(j+1)+"個點 : "+str(k[j]))
    else:
        er += 1

if er == n :
    print("0，都不是狗狗會離家的距離")
    

