# 字元出現次數

while True:
    s = input("請輸入檢測的字串 (輸入end將終止程序)")
    if s == "end":print("檢測終止");break
    else:
        s = list(s)
        times = 0
        fs = input("請輸入檢測的單一字元 : ")
        if fs == None or fs == "":
            print("未輸入檢測單一字元，無法判斷，請重新輸入")
            
        else:
            for i in range(len(s)):
                if fs ==s[i]:
                    times += 1
            print("字元"+fs+"出現次數為",times)