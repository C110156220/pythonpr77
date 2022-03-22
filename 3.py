# 輸出生肖

list =['rat','ox','tiger','rabbit','dragon','snake','horse','sheep','monkey','rooster','dog','pig']
y = int(input("請輸入西元年"))
result = (y - 2008) % 12

print(list[result])
