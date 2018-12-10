from django.shortcuts import render
from django.views import View
import pandas as pd
from pandas import DataFrame
from datetime import datetime, date, timedelta

from dolcegusto.models import daily_report, hourly_report
from dolcegusto.times import get_weekday
from dolcegusto.get_values import past_seven_days


# assign variables from database columns


def get_value_for_machine_per_period_hourly(line):

    now = time.asctime(time.localtime(time.time())).strftime('%Y-%m-%d')

    prod_time1 = str(hourly_report(line).hour[1])
    prod_time1 = prod_time1[0:10]

    # assign variables from specific columns from database based on date
    for_count = 0
    for i in hourly_report(line).a_top_ng:
        for_count += 1
        if for_count == 1:
            if prod_date0 == today:
                line0_a_ng = i
            elif prod_date0 == yesterday:
                line1_a_ng = i
            elif prod_date0 == two_days_ago:
                line2_a_ng = i
            elif prod_date0 == three_days_ago:
                line3_a_ng = i
            elif prod_date0 == four_days_ago:
                line4_a_ng = i
            elif prod_date0 == five_days_ago:
                line5_a_ng = i
            elif prod_date0 == six_days_ago:
                line6_a_ng = i

        elif for_count == 2:
            if prod_date1 == yesterday:
                line1_a_ng = i
            elif prod_date1 == two_days_ago:
                line2_a_ng = i
            elif prod_date1 == three_days_ago:
                line3_a_ng = i
            elif prod_date1 == four_days_ago:
                line4_a_ng = i
            elif prod_date1 == five_days_ago:
                line5_a_ng = i
            elif prod_date1 == six_days_ago:
                line6_a_ng = i


        elif for_count == 3:
            if prod_date2 == two_days_ago:
                line2_a_ng = i
            elif prod_date2 == three_days_ago:
                line3_a_ng = i
            elif prod_date2 == four_days_ago:
                line4_a_ng = i
            elif prod_date2 == five_days_ago:
                line5_a_ng = i
            elif prod_date2 == six_days_ago:
                line6_a_ng = i

        elif for_count == 4:
            if prod_date3 == three_days_ago:
                line3_a_ng = i
            elif prod_date3 == four_days_ago:
                line4_a_ng = i
            elif prod_date3 == five_days_ago:
                line5_a_ng = i
            elif prod_date3 == six_days_ago:
                line6_a_ng = i

        elif for_count == 5:
            if prod_date4 == four_days_ago:
                line4_a_ng = i
            elif prod_date4 == five_days_ago:
                line5_a_ng = i
            elif prod_date4 == six_days_ago:
                line6_a_ng = i

        elif for_count == 6:
            if prod_date5 == five_days_ago:
                line5_a_ng = i
            elif prod_date5 == six_days_ago:
                line6_a_ng = i

        elif for_count == 7:
            if prod_date6 == six_days_ago:
                line6_a_ng = i


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

    # # determin if both side are running. If not, don't devide the result
    # if data_dict["line0_a_ng"] < 0.1 or data_dict["line0_b_ng"] < 0.1:
    #     combined_scrap_0 = data_dict["line0_a_ng"] + data_dict["line0_a_re"] + data_dict["line0_b_ng"] + data_dict["line0_a_re"]
    # elif data_dict["line0_a_ng"] > 0.1 and data_dict["line0_b_ng"] > 0.1:
    #     combined_scrap_0 = (data_dict["line0_a_ng"] + data_dict["line0_a_re"] + data_dict["line0_b_ng"] + data_dict["line0_a_re"]) / 2
    #
    # if data_dict["line1_a_ng"] < 0.1 or data_dict["line1_b_ng"] < 0.1:
    #     combined_scrap_1 = data_dict["line1_a_ng"] + data_dict["line1_a_re"] + data_dict["line1_b_ng"] + data_dict["line1_a_re"]
    # elif data_dict["line1_a_ng"] > 0.1 and data_dict["line1_b_ng"] > 0.1:
    #     combined_scrap_1 = (data_dict["line1_a_ng"] + data_dict["line1_a_re"] + data_dict["line1_b_ng"] + data_dict["line1_a_re"]) / 2
    #
    # if data_dict["line2_a_ng"] < 0.1 or data_dict["line2_b_ng"] < 0.1:
    #     combined_scrap_2 = data_dict["line2_a_ng"] + data_dict["line2_a_re"] + data_dict["line2_b_ng"] + data_dict["line2_a_re"]
    # elif data_dict["line2_a_ng"] > 0.1 and data_dict["line2_b_ng"] > 0.1:
    #     combined_scrap_2 = (data_dict["line2_a_ng"] + data_dict["line2_a_re"] + data_dict["line2_b_ng"] + data_dict["line2_a_re"]) / 2
    #
    # if data_dict["line3_a_ng"] < 0.1 or data_dict["line3_b_ng"] < 0.1:
    #     combined_scrap_3 = data_dict["line3_a_ng"] + data_dict["line3_a_re"] + data_dict["line3_b_ng"] + data_dict["line3_a_re"]
    # elif data_dict["line3_a_ng"] > 0.1 and data_dict["line3_b_ng"] > 0.1:
    #     combined_scrap_3 = (data_dict["line3_a_ng"] + data_dict["line3_a_re"] + data_dict["line3_b_ng"] + data_dict["line3_a_re"]) / 2
    #
    # if data_dict["line4_a_ng"] < 0.1 or data_dict["line4_b_ng"] < 0.1:
    #     combined_scrap_4 = data_dict["line4_a_ng"] + data_dict["line4_a_re"] + data_dict["line4_b_ng"] + data_dict["line4_a_re"]
    # elif data_dict["line4_a_ng"] > 0.1 and data_dict["line4_b_ng"] > 0.1:
    #     combined_scrap_4 = (data_dict["line4_a_ng"] + data_dict["line4_a_re"] + data_dict["line4_b_ng"] + data_dict["line4_a_re"]) / 2
    #
    # if data_dict["line5_a_ng"] < 0.1 or data_dict["line5_b_ng"] < 0.1:
    #     combined_scrap_5 = data_dict["line5_a_ng"] + data_dict["line5_a_re"] + data_dict["line5_b_ng"] + data_dict["line5_a_re"]
    # elif data_dict["line5_a_ng"] > 0.1 and data_dict["line5_b_ng"] > 0.1:
    #     combined_scrap_5 = (data_dict["line5_a_ng"] + data_dict["line5_a_re"] + data_dict["line5_b_ng"] + data_dict["line5_a_re"]) / 2
    #
    # if data_dict["line6_a_ng"] < 0.1 or data_dict["line6_b_ng"] < 0.1:
    #     combined_scrap_6 = data_dict["line6_a_ng"] + data_dict["line6_a_re"] + data_dict["line6_b_ng"] + data_dict["line6_a_re"]
    # elif data_dict["line6_a_ng"] > 0.1 and data_dict["line6_b_ng"] > 0.1:
    #     combined_scrap_6 = (data_dict["line6_a_ng"] + data_dict["line6_a_re"] + data_dict["line6_b_ng"] + data_dict["line6_a_re"]) / 2

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
    # "combined_scrap_0":combined_scrap_0,
    # "combined_scrap_1":combined_scrap_1,
    # "combined_scrap_2":combined_scrap_2,
    # "combined_scrap_3":combined_scrap_3,
    # "combined_scrap_4":combined_scrap_4,
    # "combined_scrap_5":combined_scrap_5,
    # "combined_scrap_6":combined_scrap_6
    }


