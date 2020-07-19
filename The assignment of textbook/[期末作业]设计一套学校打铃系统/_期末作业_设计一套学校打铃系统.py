import datetime
import tkinter.messagebox
import tkinter as tk
import threading
import myStop
import os
from pygame import mixer
from time import strftime,sleep,localtime
from os import _exit
from mutagen.mp3 import MP3 
from tkinter import filedialog
from re import match
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#播放音乐与选择音乐的Audio类，不实例化该类
class Audio():

    def ChooseBeginAudio():
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
                    f.write(filepath)
            return filepath
        elif filepath.endswith('.mp3'):
             return filepath
        else:
             tk.messagebox.showerror(title = '格式错误', message = '音乐未被设置为MP3文件\n请重新设置')
             return filepath
    def ChooseOverAudio():
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
          
    def BeginAudio():
        root = tk.Tk()
        root.withdraw()
        root.title('Choose the path of class begin audio')
        filepath = filedialog.askopenfilename()
        if not filepath.endswith('.mp3'):
            tk.messagebox.showerror(title = '格式错误', message = '请选择MP3文件')
            return Audio.BeginAudio()
        else:
            with open('1.txt',"w+") as f:
                f.write(filepath)
                return filepath

    def OverAudio():
        root = tk.Tk()
        root.withdraw()
        root.title('Choose the path of class begin audio')
        filepath = filedialog.askopenfilename()
        if not filepath.endswith('.mp3'):
            tk.messagebox.showerror(title = '格式错误', message = '请选择MP3文件')
            return Audio.OverAudio()
        else:
            with open('2.txt',"w+") as f:
                f.writelines(filepath)
                return filepath


    def ChooseOtherAudio(n):
         with open(r'3.txt', 'r') as f:
             filepath = f.read()
         if filepath == '':
             root = tk.Tk()
             root.withdraw()
             root.title('Choose the path of other audio')
             filepath = filedialog.askopenfilename()
             if not filepath.endswith('.mp3'):
                tk.messagebox.showerror(title = '格式错误', message = '请选择MP3文件')
             with open('3.txt',"w+") as f:
                 f.writelines(filepath)
             return filepath
         else:
             return filepath

    def ClassBeginAudio():
        filepath = Audio.ChooseBeginAudio()
        beginAudio = MP3(filepath)
        mixer.init()
        mixer.music.load(filepath)
        mixer.music.play(0)
        sleep(beginAudio.info.length)
        mixer.music.stop()

    def ClassOverAudio():
        filepath = Audio.ChooseOverAudio()
        overAudio = MP3(filepath)
        mixer.init()
        mixer.music.load(filepath)
        mixer.music.play(0)
        sleep(overAudio.info.length)
        mixer.music.stop()

    def OtherAudio():
        filepath = Audio.ChooseOtherAudio()
        overAudio = MP3(filepath)
        mixer.init()
        mixer.music.load(filepath)
        mixer.music.play(0)
        sleep(overAudio.info.length)
        mixer.music.stop() 

#“响铃”核心功能、菜单栏“开始”-------------------------------------------------------------------------------------------------------------------------------

#点击“开始”后提示用户程序已经开始运行并自检,防止运行错误
def BeforeStart():
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
        Audio.BeginAudio()
    if not a.endswith('.mp3'):
        tk.messagebox.showerror(title = '格式错误', message = '下课音乐未被设置为MP3文件\n请重新设置')
        Audio.OverAudio()
    if x =='' and y =='':
        tk.messagebox.showerror(title = '时间不正确', message = '你还未设置响铃时间\n请在下方输入框中输入时间\n设置完成后请在“开始/停止/暂停”中点击“开始”')
    elif JudgeTime(x) and JudgeTime(y):
        global st
        st +=1
        if st == 1:
            tk.messagebox.showinfo(title = '程序开始运行', message = '程序开始运行')
            ShowTime.insert('end','开始工作\n上课铃响铃时间为：{0}\n下课铃响铃时间为：{1}\n'.format(x,y))
            Start()
            Update()
        elif st >=5 and st<10:
            tk.messagebox.showerror(title = '错误', message = '你很顽皮啊，不要重复点击开始哦！\n会被玩坏的！😕')
        elif st == 10:
            tk.messagebox.showerror(title = '错误', message = '你很顽皮啊，说了不要重复点击开始你还点！\n再点一次我就生气了😕')
        elif st>=10:
            tk.messagebox.showerror(title = '错误', message = '生气了(╯▔皿▔)╯\n我不陪你玩了,再见！！！\n(￢︿̫̿￢☆)😕')
            _exit(0)
        else:
            tk.messagebox.showerror(title = '错误', message = '请不要重复点击“开始”')
    else:
        tk.messagebox.showwarning(title = '时间不正确', message = '你可能还未设置响铃时间\n请在下方输入框中输入时间\n设置完成后请在“开始/停止/暂停”中点击“开始”')

