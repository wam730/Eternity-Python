while True:
    n = input("Please input a number: ")
    try:
        assert(int(n)>=0)
    except:
        print("Your input is error! ")
    else:
        n = int(n)
        data = [i for i in range(1,5*n)]
        print(data)
        def isEvennumbers(lst = []):
            '''for i in lst:
                if i%2 != 0:
                    lst.remove(i)'''
            lst = list(filter(lambda x: x%2 == 0,lst))
            return lst
        print('\nThe even numbers in data are: \n',isEvennumbers(data))
        break
    finally:
        print('\n\n\n','*'*48,"Powered by Wang Yujie",'*'*48)