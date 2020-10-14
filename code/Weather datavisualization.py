# importing libreries

#import inline
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#importing csv file

dataset = pd.read_csv('Weather.csv')
ds=dataset[:10]
#d=dataset[:50]
#print(d)
# printing dataset

#print(dataset)
#print(dataset.columns)


# getting the maximum tempareture of max_temp row

#print(n)
#n=dataset[dataset['Max_Temp']>=44]
#print(n, "The Highest temperature from 1949 to 2013 is")


# getting the lowest maximum temperature of max_temp row

#n=dataset[dataset['Max_Temp']<=23]
#print(n)
#print("The lowest maximum temperature  from 1949 to 2013 is ",n["Max_Temp"] )

# getting bright Sunshine

#n=dataset[dataset['Bright_Sunshine']>10]
#max_n=np.max(dataset.Bright_Sunshine)
#min_n=np.min(dataset[dataset['Bright_Sunshine']<1])
#print(min_n)
#print(n)

# getting Latitude and longitude of a station

#n=dataset[dataset['Station Names']=='Rajshahi']
#print(n)


#getting  specific  temperature


#n=dataset[['Bright_Sunshine'[dataset['Station Names']=='Barisal']>9]]
#print(n)
                            #ploting

#ploting with a single column
#x=dataset.Max_Temp
#y=range(0,len(x))
#plt.plot(x,y,'.',color='b')
#plt.show()

#ploting with multiple column

#x=dataset.Max_Temp
#y=range(0,len(x))
#z=dataset.Cold_Coverage
#w=dataset.Min_Temp
#plt.plot(y,x,'.',color='red')
#plt.plot(y,w,'.',color='green')
#plt.plot(y,z,'.',color='black')
#plt.show()

                                #Bar chart

#Creating a bar chart using multiple column
#b=dataset.Wind_Speed[0,15000]
#c=b.sliceable

#a=dataset.Relative_Humidity[range(0,c)]
#print(b)
#w=a.range(0,15000)

x=ds.Wind_Speed
y=range(len(x))
w=ds.Relative_Humidity
z=ds.Cold_Coverage
#print(z)
plt.bar([a-0.25 for a in y],w,color='r',width=0.25,label='Relative Humidity')
plt.bar([a-0.50 for a in y],x,color='g',width=0.25,label='Wind Speed')
plt.bar([a-0.75 for a in y],z,color='b',width=0.25,label='Cold Coverage')
plt.xlabel("Weather")
plt.ylabel("Days")
plt.legend()
plt.show()


                                                # Pie chart

#w=np.mean(dataset.Relative_Humidity)
#x=np.mean(dataset.Wind_Speed)
#y=np.mean(dataset.Cold_Coverage)
#z=np.mean(dataset.Rainfall)
#labels=['Relative Humidity','Wind Speed','Cold Coverage','Rainfall']
#r=[w,x,y,z]
#explode=[0,0,0.1,0]
#plt.pie(r,labels=labels,explode=explode,autopct='%1.1f%%',wedgeprops={'width':1},shadow=True,)
#plt.show()

