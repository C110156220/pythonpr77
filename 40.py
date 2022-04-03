# 輸出十字架

a = ['1','3','5','7','9']
C = ['1','3','5','7']
k = int(input("請輸入正數n"))
mid = int(round(k/2,0))
for i in range(k):
    if i < mid :
        for  j in range(mid):
            print(" ",end="")
        print(a[i],end="")
    elif i == mid :
        for  i in range(0,int(round(k/5,2))+1):
            if i < int(round(k/len(a),0)-1):
                for b in range(len(a)):
                    print(a[b],end="")
            else:
                for c in range(k-len(a)):
                    print(a[c],end="")
    elif i > mid :
        for  l in range(mid):
            print(" ",end="")
        print(C[k -i -1],end="")
    
    print()

