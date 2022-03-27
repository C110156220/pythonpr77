# 最大的迴文數字子數列
while True :
    st = input("輸入整數數列(輸入end結束)")
    if st =="end":print("結束");break
    else:
        for i in range(len(list(st))):
            if st[i:i:]