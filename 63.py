# Perfect Number

nu = int(input("請輸入一個數字"))
factor = []
for i in range(1,nu):
    if nu % i == 0 :
        factor.append(i)
s = sum(factor)
if s == nu :
    print("perfect")
elif s > nu :
    print("abundant")
else:
    print("deficient")