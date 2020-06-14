from random import randint
from os  import listdir
from PIL import Image

im = Image.open('水印.png')
width, height = im.size
pixels = dict()
for w in range(width):
    for h in range(height):
        c = im.getpixel((w, h))[:3]
        if c != (255,255,255):
            pixels[(w, h)] = c

def addWaterMark(srcDir):
    picFiles = [srcDir + '\\' + fn for fn in listdir(srcDir)
                if fn.endswith(('.jpg','.png','.bmp','.jpeg'))]
    for fn in picFiles:
        iml = Image.open(fn)
        w, h = iml.size
        if w < width or h < height:
            continue
        p = {0:(0,0),
             1:((w - width)//2, (h - height)//2),
             2:(w - width, h - height)}
        position = randint(0,2)
        left, top = p[position]
        for p, c in pixels.items():
            try:
                iml.putpixel((p[0] + left, p[1] + top), c)
            except:
                iml.putpixel((p[0] + left, p[1] + top),
                             sum(c)//len(c))
        iml.save(fn[:-4] + '_new.' + fn[-4:])

addWaterMark('.')
