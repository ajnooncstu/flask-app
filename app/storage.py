import os

def ensure_data_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
