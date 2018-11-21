from django.shortcuts import render
from django.views import View
import pandas as pd
from pandas import DataFrame
from datetime import datetime

from dolcegusto.models import daily_report

class Table(View):
    model = daily_report

    def get(self, request):

        # Function to get a weekday name to display in the html
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

        # This gives the function above an integer which translates to the weekday name
        day0 = get_weekday(datetime.strptime(str(daily_report(5).production_day[0])[0:10], '%Y-%m-%d').date().weekday)
        day1 = get_weekday(datetime.strptime(str(daily_report(5).production_day[1])[0:10], '%Y-%m-%d').date().weekday)
        day2 = get_weekday(datetime.strptime(str(daily_report(5).production_day[2])[0:10], '%Y-%m-%d').date().weekday)
        day3 = get_weekday(datetime.strptime(str(daily_report(5).production_day[3])[0:10], '%Y-%m-%d').date().weekday)
        day4 = get_weekday(datetime.strptime(str(daily_report(5).production_day[4])[0:10], '%Y-%m-%d').date().weekday)
        day5 = get_weekday(datetime.strptime(str(daily_report(5).production_day[5])[0:10], '%Y-%m-%d').date().weekday)
        day6 = get_weekday(datetime.strptime(str(daily_report(5).production_day[6])[0:10], '%Y-%m-%d').date().weekday)


        def get_value_for_machine_per_period(line):

            # get combined reject rate for the whole machine. Rejects for each side + recycles for each side
            # if one side is not running, do not devide final vale by 2

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

        def evaluate_per_side(data_dict):
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
            }
        render_dictionary = {}
        print(evaluate_per_side(get_value_for_machine_per_period(3)))
        line4_scrap = get_value_for_machine_per_period(4)
        line5_scrap = get_value_for_machine_per_period(5)
        line7_scrap = get_value_for_machine_per_period(7)
        line8_scrap = get_value_for_machine_per_period(8)
        line9_scrap = get_value_for_machine_per_period(9)
        line10_scrap = get_value_for_machine_per_period(10)

        return render(request, "dolcegusto/scrap_rate.html", {
        "line_3": 3,
        "line_4": 4,
        "line_5": 5,
        "line_7": 7,
        "line_8": 8,
        "line_9": 9,
        "line_10": 10,
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
        #
        })