#响铃函数，使程序在规定时间响铃
def Start():
    H = strftime('%H')
    M = strftime('%M')
    S = strftime('%S')
    global timer
    timer = threading.Timer(1,Start)
    timer.start()
    with open('Begin.txt','r') as f:
        x = f.read()
    with open('Over.txt','r') as g:
        y = g.read()
    x = x.split()
    y = y.split()
    if H+':'+M+':'+S in x:
        Audio.ClassBeginAudio()
    if H+':'+M+':'+S in y:
        Audio.ClassOverAudio()

#菜单栏“停止/暂停/状态”-------------------------------------------------------------------------------------------------------------------------------------

#结束程序函数
def End():
    x = tkinter.messagebox.askquestion('提示', '确认退出吗？')
    if x == 'yes':
        global st
        st = 0
        root.destroy()
        _exit(0)
        print('Stop')
    else:
        pass

#暂停程序函数
def Pause():
    x = tkinter.messagebox.askquestion('提示', '确认暂停吗？')
    if x == 'yes':
        try:
            #这里调用别人写的 myStop库 来实现结束线程
            myStop.stop_thread(timer)
        except:
            tk.messagebox.showerror(title = '程序未运行',message = '程序似乎还没有开始运行')
        else:
            global st
            st = 0
            myStop.stop_thread(timer)
            ShowTime.insert('end','\n程序已暂停\n再次点击“开始”以运行程序')
            tk.messagebox.showinfo(title = '程序已暂停',message = '程序已经暂停运行\n再次点击“开始”以运行程序')

#状态查询函数
def Status():
    if st == 0:
        tk.messagebox.showinfo(title = '程序未运行',message = '程序已经暂停运行或者还未运行\n点击“开始”以运行程序')
    else:
        tk.messagebox.showinfo(title = '程序正在运行',message = '程序正在运行中\n点击“暂停/退出”可以结束运行')

#菜单栏“增加/删除时间”---------------------------------------------------------------------------------------------------------------------------------------

#增加上课时间函数
def AppendBegin():
    def aaa():
        x = inputTime.get()
        if x == '':
            window.destroy()
            return appendBegin()
        if JudgeTime(x):
            with open('Begin.txt','a+') as f:
                f.writelines(' '+x)
            Update()
            tk.messagebox.showinfo(title = '增加时间' ,message = '增加上课时间成功')
            window.destroy()
            return True
        else:
            window.destroy()
            return AppendBegin()
    window = tk.Tk()
    window.title('请输入时间,并点击确认')
    window.iconbitmap("虹.ico")
    inputTime = tk.Entry(window,width = 50,bd=3)
    button = tk.Button(window,text = '确认',width = 10,height = 1,command=aaa,font=('微软雅黑',10))
    inputTime.pack()
    button.pack()
    window.mainloop()

