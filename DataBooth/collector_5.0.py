import pandas as pd
from pandas import Series, DataFrame
import datetime
import psycopg2 #postgres library
import os, fnmatch
import time

line = 8
# 72 cavity stack tool only. Change funcion names for other tool designs
log_folder = os.listdir('C:\\Users\mogyorosp\Documents\GitHub\DataBooth_project\DataBooth')
pattern = '*.csv' # choose search pater
new_location = 'C:\\Users\mogyorosp\Documents\GitHub\DataBooth_project\DataBooth\csv_backup/%s'

def create_connection():
    conn = psycopg2.connect("dbname='webserver1db' user='postgres' host='localhost' password='DolceGusto'")
    return conn


def get_values_72_imp_stack_tool(csv1, list_of_results):
    #convert time and date from csv format to seconds for easier handling
    date = csv1.loc[[1], 'Date']
    time_ = csv1.loc[[1], 'Time']
    str_date = str(date)
    str_time = str(time_)
    year = int(str_date[5:9])
    month = int(str_date[10:12])
    day = int(str_date[13:15])
    hour = int(str_time[5:7])
    minute = int(str_time[8:10])
    t = datetime.datetime(year, month, day, hour, minute)
    raw_time = (t-datetime.datetime(1970,1,1)).total_seconds() #this is the time in seconds (epoch time)
    raw_time = int(raw_time)

    # extracting data from *.cvs into Series
    batch = int(csv1.loc[[1], 'Total'])
    ok = csv1.loc[[148, 296], 'OK']
    rejects = csv1.loc[[148, 296, 149, 297, 150, 298, 151, 299], 'Reject']
    recycles = csv1.loc[[148, 296, 149, 297, 150, 298, 151, 299], 'Recycle']

    # converting Series to dict
    ok_dict_raw = ok.to_dict()
    reject_dict_raw = rejects.to_dict()
    recycle_dict_raw = recycles.to_dict()

    # assigning descriptive dictionary keys
    ok_dict_keys = {148:"side_b", 296:"side_a"}
    ng_dict_keys = {148:"combined_side_b_ng", 296:"combined_side_a_ng", 149:"top_b", 297:"top_a", 150:"bottom_b", 298:"bottom_a", 151:"side_b", 299:"side_a"}
    re_dict_keys = {148:"combined_side_b_re", 296:"combined_side_a_re", 149:"top_b", 297:"top_a", 150:"bottom_b", 298:"bottom_a", 151:"side_b", 299:"side_a"}


    ok_dict = dict((ok_dict_keys[key], int(value)) for (key, value) in ok_dict_raw.items())
    reject_dict = dict((ng_dict_keys[key], int(value)) for (key, value) in reject_dict_raw.items())
    recycle_dict = dict((re_dict_keys[key], int(value)) for (key, value) in recycle_dict_raw.items())

    list_of_results.append(ok_dict)
    list_of_results.append(reject_dict)
    list_of_results.append(recycle_dict)
    list_of_results.append(raw_time)
    list_of_results.append(batch)

    return list_of_results

def update_db_72_imp_stack_tool(list_of_results, line):

    #update db
    ok_dict = list_of_results[0]
    reject_dict = list_of_results[1]
    recycle_dict = list_of_results[2]
    raw_time = list_of_results[3]
    batch = list_of_results[4]

    conn = create_connection()
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS public.dolcegusto_values_in_db(

    raw_time integer NOT NULL,
    line integer NOT NULL,
    batch integer,
    a_ok integer,
    b_ok integer,
    combined_side_a_ng integer,
    combined_side_b_ng integer,
    a_top_ng integer,
    b_top_ng integer,
    a_bottom_ng integer,
    b_bottom_ng integer,
    a_side_ng integer,
    b_side_ng integer,
    combined_side_a_re integer,
    combined_side_b_re integer,
    a_top_re integer,
    b_top_re integer,
    a_bottom_re integer,
    b_bottom_re integer,
    a_side_re integer,
    b_side_re integer
    )''')

    cur.execute('''INSERT INTO public.dolcegusto_values_in_db(raw_time, Line, Batch,
     A_OK, B_OK,
     Combined_Side_A_NG, Combined_Side_B_NG,
     A_Top_NG, B_Top_NG,
     A_Bottom_NG, B_Bottom_NG,
     A_Side_NG, B_Side_NG,
     Combined_Side_A_RE, Combined_Side_B_RE,
     A_Top_Re, B_Top_Re,
     A_Bottom_Re, B_Bottom_Re,
     A_Side_Re, B_Side_Re)
    VALUES (%s, %s, %s,
    %s, %s,
    %s, %s,
    %s, %s,
    %s, %s,
    %s, %s,
    %s, %s,
    %s, %s,
    %s, %s,
    %s, %s)''',
    (raw_time, line, batch,
    int(ok_dict["side_a"]), int(ok_dict["side_b"]),
    int(reject_dict["combined_side_a_ng"]), int(reject_dict["combined_side_b_ng"]),
    int(reject_dict["top_a"]), int(reject_dict["top_b"]),
    int(reject_dict["bottom_a"]), int(reject_dict["bottom_b"]),
    int(reject_dict["side_a"]), int(reject_dict["side_b"]),
    int(recycle_dict["combined_side_a_re"]), int(recycle_dict["combined_side_b_re"]),
    int(recycle_dict["top_a"]), int(recycle_dict["top_b"]),
    int(recycle_dict["bottom_a"]), int(recycle_dict["bottom_b"]),
    int(recycle_dict["side_a"]), int(recycle_dict["side_b"])))

    conn.commit()
    cur.close()


counter = 0

list_of_results = []

for entry in log_folder:
    if fnmatch.fnmatch(entry, pattern):
        csv1 = pd.read_csv(entry, index_col=False) # returns a DataFrame
        # Determine tool cavitation number
        if int(csv1.loc[[149], 'Cavity']) < 0: #72 cavity tool
            list_of_results = []
            get_values_72_imp_stack_tool(csv1, list_of_results)

            if bool(list_of_results) is True:
                update_db_72_imp_stack_tool(list_of_results, line)
            else:
                print("Empty list - PROBLEM IN CODE")

        else:
            print("wrong file type")

        move_to = (new_location %(entry))
        os.rename(entry, move_to)
        counter += 1
        print(counter, 'files processed')

        time.sleep(0.1)
