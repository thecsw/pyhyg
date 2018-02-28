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
names = []
code = []
with open('HYG-Database/hygdata_v3.csv', 'r') as file:
    cord = csv.reader(file)
    counter = 0
    added_values = 0
    for row in tqdm(cord):
        if not counter == 0 and counter % 1 == 0 or counter == 1:
            # We are skipping first row, as it is text title, not needed
            if not row[16] == '' and not row[4] == '' and (row[4] == "Gl 551" or row[4] == "Gl 623" or row[4] == "Gl 482A" or row[4] == "Gl 231" or row[4]=="Gl 286" or row[4] == "Gl 841A" or row[4] == "Gl 35" or row[4] == "Gl 440"): #If its empty, skip it
                stars_abs_mag.append(float(row[14])) 
                stars_color_index.append(float(row[16]))
                names.append(row[6])
                code.append(row[4])
                print("ID -> {} Abs. Mag -> {} Luminosity/solar -> {}".format(row[4], row[14], row[33]))
                #print(row[4])
                #print(row[13])
                #print(row[9])
        counter += 1
file.close()

plt.scatter(stars_color_index, stars_abs_mag, s = 10)

for i in range(8):
    if not names[i] == '':
        plt.annotate(names[i], xy = (stars_color_index[i], stars_abs_mag[i]))
    else:
        plt.annotate(code[i], xy = (stars_color_index[i], stars_abs_mag[i]))

plt.ylim([16, -10])
plt.xlim([-0.5, 2])

plt.xlabel('Color index')
plt.ylabel('Absolute magnitude')

plt.title('Hertzprung-Russel diagram')
print('Saving the diagrams...')
#save_figure('pics/HRD', 2500)
print('Done!')


plt.show()
