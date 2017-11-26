'''
Data Visualization
Exercise 03
Task 1
Author: Nik Zaugg
Student Number: 12-716-734


Create a 2D plot (Plot1) from data in Iris dataset, using the sepal length and sepal width. Use
separate color for each species for visually identifying the iris species.
'''

import numpy as np
import pandas as pd
from bokeh.plotting import output_file, show
import func as f

################
# Main Program #
################

# Load dataset from file and separate into its three classes
dataset = f.loadDataSet('iris.data')
setosa_flowers = f.getFlowerDataset(dataset, 'Iris-setosa')
versicolor_flowers = f.getFlowerDataset(dataset, 'Iris-versicolor')
virginica_flowers = f.getFlowerDataset(dataset, 'Iris-virginica')

# Extract sepal lengths and widths
setosa_sepal_length, setosa_sepal_width = f.getSepalDataset(setosa_flowers)
versicolor_sepal_length, versicolor_sepal_width = f.getSepalDataset(versicolor_flowers)
virginica_sepal_length, virginica_sepal_width = f.getSepalDataset(virginica_flowers)

#Plot Task 1
output_file('task1.html')

plot = f.plot_iris_data(
    setosa_sepal_length, 
    setosa_sepal_width, 
    versicolor_sepal_length,  
    versicolor_sepal_width,
    virginica_sepal_length,
    virginica_sepal_width,
    "gray",
    "orange",
    "olive",
    "Iris-setosa",
    "Iris-versicolor",
    "Iris-virginica",
    "Sepal length",
    "Sepal width",
    10
    )

# Display the plot in html file
show(plot)
