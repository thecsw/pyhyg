import matplotlib.pyplot as plt
import csv
import math

stars_abs_mag = []
stars_color_index = []
with open('HYG-Database/hygdata_v3.csv', 'r') as file:
    cord = csv.reader(file)
    counter = 0
    stars = 0
    for row in cord:
        if not counter == 0 and counter % 25 == 0 or counter == 1:
            # We are skipping first row, as it is text title, not needed
            if not row[16] == '': #If its empty, skip it
                stars_abs_mag.append(float(row[14]))
                stars_color_index.append(float(row[16]))
                stars += 1
                print ('Progress: {}%'.format(counter*100/119575))
        counter += 1
file.close()

plt.scatter(stars_color_index, stars_abs_mag, s = 0.5)
plt.annotate('Sun', xy = (stars_color_index[0], stars_abs_mag[0]))

print ("Our sun: Absolute magnitude : {}\n\
Color index : {}".format(stars_abs_mag[0], stars_color_index[0]))
plt.ylim([15, -10])
plt.xlim([-0.5, 2])
plt.xlabel('Color index')
plt.ylabel('Absolute magnitude')
plt.title('Hertzprung-Russel diagram')
plt.show()
