# -*- coding: utf-8 -*-
# Author: Nik Zaugg, 12-716-734
# Data Visualization
# Exercise 2
# University of Zurich - HS17

# Import modules
import numpy as np
import scipy
import PIL as pil
from PIL import Image
from bokeh.plotting import figure, ColumnDataSource, curdoc
from bokeh.layouts import column, row, widgetbox, layout
from bokeh.models import Div, CustomJS, Slider
from bokeh.models.widgets import Panel, Tabs

##############################################################################
# DATA MANIPULATION FUNCTIONS
##############################################################################

def loadImage(image):
    ''' Reads an image file and return the raw image, image as array and the view of the image
    '''
    # open image, convert to rgba and get width and height
    raw_image = Image.open(image)
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
    green_channel[:,:,0] = zeros_array
    green_channel[:,:,1] = green_colors
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
    blue_channel[:,:,0] = zeros_array
    blue_channel[:,:,1] = zeros_array
    blue_channel[:,:,2] = blue_colors
    blue_channel[:,:,3] = alpha_values  
    
    # return all 3 color channels
    return red_channel, green_channel, blue_channel

def gray_scale_weighted(pixel):
    return 0.3*pixel[0] + 0.59*pixel[1] + 0.11*pixel[2]

def get_grayscale_channel(image):
    grey = np.zeros((image.shape[0], image.shape[1],1), 'uint8')
    for rownum in range(len(image)):
        for colnum in range(len(image[rownum])):
            grey[rownum][colnum] = gray_scale_weighted(image[rownum][colnum])
    return grey

def reduced_color_channel(image, size):
    # TODO: implement function that allows for more control
    # This is not the algo we saw in the exercise
    from scipy import ndimage
    copy_image = np.copy(image)
    return ndimage.median_filter(copy_image, size)

def salt_pepper_noise(image, percentage):
    import random
    salt_pepper = np.copy(image)
    counter = 0
    black = [0,0,0,255]
    white = [255,255,255,255]
    while counter <= int(768*1024*(percentage/100.0)):
        random_col = random.randint(0, 1023)
        random_row = random.randint(0, 767)
        random_color = random.randint(0,1)
        if(random_color == 0):
                salt_pepper[random_row][random_col] = black
                counter += 1
        if(random_color == 1):
            salt_pepper[random_row][random_col] = white
            counter += 1
    return salt_pepper

# https://stackoverflow.com/questions/31751210/how-can-i-prevent-numpy-scipy-gaussian-blur-from-converting-image-to-grey-scale
# As the values in the third dimension are too close together with this filter, it will result in a gray-scale like blur
def gaussian_filter(channel, sigma):
    '''
    '''
    x = scipy.ndimage.filters.gaussian_filter(channel[:,:,0:3], sigma)
    return x

# Apply gaussian filter to all three color channel seperately to keep color in the image
def gaussian_filter_3_channels(red, green, blue, sigma):
    combined_gaussian = np.zeros((red.shape[0], red.shape[1], 4), 'uint8')
    
    copy_red = np.copy(red)
    copy_green = np.copy(green)
    copy_blue = np.copy(blue)
    
    gaussian_red = scipy.ndimage.filters.gaussian_filter(copy_red[:,:,0], sigma)
    gaussian_green = scipy.ndimage.filters.gaussian_filter(copy_green[:,:,1], sigma)
    gaussian_blue = scipy.ndimage.filters.gaussian_filter(copy_blue[:,:,2], sigma)
    
    combined_gaussian[:,:,0] = gaussian_red[:]
    combined_gaussian[:,:,1] = gaussian_green[:] 
    combined_gaussian[:,:,2] = gaussian_blue[:]
    combined_gaussian[:,:,3] = 255
    
    return combined_gaussian 


###############################################################################
# DEFINE PLOT FUNCTIONS
###############################################################################
def plot_original_image(image_path, height, width):
    ''' Plot original image
    '''
    image, image_arr, image_view = loadImage(image_path)
    image_width, image_height = image.size
    
    # Create plot for original image
    fig = figure(title="Original Image", x_range=(0, image_width), y_range=(0, image_height), plot_width = width, plot_height = height)
    fig.image_rgba(image=[image_view], x=0, y=0, dw=image_width, dh=image_height)
    
    return fig

