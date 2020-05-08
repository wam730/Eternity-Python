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

        #通过另一个函数来调用Fibonacci()函数来实现存储目的不是最好的办法，因为这样会造成很多次重复计算。
        #比如，计算前10位时，我们需要对每一个数求一次它前面的数才能得到该数，这就是个重复的过程。

        '''def fibo(n):
	        a=1
	        b=1
	        data=[1,1]
	        for i in range(n-2):
		        c = a+b
		        a,b = b,c
		        data.append(c)
	        return data
        print(data)'''
        
       