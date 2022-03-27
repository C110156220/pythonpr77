# 轉置矩陣
while True :
    n,m = input("請輸入N跟M :(以空白隔開)").split()
    data = []
    
    for i in range(int(n)):
        data.append(input("請輸入第"+str(i+1)+"列").split())  


    for i in range(int(m)):
        tmp = []
        for j in range(int(n)):
            tmp.append(data[j][i])
            
        print("輸出矩陣數值第"+str(i+1)+"列為",tmp)
        
    break
