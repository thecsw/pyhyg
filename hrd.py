import matplotlib.pyplot as plt
import csv
import math
from progressbar import ProgressBar, Percentage, Bar, AnimatedMarker 
import thread
import time
amount = 119575
ax = plt.gca()
ax.set_facecolor('black')
stars_abs_mag = []
stars_color_index = []
work = True
pbar = ProgressBar(widgets=['Working: ', AnimatedMarker()])

def save_figure(cname, cdpi):
    plt.savefig('{}.png'.format(cname), dpi=cdpi, format = 'png')
    plt.savefig('{}.svg'.format(cname), dpi=cdpi, format = 'svg')

def working_bar():
    global pbar
    i=0
    pbar.start()
    for i in pbar((i for i in range(150))):
        time.sleep(.08)
        if work == False:
            return
    
with open('HYG-Database/hygdata_v3.csv', 'r') as file:
    cord = csv.reader(file)
    counter = 0
    stars = 0
    progress = ProgressBar(widgets=[Percentage(), Bar()], maxval = amount/25)
    progress.start()
    for row in cord:
        if not counter == 0 and counter % 25 == 0 or counter == 1:
            # We are skipping first row, as it is text title, not needed
            if not row[16] == '': #If its empty, skip it
                stars_abs_mag.append(float(row[14]))
                stars_color_index.append(float(row[16]))
                stars += 1
                progress.update(stars)
                #print ('Progress: {}%'.format(counter*100/119575))
        counter += 1
    progress.finish()
file.close()

plt.scatter(stars_color_index, stars_abs_mag, s = 0.3, c = 'w')

plt.annotate('Sun', xy = (stars_color_index[0], stars_abs_mag[0]))

print ("Our sun: Absolute magnitude : {}\n\
Color index : {}".format(stars_abs_mag[0], stars_color_index[0]))

plt.ylim([15, -10])
plt.xlim([-0.5, 2])

plt.xlabel('Color index')
plt.ylabel('Absolute magnitude')

plt.title('Hertzprung-Russel diagram')
thread.start_new_thread(working_bar, ())
save_figure('pics/HRD', 2500)
pbar.finish()
work = False
print('Done!')
plt.show()
