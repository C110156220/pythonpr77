#判斷星座
m,d = input("請輸入月及日").split() 
ml = ["",31,28,31,30,31,30,31,31,30,31,30,31]
F = ["",21,19,21,21,22,22,23,24,24,24,23,22]
T = ["魔羯","水瓶","雙魚","牧羊","金牛","雙子","巨蟹","獅子","處女","天秤","天蠍","射手","魔羯"]
m = int(m) ; d = int(d)
if 0 <= m and m <= 12 :
    if 0 <= d and d <= ml[m]:
        if d < F[m]:
            print("星座為",T[m-1])
        else:
            print("星座為",T[m])