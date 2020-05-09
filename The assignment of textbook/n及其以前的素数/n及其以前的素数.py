while True:
    n = input("Please input n: ")
    try:
        assert(int(n)>=1)
    except:
        print("\n{0} is error. The n you inputted must >= 1 and must a int-number!".format(n))
    else:
        n = int(n)
        def prime(n):
            data = []
            for i in range(2,n+1):
                if not 0 in [i%j for j in range(2,i)]:
                             data.append(i)
            return data
        print("The prime numbers have: \n",prime(n),'\n')
        exit = input("If you want continue, please input 'y'. If not, input anything to exit :")
        try:
            assert(exit == 'y')
        except:
            break

#也可以换一种方式实现求前n个素数，不过在理解上比这个困难,用筛选法求素数:

'''
def prime1(n):
    data = [i for i in range(2,n+1)]
    m = int(n**0.5)
    for index, value in enumerate(data):
        if value > m:
            break
        data[index+1:] = filter(lambda x: x%value != 0,data[index+1:])
    return data
print('\n',prime1(n))
'''