# 共同朋友的數量
A = list(input("請輸入A朋友的朋友們 : ").split())
B = list(input("請輸入B朋友的朋友們 : ").split())
find = 0
for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            find += 1
print(find)