# 2D座標判斷及計算原點距離
x = int(input("請輸入X軸座標"))
y = int(input("請輸入Y軸座標"))

d = (x**2+y**2)
if x != 0 and y == 0:
    if x > 0 :
        print("該點位於右半平面X軸上，離原點距離為",abs(x))
    else:
        print("該點位於左半平面X軸上，離原點距離為",abs(x))
elif x == 0 and y != 0:
    if y > 0 :
        print("該點位於上半平面Y軸上，離原點距離為",abs(y))
    else :
        print("該點位於下半平面Y軸上，離原點距離為",abs(y))
elif x == 0 and y == 0:
    print("該點位於原點")
elif x > 0 :
    if y > 0  :
        print("該點位於第一象限，離原點距離為根號",d)
    elif y < 0 :
        print("該點位於第四象限，離原點距離為根號",d)
elif x < 0:
    if y > 0  :
        print("該點位於第二象限，離原點距離為根號",d)
    elif y < 0 :
        print("該點位於第三象限，離原點距離為根號",d)
else :
    print("發生非預期錯誤")