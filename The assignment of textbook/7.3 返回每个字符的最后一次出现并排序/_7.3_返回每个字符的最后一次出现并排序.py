#仅实现功能，不考虑异常处理和优化文本显示
def returnStr(data):
    result = []
    data = list(reversed(data))
    for st in data:
        if st in result:
            pass
        else:
            result.append(st)
    return list(reversed(result))

text = input("Input some strings:")
print(returnStr(text))