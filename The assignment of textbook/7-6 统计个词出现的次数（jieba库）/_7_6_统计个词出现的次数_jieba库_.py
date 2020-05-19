import collections as col
from jieba import cut

files = open('fraquency.txt','w')
text = input("Input a text:\n")

def frequency(text):
    return col.Counter(cut(text))

print(frequency(text))
print(frequency(text),file = files)