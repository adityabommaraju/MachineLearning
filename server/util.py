import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(longitude, latitude, housing_median_age,
                        households, median_income):
    # try:
    #     loc_index = __data_columns.index(location.lower())
    # except:
    #     loc_index = -1

    x = np.zeros(len(__data_columns))
    print(len(__data_columns))
    x[0] = longitude
    x[1] = latitude
    x[2] = housing_median_age
    x[3] = households
    x[4] = median_income
    x[5] = 1
    x[6] = 0
    x[7] = 0
    x[8] = 0
    x[9] = 0

    print([x])
    return np.round(__model.predict([x][0]), 2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("C:/Users/029338502/MachineLearning/artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        # __locations = __data_columns[0:4]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('C:/Users/029338502/MachineLearning/artifacts/house_value_prediction_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


# def get_location_names():
#     return __locations


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    # print(get_location_names())
    print(get_estimated_price(-122.230, 37.880, 41.000, 126.000,8.325,1,0,0,0,0))
    # print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    # print(get_estimated_price('Kalhalli', 1000, 2, 2))  # other location
    # print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location
