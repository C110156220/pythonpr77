# 存取串列中元素


str1 = list(input("請輸入一個英文句子").split()) 
revstr = []
for i in range(len(str1)-1,-1,-1):
    revstr.append(str1[i])

print("輸出結果為",revstr)

