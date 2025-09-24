import os

def read_data(file_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, file_name)

    with open(file_path, "r") as f:
        for line in f:
            parts = [x.strip() for x in line.split(",")]
            print(parts)


read_data("data.txt")   # always looks in same folder as reader.py
