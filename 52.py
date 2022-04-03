# 找出兩首詩共同的字
data1 = list("春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。")
data2 = list("紅豆生南國，春來發幾枝。願君多采擷，此物最相思。")
ap = []

for i in range(len(data1)):
    ap1 = 0
    for j in range(len(data2)):
        if data1[i] == data2[j] :
            ap1 += 1
    ap.append(ap1)
res = []
for i in range(len(ap)):
    if ap[i] == 1 :
        res.append(data1[i])

print(res)
