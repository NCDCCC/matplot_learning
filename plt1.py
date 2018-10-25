import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,100)
y1 = 2*x
y2 = x**2

plt.figure(figsize=(8,5))
#set ticks
plt.xlim((-1,2))
plt.ylim((1,3))
plt.xlabel('x')
plt.ylabel('y')
new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],
	[r'$blue$',r'$pink$',r'$medium$',r'$medium well$',r'$well done$'])
#gca = 'get current axis'
ax = plt.gca()
#hide top & right spines
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#place ticks
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
#place axises
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
########
l1, =plt.plot(x,y1,label='y=x')
l2, =plt.plot(x,y2,color='red',linestyle='--',label='y=x^2')
plt.legend(handles=[l1,l2],loc='best')
########
plt.show()