def plot_color_channel(channel, image, height, width, plot_name):
    
    image_width, image_height = image.size
    
    # Create plot for original image
    fig = figure(title=plot_name, x_range=(0, image_width), y_range=(0, image_height), plot_width = width, plot_height = height)
    fig.image_rgba(image=[channel], x=0, y=0, dw=image_width, dh=image_height)

    return fig

def plot_grayscale_and_reduced(grey, reduced, image, height, width, plot_name):
    
    image_width, image_height = image.size
    
    # Tab 1
    fig_greyscale = figure(title=plot_name, x_range=(0, image_width), y_range=(0, image_height), plot_width = width, plot_height = height)
    fig_greyscale.image(image=[grey], x=0, y=0, dw=image_width, dh=image_height)
    tab1 = Panel(child=fig_greyscale, title="Greyscale")
    
    # Tab 2
    fig_reduced = figure(title=plot_name, x_range=(0, image_width), y_range=(0, image_height), plot_width = width, plot_height = height)
    fig_reduced.image_rgba(image=[reduced], x=0, y=0, dw=image_width, dh=image_height)
    tab2 = Panel(child=fig_reduced, title="Reduced Colors")
    
    # Build Tab
    tabs = Tabs(tabs=[ tab1, tab2 ])
    
    return tabs

def plot_salt_pepper_plot(img_noise, image, height, width, plot_name):
    '''
    '''
  
    image_width, image_height = image.size   
    
    fig = figure(title=plot_name, x_range=(0, image_width), y_range=(0, image_height), plot_width = width, plot_height = height)
    fig.image_rgba(image=[img_noise], x=0, y=0, dw=image_width, dh=image_height)
        
    return fig

def plot_salt_pepper_plot_slider(img_noise, image_view, height, width, plot_name):
    
    image_width = 1024
    image_height = 768

    fig = figure(title=plot_name, x_range=(0, image_width), y_range=(0, image_height), plot_width = width, plot_height = height)
    
    image = fig.image_rgba(image=[img_noise], x=0, y=0, dw=image_width, dh=image_height)

    salt_pepper_slider = Slider(title = 'Percentage of Noise', start=0, end=50, step=1, value=10)

    def update_salt_pepper(attrname, old, new):
        new_image = salt_pepper_noise(image_view, salt_pepper_slider.value)
        image.data_source.data = {'image': [new_image]}
    
    salt_pepper_slider.on_change('value', update_salt_pepper)
    
    plot_salt_pepper_slider = widgetbox(salt_pepper_slider)

    return fig, plot_salt_pepper_slider

def plot_gaussian_filter(gauss_image, image, height, width, plot_name):
    
    image_width, image_height = image.size   
    
    fig = figure(title=plot_name, x_range=(0, image_width), y_range=(0, image_height), plot_width = width, plot_height = height)
    gauss_image = fig.image_rgba(image=[gauss_image], x=0, y=0, dw=image_width, dh=image_height)
    
    return fig

def plot_gaussian_filter_slider(img_gauss, red, green, blue, height, width, plot_name):
    
    image_width = 1024
    image_height = 768
    
    fig = figure(title=plot_name, x_range=(0, image_width), y_range=(0, image_height), plot_width = width, plot_height = height)
    image = fig.image_rgba(image=[img_gauss], x=0, y=0, dw=image_width, dh=image_height)
        
    gauss_slider = Slider(title = 'Sigma value', start=0, end=5, step=1, value=2)

    def update_gaussian(attrname, old, new):
        new_image = gaussian_filter_3_channels(red, green, blue, gauss_slider.value)
        image.data_source.data = {'image': [new_image]}
    
    gauss_slider.on_change('value', update_gaussian)
    
    plot_gaussian_slider = widgetbox(gauss_slider)

    return fig, plot_gaussian_slider

###############################################################################
# Main Program
###############################################################################

# Define dashboard parameters
dashboard_width = 1300
width_big = 900
width_medium = 400
width_small = 300
height_big = 594
height_medium = 274
height_small = 200

