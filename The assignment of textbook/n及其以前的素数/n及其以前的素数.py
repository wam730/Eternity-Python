import easygui as eg
import tkinter as tk

def prime(n):
    data = []
    for i in range(2,n+1):
        if not 0 in [i%j for j in range(2,i)]:
            data.append(i)
    return data

window = tk.Tk()
show = tk.Text(window)


while True:
    n = eg.enterbox(msg='Please input n',strip = False)
    try:
        assert(int(n)>=1 or n == None)
    except:
        eg.msgbox(msg = "\n{0} is error. The n you inputted must >= 1 and must a int-number!".format(n)
                  ,ok_button = 'Re-input')
    else:
        n = int(n)
        show.pack()
        text = 'The prime numbers have: \n'
        show.insert('end',prime(n))
        exit = eg.buttonbox(msg = "Do you want to exit?", title = 'Exit', choices=('Yes','No'))
        try:
            assert(exit == 'No')
            show.delete('1.0','end')
        except:
            window.destroy()
            break
#也可以换一种方式实现求前n个素数，不过在理解上比这个困难,用筛选法求素数:
window.mainloop()
'''
def prime1(n):
    data = [i for i in range(2,n+1)]
    m = int(n**0.5)
    for index, value in enumerate(data):
        if value > m:
            break
        data[index+1:] = filter(lambda x: x%value != 0,data[index+1:])
    return data
print('\n',prime1(n))
'''