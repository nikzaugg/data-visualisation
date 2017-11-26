'''
This file holds functions with are used for data preprocessing and plotting

Data Visualization
Exercise 03
Author: Nik Zaugg
Student Number: 12-716-734
'''

import csv
import random
import math
import operator
import numpy as np

def loadDataSet(filename):
    ''' Load a .data file into a data set

    Args: 
        filename (str): filename of .data-extension file
    Return:
        dataset: 2D list
    '''
    import csv
    
    data = []
    with open(filename, 'rt', encoding='utf8') as csvfile:
        lines = csv.reader(csvfile)
        for row in lines:
            data.append(row)
    
    return data


def loadDataset(filename, split):
    '''
    Load a .data file into a data set and split it into two
    sets according to the provided value between 0 and 1

    Args: 
        filename (str): filename of .data-extension file
        split (float): between 0 and 1
    Return:
        trainingSet: 2D list with training values
        testSet: 2D list with test values
    '''
    trainingSet = []
    testSet = []

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
    
    return trainingSet, testSet

def getFlowerDataset(data, flowerName):
    ''' 
    Split data into its flower category
    
    Args:
        data: 2D-list containing data
        flowerName (str): name of the flower
    '''
    flowers = []
    for x in range(len(data)):
        if data[x][4] == flowerName:
            flowers.append(data[x])
    return flowers


def getSepalDataset(data):
    ''' 
    Extract sepal width and length of flower data set

    Args:
        data: 2D-list containing data
    Return:
        lengths: 1D-list containing all sepal lengths of the flower
        widths: 1D-list containing all sepal widths of the flower
    '''
    lengths = []
    widths = []
    for x in range(len(data)):
        lengths.append(float(data[x][0]))
        widths.append(float(data[x][1]))

    return lengths, widths


# Calculate the euclidean distance between two data points
def euclideanDistance(instance1, instance2, length):
    '''
    Compute the euclidean distance between two instances

    Args:
        instance1: data point 1
        instance2: data point 2
        length (int): length of the datapoints

    Return:
        distance: euclidean distance btween the two data points
    '''
    distance = 0

    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)


# Get the k-neighbors of a data point
def getNeighbors(trainingSet, testInstance, k):
    '''
    Compute the k neares neighbors of a datapoint

    Args:
        trainingSet: 2D list with training values
        testSet: 2D list with test values
        k (int): how many neighbors should be looked at
    Return:
        neighbors: 2D list of the k nearest neighbors
    '''
    distances = []

    # length = 4
    length = len(testInstance)-1

    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        # add tuple containing the training set data point and distance of it to the test instance
        distances.append((trainingSet[x], dist))
    # sort all datapoints
    distances.sort(key=operator.itemgetter(1))
    neighbors = []

    # get the k nearest neighbors
    for x in range(k):
        neighbors.append(distances[x])
    return neighbors


# Get guesses of the neighbors
def get_vote(neighbors):
    '''
    Compute votes of neighbors in relation to their distance to a datapoint

    Args:
        neighbors: 2D list of neighbor data points
    Return:
        vote: dominating class
    '''

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
    '''
    Check the accuracy of a set with the predictions of its classes

    Args:
        testSet: testSet: 2D list with test values
        predictions: list of all votes
    Return:
        correct: percentage of correctly guessed data points
    '''
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet)))*100.0


def k_nearest(filename, k, split):
    '''
    Compute the k nearest neighbors for a data file that is split up into training and test sets
    
    Args:
        filename: name a .data file
        k: number of neighbors to consider for the classification 
        split: split between 0 and 1
    Return:
        trainingSet: 2D list with training values
        testSet: 2D list with test values
        matched: list of all datapoints with indication if guessed correctly
    '''
    class_guesses = []
    matched = []
    labels = []

    trainingSet, testSet = loadDataset(filename, split)

    for i in range(len(testSet)):
        neighbors= getNeighbors(trainingSet, testSet[i], k)
        vote = get_vote(neighbors)
        class_guesses.append(vote)
        if(vote == testSet[i][-1]):
            matched.append((testSet[i], 1, vote))
        else:
            matched.append((testSet[i], 0, vote))
    print("TASK 2 & 3")
    print("--------------------")
    print('Accuracy: ', getAccuracy(testSet, class_guesses), '%')
    print('\n')

    return trainingSet, testSet, matched

