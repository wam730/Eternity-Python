import tkinter as tk
window = tk.Tk()
window.title('My first window')
window.geometry('800x600')

def hit(var):
     if var == '1': 
          return 'Hit successful！\n'
     else:
          return 'The text you have inputted is not 1.\n'
     
def get():
    var = e.get()
    hit(var)
    t.insert('end',hit(var))
    
l = tk.Label(window,text = 'This is a test window',bg='white',font=('Arial',12)
             ,width=60,height=2)
e = tk.Entry(window,show=None)
b1 = tk.Button(window, text='Ok', width=10,
               height=2, command=get)
t = tk.Text(window,height=10)

l.pack()
e.pack()
b1.pack()
t.pack()

window.mainloop()
