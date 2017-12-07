# Data Visualisation
# University of Zurich
# Exercise 4
# Nik Zaugg
# 12-716-734
# Task 2

'''
Create a line plot, where the vertical axis will show the temperature (TCf) and the horizontal
axis will show all the available altitude levels (height) for the location (200, 250) on the map.
The data you will use will be from the 1st simulated hour of the hurricane dataset.
'''

def task2_temp_line():
    '''
    Plot temparature line plot for Hour 1 of the Hurricane
    '''

    #Imports
    import numpy as np
    import matplotlib.pyplot as plt
    import data_controller as dc

    # The position in the hurricane from which we want to plot the data
    LOGITUDE = 200
    LATITUDE = 250

    # 0.0.35 km to 19.835 km spaced with delta = 0.2 km
    MIN_HEIGHT = 0.035
    MAX_HEIGHT = 19.835
    DELTA = 0.2

    #Load Temparature Data Set for Hour 1
    data = dc.read_data('TC', 1)

    # Gives back 100 values of temperatures at the 100 predefined height levels (y-values)
    temps = data[LOGITUDE-1][LATITUDE-1]

    # x values should represent the altitude levels
    altitude = np.arange(MIN_HEIGHT, MAX_HEIGHT + DELTA, DELTA)

    # Set up the plot
    plt.plot(altitude, temps, color = 'blue')
    plt.title('Temperature data at altitude levels in hour 1')
    plt.xlabel('Altitude levels [km]')
    plt.ylabel('Temperature [$^\circ$C]')

    plt.show()

def temp_line_data():
    '''
    Return temparature line plot data for Hour 1 of the Hurricane
    '''
    #Imports
    import numpy as np
    import matplotlib.pyplot as plt
    import data_controller as dc

    # The position in the hurricane from which we want to plot the data
    LOGITUDE = 200
    LATITUDE = 250

    # 0.0.35 km to 19.835 km spaced with delta = 0.2 km
    MIN_HEIGHT = 0.035
    MAX_HEIGHT = 19.835
    DELTA = 0.2

    #Load Temparature Data Set for Hour 1
    data = dc.read_data('TC', 1)

    # Gives back 100 values of temperatures at the 100 predefined height levels (y-values)
    temps = data[LOGITUDE-1][LATITUDE-1]

    # x values should represent the altitude levels
    altitude = np.arange(MIN_HEIGHT, MAX_HEIGHT + DELTA, DELTA)

    return temps, altitude