while True:
    x = input("请输入一个整数：")
    try:
        eval(x) == int(x)
    except:
        print("输入错误请重新输入：")
    else:
        x = eval(x)
        print("\n{}={}={}={}\n".format(int(x),bin(x),oct(x),hex(x)))
        break