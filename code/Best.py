import pandas as pd
import matplotlib.pyplot as plt
x=['IG','CFSSE','GR','SU','CsT']
x_pos=[i for i,_ in enumerate(x)]
y=[79.36,79.249,81.946,80.708,80.132]
fig,ax=plt.subplots()

reacts1=ax.bar(x[0],y[0],color='darkorange',label='Random Forest')
rects2=ax.bar(x[1],y[1],color='g',label='PART')
rects3=ax.bar(x[2],y[2],color='darkorange')
rects4=ax.bar(x[3],y[3],color='darkorange')
rects5=ax.bar(x[4],y[4],color='darkorange')


csfont={'fontname':'Times New Roman'}
plt.xlabel("Feature Selection Method",**csfont)
plt.ylabel("Accuracy",**csfont)
plt.title('Best Value',**csfont)
plt.xticks(x_pos,x)
plt.minorticks_on()
plt.grid(True,which='major')
plt.grid(False,which='minor')


def autolabel(reacts):
    for rect in reacts:
        height=rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.,1.0*height,
        '%.3f'%float(height),
        ha='center',va='bottom')

autolabel(reacts1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
autolabel(rects4)
autolabel(rects5)

plt.legend(loc='lower right')
plt.show()