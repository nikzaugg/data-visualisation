# Data Visualisation
# University of Zurich
# Exercise 4
# Nik Zaugg
# 12-716-734
# Task 3

'''
Although the above plot is quite informative, it provides information only for the first hour at the
given location. Sometimes it is also useful to compare line plots for the same interval, such as
from hour-to-hour, day-to-day, etc. Since the hurricane event spans 48 hours, you will collect
the required hurricane temperature (TCf) data (from the different files) and you will create a line
plot for each hour. For direct comparison, you will place one line plot on top of the other, creating
a stacked line plot with common X axis. For simplicity, use data only from the first 5 hours,
while the location will be again the same as in Task 2.
'''
#Imports
import numpy as np
import matplotlib.pyplot as plt
import data_controller as dc

# The position in the hurricane from which we want to plot the data
LONGITUDE = 200
LATITUDE = 250

# 0.0.35 km to 19.835 km spaced with delta = 0.2 km
MIN_HEIGHT = 0.035
MAX_HEIGHT = 19.835
DELTA = 0.2

datasets = []

# Load Temperature data for hours 1 to 5
for i in range(1, 6):
    datasets.append(dc.read_data('TC',i))

# Temperature data per hour at position (200, 250)
temperatures_per_hour = list()
for i in range(0, 5):
    temperatures_per_hour.append(datasets[i][LONGITUDE - 1][LATITUDE - 1])

# x values should represent the altitude levels
altitude = np.arange(MIN_HEIGHT, MAX_HEIGHT + DELTA, DELTA)


figure, plot = plt.subplots()


figure.canvas.set_window_title("Task 3")


plot.set_title("Temperatures at different altitude levels. (200, 250)")
plot.set_xlabel("Altitude Level [km]")
plot.set_ylabel("Temperature [$^\circ$C]")
plot.minorticks_on()


plot.plot(altitude, temperatures_per_hour[0], label='Hour 1')
plot.plot(altitude, temperatures_per_hour[1], label='Hour 2')
plot.plot(altitude, temperatures_per_hour[2], label='Hour 3')
plot.plot(altitude, temperatures_per_hour[3], label='Hour 4')
plot.plot(altitude, temperatures_per_hour[4], label='Hour 5')
plot.legend()


plt.show()