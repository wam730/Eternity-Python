#coding:utf-8
import sys,os
from PIL import Image,ImageDraw
from CutImage import cut, cutX, cutY, countX, countY, \
    findPoint, zeroToMore, moreToZero, ccut 
#二值判断,如果确认是噪声,用改点的上面一个点的灰度进行替换
#该函数也可以改成RGB判断的,具体看需求如何
def getPixel(image,x,y,G,N):
    L = image.getpixel((x,y))
    if L > G:
        L = True
    else:
        L = False
 
    nearDots = 0
    if L == (image.getpixel((x - 1,y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1,y)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1,y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x,y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x,y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1,y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1,y)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1,y + 1)) > G):
        nearDots += 1
 
    if nearDots < N:
        return image.getpixel((x,y-1))
    else:
        return None
 
# 降噪 
# 根据一个点A的RGB值，与周围的8个点的RBG值比较，设定一个值N（0 <N <8），当A的RGB值与周围8个点的RGB相等数小于N时，此点为噪点 
# G: Integer 图像二值化阀值 
# N: Integer 降噪率 0 <N <8 
# Z: Integer 降噪次数 
# 输出 
#  0：降噪成功 
#  1：降噪失败 
def clearNoise(image,G,N,Z):
    draw = ImageDraw.Draw(image)
    for i in range(0,Z):
        for x in range(1,image.size[0] - 1):
            for y in range(1,image.size[1] - 1):
                color = getPixel(image,x,y,G,N)
                if color != None:
                    draw.point((x,y),color)
 
#测试代码
def NR(filepath, G=50, N=5, Z = 4):
    '''# G: Integer 图像二值化阀值 # N: Integer 降噪率 0 <N <8 # Z: Integer 降噪次数 '''
    #打开图片
    image = Image.open(filepath)
    #将图片转换成灰度图片
    image = image.convert("L")
    #去噪,G = 50,N = 4,Z = 4
    clearNoise(image,G,N,Z)
    #保存图片
    image.save("noise_reduction_image\\result.jpg")
    return ccut(r'noise_reduction_image\\result.jpg')
