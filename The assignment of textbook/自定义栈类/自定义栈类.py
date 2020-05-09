class Stack:
    def __init__(self,maxlen=10):
        self.__content = []
        self.__size = maxlen
        self.__current = 0

    def __del__(self):
        del self.__content

    def clear(self):
        self.__content = []
        self.__current = 0

    def isEmpty(self):
        return not self.__content

    def setSize(self,size):
        if size <self.__current:
            print('New size must >=',+str(self.__current))
            return
        self.__size =  size

    def isFull(self):
        return self.__current == self.__size

    def push(self,v):
        if self.__current < self.__size:
            self.__content.append(v)
            self.__current += 1
        else:
            print('stack Full')

    def pop(self):
        if self.__content:
            self.__current -= 1
            return self.__content.pop()
        else:
            print('Stack in emppty!')

    def __str__(self):
        return 'Stack('+ str(self.__content)\
            + ', maxlen = ' + str(self.__size) + ')'

    __repr__ = __str__

#from myStack import Stack
s = Stack()
s.push(8)
print(s)

s.push(5)
print(s)

s.push('a')
print(s)

s.pop()
print(s)

s.setSize(20)
print(s)

print(s.isFull())
print(s.isEmpty())
s.clear()
print(s)
print(s.isEmpty())
