from src.data_frame import data_frame
from src.median import median

if __name__ == '__main__':
    sample = list(map(int, input("please enter the sample value").split(" ")))
    print(median(sample))
    path = input("please enter the csv file path")
    print(data_frame(path))