class Charts_per_Line(View):
    model = daily_report

    def get(self, request):

        return render(request, "dolcegusto/Charts_per_Line.html", {"chart":"chart"})








            ## statements for Line 3
            # if daily_report(line3).combined_side_a_ng[0] < 0.1 or daily_report(line3).combined_side_b_ng[0] < 0.1:
            #     combined_scrap_0_line_3 = daily_report(line3).combined_side_a_ng[0] + daily_report(line3).combined_side_b_ng[0] + daily_report(line3).combined_side_a_re[0] + daily_report(line3).combined_side_b_re[0]
            # elif daily_report(line3).combined_side_a_ng[0] > 0.1 and daily_report(line3).combined_side_b_ng[0] > 0.1:
            #     combined_scrap_0_line_3 = (daily_report(line3).combined_side_a_ng[0] + daily_report(line3).combined_side_b_ng[0] + daily_report(line3).combined_side_a_re[0] + daily_report(line3).combined_side_b_re[0]) / 2
            #
            # if daily_report(line3).combined_side_a_ng[1] < 0.1 or daily_report(line3).combined_side_b_ng[1] < 0.1:
            #     combined_scrap_1_line_3 = daily_report(line3).combined_side_a_ng[1] + daily_report(line3).combined_side_b_ng[1] + daily_report(line3).combined_side_a_re[1] + daily_report(line3).combined_side_b_re[1]
            # elif daily_report(line3).combined_side_a_ng[1] > 0.1 and daily_report(line3).combined_side_b_ng[1] > 0.1:
            #     combined_scrap_1_line_3 = (daily_report(line3).combined_side_a_ng[1] + daily_report(line3).combined_side_b_ng[1] + daily_report(line3).combined_side_a_re[1] + daily_report(line3).combined_side_b_re[1]) / 2
            #
            # if daily_report(line3).combined_side_a_ng[2] < 0.1 or daily_report(line3).combined_side_b_ng[2] < 0.1:
            #     combined_scrap_2_line_3 = daily_report(line3).combined_side_a_ng[2] + daily_report(line3).combined_side_b_ng[2] + daily_report(line3).combined_side_a_re[2] + daily_report(line3).combined_side_b_re[2]
            # elif daily_report(line3).combined_side_a_ng[2] > 0.1 and daily_report(line3).combined_side_b_ng[2] > 0.1:
            #     combined_scrap_2_line_3 = (daily_report(line3).combined_side_a_ng[2] + daily_report(line3).combined_side_b_ng[2] + daily_report(line3).combined_side_a_re[2] + daily_report(line3).combined_side_b_re[2]) / 2
            #
            # if daily_report(line3).combined_side_a_ng[3] < 0.1 or daily_report(line3).combined_side_b_ng[3] < 0.1:
            #     combined_scrap_3_line_3 = daily_report(line3).combined_side_a_ng[3] + daily_report(line3).combined_side_b_ng[3] + daily_report(line3).combined_side_a_re[3] + daily_report(line3).combined_side_b_re[3]
            # elif daily_report(line3).combined_side_a_ng[3] > 0.1 and daily_report(line3).combined_side_b_ng[3] > 0.1:
            #     combined_scrap_3_line_3 = (daily_report(line3).combined_side_a_ng[3] + daily_report(line3).combined_side_b_ng[3] + daily_report(line3).combined_side_a_re[3] + daily_report(line3).combined_side_b_re[3]) / 2
            #
            # if daily_report(line3).combined_side_a_ng[4] < 0.1 or daily_report(line3).combined_side_b_ng[4] < 0.1:
            #     combined_scrap_4_line_3 = daily_report(line3).combined_side_a_ng[4] + daily_report(line3).combined_side_b_ng[4] + daily_report(line3).combined_side_a_re[4] + daily_report(line3).combined_side_b_re[4]
            # elif daily_report(line3).combined_side_a_ng[4] > 0.1 and daily_report(line3).combined_side_b_ng[4] > 0.1:
            #     combined_scrap_4_line_3 = (daily_report(line3).combined_side_a_ng[4] + daily_report(line3).combined_side_b_ng[4] + daily_report(line3).combined_side_a_re[4] + daily_report(line3).combined_side_b_re[4]) / 2
            #
            # if daily_report(line3).combined_side_a_ng[5] < 0.1 or daily_report(line3).combined_side_b_ng[5] < 0.1:
            #     combined_scrap_5_line_3 = daily_report(line3).combined_side_a_ng[5] + daily_report(line3).combined_side_b_ng[5] + daily_report(line3).combined_side_a_re[5] + daily_report(line3).combined_side_b_re[5]
            # elif daily_report(line3).combined_side_a_ng[5] > 0.1 and daily_report(line3).combined_side_b_ng[5] > 0.1:
            #     combined_scrap_5_line_3 = (daily_report(line3).combined_side_a_ng[5] + daily_report(line3).combined_side_b_ng[5] + daily_report(line3).combined_side_a_re[5] + daily_report(line3).combined_side_b_re[5]) / 2
            #
            # if daily_report(line3).combined_side_a_ng[6] < 0.1 or daily_report(line3).combined_side_b_ng[6] < 0.1:
            #     combined_scrap_6_line_3 = daily_report(line3).combined_side_a_ng[6] + daily_report(line3).combined_side_b_ng[6] + daily_report(line3).combined_side_a_re[6] + daily_report(line3).combined_side_b_re[6]
            # elif daily_report(line3).combined_side_a_ng[6] > 0.1 and daily_report(line3).combined_side_b_ng[6] > 0.1:
            #     combined_scrap_6_line_3 = (daily_report(line3).combined_side_a_ng[6] + daily_report(line3).combined_side_b_ng[6] + daily_report(line3).combined_side_a_re[6] + daily_report(line3).combined_side_b_re[6]) / 2
            #
            #
            # # statements for Line 4
            # if daily_report(line4).combined_side_a_ng[0] < 0.1 or daily_report(line4).combined_side_b_ng[0] < 0.1:
            #     combined_scrap_0_line_4 = daily_report(line4).combined_side_a_ng[0] + daily_report(line4).combined_side_b_ng[0] + daily_report(line4).combined_side_a_re[0] + daily_report(line4).combined_side_b_re[0]
            # elif daily_report(line4).combined_side_a_ng[0] > 0.1 and daily_report(line4).combined_side_b_ng[0] > 0.1:
            #     combined_scrap_0_line_4 = (daily_report(line4).combined_side_a_ng[0] + daily_report(line4).combined_side_b_ng[0] + daily_report(line4).combined_side_a_re[0] + daily_report(line4).combined_side_b_re[0]) / 2
            #
            # if daily_report(line4).combined_side_a_ng[1] < 0.1 or daily_report(line4).combined_side_b_ng[1] < 0.1:
            #     combined_scrap_1_line_4 = daily_report(line4).combined_side_a_ng[1] + daily_report(line4).combined_side_b_ng[1] + daily_report(line4).combined_side_a_re[1] + daily_report(line4).combined_side_b_re[1]
            # elif daily_report(line4).combined_side_a_ng[1] > 0.1 and daily_report(line4).combined_side_b_ng[1] > 0.1:
            #     combined_scrap_1_line_4 = (daily_report(line4).combined_side_a_ng[1] + daily_report(line4).combined_side_b_ng[1] + daily_report(line4).combined_side_a_re[1] + daily_report(line4).combined_side_b_re[1]) / 2
            #
            # if daily_report(line4).combined_side_a_ng[2] < 0.1 or daily_report(line4).combined_side_b_ng[2] < 0.1:
            #     combined_scrap_2_line_4 = daily_report(line4).combined_side_a_ng[2] + daily_report(line4).combined_side_b_ng[2] + daily_report(line4).combined_side_a_re[2] + daily_report(line4).combined_side_b_re[2]
            # elif daily_report(line4).combined_side_a_ng[2] > 0.1 and daily_report(line4).combined_side_b_ng[2] > 0.1:
            #     combined_scrap_2_line_4 = (daily_report(line4).combined_side_a_ng[2] + daily_report(line4).combined_side_b_ng[2] + daily_report(line4).combined_side_a_re[2] + daily_report(line4).combined_side_b_re[2]) / 2
            #
            # if daily_report(line4).combined_side_a_ng[3] < 0.1 or daily_report(line4).combined_side_b_ng[3] < 0.1:
            #     combined_scrap_3_line_4 = daily_report(line4).combined_side_a_ng[3] + daily_report(line4).combined_side_b_ng[3] + daily_report(line4).combined_side_a_re[3] + daily_report(line4).combined_side_b_re[3]
            # elif daily_report(line4).combined_side_a_ng[3] > 0.1 and daily_report(line4).combined_side_b_ng[3] > 0.1:
            #     combined_scrap_3_line_4 = (daily_report(line4).combined_side_a_ng[3] + daily_report(line4).combined_side_b_ng[3] + daily_report(line4).combined_side_a_re[3] + daily_report(line4).combined_side_b_re[3]) / 2
            #
            # if daily_report(line4).combined_side_a_ng[4] < 0.1 or daily_report(line4).combined_side_b_ng[4] < 0.1:
            #     combined_scrap_4_line_4 = daily_report(line4).combined_side_a_ng[4] + daily_report(line4).combined_side_b_ng[4] + daily_report(line4).combined_side_a_re[4] + daily_report(line4).combined_side_b_re[4]
            # elif daily_report(line4).combined_side_a_ng[4] > 0.1 and daily_report(line4).combined_side_b_ng[4] > 0.1:
            #     combined_scrap_4_line_4 = (daily_report(line4).combined_side_a_ng[4] + daily_report(line4).combined_side_b_ng[4] + daily_report(line4).combined_side_a_re[4] + daily_report(line4).combined_side_b_re[4]) / 2
            #
            # if daily_report(line4).combined_side_a_ng[5] < 0.1 or daily_report(line4).combined_side_b_ng[5] < 0.1:
            #     combined_scrap_5_line_4 = daily_report(line4).combined_side_a_ng[5] + daily_report(line4).combined_side_b_ng[5] + daily_report(line4).combined_side_a_re[5] + daily_report(line4).combined_side_b_re[5]
            # elif daily_report(line4).combined_side_a_ng[5] > 0.1 and daily_report(line4).combined_side_b_ng[5] > 0.1:
            #     combined_scrap_5_line_4 = (daily_report(line4).combined_side_a_ng[5] + daily_report(line4).combined_side_b_ng[5] + daily_report(line4).combined_side_a_re[5] + daily_report(line4).combined_side_b_re[5]) / 2
            #
            # if daily_report(line4).combined_side_a_ng[6] < 0.1 or daily_report(line4).combined_side_b_ng[6] < 0.1:
            #     combined_scrap_6_line_4 = daily_report(line4).combined_side_a_ng[6] + daily_report(line4).combined_side_b_ng[6] + daily_report(line4).combined_side_a_re[6] + daily_report(line4).combined_side_b_re[6]
            # elif daily_report(line4).combined_side_a_ng[6] > 0.1 and daily_report(line4).combined_side_b_ng[6] > 0.1:
            #     combined_scrap_6_line_4 = (daily_report(line4).combined_side_a_ng[6] + daily_report(line4).combined_side_b_ng[6] + daily_report(line4).combined_side_a_re[6] + daily_report(line4).combined_side_b_re[6]) / 2
            #
            #
            # # statements for Line 5
            # if daily_report(line5).combined_side_a_ng[0] < 0.1 or daily_report(line5).combined_side_b_ng[0] < 0.1:
            #     combined_scrap_0_line_5 = daily_report(line5).combined_side_a_ng[0] + daily_report(line5).combined_side_b_ng[0] + daily_report(line5).combined_side_a_re[0] + daily_report(line5).combined_side_b_re[0]
            # elif daily_report(line5).combined_side_a_ng[0] > 0.1 and daily_report(line5).combined_side_b_ng[0] > 0.1:
            #     combined_scrap_0_line_5 = (daily_report(line5).combined_side_a_ng[0] + daily_report(line5).combined_side_b_ng[0] + daily_report(line5).combined_side_a_re[0] + daily_report(line5).combined_side_b_re[0]) / 2
            #
            # if daily_report(line5).combined_side_a_ng[1] < 0.1 or daily_report(line5).combined_side_b_ng[1] < 0.1:
            #     combined_scrap_1_line_5 = daily_report(line5).combined_side_a_ng[1] + daily_report(line5).combined_side_b_ng[1] + daily_report(line5).combined_side_a_re[1] + daily_report(line5).combined_side_b_re[1]
            # elif daily_report(line5).combined_side_a_ng[1] > 0.1 and daily_report(line5).combined_side_b_ng[1] > 0.1:
            #     combined_scrap_1_line_5 = (daily_report(line5).combined_side_a_ng[1] + daily_report(line5).combined_side_b_ng[1] + daily_report(line5).combined_side_a_re[1] + daily_report(line5).combined_side_b_re[1]) / 2
            #
            # if daily_report(line5).combined_side_a_ng[2] < 0.1 or daily_report(line5).combined_side_b_ng[2] < 0.1:
            #     combined_scrap_2_line_5 = daily_report(line5).combined_side_a_ng[2] + daily_report(line5).combined_side_b_ng[2] + daily_report(line5).combined_side_a_re[2] + daily_report(line5).combined_side_b_re[2]
            # elif daily_report(line5).combined_side_a_ng[2] > 0.1 and daily_report(line5).combined_side_b_ng[2] > 0.1:
            #     combined_scrap_2_line_5 = (daily_report(line5).combined_side_a_ng[2] + daily_report(line5).combined_side_b_ng[2] + daily_report(line5).combined_side_a_re[2] + daily_report(line5).combined_side_b_re[2]) / 2
            #
            # if daily_report(line5).combined_side_a_ng[3] < 0.1 or daily_report(line5).combined_side_b_ng[3] < 0.1:
            #     combined_scrap_3_line_5 = daily_report(line5).combined_side_a_ng[3] + daily_report(line5).combined_side_b_ng[3] + daily_report(line5).combined_side_a_re[3] + daily_report(line5).combined_side_b_re[3]
            # elif daily_report(line5).combined_side_a_ng[3] > 0.1 and daily_report(line5).combined_side_b_ng[3] > 0.1:
            #     combined_scrap_3_line_5 = (daily_report(line5).combined_side_a_ng[3] + daily_report(line5).combined_side_b_ng[3] + daily_report(line5).combined_side_a_re[3] + daily_report(line5).combined_side_b_re[3]) / 2
            #
            # if daily_report(line5).combined_side_a_ng[4] < 0.1 or daily_report(line5).combined_side_b_ng[4] < 0.1:
            #     combined_scrap_4_line_5 = daily_report(line5).combined_side_a_ng[4] + daily_report(line5).combined_side_b_ng[4] + daily_report(line5).combined_side_a_re[4] + daily_report(line5).combined_side_b_re[4]
            # elif daily_report(line5).combined_side_a_ng[4] > 0.1 and daily_report(line5).combined_side_b_ng[4] > 0.1:
            #     combined_scrap_4_line_5 = (daily_report(line5).combined_side_a_ng[4] + daily_report(line5).combined_side_b_ng[4] + daily_report(line5).combined_side_a_re[4] + daily_report(line5).combined_side_b_re[4]) / 2
            #
            # if daily_report(line5).combined_side_a_ng[5] < 0.1 or daily_report(line5).combined_side_b_ng[5] < 0.1:
            #     combined_scrap_5_line_5 = daily_report(line5).combined_side_a_ng[5] + daily_report(line5).combined_side_b_ng[5] + daily_report(line5).combined_side_a_re[5] + daily_report(line5).combined_side_b_re[5]
            # elif daily_report(line5).combined_side_a_ng[5] > 0.1 and daily_report(line5).combined_side_b_ng[5] > 0.1:
            #     combined_scrap_5_line_5 = (daily_report(line5).combined_side_a_ng[5] + daily_report(line5).combined_side_b_ng[5] + daily_report(line5).combined_side_a_re[5] + daily_report(line5).combined_side_b_re[5]) / 2
            #
            # if daily_report(line5).combined_side_a_ng[6] < 0.1 or daily_report(line5).combined_side_b_ng[6] < 0.1:
            #     combined_scrap_6_line_5 = daily_report(line5).combined_side_a_ng[6] + daily_report(line5).combined_side_b_ng[6] + daily_report(line5).combined_side_a_re[6] + daily_report(line5).combined_side_b_re[6]
            # elif daily_report(line5).combined_side_a_ng[6] > 0.1 and daily_report(line5).combined_side_b_ng[6] > 0.1:
            #     combined_scrap_6_line_5 = (daily_report(line5).combined_side_a_ng[6] + daily_report(line5).combined_side_b_ng[6] + daily_report(line5).combined_side_a_re[6] + daily_report(line5).combined_side_b_re[6]) / 2
            #
            #
            #
            # # statements for Line 7
            # if daily_report(line7).combined_side_a_ng[0] < 0.1 or daily_report(line7).combined_side_b_ng[0] < 0.1:
            #     combined_scrap_0_line_7 = daily_report(line7).combined_side_a_ng[0] + daily_report(line7).combined_side_b_ng[0] + daily_report(line7).combined_side_a_re[0] + daily_report(line7).combined_side_b_re[0]
            # elif daily_report(line7).combined_side_a_ng[0] > 0.1 and daily_report(line7).combined_side_b_ng[0] > 0.1:
            #     combined_scrap_0_line_7 = (daily_report(line7).combined_side_a_ng[0] + daily_report(line7).combined_side_b_ng[0] + daily_report(line7).combined_side_a_re[0] + daily_report(line7).combined_side_b_re[0]) / 2
            #
            # if daily_report(line7).combined_side_a_ng[1] < 0.1 or daily_report(line7).combined_side_b_ng[1] < 0.1:
            #     combined_scrap_1_line_7 = daily_report(line7).combined_side_a_ng[1] + daily_report(line7).combined_side_b_ng[1] + daily_report(line7).combined_side_a_re[1] + daily_report(line7).combined_side_b_re[1]
            # elif daily_report(line7).combined_side_a_ng[1] > 0.1 and daily_report(line7).combined_side_b_ng[1] > 0.1:
            #     combined_scrap_1_line_7 = (daily_report(line7).combined_side_a_ng[1] + daily_report(line7).combined_side_b_ng[1] + daily_report(line7).combined_side_a_re[1] + daily_report(line7).combined_side_b_re[1]) / 2
            #
            # if daily_report(line7).combined_side_a_ng[2] < 0.1 or daily_report(line7).combined_side_b_ng[2] < 0.1:
            #     combined_scrap_2_line_7 = daily_report(line7).combined_side_a_ng[2] + daily_report(line7).combined_side_b_ng[2] + daily_report(line7).combined_side_a_re[2] + daily_report(line7).combined_side_b_re[2]
            # elif daily_report(line7).combined_side_a_ng[2] > 0.1 and daily_report(line7).combined_side_b_ng[2] > 0.1:
            #     combined_scrap_2_line_7 = (daily_report(line7).combined_side_a_ng[2] + daily_report(line7).combined_side_b_ng[2] + daily_report(line7).combined_side_a_re[2] + daily_report(line7).combined_side_b_re[2]) / 2
            #
            # if daily_report(line7).combined_side_a_ng[3] < 0.1 or daily_report(line7).combined_side_b_ng[3] < 0.1:
            #     combined_scrap_3_line_7 = daily_report(line7).combined_side_a_ng[3] + daily_report(line7).combined_side_b_ng[3] + daily_report(line7).combined_side_a_re[3] + daily_report(line7).combined_side_b_re[3]
            # elif daily_report(line7).combined_side_a_ng[3] > 0.1 and daily_report(line7).combined_side_b_ng[3] > 0.1:
            #     combined_scrap_3_line_7 = (daily_report(line7).combined_side_a_ng[3] + daily_report(line7).combined_side_b_ng[3] + daily_report(line7).combined_side_a_re[3] + daily_report(line7).combined_side_b_re[3]) / 2
            #
            # if daily_report(line7).combined_side_a_ng[4] < 0.1 or daily_report(line7).combined_side_b_ng[4] < 0.1:
            #     combined_scrap_4_line_7 = daily_report(line7).combined_side_a_ng[4] + daily_report(line7).combined_side_b_ng[4] + daily_report(line7).combined_side_a_re[4] + daily_report(line7).combined_side_b_re[4]
            # elif daily_report(line7).combined_side_a_ng[4] > 0.1 and daily_report(line7).combined_side_b_ng[4] > 0.1:
            #     combined_scrap_4_line_7 = (daily_report(line7).combined_side_a_ng[4] + daily_report(line7).combined_side_b_ng[4] + daily_report(line7).combined_side_a_re[4] + daily_report(line7).combined_side_b_re[4]) / 2
            #
            # if daily_report(line7).combined_side_a_ng[5] < 0.1 or daily_report(line7).combined_side_b_ng[5] < 0.1:
            #     combined_scrap_5_line_7 = daily_report(line7).combined_side_a_ng[5] + daily_report(line7).combined_side_b_ng[5] + daily_report(line7).combined_side_a_re[5] + daily_report(line7).combined_side_b_re[5]
            # elif daily_report(line7).combined_side_a_ng[5] > 0.1 and daily_report(line7).combined_side_b_ng[5] > 0.1:
            #     combined_scrap_5_line_7 = (daily_report(line7).combined_side_a_ng[5] + daily_report(line7).combined_side_b_ng[5] + daily_report(line7).combined_side_a_re[5] + daily_report(line7).combined_side_b_re[5]) / 2
            #
            # if daily_report(line7).combined_side_a_ng[6] < 0.1 or daily_report(line7).combined_side_b_ng[6] < 0.1:
            #     combined_scrap_6_line_7 = daily_report(line7).combined_side_a_ng[6] + daily_report(line7).combined_side_b_ng[6] + daily_report(line7).combined_side_a_re[6] + daily_report(line7).combined_side_b_re[6]
            # elif daily_report(line7).combined_side_a_ng[6] > 0.1 and daily_report(line7).combined_side_b_ng[6] > 0.1:
            #     combined_scrap_6_line_7 = (daily_report(line7).combined_side_a_ng[6] + daily_report(line7).combined_side_b_ng[6] + daily_report(line7).combined_side_a_re[6] + daily_report(line7).combined_side_b_re[6]) / 2
            #
            #
            # # statements for Line 8
            # if daily_report(line8).combined_side_a_ng[0] < 0.1 or daily_report(line8).combined_side_b_ng[0] < 0.1:
            #     combined_scrap_0_line_8 = daily_report(line8).combined_side_a_ng[0] + daily_report(line8).combined_side_b_ng[0] + daily_report(line8).combined_side_a_re[0] + daily_report(line8).combined_side_b_re[0]
            # elif daily_report(line8).combined_side_a_ng[0] > 0.1 and daily_report(line8).combined_side_b_ng[0] > 0.1:
            #     combined_scrap_0_line_8 = (daily_report(line8).combined_side_a_ng[0] + daily_report(line8).combined_side_b_ng[0] + daily_report(line8).combined_side_a_re[0] + daily_report(line8).combined_side_b_re[0]) / 2
            #
            # if daily_report(line8).combined_side_a_ng[1] < 0.1 or daily_report(line8).combined_side_b_ng[1] < 0.1:
            #     combined_scrap_1_line_8 = daily_report(line8).combined_side_a_ng[1] + daily_report(line8).combined_side_b_ng[1] + daily_report(line8).combined_side_a_re[1] + daily_report(line8).combined_side_b_re[1]
            # elif daily_report(line8).combined_side_a_ng[1] > 0.1 and daily_report(line8).combined_side_b_ng[1] > 0.1:
            #     combined_scrap_1_line_8 = (daily_report(line8).combined_side_a_ng[1] + daily_report(line8).combined_side_b_ng[1] + daily_report(line8).combined_side_a_re[1] + daily_report(line8).combined_side_b_re[1]) / 2
            #
            # if daily_report(line8).combined_side_a_ng[2] < 0.1 or daily_report(line8).combined_side_b_ng[2] < 0.1:
            #     combined_scrap_2_line_8 = daily_report(line8).combined_side_a_ng[2] + daily_report(line8).combined_side_b_ng[2] + daily_report(line8).combined_side_a_re[2] + daily_report(line8).combined_side_b_re[2]
            # elif daily_report(line8).combined_side_a_ng[2] > 0.1 and daily_report(line8).combined_side_b_ng[2] > 0.1:
            #     combined_scrap_2_line_8 = (daily_report(line8).combined_side_a_ng[2] + daily_report(line8).combined_side_b_ng[2] + daily_report(line8).combined_side_a_re[2] + daily_report(line8).combined_side_b_re[2]) / 2
            #
            # if daily_report(line8).combined_side_a_ng[3] < 0.1 or daily_report(line8).combined_side_b_ng[3] < 0.1:
            #     combined_scrap_3_line_8 = daily_report(line8).combined_side_a_ng[3] + daily_report(line8).combined_side_b_ng[3] + daily_report(line8).combined_side_a_re[3] + daily_report(line8).combined_side_b_re[3]
            # elif daily_report(line8).combined_side_a_ng[3] > 0.1 and daily_report(line8).combined_side_b_ng[3] > 0.1:
            #     combined_scrap_3_line_8 = (daily_report(line8).combined_side_a_ng[3] + daily_report(line8).combined_side_b_ng[3] + daily_report(line8).combined_side_a_re[3] + daily_report(line8).combined_side_b_re[3]) / 2
            #
            # if daily_report(line8).combined_side_a_ng[4] < 0.1 or daily_report(line8).combined_side_b_ng[4] < 0.1:
            #     combined_scrap_4_line_8 = daily_report(line8).combined_side_a_ng[4] + daily_report(line8).combined_side_b_ng[4] + daily_report(line8).combined_side_a_re[4] + daily_report(line8).combined_side_b_re[4]
            # elif daily_report(line8).combined_side_a_ng[4] > 0.1 and daily_report(line8).combined_side_b_ng[4] > 0.1:
            #     combined_scrap_4_line_8 = (daily_report(line8).combined_side_a_ng[4] + daily_report(line8).combined_side_b_ng[4] + daily_report(line8).combined_side_a_re[4] + daily_report(line8).combined_side_b_re[4]) / 2
            #
            # if daily_report(line8).combined_side_a_ng[5] < 0.1 or daily_report(line8).combined_side_b_ng[5] < 0.1:
            #     combined_scrap_5_line_8 = daily_report(line8).combined_side_a_ng[5] + daily_report(line8).combined_side_b_ng[5] + daily_report(line8).combined_side_a_re[5] + daily_report(line8).combined_side_b_re[5]
            # elif daily_report(line8).combined_side_a_ng[5] > 0.1 and daily_report(line8).combined_side_b_ng[5] > 0.1:
            #     combined_scrap_5_line_8 = (daily_report(line8).combined_side_a_ng[5] + daily_report(line8).combined_side_b_ng[5] + daily_report(line8).combined_side_a_re[5] + daily_report(line8).combined_side_b_re[5]) / 2
            #
            # if daily_report(line8).combined_side_a_ng[6] < 0.1 or daily_report(line8).combined_side_b_ng[6] < 0.1:
            #     combined_scrap_6_line_8 = daily_report(line8).combined_side_a_ng[6] + daily_report(line8).combined_side_b_ng[6] + daily_report(line8).combined_side_a_re[6] + daily_report(line8).combined_side_b_re[6]
            # elif daily_report(line8).combined_side_a_ng[6] > 0.1 and daily_report(line8).combined_side_b_ng[6] > 0.1:
            #     combined_scrap_6_line_8 = (daily_report(line8).combined_side_a_ng[6] + daily_report(line8).combined_side_b_ng[6] + daily_report(line8).combined_side_a_re[6] + daily_report(line8).combined_side_b_re[6]) / 2
            #
            #
            #
            # # statements for Line 9
            # if daily_report(line9).combined_side_a_ng[0] < 0.1 or daily_report(line9).combined_side_b_ng[0] < 0.1:
            #     combined_scrap_0_line_9 = daily_report(line9).combined_side_a_ng[0] + daily_report(line9).combined_side_b_ng[0] + daily_report(line9).combined_side_a_re[0] + daily_report(line9).combined_side_b_re[0]
            # elif daily_report(line9).combined_side_a_ng[0] > 0.1 and daily_report(line9).combined_side_b_ng[0] > 0.1:
            #     combined_scrap_0_line_9 = (daily_report(line9).combined_side_a_ng[0] + daily_report(line9).combined_side_b_ng[0] + daily_report(line9).combined_side_a_re[0] + daily_report(line9).combined_side_b_re[0]) / 2
            #
            # if daily_report(line9).combined_side_a_ng[1] < 0.1 or daily_report(line9).combined_side_b_ng[1] < 0.1:
            #     combined_scrap_1_line_9 = daily_report(line9).combined_side_a_ng[1] + daily_report(line9).combined_side_b_ng[1] + daily_report(line9).combined_side_a_re[1] + daily_report(line9).combined_side_b_re[1]
            # elif daily_report(line9).combined_side_a_ng[1] > 0.1 and daily_report(line9).combined_side_b_ng[1] > 0.1:
            #     combined_scrap_1_line_9 = (daily_report(line9).combined_side_a_ng[1] + daily_report(line9).combined_side_b_ng[1] + daily_report(line9).combined_side_a_re[1] + daily_report(line9).combined_side_b_re[1]) / 2
            #
            # if daily_report(line9).combined_side_a_ng[2] < 0.1 or daily_report(line9).combined_side_b_ng[2] < 0.1:
            #     combined_scrap_2_line_9 = daily_report(line9).combined_side_a_ng[2] + daily_report(line9).combined_side_b_ng[2] + daily_report(line9).combined_side_a_re[2] + daily_report(line9).combined_side_b_re[2]
            # elif daily_report(line9).combined_side_a_ng[2] > 0.1 and daily_report(line9).combined_side_b_ng[2] > 0.1:
            #     combined_scrap_2_line_9 = (daily_report(line9).combined_side_a_ng[2] + daily_report(line9).combined_side_b_ng[2] + daily_report(line9).combined_side_a_re[2] + daily_report(line9).combined_side_b_re[2]) / 2
            #
            # if daily_report(line9).combined_side_a_ng[3] < 0.1 or daily_report(line9).combined_side_b_ng[3] < 0.1:
            #     combined_scrap_3_line_9 = daily_report(line9).combined_side_a_ng[3] + daily_report(line9).combined_side_b_ng[3] + daily_report(line9).combined_side_a_re[3] + daily_report(line9).combined_side_b_re[3]
            # elif daily_report(line9).combined_side_a_ng[3] > 0.1 and daily_report(line9).combined_side_b_ng[3] > 0.1:
            #     combined_scrap_3_line_9 = (daily_report(line9).combined_side_a_ng[3] + daily_report(line9).combined_side_b_ng[3] + daily_report(line9).combined_side_a_re[3] + daily_report(line9).combined_side_b_re[3]) / 2
            #
            # if daily_report(line9).combined_side_a_ng[4] < 0.1 or daily_report(line9).combined_side_b_ng[4] < 0.1:
            #     combined_scrap_4_line_9 = daily_report(line9).combined_side_a_ng[4] + daily_report(line9).combined_side_b_ng[4] + daily_report(line9).combined_side_a_re[4] + daily_report(line9).combined_side_b_re[4]
            # elif daily_report(line9).combined_side_a_ng[4] > 0.1 and daily_report(line9).combined_side_b_ng[4] > 0.1:
            #     combined_scrap_4_line_9 = (daily_report(line9).combined_side_a_ng[4] + daily_report(line9).combined_side_b_ng[4] + daily_report(line9).combined_side_a_re[4] + daily_report(line9).combined_side_b_re[4]) / 2
            #
            # if daily_report(line9).combined_side_a_ng[5] < 0.1 or daily_report(line9).combined_side_b_ng[5] < 0.1:
            #     combined_scrap_5_line_9 = daily_report(line9).combined_side_a_ng[5] + daily_report(line9).combined_side_b_ng[5] + daily_report(line9).combined_side_a_re[5] + daily_report(line9).combined_side_b_re[5]
            # elif daily_report(line9).combined_side_a_ng[5] > 0.1 and daily_report(line9).combined_side_b_ng[5] > 0.1:
            #     combined_scrap_5_line_9 = (daily_report(line9).combined_side_a_ng[5] + daily_report(line9).combined_side_b_ng[5] + daily_report(line9).combined_side_a_re[5] + daily_report(line9).combined_side_b_re[5]) / 2
            #
            # if daily_report(line9).combined_side_a_ng[6] < 0.1 or daily_report(line9).combined_side_b_ng[6] < 0.1:
            #     combined_scrap_6_line_9 = daily_report(line9).combined_side_a_ng[6] + daily_report(line9).combined_side_b_ng[6] + daily_report(line9).combined_side_a_re[6] + daily_report(line9).combined_side_b_re[6]
            # elif daily_report(line9).combined_side_a_ng[6] > 0.1 and daily_report(line9).combined_side_b_ng[6] > 0.1:
            #     combined_scrap_6_line_9 = (daily_report(line9).combined_side_a_ng[6] + daily_report(line9).combined_side_b_ng[6] + daily_report(line9).combined_side_a_re[6] + daily_report(line9).combined_side_b_re[6]) / 2
            #
            #
            #
            # # statements for Line 10
            # if daily_report(line10).combined_side_a_ng[0] < 0.1 or daily_report(line10).combined_side_b_ng[0] < 0.1:
            #     combined_scrap_0_line_10 = daily_report(line10).combined_side_a_ng[0] + daily_report(line10).combined_side_b_ng[0] + daily_report(line10).combined_side_a_re[0] + daily_report(line10).combined_side_b_re[0]
            # elif daily_report(line10).combined_side_a_ng[0] > 0.1 and daily_report(line10).combined_side_b_ng[0] > 0.1:
            #     combined_scrap_0_line_10 = (daily_report(line10).combined_side_a_ng[0] + daily_report(line10).combined_side_b_ng[0] + daily_report(line10).combined_side_a_re[0] + daily_report(line10).combined_side_b_re[0]) / 2
            #
            # if daily_report(line10).combined_side_a_ng[1] < 0.1 or daily_report(line10).combined_side_b_ng[1] < 0.1:
            #     combined_scrap_1_line_10 = daily_report(line10).combined_side_a_ng[1] + daily_report(line10).combined_side_b_ng[1] + daily_report(line10).combined_side_a_re[1] + daily_report(line10).combined_side_b_re[1]
            # elif daily_report(line10).combined_side_a_ng[1] > 0.1 and daily_report(line10).combined_side_b_ng[1] > 0.1:
            #     combined_scrap_1_line_10 = (daily_report(line10).combined_side_a_ng[1] + daily_report(line10).combined_side_b_ng[1] + daily_report(line10).combined_side_a_re[1] + daily_report(line10).combined_side_b_re[1]) / 2
            #
            # if daily_report(line10).combined_side_a_ng[2] < 0.1 or daily_report(line10).combined_side_b_ng[2] < 0.1:
            #     combined_scrap_2_line_10 = daily_report(line10).combined_side_a_ng[2] + daily_report(line10).combined_side_b_ng[2] + daily_report(line10).combined_side_a_re[2] + daily_report(line10).combined_side_b_re[2]
            # elif daily_report(line10).combined_side_a_ng[2] > 0.1 and daily_report(line10).combined_side_b_ng[2] > 0.1:
            #     combined_scrap_2_line_10 = (daily_report(line10).combined_side_a_ng[2] + daily_report(line10).combined_side_b_ng[2] + daily_report(line10).combined_side_a_re[2] + daily_report(line10).combined_side_b_re[2]) / 2
            #
            # if daily_report(line10).combined_side_a_ng[3] < 0.1 or daily_report(line10).combined_side_b_ng[3] < 0.1:
            #     combined_scrap_3_line_10 = daily_report(line10).combined_side_a_ng[3] + daily_report(line10).combined_side_b_ng[3] + daily_report(line10).combined_side_a_re[3] + daily_report(line10).combined_side_b_re[3]
            # elif daily_report(line10).combined_side_a_ng[3] > 0.1 and daily_report(line10).combined_side_b_ng[3] > 0.1:
            #     combined_scrap_3_line_10 = (daily_report(line10).combined_side_a_ng[3] + daily_report(line10).combined_side_b_ng[3] + daily_report(line10).combined_side_a_re[3] + daily_report(line10).combined_side_b_re[3]) / 2
            #
            # if daily_report(line10).combined_side_a_ng[4] < 0.1 or daily_report(line10).combined_side_b_ng[4] < 0.1:
            #     combined_scrap_4_line_10 = daily_report(line10).combined_side_a_ng[4] + daily_report(line10).combined_side_b_ng[4] + daily_report(line10).combined_side_a_re[4] + daily_report(line10).combined_side_b_re[4]
            # elif daily_report(line10).combined_side_a_ng[4] > 0.1 and daily_report(line10).combined_side_b_ng[4] > 0.1:
            #     combined_scrap_4_line_10 = (daily_report(line10).combined_side_a_ng[4] + daily_report(line10).combined_side_b_ng[4] + daily_report(line10).combined_side_a_re[4] + daily_report(line10).combined_side_b_re[4]) / 2
            #
            # if daily_report(line10).combined_side_a_ng[5] < 0.1 or daily_report(line10).combined_side_b_ng[5] < 0.1:
            #     combined_scrap_5_line_10 = daily_report(line10).combined_side_a_ng[5] + daily_report(line10).combined_side_b_ng[5] + daily_report(line10).combined_side_a_re[5] + daily_report(line10).combined_side_b_re[5]
            # elif daily_report(line10).combined_side_a_ng[5] > 0.1 and daily_report(line10).combined_side_b_ng[5] > 0.1:
            #     combined_scrap_5_line_10 = (daily_report(line10).combined_side_a_ng[5] + daily_report(line10).combined_side_b_ng[5] + daily_report(line10).combined_side_a_re[5] + daily_report(line10).combined_side_b_re[5]) / 2
            #
            # if daily_report(line10).combined_side_a_ng[6] < 0.1 or daily_report(line10).combined_side_b_ng[6] < 0.1:
            #     combined_scrap_6_line_10 = daily_report(line10).combined_side_a_ng[6] + daily_report(line10).combined_side_b_ng[6] + daily_report(line10).combined_side_a_re[6] + daily_report(line10).combined_side_b_re[6]
            # elif daily_report(line10).combined_side_a_ng[6] > 0.1 and daily_report(line10).combined_side_b_ng[6] > 0.1:
            #     combined_scrap_6_line_10 = (daily_report(line10).combined_side_a_ng[6] + daily_report(line10).combined_side_b_ng[6] + daily_report(line10).combined_side_a_re[6] + daily_report(line10).combined_side_b_re[6]) / 2
