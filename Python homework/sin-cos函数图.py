import numpy as np
import pylab as pl
import matplotlib.font_manager as fm

myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\STKAITI.TTF')
t = np.arange(0.0,4.0*np.pi,0.01)
s  = np.sin(t)
z = np.cos(t)
pl.plot(t,s,label='正弦')
pl.plot(t,z,label='余弦')
pl.xlabel('x-变量',fontproperties='STKAITI',fontsize=10)
pl.ylabel('y-函数值',fontproperties='STKAITI',fontsize=10)
pl.title('sin-cos函数图像',fontproperties='STKAITI',fontsize=20)
pl.legend(prop=myfont)
pl.show()
