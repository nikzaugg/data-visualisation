'''
Data Visualization
Exercise 03
Task 4
Author: Nik Zaugg
Student Number: 12-716-734


Using the original dataset compute the total and the intraclass minimum, maximum, mean and
standard deviation of each attribute. The results should be presented automatically when running
the code.
'''

import numpy as np
import func as f

# Load all datasets
data = f.loadDataSet('iris.data')
species1 = f.getFlowerDataset(data, 'Iris-setosa')
species2 = f.getFlowerDataset(data, 'Iris-versicolor')
species3 = f.getFlowerDataset(data, 'Iris-virginica')

flowersets = []

flowersets.append(species1)
flowersets.append(species2)
flowersets.append(species3)
flowersets.append(data)

calc_rows = []

# Compute statistical data of the flower sets
for set in flowersets:
    rows = []
    rows.append(f.calc_max(set, True))
    rows.append(f.calc_min(set, True))
    rows.append(f.calc_mean(set, True))
    rows.append(f.calc_standard_deviation(set, True))

    calc_rows.append(rows)

flower_words = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica', 'Total']
words = ['max \t\t|', 'min \t\t|', 'mean \t\t|', 'stand. dev. \t|']
first_row = "Attributes \t| sepal length \t| sepal width \t| petal length \t| petal width"

print(calc_rows)

print("TASK 4")
print("--------------------")
for i in range(len(flowersets)):
    print(flower_words[i])
    print(first_row)
    for x in range(len(calc_rows[i])):
        print(words[x],"\t\t| ".join(map(str, calc_rows[i][x])))  
    print("\n")
