import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#df=pd.read_csv("Chi-Square_Test.csv")



csfont={'fontname':'Times New Roman'}

x=['J48','RF','PART','NB','DT','RBFN','BN']
x_pos=[i for i,_ in enumerate(x)]
y=[78.051,80.132,77.989,72.618,72.595,70.723,72.409]
fig,ax=plt.subplots()

reacts1=ax.bar(x[0],y[0])
rects2=ax.bar(x[1],y[1])
rects3=ax.bar(x[2],y[2])
rects4=ax.bar(x[3],y[3])
rects5=ax.bar(x[4],y[4])
rects6=ax.bar(x[5],y[5])
rects7=ax.bar(x[6],y[6])


plt.xlabel("Classifier Techniques",**csfont)
plt.ylabel("Accuracy",**csfont)
plt.title('Chi-square Test',**csfont)
plt.xticks(x_pos,x,**csfont)
plt.minorticks_on()
plt.grid(False,which='major')
plt.grid(False,which='minor')

#reacts=rects1,rects2,rects3,rects4,rects5,rects6

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


#x=df.Classifier_Techniques
#y=df.Accuracy
#plt.bar(x,y,label='Chi-Square Test')
#plt.xlabel("Classifier Techniques")
#plt.ylabel("Accuracy")
#plt.legend()


plt.grid()
plt.show()
