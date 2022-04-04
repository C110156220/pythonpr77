# 母音轉換
s = list(input("請輸入一串小寫英文"))

母 = ['a','e','i','o','u']

for i in range(len(s)):
    for j in range(len(母)):
        if s[i] == 母[j]:
            s[i] = "."
res = ""
for i in range(len(s)):
    res += s[i]

print(res)