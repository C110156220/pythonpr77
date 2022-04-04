# 共同出現的英文字母

a = list(input("請輸入第一個字串"))
b = list(input("請輸入第二個字串"))
alp = []
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            if a[i] not in alp:
                alp.append(a[i])

alp.sort();res =""
if len(alp) > 0:
    for i in range(len(alp)):
        res += alp[i]
    print(res)
else:
    print("N")