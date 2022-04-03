# 期末成績

subject = ["國文","英文","微積分","體育","程式設計"]
score = []
for i in range(len(subject)):
    score.append(int(input("輸入"+subject[i]+"的分數")))
print("平均分數:%.2f分" %(sum(score)/len(subject)))
print("最高分為 : "+subject[score.index(max(score))],max(score),"分")
print("最低分為 : "+subject[score.index(min(score))],min(score),"分")