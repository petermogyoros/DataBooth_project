from django.shortcuts import render
from django.views import View
import pandas as pd
from pandas import DataFrame
from datetime import datetime

from dolcegusto.models import daily_report

# assign weekday name to variable
def get_weekday(weekday_number):

    if weekday_number() == 0:
        weekday_name = "Monday"
    elif weekday_number() == 1:
        weekday_name = "Tuesday"
    elif weekday_number() == 2:
        weekday_name = "Wednesday"
    elif weekday_number() == 3:
        weekday_name = "Thursday"
    elif weekday_number() == 4:
        weekday_name = "Friday"
    elif weekday_number() == 5:
        weekday_name = "Saturday"
    elif weekday_number() == 6:
        weekday_name = "Sunday"

    return weekday_name

# assign variables from database columns
def get_value_for_machine_per_period(line):

    # reset variables
    line0_a_ng = 0
    line1_a_ng = 0
    line2_a_ng = 0
    line3_a_ng = 0
    line4_a_ng = 0
    line5_a_ng = 0
    line6_a_ng = 0

    line0_b_ng = 0
    line1_b_ng = 0
    line2_b_ng = 0
    line3_b_ng = 0
    line4_b_ng = 0
    line5_b_ng = 0
    line6_b_ng = 0

    line0_a_re = 0
    line1_a_re = 0
    line2_a_re = 0
    line3_a_re = 0
    line4_a_re = 0
    line5_a_re = 0
    line6_a_re = 0

    line0_b_re = 0
    line1_b_re = 0
    line2_b_re = 0
    line3_b_re = 0
    line4_b_re = 0
    line5_b_re = 0
    line6_b_re = 0

    # assign variables from specific columns from database
    for_count = 0
    for i in daily_report(line).combined_side_a_ng:
        for_count += 1
        if for_count == 1:
            line0_a_ng = i
        elif for_count == 2:
            line1_a_ng = i
        elif for_count == 3:
            line2_a_ng = i
        elif for_count == 4:
            line3_a_ng = i
        elif for_count == 5:
            line4_a_ng = i
        elif for_count == 6:
            line5_a_ng = i
        elif for_count == 7:
            line6_a_ng = i

    for_count = 0
    for e in daily_report(line).combined_side_b_ng:
        for_count += 1
        if for_count == 1:
            line0_b_ng = e
        elif for_count == 2:
            line1_b_ng = e
        elif for_count == 3:
            line2_b_ng = e
        elif for_count == 4:
            line3_b_ng = e
        elif for_count == 5:
            line4_b_ng = e
        elif for_count == 6:
            line5_b_ng = e
        elif for_count == 7:
            line6_b_ng = e

    for_count = 0
    for a in daily_report(line).combined_side_a_re:
        for_count += 1
        if for_count == 1:
            line0_a_re = a
        elif for_count == 2:
            line1_a_re = a
        elif for_count == 3:
            line2_a_re = a
        elif for_count == 4:
            line3_a_re = a
        elif for_count == 5:
            line4_a_re = a
        elif for_count == 6:
            line5_a_re = a
        elif for_count == 7:
            line6_a_re = a

    for_count = 0
    for u in daily_report(line).combined_side_b_re:
        for_count += 1
        if for_count == 1:
            line0_b_re = u
        elif for_count == 2:
            line1_b_re = u
        elif for_count == 3:
            line2_b_re = u
        elif for_count == 5:
            line3_b_re = u
        elif for_count == 6:
            line4_b_re = u
        elif for_count == 7:
            line5_b_re = u
        elif for_count == 8:
            line6_b_re = u


    return {
    "line":line,
    "line0_a_ng":line0_a_ng,
    "line1_a_ng":line1_a_ng,
    "line2_a_ng":line2_a_ng,
    "line3_a_ng":line3_a_ng,
    "line4_a_ng":line4_a_ng,
    "line5_a_ng":line5_a_ng,
    "line6_a_ng":line6_a_ng,
    "line0_b_ng":line0_b_ng,
    "line1_b_ng":line1_b_ng,
    "line2_b_ng":line2_b_ng,
    "line3_b_ng":line3_b_ng,
    "line4_b_ng":line4_b_ng,
    "line5_b_ng":line5_b_ng,
    "line6_b_ng":line6_b_ng,
    "line0_a_re":line0_a_re,
    "line1_a_re":line1_a_re,
    "line2_a_re":line2_a_re,
    "line3_a_re":line3_a_re,
    "line4_a_re":line4_a_re,
    "line5_a_re":line5_a_re,
    "line6_a_re":line6_a_re,
    "line0_b_re":line0_b_re,
    "line1_b_re":line1_b_re,
    "line2_b_re":line2_b_re,
    "line3_b_re":line3_b_re,
    "line4_b_re":line4_b_re,
    "line5_b_re":line5_b_re,
    "line6_b_re":line6_b_re
    }

