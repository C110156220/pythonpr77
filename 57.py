# 麥當勞消費

from re import A


combo = list(input("請輸入主餐及升級的套餐 : "))
combo[0] = int(combo[0])
biggerd = input("是否要升級大杯飲料 : ")
biggerf = input("是否要升級大薯 : ")

data1 = [0,72,62,82,44,60]
data2 = [55,68]
add = [7,13]
if len(combo) == 2:
    if combo[0] >= 1 and combo[0] <=5:
        if combo[1] == "A":
            if biggerd == "是":
                if biggerf == "是": 
                    print("總共為",data1[combo[0]]+data2[0]+add[0]+add[1],"元")
                
                else:
                    print("總共為",data1[combo[0]]+data2[0]+add[0],"元")
            else:
                if biggerf == "是": 
                    print("總共為",data1[combo[0]]+data2[0]+add[1],"元")
                
                else:
                    print("總共為",data1[combo[0]]+data2[0],"元")
        elif combo[1] == "B":
            if biggerd == "是":
                if biggerf == "是": 
                    print("總共為",data1[combo[0]]+data2[1]+add[0]+add[1],"元")
                
                else:
                    print("總共為",data1[combo[0]]+data2[1]+add[0],"元")
            else:
                if biggerf == "是": 
                    print("總共為",data1[combo[0]]+data2[1]+add[1],"元")
                
                else:
                    print("總共為",data1[combo[0]]+data2[1],"元")
    else:
        print("套餐輸入錯誤，無法計算")
elif len(combo) == 1:
    if combo[0] >= 1 and combo[0] <=5:
        if biggerd == "是":
            if biggerf == "是": 
                print("總共為",data1[combo[0]]+add[0]+add[1],"元")
                
            else:
                print("總共為",data1[combo[0]]+add[0],"元")
        else:
            if biggerf == "是": 
                print("總共為",data1[combo[0]]+add[1],"元")
                
            else:
                print("總共為",data1[combo[0]],"元")
    else:
        print("套餐輸入錯誤，無法計算")
else:
    print("套餐輸入錯誤，無法計算")