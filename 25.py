# 學期成績計算 

data = [[70,80,90,80,100,80],[60,70,80,70,40,70],[30,50,40,60,50,40]]
rate = []
n,m=input("請輸入考試次數及考生人數 : ").split()
n = int(n); m =int(m)
rate.extend((input("請輸入這"+str(n)+"次的考試比率 :").split()))

for i in range(n):
    rate[i] = float(rate[i])
result = []
for i in range(m):
    T =[]
    for j in range(n):
        T.append(data[i][j]*rate[j])
        
    result.append(sum(T))
    
print("全班的總平均分數為%.2f分" %(sum(result)/m))


