
a = list(input("請輸入第一個矩陣的大小").split())
b = [[]for i in range(int(a[0]))]
for i in range(int(a[0])):
    b[i] = input("請輸入第一個矩陣第"+str(i+1)+"列的值").split()
    print(b[i])

c = list(input("請輸入第二個矩陣大小").split())

b1 = [[]for i in range(int(c[0]))]
for i in range(int(a[0])):
    b1[i] = input("請輸入第一個矩陣第"+str(i+1)+"列的值").split()
    print(b1[i])

if a == c:
    ans = [[]for i in range(int(a[0]))]
    for i in range(int(a[0])):
        m = []
        for j in range(int(a[1])):
            m.append(int(b[i][j])+int(b1[i][j]))
        ans[i] = m
        print(m)
    
else:
    print("兩矩陣大小不同，無法相加")




        
        

