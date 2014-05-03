import os


def get_data_dir():
    currdir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(currdir, "data")
