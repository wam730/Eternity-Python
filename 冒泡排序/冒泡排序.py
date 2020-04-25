from random import randint as r
while True:
    print('只支持整数')
    minnum = input("请输入排序范围最小值（整数）：")
    maxnum = input("请输入排序范围最大值（整数）：")
    t = input("请输入你想在该范围内随机排序的数的个数：")
    how = input("你想升序排序（输入1）还是降序排序（输入2）") 
    try:
        assert(int(t) > 0)
        assert(int(minnum) < int(maxnum))
        assert(int(t) <= 1 + (int(maxnum) - int(minnum)))
        assert(int(how) == 1 or int(how) == 2)
    except:
        print("\n请检查输入")
    else:
        minnum = int(minnum)
        maxnum = int(maxnum)
        t = int(t)
        how = int(how)
        lst = [r(minnum,maxnum) for i in range(t)]
        print('\n原序列为：',lst)
        def selectSort(data,hhow):
            if hhow == 1:
                for i in range(0,len(data)-1):
                    for j in range(0,len(data)-i-1):
                        if data[j] > data[j+1]:
                            data[j] , data[j+1] = data[j+1] , data[j]
            elif hhow == 2:
                for i in range(0,len(data)-1):
                    for j in range(0,len(data)-i-1):
                        if data[j] < data[j+1]:
                            data[j] , data[j+1] = data[j+1] , data[j]
            return data
        print('\n排序后为：',selectSort(lst,how))
        x = (input('\n你还想继续吗？是请输入1，否请输入其他任意字符或回车：'))
        try:
            assert(x == int(x))
        except:
            break