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
import sys
import tkinter as tk
import threading
import myStop
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
            if not filepath.endswith('.mp3'):
                tk.messagebox.showerror(title = '格式错误', message = '请选择MP3文件')
            else:
                with open('1.txt',"w+") as f:
                    f.writelines(filepath)
            return filepath
        elif filepath.endswith('.mp3'):
             return filepath
        else:
             tk.messagebox.showerror(title = '格式错误', message = '音乐未被设置为MP3文件\n请重新设置')
    def chooseoverAudio():
         with open(r'2.txt', 'r') as f:
             filepath = f.read()
         if filepath == '':
             root = tk.Tk()
             root.withdraw()
             root.title('Choose the path of class over audio')
             filepath = filedialog.askopenfilename()
             if not filepath.endswith('.mp3'):
                 tk.messagebox.showerror(title = '格式错误', message = '请选择MP3文件')
             else:
                 with open('2.txt',"w+") as f:
                    f.writelines(filepath)
                    return filepath
         elif filepath.endswith('.mp3'):
             return filepath
         else:
             tk.messagebox.showerror(title = '格式错误', message = '音乐未被设置为MP3文件\n请重新设置')
          
    def beginAudio():
        root = tk.Tk()
        root.withdraw()
        root.title('Choose the path of class begin audio')
        filepath = filedialog.askopenfilename()
        if not filepath.endswith('.mp3'):
            tk.messagebox.showerror(title = '格式错误', message = '请选择MP3文件')
            return Audio.beginAudio()
        else:
            with open('1.txt',"w+") as f:
                f.writelines(filepath)
                return filepath

    def overAudio():
        root = tk.Tk()
        root.withdraw()
        root.title('Choose the path of class begin audio')
        filepath = filedialog.askopenfilename()
        if not filepath.endswith('.mp3'):
            tk.messagebox.showerror(title = '格式错误', message = '请选择MP3文件')
            return Audio.overAudio()
        else:
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
             if not filepath.endswith('.mp3'):
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
#用于显示消息，点击“开始”后提示用户程序已经开始运行，实现自检,防止运行错误
def before_start():
    with open('Begin.txt','r') as f:
        x = f.read()
    with open('Over.txt','r') as g:
        y = g.read()
    with open('1.txt','r') as h:
        z = h.read()
    with open('2.txt','r') as i:
        a = i.read()
    if not z.endswith('.mp3'):
        tk.messagebox.showerror(title = '格式错误', message = '上课音乐未被设置为MP3文件\n请重新设置')
        Audio.beginAudio()
    if not a.endswith('.mp3'):
        tk.messagebox.showerror(title = '格式错误', message = '下课音乐未被设置为MP3文件\n请重新设置')
        Audio.overAudio()
    if x =='' and y =='':
        tk.messagebox.showerror(title = '时间不正确', message = '你还未设置响铃时间\n请在下方输入框中输入时间\n设置完成后请在“开始/停止/暂停”中点击“开始”')
    elif JudgeTime(x) and JudgeTime(y):
        global st
        st +=1
        print(st)
        if st == 1:
            showTime.insert('end','开始工作\n上课铃响铃时间为：{0}\n下课铃响铃时间为：{1}\n'.format(x,y))
            start()
        else:
            tk.messagebox.showerror(title = '错误', message = '请不要重复点击“开始”')
    else:
        tk.messagebox.showwarning(title = '时间不正确', message = '你可能还未设置响铃时间\n请在下方输入框中输入时间\n设置完成后请在“开始/停止/暂停”中点击“开始”')
#响铃函数，使程序在规定时间响铃
def start():
    H = time.strftime('%H')
    M = time.strftime('%M')
    S = time.strftime('%S')
    global timer
    timer = threading.Timer(1,start)
    timer.start()
    with open('Begin.txt','r') as f:
        x = f.read()
    with open('Over.txt','r') as g:
        y = g.read()
    x = x.split()
    y = y.split()
    #print('现在是（测试）',H+':'+M+':'+S)
    if H+':'+M+':'+S in x:
        print("Work")
        Audio.classbeginAudio()
    if H+':'+M+':'+S in y:
        print("Work")
        Audio.classoverAudio()
#结束程序函数
def end():
    x = tkinter.messagebox.askquestion('提示', '确认退出吗？')
    if x == 'yes':
        global st
        st = 0
        root.destroy()
        os._exit(0)
        print('Stop')
    else:
        pass
