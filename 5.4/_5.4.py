data = list(input('请输入一些任意字符：'))

def huiwen(x):
    y = x[::-1]#和下面的代码等价
    #y = list(reversed(x))
    if y == x:
        print('这些字符是回文\n',y,'=',x)
    elif y != x:
        print('这些字符不是回文\n',y,'!=',x)

huiwen(data)