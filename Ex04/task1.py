# Data Visualisation
# University of Zurich
# Exercise 4
# Nik Zaugg
# 12-716-734
# Task 1

'''
Sets up a map for visualizing the terrain where the hurricane happened.
'''
def task1_terrain_map():
    '''
    Plots a terrain map of the hurricain location
    '''

    from data_controller import get_terrain_data
    import matplotlib.pyplot as plt

    # load terrain data
    data = get_terrain_data()

    # load plots
    fig, plot = plt.subplots()

    fig.canvas.set_window_title('Task 1 - terrain map') 

    # define title of the plot
    plot.set_title('Terrain Contour Map')

    plot.set_xlabel('Longitude (X)')
    plot.set_ylabel('Latitude (Y)')

    # invert the y-axis to display proper relations
    plot.invert_yaxis()

    # create a filled contour plot
    terrain_plot = plot.contourf(data, cmap='terrain')

    # add a colorbar to visualize different terrain elevations
    colorbar = plt.colorbar(terrain_plot)
    colorbar.set_label('terrain elevation [m]')

    # display the plot
    plt.show()

def terrain_data():
    '''
    Return data needed to plot the terrain map
    '''
    from data_controller import get_terrain_data
    import matplotlib.pyplot as plt

    # load terrain data
    data = get_terrain_data()

    return data
