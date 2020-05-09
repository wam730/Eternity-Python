'''设计自定义双端队列类,模拟入队、出队等基本操作。

问题描述:双端队列是指在左右两侧都可以入队和出队的一种数据结构所馆,是指,在队列的头部或尾部增加一个元素。
而所谓出队是指,朋除队列头部或民部的个元素。

基本思路:对列表进行封装和扩展,对外提供接口模拟双端队列的操作,假装自己是一个双端队列,把外部对双端队列的操作转换为内部对列表的操作。
在列表尾部使用apend()方法追加一个元素用来模拟右端入队操作,使用pop()方法删除列表尾部元素移'''
class myDeque:
    def __init__(self,iterable=None,maxlen=10):
        if iterable==None:
            self._content = []  #存储实际数据
            self._current = 0  #队列中元素个数,是实际的输入元素的个数，不是规定的列表的长度。不输入，则其值为0
        else:
            self._content = list(iterable)
            self._current = len(iterable) #初始化其值
        self._size = maxlen     #这个self._size是指我规定的列表的长度，我规定10，则不管你输入几个数，反正我只能存10个
        if self._size < self._current:  #小于输入的个数则将其替换为输入的个数
            self._size = self._current

    def __del__(self):
        del self._content   #删除输入的数据

    def setSize(self,size): #修改队列的大小
        if size < self._current:    #如果修改后小于原来的大小，则删除后面多的元素
            for i in range(size,self._current)[::-1]:
                del self._content[i]
            self._current = size
        self._size = size

    def appendRight(self,v):    #在右侧入队
        if self._current < self._size:
            self._content.append(v)
            self._current += 1
        else:
            print("The queue is fall!") #满了则忽略操作

    def appendLeft(self,v):     #在左侧入队
        if self._current < self._size:
            self._content.insert(0,v)
            self._current += 1
        else:
            print("The queue is fall!")

    def popLeft(self):      #左侧出队 
        if self._content:
            self._current -= 1
            return self._content.pop(0)
        else:
            print('The queue is empty!')

    def popRight(self):     #右侧出队
        if self._content:
            self._current -= 1
            return self._content.pop()
        else:
            print("The queue is empty!")

    def rotate(self,k):     #循环移位，负值则左移
        if abs(k) > self._current:  #如果k比长度大，则打印k必须小于长度
            print('k must <= '+str(self._current))
            return
        self._content = self._content[-k:] + self._content[:-k] #以k大于0为例，表示的是将后k个元素+后k个元素前面的元素，实现右移
        '''
        如：
       x = [1,2,3,4,5]
       >>>x[:-2] == [1, 2, 3]
       >>>x[-2:] == [4, 5]
       >>>x = x[-2:] + x[:-2] == [4, 5, 1, 2, 3]
        '''

    def reverse(self):      #前后倒置
       self._content.reverse()

    def __len__(self):      #计算长度，所含元素个数
        return self._current

    def __str__(self):      #使用print打印时，显示当前队列中剩余的元素
        return 'myDeque(' + str(self._content)\
            + ', maxlen = '+ str(self._size) + ')'

    __repr__ = __str__

    def clear(self):        #置空
        self._content = []
        self._current = 0

    def isFull(self):       #是否满了
        return self._current ==self._size

    def isEmpty(self):      #是否空的
        return not self._content

if __name__ == '__main__':
        print('Please use me as a module!')
