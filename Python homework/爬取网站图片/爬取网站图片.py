from re import findall
from urllib.request import urlopen
url = r'https://mp.weixin.qq.com/s?__biz=MzUxNDkxMzgwMQ==&mid=2247537938&idx=2&sn=081e9d93e961ef644a6b4cc84573b15b&chksm=f9bcb674cecb3f62448cc9b1f2cd8669dc350fea635e9e2880f7f8d971800d9d8c23f534a146&scene=0&xtrack=1&key=98dcfdf29c3caba99df304f42802eca9e9cfd1468811c057a8d55c2662eef39d9498eeb29a2650c0cebef5dd4da32b7e5709fd5bea83b883e7ba2bbe0d698e5d7043007e65309bd89fb5b44a5300383d&ascene=1&uin=MjkyMDU0MzMyNg%3D%3D&devicetype=Windows+10+x64&version=6209007b&lang=zh_CN&exportkey=A0QNak4SV1gCBtZJq534ZCk%3D&pass_ticket=s6%2BUIms6qz0YK8HOJrCA0GQ1SNDi1LyKLqTxFVmyuAOIzQLjD7zsLCwd914B4znI'
pattern = 'img data-ratio="1" data-src="(.+?)"'
with urlopen(url) as fp:
    content = fp.read().decode()
result = findall(pattern, content)
for index, item in enumerate(result):
    with urlopen(str(item)) as fp:
        with open(str(index)+'.jpeg', 'wb') as fp1:
            fp1.write(fp.read())