class Table(View):
    model = daily_report
    def get(self, request):
        # This gives the function above an integer which translates to the weekday name
        day2 = get_weekday(datetime.strptime(str(daily_report(5).production_day[2])[0:10], '%Y-%m-%d').date().weekday)
        day3 = get_weekday(datetime.strptime(str(daily_report(5).production_day[3])[0:10], '%Y-%m-%d').date().weekday)
        day4 = get_weekday(datetime.strptime(str(daily_report(5).production_day[4])[0:10], '%Y-%m-%d').date().weekday)
        day5 = get_weekday(datetime.strptime(str(daily_report(5).production_day[5])[0:10], '%Y-%m-%d').date().weekday)
        day6 = get_weekday(datetime.strptime(str(daily_report(5).production_day[6])[0:10], '%Y-%m-%d').date().weekday)

        line3 = assign_variables(past_seven_days(3))
        line4 = assign_variables(past_seven_days(4))
        line5 = assign_variables(past_seven_days(5))
        line7 = assign_variables(past_seven_days(7))
        line8 = assign_variables(past_seven_days(8))
        line9 = assign_variables(past_seven_days(9))
        line10 = assign_variables(past_seven_days(10))

        return render(request, "dolcegusto/scrap_rate.html", {
        "line_3": 3,
        "line_4": 4,
        "line_5": 5,
        "line_7": 7,
        "line_8": 8,
        "line_9": 9,
        "line_10": 10,
        "day2": day2,
        "day3": day3,
        "day4": day4,
        "day5": day5,
        "day6": day6,
        "combined_scrap_0_3_a": line3["day0_a"],
        "combined_scrap_0_3_b": line3["day0_b"],
        "combined_scrap_1_3_a": line3["day1_a"],
        "combined_scrap_1_3_b": line3["day1_b"],
        "combined_scrap_2_3_a": line3["day2_a"],
        "combined_scrap_2_3_b": line3["day2_b"],
        "combined_scrap_3_3_a": line3["day3_a"],
        "combined_scrap_3_3_b": line3["day3_b"],
        "combined_scrap_4_3_a": line3["day4_a"],
        "combined_scrap_4_3_b": line3["day4_b"],
        "combined_scrap_5_3_a": line3["day5_a"],
        "combined_scrap_5_3_b": line3["day5_b"],
        "combined_scrap_6_3_a": line3["day6_a"],
        "combined_scrap_6_3_b": line3["day6_b"],

        "combined_scrap_0_4_a": line4["day0_a"],
        "combined_scrap_0_4_b": line4["day0_b"],
        "combined_scrap_1_4_a": line4["day1_a"],
        "combined_scrap_1_4_b": line4["day1_b"],
        "combined_scrap_2_4_a": line4["day2_a"],
        "combined_scrap_2_4_b": line4["day2_b"],
        "combined_scrap_3_4_a": line4["day3_a"],
        "combined_scrap_3_4_b": line4["day3_b"],
        "combined_scrap_4_4_a": line4["day4_a"],
        "combined_scrap_4_4_b": line4["day4_b"],
        "combined_scrap_5_4_a": line4["day5_a"],
        "combined_scrap_5_4_b": line4["day5_b"],
        "combined_scrap_6_4_a": line4["day6_a"],
        "combined_scrap_6_4_b": line4["day6_b"],

        "combined_scrap_0_5_a": line5["day0_a"],
        "combined_scrap_0_5_b": line5["day0_b"],
        "combined_scrap_1_5_a": line5["day1_a"],
        "combined_scrap_1_5_b": line5["day1_b"],
        "combined_scrap_2_5_a": line5["day2_a"],
        "combined_scrap_2_5_b": line5["day2_b"],
        "combined_scrap_3_5_a": line5["day3_a"],
        "combined_scrap_3_5_b": line5["day3_b"],
        "combined_scrap_4_5_a": line5["day4_a"],
        "combined_scrap_4_5_b": line5["day4_b"],
        "combined_scrap_5_5_a": line5["day5_a"],
        "combined_scrap_5_5_b": line5["day5_b"],
        "combined_scrap_6_5_a": line5["day6_a"],
        "combined_scrap_6_5_b": line5["day6_b"],

        "combined_scrap_0_7_a": line7["day0_a"],
        "combined_scrap_0_7_b": line7["day0_b"],
        "combined_scrap_1_7_a": line7["day1_a"],
        "combined_scrap_1_7_b": line7["day1_b"],
        "combined_scrap_2_7_a": line7["day2_a"],
        "combined_scrap_2_7_b": line7["day2_b"],
        "combined_scrap_3_7_a": line7["day3_a"],
        "combined_scrap_3_7_b": line7["day3_b"],
        "combined_scrap_4_7_a": line7["day4_a"],
        "combined_scrap_4_7_b": line7["day4_b"],
        "combined_scrap_5_7_a": line7["day5_a"],
        "combined_scrap_5_7_b": line7["day5_b"],
        "combined_scrap_6_7_a": line7["day6_a"],
        "combined_scrap_6_7_b": line7["day6_b"],

        "combined_scrap_0_8_a": line8["day0_a"],
        "combined_scrap_0_8_b": line8["day0_b"],
        "combined_scrap_1_8_a": line8["day1_a"],
        "combined_scrap_1_8_b": line8["day1_b"],
        "combined_scrap_2_8_a": line8["day2_a"],
        "combined_scrap_2_8_b": line8["day2_b"],
        "combined_scrap_3_8_a": line8["day3_a"],
        "combined_scrap_3_8_b": line8["day3_b"],
        "combined_scrap_4_8_a": line8["day4_a"],
        "combined_scrap_4_8_b": line8["day4_b"],
        "combined_scrap_5_8_a": line8["day5_a"],
        "combined_scrap_5_8_b": line8["day5_b"],
        "combined_scrap_6_8_a": line8["day6_a"],
        "combined_scrap_6_8_b": line8["day6_b"],

        "combined_scrap_0_9_a": line9["day0_a"],
        "combined_scrap_0_9_b": line9["day0_b"],
        "combined_scrap_1_9_a": line9["day1_a"],
        "combined_scrap_1_9_b": line9["day1_b"],
        "combined_scrap_2_9_a": line9["day2_a"],
        "combined_scrap_2_9_b": line9["day2_b"],
        "combined_scrap_3_9_a": line9["day3_a"],
        "combined_scrap_3_9_b": line9["day3_b"],
        "combined_scrap_4_9_a": line9["day4_a"],
        "combined_scrap_4_9_b": line9["day4_b"],
        "combined_scrap_5_9_a": line9["day5_a"],
        "combined_scrap_5_9_b": line9["day5_b"],
        "combined_scrap_6_9_a": line9["day6_a"],
        "combined_scrap_6_9_b": line9["day6_b"],

        "combined_scrap_0_10_a": line10["day0_a"],
        "combined_scrap_0_10_b": line10["day0_b"],
        "combined_scrap_1_10_a": line10["day1_a"],
        "combined_scrap_1_10_b": line10["day1_b"],
        "combined_scrap_2_10_a": line10["day2_a"],
        "combined_scrap_2_10_b": line10["day2_b"],
        "combined_scrap_3_10_a": line10["day3_a"],
        "combined_scrap_3_10_b": line10["day3_b"],
        "combined_scrap_4_10_a": line10["day4_a"],
        "combined_scrap_4_10_b": line10["day4_b"],
        "combined_scrap_5_10_a": line10["day5_a"],
        "combined_scrap_5_10_b": line10["day5_b"],
        "combined_scrap_6_10_a": line10["day6_a"],
        "combined_scrap_6_10_b": line10["day6_b"],
        })

        # line3 = past_seven_days(3)
        #combined_scrap_0_line_3 = line3["combined_scrap_0"]
        # combined_scrap_1_line_3 = line3["combined_scrap_1"]
        # combined_scrap_2_line_3 = line3["combined_scrap_2"]
        # combined_scrap_3_line_3 = line3["combined_scrap_3"]
        # combined_scrap_4_line_3 = line3["combined_scrap_4"]
        # combined_scrap_5_line_3 = line3["combined_scrap_5"]
        # combined_scrap_6_line_3 = line3["combined_scrap_6"]
        line4 = assign_variables(past_seven_days(4))

        return render(request, "dolcegusto/line4.html", {
        "line_3": 3,
        "line_4": 4,
        "line_5": 5,
        "line_7": 7,
        "line_8": 8,
        "line_9": 9,
        "line_10": 10,
        "day2": day2,
        "day3": day3,
        "day4": day4,
        "day5": day5,
        "day6": day6,
        "combined_scrap_0_a": line4["day0_a"],
        "combined_scrap_0_b": line4["day0_b"],
        "combined_scrap_1_a": line4["day1_a"],
        "combined_scrap_1_b": line4["day1_b"],
        "combined_scrap_2_a": line4["day2_a"],
        "combined_scrap_2_b": line4["day2_b"],
        "combined_scrap_3_a": line4["day3_a"],
        "combined_scrap_3_b": line4["day3_b"],
        "combined_scrap_4_a": line4["day4_a"],
        "combined_scrap_4_b": line4["day4_b"],
        "combined_scrap_5_a": line4["day5_a"],
        "combined_scrap_5_b": line4["day5_b"],
        "combined_scrap_6_a": line4["day6_a"],
        "combined_scrap_6_b": line4["day6_b"]
        })

        # # This gives the function above an integer which translates to the weekday name
        # day0 = get_weekday(datetime.strptime(str(daily_report(5).production_day[0])[0:10], '%Y-%m-%d').date().weekday)
        # day1 = get_weekday(datetime.strptime(str(daily_report(5).production_day[1])[0:10], '%Y-%m-%d').date().weekday)
        # day2 = get_weekday(datetime.strptime(str(daily_report(5).production_day[2])[0:10], '%Y-%m-%d').date().weekday)
        # day3 = get_weekday(datetime.strptime(str(daily_report(5).production_day[3])[0:10], '%Y-%m-%d').date().weekday)
        # day4 = get_weekday(datetime.strptime(str(daily_report(5).production_day[4])[0:10], '%Y-%m-%d').date().weekday)
        # day5 = get_weekday(datetime.strptime(str(daily_report(5).production_day[5])[0:10], '%Y-%m-%d').date().weekday)
        # day6 = get_weekday(datetime.strptime(str(daily_report(5).production_day[6])[0:10], '%Y-%m-%d').date().weekday)
        #
        # render_dictionary = {}
        # line3 = assign_variables(past_seven_days(3))
        # combined_scrap_0_line_3 = line3["combined_scrap_0"]
        # combined_scrap_1_line_3 = line3["combined_scrap_1"]
        # combined_scrap_2_line_3 = line3["combined_scrap_2"]
        # combined_scrap_3_line_3 = line3["combined_scrap_3"]
        # combined_scrap_4_line_3 = line3["combined_scrap_4"]
        # combined_scrap_5_line_3 = line3["combined_scrap_5"]
        # combined_scrap_6_line_3 = line3["combined_scrap_6"]
        #
        #
        # line4 = assign_variables(past_seven_days(4))
        # combined_scrap_0_line_4 = line4["combined_scrap_0"]
        # combined_scrap_1_line_4 = line4["combined_scrap_1"]
        # combined_scrap_2_line_4 = line4["combined_scrap_2"]
        # combined_scrap_3_line_4 = line4["combined_scrap_3"]
        # combined_scrap_4_line_4 = line4["combined_scrap_4"]
        # combined_scrap_5_line_4 = line4["combined_scrap_5"]
        # combined_scrap_6_line_4 = line4["combined_scrap_6"]
        #
        #
        # line5 = assign_variables(past_seven_days(5))
        # combined_scrap_0_line_5 = line5["combined_scrap_0"]
        # combined_scrap_1_line_5 = line5["combined_scrap_1"]
        # combined_scrap_2_line_5 = line5["combined_scrap_2"]
        # combined_scrap_3_line_5 = line5["combined_scrap_3"]
        # combined_scrap_4_line_5 = line5["combined_scrap_4"]
        # combined_scrap_5_line_5 = line5["combined_scrap_5"]
        # combined_scrap_6_line_5 = line5["combined_scrap_6"]
        #
        #
        # line7 = assign_variables(past_seven_days(7))
        # combined_scrap_0_line_7 = line7["combined_scrap_0"]
        # combined_scrap_1_line_7 = line7["combined_scrap_1"]
        # combined_scrap_2_line_7 = line7["combined_scrap_2"]
        # combined_scrap_3_line_7 = line7["combined_scrap_3"]
        # combined_scrap_4_line_7 = line7["combined_scrap_4"]
        # combined_scrap_5_line_7 = line7["combined_scrap_5"]
        # combined_scrap_6_line_7 = line7["combined_scrap_6"]
        #
        #
        # line8 = assign_variables(past_seven_days(8))
        # combined_scrap_0_line_8 = line8["combined_scrap_0"]
        # combined_scrap_1_line_8 = line8["combined_scrap_1"]
        # combined_scrap_2_line_8 = line8["combined_scrap_2"]
        # combined_scrap_3_line_8 = line8["combined_scrap_3"]
        # combined_scrap_4_line_8 = line8["combined_scrap_4"]
        # combined_scrap_5_line_8 = line8["combined_scrap_5"]
        # combined_scrap_6_line_8 = line8["combined_scrap_6"]
        #
        #
        # line9 = assign_variables(past_seven_days(9))
        # combined_scrap_0_line_9 = line9["combined_scrap_0"]
        # combined_scrap_1_line_9 = line9["combined_scrap_1"]
        # combined_scrap_2_line_9 = line9["combined_scrap_2"]
        # combined_scrap_3_line_9 = line9["combined_scrap_3"]
        # combined_scrap_4_line_9 = line9["combined_scrap_4"]
        # combined_scrap_5_line_9 = line9["combined_scrap_5"]
        # combined_scrap_6_line_9 = line9["combined_scrap_6"]
        #
        #
        # line10 = assign_variables(past_seven_days(10))
        # combined_scrap_0_line_10 = line10["combined_scrap_0"]
        # combined_scrap_1_line_10 = line10["combined_scrap_1"]
        # combined_scrap_2_line_10 = line10["combined_scrap_2"]
        # combined_scrap_3_line_10 = line10["combined_scrap_3"]
        # combined_scrap_4_line_10 = line10["combined_scrap_4"]
        # combined_scrap_5_line_10 = line10["combined_scrap_5"]
        # combined_scrap_6_line_10 = line10["combined_scrap_6"]
        #
        # return render(request, "dolcegusto/scrap_rate.html", {
        # "line_3": 3,
        # "line_4": 4,
        # "line_5": 5,
        # "line_7": 7,
        # "line_8": 8,
        # "line_9": 9,
        # "line_10": 10,
        # "combined_scrap_0_line_3": combined_scrap_0_line_3,
        # "combined_scrap_0_line_4": combined_scrap_0_line_4,
        # "combined_scrap_0_line_5": combined_scrap_0_line_5,
        # "combined_scrap_0_line_7": combined_scrap_0_line_7,
        # "combined_scrap_0_line_8": combined_scrap_0_line_8,
        # "combined_scrap_0_line_9": combined_scrap_0_line_9,
        # "combined_scrap_0_line_10": combined_scrap_0_line_10,
        # "day1": day1,
        # "combined_scrap_1_line_3": combined_scrap_1_line_3,
        # "combined_scrap_1_line_4": combined_scrap_1_line_4,
        # "combined_scrap_1_line_5": combined_scrap_1_line_5,
        # "combined_scrap_1_line_7": combined_scrap_1_line_7,
        # "combined_scrap_1_line_8": combined_scrap_1_line_8,
        # "combined_scrap_1_line_9": combined_scrap_1_line_9,
        # "combined_scrap_1_line_10": combined_scrap_1_line_10,
        # "day2": day2,
        # "combined_scrap_2_line_3": combined_scrap_2_line_3,
        # "combined_scrap_2_line_4": combined_scrap_2_line_4,
        # "combined_scrap_2_line_5": combined_scrap_2_line_5,
        # "combined_scrap_2_line_7": combined_scrap_2_line_7,
        # "combined_scrap_2_line_8": combined_scrap_2_line_8,
        # "combined_scrap_2_line_9": combined_scrap_2_line_9,
        # "combined_scrap_2_line_10": combined_scrap_2_line_10,
        # "day3": day3,
        # "combined_scrap_3_line_3": combined_scrap_3_line_3,
        # "combined_scrap_3_line_4": combined_scrap_3_line_4,
        # "combined_scrap_3_line_5": combined_scrap_3_line_5,
        # "combined_scrap_3_line_7": combined_scrap_3_line_7,
        # "combined_scrap_3_line_8": combined_scrap_3_line_8,
        # "combined_scrap_3_line_9": combined_scrap_3_line_9,
        # "combined_scrap_3_line_10": combined_scrap_3_line_10,
        # "day4": day4,
        # "combined_scrap_4_line_3": combined_scrap_4_line_3,
        # "combined_scrap_4_line_4": combined_scrap_4_line_4,
        # "combined_scrap_4_line_5": combined_scrap_4_line_5,
        # "combined_scrap_4_line_7": combined_scrap_4_line_7,
        # "combined_scrap_4_line_8": combined_scrap_4_line_8,
        # "combined_scrap_4_line_9": combined_scrap_4_line_9,
        # "combined_scrap_4_line_10": combined_scrap_4_line_10,
        # "day5": day5,
        # "combined_scrap_5_line_3": combined_scrap_5_line_3,
        # "combined_scrap_5_line_4": combined_scrap_5_line_4,
        # "combined_scrap_5_line_5": combined_scrap_5_line_5,
        # "combined_scrap_5_line_7": combined_scrap_5_line_7,
        # "combined_scrap_5_line_8": combined_scrap_5_line_8,
        # "combined_scrap_5_line_9": combined_scrap_5_line_9,
        # "combined_scrap_5_line_10": combined_scrap_5_line_10,
        # "day6": day6,
        # "combined_scrap_6_line_3": combined_scrap_6_line_3,
        # "combined_scrap_6_line_4": combined_scrap_6_line_4,
        # "combined_scrap_6_line_5": combined_scrap_6_line_5,
        # "combined_scrap_6_line_7": combined_scrap_6_line_7,
        # "combined_scrap_6_line_8": combined_scrap_6_line_8,
        # "combined_scrap_6_line_9": combined_scrap_6_line_9,
        # "combined_scrap_6_line_10": combined_scrap_6_line_10
        # })


