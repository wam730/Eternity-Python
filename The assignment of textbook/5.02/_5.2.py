while True:
    a = input('Please input the first number :')
    b = input('Plese input the second number :')
    try:
        assert(int(a) > 0)
        assert(int(b) > 0)
    except:
        print('\nYou entered is error . Please re-enter.')
    else:
        a = int(a)
        b = int(b)
        def Max(a,b):
            if a < b :
                a , b = b , a
            c = a%b
            if c != 0:
                return Max(b,c)
            elif c == 0:
                return b

        print('\nThe lowest common multiple of {0} and {1} is：{2}'.format(a,b,int(a*b / Max(a,b))))
        print('And the greatest common divisor of {0} and {1} is {2}'.format(a,b,Max(a,b)))
        x = input("\nDo you want to continue ? If yes , plese input 1' to cintinue . If not, Enter any to continue:")
        try:
            assert(int(x) == 1)
        except:
            print('\nThank you for using')
            print('Powered by Wang Yujie\n')
            break