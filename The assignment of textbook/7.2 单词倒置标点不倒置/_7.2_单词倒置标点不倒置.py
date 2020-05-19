def inversion(data):
    data = ' '.join(list(reversed(data)))
    return data
while True:
    print(' Welcome '.center(120,'*'))
    text = input("Please input some English sentences:").split()
    try:
        for st in text:
            assert(type(st) == str)
    except:
        print('Your input is wrong!'.center(120,'*'))
    else:
        print(' The result is as follows '.center(120,'-'))
        print(inversion(text))
        print(''.center(120,'-'))
        exit = input("\nIf you want to continue, please input 'y':")
        try:
            assert(exit == 'y')
        except:
            print(' Thank you for you using '.center(120,'*'))