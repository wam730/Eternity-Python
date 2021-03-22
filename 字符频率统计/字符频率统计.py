st = input("Please input a text:").strip(",，。/?、？（）().").strip(" ")
lt = list()
dic = dict()
for i in st:
    lt.append(i)
print(lt)
for i in lt:
    print(i)
print(lt)