#暂停程序函数
def pause():
    x = tkinter.messagebox.askquestion('提示', '确认暂停吗？')
    if x == 'yes':
        try:
            #这里调用写的myStop库来实现结束线程
            myStop.stop_thread(timer)
        except:
            tk.messagebox.showerror(title = '程序未运行',message = '程序似乎还没有开始运行')
        else:
            global st
            st = 0
            print(st)
            print('Pause')
            myStop.stop_thread(timer)
            tk.messagebox.showinfo(title = '程序已暂停',message = '程序已经暂停运行\n再次点击“开始”以运行程序')
#更新系统时间显示函数
def update_time():
    clock_label.configure(text=time.strftime('现在是：%Y-%m-%d %H:%M:%S',time.localtime()))
    clock_label.after(1000,update_time)
#时间格式正误判断函数
def JudgeTime(data):
    if data == '':
        return True
    data = list(data.split())
    for t in data:
        if '：' in t:
            tk.messagebox.showerror(title = '格式错误', message = '请不要输入中文状态下的冒号“ ：”')
            return False
        s = re.match('\d\d:\d\d:\d\d',t)
        if s == None:
            tk.messagebox.showerror(title = '格式错误', message = '输入中有错入的格式，请检查后重新输入')
            return False
    return True
#增加上课时间函数
def appendBegin():
    def aaa():
        x = inputTime.get()
        if x == '':
            window.destroy()
            return appendBegin()
        print(x,type(x))
        if JudgeTime(x):
            with open('Begin.txt','a+') as f:
                f.writelines(' '+x)
            tk.messagebox.showinfo(title = '增加时间' ,message = '增加上课时间成功')
            window.destroy()
            return True
        else:
            window.destroy()
            return appendBegin()
    window = tk.Tk()
    window.title('请输入时间,并点击确认')
    window.iconbitmap("虹.ico")
    inputTime = tk.Entry(window,width = 50,bd=3)
    button = tk.Button(window,text = '确认',width = 10,height = 1,command=aaa,font=('微软雅黑',10))
    inputTime.pack()
    button.pack()
    window.mainloop()
#增加上课时间函数
def appendOver():
    def aaa():
        x = inputTime.get()
        if x == '':
            window.destroy()
            return appendBegin()
        print(x,type(x))
        if JudgeTime(x):
            with open('Over.txt','a+') as f:
                f.writelines(' '+x)
            tk.messagebox.showinfo(title = '增加时间' ,message = '增加下课时间成功')
            window.destroy()
            return True
        else:
            window.destroy()
            return appendOver()
    window = tk.Tk()
    window.title('请输入时间,并点击确认')
    window.iconbitmap("虹.ico")
    inputTime = tk.Entry(window,width = 50,bd=3)
    button = tk.Button(window,text = '确认',width = 10,height = 1,command=aaa,font=('微软雅黑',10))
    inputTime.pack()
    button.pack()
    window.mainloop()
#删除上课时间函数
def popBegin():
    def aaa():
        x = inputTime.get()
        if x == '':
            window.destroy()
            return popBegin()
        print(x,type(x))
        if JudgeTime(x):
            with open('Begin.txt','r') as f:
                y = f.read()
            y = y.split()
            print(y)
            if x in y:
                y.remove(x)
                print(y)
                with open('Begin.txt','w+') as f:
                    for i in y:
                        f.writelines(' '+i)
                tk.messagebox.showinfo(title = '删除时间' ,message = '删除上课时间成功')
                window.destroy()
            else:
                window.destroy()
                z = tkinter.messagebox.askquestion('删除时间', '要删除的时间不存在\n重新输入请选择"确认"')
                if z == 'yes':
                    return popBegin()
        else:
              window.destroy()
              return popBegin()
    window = tk.Tk()
    window.title('请输入时间,并点击确认')
    window.iconbitmap("哭.ico")
    inputTime = tk.Entry(window,width = 50,bd=3)
    button = tk.Button(window,text = '确认',width = 10,height = 1,command=aaa,font=('微软雅黑',10))
    inputTime.pack()
    button.pack()
    window.mainloop()
