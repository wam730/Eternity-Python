while True:
    try:
        x,y = input("请输入两个正整数，以空格分开：").split(' ')
        assert(int(x) == eval(x) and int(y) == eval(y) and int(x)>=0 and int(y)>=0)
    except:
        print("输入有误，请按要求重新输入：")
    else:
        x = eval(x)
        y = eval(y)
        a=x
        b=y
        c=x*y        
        if x<y:
            x,y = y,x
        z = x%y
        while z != 0:
            x,y = y,z
            z = x%y
            if z==0:
                break
        print("{} 和 {} 的最大公约数是：{}，最小公倍数是：{}".format(a,b,y,int(c/y)))
        break
    finally:
        print("by Wang Yujie".center(120,'*'))