# 找出數字字串中的最大質數

s = input("請輸入數字 : ")
res = []
for i in range(0,len(s)):
    for j in range(i+1):
        say = int(s[j:len(s)-i+j])
        if say % 2 == 1 :
            sayl = []
            for k in range(1,say+1):
                if say % k == 0 :
                    sayl.append(k)
            if len(sayl) == 2 : res.append(say)

if len(res) == 0:
    print("子字串中最大的質數是 : No prime found")
else:
    if len(res) == 1 and 1 in res:
        print("子字串中最大的質數是 : No prime found")
    else:
        print("子字串中最大的質數是 : ",max(res))



# 12345
# 12345 --> s[0:5]
# 1234 -->s[0:4] ; 2345 --> s[1:5]
# 123 --> s[0:3] ; 234 --> s[1:4] ; 345 --> s[2:5]
# 12 --> s[0:2] ; 23 --> s[1:3] ; 34 --> s[2:4] ;45 --> s[3:5]
