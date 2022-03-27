# 親骨肉測驗
n = (input("請輸入測試量"))
try :
    int(n)
    yes = True
except ValueError:
    yes = False
if yes == True  :
    for z in range(int(n)):
        
        b = list(input("請輸入父、母、子女血型 :(請用空格隔開)").split())
        result = False
        
        if b[0] == "O" :
            if b[1] =="O":
                if b[2] == "O":
                    result =True
                else:
                    result = False
            elif b[1]=="A":
                if b[2] == "O" or b[2] =="A":
                    result =True
                else:
                    result = False
            elif b[1]=="B":
                if b[2] == "O" or b[2] =="B":
                    result =True
                else:
                    result = False
            elif b[1] =="AB":
                if b[2] == "A" or b[2] =="B":
                    result =True
                else:
                    result = False
            else :
                print("母親血型輸入錯誤")
        elif b[0] == "A":
            if b[1]=="A":
                if b[2] == "O" or b[2] =="A":
                    result =True
                else:
                    result = False
            elif b[1]=="B":
                    result =True
            elif b[1] =="AB":
                if b[2] == "O":
                    result = False
                else:
                    result =True
            elif b[1] =="O":
                if b[2] == "O" or b[2] =="A":
                    result =True
                else:
                    result = False
            else :
                print("母親血型輸入錯誤")
        elif b[0] == "B":
            if b[1]=="A":
                    result =True
            elif b[1]=="O":
                if b[2] =="B" or b[2]=="O":
                    result =True
                else:
                    result =False
            elif b[1]=="B":
                if b[2] == "O" or b[2] =="B":
                    result =True
                else:
                    result = False
            elif b[1] =="AB":
                if b[2] == "O":
                    result = False
                else:
                    result =True
            else :
                print("母親血型輸入錯誤")
        elif b[0] == "AB":
            if b[1] =="AB":
                if b[2] == "O":
                    result = False
                else:
                    result =True
            elif b[1]=="A":
                if b[2] == "O":
                    result = False
                else:
                    result =True
            elif b[1]=="B":
                if b[2] == "O":
                    result = False
                else:
                    result =True
            elif b[1]=="O":
                if b[2] == "O" or b[2] =="AB":
                    result = False
                else:
                    result =True
            else :
                print("母親血型輸入錯誤")
        else:
            print("父親血型輸入錯誤")

        if result == True :
            print("YES")
        else :
            print("IMPOSSIBLE")
else:
    print("輸入錯誤")