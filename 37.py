# 3n+1 問題

n = int(input("請輸入一個數"))
process = []

while True:
    if n == 1:
        st = ""
        for i in range(len(process)):
            st =st + str(process[i])+" "
        print("數列 : "+st)
        print("cycle length :",len(process));
        break

    if n % 2 == 0:
        n = n /2 
        process.append(int(n))

    elif n % 2 == 1:
        n = 3 * n + 1
        process.append(int(n))

    