# assign values to variables and destinguish if one side is not running
def assign_variables(data_dict):
    combined_scrap_0_a = data_dict["line0_a_ng"] + data_dict["line0_a_re"]
    combined_scrap_0_b = data_dict["line0_b_ng"] + data_dict["line0_a_re"]
    combined_scrap_1_a = data_dict["line1_a_ng"] + data_dict["line1_a_re"]
    combined_scrap_1_b = data_dict["line1_b_ng"] + data_dict["line1_a_re"]
    combined_scrap_2_a = data_dict["line2_a_ng"] + data_dict["line2_a_re"]
    combined_scrap_2_b = data_dict["line2_b_ng"] + data_dict["line2_a_re"]
    combined_scrap_3_a = data_dict["line3_a_ng"] + data_dict["line3_a_re"]
    combined_scrap_3_b = data_dict["line3_b_ng"] + data_dict["line3_a_re"]
    combined_scrap_4_a = data_dict["line4_a_ng"] + data_dict["line4_a_re"]
    combined_scrap_4_b = data_dict["line4_b_ng"] + data_dict["line4_a_re"]
    combined_scrap_5_a = data_dict["line5_a_ng"] + data_dict["line5_a_re"]
    combined_scrap_5_b = data_dict["line5_b_ng"] + data_dict["line5_a_re"]
    combined_scrap_6_a = data_dict["line6_a_ng"] + data_dict["line6_a_re"]
    combined_scrap_6_b = data_dict["line6_b_ng"] + data_dict["line6_a_re"]

    # determin if both side are running. If not, don't devide the result
    if data_dict["line0_a_ng"] < 0.1 or data_dict["line0_b_ng"] < 0.1:
        combined_scrap_0 = data_dict["line0_a_ng"] + data_dict["line0_a_re"] + data_dict["line0_b_ng"] + data_dict["line0_a_re"]
    elif data_dict["line0_a_ng"] > 0.1 and data_dict["line0_b_ng"] > 0.1:
        combined_scrap_0 = (data_dict["line0_a_ng"] + data_dict["line0_a_re"] + data_dict["line0_b_ng"] + data_dict["line0_a_re"]) / 2

    if data_dict["line1_a_ng"] < 0.1 or data_dict["line1_b_ng"] < 0.1:
        combined_scrap_1 = data_dict["line1_a_ng"] + data_dict["line1_a_re"] + data_dict["line1_b_ng"] + data_dict["line1_a_re"]
    elif data_dict["line1_a_ng"] > 0.1 and data_dict["line1_b_ng"] > 0.1:
        combined_scrap_1 = (data_dict["line1_a_ng"] + data_dict["line1_a_re"] + data_dict["line1_b_ng"] + data_dict["line1_a_re"]) / 2

    if data_dict["line2_a_ng"] < 0.1 or data_dict["line2_b_ng"] < 0.1:
        combined_scrap_2 = data_dict["line2_a_ng"] + data_dict["line2_a_re"] + data_dict["line2_b_ng"] + data_dict["line2_a_re"]
    elif data_dict["line2_a_ng"] > 0.1 and data_dict["line2_b_ng"] > 0.1:
        combined_scrap_2 = (data_dict["line2_a_ng"] + data_dict["line2_a_re"] + data_dict["line2_b_ng"] + data_dict["line2_a_re"]) / 2


    if data_dict["line3_a_ng"] < 0.1 or data_dict["line3_b_ng"] < 0.1:
        combined_scrap_3 = data_dict["line3_a_ng"] + data_dict["line3_a_re"] + data_dict["line3_b_ng"] + data_dict["line3_a_re"]
    elif data_dict["line3_a_ng"] > 0.1 and data_dict["line3_b_ng"] > 0.1:
        combined_scrap_3 = (data_dict["line3_a_ng"] + data_dict["line3_a_re"] + data_dict["line3_b_ng"] + data_dict["line3_a_re"]) / 2

    if data_dict["line4_a_ng"] < 0.1 or data_dict["line4_b_ng"] < 0.1:
        combined_scrap_4 = data_dict["line4_a_ng"] + data_dict["line4_a_re"] + data_dict["line4_b_ng"] + data_dict["line4_a_re"]
    elif data_dict["line4_a_ng"] > 0.1 and data_dict["line4_b_ng"] > 0.1:
        combined_scrap_4 = (data_dict["line4_a_ng"] + data_dict["line4_a_re"] + data_dict["line4_b_ng"] + data_dict["line4_a_re"]) / 2

    if data_dict["line5_a_ng"] < 0.1 or data_dict["line5_b_ng"] < 0.1:
        combined_scrap_5 = data_dict["line5_a_ng"] + data_dict["line5_a_re"] + data_dict["line5_b_ng"] + data_dict["line5_a_re"]
    elif data_dict["line5_a_ng"] > 0.1 and data_dict["line5_b_ng"] > 0.1:
        combined_scrap_5 = (data_dict["line5_a_ng"] + data_dict["line5_a_re"] + data_dict["line5_b_ng"] + data_dict["line5_a_re"]) / 2

    if data_dict["line6_a_ng"] < 0.1 or data_dict["line6_b_ng"] < 0.1:
        combined_scrap_6 = data_dict["line6_a_ng"] + data_dict["line6_a_re"] + data_dict["line6_b_ng"] + data_dict["line6_a_re"]
    elif data_dict["line6_a_ng"] > 0.1 and data_dict["line6_b_ng"] > 0.1:
        combined_scrap_6 = (data_dict["line6_a_ng"] + data_dict["line6_a_re"] + data_dict["line6_b_ng"] + data_dict["line6_a_re"]) / 2

    return {
    "day0_a":combined_scrap_0_a,
    "day0_b":combined_scrap_0_b,
    "day1_a":combined_scrap_1_a,
    "day1_b":combined_scrap_1_b,
    "day2_a":combined_scrap_2_a,
    "day2_b":combined_scrap_2_b,
    "day3_a":combined_scrap_3_a,
    "day3_b":combined_scrap_3_b,
    "day4_a":combined_scrap_4_a,
    "day4_b":combined_scrap_4_b,
    "day5_a":combined_scrap_5_a,
    "day5_b":combined_scrap_5_b,
    "day6_a":combined_scrap_6_a,
    "day6_b":combined_scrap_6_b,
    "combined_scrap_0":combined_scrap_0,
    "combined_scrap_1":combined_scrap_1,
    "combined_scrap_2":combined_scrap_2,
    "combined_scrap_3":combined_scrap_3,
    "combined_scrap_4":combined_scrap_4,
    "combined_scrap_5":combined_scrap_5,
    "combined_scrap_6":combined_scrap_6
    }


