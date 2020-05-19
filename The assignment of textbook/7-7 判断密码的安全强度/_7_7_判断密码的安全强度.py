import string
def cheakSafe(pas):
    level = {1:'\nWeak',2:'\nBelow middle',3:'\nAbove middle',4:'\nStrong'}
    r = [False]*4
    for ch in pas:
        if not r[0] and ch in string.digits:
            r[0] = True
        elif not r[1] and ch in string.ascii_lowercase:
            r[1] = True
        elif not r[2] and ch in string.ascii_uppercase:
            r[2] = True
        elif not r[3] and ch in ''',.!@#$%^&*()<>?/\{}[]:;"‘’“”：；，。《》、？~·`|''':
            r[3] = True
    return level.get(r.count(True),'error')

while True:
    password = input('\nPlease input your password:')
    try:
        assert(isinstance(password,str) and len(password) >= 6)
    except:
        print('\n',password + ' is not suitbale for password')
    else:
        print(cheakSafe(password))
        exit = input("\nDo you want to continue? If yes, Please input 'y':")
        try:
            assert(exit == 'y')
        except:
            break