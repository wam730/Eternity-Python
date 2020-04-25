from itertools import cycle
while True:
    n = input("请输入人数：")
    k = input('请输入报数最大数：')
    try:
        assert(int(n) >= 2)
        assert(int(k) >= 2)
    except:
        print('输入错误，请重新输入')
    else:
        n = int(n)
        k = int(k)
        def demo(lst,k):
            t_lst = lst[:]
            while len(t_lst) > 1:
                c = cycle(t_lst)
                for i in range(k):
                    t = next(c)
                index = t_lst.index(t)
                t_lst = t_lst[index+1:] + t_lst[:index]
            return t_lst
        list_1 = list(range(1,n+1))
        print('最后留下的是',demo(list_1,k),'号')
        break