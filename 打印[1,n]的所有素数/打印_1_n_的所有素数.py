n = eval(input("请输入一个正整数："))
def isPrime(n):
    lt = []
    for i in range(2,n+1):
        if 0 not in [i%j for j in range(2,int(i**0.5)+1)]:
            lt.append(i)
    for i in lt:
       print(i,end = ' ')
isPrime(n)