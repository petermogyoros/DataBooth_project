from secure_flip_i2s.models import SecureFlip_I2S_table
import os, fnmatch
import time
import traceback
import pandas as pd
from pandas import DataFrame
from datetime import datetime

def process_data(line):
    def clean_csv_and_return_list(list_of_results, read_csv):
        # remove empty spaces from between the charachters
        c = -1
        decoded_from_csv = ""

        for i in read_csv:
            c += 1
            y = c%2  # odd/even number calculation

            if y == 0:  # check if number is an even number
                decoded_from_csv = decoded_from_csv + i
            else:
                pass

        # remove empty strings from the list
        to_list = decoded_from_csv.split(",")
        try:
            while True:
                to_list.remove("")

        except:
            pass

        del to_list[-1]  # delete the last string in the list, which was /n
        del to_list[2]  # delete an unimportant value "Shift"

        x = -1
        key_list = []
        value_list = []

        for t in to_list:
            x += 1
            if (x%2) == 0:
                key_list.append(t)
            else:
                value_list.append(t)

        # create dataframe from the list
        to_dataframe = DataFrame(value_list, key_list)
        to_dataframe.columns = ["values"]  # assign column name for easy reading

        # assign dataframe values to variables
        date = str(to_dataframe.iloc[0])
        product = str(to_dataframe.iloc[1]).split("\n")[0][10:]  # clean up product name
        pass_ = int(to_dataframe.iloc[2])
        reject = int(to_dataframe.iloc[3])
        search = int(to_dataframe.iloc[4])
        remap = int(to_dataframe.iloc[5])
        idv = int(to_dataframe.iloc[6])
        spout_top = int(to_dataframe.iloc[7])
        cap_top = int(to_dataframe.iloc[8])
        seal_side = int(to_dataframe.iloc[9])
        dc_side = int(to_dataframe.iloc[10])
        cap_side = int(to_dataframe.iloc[11])
        measure_slit = int(to_dataframe.iloc[12])

        # Convert csv month name to month number string and save it to "month"
        if date[14:17] == "Jan":
            month = "01"
        elif date[14:17] == "Feb":
            month = "02"
        elif date[14:17] == "Mar":
            month = "03"
        elif date[14:17] == "Apr":
            month = "04"
        elif date[14:17] == "May":
            month = "05"
        elif date[14:17] == "Jun":
            month = "06"
        elif date[14:17] == "Jul":
            month = "07"
        elif date[14:17] == "Aug":
            month = "08"
        elif date[14:17] == "Sep":
            month = "09"
        elif date[14:17] == "Oct":
            month = "10"
        elif date[14:17] == "Nov":
            month = "11"
        elif date[14:17] == "Dec":
            month = "12"

        # create datetime from variable date
        datetime_list = []

        year = date[30:34]
        day = date[18:20]
        time_ = date[21:29]

        datetime_list.append(year)
        datetime_list.append("-")
        datetime_list.append(month)
        datetime_list.append("-")
        datetime_list.append(day)
        datetime_list.append(" ")
        datetime_list.append(time_)

        # join strings to create date string
        datetime_str = ''.join(datetime_list)
        # create a datetime format from the date string
        datetime_value = datetime.strptime(datetime_str,'%Y-%m-%d %H:%M:%S')

        list_of_results.append(datetime_value)
        list_of_results.append(product)
        list_of_results.append(pass_)
        list_of_results.append(reject)
        list_of_results.append(search)
        list_of_results.append(remap)
        list_of_results.append(idv)
        list_of_results.append(spout_top)
        list_of_results.append(cap_top)
        list_of_results.append(seal_side)
        list_of_results.append(dc_side)
        list_of_results.append(cap_side)
        list_of_results.append(measure_slit)

        return list_of_results

    def update_db(line, list_of_results):

        db_update = SecureFlip_I2S_table(
        production_line = line,
        csv_datetime = list_of_results[0],
        program = list_of_results[1],
        ok_caps = list_of_results[2],
        rejects_overal = list_of_results[3],
        reject_search = list_of_results[4],
        reject_remap = list_of_results[5],
        reject_idv = list_of_results[6],
        reject_spout_top = list_of_results[7],
        reject_cap_top = list_of_results[8],
        reject_seal_side = list_of_results[9],
        reject_dc_side = list_of_results[10],
        reject_cap_side = list_of_results[11],
        reject_measure_slit = list_of_results[12],

        product = "SF 1881",
        production_site = "Flitwick")

        db_update.save()

    working_directory = '/home/peter/DataBooth_project'

    # assign directories for each line option
    if line == 1:
        csv_working_directory = '/home/peter/csv/FL1881'
        new_location = '/home/peter/csv/FL1881/processed/%s'
        failed_location = '/home/peter/csv/FL1881/failed/%s'


    # list through each file in the working_directory
    log_folder = os.listdir(csv_working_directory)
    pattern = '*.csv' # choose search pater
    for entry in log_folder:

        # only find files with the .csv extention
        if fnmatch.fnmatch(entry, pattern):
            os.chdir(csv_working_directory)  # Change working directory to log_folder to be able to ready cvs files
            print("Working on line: ",line, " file: ", entry)
        # read csv into "i2s" then close the original document
            with open(entry, "r") as opened_csv:
                read_csv = opened_csv.read()

            list_of_results = []

            # some .csv file are irregular and will crash the program
            # these will be storred in ~/csv/ES#/failed
            # for further analysis
            # try:
            clean_csv_and_return_list(list_of_results, read_csv)

          #  if bool(list_of_results) is True:
            update_db(line, list_of_results)

            move_to = (new_location %(entry))
            os.rename(entry, move_to)
            print("Success")

            # except:
            move_to = (failed_location %(entry))
            os.rename(entry, move_to)
            print("File Failed to Process. Moved to 'failed' folder")

            # change back working directory to where collector.py is located
            os.chdir(working_directory)

            time.sleep(0.1)

def check_machine_folder(line):
    # try:
    process_data(line)
    # except:
    #     pass


# searches for csv and updates database
class Collector():
    while_counter = 0
    while True:
        while_counter += 1

        # add machine here to update database
        check_machine_folder(1)

        time.sleep(5)
        if while_counter == 2:
            quit()
