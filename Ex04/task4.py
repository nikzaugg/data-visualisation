# Data Visualisation
# University of Zurich
# Exercise 4
# Nik Zaugg
# 12-716-734
# Task 4

'''
Create a color contour plot for the temperature (TCf). For those who have implemented Task 1,
the contour plot should be on top of the terrain map. Include proper legends, colormaps, titles,
etc. for presenting the data. You will use data that cover the whole provided area of hurricane,
using for elevation a fixed value of 1 km. Again, if you have to select a specific time step, you
will use data from the 1st hour.
'''

import data_controller as dc
import matplotlib.pyplot as plt
import numpy as np

# Load contour map
data = dc.get_terrain_data()
print(data)

# Load temperature data for hour 1
# Contains temperature values for the whole hurricane
temp_data_hour_1 = dc.read_data('TC', 1)

fig, plot = plt.subplots()

fig.canvas.set_window_title('TASK 4') 

plot.set_title('Temperatures at altitude of 1km')

plot.set_xlabel('Longitude (X)')
plot.set_ylabel('Latitude (Y)')
plot.set_aspect(1)

plot.invert_yaxis()

# plot the terrain data on the plot
terrain_plot = plot.contour(data, cmap='terrain')

colorbar = plt.colorbar(terrain_plot)
colorbar.set_label('terrain elevation [m]')

# Define the altitude at which we want to plot the color contour
# Altitude begins at 0.035 km with a delta/step-size of 0.2 km
# To approximate 1km we need to consider step 5 = 0.035 + 5*0.2 = 1.035km
ALTITUDE = 5

temp_data_altitude = temp_data_hour_1[ : , : , ALTITUDE]
print(temp_data_altitude)

# plot the temperature data on the plot
temp_contour = plot.contourf(temp_data_altitude, cmap='jet', alpha=1.0)

# add a colorbar indicating the temperature levels
colorbar = plt.colorbar(temp_contour)
colorbar.set_label('Temperature')

# show the plot
plt.show()

