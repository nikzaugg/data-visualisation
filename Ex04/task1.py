'''
(OPTIONAL) In your first task, setup a proper terrain map for visualizing (simulating) on top of it
the data from the hurricane simulation. You can select any form of terrain with the texture of
your choice, either in 2D or in 3D. Details about the exact geographical area are provided either
in the lab slides or in the above-mentioned link.
'''

from data_controller import get_terrain_data2, get_terrain_data
import matplotlib.pyplot as plt

# load terrain
data = get_terrain_data()

fig, plot = plt.subplots()

fig.canvas.set_window_title('TASK 1') 

plot.set_title('HGTdata Contour Plot Filled')

plot.set_xlabel('Longitude (X)')
plot.set_ylabel('Latitude (Y)')

plot.invert_yaxis()

terrain_plot = plot.contourf(data, cmap='terrain')

colorbar = plt.colorbar(terrain_plot)
colorbar.set_label('terrain elevation [m]')

plt.show()
