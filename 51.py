# 自傳重複的字

a = list(input("請輸入自傳或一個句子"))

ap = []
res = []
mark = ['，',"，","。",";",":","[",']','{','}','(',')',"~",'、','"',"'"," "]
for i in range(len(a)):
    ap1 = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            ap1 += 1
    ap.append(ap1)

for i in range(len(ap)):
    if ap[i] > 1:
        if a[i] not in res:
            if a[i] not in mark:
                res.append(a[i])
print(res)