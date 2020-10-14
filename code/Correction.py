# import kwargs as
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("correction.csv")
x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
x_pos=[i for i,_ in enumerate(x)]
y = [86.632, 85.534, 84.510, 86.613, 85.434, 72.89, 87.911, 83.243, 83.323, 82.167]
z = [0.0022, 0.0077, 0.05812, 0.0016, 0.0134, 0.4988, 0.0076, 0.0002, 0.0018, 0.0257]

fig, ax = plt.subplots()

reacts1 = ax.bar(x[0], z[0],width=4)
reacts2 = ax.bar(x[1], z[1],width=4)
reacts3 = ax.bar(x[2], z[2],width=4)
reacts4 = ax.bar(x[3], z[3],width=4)
reacts5 = ax.bar(x[4], z[4],width=4)
reacts6 = ax.bar(x[5], z[5],width=4)
reacts7 = ax.bar(x[6], z[6],width=4)
reacts8 = ax.bar(x[7], z[7],width=4)
reacts9 = ax.bar(x[8], z[8],width=4)
reacts10 = ax.bar(x[9],z[9],width=4)

csfont = {'fontname': 'Times New Roman'}

plt.xlabel("Time-steps", **csfont)

plt.ylabel("FAR", **csfont)
plt.title("FAR per Time-steps")
plt.xticks(np.arange(10,110,10))
plt.yticks(np.arange(0,0.7,.1))
plt.minorticks_on()
plt.grid(True, which='major')
plt.grid(False, which='minor')


def autolabel(reacts):
    for rect in reacts:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.0 * height,
                '%.2f' % float(height),
                ha='center', va='bottom')


autolabel(reacts1)
autolabel(reacts2)
autolabel(reacts3)
autolabel(reacts4)
autolabel(reacts5)

autolabel(reacts6)
autolabel(reacts7)
autolabel(reacts8)
autolabel(reacts9)
autolabel(reacts10)

#plt.legend()
plt.show()
