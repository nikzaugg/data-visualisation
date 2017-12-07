# Data Visualisation
# University of Zurich
# Exercise 4
# Nik Zaugg
# 12-716-734
# Task 5

'''
Select proper multivariate visualization techniques in order to present in a proper and informative
way the relationship between multiple data variables. Create a grid of cells 10x10 on top of
the map and display in each cell of the grid a vector-valued data attribute (e.g. wind direction
and wind speed) using a directional marker (e.g. arrow with length for orientation and amplitude).
Additionally, for 4 locations of your choice, select at least three scalar variables (e.g.
temperature, pressure, precipitation) and present them below the map as scatterplot-matrices.
You can chose the data values from the first hour of the hurricane simulation and using an elevation
of 1km altitude.
'''

import data_controller as dc
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import cm
import numpy as np


def calc_mean(data_list):
    '''
    Calculate mean of a list of values
    '''
    return sum(data_list) / len(data_list)


def task5_quiver_plot():
    '''
    Plot a quiver plot with wind speed and direction
    '''

    # WIND DATA PLOTTING

    # load raw wind components
    x_wind = dc.read_data('U', 1)
    y_wind = dc.read_data('V', 1)

    # get wind data at specified altitude (1km)
    altitude = 5

    # Wind components for x and y at 1km altitude
    x_wind_altitude = x_wind[:,:,altitude]
    y_wind_altitude = y_wind[:,:,altitude]

    # Create a grid to put onto the map
    max_coord = 500
    min_coord = 0

    # grid of cells 10 x 10
    # size of one cell is cell_size x cell_size
    cells_per_row = 10
    cell_size = max_coord//cells_per_row

    # Create arrays to hold the data for each cell and each wind component
    x_cell_wind_components = np.ndarray((cells_per_row, cells_per_row), dtype=float)
    y_cell_wind_components = np.ndarray((cells_per_row,cells_per_row), dtype=float)

    x_cell_coords = np.ndarray((cells_per_row,cells_per_row), dtype=float)
    y_cell_coords = np.ndarray((cells_per_row, cells_per_row), dtype=float)

    # Create array to hold wind-speed for each cell
    wind_speed = []

    # Calculate the aggregated wind speed inside every cell of size (50x50)
    cell_nr_x = 0
    cell_nr_y = 0

    # For every grid-cell
    for i in range(min_coord, max_coord, cell_size):
        cell_nr_x = 0
        for j in range(min_coord, max_coord, cell_size):
            x_wind_values = []
            y_wind_values = []
            # For every datapoint in the grid-cell
            for u in range(i, i+cell_size):
                for v in range(j, j+cell_size):
                    if not x_wind_altitude[u][v] > 100:
                        x_wind_values.append(x_wind_altitude[u][v])
                    if not y_wind_altitude[u][v] > 100:
                        y_wind_values.append(y_wind_altitude[u][v])
            
            # Get middle coordinates
            index_x = i//cell_size
            index_y = j//cell_size

            # get the mean x and y values for the current cell and store it
            x_cell_wind_components[index_x][index_y] = calc_mean(x_wind_values)
            y_cell_wind_components[index_x][index_y] = calc_mean(y_wind_values)

            # Calculate the wind speed
            speed = (pow(x_cell_wind_components[index_x][index_y],2) + pow(y_cell_wind_components[index_x][index_y],2))**0.5
            wind_speed.append(speed)

            # Add coordinates of each arrow
            x_cell_coords[index_x][index_y] = j + (cell_size/2)
            y_cell_coords[index_x][index_y] = i + (cell_size/2)

    # LOAD TERRAIN PLOT
    data = dc.get_terrain_data()

    fig, plot = plt.subplots()

    fig.canvas.set_window_title('TASK 5') 

    plot.set_title('UVW Quiver Plot')

    plot.set_xlabel('Longitude (X)')
    plot.set_ylabel('Latitude (Y)')
    plot.set_aspect(1)

    plot.invert_yaxis()

    # plot the terrain data on the plot
    terrain_plot = plot.contourf(data, cmap='cubehelix')

    # Set a colorbar
    colorbar = plt.colorbar(terrain_plot)
    colorbar.set_label('terrain elevation [m]')

    # choose a colormap
    color_map = cm.spring

    # Normalise color and speed
    norm_speed = matplotlib.colors.Normalize(vmin=min(wind_speed), vmax=max(wind_speed))

    norm_speed_colors = matplotlib.cm.ScalarMappable(norm=norm_speed, cmap=color_map)
    norm_speed_colors.set_array([ ])

    # add a colorbar indicating the wind's strength
    colorbar = plt.colorbar(norm_speed_colors)
    colorbar.set_label("wind speed [m/s]")

    # plot the wind direction and strength as arrows
    Q = plot.quiver(x_cell_coords, y_cell_coords,
                x_cell_wind_components, y_cell_wind_components,
                color=color_map(norm_speed(wind_speed)),
                pivot ='middle',
                units ='height')

    # display plot
    plt.show()

def quiver_plot_data():

    # WIND DATA PLOTTING

    # load raw wind components
    x_wind = dc.read_data('U', 1)
    y_wind = dc.read_data('V', 1)

    # get wind data at specified altitude (1km)
    altitude = 5

    # Wind components for x and y at 1km altitude
    x_wind_altitude = x_wind[:,:,altitude]
    y_wind_altitude = y_wind[:,:,altitude]

    # Create a grid to put onto the map
    max_coord = 500
    min_coord = 0

    # grid of cells 10 x 10
    # size of one cell is cell_size x cell_size
    cells_per_row = 10
    cell_size = max_coord//cells_per_row

    # Create arrays to hold the data for each cell and each wind component
    x_cell_wind_components = np.ndarray((cells_per_row, cells_per_row), dtype=float)
    y_cell_wind_components = np.ndarray((cells_per_row,cells_per_row), dtype=float)

    x_cell_coords = np.ndarray((cells_per_row,cells_per_row), dtype=float)
    y_cell_coords = np.ndarray((cells_per_row, cells_per_row), dtype=float)

    # Create array to hold wind-speed for each cell
    wind_speed = []

    # Calculate the aggregated wind speed inside every cell of size (50x50)
    cell_nr_x = 0
    cell_nr_y = 0

    # For every grid-cell
    for i in range(min_coord, max_coord, cell_size):
        cell_nr_x = 0
        for j in range(min_coord, max_coord, cell_size):
            x_wind_values = []
            y_wind_values = []
            # For every datapoint in the grid-cell
            for u in range(i, i+cell_size):
                for v in range(j, j+cell_size):
                    if not x_wind_altitude[u][v] > 100:
                        x_wind_values.append(x_wind_altitude[u][v])
                    if not y_wind_altitude[u][v] > 100:
                        y_wind_values.append(y_wind_altitude[u][v])
            
            # Get middle coordinates
            index_x = i//cell_size
            index_y = j//cell_size

            # get the mean x and y values for the current cell and store it
            x_cell_wind_components[index_x][index_y] = calc_mean(x_wind_values)
            y_cell_wind_components[index_x][index_y] = calc_mean(y_wind_values)

            # Calculate the wind speed
            speed = (pow(x_cell_wind_components[index_x][index_y],2) + pow(y_cell_wind_components[index_x][index_y],2))**0.5
            wind_speed.append(speed)

            # Add coordinates of each arrow
            x_cell_coords[index_x][index_y] = j + (cell_size/2)
            y_cell_coords[index_x][index_y] = i + (cell_size/2)

    return x_cell_coords, y_cell_coords, x_cell_wind_components, y_cell_wind_components, wind_speed
