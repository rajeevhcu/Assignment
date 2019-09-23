from src import logger
from src.data_frame import data_frame
from src.median import median

log = logger.get_logger("main")
if __name__ == '__main__':
    sample = list(map(int, input("please enter the sample value").split(" ")))
    log.info("median : %d" % median(sample))
    path = input("please enter the csv file path")
    log.info("data frame return value : %s" % data_frame(path))
