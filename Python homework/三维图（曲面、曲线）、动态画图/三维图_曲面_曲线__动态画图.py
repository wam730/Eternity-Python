import matplotlib as mpl
import mpl_toolkits.mplot3d
import numpy as np
import matplotlib.pyplot as plt
import sys
import warnings
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
#三维曲线
mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()

ax = fig.gca(projection = '3d')
theta = np.linspace(-4*np.pi,4*np.pi,200)

z = np.linspace(-4,4,200)*0.4
r = z**3+100
x = r*np.sin(theta)
y = r*np.cos(theta)
ax.plot(x,y,z,label='parametric curve')

ax.legend()
plt.show()

#三维曲面
x,y = np.mgrid[-4:4:80j, -4:4:40j]
z = 50*np.sin(x**2+y**2)
ax = plt.subplot(projection='3d')
ax.plot_surface(x,y,z,rstride=2,cstride=1,color='red')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

#测试动态画图

warnings.filterwarnings("ignore"
                        ,".*GUI is implemented")

x = np.arange(0,10)
y = np.random.randint(10,30,10)
for i in range(20):
    plt.cla()
    plt.barh(x,y)
    plt.title(str(i))
    plt.yticks(x,list(map(lambda i:'%d月'%i,x))
               ,fontproperties='simhei')
    plt.pause(1)
    y = y + np.random.randint(0,5,10)

plt.show()


#动态画图
fig, ax = plt.subplots()
fig.set_tight_layout(True)
#print('fig size: {0} DPI, size in inches {1}'.\
#    format(fig.get_dpi(),fig.set_size_inches()))
x = np.arange(0,20,0.1)
ax.scatter(x,x+np.random.normal(0,3.0,len(x)))
line, = ax.plot(x,x-5,'r-',linewidth = 2)

def update(i):
    label = 'timestep {0}'.format(i)
    print(label)
    line.set_ydata(x-5+i)
    ax.set_xlabel(label)
    return line,ax

anim = FuncAnimation(fig,update,
                     frames=np.arange(0,10),interval = 200)
if len(sys.argv) > 1 and sys.argv[1] == 'save':
    anim.save('line.gif',dpi = 80,
              writer='imagemagick')
else:
    plt.show()