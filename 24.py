# 求陣列元素最大值的和

M = int(input("請輸入陣列大小"))
a =[[]for i in range(M)]
al =[]

for i in range(M):
    a[i] = input("請輸入第"+str(i+1)+"列數值").split()
    al.extend(a[i])

for i in range(len(al)):
    al[i] = int(al[i])
al.sort();al.reverse()

for i in range(3):
    
    for j in range(M):
        if str(al[i]) in a[j]:
            print("(",j,",",a[j].index(str(al[i])),")" ,end="")


