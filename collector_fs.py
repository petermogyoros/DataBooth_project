from fruitshoot.models import FruitShoot_table
import os, fnmatch
import time
import traceback


import pandas as pd
from pandas import DataFrame
# import numpy as np
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
        # conditional statements are needed for the difference in the inspection tools between the two cameras
        # In september Line 13 was updated to have two inspections for the spout check (spout_top and spout_side)
        # however, line 15 has not been updated with this tool.
# assign dataframe values to variables
        if key_list[12] == " Spout Top":
            date = str(to_dataframe.iloc[0])
            product = str(to_dataframe.iloc[1]).split("\n")[0][10:]  # clean up product name
            pass_ = int(to_dataframe.iloc[2])
            reject = int(to_dataframe.iloc[3])
            search = int(to_dataframe.iloc[4])
            remap = int(to_dataframe.iloc[5])
            idv = int(to_dataframe.iloc[6])
            dimension = int(to_dataframe.iloc[7])
            dc_top_view = int(to_dataframe.iloc[8])
            cap_inner = int(to_dataframe.iloc[9])
            te_band = int(to_dataframe.iloc[10])
            knurling = int(to_dataframe.iloc[11])
            spout_top = int(to_dataframe.iloc[12])
            spout_side = int(to_dataframe.iloc[13])
            dc_ring = int(to_dataframe.iloc[14])
            dc_blob = int(to_dataframe.iloc[15])
            measure_height = int(to_dataframe.iloc[16])
            spout = -1


        elif key_list[12] == " Spout":
            date = str(to_dataframe.iloc[0])
            product = str(to_dataframe.iloc[1]).split("\n")[0][10:]  # clean up product name
            pass_ = int(to_dataframe.iloc[2])
            reject = int(to_dataframe.iloc[3])
            search = int(to_dataframe.iloc[4])
            remap = int(to_dataframe.iloc[5])
            idv = int(to_dataframe.iloc[6])
            dimension = int(to_dataframe.iloc[7])
            dc_top_view = int(to_dataframe.iloc[8])
            cap_inner = int(to_dataframe.iloc[9])
            te_band = int(to_dataframe.iloc[10])
            knurling = int(to_dataframe.iloc[11])
            spout_top = -1
            spout_side = -1
            dc_ring = int(to_dataframe.iloc[13])
            dc_blob = int(to_dataframe.iloc[14])
            measure_height = int(to_dataframe.iloc[15])
            spout = int(to_dataframe.iloc[12])

        # update key_list to add spout=-1, as this value was not present in the .csv
        key_list = ['date', 'product', 'pass_', 'reject', 'search', 'remap', 'idv', 'dimension', 'dc_top_view', 'cap_inner',
       'te_band', 'knurling', 'spout_top', 'spout_side', 'dc_ring', 'dc_blob', 'measure_height', 'spout']
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
        list_of_results.append(dimension)
        list_of_results.append(dc_top_view)
        list_of_results.append(cap_inner)
        list_of_results.append(te_band)
        list_of_results.append(knurling)
        list_of_results.append(spout_top)
        list_of_results.append(spout_side)
        list_of_results.append(dc_ring)
        list_of_results.append(dc_blob)
        list_of_results.append(measure_height)
        list_of_results.append(spout)

        return list_of_results

    def update_db(line, list_of_results):
        db_update = FruitShoot_table(
        production_line = line,
        csv_datetime = list_of_results[0],
        program = list_of_results[1],
        ok_caps = list_of_results[2],
        rejects_overal = list_of_results[3],
        reject_search = list_of_results[4],
        reject_remap = list_of_results[5],
        reject_idv = list_of_results[6],
        reject_dimension = list_of_results[7],
        reject_dc_top_view = list_of_results[8],
        reject_cap_inner = list_of_results[9],
        reject_te_band = list_of_results[10],
        reject_body = list_of_results[11],
        reject_spout_top = list_of_results[12],
        reject_spout_side = list_of_results[13],
        reject_dc_ring = list_of_results[14],
        reject_dc_blob = list_of_results[15],
        reject_short_spout = list_of_results[16],
        product = "Fruit Shoot",
        production_site = "Eaton Socon",
        spout = list_of_results[17])

        db_update.save()

    working_directory = '/home/peter/DataBooth_project'

    # assign directories for each line option
    if line == 15:
        csv_working_directory = '/home/peter/csv/ES_FL1'
        new_location = '/home/peter/csv/ES_FL1/%s'

    elif line == 13:
        csv_working_directory = '/home/peter/csv/ES_FL2'
        new_location = '/home/peter/csv/ES_FL2/%s'

    # list through each file in the working_directory
    log_folder = os.listdir(csv_working_directory)
    pattern = '*.csv' # choose search pater
    for entry in log_folder:

        # only find files with the .csv extention
        if fnmatch.fnmatch(entry, pattern):
            os.chdir(csv_working_directory)  # Change working directory to log_folder to be able to ready cvs files
            print("Working on line: ",line, " file: " entry)
        # read csv into "i2s" then close the original document
            with open(entry, "r") as opened_csv:
                read_csv = opened_csv.read()

            list_of_results = []
            clean_csv_and_return_list(list_of_results, read_csv)

            if bool(list_of_results) is True:
                update_db(line, list_of_results)

            else:
                print("Empty list - PROBLEM IN CODE")


            move_to = (new_location %(entry))
            os.rename(entry, move_to)

            # change back working directory to where collector.py is located
            os.chdir(working_directory)

            time.sleep(0.2)

def check_machine_folder(line):
    try:
        process_data(line)
    except:
        pass


# searches for csv and updates database
class Collector():
    while_counter = 0
    while True:
        while_counter += 1

        # add machine here to update database
        check_machine_folder(15)
        check_machine_folder(13)
        time.sleep(5)
        if while_counter == 2:
            quit()
