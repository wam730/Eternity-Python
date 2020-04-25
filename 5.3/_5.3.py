while True:
    a = input("Please input a number:")
    n = input('Please input n:')
    try:
        n = int(n)
    except:
        print("Error. Please re-enter a number")
    else:
        def summ(x,y,lst = []):
            for i in range (1,y+1):
                tem = x*i
                lst.append(tem)
            print(' + '.join(lst),'=',sum(list(map(int,lst))))

        summ(a,n)
        break