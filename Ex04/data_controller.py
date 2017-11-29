'''
Interacts with the data sources inside /data
'''


import numpy as np
import pandas as pd

DATA_FOLDER = 'data/'

def get_terrain_data():
    return np.memmap(DATA_FOLDER + 'HGTdata.bin', dtype='>f', shape=(500, 500))

def get_terrain_data2():
    # Create a dtype with the binary data format and the desired column names
    dt = np.dtype('f8', 'f8', 'f8')
    data = np.fromfile('data/HGTdata.bin', dtype=dt)
    df = pd.DataFrame(data.tolist(), columns=data.dtype.names)
    return df

def read_data(datatype, hour):
    # formating the hour input to string and format '##'
    str_hour = str(hour)
    
    if hour < 10:
        str_hour = '0' + str_hour

    filename = DATA_FOLDER + datatype + 'f' + str_hour + '.bin'
    return np.memmap(filename, dtype=">f", mode="r", shape=(500, 500, 100), order='F')