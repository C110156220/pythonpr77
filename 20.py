# 電影票購買計算
n = int(input("組數為 : "))

for i in range(n):
    m = list(input("第"+str(i+1)+"組").split())
    print("第"+str(i+1)+"組應收費用：",int(m[0])*250+int(m[1])*175)

