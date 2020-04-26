while True:
    n = input('请输入一个正整数：')
    try:
        assert(int(n) > 0)
    except:
        print("输入错误！请检查输入")
    else:
        n = int(n)
        def IsPrime(p):
            if p == 1:
                return False
            if p == 2:
                return True
            if p%2 == 0:
                return False
            for i in range(3,int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True
        if IsPrime(n):
            print(n,'是素数')
        else:
            print(n,'不是素数')
        x = (input('\n你还想继续吗？是请输入1，否请输入其他任意字符或回车：'))
        try:
            assert(int(x) == 1)
        except:
            break
