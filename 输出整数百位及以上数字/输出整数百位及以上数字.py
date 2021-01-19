n = eval(input("请输入一个三位以上的整数："))
if n/100<1 or n != int(n):
    print("你的输入有误")
else:
    print("{} 的百位及以上是：{}".format(n,int(n/100)))