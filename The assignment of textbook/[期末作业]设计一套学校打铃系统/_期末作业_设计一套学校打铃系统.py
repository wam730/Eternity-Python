'''
需要解决的问题：
1、如何获取系统时间并匹配用户输入的时间，在设置时间内响铃；
2、如何绘制一套GUI使得用户便于输入设置时间（包括音乐文件路径）；
3、如何对音乐进行调节（音量大小、播放时长）；
4、如何保存用户设置为一套方案，便于用户调用。
'''
import pygame
import time
import datetime
import re
import tkinter.messagebox
import tkinter as tk
from mutagen.mp3 import MP3 
from tkinter import filedialog

class Audio():

    def choosebeginAudio():
        with open(r'1.txt', 'r') as f:
            filepath = f.read()
        if filepath == '':
            root = tk.Tk()
            root.withdraw()
            root.title('Choose the path of class begin audio')
            filepath = filedialog.askopenfilename()
            with open('1.txt',"a+") as f:
                f.writelines(filepath)
            return filepath
        else:
            return filepath

    def chooseoverAudio():
         with open(r'2.txt', 'r') as f:
             filepath = f.read()
         if filepath == '':
             root = tk.Tk()
             root.withdraw()
             root.title('Choose the path of class over audio')
             filepath = filedialog.askopenfilename()
             with open('2.txt',"a+") as f:
                 f.writelines(filepath)
             return filepath
         else:
             return filepath

    def chooseotherAudio(n):
         with open(r'3.txt', 'r') as f:
             filepath = f.read()
         if filepath == '':
             root = tk.Tk()
             root.withdraw()
             root.title('Choose the path of class over audio')
             filepath = filedialog.askopenfilename()
             with open('3.txt',"a+") as f:
                 f.writelines(filepath)
             return filepath
         else:
             return filepath

    def classbeginAudio():
        filepath = Audio.choosebeginAudio()
        beginAudio = MP3(filepath)
        pygame.mixer.init()
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play(0)
        time.sleep(beginAudio.info.length)
        pygame.mixer.music.stop()

    def classoverAudio():
        filepath = Audio.chooseoverAudio()
        overAudio = MP3(filepath)
        pygame.mixer.init()
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play(0)
        time.sleep(overAudio.info.length)
        pygame.mixer.music.stop() 

    def otherAudio():
        filepath = Audio.chooseotherAudio()
        overAudio = MP3(filepath)
        pygame.mixer.init()
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play(0)
        time.sleep(overAudio.info.length)
        pygame.mixer.music.stop() 

def start():
    with open('Begin.txt','r') as f:
        x = f.read()
        if x != '':
            showBeginTime.insert('end','开始工作\t上课铃响铃时间为：{0}\n'.format(x))
            while True:
                root.mainloop()
                x = x.split(' ')
                print(x)
                time.sleep(1)
                now_h = datetime.datetime.now().strftime('%H')
                now_m = datetime.datetime.now().strftime('%M')
                now_hm = now_h + ':' + now_m
                if now_hm in x:
                     Audio.classbeginAudio()
                     continue
            return True
        else:
            tk.messagebox.showwarning(title = '时间不正确', message = '你还未设置响铃时间\n请在下方输入框中输入时间后，点击“确认”再点击“开始”')

def update_time():
    clock_label.configure(text=time.strftime('现在是：%Y-%m-%d %H:%M:%S',time.localtime()))
    clock_label.after(1000,update_time)

def judgebeginTime():
    data = list(BeginTime.split(' '))
    for t in data:
        s = re.match('\d\d:\d\d',t)
        if s == None:
            tk.messagebox.showerror(title = '格式错误', message = '输入中有错入的格式，请检查后重新输入')
            return False
    return True

def judgeoverTime():
    data = list(OverTime.split(' '))
    for t in data:
        s = re.match('\d\d:\d\d',t)
        if s == None:
            tk.messagebox.showerror(title = '格式错误', message = '输入中有错入的格式，请检查后重新输入')
            return False
    return True

def getBeginTime():
    global BeginTime
    BeginTime = inputBeginTime.get()
    if judgebeginTime():
        showBeginTime.insert('end','上课铃响铃时间为：{0}\n'.format(BeginTime))
        with open('Begin.txt',"w+") as f:
            f.writelines(BeginTime)
    return BeginTime

def getoverTime():
    global OverTime
    BeginTime = inputOverTime.get()
    if judgeoverTime():
        showOverTime.insert('end','上课铃响铃时间为：{0}\n'.format(OverTime))
        overTimelist = list(OverTime)
    return OverTime

#主程序
root = tk.Tk()
root.title('自动上下课打铃系统')
#开始按钮
startButton = tk.Button(root,text = '开始', width = 10, height = 2, command = start).pack(side = 'top')
#显示当前时间
clock_label = tk.Label(root)
clock_label.pack()
update_time()
#输入并显示上课铃播放时间
showBeginText = tk.Label(root,text = '请在下方输入框中输入一个或多个上课铃响铃的时间（精确到分）\n\
如07:30、09：00等才是正确形式，且时间请以24小时格式输入\n并用空格分格多个时间，注意，符合格式的时间可以输入，但不会响铃\
\n如果下方输入框中已经有时间，将按照框中时间运行\n你可以删除时间重新输入时间并点\
击确认重新设置时间',bg='white',width=110,height=5)
showBeginText.pack()

inputBeginTime = tk.Entry(root, show = None, width = 110)
inputBeginTime.pack()

showBeginTime = tk.Text(root,height = 3)
showBeginTime.pack()

BeginTimeButton = tk.Button(root, text = '确认',width = 10,height = 2,command = getBeginTime)
BeginTimeButton.pack()

root.mainloop()

