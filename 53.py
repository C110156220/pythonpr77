# 製作通訊錄
name = []
email = []
n = int(input("請輸入幾筆資料"))
for i in range(n):
    name.append(input("請輸入第"+str(i+1)+"名子 : "))
    email.append(input("請輸入電子郵件 : "))

查詢 = input("請輸入要查詢電子郵件的姓名 : ")

if 查詢 in name:
    print(查詢+"的電子郵件 : "+email[name.index(查詢)])
else :
    print("找不到該用戶")