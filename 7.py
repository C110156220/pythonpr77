# 通話費率
from operator import index
way,time = input("請輸入月租費型式及通話時間為: ").split(",")
way1 = ['186','386','586','986']
spend = [0.09 , 0.08, 0.07 , 0.06]
discount1 = [0.9,0.8,0.7,0.6]
discount2 = [0.8,0.7,0.6,0.5]
 
cost = int(time) * spend[way1.index(way)] 

if cost < int(way):
    print("通話費為"+way)
elif cost < int(way)*2 :
    print("通話費為",round((cost)*discount1[way1.index(way)]),"元")
else :
    print("通話費為",round((cost)*discount2[way1.index(way)]),"元")