class Line3(View):
    model = hourly_report
    def get(self, request):
        print("Hello")


# class Line3(View):
    # model = daily_report
    # def get(self, request):
    #
    #     # This gives the function above an integer which translates to the weekday name
    #     day2 = get_weekday(datetime.strptime(str(daily_report(5).production_day[2])[0:10], '%Y-%m-%d').date().weekday)
    #     day3 = get_weekday(datetime.strptime(str(daily_report(5).production_day[3])[0:10], '%Y-%m-%d').date().weekday)
    #     day4 = get_weekday(datetime.strptime(str(daily_report(5).production_day[4])[0:10], '%Y-%m-%d').date().weekday)
    #     day5 = get_weekday(datetime.strptime(str(daily_report(5).production_day[5])[0:10], '%Y-%m-%d').date().weekday)
    #     day6 = get_weekday(datetime.strptime(str(daily_report(5).production_day[6])[0:10], '%Y-%m-%d').date().weekday)
    #
    #     line3 = assign_variables(get_value_for_machine_per_period(3))
    #
    #     return render(request, "dolcegusto/line3.html", {
    #     "line": 3,
    #     "day2": day2,
    #     "day3": day3,
    #     "day4": day4,
    #     "day5": day5,
    #     "day6": day6,
    #     "combined_scrap_0_a": line3["day0_a"],
    #     "combined_scrap_0_b": line3["day0_b"],
    #     "combined_scrap_1_a": line3["day1_a"],
    #     "combined_scrap_1_b": line3["day1_b"],
    #     "combined_scrap_2_a": line3["day2_a"],
    #     "combined_scrap_2_b": line3["day2_b"],
    #     "combined_scrap_3_a": line3["day3_a"],
    #     "combined_scrap_3_b": line3["day3_b"],
    #     "combined_scrap_4_a": line3["day4_a"],
    #     "combined_scrap_4_b": line3["day4_b"],
    #     "combined_scrap_5_a": line3["day5_a"],
    #     "combined_scrap_5_b": line3["day5_b"],
    #     "combined_scrap_6_a": line3["day6_a"],
    #     "combined_scrap_6_b": line3["day6_b"]
    #     })

