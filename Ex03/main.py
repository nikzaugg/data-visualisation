# Task 1
# Data Visualisation Exercise 3
# UZH HS17 
# Nik Zaugg, 12-716-734

# Create a 2D plot (Plot1) from data in Iris dataset, using the sepal length and sepal width. Use
# separate color for each species for visually identifying the iris species.

# Question 1: What type of variables has the Iris dataset? Refer the type of each variable.
# sepal_length: Is an ordinal variable which is continuous and ordinal.
# sepal_width: Is an ordinal variable which is continuous and ordinal.
# petal_length: Is an ordinal variable which is continuous and ordinal.
# petal_width: Is an ordinal variable which is continuous and ordinal.
# species: Is a nominal variable and categorical.


# Question 2: How many features are included in the Iris dataset? Which are they?
# three features, x and y coordinates as well as the name of the flowers

import numpy as np
import pandas as pd
from bokeh.plotting import figure, ColumnDataSource, output_file, show
from bokeh.models import HoverTool

def loadDataSet(filename):
    ''' Load a .data file into a data set
    # sepal_length, sepal_width, petal_length, petal_width, species
    # Iris-setosa
    # Iris-versicolor
    # Iris-virginica

    Arguments: 
        - filename
    Return:
        - dataset as list
    '''
    import csv
    
    data = []
    with open(filename, 'rt', encoding='utf8') as csvfile:
        lines = csv.reader(csvfile)
        for row in lines:
            data.append(row)
    
    return data

def getFlowerDataset(data, flowerName):
    ''' Split data into its flower category
    '''
    flowers = []
    for x in range(len(data)-1):
        if data[x][4] == flowerName:
            flowers.append(data[x])
    return flowers

def getSepalDataset(data):
    ''' Extract sepal width and length of flower data set
    '''
    lengths = []
    widths = []
    for x in range(len(data)):
        lengths.append(float(data[x][0]))
        widths.append(float(data[x][1]))

    return lengths, widths

# Main Program
dataset = loadDataSet('iris.data')
setosa_flowers = getFlowerDataset(dataset, 'Iris-setosa')
versicolor_flowers = getFlowerDataset(dataset, 'Iris-versicolor')
virginica_flowers = getFlowerDataset(dataset, 'Iris-virginica')

setosa_sepal_length, setosa_sepal_width = getSepalDataset(setosa_flowers)
versicolor_sepal_length, versicolor_sepal_width = getSepalDataset(versicolor_flowers)
virginica_sepal_length, virginica_sepal_width = getSepalDataset(virginica_flowers)

#Plot Task 1
output_file('task1.html')

# size of points on the plot
cirle_size = 6

# specify a hover tool
hover = HoverTool(tooltips=[
    ("Sepal length", "@x"),
    ("Sepal width", "@y"),
])

# create bokeh figure
flower_plot = figure(
    plot_width=700, 
    plot_height=600,
    tools= [hover])

flower_plot.circle(
        setosa_sepal_length,
        setosa_sepal_width,
        size=cirle_size,
        color="red",
        legend='Iris-setosa')

flower_plot.circle(
        versicolor_sepal_length,
        versicolor_sepal_width,
        size=cirle_size,
        color="blue",
        legend='Iris-versicolor')

flower_plot.circle(
        virginica_sepal_length,
        virginica_sepal_width,
        size=cirle_size,
        color="green",
        legend='Iris-virginica')


# Name the axis of the plot
flower_plot.xaxis.axis_label = 'Sepal length'
flower_plot.yaxis.axis_label = 'Sepal width'

# Display the plot in html file
show(flower_plot)
