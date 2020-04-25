while True:
    n = input('请输入一个大于1的正整数：')
    try:
        assert(eval(n) == int(n) and eval(n) > 1)
    except:
        print("输入错误！请检查输入后再次输入\n")
    else:
        n = int(n)
        def HowmanyPrime(p):
            data = list(range(2,n+1))
            m = n**0.5
            if p == 2:
                data = [2]
            else:
                for index , value in enumerate(data):
                    if value > m:
                        break
                    data[index+1:] = filter(lambda x :x % value != 0 ,data[index+1:])
            return data
        print('{0}及以前的素数有:{1}'.format(n,HowmanyPrime(n)))
        x = (input('\n你还想继续吗？是请输入1，否请输入其他任意字符或回车：'))
        try:
            assert(int(x) == 1)
        except:
            break