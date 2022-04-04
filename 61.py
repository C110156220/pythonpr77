# 吃兵數
m,s=input("請輸入遊戲時間").split(':')
m = int(m)*60 ; s = int(s)
tt = m+s

round = (tt-75) // 30 
res = 0
# 加一 <1> 因為起始1 ,<2>最後沒有跑到 
for i in range(1,round+2):
    if i % 3 == 0:
        if i % 2 == 0 :
            res += 6
        else :
            res += 7
    else:
        if i % 2 == 0 :
            res += 5
        else :
            res += 6

print(res,"隻兵")