class Table(View):
    model = daily_report
    def get(self, request):

        # This gives the function above an integer which translates to the weekday name
        day0 = get_weekday(datetime.strptime(str(daily_report(5).production_day[0])[0:10], '%Y-%m-%d').date().weekday)
        day1 = get_weekday(datetime.strptime(str(daily_report(5).production_day[1])[0:10], '%Y-%m-%d').date().weekday)
        day2 = get_weekday(datetime.strptime(str(daily_report(5).production_day[2])[0:10], '%Y-%m-%d').date().weekday)
        day3 = get_weekday(datetime.strptime(str(daily_report(5).production_day[3])[0:10], '%Y-%m-%d').date().weekday)
        day4 = get_weekday(datetime.strptime(str(daily_report(5).production_day[4])[0:10], '%Y-%m-%d').date().weekday)
        day5 = get_weekday(datetime.strptime(str(daily_report(5).production_day[5])[0:10], '%Y-%m-%d').date().weekday)
        day6 = get_weekday(datetime.strptime(str(daily_report(5).production_day[6])[0:10], '%Y-%m-%d').date().weekday)

        render_dictionary = {}
        line3 = assign_variables(get_value_for_machine_per_period(3))
        combined_scrap_0_line_3 = line3["combined_scrap_0"]
        combined_scrap_1_line_3 = line3["combined_scrap_1"]
        combined_scrap_2_line_3 = line3["combined_scrap_2"]
        combined_scrap_3_line_3 = line3["combined_scrap_3"]
        combined_scrap_4_line_3 = line3["combined_scrap_4"]
        combined_scrap_5_line_3 = line3["combined_scrap_5"]
        combined_scrap_6_line_3 = line3["combined_scrap_6"]


        line4 = assign_variables(get_value_for_machine_per_period(4))
        combined_scrap_0_line_4 = line4["combined_scrap_0"]
        combined_scrap_1_line_4 = line4["combined_scrap_1"]
        combined_scrap_2_line_4 = line4["combined_scrap_2"]
        combined_scrap_3_line_4 = line4["combined_scrap_3"]
        combined_scrap_4_line_4 = line4["combined_scrap_4"]
        combined_scrap_5_line_4 = line4["combined_scrap_5"]
        combined_scrap_6_line_4 = line4["combined_scrap_6"]


        line5 = assign_variables(get_value_for_machine_per_period(5))
        combined_scrap_0_line_5 = line5["combined_scrap_0"]
        combined_scrap_1_line_5 = line5["combined_scrap_1"]
        combined_scrap_2_line_5 = line5["combined_scrap_2"]
        combined_scrap_3_line_5 = line5["combined_scrap_3"]
        combined_scrap_4_line_5 = line5["combined_scrap_4"]
        combined_scrap_5_line_5 = line5["combined_scrap_5"]
        combined_scrap_6_line_5 = line5["combined_scrap_6"]


        line7 = assign_variables(get_value_for_machine_per_period(7))
        combined_scrap_0_line_7 = line7["combined_scrap_0"]
        combined_scrap_1_line_7 = line7["combined_scrap_1"]
        combined_scrap_2_line_7 = line7["combined_scrap_2"]
        combined_scrap_3_line_7 = line7["combined_scrap_3"]
        combined_scrap_4_line_7 = line7["combined_scrap_4"]
        combined_scrap_5_line_7 = line7["combined_scrap_5"]
        combined_scrap_6_line_7 = line7["combined_scrap_6"]


        line8 = assign_variables(get_value_for_machine_per_period(8))
        combined_scrap_0_line_8 = line8["combined_scrap_0"]
        combined_scrap_1_line_8 = line8["combined_scrap_1"]
        combined_scrap_2_line_8 = line8["combined_scrap_2"]
        combined_scrap_3_line_8 = line8["combined_scrap_3"]
        combined_scrap_4_line_8 = line8["combined_scrap_4"]
        combined_scrap_5_line_8 = line8["combined_scrap_5"]
        combined_scrap_6_line_8 = line8["combined_scrap_6"]


        line9 = assign_variables(get_value_for_machine_per_period(9))
        combined_scrap_0_line_9 = line9["combined_scrap_0"]
        combined_scrap_1_line_9 = line9["combined_scrap_1"]
        combined_scrap_2_line_9 = line9["combined_scrap_2"]
        combined_scrap_3_line_9 = line9["combined_scrap_3"]
        combined_scrap_4_line_9 = line9["combined_scrap_4"]
        combined_scrap_5_line_9 = line9["combined_scrap_5"]
        combined_scrap_6_line_9 = line9["combined_scrap_6"]


        line10 = assign_variables(get_value_for_machine_per_period(10))
        combined_scrap_0_line_10 = line10["combined_scrap_0"]
        combined_scrap_1_line_10 = line10["combined_scrap_1"]
        combined_scrap_2_line_10 = line10["combined_scrap_2"]
        combined_scrap_3_line_10 = line10["combined_scrap_3"]
        combined_scrap_4_line_10 = line10["combined_scrap_4"]
        combined_scrap_5_line_10 = line10["combined_scrap_5"]
        combined_scrap_6_line_10 = line10["combined_scrap_6"]

        return render(request, "dolcegusto/scrap_rate.html", {
        "line_3": 3,
        "line_4": 4,
        "line_5": 5,
        "line_7": 7,
        "line_8": 8,
        "line_9": 9,
        "line_10": 10,
        "combined_scrap_0_line_3": combined_scrap_0_line_3,
        "combined_scrap_0_line_4": combined_scrap_0_line_4,
        "combined_scrap_0_line_5": combined_scrap_0_line_5,
        "combined_scrap_0_line_7": combined_scrap_0_line_7,
        "combined_scrap_0_line_8": combined_scrap_0_line_8,
        "combined_scrap_0_line_9": combined_scrap_0_line_9,
        "combined_scrap_0_line_10": combined_scrap_0_line_10,
        "day1": day1,
        "combined_scrap_1_line_3": combined_scrap_1_line_3,
        "combined_scrap_1_line_4": combined_scrap_1_line_4,
        "combined_scrap_1_line_5": combined_scrap_1_line_5,
        "combined_scrap_1_line_7": combined_scrap_1_line_7,
        "combined_scrap_1_line_8": combined_scrap_1_line_8,
        "combined_scrap_1_line_9": combined_scrap_1_line_9,
        "combined_scrap_1_line_10": combined_scrap_1_line_10,
        "day2": day2,
        "combined_scrap_2_line_3": combined_scrap_2_line_3,
        "combined_scrap_2_line_4": combined_scrap_2_line_4,
        "combined_scrap_2_line_5": combined_scrap_2_line_5,
        "combined_scrap_2_line_7": combined_scrap_2_line_7,
        "combined_scrap_2_line_8": combined_scrap_2_line_8,
        "combined_scrap_2_line_9": combined_scrap_2_line_9,
        "combined_scrap_2_line_10": combined_scrap_2_line_10,
        "day3": day3,
        "combined_scrap_3_line_3": combined_scrap_3_line_3,
        "combined_scrap_3_line_4": combined_scrap_3_line_4,
        "combined_scrap_3_line_5": combined_scrap_3_line_5,
        "combined_scrap_3_line_7": combined_scrap_3_line_7,
        "combined_scrap_3_line_8": combined_scrap_3_line_8,
        "combined_scrap_3_line_9": combined_scrap_3_line_9,
        "combined_scrap_3_line_10": combined_scrap_3_line_10,
        "day4": day4,
        "combined_scrap_4_line_3": combined_scrap_4_line_3,
        "combined_scrap_4_line_4": combined_scrap_4_line_4,
        "combined_scrap_4_line_5": combined_scrap_4_line_5,
        "combined_scrap_4_line_7": combined_scrap_4_line_7,
        "combined_scrap_4_line_8": combined_scrap_4_line_8,
        "combined_scrap_4_line_9": combined_scrap_4_line_9,
        "combined_scrap_4_line_10": combined_scrap_4_line_10,
        "day5": day5,
        "combined_scrap_5_line_3": combined_scrap_5_line_3,
        "combined_scrap_5_line_4": combined_scrap_5_line_4,
        "combined_scrap_5_line_5": combined_scrap_5_line_5,
        "combined_scrap_5_line_7": combined_scrap_5_line_7,
        "combined_scrap_5_line_8": combined_scrap_5_line_8,
        "combined_scrap_5_line_9": combined_scrap_5_line_9,
        "combined_scrap_5_line_10": combined_scrap_5_line_10,
        "day6": day6,
        "combined_scrap_6_line_3": combined_scrap_6_line_3,
        "combined_scrap_6_line_4": combined_scrap_6_line_4,
        "combined_scrap_6_line_5": combined_scrap_6_line_5,
        "combined_scrap_6_line_7": combined_scrap_6_line_7,
        "combined_scrap_6_line_8": combined_scrap_6_line_8,
        "combined_scrap_6_line_9": combined_scrap_6_line_9,
        "combined_scrap_6_line_10": combined_scrap_6_line_10
        })


