#应用reversed()可以优化5.4中的代码
data = list(input('请输入一些字符或数字：'))

def myreversed(x):
    y = x[::-1]
    return y

n = int(input('\n你想以列表（请输入1）、元组（请输入2）还是集合（请输入3）形式输出？'))
while(n not in [1,2,3]):
    print('输入错误，请检查后重新输入！')
    n = int(input("请重新输入："))

if n == 1:
    print(myreversed(data))
elif n ==2:
    print(tuple(myreversed(data)))
elif n==3:
    print(set(myreversed(data)))