class Line4(View):
    model = daily_report
    def get(self, request):

        # This gives the function above an integer which translates to the weekday name
        day2 = get_weekday(datetime.strptime(str(daily_report(5).production_day[2])[0:10], '%Y-%m-%d').date().weekday)
        day3 = get_weekday(datetime.strptime(str(daily_report(5).production_day[3])[0:10], '%Y-%m-%d').date().weekday)
        day4 = get_weekday(datetime.strptime(str(daily_report(5).production_day[4])[0:10], '%Y-%m-%d').date().weekday)
        day5 = get_weekday(datetime.strptime(str(daily_report(5).production_day[5])[0:10], '%Y-%m-%d').date().weekday)
        day6 = get_weekday(datetime.strptime(str(daily_report(5).production_day[6])[0:10], '%Y-%m-%d').date().weekday)

        line4 = assign_variables(past_seven_days(4))

        return render(request, "dolcegusto/line4.html", {
        "line": 4,
        "day2": day2,
        "day3": day3,
        "day4": day4,
        "day5": day5,
        "day6": day6,
        "combined_scrap_0_a": line4["day0_a"],
        "combined_scrap_0_b": line4["day0_b"],
        "combined_scrap_1_a": line4["day1_a"],
        "combined_scrap_1_b": line4["day1_b"],
        "combined_scrap_2_a": line4["day2_a"],
        "combined_scrap_2_b": line4["day2_b"],
        "combined_scrap_3_a": line4["day3_a"],
        "combined_scrap_3_b": line4["day3_b"],
        "combined_scrap_4_a": line4["day4_a"],
        "combined_scrap_4_b": line4["day4_b"],
        "combined_scrap_5_a": line4["day5_a"],
        "combined_scrap_5_b": line4["day5_b"],
        "combined_scrap_6_a": line4["day6_a"],
        "combined_scrap_6_b": line4["day6_b"]
        })