class Line3(View):
    model = daily_report
    def get(self, request):

        # This gives the function above an integer which translates to the weekday name
        day0 = get_weekday(datetime.strptime(str(daily_report(5).production_day[0])[0:10], '%Y-%m-%d').date().weekday)
        day1 = get_weekday(datetime.strptime(str(daily_report(5).production_day[1])[0:10], '%Y-%m-%d').date().weekday)
        day2 = get_weekday(datetime.strptime(str(daily_report(5).production_day[2])[0:10], '%Y-%m-%d').date().weekday)
        day3 = get_weekday(datetime.strptime(str(daily_report(5).production_day[3])[0:10], '%Y-%m-%d').date().weekday)
        day4 = get_weekday(datetime.strptime(str(daily_report(5).production_day[4])[0:10], '%Y-%m-%d').date().weekday)
        day5 = get_weekday(datetime.strptime(str(daily_report(5).production_day[5])[0:10], '%Y-%m-%d').date().weekday)
        day6 = get_weekday(datetime.strptime(str(daily_report(5).production_day[6])[0:10], '%Y-%m-%d').date().weekday)

        line3 = assign_variables(get_value_for_machine_per_period(3))

        return render(request, "dolcegusto/line3.html", {
        "line_3": 3,
        "day1": day1,
        "day2": day2,
        "day3": day3,
        "day4": day4,
        "day5": day5,
        "day6": day6,
        "combined_scrap_0_a": line3["day0_a"],
        "combined_scrap_0_b": line3["day0_b"],
        "combined_scrap_1_a": line3["day1_a"],
        "combined_scrap_1_b": line3["day1_b"],
        "combined_scrap_2_a": line3["day2_a"],
        "combined_scrap_2_b": line3["day2_b"],
        "combined_scrap_3_a": line3["day3_a"],
        "combined_scrap_3_b": line3["day3_b"],
        "combined_scrap_4_a": line3["day4_a"],
        "combined_scrap_4_b": line3["day4_b"],
        "combined_scrap_5_a": line3["day5_a"],
        "combined_scrap_5_b": line3["day5_b"],
        "combined_scrap_6_a": line3["day6_a"],
        "combined_scrap_6_b": line3["day6_b"]
        })
