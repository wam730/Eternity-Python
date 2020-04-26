data = list(input("请输入英文字符:\n"))
def demo(x):
    lower = 0
    upper = 0
    other = 0
    result = []
    for items in x:
        if 'a'<= items and items <= "z":
            lower += 1
        elif 'A' <= items and items <= 'Z':
            upper += 1
        else:
            other += 1
    result.append(upper)
    result.append(lower)
    result.append(other)
    return result

print("大写，小写字母、其他符号个数分别为：\n",demo(data))