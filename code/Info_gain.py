import pandas as pd
import matplotlib.pyplot as plt
x=['J48','RF','PART','NB','DT','RBFN','BN']
x_pos=[i for i,_ in enumerate(x)]
y=[78.006,79.36,77.102,72.068,72.595,71.965,73.203]
fig,ax=plt.subplots()

reacts1=ax.bar(x[0],y[0])
rects2=ax.bar(x[1],y[1])
rects3=ax.bar(x[2],y[2])
rects4=ax.bar(x[3],y[3])
rects5=ax.bar(x[4],y[4])
rects6=ax.bar(x[5],y[5])
rects7=ax.bar(x[6],y[6])


csfont={'fontname':'Times New Roman'}
plt.xlabel("Classifier Techniques",**csfont)
plt.ylabel("Accuracy",**csfont)
plt.title('Info Gain',**csfont)
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
autolabel(rects6)
autolabel(rects7)

plt.show()
#df=pd.read_csv("Info_Gain.csv")
#x=df.Classifier_Techniques
#y=df.Accuracy
#plt.bar(x,y,label='Info Gain')
#plt.legend()
#plt.grid()
#plt.show()