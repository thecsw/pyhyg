from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import csv

fig = plt.figure()

ax1 = fig.add_subplot(111, projection='3d')

x=[]
y=[]
z=[]

with open('HYG-Database/hygdata_v3.csv', 'r') as file:
    cord = csv.reader(file)
    i=0
    for row in cord:
        if not i==0 and i%1000==0:
            x.append(float(row[17]))
            y.append(float(row[18]))
            z.append(float(row[19]))
        i+=1
file.close()
print(len(x), len(y), len(z))
ax1.text(x[0], y[0], z[0], 'Sun')
ax1.scatter(x, y, z)
plt.show()
