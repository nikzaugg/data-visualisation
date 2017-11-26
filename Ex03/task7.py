'''
Data Visualization
Exercise 03
Task 7
Author: Nik Zaugg
Student Number: 12-716-734

Compute the interclass similarity and dis-similarity of points per attribute for each cluster of irises
flowers. Select as a distance measure either the Euclidean or the Manhattan distance. The
similarity and dis-similarity results should be presented automatically when running the code.
'''


import func as f
import math

def interclass_mean_distance(class1, class2, round_result):
    '''
    Compute the mean distance between two classes

    Args:
        class1, class2: datasets to evaluate
    Return:
        distance: mean distance between two classes based on euclidean distance
    '''
    intermediate = 0

    for i in range(len(class1)):
        intermediate += math.pow(class1[i] - class2[i],2)

    distance = math.sqrt(intermediate)

    if round_result:
        return round(distance, 4)
    else:
        return distance

def interclass_similarity(class1, class2):
    '''
    Compute the similarity between two classes

    Args:
        class1, class2: datasets to evaluate
    Return:
        similarity between the two classes (float)
    '''
    distance = interclass_mean_distance(class1, class2, False)
    return round(1/(distance+1), 4)

# load all datasets
data = f.loadDataSet('iris.data')
setosa = f.getFlowerDataset(data, 'Iris-setosa')
versicolor = f.getFlowerDataset(data, 'Iris-versicolor')
virginica = f.getFlowerDataset(data, 'Iris-virginica')

# calculate means
setosa_mean = f.calc_mean(setosa, False)
versicolor_mean = f.calc_mean(versicolor, False)
virginica_mean = f.calc_mean(virginica, False)

# print results
print("TASK 7")
print("--------------------")
print("SIMILARITIES AND DISSIMILARITIES BETWEEN CLUSTERS")
print("Iris-setosa vs. Iris-versicolor")
print("Similarity \t| ", interclass_similarity(setosa_mean, versicolor_mean))
print("Dissimilarity \t| ", interclass_mean_distance(setosa_mean, versicolor_mean, True))
print("\n")
print("Iris-setosa vs. Iris-virginica")
print("Similarity \t| ", interclass_similarity(setosa_mean, virginica_mean))
print("Dissimilarity \t| ", interclass_mean_distance(setosa_mean, virginica_mean, True))
print("\n")
print("Iris-versicolor vs. Iris-virginica")
print("Similarity \t| ", (interclass_similarity(versicolor_mean, virginica_mean)))
print("Dissimilarity \t| ", interclass_mean_distance(versicolor_mean, virginica_mean, True))

print("\n")
print("- Hightest similarity between cluster Iris-versicolor and Iris-virginica")
print("- Hightest dissimilarity between cluster Iris-setosa and Iris-virginica")





