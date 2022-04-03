# 求出 一元二次方程式 的解


a = int(input("請輸入a係數(x平方的係數) : "))
b = int(input("請輸入b係數(x的係數) : "))
c = int(input("請輸入c係數(常數項的係數) : "))
ans = []
tell =int((b ** 2)- (4*a*c)) 
formula1 = (int(round(-b/2*a,0)))+(int(round((tell **0.5)/2*a,0))) 
formula2 = (int(round(-b/2*a,0)))-(int(round((tell **0.5)/2*a,0))) 
if tell > 0:
    ans.append(formula1)
    ans.append(formula2)
    for i in range(len(ans)):
        print("第"+str(i+1)+"個解為",ans[i])

elif tell == 0:
    ans.append(-(b/(2*a))) ; print("解為 : ",ans[0],"，且為相等的實數根")

elif tell < 0:

    for i in range(len(ans)):
        ans.append(formula1)
        ans.append(formula2)
        for i in range(len(ans)):
            print("第"+str(i+1)+"個解為",ans[i])
    
else:
    print("出現意外錯誤")


