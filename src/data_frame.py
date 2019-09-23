import pandas as pd


def data_frame(path):
    data = pd.read_csv(path)
    key = data.keys()
    type_check = [type(elem) == str for elem in data[key[1]]]
    if any(type_check):
        return None
    sum = 0
    for index in range(1, len(data[key[1]]), 2):
        sum += data[key[1]][index]
    return sum
