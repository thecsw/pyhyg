from tqdm import tqdm
import matplotlib.pyplot as plt
import csv
import math
import time
import statistics
ax = plt.gca()
#ax.set_facecolor('black')
stars_abs_mag = []
stars_color_index = []

bc = {'O':-4.0,                     # O
      'B':-2.15,                    # B
      'A':-0.26,                    # A
      'F':-0.03,                    # F
      'G':-0.04,                    # G
      'K':-0.4,                     # K
      'M':-1.75                     # M
}

chzl = [[],[],[],[]]

#White Dwarfs, Main sequence, Red Giants, Super Giants
stars_types = [0.0, 0.0, 0.0, 0.0]

def chz(distance, apparent, bc):
    mv = apparent - 5 * (math.log(distance, 10) - 1)
    mbol = bc + mv
    lum = math.pow(10, 0.4 * (4.74 - mbol))
    ro = math.sqrt(lum / 0.53)
    ri = math.sqrt(lum / 1.1)
    return ri, ro
    
print("Extracting stars' data from the database...")

with open('../HYG-Database/hygdata_v3.csv', 'r') as file:
    cord = csv.reader(file)
    counter = 0
    added_values = 0
    for row in tqdm(cord):
        if not counter == 0 and counter % 1 == 0 or counter == 1:
            # We are skipping first row, as it is text title, not needed
            if not row[16] == '' and not row[15] == '': #If its empty, skip it
                stars_abs_mag.append(float(row[14]))
                stars_color_index.append(float(row[16]))
                try:
                    bcc = bc[row[15][0]] # the bolometric correction
                except:
                    bcc = 0
                try:
                    if stars_abs_mag[-1] < -5.0: # Super Giants
                        chzl[3].append(chz(float(row[9]), float(row[13]), bcc))
                        stars_types[3] += 1
                    elif stars_abs_mag[-1] > 10.0 and stars_color_index[added_values] < 1.0: # White Dwarf
                        chzl[0].append(chz(float(row[9]), float(row[13]), bcc))
                        stars_types[0] += 1
                    elif stars_abs_mag[-1] < 5.0 and stars_abs_mag[added_values] > -5.0 and stars_color_index[added_values] > 0.75: # Red giant
                        chzl[2].append(chz(float(row[9]), float(row[13]), bcc))
                        stars_types[2] += 1
                    else:
                        chzl[1].append(chz(float(row[9]), float(row[13]), bcc))
                        stars_types[1] += 1
                except:
                    print("oops")
                added_values+=1
        counter += 1

file.close()

print ("\nOur sun: \n\n\
\tAbsolute magnitude : {}\n\
\tColor index : {}\n".format(stars_abs_mag[0], stars_color_index[0]))

print("Statistics :\n\n\
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

lens = [[],[],[],[]]
ris =  [[],[],[],[]]
ros =  [[],[],[],[]]

for i in range(4):
    for j in range(int(stars_types[i])):
        lens[i].append(chzl[i][j][1]-chzl[i][j][0])
        ris[i].append(chzl[i][j][0])
        ros[i].append(chzl[i][j][1])

round_number = 8
        
print("Statistics Version 2.0\n\n\
\t Average lengths of CHZ (AU):\n\
\t\t White Dwarfs : {} ± {} ({}%)\n\
\t\t Main Sequence: {} ± {} ({}%) \n\
\t\t Red Dwarfs   : {} ± {} ({}%)\n\
\t\t Supergiants  : {} ± {} ({}%)\n\
\n\
\t Average inner and outer CHZ lengths (AU):\n\n\
\t\t White Dwarfs  : ri = {} ± {} ({}%)\n\
\t\t                 ro = {} ± {} ({}%)\n\
\t\t Main Sequence : ri = {} ± {} ({}%)\n\
\t\t                 ro = {} ± {} ({}%)\n\
\t\t Red Dwarfs    : ri = {} ± {} ({}%)\n\
\t\t                 ro = {} ± {} ({}%)\n\
\t\t Supergiants   : ri = {} ± {} ({}%)\n\
\t\t                 ro = {} ± {} ({}%)\n".format(round(statistics.mean(lens[0]), round_number), round(statistics.stdev(lens[0]), round_number),
                                    round(round(statistics.stdev(lens[0]), round_number) * 100 / round(statistics.mean(lens[0]), round_number), 2),
                                                  
                                                 round(statistics.mean(lens[1]), round_number), round(statistics.stdev(lens[1]), round_number),
                                    round(round(statistics.stdev(lens[1]), round_number) * 100 / round(statistics.mean(lens[1]), round_number), 2),
                                    
                                                 round(statistics.mean(lens[2]), round_number), round(statistics.stdev(lens[2]), round_number),
                                    round(round(statistics.stdev(lens[2]), round_number) * 100 / round(statistics.mean(lens[2]), round_number), 2),
                                    
                                                 round(statistics.mean(lens[3]), round_number), round(statistics.stdev(lens[3]), round_number),
                                    round(round(statistics.stdev(lens[3]), round_number) * 100 / round(statistics.mean(lens[3]), round_number), 2),


                                                  
                                                 round(statistics.mean(ris[0]), round_number), round(statistics.stdev(ris[0]), round_number),
                                    round(round(statistics.stdev(ris[0]), round_number) * 100 / round(statistics.mean(ris[0]), round_number), 2),

                                                 round(statistics.mean(ros[0]), round_number), round(statistics.stdev(ros[0]), round_number),
                                    round(round(statistics.stdev(ros[0]), round_number) * 100 / round(statistics.mean(ros[0]), round_number), 2),

                                                 round(statistics.mean(ris[1]), round_number), round(statistics.stdev(ris[1]), round_number),
                                    round(round(statistics.stdev(ris[1]), round_number) * 100 / round(statistics.mean(ris[1]), round_number), 2),
                                                 
                                                 round(statistics.mean(ros[1]), round_number), round(statistics.stdev(ros[1]), round_number),
                                    round(round(statistics.stdev(ros[1]), round_number) * 100 / round(statistics.mean(ros[1]), round_number), 2),
                                                 
                                                 round(statistics.mean(ris[2]), round_number), round(statistics.stdev(ris[2]), round_number),
                                    round(round(statistics.stdev(ris[2]), round_number) * 100 / round(statistics.mean(ris[2]), round_number), 2),
                                                 
                                                 round(statistics.mean(ros[2]), round_number), round(statistics.stdev(ros[2]), round_number),
                                    round(round(statistics.stdev(ros[2]), round_number) * 100 / round(statistics.mean(ros[2]), round_number), 2),
                                                 
                                                 round(statistics.mean(ris[3]), round_number), round(statistics.stdev(ris[3]), round_number),
                                    round(round(statistics.stdev(ris[3]), round_number) * 100 / round(statistics.mean(ris[3]), round_number), 2),
                                                 
                                                 round(statistics.mean(ros[3]), round_number), round(statistics.stdev(ros[3]), round_number),
                                    round(round(statistics.stdev(ros[3]), round_number) * 100 / round(statistics.mean(ros[3]), round_number), 2),
))

print("Please note that the absolute error is big due to a very large amount of data and this data is very spread out.\n\
Some values are very small and some values are very big, which makes the data not accurate.\n\
Thank you.\n")
