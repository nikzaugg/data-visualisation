'''
This file hold functions with are used for data manipulation
'''

import csv
import random
import math
import operator
import numpy as np

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
    
    print('Accuracy: ', round(getAccuracy(testSet, class_guesses), 2), '%')

    return trainingSet, testSet, matched

def plot_iris_data(x1, y1, x2, y2, x3, y3, color1, color2, color3, legend1, legend2, legend3, x_label, y_label, circle_size):
    from bokeh.plotting import figure
    # size of points on the plot
    cirle_size = 10

    # create bokeh figure
    flower_plot = figure(
        plot_width=900, 
        plot_height=900
    )

    flower_plot.circle(
            x1,
            y1,
            size=cirle_size,
            color=color1,
            legend=legend1
            )

    flower_plot.circle(
            x2,
            y2,
            size=cirle_size,
            color=color2,
            legend=legend2
            )

    flower_plot.circle(
            x3,
            y3,
            size=cirle_size,
            color=color3,
            legend=legend3
            )

    # Name the axis of the plot
    flower_plot.xaxis.axis_label = x_label
    flower_plot.yaxis.axis_label = y_label

    return flower_plot


def calc_max(data):
    sum = [0,0,0,0]
    max = [0,0,0,0]
    
    for i in range(len(data)):
        for j in range(len(data[0]) - 1):
            # caluculate max
            if float(data[i][j]) > float(max[j]):
                max[j] = round(float(data[i][j]), 2)           
    
    return max

def calc_min(data):
    from math import inf
    sum = [0,0,0,0]
    min = [inf,inf,inf,inf]
    for i in range(len(data)):
        for j in range(len(data[0]) - 1):
            # caluculate min
            if float(data[i][j]) < float(min[j]):
                min[j] = round(float(data[i][j]), 2)           
    return min

def calc_sum(data):
    sum = [0,0,0,0]
    for i in range(len(data)):
        for j in range(len(data[0]) - 1):
            # calculate sum
            sum[j] += float(data[i][j])
    return sum

def calc_mean(data):
    sum = calc_sum(data)
    mean = [0,0,0,0]
    # get mean
    for i in range(len(data[0]) - 1):
        mean[i] = round(sum[i] / len(data), 2)
    return mean

def calc_standard_deviation(data):
    from math import sqrt
    sd = [0,0,0,0]
    intermediate = [0,0,0,0]
    mean = calc_mean(data)

    for i in range(len(data)):
        for j in range(len(data[0]) - 1):
            intermediate[j] += (float(data[i][j]) - mean[j])**2
    for j in range(len(data[0]) - 1):
        sd[j] = round(sqrt(1/len(data) * intermediate[j]), 2)
    return sd
