# 孿生質數

a = []
for i in range(2):
    a.append(int(input("請輸入第"+str(i)+"個數字")))

if a[0] % 2 == 1 and a[1] % 2 == 1:
    if abs(a[0] - a[1]) == 2:
        print("Y")
    else:
        print("N")
else:
    print("N")
