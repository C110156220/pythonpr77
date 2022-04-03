# 發明新公倍數
num = int(input("請輸入一數字 : ")) ; r = False
if num % 2 == 0 and num % 11 == 0:
    if num % 5 != 0 and num % 7 != 0 :
        r = True
if r == True:
    print(num,"是新公倍數嗎? YES")
else:
    print(num,"是新公倍數嗎? NO")