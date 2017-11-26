Data Visualisation
HS 17
University of Zurich
Exercise 3

Nik Zaugg
12-716-734

##################################
# Files
##################################
file: func.py
Contains many functions which I implemented to use in different tasks. 
They are gathered there for reusability.

It is imported with ' import func as f '

##################################
# How to run
##################################
Python: version 3.6.2

Libraries
- numpy
- math
- csv
- random
- operator
- bokeh

Execute single python file from command line to see result:
    e.g.: 'python task1.py'

Execute main.py to execute all tasks
    e.g.: 'python main.py'


##################################
# Answers to Exercise Questions
##################################

Task 1
# Question 1: What type of variables has the Iris dataset? Refer the type of each variable.
    sepal_length: Is an ordinal variable which is continuous and ordinal.
    sepal_width: Is an ordinal variable which is continuous and ordinal.
    petal_length: Is an ordinal variable which is continuous and ordinal.
    petal_width: Is an ordinal variable which is continuous and ordinal.
    species: Is a nominal variable and categorical.

# Question 2: How many features are included in the Iris dataset? Which are they?
    If the attributes are considered as features, then the dataset contains four features.
    If the plot of the dataset is considered, then it has three features x & y coordinate and the color of the circle


Task 3
# Question 3: Compare the clustering results with the original labelling. What do you notice from the comparison?

    The training data is very good. We get accuracy of over 90%, mostly > 95%. 

    If the testInstance is of class Iris-setosa, then it is classified correctly as the datapoints of Iris-setosa are closely clustered. Wrongly classified data points occur between Iris-virginica and Iris-versicolor.


Task 4
    Iris-setosa
    Attributes      | sepal length  | sepal width   | petal length  | petal width
    max             | 5.8           | 4.4           | 1.9           | 0.6
    min             | 4.3           | 2.3           | 1.0           | 0.1
    mean            | 5.01          | 3.42          | 1.46          | 0.24
    stand. dev.     | 0.35          | 0.38          | 0.17          | 0.11


    Iris-versicolor
    Attributes      | sepal length  | sepal width   | petal length  | petal width
    max             | 7.0           | 3.4           | 5.1           | 1.8
    min             | 4.9           | 2.0           | 3.0           | 1.0
    mean            | 5.94          | 2.77          | 4.26          | 1.33
    stand. dev.     | 0.51          | 0.31          | 0.47          | 0.2


    Iris-virginica
    Attributes      | sepal length  | sepal width   | petal length  | petal width
    max             | 7.9           | 3.8           | 6.9           | 2.5
    min             | 4.9           | 2.2           | 4.5           | 1.4
    mean            | 6.6           | 2.97          | 5.56          | 2.03
    stand. dev.     | 0.63          | 0.32          | 0.55          | 0.27


    Total
    Attributes      | sepal length  | sepal width   | petal length  | petal width
    max             | 7.9           | 4.4           | 6.9           | 2.5
    min             | 4.3           | 2.0           | 1.0           | 0.1
    mean            | 5.84          | 3.05          | 3.76          | 1.2
    stand. dev.     | 0.83          | 0.43          | 1.76          | 0.76


Task 5
# Question 4: What should we do in order to avoid such kind of problems?

    The normalization of all values to the interval [0, 1] would allow to compare variables that were originally unrelated.


Task 6
# Question 5: Which class presents higher correlation? How much is it?

    Intraclass correlations are:

    Iris-setosa
    Intraclass correlation: ->  0.747  <-
    ------------------------------

    Iris-versicolor
    Intraclass correlation: ->  0.526  <-
    ------------------------------

    Iris-virginica
    Intraclass correlation: ->  0.465  <-

    Iris-setosa cluster has the highest intraclass correlation.


Task 7
# Question 6: Which cluster presents the highest similarity and which one the highest dis-similarity
per attribute? How similar (dis-similar) are they?

    SIMILARITIES AND DISSIMILARITIES BETWEEN CLUSTERS
    Iris-setosa vs. Iris-versicolor
    Similarity      |  0.2378
    Dissimilarity   |  3.2052


    Iris-setosa vs. Iris-virginica
    Similarity      |  0.1738
    Dissimilarity   |  4.7526


    Iris-versicolor vs. Iris-virginica
    Similarity      |  0.3816
    Dissimilarity   |  1.6205


    - Hightest similarity between cluster Iris-versicolor and Iris-virginica
    - Hightest dissimilarity between cluster Iris-setosa and Iris-virginica