#增加上课时间函数
def AppendOver():
    def aaa():
        x = inputTime.get()
        if x == '':
            window.destroy()
            return AppendOver()
        if JudgeTime(x):
            with open('Over.txt','a+') as f:
                f.writelines(' '+x)
            Update()
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
def PopBegin():
    def aaa():
        x = inputTime.get()
        if x == '':
            window.destroy()
            return PopBegin()
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
                Update()
                tk.messagebox.showinfo(title = '删除时间' ,message = '删除上课时间成功')
                window.destroy()
            else:
                window.destroy()
                z = tkinter.messagebox.askquestion('删除时间', '要删除的时间不存在\n重新输入请选择"确认"')
                if z == 'yes':
                    return PopBegin()
        else:
              window.destroy()
              return PopBegin()
    window = tk.Tk()
    window.title('请输入时间,并点击确认')
    window.iconbitmap("哭.ico")
    inputTime = tk.Entry(window,width = 50,bd=3)
    button = tk.Button(window,text = '确认',width = 10,height = 1,command=aaa,font=('微软雅黑',10))
    inputTime.pack()
    button.pack()
    window.mainloop()

#删除下课时间函数
def PopOver():
    def aaa():
        x = inputTime.get()
        if x == '':
            window.destroy()
            return popBegin()
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
                Update()
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

#主界面输入与显示-------------------------------------------------------------------------------------------------------------------------------------------

#将输入框输入上课铃时间写入文件与显示框
def GetBeginTime():
    global BeginTime
    BeginTime = InputBeginTime.get()
    if BeginTime == '':
        tk.messagebox.showerror(title='未输入',message='你还没有输入！')
    elif JudgeTime(BeginTime):
        ShowTime.insert('end','上课铃响铃时间为：{0}\n'.format(BeginTime))
        with open('Begin.txt',"w+") as f:
            f.writelines(BeginTime)
    Update()
    return BeginTime

#将输入框输入下课铃时间写入文件与显示框
def GetoverTime():
    global OverTime
    OverTime = InputOverTime.get()
    if OverTime == '':
        tk.messagebox.showerror(title='未输入',message='你还没有输入！')
    elif JudgeTime(OverTime):
        ShowTime.insert('end','下课铃响铃时间为：{0}\n'.format(OverTime))
        with open('Over.txt',"w+") as f:
            f.writelines(OverTime)
    Update()
    return OverTime

#刷新显示框中的时间
def Update():
    ShowTime.delete(0.0, 'end')
    with open('Begin.txt',"r") as f:
     x = f.read()
    with open('Over.txt','r') as g:
     y = g.read()

    JudgeTime(x)
    JudgeTime(y)

    if x !='':
        ShowTime.insert('end','上课铃响铃时间为：{0}\n'.format(x.split()))
    if y !='':
        ShowTime.insert('end','下课铃响铃时间为：{0}\n'.format(y.split()))
    try:
        timer
    except:
        ShowTime.insert('end','点击“开始”以运行\n')
    else:
        pass
    if x == '':
       tk.messagebox.showwarning(title = '未设置时间', message = '你似乎还未设置上课响铃时间！')
    if y == '':
       tk.messagebox.showwarning(title = '未设置时间', message = '你似乎还未设置下课响铃时间！')

#时间格式正误判断函数
def JudgeTime(data):
    if data == '':
        return True
    data = list(data.split())
    for t in data:
        if '：' in t:
            tk.messagebox.showerror(title = '格式错误', message = '请不要输入中文状态下的冒号“ ：”')
            return False
        s = match('\d\d:\d\d:\d\d',t)
        if s == None:
            tk.messagebox.showerror(title = '格式错误', message = '输入中有错入的格式，请检查后重新输入')
            return False
    return True

#更新系统时间显示函数
def update_time():
    clock_label.configure(text=strftime('现在是：%Y-%m-%d %H:%M:%S',localtime()))
    clock_label.after(500,update_time)

#所有的使用说明---------------------------------------------------------------------------------------------------------------------------------------------

