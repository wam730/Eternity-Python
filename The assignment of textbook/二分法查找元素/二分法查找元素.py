from random import randint as r
while True:
    minnum = input("请输入查找数范围最小值（整数）：")
    maxnum = input("请输入查找数范围最大值（整数）：")
    time = input("请输入生成数的个数：")
    t = input("请输入你想在该范围内查找的数：")
    try:
        t = int(t)
        assert(int(minnum) < int(maxnum))
        assert(int(t) <= int(maxnum) and int(t) >= int(minnum))
        assert(int(time) <= (1 + int(maxnum) - int(minnum)))
    except:
        print("\n请检查输入")
    else:
        minnum = int(minnum)
        maxnum = int(maxnum)
        time = int(time)
        t = int(t)
        data = [r(minnum,maxnum) for i in range(time)]
        temp_data = data
        def Search(value,lst=[]):
            start = 0
            end = len(lst)
            lst.sort()
            while start < end:
                middle = (start + end)//2
                if value == lst[middle]:
                    return middle
                elif value > lst[middle]:
                    start = middle + 1
                elif value < lst[middle]:
                    end = middle - 1
            return False
        result = Search(t,data)
        if result != False:
            print('\n{0} 存在于序列中，位置是{1}'.format(t,result+1))
            print('\n\n提示：这里的位置编号是从1开始而非0。若一个数多次存在，则只显示第一次出现的位置')
        else:
            print('\n{0} 并不在刚才的序列里'.format(t))
        print('\n刚才的序列是：{0}'.format(temp_data))
        x = (input('\n你还想继续吗？是请输入1，否请输入其他任意字符或回车：'))
        try:
            assert(int(x) == 1)
        except:
            break