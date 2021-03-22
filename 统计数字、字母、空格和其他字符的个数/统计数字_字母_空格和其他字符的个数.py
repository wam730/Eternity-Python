def HowManyWords(st):
    Num = 0
    Words = 0
    Blank = 0
    Others = 0
    for i in st:
        if i.isdigit():
            Num += 1
        elif i.isalpha():
            Words += 1
        elif i == ' ':
            Blank += 1
        else:
            Others += 1
    print("数字有：{}个，字母有：{}个，空格有：{}个，其他字符：{}个".format(Num,Words,Blank,Others))

data = input("请输入文字：")
HowManyWords(data)