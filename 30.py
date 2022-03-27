# 猜數字
import random as rd

Ans = [];ans =""
for i in range(4):
    Ans.append(str(rd.randint(1,9)))
    ans += Ans[i]
print(ans)
    
while True:
    say = input("請輸入4位數字")
    if len(say) == 4:
        tmp =[]
        if "0000" in say:
            print("遊戲結束，答案是",ans)
            break
        else:
            for i in range(4):
                if say[i]==Ans[i]:tmp.append("A")
                elif say[i] in Ans:tmp.append("B")
            print(tmp.count("A"),"A",tmp.count("B"),"B")
            if tmp.count("A") == 4:
                print("獲勝")
                break
    
    else:
        print("並非輸入4位數字，請重新輸入")