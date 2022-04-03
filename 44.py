# 電腦數量
T = int(input("請輸入共幾班 : "))
numberofpp = []
for i in range(T):
    try:
        numberofpp.append(int(input("請輸入班級人數 : ")))
    except:
        print("請輸入數字，非文字或不輸入")
        

try:
    if max(numberofpp) >= 0 :
        print("共需要"+str(max(numberofpp))+"台電腦")
except:print("輸入錯誤或無學生")

    