#说明：如何设置时间函数
def HowToSetTime():
    window1 = tk.Tk()
    window1.title('如何设置上下课响铃时间')
    window1.iconbitmap("心.ico")
    Text = tk.Label(window1,text = '1.请在下方第一个输入框中输入一个或多个上课铃响铃的时间（精确到秒)\n\
2.在第二个输入框中输入一个或多个上课铃响铃的时间（精确到秒）\n3.上下课铃声设置方法相同，请在英文状态下输入\n\
4.必须如07:00:00、09:00:30、19:45:40等才是正确形式\n5.时间请以24小时格式输入,用空格分格多个时间\n\
7.符合格式（xx:xx:xx）的时间可以输入，但超过24小时的不会响铃\n8.如果下方信息框中已经显示有时间，\
则说明之前已经设置过时间\n9.你可以在输入框中重新输入时间并点击确认来重新设置时间\n\
10.你可以点击“增加/删除时间”来增加或删除特定的时间\n11.特别注意：在输入框中输入时间点击“确认”后\
会清空以前的时间，如果你要增删时间，请选择“增加/删除时间”',justify='left',bg='white',font=('微软雅黑',13))
    Text.pack()
    window1.mainloop()

#说明：如何设置音乐函数
def HowToSetAudio():
    window2 = tk.Tk()
    window2.iconbitmap("心.ico")
    window2.title('如何设置上下课铃声的音乐')
    Text = tk.Label(window2,text = '1.点击菜单栏中的选择音乐进行音乐设置\n2.程序没有默认设置上下课铃声的音乐，第一次使用请记得设置\n\
3.你还可以修改程序目录下的“1.txt”、“2.txt”来修改音乐，请选择音乐所在路径（强烈不建议）\n4.请注意：在选择音乐时，如果你中途退出选择框\
或者选择错误时，选择框会反复弹出，直至你做出正确的选择',font=('微软雅黑',15),justify='left')
    Text.pack()
    window2.mainloop()

#说明：如何使用函数
def HowToUse():
    window3 = tk.Tk()
    window3.iconbitmap("心.ico")
    window3.title('如何使用程序')
    Text = tk.Label(window3,text = '使用步骤\n1、设置上下课响铃时间\n2、设置上下课响铃音乐\n3、点击“确认”按钮\n4、设置完毕后在菜单栏的“开始/退出/暂停”中\
选择“开始”\n5、严格遵循响铃设置，开始自律的（网课）生活吧！\nPS：请仔细阅读“使用说明”中其他选项',font=('微软雅黑',15),justify='left')
    Text.pack()
    window3.mainloop()

#说明：关于作者函数
def AboutAuthor():
    window4 = tk.Tk()
    window4.iconbitmap("心.ico")
    window4.title('作者与设计初衷')
    Text = tk.Label(window4,text = '作者：王钰杰\n设计初衷：疫情期间上网课，在这个充满诱惑的世界里我们总是很难静下心来学习，\
在学校有来自同学的压力或许还好,\n但是身处家中，无法通过他人评估自己的学习状态，浑浑噩噩，想学就学，没有作息规律。\n\
希望通过本程序，将学校的上下课作息时间带回家中，也算是敦促自己学习和规律自己作息的手段之一。',font=('微软雅黑',15),justify='left')
    Text.pack()
    window4.mainloop()

#说明:关于本程序
def AboutProgramme():
    window4 = tk.Tk()
    window4.iconbitmap("心.ico")
    window4.title('关于本程序')
    Texts = tk.Text(window4,font=('微软雅黑',15),height = 5, width = 35)
    Texts.insert('end','版本号:1.19.2,共19次修改,本版本为提交的最终版本\nGitHub源代码地址:http://dwz.win/GcP（短链，ctrl+c复制）\n后续会继续改进本程序')
    Texts.pack()
    window4.mainloop()

#说明：关于方案的选择
def HowToSave():
    window5 = tk.Tk()
    window5.iconbitmap("心.ico")
    window5.title('如何选择与保存方案&小贴士')
    Text = tk.Label(window5,text = '1.点击“导出方案1到当前”，会将方案1中的内容导入当前程序,\
如果程序正在运行，则将按照方案1继续运行；\n选择后会将时间显示在消息框中，“导出方案2到当前”同理\n\
2.保存方案时，你可以先通过点击“选择音乐”来为你的不同方案选择不一样的音乐，在导入时会一并导入;\
\n3.点击“保存当前到方案1”，会将当前消息框中的上下课时间保存到“方案1”中；\
"保存当前到方案2"同理\n4.请注意：如此逻辑你其实可以拥有3套方案，但当你将方案导入时，会直接覆盖消息框的时间\n\
如果你未将其保存，你将会丢失消息框中的方案\n5.将消息框中时间保存到方案，那么该方案上一次保存的数据会被覆盖',font=('微软雅黑',15),justify='left')
    Text.pack()
    window5.mainloop()

