# 猜密碼
a = list(input("請輸入第一組數字 : "))
b = list(input("請輸入第二組數字(答案) : "))
a1 = 0 
b1 = 0
if len(a) == len(b):
    for i in range(4):
        if a[i] == b[i]:
            a1 += 1
        elif a[i] in b[i]:
            b1 += 1
    print("%dA%dB" %(a1,b1))
else:
    print("字數不同無法判斷")



