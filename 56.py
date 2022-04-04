# 以三角形的方式呈現階層結果

n = int(input("請輸入一個正整數 : "))


for i in range(n+1):
    begin = i
    for j in range(i):
        print("%2d" % (begin+begin*j), end=" ")
    print()
