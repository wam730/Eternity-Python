mingwen = input('Please input the text you want to encrypt： ')
key = input('Plaese input the key: ')
print('The text you inputted is: ',mingwen)
doc = open('miwen.txt','w')
def jiami(text,keys):
    from itertools import cycle
    func = lambda x,y:chr(ord(x)^ord(y))
    return ''.join(map(func,text,cycle(keys)))

print('The text after encrypted is:',jiami(mingwen,key))

print('The text after encrypted is:',jiami(mingwen,key),file = doc)