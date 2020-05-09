class Vector3():
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def add(self,anotherPoint):
        x = self.__x + anotherPoint.__x
        y = self.__y + anotherPoint.__y
        z = self.__z + anotherPoint.__z
        return Vector3(x,y,z)

    def sub(self,anotherPoint):
        x = self.__x - anotherPoint.__x
        y = self.__y - anotherPoint.__y
        z = self.__z - anotherPoint.__z
        return Vector3(x,y,z)

    def mul(self,n):
        x,y,z = self.__x*n, self.__y*n, self.__z*n
        return Vector3(x,y,z)

    def  div(self,n):
        x,y,z = self.__x/n, self.__y/n, self.__z/n
        return Vector3(x,y,z)

    def show(self):
        print('X:{0}, Y:{1}, Z:{2} '.format(self.__x, self.__y, self.__z))

    def show_1(self):
        #不直接打印，则可在打印语句中使用
        return (self.__x, self.__y, self.__z)

    @property
    #查看向量长度，长度为所有分量平方和的平方根，和几何上定义一致。
    def length(self):
        return(self.__x**2 + self.__y**2 + self.__z**2)**0.5

V = Vector3(6,2,9)
print('V = ',V.show_1())
v1 = V.mul(3)
print('v1 = V * 3 = ',v1.show_1())
v2 = v1.add(V)
print('v2 = v1 + V = ',v2.show_1())
v3 = v2.div(2)
print('v3 = v2 / 2 = ',v3.show_1())
print(' length V  = ',V.length,'\n',
      'length v1 = ',v1.length,'\n',
      'length v2 = ',v2.length,'\n',
      'length v3 = ',v3.length,'\n')

#如何使得V的长度为整数？人为计算肯定可以；也可以通过下列函数：
'''
def find(n):
	data = []
	for i in range(1,n+1):
		for j in range(1,n+1):
			for k in range(1,n+1):
				if (i**2+j**2+k**2)**0.5 == int((i**2+j**2+k**2)**0.5):
					data.append((i,j,k))
	return data
>>>find(10)
>>>[(1, 2, 2), (1, 4, 8), (1, 8, 4), (2, 1, 2), (2, 2, 1), (2, 3, 6), (2, 4, 4), 
    (2, 6, 3), (2, 6, 9), (2, 9, 6), (3, 2, 6), (3, 6, 2), (3, 6, 6), (4, 1, 8), 
    (4, 2, 4), (4, 4, 2), (4, 4, 7), (4, 7, 4), (4, 8, 1), (4, 8, 8), (5, 10, 10), 
    (6, 2, 3), (6, 2, 9), (6, 3, 2), (6, 3, 6), (6, 6, 3), (6, 6, 7), (6, 7, 6), 
    (6, 9, 2), (7, 4, 4), (7, 6, 6), (8, 1, 4), (8, 4, 1), (8, 4, 8), (8, 8, 4), 
    (9, 2, 6), (9, 6, 2), (10, 5, 10), (10, 10, 5)]
'''