class Line5(View):
    model = daily_report
    def get(self, request):

        # This gives the function above an integer which translates to the weekday name
        day2 = get_weekday(datetime.strptime(str(daily_report(5).production_day[2])[0:10], '%Y-%m-%d').date().weekday)
        day3 = get_weekday(datetime.strptime(str(daily_report(5).production_day[3])[0:10], '%Y-%m-%d').date().weekday)
        day4 = get_weekday(datetime.strptime(str(daily_report(5).production_day[4])[0:10], '%Y-%m-%d').date().weekday)
        day5 = get_weekday(datetime.strptime(str(daily_report(5).production_day[5])[0:10], '%Y-%m-%d').date().weekday)
        day6 = get_weekday(datetime.strptime(str(daily_report(5).production_day[6])[0:10], '%Y-%m-%d').date().weekday)

        line5 = assign_variables(past_seven_days(5))

        return render(request, "dolcegusto/line5.html", {
        "line": 5,
        "day2": day2,
        "day3": day3,
        "day4": day4,
        "day5": day5,
        "day6": day6,
        "combined_scrap_0_a": line5["day0_a"],
        "combined_scrap_0_b": line5["day0_b"],
        "combined_scrap_1_a": line5["day1_a"],
        "combined_scrap_1_b": line5["day1_b"],
        "combined_scrap_2_a": line5["day2_a"],
        "combined_scrap_2_b": line5["day2_b"],
        "combined_scrap_3_a": line5["day3_a"],
        "combined_scrap_3_b": line5["day3_b"],
        "combined_scrap_4_a": line5["day4_a"],
        "combined_scrap_4_b": line5["day4_b"],
        "combined_scrap_5_a": line5["day5_a"],
        "combined_scrap_5_b": line5["day5_b"],
        "combined_scrap_6_a": line5["day6_a"],
        "combined_scrap_6_b": line5["day6_b"]
        })

