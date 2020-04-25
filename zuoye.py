import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,500)
y = np.1/(1+x^2)
z = np.cos(x*x)
plt.figure(figsize = (8,4))
''' r--:红色的破折号；bs：蓝色的方块；g^：绿色的三角形'''
'''定义颜色，宽度，图例名称，线的方式（无则为光滑曲线）
并将x与y、z分别对应'''
plt.plot(x,y,label ='sin(x)',color = 'yellow',linewidth = 2)
plt.plot(x,z,label = 'cos(x^2)',color = 'green' ,linewidth = 2)
'''x轴名称'''
plt.xlabel('Time(S)')
'''y轴名称'''
plt.ylabel('Volt')
'''标题'''
plt.title('1/(1+x^2) and arctan(x) figure')
'''y轴上下限,没有默认'''
#plt.ylim(-1.3,1.3)
'''图例'''
plt.legend()
plt.show()
