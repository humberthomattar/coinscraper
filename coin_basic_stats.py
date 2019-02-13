import sys
import os
import pandas as pd

path_data_file = 'data_historical/'
path_data_basicstats = 'data_basicstats/'
file_name_pattern = 'csv'


def get_files(path_data_file, file_name_pattern):
    import glob
    return glob.glob(path_data_file + '*.' + file_name_pattern)

def get_currency(file_path):
    return  os.path.basename(os.path.splitext(file_path)[0])

def file_to_dataframe(file):
    return pd.read_csv(os.path.basename(file))

def main():
    files = get_files(path_data_file, file_name_pattern)
    for file in files:
        df = file_to_dataframe(file)
        currency = get_currency(file)
        df.describe().to_csv('data_basicstats/' + currency + '.csv')

if __name__ == '__main__':
    sys.exit(main())