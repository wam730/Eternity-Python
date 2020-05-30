'''
需要解决的问题：
1、如何获取系统时间并匹配用户输入的时间，在设置时间内响铃；
2、如何绘制一套GUI使得用户便于输入设置时间（包括音乐文件路径）；
3、如何对音乐进行调节（音量大小、播放时长）；
4、如何保存用户设置为一套方案，便于用户调用。
'''
import pygame
import time
from mutagen.mp3 import MP3 
import tkinter as tk
from tkinter import filedialog
import datetime
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

    def classBegin():
        filepath = Audio.choosebeginAudio()
        beginAudio = MP3(filepath)
        pygame.mixer.init()
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play(0)
        time.sleep(beginAudio.info.length)
        pygame.mixer.music.stop()

    def classOver():
        filepath = Audio.chooseoverAudio()
        overAudio = MP3(filepath)
        pygame.mixer.init()
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play(0)
        time.sleep(overAudio.info.length)
        pygame.mixer.music.stop() 
run = True
while True:
    Hour = time.strftime('%H',time.localtime(time.time()))
    Min = time.strftime('%M',time.localtime(time.time()))
    if Hour == '20' and Min == '56':
        Audio.classBegin()
        break
    print(time.strftime('%H:%M:%S',time.localtime(time.time())))
    time.sleep(1)