class Line7(View):
    model = daily_report
    def get(self, request):

        # This gives the function above an integer which translates to the weekday name
        day2 = get_weekday(datetime.strptime(str(daily_report(5).production_day[2])[0:10], '%Y-%m-%d').date().weekday)
        day3 = get_weekday(datetime.strptime(str(daily_report(5).production_day[3])[0:10], '%Y-%m-%d').date().weekday)
        day4 = get_weekday(datetime.strptime(str(daily_report(5).production_day[4])[0:10], '%Y-%m-%d').date().weekday)
        day5 = get_weekday(datetime.strptime(str(daily_report(5).production_day[5])[0:10], '%Y-%m-%d').date().weekday)
        day6 = get_weekday(datetime.strptime(str(daily_report(5).production_day[6])[0:10], '%Y-%m-%d').date().weekday)

        line7 = assign_variables(past_seven_days(7))

        return render(request, "dolcegusto/line7.html", {
        "line": 7,
        "day2": day2,
        "day3": day3,
        "day4": day4,
        "day5": day5,
        "day6": day6,
        "combined_scrap_0_a": line7["day0_a"],
        "combined_scrap_0_b": line7["day0_b"],
        "combined_scrap_1_a": line7["day1_a"],
        "combined_scrap_1_b": line7["day1_b"],
        "combined_scrap_2_a": line7["day2_a"],
        "combined_scrap_2_b": line7["day2_b"],
        "combined_scrap_3_a": line7["day3_a"],
        "combined_scrap_3_b": line7["day3_b"],
        "combined_scrap_4_a": line7["day4_a"],
        "combined_scrap_4_b": line7["day4_b"],
        "combined_scrap_5_a": line7["day5_a"],
        "combined_scrap_5_b": line7["day5_b"],
        "combined_scrap_6_a": line7["day6_a"],
        "combined_scrap_6_b": line7["day6_b"]
        })

