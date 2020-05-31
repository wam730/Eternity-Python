'''import tkinter as tk
import tkinter.messagebox
global mw,key
#------------------------------------------------------------------------
def showmingwen():
    mingwen = input1.get()
    print(mingwen)
    if mingwen == '':
        tk.messagebox.showerror(title='输入错误',
                                           message='输入错误，请检查输入')
    else:
        t1.insert('end','你输入的明文是: {0}\n'.format(mingwen))
    return mingwen

def showkeys():
    keys = input2.get()
    print(keys)
    if keys == '':
        tk.messagebox.showerror(title='输入错误',
                                           message='输入错误，请检查输入')
    else:
        t2.insert('end','你输入的key是: {0}\n'.format(keys))
    return keys
    
def jiami(mingwen,keys):
    from itertools import cycle
    func = lambda x,y:chr(ord(x)^ord(y))
    if mingwen == '' or keys == '':
        tk.messagebox.showerror(title='输入错误',
                                           message='输入错误，请检查输入')
    else:
        x = ''.join(map(func,mingwen,cycle(keys)))
        t3.insert('end',x)
        t3.insert('end','\n')

def showmiwen():
    mw = showmingwen()
    key = showkeys()
    jiami(mw,key)

#------------------------------------------------------------------------
window = tk.Tk()
window.title('异或算法实现文字加密')
window.geometry('800x800')
#------------------------------------------------------------------------
text1=tk.Label(window,text='请在下方输入框中输入你想要加密的明文',
                 bg='white',width=110,height=5,font=15)
text1.pack()

input1=tk.Entry(window,show=None,width=110)
input1.pack()

b1=tk.Button(window, text='完成输入', width=10,
               height=2,command=showmingwen)
b1.pack()

t1=tk.Text(window,height=3,font=0.5)
t1.pack()
#------------------------------------------------------------------------
text2=tk.Label(window,text='请在下方输入框中输入加密的密钥',
                 bg='white',width=110,height=5,font=15)
text2.pack()

input2=tk.Entry(window,show=None,width=110)
input2.pack()

b2=tk.Button(window, text='完成输入', width=10,
               height=2,command=showkeys)
b2.pack()

t2=tk.Text(window,height=3,font=0.5)
t2.pack()
#------------------------------------------------------------------------
text3=tk.Label(window,text='加密后的密文是',
                 bg='white',width=110,height=5,font=15)
text3.pack()

b3=tk.Button(window, text='展示密文', width=10,
               height=2,command=showmiwen)
b3.pack()

t3=tk.Text(window,height=3,font=0.5)
t3.pack()
#------------------------------------------------------------------------
window.mainloop()'''

'''import tkinter as tk
import time

# 更新时间,每一秒调用一次
def update_time():
    clock_label.configure(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
    clock_label.after(1000,update_time)

root = tk.Tk()
root.geometry('300x200')
clock_label = tk.Label(root)
clock_label.pack()
update_time()
root.mainloop()'''

import pygame
import time
import datetime

pygame.mixer.init()
pygame.mixer.music.load(r'D:\source\Eternity-Python\The assignment of textbook\[期末作业]设计一套学校打铃系统\1.mp3')

hm = ['17:16','17:17','17:18']

while True:
    time.sleep(1)
    now_h = datetime.datetime.now().strftime('%H')
    now_m = datetime.datetime.now().strftime('%M')
    now_hm = now_h + ':' + now_m
    if now_hm in hm:
        pygame.mixer.music.play()
        time.sleep(60)
