# -*- coding: utf-8 -*-
# Author: Nik Zaugg, 12-716-734
# Data Visualization
# University of Zurich - HS17

# Import modules
import numpy as np
from PIL import Image
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import layout, column, row
from bokeh.models import HoverTool, Div

##############################################################################
# FUNCTIONS
##############################################################################

def loadImage(image):
    ''' Reads an image file and return the raw image, image as array and the view of the image
    '''
    import PIL as pil 
    import numpy as np
    
    # open image, convert to rgba and get width and height
    raw_image = pil.Image.open(image)
    img_width, img_height = raw_image.size
    image_in_rgba = raw_image.convert('RGBA')
    
    
    # transform the input rgba image into an 8-bit "4 layer/RGBA" array
    image_array = np.empty((img_height, img_width), dtype = np.uint32)
    image_view = image_array.view(dtype = np.uint8).reshape(img_height, img_width, 4)
    
    # Copy the RGBA image into view, flipping it so it comes right-side up
    # with a lower-left origin
    image_view[:,:,:] = np.flipud(np.asarray(image_in_rgba))
    
    return raw_image, image_array, image_view

    
def getColorChannels(image_view):
    ''' 
    Extract color channels of an image view
    
    Return:
    red_channel: array containing red values
    green_channel: array containing green values
    blue_channel: array containing blue values
    alpha_channel: array containing alpha values
    
    '''
    # RGBA - [Red, Green, Blue, Alpha]
    # Split image view into 4 arrays, each representing one channel [Red], [Green], [Blue], [Alpha]
    # So the image view array gets split on the vertical rows
    channels = np.dsplit(image_view, 4)
    
    # Create color array for each RGBA color/alpha value
    red_colors = np.add.reduce(channels[0],2)
    green_colors = np.add.reduce(channels[1],2)
    blue_colors = np.add.reduce(channels[2],2)
    alpha_values = np.add.reduce(channels[3],2)
    
    # Adjust alpha values
    #alpha_values[:] = np.uint32(alpha_values[:]* (1/3) )
    
    ##########################################################################
    # RED CHANNEL                                                            
    ##########################################################################
    # Get the dimensions of the red channel (768 X 1024 in this case)
    height, width = red_colors.shape
    
    # Create array filled with zeros of dimension 768 x 1024
    # 768 rows, each containing one array with 1024 zeros
    zeros_array = np.zeros(red_colors.shape)
    
    # Initialize the red channel
    # Create array of dimension 768 x 1024 with each data point containing an array [0 0 0 0]
    # Data Type of the values inside the arrays are unsigned 8-bit integers
    red_channel = np.zeros((height, width,4), 'uint8')
    
    # Inserts the red color array into the zero-array
    # red_channel has the shape: (768, 1024, 4)
    # [:,:,0] the 0 depicts the first position inside every inner array
    # [:,:,1] the 1 depicts the second position inside every inner array
    # [:,:,2] the 2 depicts the third position inside every inner array
    # [:,:,3] the 3 depicts the fourth position inside every inner array
    red_channel[:,:,0] = red_colors
    red_channel[:,:,1] = zeros_array
    red_channel[:,:,2] = zeros_array
    red_channel[:,:,3] = alpha_values
    
    ##########################################################################
    # GREEN CHANNEL                                                          
    ##########################################################################
    # Get the dimensions of the green channel (768 X 1024 in this case)
    height, width = green_colors.shape
    
    # Create array filled with zeros of dimension 768 x 1024
    # 768 rows, each containing one array with 1024 zeros
    zeros_array = np.zeros(green_colors.shape)
    
    # Initialize the green channel
    # Create array of dimension 768 x 1024 with each data point containing an array [0 0 0 0]
    # Data Type of the values inside the arrays are unsigned 8-bit integers
    green_channel = np.zeros((height, width,4), 'uint8')
    
    # Inserts the green color array into the zero-array
    # green_channel has the shape: (768, 1024, 4)
    # [:,:,0] the 0 depicts the first position inside every inner array
    # [:,:,1] the 1 depicts the second position inside every inner array
    # [:,:,2] the 2 depicts the third position inside every inner array
    # [:,:,3] the 3 depicts the fourth position inside every inner array
    green_channel[:,:,0] = green_colors
    green_channel[:,:,1] = zeros_array
    green_channel[:,:,2] = zeros_array
    green_channel[:,:,3] = alpha_values    
    
    ##########################################################################
    # BLUE CHANNEL                                                           
    ##########################################################################
    # Get the dimensions of the blue channel (768 X 1024 in this case)
    height, width = blue_colors.shape
    
    # Create array filled with zeros of dimension 768 x 1024
    # 768 rows, each containing one array with 1024 zeros
    zeros_array = np.zeros(blue_colors.shape)
    
    # Initialize the blue channel
    # Create array of dimension 768 x 1024 with each data point containing an array [0 0 0 0]
    # Data Type of the values inside the arrays are unsigned 8-bit integers
    blue_channel = np.zeros((height, width,4), 'uint8')
    
    # Inserts the blue color array into the zero-array
    # blue_channel has the shape: (768, 1024, 4)
    # [:,:,0] the 0 depicts the first position inside every inner array
    # [:,:,1] the 1 depicts the second position inside every inner array
    # [:,:,2] the 2 depicts the third position inside every inner array
    # [:,:,3] the 3 depicts the fourth position inside every inner array
    blue_channel[:,:,0] = blue_colors
    blue_channel[:,:,1] = zeros_array
    blue_channel[:,:,2] = zeros_array
    blue_channel[:,:,3] = alpha_values  
    
    # return all 3 color channels
    return red_channel, green_channel, blue_channel

def divider_div():
    div = Div(text= '<div style="height: 30px"></div>')
    return div

def plot_original_image():
    return None

def plot_color_channel():
    return None


# =============================================================================
# Main Entry
# =============================================================================

# Create HTML-tags for title and subtitle
dashboard_title = Div(text= '<div style="text-align: center; margin-top: 40px !important"><h1>Dashboard</h1></div>')
dashboard_subtitle = Div(text= '<div style="text-align: center; color: grey"><h2>Image Processing Applications</h1></div>')

# Simple HTML-div to add margin between first plot and the following plots
divider = divider_div()

image, image_arr, image_view = loadImage('image.jpg')
    
image_width, image_height = image.size



red, green, blue = getColorChannels(image_view)

# Display the 32-bit RGBA image
dim = max(image_width, image_height)
fig = figure(title="Scrat", x_range=(0, image_width), y_range=(0, image_height), plot_width=600, plot_height=412)
fig.image_rgba(image=[red], x=0, y=0, dw=image_width, dh=image_height)
output_file("scrat.html", title="image example")

show(fig)
# =============================================================================





    
