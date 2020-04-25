n = input("请输入一个正偶数：")
while(eval(n) == int(n)):
    if eval(n) >0 or eval(n)%2 == 0:
        print(n)
        break
