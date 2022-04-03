# 微分
print("求出a * x 的n次方的微分")
a,n = input("請填入a,n(以空格隔開) : ").split()
a = int(a) ; n =int(n)
print(str(a*n)+"x**"+str(n-1))