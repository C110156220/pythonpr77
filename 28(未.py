# 逆矩陣


a = []
ans = [[1,0],[0,1]]
for i in range(2):
    a.append(list(input("矩陣大小為2*2，請輸入第"+str(i+1)+"列")))

for i in range(2):
    for j in range(2):
        a[i][j]=int(a[i][j])

for j in range(2):
    t = []
    for k in range(2):
        t.append()