#菜单栏“方案选择与保存”-------------------------------------------------------------------------------------------------------------------------------------

#保存到方案1
def SaveProgramme1():
    wh = tk.messagebox.askquestion("提示",'你确认要将消息框中时间写入到方案1吗?')
    if wh == 'yes':
        with open('Begin.txt','r+') as a:
          x = a.read()
          with open('Over.txt','r+') as b:
              y = b.read()
              with open('方案1.txt','w+') as c:
                  x = x.split()
                  y = y.split()
                  for i in x:
                      c.writelines(' '+i)
                  c.write('\n')
                  for j in y:
                      c.writelines(' '+j)
        with open('1.txt','r') as q:
            e = q.read()
            with open('方案1Begin.txt','w+') as b1:
                b1.writelines(e)
        with open('2.txt','r') as w:
            r = w.read()
            with open('方案1Over.txt','w+') as o1:
                o1.writelines(r)
        tk.messagebox.showinfo(title = '保存到方案1', message = '成功将当前数据保存到了方案1')
    else:
        tk.messagebox.showinfo('取消','已取消操作!')

#打开方案1
def Programme1():
    wh = tk.messagebox.askquestion("提示",'你确认要导入方案1作为响铃数据吗?')
    if wh == 'yes':
        with open('方案1.txt','r+') as c:
            x = c.readlines()
            with open('Begin.txt','w+') as a:
                a.write(x[0])
                with open('Over.txt','w+') as b:
                    b.write(x[1])
        with open('方案1Begin.txt','r') as b1:
            g = b1.readline()
            with open('方案1Over.txt','r') as o1:
                h = o1.readline()
                with open('1.txt','w+') as d:
                    d.write(g)
                    with open('2.txt','w+') as e:
                        e.write(h)
        Update()
        tk.messagebox.showinfo(title = '打开方案1', message = '成功导入了方案1\n程序将按照方案1执行')
    else:
        tk.messagebox.showinfo('取消','已取消操作!')

#保存到方案2
def SaveProgramme2():
    wh = tk.messagebox.askquestion("提示",'你确认要将消息框中时间写入到方案2吗?')
    if wh == 'yes':
        with open('Begin.txt','r+') as a:
            x = a.read()
            with open('Over.txt','r+') as b:
                y = b.read()
                with open('方案2.txt','w+') as c:
                    x = x.split()
                    y = y.split()
                    for i in x:
                        c.writelines(' '+i)
                    c.write('\n')
                    for j in y:
                        c.writelines(' '+j)
        with open('1.txt','r') as q:
            e = q.read()
            with open('方案2Begin.txt','w+') as b2:
                b2.writelines(e)
        with open('2.txt','r') as w:
            r = w.read()
            with open('方案2Over.txt','w+') as o2:
                o2.writelines(r)
        tk.messagebox.showinfo(title = '保存到方案2', message = '成功将当前数据保存到了方案2')
    else:
        tk.messagebox.showinfo('取消','已取消操作!')

#打开方案2
def Programme2():
    wh = tk.messagebox.askquestion("提示",'你确认要导入方案2作为响铃数据吗?')
    if wh == 'yes':
        with open('方案2.txt','r+') as c:
            x = c.readlines()
            with open('Begin.txt','w+') as a:
                a.write(x[0])
                with open('Over.txt','w+') as b:
                    b.write(x[1])
        with open('方案2Begin.txt','r') as b2:
            g = b2.readline()
            with open('方案2Over.txt','r') as o2:
                h = o2.readline()
                with open('1.txt','w+') as d:
                    d.write(g)
                    with open('2.txt','w+') as e:
                        e.write(h)
        Update()
        tk.messagebox.showinfo(title = '打开方案2', message = '成功导入了方案2\n程序将按照方案2执行')
    else:
        tk.messagebox.showinfo('取消','已取消操作!')