#删除下课时间函数
def popOver():
    def aaa():
        x = inputTime.get()
        if x == '':
            window.destroy()
            return popBegin()
        print(x,type(x))
        if JudgeTime(x):
            with open('Over.txt','r') as f:
                y = f.read()
            y = y.split()
            print(y)
            if x in y:
                y.remove(x)
                print(y)
                with open('Over.txt','w+') as f:
                    for i in y:
                        f.writelines(' '+i)
                tk.messagebox.showinfo(title = '删除时间' ,message = '删除下课时间成功')
                window.destroy()
            else:
                window.destroy()
                z = tkinter.messagebox.askquestion('删除时间', '要删除的时间不存在\n重新输入请选择"确认"')
                if z == 'yes':
                    return popBegin()
        else:
              window.destroy()
              return popBegin()
    window = tk.Tk()
    window.title('请输入时间,并点击确认')
    window.iconbitmap("哭.ico")
    inputTime = tk.Entry(window,width = 50,bd=3)
    button = tk.Button(window,text = '确认',width = 10,height = 1,command=aaa,font=('微软雅黑',10))
    inputTime.pack()
    button.pack()
    window.mainloop()
#将输入框输入上课铃时间写入文件与显示框
def getBeginTime():
    global BeginTime
    BeginTime = inputBeginTime.get()
    if BeginTime == '':
        tk.messagebox.showerror(title='未输入',message='你还没有输入！')
    elif JudgeTime(BeginTime):
        showTime.insert('end','上课铃响铃时间为：{0}\n'.format(BeginTime))
        with open('Begin.txt',"w+") as f:
            f.writelines(BeginTime)
    return BeginTime
#将输入框输入下课铃时间写入文件与显示框
def update():
    showTime.delete(0.0, 'end')
    with open('Begin.txt',"r") as f:
     x = f.read()
    with open('Over.txt','r') as g:
     y = g.read()

    JudgeTime(x)
    JudgeTime(y)

    if x !='':
      showTime.insert('end','上课铃响铃时间为：{0}\n'.format(x.split()))
    if y !='':
       showTime.insert('end','下课铃响铃时间为：{0}\n'.format(y.split()))
    try:
        timer
    except:
        showTime.insert('end','点击“开始”以运行\n')
    else:
        pass
    if x == '':
       tk.messagebox.showwarning(title = '未设置时间', message = '你似乎还未设置上课响铃时间！')
    if y == '':
       tk.messagebox.showwarning(title = '未设置时间', message = '你似乎还未设置下课响铃时间！')
def getoverTime():
    global OverTime
    OverTime = inputOverTime.get()
    if OverTime == '':
        tk.messagebox.showerror(title='未输入',message='你还没有输入！')
    elif JudgeTime(OverTime):
        showTime.insert('end','下课铃响铃时间为：{0}\n'.format(OverTime))
        with open('Over.txt',"w+") as f:
            f.writelines(OverTime)
    return OverTime
#说明：如何设置时间函数
def howtosetTime():
    window1 = tk.Tk()
    window1.title('如何设置上下课响铃时间')
    window1.iconbitmap("心.ico")
    Text = tk.Label(window1,text = '1.请在下方第一个输入框中输入一个或多个上课铃响铃的时间（精确到秒)\n\
2.在第二个输入框中输入一个或多个上课铃响铃的时间（精确到秒）\n3.上下课铃声设置方法相同\n\
4.必须如07：00：00、09：00：30、19：45：40等才是正确形式\n5.时间请以24小时格式输入,用空格分格多个时间\n\
7.符合格式（xx：xx：xx）的时间可以输入，但超过24小时的不会响铃\n8.如果下方信息框中已经显示有时间，\
则说明之前已经设置过时间\n9.你可以在输入框中重新输入时间并点击确认来重新设置时间\n\
10.你可以点击“增加/删除时间”来增加或删除特定的时间\n11.特别注意：在输入框中输入时间点击“确认”后\
会清空以前的时间，如果你要增删时间，请选择“增加/删除时间”',justify='left',bg='white',font=('微软雅黑',13))
    Text.pack()
    window1.mainloop()
#说明：如何设置音乐函数
def howtosetAudio():
    window2 = tk.Tk()
    window2.iconbitmap("心.ico")
    window2.title('如何设置上下课铃声的音乐')
    Text = tk.Label(window2,text = '1.点击菜单栏中的选择音乐进行音乐设置\n2.程序没有默认设置上下课铃声的音乐，第一次使用请记得设置\n\
3.你还可以修改程序目录下的“1.txt”、“2.txt”来修改音乐，请选择音乐所在路径\n4.请注意：在选择音乐时，如果你中途退出选择框\
或者选择错误时，选择框会反复弹出，直至你做出正确的选择',font=('微软雅黑',15),justify='left')
    Text.pack()
    window2.mainloop()
