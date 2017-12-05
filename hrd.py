import matplotlib.pyplot as plt
import csv
import math

lum = []
ci = []

with open('HYG-Database/hygdata_v3.csv', 'r') as file:
    cord = csv.reader(file)
    i = 0
    for row in cord:
        if not i==0 and i % 50 == 0:
            if not row[16] == '': #If its empty, skip it
                lum.append(float(row[14]))
                ci.append(float(row[16]))
        i+=1
file.close()
plt.scatter(ci, lum, s=0.5)
plt.annotate('Sun', xy=(ci[0], lum[0]))
print(lum[0])
print(ci[0])
plt.ylim([15, -10])
plt.xlim([-0.5, 2])
plt.show()
