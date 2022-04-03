# 英文單字翻譯
data = {
    'Cat':"貓",
    'Dog':"狗",
    'Bear':"熊",
    'Snake':"蛇" }


reply = input("請輸入英文單字")
if reply.capitalize() in data:
    print(reply.capitalize()+"的翻譯是"+data[reply.capitalize()])
else:
    print("字典未有此單字")