def isNum(x):
    if type(x) == int or float or complex:
        print("你输入的是整数、浮点数或者复数")
        return True
    else:
        print("你输入的不是整数、浮点数或者复数")
        return False

try:
    data = eval(input("请输入一个数："))
except:
    print("你输入的不是整数、浮点数或者复数")
else:
    isNum(data)