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

root = tk.Tk()

# sticky='w'，实现两个标签文本左对齐
tk.Label(root, text='用户名').grid(row=0, column=0, padx=10, pady=5, sticky='w')
tk.Label(root, text='密码').grid(row=1, column=0, padx=10, pady=5, sticky='w')

tk.Entry(root).grid(row=0, column=1, padx=10, pady=5)
tk.Entry(root, show='*').grid(row=1, column=1, padx=10, pady=5)

# 登录按钮跨越三列
tk.Button(text='登录', width=10).grid(row=2, columnspan=3, padx=5, pady=5)

tk.mainloop()

