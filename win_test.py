# from dolcegusto.models import DolceGusto_table
import pandas as pd
from pandas import Series, DataFrame
from datetime import datetime
import os, fnmatch
import time


working_directory = 'C:\\Users\\mogyorosp\\Documents\\GitHub\\csv'

# list through each file in the working_directory
log_folder = os.listdir(working_directory)
pattern = '*.csv' # choose search pater

# copy csv to this new directory (backup)
new_location = 'C:\\Users\mogyorosp\Documents\GitHub\DataBooth_project\csv_backup/%s'



def get_data(csv1, list_of_results):
    datetime_list = []

    date_of_csv_raw = csv1.loc[[0],]
    str_date = str(date_of_csv_raw)
    year = str(str_date[40:50])
    month = str(str_date[10:12])
    day = str(str_date[13:15])


    # print(str_date)
    list_of_results.append(year)
    list_of_results.append(day)

    return list_of_results

def update_db(list_of_results, line):
    #update db
    # ok_dict = list_of_results[0]
    # reject_dict = list_of_results[1]
    # recycle_dict = list_of_results[2]
    datetime_of_csv = list_of_results[0]
    # batch = list_of_results[4]

    print(datetime_of_csv)

counter = 0

list_of_results = []

for entry in log_folder:

    if fnmatch.fnmatch(entry, pattern):
        # Change working directory to log_folder to be able to ready cvs files
        os.chdir(working_directory)

        csv1 = pd.read_csv(entry, index_col=False) # returns a DataFrame

        # Determine tool cavitation number
        list_of_results = []
        get_data(csv1, list_of_results)



        line = 1

        if bool(list_of_results) is True:
            update_db(list_of_results, line)
        else:
            print("Empty list - PROBLEM IN CODE")

    else:
        print("wrong file type")

    # move_to = (new_location %(entry))
    # os.rename(entry, move_to)

    # completion feedback after every file. Probably can be removed after testing
    counter += 1
    print(counter, entry)

    # change back working directory to where collector.py is located
    os.chdir("C:\\Users\\mogyorosp\\Documents\\GitHub\\DataBooth_project")

    time.sleep(0.1)
