'''
Interacts with the data sources inside /data
'''


import numpy as np
import pandas as pd

DATA_FOLDER = 'data/'

def get_terrain_data():
    return np.memmap(DATA_FOLDER + 'HGTdata.bin', dtype='>f', shape=(500, 500))

def read_data(datatype, hour):
    # formating the hour input to string and format '##'
    str_hour = str(hour)
    
    if hour < 10:
        str_hour = '0' + str_hour

    filename = DATA_FOLDER + datatype + 'f' + str_hour + '.bin'
    return np.memmap(filename, dtype=">f", shape=(500, 500, 100), order='F')