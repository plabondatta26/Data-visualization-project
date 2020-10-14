import pandas as pd
import matplotlib.pyplot as plt

#z=['CFS_Subset_Eveluator','Chi-Square_Test','Gain_Ratio','Info_Gain','Symmetric_Uncertainty']

cfs=pd.read_csv("CFS_Subset_Eveluator.csv")
cfsx=cfs.Classifier_Techniques
cfsy=cfs.Accuracy

chi=pd.read_csv("Chi-Square_Test.csv")
chiy=chi.Accuracy

gain=pd.read_csv("Gain_Ratio.csv")
gainy=gain.Accuracy

info=pd.read_csv("Info_Gain.csv")
infoy=info.Accuracy

Symmatric=pd.read_csv("Symmetric_Uncertainty.csv")
Symmatricy=Symmatric.Accuracy

plt.plot(cfsx,cfsy,label='CFS Subset Eveluator',linewidth=4,marker='o',linestyle='-')
plt.plot(cfsx,chiy,label='Chi-Square Test',linewidth=4,marker='o')
plt.plot(cfsx,gainy,label='Gain Ratio',linewidth=4,marker='o')
plt.plot(cfsx,infoy,label='Info Gain',linewidth=4,marker='o')
plt.plot(cfsx,Symmatricy,label='Symmetric Uncertainty',linewidth=4,marker='o')
plt.legend()
plt.grid()
plt.xlabel("Classifier_Techniques")
plt.ylabel("Accuracy")
plt.show()
#print(Symmatric)
