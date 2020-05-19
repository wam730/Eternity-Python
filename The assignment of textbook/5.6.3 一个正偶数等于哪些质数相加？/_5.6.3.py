while True:
    n = input("请输入一个正偶数：")
    try:
        assert(eval(n) > 0 and eval(n)%2 == 0)
    except:
        print('Error')
    else:
        n = int(n)
        def IsPrime(p):
            if p == 1:
                return False
            if p == 2:
                return True
            if p%2 == 0:
                return False
            for i in range(3,int(p**0.5)+1,2):
                if p%i == 0:
                    return False
            return True

        for i in range(2,n//2+1):#只算到n的一半原因在于防止n 与 n-i 交换顺序再次输出
            if IsPrime(i) and IsPrime(n-i):
                print(i,'+',n-i,'=',n)
        break