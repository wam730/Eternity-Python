'''import tkinter as tk
import tkinter.filedialog
def selectPath():
    #选择文件path_接收文件地址
    path_ = tkinter.filedialog.askopenfilename()
    #通过replace函数替换绝对文件地址中的/来使文件可被程序读取 
    #注意：\\转义后为\，所以\\\\转义后为\\
    path_=path_.replace("/","\\\\")
    #path设置path_的值
    path.set(path_)
    return path_
    
main_box = tk.Tk()
#变量path
path = tk.StringVar()
#输入框，标记，按键
tk.Label(main_box,text = "目标路径:").grid(row = 0, column = 0)
#输入框绑定变量path
tk.Entry(main_box, textvariable = path).grid(row = 0, column = 1)
tk.Button(main_box, text = "路径选择", command = selectPath).grid(row = 0, column = 2)
print(selectPath())
main_box.mainloop()'''
import tkinter as tk
from tkinter import filedialog

'''打开选择文件夹对话框'''

'''root = tk.Tk()
root.withdraw()

Folderpath = filedialog.askdirectory() #获得选择好的文件夹
Filepath = filedialog.askopenfilename() #获得选择好的文件

print('Folderpath:',Folderpath)
print('Filepath:',Filepath)'''
with open(r'D:/Python/file.txt', 'r',encoding='UTF-8') as f:
    n = f.read()

if n == '':
    print('1')
else:
    print('2')
