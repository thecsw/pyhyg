import math

app_mag = [11.010,
           10.270,
           2.740,
           5.080,
           1.160,
           10.360,
           12.370,
           11.500]
dist = [1.2959,
        8.0567,
        11.6850,
        10.1978,
        10.3584,
        15.9719,
        4.2626,
        4.6081]
glisid = [551,
          623,
          "482A",
          231,
          286,
          841,
          35,
          440]
bc = [-2.3,
      -1.86,
      -0.06,
      -0.07,
      -0.2,
      -1.2,
      0,
      0]

mbolsun = 4.74
print("Glis ID & Luminosity")
for i in range(len(app_mag)):
    avm = app_mag[i] - 5 * (math.log(dist[i], 10) - 1)
    mbol = bc[i] + avm
    lum = math.pow(10, 0.4 * (4.74 - mbol))
    print("{} & {} & {} \\\\".format(glisid[i], lum, round(lum, 8)))
 