#展示方案1数据
def ShowPlan1():
    window6 = tk.Tk()
    window6.iconbitmap("心.ico")
    window6.title('方案1具体数据')
    sh = tk.Text(window6,font=('微软雅黑',11))
    with open('方案1.txt','r+') as c:
            x = c.readlines()
            with open('方案1Begin.txt','r') as a:
                y= a.readline()
                with open('方案1Over.txt','r') as b:
                    z = b.readline()
                    sh.insert('end','上课时间:{0}下课时间:{1}\n上课铃音乐路径:{2}\n下课铃音乐路径:{3}'.format(x[0],x[1],y,z))
    sh.pack()
    window6.mainloop()

#展示方案2数据
def ShowPlan2():
    window7 = tk.Tk()
    window7.iconbitmap("心.ico")
    window7.title('方案2具体数据')
    sh = tk.Text(window7,font=('微软雅黑',11))
    with open('方案2.txt','r+') as c:
            x = c.readlines()
            with open('方案2Begin.txt','r') as a:
                y= a.readline()
                with open('方案2Over.txt','r') as b:
                    z = b.readline()
                    sh.insert('end','上课时间:{0}下课时间:{1}\n上课铃音乐路径:{2}\n下课铃音乐路径:{3}'.format(x[0],x[1],y,z))
    sh.pack()
    window7.mainloop()

#-------------------------------------------------------------------主程序---------------------------------------------------------------------------------
root = tk.Tk()
root.title('自动上下课打铃系统')
root.geometry('800x600')
root.resizable(width=False, height=False)
root.iconbitmap("laba.ico")
st = 0

#菜单栏----------------------------------------------------------------------------------------------------------------------------------------------------
menuBar = tk.Menu(root)
'使用说明'
usemenu = tk.Menu(menuBar,tearoff=0)
menuBar.add_cascade(label = '使用说明', menu = usemenu)
usemenu.add_command(label = '上课时间设置',command = HowToSetTime)
usemenu.add_command(label = '如何设置音乐',command = HowToSetAudio)
usemenu.add_command(label = '如何使用程序',command = HowToUse)

root.config(menu=menuBar)

'方案选择'
selectmenu = tk.Menu(menuBar,tearoff=0)
menuBar.add_cascade(label = '方案选择与保存',menu = selectmenu)
selectmenu.add_cascade(label = '导出方案1到当前',command = Programme1)
selectmenu.add_cascade(label = '导出方案2到当前',command = Programme2)
selectmenu.add_cascade(label = '保存当前到方案1',command = SaveProgramme1)
selectmenu.add_cascade(label = '保存当前到方案2',command = SaveProgramme2)
selectmenu.add_cascade(label = '查看方案1数据',command = ShowPlan1)
selectmenu.add_cascade(label = '查看方案2数据',command = ShowPlan2)
selectmenu.add_cascade(label = '如何选择与保存方案',command = HowToSave)
'开始/暂停/退出/状态'
startendmenu = tk.Menu(menuBar,tearoff=0)
menuBar.add_cascade(label = '开始/暂停/退出/状态',menu = startendmenu)
startendmenu.add_cascade(label = '开始',command = BeforeStart)
startendmenu.add_cascade(label = '暂停',command = Pause)
startendmenu.add_cascade(label = '退出',command = End)
startendmenu.add_cascade(label = '状态',command = Status)
'选择音乐'
musicmenu = tk.Menu(menuBar,tearoff=0)
menuBar.add_cascade(label = '选择音乐',menu = musicmenu)
musicmenu.add_cascade(label = '上课铃声',command = Audio.BeginAudio)
musicmenu.add_cascade(label = '下课铃声',command = Audio.OverAudio)
'增删与刷新时间功能'
appendpopmenu = tk.Menu(menuBar,tearoff=0)
menuBar.add_cascade(label = '增加/删除/刷新时间',menu = appendpopmenu)
appendpopmenu.add_cascade(label = '刷新窗口时间',command = Update)
appendpopmenu.add_cascade(label = '增加上课时间',command = AppendBegin)
appendpopmenu.add_cascade(label = '增加下课时间',command = AppendOver)
appendpopmenu.add_cascade(label = '删除上课时间',command = PopBegin)
appendpopmenu.add_cascade(label = '删除下课时间',command = PopOver)
'关于'
aboutmenu = tk.Menu(menuBar,tearoff=0)
menuBar.add_cascade(label = '关于',menu = aboutmenu)
aboutmenu.add_command(label = '作者与设计初衷',command = AboutAuthor)
aboutmenu.add_command(label = '关于本程序',command = AboutProgramme)
#主界面显示------------------------------------------------------------------------------------------------------------------------------------------------

