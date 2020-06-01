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
import os
import tkinter as tk
import threading
from mutagen.mp3 import MP3 
from tkinter import filedialog
#预设函数、类———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#播放音乐与选择音乐的Audio类，不实例化该类
class Audio():

    def choosebeginAudio():
        with open(r'1.txt', 'r') as f:
            filepath = f.read()
        if filepath == '':
            root = tk.Tk()
            root.withdraw()
            root.title('Choose the path of class begin audio')
            filepath = filedialog.askopenfilename()
            path = os.path.splitext(filepath)
            if not '.mp3' in re.findall('.mp3',filepath):
                tk.messagebox.showerror(title = '格式错误', message = '请选择MP3文件')
            with open('1.txt',"w+") as f:
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
             if not '.mp3' in re.findall('.mp3',filepath):
                 tk.messagebox.showerror(title = '格式错误', message = '请选择MP3文件')
             else:
                 with open('2.txt',"w+") as f:
                    f.writelines(filepath)
                    return filepath
         else:
             return filepath
          
    def beginAudio():
        root = tk.Tk()
        root.withdraw()
        root.title('Choose the path of class begin audio')
        filepath = filedialog.askopenfilename()
        if not '.mp3' in re.findall('.mp3',filepath):
            tk.messagebox.showerror(title = '格式错误', message = '请选择MP3文件')
        with open('1.txt',"w+") as f:
            f.writelines(filepath)
        return filepath

    def overAudio():
        root = tk.Tk()
        root.withdraw()
        root.title('Choose the path of class begin audio')
        filepath = filedialog.askopenfilename()
        if not '.mp3' in re.findall('.mp3',filepath):
            tk.messagebox.showerror(title = '格式错误', message = '请选择MP3文件')
        with open('2.txt',"w+") as f:
            f.writelines(filepath)
        return filepath


    def chooseotherAudio(n):
         with open(r'3.txt', 'r') as f:
             filepath = f.read()
         if filepath == '':
             root = tk.Tk()
             root.withdraw()
             root.title('Choose the path of class over audio')
             filepath = filedialog.askopenfilename()
             if not '.mp3' in re.findall('.mp3',filepath):
                tk.messagebox.showerror(title = '格式错误', message = '请选择MP3文件')
             with open('3.txt',"w+") as f:
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
#开始响铃函数
def start():
    with open('Begin.txt','r') as f:
        x = f.read()
        x = x.split(' ')
        print(x,type(x))
        if x != '':
            showBeginTime.insert('end','开始工作\t上课铃响铃时间为：{0}\n'.format(x))
            for t in x:
                if (gettime())[0]+':'+(gettime())[1] in x:
                    Audio.classbeginAudio
        else:
            tk.messagebox.showwarning(title = '时间不正确', message = '你可能还未设置响铃时间\n请在下方输入框中输入时间')
    global timer
    timer = threading.Timer(1,start)
    timer.start()
#结束程序函数
def end():
    print('Not designed.')
#更新时间显示函数
def update_time():
    clock_label.configure(text=time.strftime('现在是：%Y-%m-%d %H:%M:%S',time.localtime()))
    clock_label.after(1000,update_time)
#获取时间
def gettime():
    Hour = time.strftime('%H')
    Min = time.strftime('%M')
    global timer
    timer = threading.Timer(1,gettime)
    timer.start()
    return Hour,Min
#判断输入框输入上课铃时间是否正确函数
def judgebeginTime():
    data = list(BeginTime.split(' '))
    for t in data:
        s = re.match('\d\d:\d\d',t)
        if s == None:
            tk.messagebox.showerror(title = '格式错误', message = '输入中有错入的格式，请检查后重新输入')
            return False
    return True
#判断输入框输入下课铃时间是否正确函数
def judgeoverTime():
    data = list(OverTime.split(' '))
    for t in data:
        s = re.match('\d\d:\d\d',t)
        if s == None:
            tk.messagebox.showerror(title = '格式错误', message = '输入中有错入的格式，请检查后重新输入')
            return False
    return True
#将输入框输入上课铃时间写入文件与显示框
def getBeginTime():
    global BeginTime
    BeginTime = inputBeginTime.get()
    if judgebeginTime():
        showBeginTime.insert('end','上课铃响铃时间为：{0}\n'.format(BeginTime))
        with open('Begin.txt',"w+") as f:
            f.writelines(BeginTime)
    return BeginTime
#将输入框输入下课铃时间写入文件与显示框
def getoverTime():
    global OverTime
    BeginTime = inputOverTime.get()
    if judgeoverTime():
        showOverTime.insert('end','上课铃响铃时间为：{0}\n'.format(OverTime))
        overTimelist = list(OverTime)
    return OverTime