#说明：如何使用函数
def howtouse():
    window3 = tk.Tk()
    window3.iconbitmap("心.ico")
    window3.title('如何使用程序')
    Text = tk.Label(window3,text = '使用步骤\n1、设置上下课响铃时间\n2、设置上下课响铃音乐\n3、点击“确认”按钮\n4、设置完毕后在菜单栏的“开始/停止/暂停”中\
选择“开始”\n5、严格遵循响铃设置，开始自律的（网课）生活吧！\nPS：请仔细阅读“使用说明”中其他选项',font=('微软雅黑',15),justify='left')
    Text.pack()
    window3.mainloop()
#说明：关于作者函数
def aboutAuthor():
    window4 = tk.Tk()
    window4.iconbitmap("心.ico")
    window4.title('作者与设计初衷')
    Text = tk.Label(window4,text = '作者：王*杰，******************，学号：19******\n\
设计初衷：疫情期间上网课，在这个充满诱惑的世界里我们总是很难静下心来学习，\
在学校有来自同学的压力或许还好,\n\
但是身处家中，无法通过他人评估自己的学习状态，\
浑浑噩噩，想学就学，没有作息规律。\n\
希望通过本程序，将学校的上下课作息时间带回家中，\
也算是敦促自己学习和规律自己作息的手段之一。',font=('微软雅黑',15),justify='left')
    Text.pack()
    window4.mainloop()
#选择当前方案作为响铃方案函数
def commonProgramme():
    print('Not designed.')
    print('Not designed.')
#选择高考响铃方案作为方案函数
def examProgramme():
    print('Not designed.')
    print('Not designed.')
#主程序————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
root = tk.Tk()
root.title('自动上下课打铃系统')
root.geometry('800x600')
root.resizable(width=False, height=False)
root.iconbitmap("喇叭.ico")
st = 0
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
menuBar.add_cascade(label = '开始/停止/暂停',menu = startendmenu)
startendmenu.add_cascade(label = '开始',command = before_start)
startendmenu.add_cascade(label = '停止',command = end)
startendmenu.add_cascade(label = '暂停',command = pause)
'选择音乐'
musicmenu = tk.Menu(menuBar,tearoff=0)
menuBar.add_cascade(label = '选择音乐',menu = musicmenu)
musicmenu.add_cascade(label = '上课铃声',command = Audio.beginAudio)
musicmenu.add_cascade(label = '下课铃声',command = Audio.overAudio)
'增删时间功能'
appendpopmenu = tk.Menu(menuBar,tearoff=0)
menuBar.add_cascade(label = '增加/删除时间',menu = appendpopmenu)
appendpopmenu.add_cascade(label = '增加上课时间',command = appendBegin)
appendpopmenu.add_cascade(label = '增加下课时间',command = appendOver)
appendpopmenu.add_cascade(label = '删除上课时间',command = popBegin)
appendpopmenu.add_cascade(label = '删除下课时间',command = popOver)
#显示当前时间
clock_label = tk.Label(root)
clock_label.pack()
update_time()
#输入并显示上课铃播放时间
TextBegin = tk.Label(root,text= '在这里输入上课时间').place(y=25,x=0)
inputBeginTime = tk.Entry(root, show = None, width = 80,bd=6)
inputBeginTime.pack()
#输入并显示下课铃播放时间
TextOver = tk.Label(root,text= '在这里输入下课时间').place(y=56,x=0)
inputOverTime = tk.Entry(root, show = None, width = 80,bd=6)
inputOverTime.pack()
#消息框
scroll = tk.Scrollbar()
showTime = tk.Text(root,height = 10, width = 80,bd=6,font=('微软雅黑',9))
showTime.pack()
scroll.pack(side=tk.RIGHT,fill=tk.Y)
scroll.config(command=showTime.xview)
showTime.config(yscrollcommand=scroll.set)
#上课铃确认按钮
BeginTimeButton = tk.Button(root, text = '确认',width = 10,height = 1,command = getBeginTime,font=('微软雅黑',10)).place(x=700,y=22)
#下课铃确认按钮
OverTimeButton = tk.Button(root, text = '确认',width = 10,height = 1,command = getoverTime,font=('微软雅黑',10)).place(x=700,y=52)
updateButton = tk.Button(root, text = '刷新时间',width = 10,height = 1,command = update,font=('微软雅黑',10))#.place(x=700,y=52)
updateButton.pack()
#初始化显示，使进入程序就显示信息
update()
root.mainloop()