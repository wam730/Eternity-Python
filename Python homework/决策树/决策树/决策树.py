from sklearn import tree
import numpy as np

questions = ('操作系统的定义','如何安装扩展库',
             '变量名aFunction 与 afunction的区别',
             '汉字是否可以作为变量名',
             '5201314如何变2进制数',
             '0.2*0.2 == 0.040000000000是否正确',
             '可以用pygame开发小游戏',
             '如何用一行代码判断素数',
             '级数(1/(n^2))收敛',
             ' join()是谁的操作方法')

labels = ['极具学习天赋', '暂不适合学习', '适合学习', '有学习基础',
          '有相当高学习天赋', '有学习基础', '有相当高学习天赋', '有学习基础',
          '适合学习', '有学习基础', '有相当高学习天赋', '有相当高学习天赋']

answers = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [3, 3, 3, 0, 0, 0, 0, 1, 3, 0],
           [0, 0, 0, 3, 3, 0, 0, 3, 3, 3],
           [3, 3, 3, 3, 0, 0, 0, 3, 3, 0],
           [3, 0, 3, 0, 3, 0, 0, 3, 3, 2],
           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
           [0, 0, 0, 0, 0, 0, 0, 2, 2, 0],
           [0, 0, 0, 3, 0, 0, 0, 3, 3, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
           [0, 0, 0, 0, 3, 0, 0, 3, 3, 0],
           ]

clf = tree.DecisionTreeClassifier().fit(answers, labels) 
yourAnswer = []
for question in questions:
    print('\n你对问题：','[',question,']' '清楚吗(知道吗)？')
    while True:
        print('完全不知道-0\t听说过\知道一点-1\t知道较多-2\t完全了解-3\t')
        try:
            answer = int(input('请输入：'))
            assert 0<=answer<=3
            break
        except:
            print('请输入正确的数字!')
    yourAnswer.append(answer)
    
yourAnswer = np.array(yourAnswer).reshape(1,-1)
print(clf.predict(yourAnswer))