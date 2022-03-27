# 學生資料搜尋
data = [["123","Tom DTGD"],["456","Cat CSIE"],["789","Nana ASIE"],["321","Lim DBA"],["654","Won FDD"]]
i = input("請輸入學生學號 : ")

for z in range(len(data)):
    if i == data[z][0]:
        print("學生資料為",i,data[z][1])