#说明：如何设置时间函数
def howtosetTime():
    window1 = tk.Tk()
    window1.title('如何设置上下课响铃时间')
    Text = tk.Label(window1,text = '请在下方第一个输入框中输入一个或多个上课铃响铃的时间（精确到分），\n\
    在第二个输入框中输入一个或多个上课铃响铃的时间（精确到分），\n上下课铃声设置方法相同，\
    必须如07:30、09：00、19：45等才是正确形式，并且时间请以24小时格式输入\n并用空格分格多个时间，\
    注意，符合格式（xx：xx）的时间可以输入，但超过24小时的不会响铃\n如果下方输入框中已经显示有时间，\
    则将按照框中时间运行\n你可以在输入框中重新输入时间并点击确认来重新设置时间。',bg='white',font=1)
    Text.pack()
    window1.mainloop()
#说明：如何设置音乐函数
def howtosetAudio():
    window2 = tk.Tk()
    window2.title('如何设置上下课铃声的音乐')
    Text = tk.Label(window2,text = '点击菜单栏中的选择音乐进行音乐设置，程序默认设置了上下课铃声的音乐，你可以更换他们\n\
    除此之外，你还可以修改程序目录下的“1.txt”、“2.txt”来修改音乐，修改时请选择音乐所在路径',font=1)
    Text.pack()
    window2.mainloop()
#说明：如何使用函数
def howtouse():
    window3 = tk.Tk()
    window3.title('如何使用程序')
    Text = tk.Label(window3,text = '使用步骤\n1、设置上下课响铃时间\n2、设置上下课响铃音乐\n3、设置完毕后在菜单栏的“开始\停止”中\
    选择“开始运行”\n4、严格遵循响铃设置，开始自律的（网课）生活吧！',font=1)
    Text.pack()
    window3.mainloop()
#说明：关于作者函数
def aboutAuthor():
    window4 = tk.Tk()
    window4.title('作者与设计初衷')
    Text = tk.Label(window4,text = '作者：王钰杰，中央民族大学理学院信息与计算科学2班，学号：19040041\n\
    设计初衷：疫情期间上网课，在这个充满诱惑的世界里我们总是很难静下心来学习，在学校有来自同学的压力或许还好,\n\
    但是身处家中，无法通过他人评估自己的学习状态，浑浑噩噩，想学就学，没有作息规律。\n\
    希望通过本程序，将学校的上下课作息时间带回家中，也算是敦促自己学习和规律自己作息的手段之一。',font=1)
    Text.pack()
    window4.mainloop()
#选择当前方案作为响铃方案函数
def commonProgramme():
    print('Not designed.')
#选择高考响铃方案作为方案函数
def examProgramme():
    print('Not designed.')
#主程序————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
root = tk.Tk()
root.title('自动上下课打铃系统')
root.geometry('800x600')
#菜单栏
menuBar = tk.Menu(root)
'使用说明'
usemenu = tk.Menu(menuBar,tearoff=0)
menuBar.add_cascade(label = '使用说明', menu = usemenu)
usemenu.add_command(label = '上课铃声设置',command = howtosetTime)
usemenu.add_command(label = '如何设置音乐',command = howtosetAudio)
usemenu.add_command(label = '如何使用程序',command = howtouse)
root.config(menu=menuBar)
'关于'
aboutmenu = tk.Menu(menuBar,tearoff=0)
menuBar.add_cascade(label = '关于',menu = aboutmenu)
aboutmenu.add_command(label = '作者与设计初衷',command = aboutAuthor)
'方案选择'
selectmenu = tk.Menu(menuBar,tearoff=0)
menuBar.add_cascade(label = '方案选择',menu = selectmenu)
selectmenu.add_cascade(label = '当前方案',command = commonProgramme)
selectmenu.add_cascade(label = '高考响铃方案',command = examProgramme)
'开始/停止'
startendmenu = tk.Menu(menuBar,tearoff=0)
menuBar.add_cascade(label = '开始/停止',menu = startendmenu)
startendmenu.add_cascade(label = '开始',command = start)
startendmenu.add_cascade(label = '停止',command = end)
'选择音乐'
musicmenu = tk.Menu(menuBar,tearoff=0)
menuBar.add_cascade(label = '选择音乐',menu = musicmenu)
musicmenu.add_cascade(label = '上课铃声',command = Audio.beginAudio)
musicmenu.add_cascade(label = '下课铃声',command = Audio.overAudio)
#开始按钮
startButton = tk.Button(root,text = '开始', width = 10, height = 2, command = start).place(x=725, y=0, anchor='nw')
#显示当前时间
clock_label = tk.Label(root)
clock_label.pack()
update_time()
#输入并显示上课铃播放时间
inputBeginTime = tk.Entry(root, show = None, width = 80)
inputBeginTime.pack()
'为上课铃消息框设置一个滑块'
scroll = tk.Scrollbar()
showBeginTime = tk.Text(root,height = 5, width = 80)
showBeginTime.pack()
scroll.pack(side=tk.RIGHT,fill=tk.Y)
scroll.config(command=showBeginTime.yview)
showBeginTime.config(yscrollcommand=scroll.set)
'确认按钮'
BeginTimeButton = tk.Button(root, text = '确认',width = 10,height = 2,command = getBeginTime)
BeginTimeButton.pack()
#主程序
root.mainloop()

