while True:
    n = input('请输入一个正整数，然后判断是不是素数：')
    try:
        assert(int(n) > 0)
    except:
        print("你的输入不符合要求，请检查后重新输入！")
    else:
        n = int(n)
        def IsPrime(p):
            if p == 1:
                return False
            if p == 2:
                return True
            if p%2 == 0:
                print('∵',n,'=','2 * ',int(n/2))
                return False
            for i in range(3,int(n**0.5)+1):
                if n % i == 0:
                    print('∵',n,'=',i,'*',int((n/i)))
                    return False
            print('∵',n,'=','1 * ',n)
            return True
        if IsPrime(n):
            print('\n∴ {0}是素数'.format(n))
        else:
            print('\n∴ {0}不是素数'.format(n))
        
        x = (input('\n你还想继续吗？是请输入1，否请输入其他任意字符或回车：'))
        try:
            assert(int(x) == 1)
        except:
            break
