'''
Using the original dataset compute the total and the intraclass minimum, maximum, mean and
standard deviation of each attribute. The results should be presented automatically when running
the code. 
'''

import numpy as np

def loadDataSet(filename):
    import csv
    
    data = []
    with open(filename, 'rt', encoding='utf8') as csvfile:
        lines = csv.reader(csvfile)
        for row in lines:
            data.append(row)
    
    return data


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


data = loadDataSet('iris.data')
species1 = getFlowerDataset(data, 'Iris-setosa')
species2 = getFlowerDataset(data, 'Iris-versicolor')
species3 = getFlowerDataset(data, 'Iris-virginica')

flowersets = []

flowersets.append(species1)
flowersets.append(species2)
flowersets.append(species3)
flowersets.append(data)

calc_rows = []

for set in flowersets:
    rows = []
    rows.append(calc_max(set))
    rows.append(calc_min(set))
    rows.append(calc_mean(set))
    rows.append(calc_standard_deviation(set))
    
    calc_rows.append(rows)

flower_words = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica', 'Total']
words = ['max \t\t|', 'min \t\t|', 'mean \t\t|', 'stand. dev. \t|']
first_row = "Attributes \t| sepal length \t| sepal width \t| petal length \t| petal width"

for i in range(len(flowersets)):
    print(flower_words[i])
    print(first_row)
    for x in range(len(calc_rows[i])):
        print(words[x],"\t\t| ".join(map(str, calc_rows[i][x])))  
    print("\n")
