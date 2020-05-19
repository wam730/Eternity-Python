import string
def longgestNumber(st):
    data = []
    r = [0]*len(st)
    for i in range(len(st)):
        if st[i] in string.digits:
            for j in range(i,len(st)):
                s = st[i:j+1:1]
                if s.isdigit():
                    data.append(s)
        elif st[i] not in string.digits:
            r[i] = 1
    if all(r):
        return 'There are no numbers in it!'
    else:
        return max(data,key=len)

while True:
    text = input("Input a string and return the longgest numeric string:")
    try:
        assert(isinstance(text,str))
    except:
        print("\nError. Plaese re-enter.\n")
    else:
        print('\nThe longgest numeric string is: ' ,longgestNumber(text))
        exit = input('''\nIf you want to continue, please input 'y', If not, input anything to exit:''')
        try:
            assert(exit == 'y')
            print('\n')
        except:
            print('\n')
            break