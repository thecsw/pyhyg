from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import csv

fig = plt.figure()

ax1 = fig.add_subplot(111, projection='3d')

x=[]
y=[]
z=[]

with open('stars/x', 'r') as file:
    cord = csv.reader(file)
    for row in cord:
        x.append(float(row[0]))
file.close()
with open('stars/y', 'r') as file:
    cord = csv.reader(file)
    for row in cord:
        y.append(float(row[0]))
file.close()
with open('stars/z', 'r') as file:
    cord = csv.reader(file)
    for row in cord:
        z.append(float(row[0]))
file.close()
print(len(x), len(y), len(z))
ax1.text(x[0], y[0], z[0], 'Sun')
ax1.scatter(x, y, z)
plt.show()
