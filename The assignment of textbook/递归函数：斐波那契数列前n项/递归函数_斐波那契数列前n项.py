while True:
    x = input("How many numbers you what to show in Fibonacci Sequence? ")
    try:
        assert(int(x)>=1)
    except:
        print("\nError. The number you inputted must >= 1 and must is a int-number!\n")
    else:
        x = int(x)
        def Fibonacci(x):
            if x == 1:
                return 1
            elif x == 2:
                return 1
            else:
                return Fibonacci(x-1)+Fibonacci(x-2)
        def Storge(x):
            data = []
            for i in range(1,x+1):
                data.append(Fibonacci(i))
            return data
        print('All the numbers are:\n',Storge(x),"\n")
        y = input("Do you want to continue? If yes, please input 'y' to continue.If not, input anything to exit. ")
        try:
            assert(y=='y')        
        except:
            print("\n")
            break