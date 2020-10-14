import pandas as pd
import matplotlib.pyplot as plt

x=['IG','CFSSE','GR','SU','CsT']
x_pos=[i for i,_ in enumerate(x)]
y=[74.899,68.229,76.750,75.853,74.931]
fig,ax=plt.subplots()

reacts1=ax.bar(x[0],y[0],width=0.8)
rects2=ax.bar(x[1],y[1],width=0.8)
rects3=ax.bar(x[2],y[2],width=0.8)
rects4=ax.bar(x[3],y[3],width=0.8)
rects5=ax.bar(x[4],y[4],width=0.8)

csfont={'fontname':'Times New Roman'}
plt.xlabel("Feature_Selection_Method",**csfont)
plt.ylabel("Accuracy",**csfont)
plt.title('Comparing with Classifier Techniques',**csfont)
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


plt.show()


#df=pd.read_csv("Mean.csv")
#x=df.Classifier_Techniques
#y=df.Accuracy
#plt.bar(x,y,label='Comparing with Classifier Techniques')
#plt.legend()
#plt.grid()
#plt.show()
