# 导入弹窗库
import tkinter as tk
import tkinter.messagebox 
# 1.创建一个主窗口
root = tk.Tk()

# 提示消息框
tkinter.messagebox.showinfo('提示','恭喜你，账号注册成功！')

# 消息警告框
tkinter.messagebox.showwarning('警告','注意保护你的密码！')

# 错误消息框
tkinter.messagebox.showerror('错误','你的密码错误，请重新输入！')

# 对话框
#是/否，返回值yes/no
tkinter.messagebox.askquestion('提示', '确定要登录吗')

#确定/取消，返回值true/false
tkinter.messagebox.askokcancel('提示', '确定删除文件吗？')

#是/否，返回值true/false
tkinter.messagebox.askyesno('提示', '确定保存密码吗？')

#重试/取消，返回值true/false
tkinter.messagebox.askretrycancel('提示', '要执行此操作吗')

# 2.程序一直循环，直到我们关闭窗口
root.mainloop()
