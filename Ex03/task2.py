import csv
import random
import math
import operator
import numpy as np

# TODO: remove link, only for validating implementation
#https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/

# Load dataset and split into trainingSet and testSet
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
    with open(filename, 'rt', encoding='utf8') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])

# Calculate the euclidean distance between two data points
def euclideanDistance(instance1, instance2, length):
    
    distance = 0

    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)

# Get the k-neighbors of a data point
def getNeighbors(trainingSet, testInstance, k):
    
    distances = []

    # length = 4
    length = len(testInstance)-1

    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        # add tuple containing the training set data point and distance of it to the test instance
        # ([4.8, 3.0, 1.4, 0.1, 'Iris-setosa'], 0.1414213562373099)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []

    for x in range(k):
        neighbors.append(distances[x])
    return neighbors

# Get guesses of the neighbors
def get_vote(neighbors):

    # define dictionary to hold votes of each class
    classVotes = {}

    for x in range(len(neighbors)):
        guessed_class = neighbors[x][0][-1]
        if guessed_class in classVotes:
            if(neighbors[x][1] == 0.0):
                classVotes[guessed_class] += 1
            else:
                classVotes[guessed_class] += 1/neighbors[x][1]
        else:
            if(neighbors[x][1] == 0.0):
                classVotes[guessed_class] = 1
            else:
                classVotes[guessed_class] = 1/neighbors[x][1]
        
    # sort the votes and return the max
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

# Get the accuracy of the testset and predictions
def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet)))*100.0


def k_nearest(filename, k, split):
    
    trainingSet=[]
    testSet=[]
    class_guesses = []
    matched = []
    labels = []

    loadDataset(filename, split, trainingSet, testSet)

    for i in range(len(testSet)):
        neighbors= getNeighbors(trainingSet, testSet[i], k)
        vote = get_vote(neighbors)
        class_guesses.append(vote)
        if(vote == testSet[i][-1]):
            matched.append((testSet[i], 1, vote))
        else:
            matched.append((testSet[i], 0, vote))
    
    # matched ([4.9, 3.0, 1.4, 0.2, 'Iris-setosa'], 1, 'Iris-setosa')
    
    print('Accuracy: ', round(getAccuracy(testSet, class_guesses), 2), '%')

    return trainingSet, testSet, matched

####################################################
# MAIN PROGRAM
####################################################

# Task 2
trainingSet, testSet, matched = k_nearest('iris.data', 3, 0.7)

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

# build the cluster-plot
from bokeh.plotting import figure, output_file, show
circle_size = 8

p = figure(plot_width=750, plot_height=750, x_range=(4, 9), y_range=(1, 6))

p.circle(
    class_1[:,0],
    class_1[:,1],
    size=circle_size,
    color="red",
    legend='Iris-setosa'
    )
p.circle(
    class_2[:,0],
    class_2[:,1],
    size=circle_size,
    color="blue",
    legend='Iris-versicolor'
    )
p.circle(
    class_3[:,0],
    class_3[:,1],
    size=circle_size,
    color="green",
    legend='Iris-virginica'
    )
p.circle(
    errors[:,0],
    errors[:,1],
    size=circle_size,
    color="black",
    legend='wrongly classified'
    )

# set axis titles
p.xaxis.axis_label = 'sepal length'
p.yaxis.axis_label = 'sepal width'

# display plot
show(p)

