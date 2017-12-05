# Data Visualisation
# University of Zurich
# Exercise 4
# Nik Zaugg
# 12-716-734
# Task 5

'''
Additionally, for 4 locations of your choice, select at least three scalar variables (e.g.
temperature, pressure, precipitation) and present them below the map as scatterplot-matrices.
You can chose the data values from the first hour of the hurricane simulation and using an elevation
of 1km altitude.
'''
import data_controller as dc
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np


temp = dc.read_data('TC', 1)
pressure = dc.read_data('P', 1)
precipitation = dc.read_data('PRECIP', 1)

# FOR 1KM
ALTITUDE = 5

locations = [(0,0),(150,150),(300,300),(450,450)]

locs = list()

for i in range(0,50, 1):
    for j in range(0,50, 1):
        locs.append((i,j))

temp_altitude = temp[:,:,5]
pressure_altitude = pressure[:,:,5]
precipitation_altitude = precipitation[:,:,5]

all_data = list()
for location in locations:
    location_data = list()
    for dataset in [temp_altitude, pressure_altitude, precipitation_altitude]:
        location_data.append(dataset[location[0]][location[1]])
    all_data.append(location_data)



columns=['Temperature [C°]', 'Pressure [Pa]', 'Precipitation']

data_frame = pd.DataFrame(all_data, columns=columns)

scatter_matrix(data_frame, figsize=(20, 20), diagonal='hist')

plt.show()