def plot_iris_data(plot_title, x1, y1, x2, y2, x3, y3, color1, color2, color3, legend1, legend2, legend3, x_label, y_label, circle_size):
    '''
    Plot the iris data set

    Args:
        x1,x2,x3: values for the x-axis
        y1,y2,y3: values for the y-axis
        color1, color2: color3: colors for each (x,y) pair
        legend1, legend2, legend3: strings to display for each dataset
        x_label: x-axis label
        y_label: y-axis label
        circle_size: size of the data point circles on the plot
    Return:
        flower_plot: bokeh plot of the data
    '''
    from bokeh.plotting import figure
    # size of points on the plot
    cirle_size = 10

    # create bokeh figure
    flower_plot = figure(
        title=plot_title,
        plot_width=900, 
        plot_height=900,
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


def calc_max(data, round_return):
    '''
    Calculate the maximum values for each attribute in a 2D list
    '''
    sum = [0,0,0,0]
    max = [0,0,0,0]
            
    if round_return:
        for i in range(len(data)):
            for j in range(len(data[0]) - 1):
                # caluculate max
                if float(data[i][j]) > float(max[j]):
                    max[j] = round(float(data[i][j]), 2) 
    else:
        for i in range(len(data)):
            for j in range(len(data[0]) - 1):
                # caluculate max
                if float(data[i][j]) > float(max[j]):
                    max[j] = float(data[i][j])  
    return max

def calc_min(data, round_return):
    '''
    Calculate the minimum values for each attribute in a 2D list
    '''
    from math import inf
    sum = [0,0,0,0]
    min = [inf,inf,inf,inf]
    
    if round_return:
        for i in range(len(data)):
            for j in range(len(data[0]) - 1):
                # caluculate min
                if float(data[i][j]) < float(min[j]):
                    min[j] = round(float(data[i][j]),2)
    else:          
        for i in range(len(data)):
            for j in range(len(data[0]) - 1):
                # caluculate min
                if float(data[i][j]) < float(min[j]):
                    min[j] = float(data[i][j])
    return min

def calc_sum(data, round_return):
    '''
    Calculate the sum values for each attribute in a 2D list
    '''
    sum = [0,0,0,0]
    
    if round_return:
        for i in range(len(data)):
            for j in range(len(data[0]) - 1):
                # calculate sum
                sum[j] += round(float(data[i][j]),2)
    else:
        for i in range(len(data)):
            for j in range(len(data[0]) - 1):
                # calculate sum
                sum[j] += float(data[i][j])
    return sum

def calc_mean(data, round_return):
    '''
    Calculate the mean for each attribute in a 2D list
    '''
    
    mean = [0,0,0,0]
    # get mean
    
    if round_return:
        sum = calc_sum(data, True)
        for i in range(len(data[0]) - 1):
            mean[i] = round(sum[i] / len(data), 2)
    else:
        sum = calc_sum(data, False)
        for i in range(len(data[0]) - 1):
            mean[i] = sum[i] / len(data)
    return mean

def calc_standard_deviation(data, round_return):
    '''
    Calculate the standard deviation for each attribute in a 2D list
    '''
    from math import sqrt
    sd = [0,0,0,0]
    intermediate = [0,0,0,0]
    

    if round_return:
        mean = calc_mean(data, True)
        for i in range(len(data)):
            for j in range(len(data[0]) - 1):
                intermediate[j] += (float(data[i][j]) - mean[j])**2
        for j in range(len(data[0]) - 1):
            sd[j] = round(sqrt(1/len(data) * intermediate[j]), 2)
        
    else:
        mean = calc_mean(data, False)
        for i in range(len(data)):
            for j in range(len(data[0]) - 1):
                intermediate[j] += (float(data[i][j]) - mean[j])**2
        for j in range(len(data[0]) - 1):
            sd[j] = sqrt(1/len(data) * intermediate[j])
    
    return sd
