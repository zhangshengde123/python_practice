# 利用条件运算符的嵌套来完成此题：学习成绩 >=90 分的同学用 A 表示，60-89 分之间的用 B 表示，60 分以下的用 C 表示。

def rank(score):
    print('请输入你的成绩：')
    if score >=90:
        print('你的得分等级为：A')
    elif score >=60 and score < 90:
        print('你的等级为：B')
    else:
        print('你的等级为：C')
    return
rank(89)
