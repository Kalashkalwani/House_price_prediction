import json
import pickle
import numpy as np

__loaction = None
__data_column = None
__model = None


def get_estimated_price(location,sqft,bhk,bath):

    try:
        loc_index = __data_column.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_column))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)


def get_location_name():
    return __loaction

def load_saved_artifcats():
    print("loading saved artifacts... start")
    global __data_column
    global __loaction
    global __model

    with open("./artifacts/columns.json",'r') as f:
        __data_column = json.load(f)['data_columns']
        __loaction = __data_column[3:]

    with open("./artifacts/bengaluru_house_price_pickle",'rb') as f:
        __model = pickle.load(f)

    print("loading saved artifacts... done")


if __name__ == '__main__':
    load_saved_artifcats()
    print(get_location_name())

    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('Indira Nagar',1000, 2, 2))
    print(get_estimated_price('Indira Nagar',1000, 3, 3))