class Line8(View):
    model = daily_report
    def get(self, request):

        # This gives the function above an integer which translates to the weekday name
        day2 = get_weekday(datetime.strptime(str(daily_report(5).production_day[2])[0:10], '%Y-%m-%d').date().weekday)
        day3 = get_weekday(datetime.strptime(str(daily_report(5).production_day[3])[0:10], '%Y-%m-%d').date().weekday)
        day4 = get_weekday(datetime.strptime(str(daily_report(5).production_day[4])[0:10], '%Y-%m-%d').date().weekday)
        day5 = get_weekday(datetime.strptime(str(daily_report(5).production_day[5])[0:10], '%Y-%m-%d').date().weekday)
        day6 = get_weekday(datetime.strptime(str(daily_report(5).production_day[6])[0:10], '%Y-%m-%d').date().weekday)

        line8 = assign_variables(past_seven_days(8))

        return render(request, "dolcegusto/line8.html", {
        "line": 8,
        "day2": day2,
        "day3": day3,
        "day4": day4,
        "day5": day5,
        "day6": day6,
        "combined_scrap_0_a": line8["day0_a"],
        "combined_scrap_0_b": line8["day0_b"],
        "combined_scrap_1_a": line8["day1_a"],
        "combined_scrap_1_b": line8["day1_b"],
        "combined_scrap_2_a": line8["day2_a"],
        "combined_scrap_2_b": line8["day2_b"],
        "combined_scrap_3_a": line8["day3_a"],
        "combined_scrap_3_b": line8["day3_b"],
        "combined_scrap_4_a": line8["day4_a"],
        "combined_scrap_4_b": line8["day4_b"],
        "combined_scrap_5_a": line8["day5_a"],
        "combined_scrap_5_b": line8["day5_b"],
        "combined_scrap_6_a": line8["day6_a"],
        "combined_scrap_6_b": line8["day6_b"]
        })

