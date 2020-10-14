import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df= pd.read_csv("H:\DS & ML\Code\Work\Book1.csv",encoding='latin1')
#print(df)
p=df[(df["Classifier_Techniques"] == "Random_Forest") & (df["Accuracy"] == 79.36)]
#print(p)
#x=p.columns[0:]
#y=p.iloc[0]
#plt.bar(x,y)
#plt.grid()
#plt.show()

x=p.Classifier_Techniques
#y=p.Accuracy

#print(p.columns)
a=p.Accuracy
b=p.TP_Rate
c=p.FP_Rate
d=p.Precision
e=p.Recall
f=p.FAR
g=p.F_Measure
h=p.MCC
i=p.MAE


#x=['Accuracy','TP_Rate','FP_Rate','Precision','Recall','FAR','F_Measure','MCC','MAE']
#r=[a,b,c,d,e,f,g,h,i]
plt.bar(x,a)
plt.bar(x,b)
plt.bar(b,c)
plt.show()


#explode=[0,0,0,0,0,0,0,0,0]
#plt.pie(r,labels=labels,explode=explode,autopct='%1.1f%%',shadow=True)
#plt.scatter(e,f)
#plt.show()
#print(a)



#df=pd.read_csv("sort.csv")
#labels=df.columns
#y=df.iloc[0]
#explode=[0,.8,.8,.8,.8,.8,.8,.8,.8]
#plt.pie(y,labels=labels,explode=explode,autopct='%1.1f%%',startangle=140)
#plt.legend(df.iloc[0],loc='lower left')
#plt.show()
