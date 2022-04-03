# 檢查數值是否重複

a =int(input("請輸入第一行正整數為...?"))
b = list(input("第二行中數列中的數字為: ").split())
rptm = []
for i in range(a):
    c = 0 
    for j in range(a):
        if b[i] ==b[j] :
            c += 1
    rptm.append(c)

if sum(rptm) == a :
    print("每個數字剛好只出現一次")
else :
    print("最大出現次數為",b[rptm.index(max(rptm))])
    print()
    print("出現次數為",max(rptm))
