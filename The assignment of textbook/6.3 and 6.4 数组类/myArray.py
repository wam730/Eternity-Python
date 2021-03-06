import array as arr

class myArray():
    def __init__(self,data =[]):
        if type(data) == int or type(data) == str:
            return
        elif isinstance(data,list) or isinstance(data,tuple):
            for i in data:
                if not isinstance(i,int):
                    return
            self.__myarray = arr.array('b',data)
        elif isinstance(data,range):
            self.__myarray = arr.array('b',data)
        else:
            return

    def setArray(self,data):
       if type(data) == int or type(data) == str:
            return 'You only can input list, tuple and range()'
       elif isinstance(data,list) or isinstance(data,tuple):
            for i in data:
                if not isinstance(i,int):
                    return 'You only can input int-number!'
            self.__myarray = arr.array('b',data)
            return self.__myarray
       elif isinstance(data,range):
            self.__myarray = arr.array('b',data)
            return self.__myarray
       else:
            return 'Your input is error!'


    def change(self,index,value):
        if index < len(self.__myarray)  and type(value) == int:
            self.__myarray[index] = value
            return self.__myarray
        else:
            print("Error. Your input is illegal.")

    def returnValue(self,index):
        length = len(self.__myarray)
        if type(index) == int and 0<= index < length:
            return self.__myarray[index]
        elif isinstance(index,list) or isinstance(index,tuple):
            for i in index:
                if not(isinstance(i,int) and 0<= i < length ):
                    return 'Index error!'
            result = []
            for item in index:
                result.append(self.__myarray[item])
            return result
        elif isinstance(index,range):
            index=list(index)
            for i in index:
                if not(isinstance(i,int) and 0<= i < length ):
                    return 'Index error!'
            result = []
            for item in index:
                result.append(self.__myarray[item])
            return result
        else:
            return 'Index error!'

    def show(self):
        print(self.__myarray)

    def clearArray(self):
         self.__myarray = arr.array('b')
         return self.__myarray

    def addValue(self,value):
        if type(value) == int:
            self.__myarray.append(value)
            return self.__myarray
        else:
            return 'Your input is error!'

    def removeValue(self,value):
        if type(value) == int:
            if value in self.__myarray:
                self.__myarray.remove(value)
                return self.__myarray
            else:
                return '{0} is not in the array'.format(value)
        elif self.__myarray == arr.array('b'):
            return 'Array is empty!'
        else:
            return 'Your input is error!'

x = myArray()
x.setArray(range(11))
x.show()

x.change(10,90)
x.show()

print(x.returnValue([1,4,7,9,10]))

x.addValue(91)
x.removeValue(90)
print(x.removeValue(1000))
x.show()

x.clearArray()
x.show()