#显示当前时间
clock_label = tk.Label(root)
clock_label.pack()
update_time()

#输入并显示上课铃播放时间
TextBegin = tk.Label(root,text= '请在这一行输入上课时间：').place(y=25,x=0)
InputBeginTime = tk.Entry(root, show = None, width = 80,bd=6)
InputBeginTime.pack()

#输入并显示下课铃播放时间
TextOver = tk.Label(root,text= '请在这一行输入下课时间：').place(y=56,x=0)
InputOverTime = tk.Entry(root, show = None, width = 80,bd=6)
InputOverTime.pack()

#消息框
scroll = tk.Scrollbar()
ShowTime = tk.Text(root,height = 10, width = 69,bd=6,font=('微软雅黑',10))
ShowTime.pack()
scroll.pack(side=tk.RIGHT,fill=tk.Y)
scroll.config(command=ShowTime.xview)
ShowTime.config(yscrollcommand=scroll.set)

#上课铃确认按钮
BeginTimeButton = tk.Button(root, text = '确认',width = 10,height = 1,command = GetBeginTime,font=('微软雅黑',10)).place(x=700,y=22)

#下课铃确认按钮
OverTimeButton = tk.Button(root, text = '确认',width = 10,height = 1,command = GetoverTime,font=('微软雅黑',10)).place(x=700,y=52)

#刷新消息框按钮
UpdateButton = tk.Button(root, text = '刷新时间',width = 10,height = 1,command = Update,font=('微软雅黑',10)).place(x=700,y=82)

#背景图片
photo1=tkinter.PhotoImage(file=r"hua.png")
label1=tkinter.Label(root,image=photo1).place(x=670,y=456)  
photo2=tkinter.PhotoImage(file=r"hua.png")
label2=tkinter.Label(root,image=photo2).place(x=540,y=456)  
photo3=tkinter.PhotoImage(file=r"hua.png")
label3=tkinter.Label(root,image=photo3).place(x=410,y=456)
photo4=tkinter.PhotoImage(file=r"hua.png")
label4=tkinter.Label(root,image=photo4).place(x=280,y=456)
photo5=tkinter.PhotoImage(file=r"hua.png")
label5=tkinter.Label(root,image=photo5).place(x=150,y=456)
photo6=tkinter.PhotoImage(file=r"hua.png")
label6=tkinter.Label(root,image=photo6).place(x=20,y=456)

photo7=tkinter.PhotoImage(file=r"sun.png")
label7=tkinter.Label(root,image=photo7).place(x=10,y=210)
photo8=tkinter.PhotoImage(file=r"hong.png")
label8=tkinter.Label(root,image=photo8).place(x=600,y=300)
photo9=tkinter.PhotoImage(file=r"yun.png")
label9=tkinter.Label(root,image=photo9).place(x=390,y=280)
photo10=tkinter.PhotoImage(file=r"yun.png")
label10=tkinter.Label(root,image=photo10).place(x=150,y=280)

#初始化显示，使进入程序就显示信息----------------------------------------------------------------------------------------------------------------------------
tk.messagebox.showinfo(title = 'Tips', message = '要开始运行，请在菜单栏选择“运行”\n如果你是第一次使用，请务必阅读菜单栏中的“使用说明”')
Update()
root.mainloop()