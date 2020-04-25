n = int(input('Please input a int number:'))
def yanghui(x):
    print([1])
    line = [1,1]
    print(line)
    for i in range(2,x):
        r = []
        for j in range(0,len(line)-1):
            r.append(line[j]+line[j+1])#等于上一行正上方的数字line[j+1],与正上方的line[j]之和
        line = [1] + r + [1]
        print(line)

yanghui(n)