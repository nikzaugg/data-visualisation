# Data Visualisation
# University of Zurich
# Exercise 4
# Nik Zaugg
# 12-716-734
# Task 1

'''
Loads all plots except the scatter matrix in one figure.
The scatter-plot matrix is shown in a separate figure
'''


import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd
from pandas.plotting import scatter_matrix
from task1 import terrain_data
from task2 import temp_line_data
from task3 import stacked_line_data
from task4 import color_contour_map_data
from task5 import quiver_plot_data
from task5_2 import scatterplot_matrix_data
import seaborn as sns

# Load data for plot 1 - task 1 - terrain map
plot1_data = terrain_data()

# Load data for plot 2 - task 2 - line plot
temps, altitude_1 = temp_line_data()

# Load data for plot 3 - task 3 - stacked line plot
temperatures_per_hour, altitude_2 = stacked_line_data()

# Load data for plot 4 - task 4 - color contour map
temp_data_altitude = color_contour_map_data()

# Load data for plot 5a - task 5a - quiver plot
x_cell_coords, y_cell_coords, x_cell_wind_components, y_cell_wind_components, wind_speed = quiver_plot_data()

# Load data for plot 5b - task 5b - scatter plot matrix
all_data, columns = scatterplot_matrix_data()

fig = plt.figure(figsize=(13,10))

ax1 = plt.subplot2grid((3, 2), (0, 0))
ax1.set_title("Filled Contour Map")
terrain_plot = ax1.contourf(plot1_data, cmap='terrain')
ax1.set_xlabel("Longitude (X)")
ax1.set_ylabel("Latitude (Y)")
ax1.invert_yaxis()
ax1.set_aspect(1)
colorbar = plt.colorbar(terrain_plot, ax=ax1)
colorbar.set_label('terrain elevation [m]')

ax2 = plt.subplot2grid((3, 2), (1, 0))
ax2.set_title("Temperature data at altitude levels in hour 1")
terrain_plot = ax2.plot(altitude_1, temps, color = 'blue')
ax2.set_xlabel("Altitude levels [km]")
ax2.set_ylabel("Temperature [$^\circ$C]")

ax3 = plt.subplot2grid((3, 2), (2, 0))
ax3.set_title("Temperatures at different altitude levels. (200, 250)")
ax3.plot(altitude_2, temperatures_per_hour[0], label='Hour 1')
ax3.plot(altitude_2, temperatures_per_hour[1], label='Hour 2')
ax3.plot(altitude_2, temperatures_per_hour[2], label='Hour 3')
ax3.plot(altitude_2, temperatures_per_hour[3], label='Hour 4')
ax3.plot(altitude_2, temperatures_per_hour[4], label='Hour 5')
ax3.minorticks_on()
ax3.set_xlabel("Altitude Level [km]")
ax3.set_ylabel("Temperature [$^\circ$C]")

ax4 = plt.subplot2grid((3, 2), (0, 1))
ax4.set_title('Temperatures at altitude of 1km')
ax4.set_xlabel('Longitude (X)')
ax4.set_ylabel('Latitude (Y)')
ax4.invert_yaxis()
ax4.set_aspect(1)
terrain_plot_2 = ax4.contourf(plot1_data, cmap='terrain')
colorbar = plt.colorbar(terrain_plot_2, ax=ax4)
colorbar.set_label('terrain elevation [m]')
temp_contour = ax4.contourf(temp_data_altitude, cmap='jet', alpha=0.8)
colorbar = plt.colorbar(temp_contour)
colorbar.set_label('Temperature')

ax5 = plt.subplot2grid((3, 2), (1, 1))
ax5.set_title('UVW Quiver Plot')
ax5.set_xlabel('Longitude (X)')
ax5.set_ylabel('Latitude (Y)')
ax5.invert_yaxis()
ax5.set_aspect(1)
terrain_plot_3 = ax5.contourf(plot1_data, cmap='cubehelix')
colorbar = plt.colorbar(terrain_plot_3, ax=ax5)
colorbar.set_label('terrain elevation [m]')
color_map = cm.spring
norm_speed = matplotlib.colors.Normalize(vmin=min(wind_speed), vmax=max(wind_speed))
norm_speed_colors = matplotlib.cm.ScalarMappable(norm=norm_speed, cmap=color_map)
norm_speed_colors.set_array([ ])

colorbar = plt.colorbar(norm_speed_colors, ax=ax5)
colorbar.set_label("wind speed [m/s]")
ax5.quiver(x_cell_coords, y_cell_coords,
                x_cell_wind_components, y_cell_wind_components,
                color=color_map(norm_speed(wind_speed)),
                pivot ='middle',
                units ='height')
plt.tight_layout()
data_frame = pd.DataFrame(all_data, columns=columns)
sns.pairplot(data_frame)


plt.tight_layout()
plt.show()