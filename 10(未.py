import numpy as np
while True :
    n,m = input("請輸入N跟M :(以空白隔開)").split()
    data = []
    
    for i in range(int(n)):
        data.append(input("請輸入第"+str(i+1)+"列").split())  
    print(data)
    datal = np.empty(int(m) * 1) ; print(datal);
    for i in range(int(m)):
        for j in range(int(n)):
            np.append(datal[i],data[j][i])
            print(datal)
        print("輸出矩陣數值第"+str(i+1)+"列為",datal[i])
        0
    break
