# 字根與子字串
s1 = input("請輸入一個字串")
s2 = input("請輸入另一個字串")
if len(s1) <= len(s2):
    if s1 in s2 :
        print("YES，包含在裡面")
    else :
        print("NO，不含在裡面")
if len(s1) >= len(s2):
    if s2 in s1 :
        print("YES，包含在裡面")
    else :
        print("NO，不含在裡面")