# Create HTML-tags for title and subtitle
dashboard_title = Div(text= '<div style="text-align: center; margin-top: 10px !important; padding: 0 !important;"><h1 style="margin-bottom: 0 !important;">Dashboard</h1></div>', width= dashboard_width)
dashboard_subtitle = Div(text= '<div style="text-align: center; color: grey"><h2>Image Processing Applications</h1></div>', width= dashboard_width)

# Load the image details for later plotting
image, image_arr, image_view = loadImage('image.jpg')

# Do modifications on the image data
red, green, blue = getColorChannels(image_view)
grey = get_grayscale_channel(image_view)
reduced = reduced_color_channel(image_view, 3)

salt_pepper = salt_pepper_noise(image_view, 10)

gaussian = gaussian_filter_3_channels(red, green, blue, 2)

# PLOT 1: Plot with original image
plot_original = plot_original_image('image.jpg', height_big, width_big)

# PLOT 2,3,4: Generate Plot for each color channel
plot_red = plot_color_channel(red, image, height_small, width_small, "Red")
plot_green = plot_color_channel(green, image, height_small, width_small, "Green")
plot_blue = plot_color_channel(blue, image, height_small, width_small, "Blue")

# PLOT 5: Generate tab-plot with grayscale & reduced colors
plot_tabs = plot_grayscale_and_reduced(grey, reduced, image, height_medium, width_medium, 'Greyscale & Reduced Color')

# PLOT 6: Generate plot with salt & pepper noise
plot_salt_pepper, slider_salt_pepper = plot_salt_pepper_plot_slider(salt_pepper, image_view, height_medium, width_medium, "Random Salt & Pepper Noise")       

# PLOT 7: Generate plot with gaussian filter applied to it
plot_gaussian, slider_gaussian = plot_gaussian_filter_slider(gaussian, red, green, blue, height_medium, width_medium, "Gaussian Filter")   

# Define Layout for dashboard
curdoc().add_root(row(dashboard_title))
curdoc().add_root(row(dashboard_subtitle))
curdoc().add_root(row([
            column([
                row(plot_original), 
                row([plot_red,plot_green,plot_blue])
            ]),
            column([
                row(plot_tabs),
                row([plot_salt_pepper, slider_salt_pepper]),
                row([plot_gaussian, slider_gaussian])
            ])
        ])
        ) 
# =============================================================================
# =============================================================================
# LAYOUT TESTS 
# TODO: remove after 
# =============================================================================
# fig1 = figure(title="TEST", x_range=(0, 1024), y_range=(0, 768), plot_width = 900, plot_height = 594)
# fig2 = figure(title="TEST", x_range=(0, 1024), y_range=(0, 768), plot_width = 300, plot_height = 200)
# fig3 = figure(title="TEST", x_range=(0, 1024), y_range=(0, 768), plot_width = 300, plot_height = 200)
# fig4 = figure(title="TEST", x_range=(0, 1024), y_range=(0, 768), plot_width = 300, plot_height = 200)
# 
# fig5 = figure(title="TEST", x_range=(0, 1024), y_range=(0, 768), plot_width = 400, plot_height = 274)
# 
# fig6 = figure(title="TEST", x_range=(0, 1024), y_range=(0, 768), plot_width = 400, plot_height = 274)
# fig7 = figure(title="TEST", x_range=(0, 1024), y_range=(0, 768), plot_width = 400, plot_height = 274)
# 
# slide = Slider(start=1, end=5, step=1, value=2)
# slider = widgetbox(slide)
# 
# slide2 = Slider(start=1, end=5, step=1, value=2)
# slider2 = widgetbox(slide2)
# =============================================================================
# dashboard = layout(row(dashboard_title),
#         row(dashboard_subtitle),
#         row([
#             column([row(fig1), 
#                     row([fig2,fig3,fig4])
#                     ]),
#             column([row(fig5),
#                     row([fig6, slider]),
#                     row([fig7, slider2])
#                     ])
#         ]))
# =============================================================================
# Load the dasboard into the output_file  
# show(dashboard)
# =============================================================================
# =============================================================================





    
