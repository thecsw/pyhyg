import matplotlib.pyplot as plt
import csv

lum = []
ci = []

with open('HYG-Database/hygdata_v3.csv', 'r') as file:
    cord = csv.reader(file)
    i = 0
    for row in cord:
        if i==1:
            print(row[33])
        if not i==0 and float(row[33])<10000 and float(row[33])>0.0001:
            if not row[16] == '':
                lum.append(float(row[33]))
                ci.append(float(row[16]))
        i+=1
file.close()

plt.scatter(ci, lum, s=1)
plt.annotate('Sun', xy=(ci[0], lum[0]))
print(lum[0])
print(ci[0])
plt.show()
