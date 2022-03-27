# 洗刷刷

A = list(input("甲方的數字為 : "))
B = list(input("乙方的數字為 : "))
limit = ["1","2","3","4","5"]
if len(A) == len(B) :
    R = []
    for i in range(len(A)):
        if A[i]=="1" and B[i]=="5":R.append("贏")
        elif A[i]=="5" and B[i]=="1":R.append("輸")

        elif A[i]=="2" and B[i]=="1":R.append("贏")
        elif A[i]=="1" and B[i]=="2":R.append("輸")

        elif A[i]=="3" and B[i]=="2":R.append("贏")
        elif A[i]=="2" and B[i]=="3":R.append("輸")

        elif A[i]=="4" and B[i]=="3":R.append("贏")
        elif A[i]=="3" and B[i]=="4":R.append("輸")
        
        elif A[i]=="5" and B[i]=="4":R.append("贏")
        elif A[i]=="4" and B[i]=="5":R.append("輸")
        
        elif A[i] not in limit or B[i] not in limit:
            R.append("X")
        else:
            R.append("和")
    resul = ""
    for i in range(len(R)):
        if R[i] == "X" :print("出現1~5以外的數字，以X表示")
        resul += R[i]
        
    print("洗刷刷結果 : ",resul)

else:
    print("雙方數字不同，不能比較")