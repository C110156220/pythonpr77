# 找出學生成績問題

all = set(['John','Mary','Tina','Fiona','Claire','Eva','Ben','Bill','Bert'])
engpass = set(['John','Mary','Fiona','Claire','Ben','Bill'])
mathpass = set(['Mary','Fiona','Claire','Eva','Ben'])

print("英文與數學皆及格是",engpass & mathpass)
print("數學不及格是",all - mathpass)
print("英文及格但數學不及格是",engpass & (all -mathpass ))