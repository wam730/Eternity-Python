#导入库
import tkinter as tk
import os
import tkinter.messagebox
import time
import cv2
import keras.models as km
import numpy as np
import datetime
import sys

from time import strftime,localtime
from tkinter import filedialog
from PIL import Image,ImageDraw,ImageTk

#更新系统时间显示函数
def update_time():
    global TimeLabel
    show_time["text"] = datetime.datetime.now().strftime('{n}%Y{y}%m{m}%d{d} %H:%M:%S').format(n='现在是：',y='年', m='月', d='日') #+ "%d" %(datetime.datetime.now().microsecond // 100000)
    root.after(100,update_time)

#文件选择
def select_image():
    filepath = filedialog.askopenfilename()
    #path = os.path.splitext(filepath)
    #print(path,type(path))
    print(filepath,type(filepath))
    x = filepath[-4:]
    if not x in ['.jpg','.bmp','.png','.JPG','.BMP','.PNG','jpeg','JPEG']:
        tk.messagebox.showerror(title = '文件格式错误', message = '只支持jpg、bmp、png、jpeg格式的图片，请重新选择')
        #select_image_root.destroy()
        return select_image()
    else:
        #tk.messagebox._show(title = '正在识别中', message = '正在识别图片中的文字，请稍后')
        y = show_image_path.get(0.0)
        x = show_result.get(0.1,'end')
        if not x =='':
            show_result.delete(0.0, 'end')
        if y == '':
            show_image_path.insert('end', filepath)
        else:
            show_image_path.delete(0.0,'end')
            show_image_path.insert('end', filepath)
            #image_show(filepath)
            return Handle_Predication(filepath)

#处理图片
def Handle_Predication(filepath):
	image = os.listdir(r'noise_reduction_image')
	if not len(image) == 0:
		for photo in image:
			os.remove('noise_reduction_image\\' + photo)
	tk.messagebox.showinfo(title = '温馨提示', message = '图片降噪、切割和预测速度较慢，请耐心等待')
	return NR(filepath)

#预测————————————————————————————————————————————————————————————————————————————————————————
def predication(path = r'test_image'):
    image = os.listdir(path)
    if len(image) == 0:
        tk.messagebox.showerror(title='图片错误', message='你选择的图片无法进行切割，请重新选择')
        return select_image()
    else:
        for photo in image:
            show_result.insert('end', predication_image("test_image\\" + photo))

#预测接口
def predication_image(image_name):
    '''输入模型路径'''
    model = km.load_model(filepath = r'C:\Users\QQ\Desktop\Word.h5')
    obj = ['弃', '景', '掠', '谋', '堵', '席', '糊', '怀', '押', '搽', '找', '档', '超', '掂', '亡', \
        '频', '奏', '姿', '订', '表', '伦', '藻', '嘿', '哉', '冯', '肇', '两', '句', '低', '啮', '放',\
       '避', '换', '熬', '辐', '望', '愈', '荫', '绸', '笼', '慢', '哨', '霄', '聊', '就', '盼', '界',\
      '剖', '免', '毋', '倚', '屹', '矮', '墒', '防', '饮', '累', '唱', '鞋', '毅', '纶', '媳', '店', \
      '哪', '茁', '右', '岛', '草', '啡', '雾', '辩', '琵', '殿', '乍', '散', '阎', '幂', '阀', '珍', \
      '填', '茂', '未', '语', '脂', '刨', '脯', '辨', '伎', '酉', '洽', '贿', '詹', '傈', '创', '穗', \
      '幢', '坪', '靴', '液', '铰', '砍', '兜', '硅', '亨', '锄', '寞', '憾', '哑', '狠', '军', '宽', \
      '绵', '蛊', '艇', '坯', '疲', '氛', '挺', '胯', '禹', '给', '柬', '玩', '坑', '坛', '铺', '检', \
      '扼', '淄', '排', '增', '搅', '号', '炔', '黑', '凭', '管', '箍', '霹', '谆', '赐', '巳', '室',\
     '祖', '释', '敲', '播', '抢', '照', '白', '陵', '歇', '彰', '柒', '陶', '陈', '凌', '农', '灌', \
     '浚', '邦', '度', '粉', '踪', '臼', '衣', '釜', '烬', '疆', '筐', '盛', '厢', '髓', '亩', '赴', \
     '调', '饺', '葵', '丛', '胆', '命', '信', '含', '俊', '胜', '焕', '蹋', '烤', '践', '畔', '嗜', \
     '舞', '饿', '泽', '法', '肪', '讲', '现', '带', '冕', '捻', '恍', '律', '备', '按', '非', '覆', \
     '牧', '次', '嵌', '则', '诧', '冷', '稼', '淋', '巍', '睬', '饱', '痰', '栅', '突', '苟', '琢', \
     '埋', '铃', '美', '贴', '赞', '棺', '禾', '锹', '株', '又', '氯', '艰', '丹', '比', '掺', '基', \
     '围', '锑', '莹', '诛', '戈', '鼎', '彭', '抗', '蒸', '瀑', '逃', '缅', '史', '嚏', '扬', '沦', \
     '莉', '汇', '峡', '守', '肘', '迭', '返', '窟', '乒', '宪', '弦', '兄', '潮', '砧', '酵', '峪', \
     '网', '楔', '肺', '蹈', '丢', '识', '皮', '惧', '巡', '惊', '奖', '新', '喘', '钟', '难', '栓', \
     '翼', '酗', '献', '牡', '衰', '旷', '肖', '酱', '栽', '珐', '汐', '丫', '唬']

    try:
        img = Image.open(image_name)
        img = img.resize((64, 64))
    
        #调整图片的尺寸以符合数据集图片的规格
        number_data = img.getdata()
        number_data_array = np.array(number_data)
        number_data_array = number_data_array.reshape(1,64,64,3).astype(float)
        number_data_nor = number_data_array / 255
    
        pre = model.predict(number_data_nor)
        pre_list = pre.tolist()
        index = np.argmax(pre)
        #print("----------------------------------------------------------------------------------------------------")
        return obj[index] 
    except ValueError:
        tk.messagebox.showerror(title='图片错误', message='你选择的图片尺寸不符合要求，请重新选择')
        return select_image()
    except:
        tk.messagebox.showerror(title='图片错误', message='由于某种原因，你选择的图片无法识别，请重新选择')

