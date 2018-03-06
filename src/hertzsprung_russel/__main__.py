from tqdm import tqdm
import matplotlib.pyplot as plt
import csv
import math
import time
ax = plt.gca()
#ax.set_facecolor('black')
stars_abs_mag = []
stars_color_index = []

#White Dwarfs, Main sequence, Red Giants, Super Giants
stars_types = [0.0, 0.0, 0.0, 0.0]

def save_figure(cname, cdpi):
    plt.savefig('{}.png'.format(cname), dpi = cdpi, format = 'png')
    plt.savefig('{}.svg'.format(cname), dpi = cdpi, format = 'svg')

print("Extracting stars' data from the database...")

with open('../HYG-Database/hygdata_v3.csv', 'r') as file:
    cord = csv.reader(file)
    counter = 0
    added_values = 0
    for row in tqdm(cord):
        if not counter == 0 and counter % 25 == 0 or counter == 1:
            # We are skipping first row, as it is text title, not needed
            if not row[16] == '': #If its empty, skip it
                stars_abs_mag.append(float(row[14]))
                stars_color_index.append(float(row[16]))
                
                if stars_abs_mag[added_values] < -5.0:
                    stars_types[3] += 1
                elif stars_abs_mag[added_values] > 10.0 and stars_color_index[added_values] < 1.0:
                    stars_types[0] += 1
                elif stars_abs_mag[added_values] < 5.0 and stars_abs_mag[added_values] > -5.0 and stars_color_index[added_values] > 0.75:
                    stars_types[2] += 1
                    
                added_values+=1
        counter += 1
file.close()

plt.scatter(stars_color_index, stars_abs_mag, s = 0.37)

plt.annotate('Sun', xy = (stars_color_index[0], stars_abs_mag[0]))

print ("\nOur sun: \n\
\tAbsolute magnitude : {}\n\
\tColor index : {}\n".format(stars_abs_mag[0], stars_color_index[0]))

stars_types[1] = added_values-stars_types[0]-stars_types[2]-stars_types[3]

print("Statistics :\n\
\t Parsed stars : {} ({}%)\n\
\t Main Sequence: {} ({}%)\n\
\t Read Giants  : {} ({}%)\n\
\t White Dwarfs : {} ({}%)\n\
\t Super Giants : {} ({}%)\n".format(added_values,
                                    round(added_values/added_values*100, 2),
                                    stars_types[1],
                                    round(stars_types[1]/added_values*100, 2),
                                    stars_types[2],
                                    round(stars_types[2]/added_values*100, 2),
                                    stars_types[0],
                                    round(stars_types[0]/added_values*100, 2),
                                    stars_types[3],
                                    round(stars_types[3]/added_values*100, 2)
      ))

plt.ylim([15, -10])
plt.xlim([-0.5, 2])

plt.xlabel('Color index')
plt.ylabel('Absolute magnitude')

plt.title('Hertzprung-Russel diagram')
print('Saving the diagrams...')
#save_figure('pics/HRD', 2500)
print('Done!')


plt.show()
