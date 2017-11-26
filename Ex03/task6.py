'''
Data Visualization
Exercise 03
Task 6
Author: Nik Zaugg
Student Number: 12-716-734


Compute the interclass correlation of sepal length vs. sepal width for each cluster of irises
flowers. You can use either the Pearson or any other suitable correlation coefficient for this
computation. The correlation coefficients for each cluster should be presented automatically
when running the code.

Assumption: there are three clusters, namely Iris-setosa, Iris-versicolor, Iris-virginica
'''
import math
import func as f
import numpy as np

def pearson_correlation(data):
    '''
    Calculate the pearson correlation coefficient

    Args:
        data: dataset to evaluate
    Return:
        the pearson correlation coefficient of the dataset
    '''

    cov = calc_covariance(data)
    sd_x, sd_y = calc_standard_deviation(data)
    
    return cov / (sd_x * sd_y)

def calc_covariance(data):
    '''
    Calculate the covariance of a provided dataset

    Args:
        data: data set to evaluate
    Return:
        covariance: covariance of dataset
    '''
    x_values = data[:,0]
    y_values = data[:,1]
    mean_x = get_mean(x_values)
    mean_y = get_mean(y_values)
    length = len(data[:,0])

    covariance = 0

    for i in range(length):
        covariance += (float(x_values[i] - mean_x) * float(y_values[i]-mean_y))
    
    covariance = 1/length * covariance

    return covariance

def get_mean(data):
    '''
    Calculate the mean of a provided dataset

    Args:
        data: data set to evaluate
    Return:
        mean: mean of the dataset
    '''
    data_length = len(data)
    data_sum = get_sum(data)
    
    return data_sum / data_length

def get_sum(data):
    '''
    Calculate sum of a provided dataset

    Args:
        data: data set to evaluate
    Return:
        sum: sum of the dataset
    '''
    sum = 0
    length = len(data)
    
    for i in range(length):
        sum += float(data[i])
    
    return sum


def calc_standard_deviation(data):
    '''
    Calculate standard deviation of the dataset according to its (x,y) pairs

    Args:
        data: data set to evaluate
    Return:
        sd_x: standard deviation of x values
        sd_y: standard deviation of y values
    '''
    x_values = data[:,0]
    y_values = data[:,1]

    # get mean of x and y values
    mean_x = get_mean(x_values)
    mean_y = get_mean(y_values)
    length = len(x_values)

    squared_x = 0 
    squared_y = 0

    for i in range(length):
        squared_x += (float(x_values[i]-mean_x)**2)
    
    for i in range(length):
        squared_y += (float(y_values[i]-mean_y)**2)

    sd_x = math.sqrt(squared_x/(length)) 
    sd_y = math.sqrt(squared_y/(length)) 

    return sd_x, sd_y


def display_pearson_correlation(setosa_pearson_correlation, versicolor_pearson_correlation, virginica_pearson_correlation):
    '''
    Print pearson correlation coefficients to the console
    '''
    
    correlations = []
    correlations.append(setosa_pearson_correlation)
    correlations.append(versicolor_pearson_correlation)
    correlations.append(virginica_pearson_correlation)

    flower_names = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    print("TASK 6")
    print("--------------------")
    print('Intraclass correlation of sepal length vs. sepal width for each cluster of irises flowers \n')

    for i in range(len(flower_names)):
        print(flower_names[i])
        print('Intraclass correlation: -> ',round(correlations[i],3), ' <-')
        print(30*'-')
        print('\n')
        
################
# Main Program #
################

# Load all data sets
data = f.loadDataSet('iris.data')
setosa = f.getFlowerDataset(data, 'Iris-setosa')
versicolor = f.getFlowerDataset(data, 'Iris-versicolor')
virginica = f.getFlowerDataset(data, 'Iris-virginica')

# setosa values and pearson correlation coefficient
setosa_array = np.array(setosa)
setosa_sepal = setosa_array[:,:-3]
setosa_sepal = np.array(setosa_sepal, dtype=float)
setosa_pearson_correlation = pearson_correlation(setosa_sepal)

# versicolor values and pearson correlation coefficient
versicolor_array = np.array(versicolor)
versicolor_sepal = versicolor_array[:,:-3]
versicolor_sepal = np.array(versicolor_sepal, dtype=float)
versicolor_pearson_correlation = pearson_correlation(versicolor_sepal)

# virginica values and pearson correlation coefficient
virginica_array = np.array(virginica)
virginica_sepal = virginica_array[:,:-3]
virginica_sepal = np.array(virginica_sepal, dtype=float)
virginica_pearson_correlation = pearson_correlation(virginica_sepal)

# display results
display_pearson_correlation(setosa_pearson_correlation, versicolor_pearson_correlation, virginica_pearson_correlation)


