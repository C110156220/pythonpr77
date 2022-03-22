# 計算電量

lim = [120,330,500,700,700]
moneyn= [2.10,2.68,3.61,4.01,4.50]
moneys= [2.10,3.02,4.39,4.97,5.63]
a = ["Summer months","Non-Summer months"]
i = input("請輸入一個度數(正整數)  :")

try :
    int(i)
    yes = True
except ValueError:
    yes = False
    
if yes == True and int(i) > 0:
    i = int(i)
    if   0 < i and i < lim[0] :
        print(a[0],round(i *moneys[0],2))
        print(a[1],round(i *moneyn[0],2))
    elif  i < lim[1] :
        print(a[0],round(120*moneys[0]+(i -120)*moneys[1],2))
        print(a[1],round(120*moneyn[0]+(i -120)*moneyn[1],2))
    elif i < lim[2]:
        print(a[0],round(120*moneys[0]+210*moneys[1]+(i - 330) * moneys[2],2))
        print(a[1],round(120*moneyn[0]+210*moneyn[1]+(i - 330) * moneyn[2],2))
    elif i < lim[3]:
        print(a[0],round(120*moneys[0]+210*moneys[1] + 170 * moneys[2] + (i-500) * moneys[3],2))
        print(a[1],round(120*moneyn[0]+210*moneyn[1] + 170 * moneyn[2] + (i-500) * moneyn[3],2))
    else:
        print(a[0],round(120*moneys[0]+210*moneys[1] + 170 * moneys[2] + 200 * moneys[3] +(i-700)*moneys[4],2))
        print(a[1],round(120*moneyn[0]+210*moneyn[1] + 170 * moneyn[2] + 200 * moneyn[3] +(i-700)*moneyn[4],2))
else :
    print("輸入非整數 OR 負數")