#降噪————————————————————————————————————————————————————————————————————————————————————————
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

def NR(filepath, G = 60, N = 6, Z = 4):
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

#切割————————————————————————————————————————————————————————————————————————————————————————
def cut(image):
	re=[]
	reX=cutX(image)
	length=len(reX)
	for i in range(length):
		reY=cutY(reX[i])
		re.append(reY)
	return re

def cutX(arr):
	length=len(arr[0])
	re=[]
	count =countX(arr)
	point =findPoint(count)
	lengthP=len(point)
	if lengthP%2==1:
		lengthP=lengthP-1
	for i in range(0,lengthP,2):
		re.append(arr[point[i]:point[i+1],0:length])
	return re;

def cutY(arr):
	length=len(arr)
	#print(length)
	re=[]
	count =countY(arr)
	#print(count)
	point =findPoint(count)
	#print(point)
	for i in range(0,len(point),2):
		re.append(arr[0:length,point[i]:point[i+1]])
		
	return re;

#统计一行黑色点的个数
def countX(arr):
	count=[0]*len(arr)
	#print(len(count),len(arr))
	for h in range(len(arr)):
		count2=0
		for l in range(len(arr[h])):
			if arr[h,l,0]!=255:
				count2=count2+1
				arr[h,l]=[1]
		count[h]=count2
	return count

#统计一列黑色点的个数
def countY(arr):
	count=[0]*len(arr[0])
	#print(len(count),len(arr[0]))
	for l in range(len(arr[0])):
		count2=0
		for h in range(len(arr)):
			if arr[h,l,0]!=255:
				count2=count2+1
				arr[h,l]=[1]
		count[l]=count2
	return count

#参数：纵向或横向的映射数组  返回：一维数组，0是开始1是结束，2是开始3是结束。表示行或列的分水岭  
def findPoint(arr):
	index=-1
	re=[]
	zeroToMore(arr,index,re)
	return re

#参数：纵向或横向的映射数组 数组当前下标 返回结果集  返回：re，一维数组   递归调用，记录非零下标，表示一行的开始
def zeroToMore(arr,index,re):
	if index<len(arr)-1:
		for i in range(index+1,len(arr)):
			if arr[i]>1:
				index=i
				re.append(index)
				break
			if i==len(arr)-1:
				index=i
		moreToZero(arr,index,re)

#同上  记录第一个零下标，表示一行的结束
def moreToZero(arr,index,re):
	if index<len(arr)-1:
		for i in range(index+1,len(arr)):
			if arr[i]<=1:
				index=i
				re.append(index)
				break
			if i==len(arr)-1:
				index=i
		zeroToMore(arr,index,re)

#切割函数
def ccut(path ='noise_reduction_image\\result.jpg'):
     image = os.listdir(r"test_image")
     if len(image) != 0:
          for photo in image:
               os.remove("test_image\\" + photo)
     image=cv2.imread(path)
     retval, image = cv2.threshold(image, 175, 255, cv2.THRESH_BINARY)
     re=cut(image)
     count=0
     for i in range(len(re)):
          for j in range(len(re[i])):
               cv2.imwrite("test_image\\"+str(count)+".jpg",re[i][j])
               count=count+1
     return predication(r'test_image')
#————————————————————————————————————————————————————————————————————————————————————————
#主界面
root = tk.Tk()
#主界面标题
root.title('手写汉字识别系统®')
#主界面大小
root.geometry('800x400')
root.resizable(width = False, height = False)
#主界面图标
root.iconbitmap("icon1.ico")
#时间显示
show_time = tk.Label(root,font=('微软雅黑',10))
show_time.pack()
update_time()
#选择图片按钮
select_image_button = tk.Button(root, command = select_image, text = '点击此处选择图片', width = 15, height = 1, font = ('微软雅黑',10)).pack()
#显示选择图片的路径消息框
text_image_path = tk.Label(root, text= '你选择的图片路径是：', font=('微软雅黑',12))
text_image_path.pack()
show_image_path = tk.Text(root, height = 1.2, width = 60,bd=6,font=('微软雅黑',12))
show_image_path.pack()
#显示识别后的文字消息框
test_result = tk.Label(root, text= '识别后的结果是：', font=('微软雅黑',12))
test_result.pack()
show_result = tk.Text(root, height = 10, width = 60,bd=6,font=('微软雅黑',12))
show_result.pack()
#显示图片
photo=tkinter.PhotoImage(file=r"MUClogo.png")
show_photo=tkinter.Label(root,image=photo).place(x=0,y=0)
#显示主界面
tk.messagebox.showinfo(title = '使用提示', message = '点击按钮选择图片即可')
root.mainloop()