class Line9(View):
    model = daily_report
    def get(self, request):

        # This gives the function above an integer which translates to the weekday name
        day2 = get_weekday(datetime.strptime(str(daily_report(5).production_day[2])[0:10], '%Y-%m-%d').date().weekday)
        day3 = get_weekday(datetime.strptime(str(daily_report(5).production_day[3])[0:10], '%Y-%m-%d').date().weekday)
        day4 = get_weekday(datetime.strptime(str(daily_report(5).production_day[4])[0:10], '%Y-%m-%d').date().weekday)
        day5 = get_weekday(datetime.strptime(str(daily_report(5).production_day[5])[0:10], '%Y-%m-%d').date().weekday)
        day6 = get_weekday(datetime.strptime(str(daily_report(5).production_day[6])[0:10], '%Y-%m-%d').date().weekday)

        line9 = assign_variables(past_seven_days(9))

        return render(request, "dolcegusto/line9.html", {
        "line": 9,
        "day2": day2,
        "day3": day3,
        "day4": day4,
        "day5": day5,
        "day6": day6,
        "combined_scrap_0_a": line9["day0_a"],
        "combined_scrap_0_b": line9["day0_b"],
        "combined_scrap_1_a": line9["day1_a"],
        "combined_scrap_1_b": line9["day1_b"],
        "combined_scrap_2_a": line9["day2_a"],
        "combined_scrap_2_b": line9["day2_b"],
        "combined_scrap_3_a": line9["day3_a"],
        "combined_scrap_3_b": line9["day3_b"],
        "combined_scrap_4_a": line9["day4_a"],
        "combined_scrap_4_b": line9["day4_b"],
        "combined_scrap_5_a": line9["day5_a"],
        "combined_scrap_5_b": line9["day5_b"],
        "combined_scrap_6_a": line9["day6_a"],
        "combined_scrap_6_b": line9["day6_b"]
        })

class Line10(View):
    model = daily_report
    def get(self, request):

        # This gives the function above an integer which translates to the weekday name
        day2 = get_weekday(datetime.strptime(str(daily_report(5).production_day[2])[0:10], '%Y-%m-%d').date().weekday)
        day3 = get_weekday(datetime.strptime(str(daily_report(5).production_day[3])[0:10], '%Y-%m-%d').date().weekday)
        day4 = get_weekday(datetime.strptime(str(daily_report(5).production_day[4])[0:10], '%Y-%m-%d').date().weekday)
        day5 = get_weekday(datetime.strptime(str(daily_report(5).production_day[5])[0:10], '%Y-%m-%d').date().weekday)
        day6 = get_weekday(datetime.strptime(str(daily_report(5).production_day[6])[0:10], '%Y-%m-%d').date().weekday)

        line10 = assign_variables(past_seven_days(10))

        return render(request, "dolcegusto/line10.html", {
        "line": 10,
        "day2": day2,
        "day3": day3,
        "day4": day4,
        "day5": day5,
        "day6": day6,
        "combined_scrap_0_a": line10["day0_a"],
        "combined_scrap_0_b": line10["day0_b"],
        "combined_scrap_1_a": line10["day1_a"],
        "combined_scrap_1_b": line10["day1_b"],
        "combined_scrap_2_a": line10["day2_a"],
        "combined_scrap_2_b": line10["day2_b"],
        "combined_scrap_3_a": line10["day3_a"],
        "combined_scrap_3_b": line10["day3_b"],
        "combined_scrap_4_a": line10["day4_a"],
        "combined_scrap_4_b": line10["day4_b"],
        "combined_scrap_5_a": line10["day5_a"],
        "combined_scrap_5_b": line10["day5_b"],
        "combined_scrap_6_a": line10["day6_a"],
        "combined_scrap_6_b": line10["day6_b"]
        })
