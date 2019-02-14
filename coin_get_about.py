import os
import sys
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

path_data_file = 'data_historical/'
file_name_pattern = '.csv'

def get_files(path_data_file, file_name_pattern):
    import glob
    return glob.glob(path_data_file + '*' + file_name_pattern)

def get_currency(file_path):
    return  os.path.basename(os.path.splitext(file_path)[0])

def download_data_by_currency (currency):
    try:
        time.sleep(2)
        url = 'https://coinmarketcap.com/currencies/' + currency + '/historical-data/'
        r = requests.get(url)
        print(currency + ' - ' + str(r.status_code))
        html_page = r.text
        soup = BeautifulSoup(html_page, features="lxml")
        data = soup.find_all('div',attrs={'class' : 'col-sm-8'})
        if (data):            
           return data[0].text.replace('\n', '')
        else:
            return None
    except Exception as e:
        print("Error : Could not Download - " + currency)
        print(e)

def main():
    files = get_files(path_data_file, file_name_pattern)
    about_currencies = {}
    for file in files:
        try:
            currency = get_currency(file)
            about_currencies[currency] = download_data_by_currency(currency)
        except Exception as e:
            print(e)
    df = pd.DataFrame.from_dict(about_currencies, orient="index")
    df.to_csv("about_currencies.csv")

if __name__ == '__main__':
    sys.exit(main())