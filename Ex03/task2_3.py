import csv
import random
import math
import operator
import numpy as np
import func as f
from bokeh.plotting import show

# Task 2
trainingSet, testSet, matched = f.k_nearest('iris.data', 3, 0.7)

# Task 3
correctly_clustered = []
incorrectly_clustered = []
for i in range(len(matched)):
    if matched[i][1] == 1:
        correctly_clustered.append(matched[i])
    else:
        incorrectly_clustered.append(matched[i])

# Iris-setosa
class_1 = []
# Iris-versicolor
class_2 = []
# Iris-virginica
class_3 = []
# Error class
errors = []

for i in range(len(correctly_clustered)):  
    if correctly_clustered[i][0][-1] == 'Iris-setosa':
        class_1.append(correctly_clustered[i][0])
    
    elif correctly_clustered[i][0][-1] == 'Iris-versicolor':
        class_2.append(correctly_clustered[i][0])
    
    elif correctly_clustered[i][0][-1] == 'Iris-virginica':
        class_3.append(correctly_clustered[i][0]) 

for i in range(len(incorrectly_clustered)):
     errors.append(incorrectly_clustered[i][0])

# Iris-setosa
class_1 = np.array(class_1)
class_1 = np.array(class_1[:, :-1], dtype=float)

# Iris-versicolor
class_2 = np.array(class_2)
class_2 = np.array(class_2[:, :-1], dtype=float)

# Iris-virginica
class_3 = np.array(class_3)
class_3 = np.array(class_3[:, :-1], dtype=float)

# Error class
errors = np.array(errors)
errors = np.array(errors[:, :-1], dtype=float)


# Load original plot from task 1 for comparison
dataset = f.loadDataSet('iris.data')
setosa_flowers = f.getFlowerDataset(dataset, 'Iris-setosa')
versicolor_flowers = f.getFlowerDataset(dataset, 'Iris-versicolor')
virginica_flowers = f.getFlowerDataset(dataset, 'Iris-virginica')

setosa_sepal_length, setosa_sepal_width = f.getSepalDataset(setosa_flowers)
versicolor_sepal_length, versicolor_sepal_width = f.getSepalDataset(versicolor_flowers)
virginica_sepal_length, virginica_sepal_width = f.getSepalDataset(virginica_flowers)

plot = f.plot_iris_data(
    setosa_sepal_length, 
    setosa_sepal_width, 
    versicolor_sepal_length,  
    versicolor_sepal_width,
    virginica_sepal_length,
    virginica_sepal_width,
    "red",
    "blue",
    "green",
    "Iris-setosa",
    "Iris-versicolor",
    "Iris-virginica",
    "Sepal length",
    "Sepal width",
    10
    )

circle_size = 6

plot.circle(
    class_1[:,0],
    class_1[:,1],
    size=circle_size,
    fill_color="orangered",
    legend = "cluster setosa"
    )
plot.circle(
    class_2[:,0],
    class_2[:,1],
    size=circle_size,
    fill_color="aqua",
    legend = "cluster versicolor"
    )
plot.circle(
    class_3[:,0],
    class_3[:,1],
    size=circle_size,
    fill_color="palegreen",
    legend = "cluster virginica"
    )
plot.circle(
    errors[:,0],
    errors[:,1],
    size=circle_size,
    color="black",
    legend='wrongly classified'
    )

# display plot
show(plot)

