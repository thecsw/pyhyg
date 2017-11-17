from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x=[]
y=[]
z=[]

with open("x") as file:
    for i in range(0, 100):
        str = file.readline()
        x.append(float(str))
file.close()
with open("y") as file:
    for i in range(0, 100):
        str = file.readline()
        y.append(float(str))
file.close()
with open("z") as file:
    for i in range(0, 100):
        str = file.readline()
        z.append(float(str))
file.close()
ax1.scatter(x, y, z)
plt.show()
