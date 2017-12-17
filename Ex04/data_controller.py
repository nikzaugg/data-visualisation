# Data Visualisation
# University of Zurich
# Exercise 4
# Nik Zaugg
# 12-716-734

'''
Interacts with the data sources inside /data
'''

import numpy as np
import pandas as pd

DATA_FOLDER = 'data/'

def get_terrain_data():
    '''
    Load the terrain data of the dataset provided at http://vis.computer.org/vis2004contest/data.html
    '''
    return np.memmap(DATA_FOLDER + 'HGTdata.bin', dtype='>f', shape=(500, 500))

def read_data(datatype, hour):
    '''
    Load the corresponding variable of the dataset provied at http://vis.computer.org/vis2004contest/data.html

    Arguments:
    - datatype (string)
    - hour (int)

    Return:
    - np.memmap: data is mapped to the memory and can be accessed without loading the whole dataset each time
    '''

    hour_as_string = str(hour)
    
    if hour < 10:
        hour_as_string = '0' + hour_as_string

    file_name = DATA_FOLDER + datatype + 'f' + hour_as_string + '.bin'
    return np.memmap(file_name, dtype=">f", shape=(500, 500, 100), order='F')