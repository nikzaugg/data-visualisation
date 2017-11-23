'''
Using the original dataset compute the total and the intraclass minimum, maximum, mean and
standard deviation of each attribute. The results should be presented automatically when running
the code. 
'''

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
    sum = [0,0,0,0]
    min = [0,0,0,0]
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
    print(sum)
    return sum


def calc_mean(data):
    sum = calc_sum(data)
    print(sum)
    mean = [0,0,0,0]
    # get mean
    for i in range(len(data[0]) - 1):
        mean[i] = round(sum[i] / len(data), 2)
    return mean


def standard_deviation(data):
    from math import sqrt
    intermediate = [0,0,0,0]
    sd = [0,0,0,0]

    for i in range(len(data)):
        for j in range(len(data[0]) - 1):
            intermediate[j] += (float(data[i][j]) - intermediate[j])**2
    
    for j in range(len(data[0]) - 1):
        sd[j] = round(sqrt(1/len(data) * sd[j]), 2)

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

print(calc_mean(species1))