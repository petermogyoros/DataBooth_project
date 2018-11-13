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


        def render_per_line(line3, line4, line5, line7, line8, line9, line10):

            # get combined reject rate for the whole machine. Rejects for each side + recycles for each side
            # if one side is not running, do not devide final vale by 2

            # statements for Line 3
            if daily_report(line3).combined_side_a_ng[0] < 0.1 or daily_report(line3).combined_side_b_ng[0] < 0.1:
                combined_scrap_0_line_3 = daily_report(line3).combined_side_a_ng[0] + daily_report(line3).combined_side_b_ng[0] + daily_report(line3).combined_side_a_re[0] + daily_report(line3).combined_side_b_re[0]
            elif daily_report(line3).combined_side_a_ng[0] > 0.1 and daily_report(line3).combined_side_b_ng[0] > 0.1:
                combined_scrap_0_line_3 = (daily_report(line3).combined_side_a_ng[0] + daily_report(line3).combined_side_b_ng[0] + daily_report(line3).combined_side_a_re[0] + daily_report(line3).combined_side_b_re[0]) / 2

            if daily_report(line3).combined_side_a_ng[1] < 0.1 or daily_report(line3).combined_side_b_ng[1] < 0.1:
                combined_scrap_1_line_3 = daily_report(line3).combined_side_a_ng[1] + daily_report(line3).combined_side_b_ng[1] + daily_report(line3).combined_side_a_re[1] + daily_report(line3).combined_side_b_re[1]
            elif daily_report(line3).combined_side_a_ng[1] > 0.1 and daily_report(line3).combined_side_b_ng[1] > 0.1:
                combined_scrap_1_line_3 = (daily_report(line3).combined_side_a_ng[1] + daily_report(line3).combined_side_b_ng[1] + daily_report(line3).combined_side_a_re[1] + daily_report(line3).combined_side_b_re[1]) / 2

            if daily_report(line3).combined_side_a_ng[2] < 0.1 or daily_report(line3).combined_side_b_ng[2] < 0.1:
                combined_scrap_2_line_3 = daily_report(line3).combined_side_a_ng[2] + daily_report(line3).combined_side_b_ng[2] + daily_report(line3).combined_side_a_re[2] + daily_report(line3).combined_side_b_re[2]
            elif daily_report(line3).combined_side_a_ng[2] > 0.1 and daily_report(line3).combined_side_b_ng[2] > 0.1:
                combined_scrap_2_line_3 = (daily_report(line3).combined_side_a_ng[2] + daily_report(line3).combined_side_b_ng[2] + daily_report(line3).combined_side_a_re[2] + daily_report(line3).combined_side_b_re[2]) / 2

            if daily_report(line3).combined_side_a_ng[3] < 0.1 or daily_report(line3).combined_side_b_ng[3] < 0.1:
                combined_scrap_3_line_3 = daily_report(line3).combined_side_a_ng[3] + daily_report(line3).combined_side_b_ng[3] + daily_report(line3).combined_side_a_re[3] + daily_report(line3).combined_side_b_re[3]
            elif daily_report(line3).combined_side_a_ng[3] > 0.1 and daily_report(line3).combined_side_b_ng[3] > 0.1:
                combined_scrap_3_line_3 = (daily_report(line3).combined_side_a_ng[3] + daily_report(line3).combined_side_b_ng[3] + daily_report(line3).combined_side_a_re[3] + daily_report(line3).combined_side_b_re[3]) / 2

            if daily_report(line3).combined_side_a_ng[4] < 0.1 or daily_report(line3).combined_side_b_ng[4] < 0.1:
                combined_scrap_4_line_3 = daily_report(line3).combined_side_a_ng[4] + daily_report(line3).combined_side_b_ng[4] + daily_report(line3).combined_side_a_re[4] + daily_report(line3).combined_side_b_re[4]
            elif daily_report(line3).combined_side_a_ng[4] > 0.1 and daily_report(line3).combined_side_b_ng[4] > 0.1:
                combined_scrap_4_line_3 = (daily_report(line3).combined_side_a_ng[4] + daily_report(line3).combined_side_b_ng[4] + daily_report(line3).combined_side_a_re[4] + daily_report(line3).combined_side_b_re[4]) / 2

            if daily_report(line3).combined_side_a_ng[5] < 0.1 or daily_report(line3).combined_side_b_ng[5] < 0.1:
                combined_scrap_5_line_3 = daily_report(line3).combined_side_a_ng[5] + daily_report(line3).combined_side_b_ng[5] + daily_report(line3).combined_side_a_re[5] + daily_report(line3).combined_side_b_re[5]
            elif daily_report(line3).combined_side_a_ng[5] > 0.1 and daily_report(line3).combined_side_b_ng[5] > 0.1:
                combined_scrap_5_line_3 = (daily_report(line3).combined_side_a_ng[5] + daily_report(line3).combined_side_b_ng[5] + daily_report(line3).combined_side_a_re[5] + daily_report(line3).combined_side_b_re[5]) / 2

            if daily_report(line3).combined_side_a_ng[6] < 0.1 or daily_report(line3).combined_side_b_ng[6] < 0.1:
                combined_scrap_6_line_3 = daily_report(line3).combined_side_a_ng[6] + daily_report(line3).combined_side_b_ng[6] + daily_report(line3).combined_side_a_re[6] + daily_report(line3).combined_side_b_re[6]
            elif daily_report(line3).combined_side_a_ng[6] > 0.1 and daily_report(line3).combined_side_b_ng[6] > 0.1:
                combined_scrap_6_line_3 = (daily_report(line3).combined_side_a_ng[6] + daily_report(line3).combined_side_b_ng[6] + daily_report(line3).combined_side_a_re[6] + daily_report(line3).combined_side_b_re[6]) / 2


            # statements for Line 4
            if daily_report(line4).combined_side_a_ng[0] < 0.1 or daily_report(line4).combined_side_b_ng[0] < 0.1:
                combined_scrap_0_line_4 = daily_report(line4).combined_side_a_ng[0] + daily_report(line4).combined_side_b_ng[0] + daily_report(line4).combined_side_a_re[0] + daily_report(line4).combined_side_b_re[0]
            elif daily_report(line4).combined_side_a_ng[0] > 0.1 and daily_report(line4).combined_side_b_ng[0] > 0.1:
                combined_scrap_0_line_4 = (daily_report(line4).combined_side_a_ng[0] + daily_report(line4).combined_side_b_ng[0] + daily_report(line4).combined_side_a_re[0] + daily_report(line4).combined_side_b_re[0]) / 2

            if daily_report(line4).combined_side_a_ng[1] < 0.1 or daily_report(line4).combined_side_b_ng[1] < 0.1:
                combined_scrap_1_line_4 = daily_report(line4).combined_side_a_ng[1] + daily_report(line4).combined_side_b_ng[1] + daily_report(line4).combined_side_a_re[1] + daily_report(line4).combined_side_b_re[1]
            elif daily_report(line4).combined_side_a_ng[1] > 0.1 and daily_report(line4).combined_side_b_ng[1] > 0.1:
                combined_scrap_1_line_4 = (daily_report(line4).combined_side_a_ng[1] + daily_report(line4).combined_side_b_ng[1] + daily_report(line4).combined_side_a_re[1] + daily_report(line4).combined_side_b_re[1]) / 2

            if daily_report(line4).combined_side_a_ng[2] < 0.1 or daily_report(line4).combined_side_b_ng[2] < 0.1:
                combined_scrap_2_line_4 = daily_report(line4).combined_side_a_ng[2] + daily_report(line4).combined_side_b_ng[2] + daily_report(line4).combined_side_a_re[2] + daily_report(line4).combined_side_b_re[2]
            elif daily_report(line4).combined_side_a_ng[2] > 0.1 and daily_report(line4).combined_side_b_ng[2] > 0.1:
                combined_scrap_2_line_4 = (daily_report(line4).combined_side_a_ng[2] + daily_report(line4).combined_side_b_ng[2] + daily_report(line4).combined_side_a_re[2] + daily_report(line4).combined_side_b_re[2]) / 2

            if daily_report(line4).combined_side_a_ng[3] < 0.1 or daily_report(line4).combined_side_b_ng[3] < 0.1:
                combined_scrap_3_line_4 = daily_report(line4).combined_side_a_ng[3] + daily_report(line4).combined_side_b_ng[3] + daily_report(line4).combined_side_a_re[3] + daily_report(line4).combined_side_b_re[3]
            elif daily_report(line4).combined_side_a_ng[3] > 0.1 and daily_report(line4).combined_side_b_ng[3] > 0.1:
                combined_scrap_3_line_4 = (daily_report(line4).combined_side_a_ng[3] + daily_report(line4).combined_side_b_ng[3] + daily_report(line4).combined_side_a_re[3] + daily_report(line4).combined_side_b_re[3]) / 2

            if daily_report(line4).combined_side_a_ng[4] < 0.1 or daily_report(line4).combined_side_b_ng[4] < 0.1:
                combined_scrap_4_line_4 = daily_report(line4).combined_side_a_ng[4] + daily_report(line4).combined_side_b_ng[4] + daily_report(line4).combined_side_a_re[4] + daily_report(line4).combined_side_b_re[4]
            elif daily_report(line4).combined_side_a_ng[4] > 0.1 and daily_report(line4).combined_side_b_ng[4] > 0.1:
                combined_scrap_4_line_4 = (daily_report(line4).combined_side_a_ng[4] + daily_report(line4).combined_side_b_ng[4] + daily_report(line4).combined_side_a_re[4] + daily_report(line4).combined_side_b_re[4]) / 2

            if daily_report(line4).combined_side_a_ng[5] < 0.1 or daily_report(line4).combined_side_b_ng[5] < 0.1:
                combined_scrap_5_line_4 = daily_report(line4).combined_side_a_ng[5] + daily_report(line4).combined_side_b_ng[5] + daily_report(line4).combined_side_a_re[5] + daily_report(line4).combined_side_b_re[5]
            elif daily_report(line4).combined_side_a_ng[5] > 0.1 and daily_report(line4).combined_side_b_ng[5] > 0.1:
                combined_scrap_5_line_4 = (daily_report(line4).combined_side_a_ng[5] + daily_report(line4).combined_side_b_ng[5] + daily_report(line4).combined_side_a_re[5] + daily_report(line4).combined_side_b_re[5]) / 2

            if daily_report(line4).combined_side_a_ng[6] < 0.1 or daily_report(line4).combined_side_b_ng[6] < 0.1:
                combined_scrap_6_line_4 = daily_report(line4).combined_side_a_ng[6] + daily_report(line4).combined_side_b_ng[6] + daily_report(line4).combined_side_a_re[6] + daily_report(line4).combined_side_b_re[6]
            elif daily_report(line4).combined_side_a_ng[6] > 0.1 and daily_report(line4).combined_side_b_ng[6] > 0.1:
                combined_scrap_6_line_4 = (daily_report(line4).combined_side_a_ng[6] + daily_report(line4).combined_side_b_ng[6] + daily_report(line4).combined_side_a_re[6] + daily_report(line4).combined_side_b_re[6]) / 2


            # statements for Line 5
            if daily_report(line5).combined_side_a_ng[0] < 0.1 or daily_report(line5).combined_side_b_ng[0] < 0.1:
                combined_scrap_0_line_5 = daily_report(line5).combined_side_a_ng[0] + daily_report(line5).combined_side_b_ng[0] + daily_report(line5).combined_side_a_re[0] + daily_report(line5).combined_side_b_re[0]
            elif daily_report(line5).combined_side_a_ng[0] > 0.1 and daily_report(line5).combined_side_b_ng[0] > 0.1:
                combined_scrap_0_line_5 = (daily_report(line5).combined_side_a_ng[0] + daily_report(line5).combined_side_b_ng[0] + daily_report(line5).combined_side_a_re[0] + daily_report(line5).combined_side_b_re[0]) / 2

            if daily_report(line5).combined_side_a_ng[1] < 0.1 or daily_report(line5).combined_side_b_ng[1] < 0.1:
                combined_scrap_1_line_5 = daily_report(line5).combined_side_a_ng[1] + daily_report(line5).combined_side_b_ng[1] + daily_report(line5).combined_side_a_re[1] + daily_report(line5).combined_side_b_re[1]
            elif daily_report(line5).combined_side_a_ng[1] > 0.1 and daily_report(line5).combined_side_b_ng[1] > 0.1:
                combined_scrap_1_line_5 = (daily_report(line5).combined_side_a_ng[1] + daily_report(line5).combined_side_b_ng[1] + daily_report(line5).combined_side_a_re[1] + daily_report(line5).combined_side_b_re[1]) / 2

            if daily_report(line5).combined_side_a_ng[2] < 0.1 or daily_report(line5).combined_side_b_ng[2] < 0.1:
                combined_scrap_2_line_5 = daily_report(line5).combined_side_a_ng[2] + daily_report(line5).combined_side_b_ng[2] + daily_report(line5).combined_side_a_re[2] + daily_report(line5).combined_side_b_re[2]
            elif daily_report(line5).combined_side_a_ng[2] > 0.1 and daily_report(line5).combined_side_b_ng[2] > 0.1:
                combined_scrap_2_line_5 = (daily_report(line5).combined_side_a_ng[2] + daily_report(line5).combined_side_b_ng[2] + daily_report(line5).combined_side_a_re[2] + daily_report(line5).combined_side_b_re[2]) / 2

            if daily_report(line5).combined_side_a_ng[3] < 0.1 or daily_report(line5).combined_side_b_ng[3] < 0.1:
                combined_scrap_3_line_5 = daily_report(line5).combined_side_a_ng[3] + daily_report(line5).combined_side_b_ng[3] + daily_report(line5).combined_side_a_re[3] + daily_report(line5).combined_side_b_re[3]
            elif daily_report(line5).combined_side_a_ng[3] > 0.1 and daily_report(line5).combined_side_b_ng[3] > 0.1:
                combined_scrap_3_line_5 = (daily_report(line5).combined_side_a_ng[3] + daily_report(line5).combined_side_b_ng[3] + daily_report(line5).combined_side_a_re[3] + daily_report(line5).combined_side_b_re[3]) / 2

            if daily_report(line5).combined_side_a_ng[4] < 0.1 or daily_report(line5).combined_side_b_ng[4] < 0.1:
                combined_scrap_4_line_5 = daily_report(line5).combined_side_a_ng[4] + daily_report(line5).combined_side_b_ng[4] + daily_report(line5).combined_side_a_re[4] + daily_report(line5).combined_side_b_re[4]
            elif daily_report(line5).combined_side_a_ng[4] > 0.1 and daily_report(line5).combined_side_b_ng[4] > 0.1:
                combined_scrap_4_line_5 = (daily_report(line5).combined_side_a_ng[4] + daily_report(line5).combined_side_b_ng[4] + daily_report(line5).combined_side_a_re[4] + daily_report(line5).combined_side_b_re[4]) / 2

            if daily_report(line5).combined_side_a_ng[5] < 0.1 or daily_report(line5).combined_side_b_ng[5] < 0.1:
                combined_scrap_5_line_5 = daily_report(line5).combined_side_a_ng[5] + daily_report(line5).combined_side_b_ng[5] + daily_report(line5).combined_side_a_re[5] + daily_report(line5).combined_side_b_re[5]
            elif daily_report(line5).combined_side_a_ng[5] > 0.1 and daily_report(line5).combined_side_b_ng[5] > 0.1:
                combined_scrap_5_line_5 = (daily_report(line5).combined_side_a_ng[5] + daily_report(line5).combined_side_b_ng[5] + daily_report(line5).combined_side_a_re[5] + daily_report(line5).combined_side_b_re[5]) / 2

            if daily_report(line5).combined_side_a_ng[6] < 0.1 or daily_report(line5).combined_side_b_ng[6] < 0.1:
                combined_scrap_6_line_5 = daily_report(line5).combined_side_a_ng[6] + daily_report(line5).combined_side_b_ng[6] + daily_report(line5).combined_side_a_re[6] + daily_report(line5).combined_side_b_re[6]
            elif daily_report(line5).combined_side_a_ng[6] > 0.1 and daily_report(line5).combined_side_b_ng[6] > 0.1:
                combined_scrap_6_line_5 = (daily_report(line5).combined_side_a_ng[6] + daily_report(line5).combined_side_b_ng[6] + daily_report(line5).combined_side_a_re[6] + daily_report(line5).combined_side_b_re[6]) / 2



            # statements for Line 7
            if daily_report(line7).combined_side_a_ng[0] < 0.1 or daily_report(line7).combined_side_b_ng[0] < 0.1:
                combined_scrap_0_line_7 = daily_report(line7).combined_side_a_ng[0] + daily_report(line7).combined_side_b_ng[0] + daily_report(line7).combined_side_a_re[0] + daily_report(line7).combined_side_b_re[0]
            elif daily_report(line7).combined_side_a_ng[0] > 0.1 and daily_report(line7).combined_side_b_ng[0] > 0.1:
                combined_scrap_0_line_7 = (daily_report(line7).combined_side_a_ng[0] + daily_report(line7).combined_side_b_ng[0] + daily_report(line7).combined_side_a_re[0] + daily_report(line7).combined_side_b_re[0]) / 2

            if daily_report(line7).combined_side_a_ng[1] < 0.1 or daily_report(line7).combined_side_b_ng[1] < 0.1:
                combined_scrap_1_line_7 = daily_report(line7).combined_side_a_ng[1] + daily_report(line7).combined_side_b_ng[1] + daily_report(line7).combined_side_a_re[1] + daily_report(line7).combined_side_b_re[1]
            elif daily_report(line7).combined_side_a_ng[1] > 0.1 and daily_report(line7).combined_side_b_ng[1] > 0.1:
                combined_scrap_1_line_7 = (daily_report(line7).combined_side_a_ng[1] + daily_report(line7).combined_side_b_ng[1] + daily_report(line7).combined_side_a_re[1] + daily_report(line7).combined_side_b_re[1]) / 2

            if daily_report(line7).combined_side_a_ng[2] < 0.1 or daily_report(line7).combined_side_b_ng[2] < 0.1:
                combined_scrap_2_line_7 = daily_report(line7).combined_side_a_ng[2] + daily_report(line7).combined_side_b_ng[2] + daily_report(line7).combined_side_a_re[2] + daily_report(line7).combined_side_b_re[2]
            elif daily_report(line7).combined_side_a_ng[2] > 0.1 and daily_report(line7).combined_side_b_ng[2] > 0.1:
                combined_scrap_2_line_7 = (daily_report(line7).combined_side_a_ng[2] + daily_report(line7).combined_side_b_ng[2] + daily_report(line7).combined_side_a_re[2] + daily_report(line7).combined_side_b_re[2]) / 2

            if daily_report(line7).combined_side_a_ng[3] < 0.1 or daily_report(line7).combined_side_b_ng[3] < 0.1:
                combined_scrap_3_line_7 = daily_report(line7).combined_side_a_ng[3] + daily_report(line7).combined_side_b_ng[3] + daily_report(line7).combined_side_a_re[3] + daily_report(line7).combined_side_b_re[3]
            elif daily_report(line7).combined_side_a_ng[3] > 0.1 and daily_report(line7).combined_side_b_ng[3] > 0.1:
                combined_scrap_3_line_7 = (daily_report(line7).combined_side_a_ng[3] + daily_report(line7).combined_side_b_ng[3] + daily_report(line7).combined_side_a_re[3] + daily_report(line7).combined_side_b_re[3]) / 2

            if daily_report(line7).combined_side_a_ng[4] < 0.1 or daily_report(line7).combined_side_b_ng[4] < 0.1:
                combined_scrap_4_line_7 = daily_report(line7).combined_side_a_ng[4] + daily_report(line7).combined_side_b_ng[4] + daily_report(line7).combined_side_a_re[4] + daily_report(line7).combined_side_b_re[4]
            elif daily_report(line7).combined_side_a_ng[4] > 0.1 and daily_report(line7).combined_side_b_ng[4] > 0.1:
                combined_scrap_4_line_7 = (daily_report(line7).combined_side_a_ng[4] + daily_report(line7).combined_side_b_ng[4] + daily_report(line7).combined_side_a_re[4] + daily_report(line7).combined_side_b_re[4]) / 2

            if daily_report(line7).combined_side_a_ng[5] < 0.1 or daily_report(line7).combined_side_b_ng[5] < 0.1:
                combined_scrap_5_line_7 = daily_report(line7).combined_side_a_ng[5] + daily_report(line7).combined_side_b_ng[5] + daily_report(line7).combined_side_a_re[5] + daily_report(line7).combined_side_b_re[5]
            elif daily_report(line7).combined_side_a_ng[5] > 0.1 and daily_report(line7).combined_side_b_ng[5] > 0.1:
                combined_scrap_5_line_7 = (daily_report(line7).combined_side_a_ng[5] + daily_report(line7).combined_side_b_ng[5] + daily_report(line7).combined_side_a_re[5] + daily_report(line7).combined_side_b_re[5]) / 2

            if daily_report(line7).combined_side_a_ng[6] < 0.1 or daily_report(line7).combined_side_b_ng[6] < 0.1:
                combined_scrap_6_line_7 = daily_report(line7).combined_side_a_ng[6] + daily_report(line7).combined_side_b_ng[6] + daily_report(line7).combined_side_a_re[6] + daily_report(line7).combined_side_b_re[6]
            elif daily_report(line7).combined_side_a_ng[6] > 0.1 and daily_report(line7).combined_side_b_ng[6] > 0.1:
                combined_scrap_6_line_7 = (daily_report(line7).combined_side_a_ng[6] + daily_report(line7).combined_side_b_ng[6] + daily_report(line7).combined_side_a_re[6] + daily_report(line7).combined_side_b_re[6]) / 2


            # statements for Line 8
            if daily_report(line8).combined_side_a_ng[0] < 0.1 or daily_report(line8).combined_side_b_ng[0] < 0.1:
                combined_scrap_0_line_8 = daily_report(line8).combined_side_a_ng[0] + daily_report(line8).combined_side_b_ng[0] + daily_report(line8).combined_side_a_re[0] + daily_report(line8).combined_side_b_re[0]
            elif daily_report(line8).combined_side_a_ng[0] > 0.1 and daily_report(line8).combined_side_b_ng[0] > 0.1:
                combined_scrap_0_line_8 = (daily_report(line8).combined_side_a_ng[0] + daily_report(line8).combined_side_b_ng[0] + daily_report(line8).combined_side_a_re[0] + daily_report(line8).combined_side_b_re[0]) / 2

            if daily_report(line8).combined_side_a_ng[1] < 0.1 or daily_report(line8).combined_side_b_ng[1] < 0.1:
                combined_scrap_1_line_8 = daily_report(line8).combined_side_a_ng[1] + daily_report(line8).combined_side_b_ng[1] + daily_report(line8).combined_side_a_re[1] + daily_report(line8).combined_side_b_re[1]
            elif daily_report(line8).combined_side_a_ng[1] > 0.1 and daily_report(line8).combined_side_b_ng[1] > 0.1:
                combined_scrap_1_line_8 = (daily_report(line8).combined_side_a_ng[1] + daily_report(line8).combined_side_b_ng[1] + daily_report(line8).combined_side_a_re[1] + daily_report(line8).combined_side_b_re[1]) / 2

            if daily_report(line8).combined_side_a_ng[2] < 0.1 or daily_report(line8).combined_side_b_ng[2] < 0.1:
                combined_scrap_2_line_8 = daily_report(line8).combined_side_a_ng[2] + daily_report(line8).combined_side_b_ng[2] + daily_report(line8).combined_side_a_re[2] + daily_report(line8).combined_side_b_re[2]
            elif daily_report(line8).combined_side_a_ng[2] > 0.1 and daily_report(line8).combined_side_b_ng[2] > 0.1:
                combined_scrap_2_line_8 = (daily_report(line8).combined_side_a_ng[2] + daily_report(line8).combined_side_b_ng[2] + daily_report(line8).combined_side_a_re[2] + daily_report(line8).combined_side_b_re[2]) / 2

            if daily_report(line8).combined_side_a_ng[3] < 0.1 or daily_report(line8).combined_side_b_ng[3] < 0.1:
                combined_scrap_3_line_8 = daily_report(line8).combined_side_a_ng[3] + daily_report(line8).combined_side_b_ng[3] + daily_report(line8).combined_side_a_re[3] + daily_report(line8).combined_side_b_re[3]
            elif daily_report(line8).combined_side_a_ng[3] > 0.1 and daily_report(line8).combined_side_b_ng[3] > 0.1:
                combined_scrap_3_line_8 = (daily_report(line8).combined_side_a_ng[3] + daily_report(line8).combined_side_b_ng[3] + daily_report(line8).combined_side_a_re[3] + daily_report(line8).combined_side_b_re[3]) / 2

            if daily_report(line8).combined_side_a_ng[4] < 0.1 or daily_report(line8).combined_side_b_ng[4] < 0.1:
                combined_scrap_4_line_8 = daily_report(line8).combined_side_a_ng[4] + daily_report(line8).combined_side_b_ng[4] + daily_report(line8).combined_side_a_re[4] + daily_report(line8).combined_side_b_re[4]
            elif daily_report(line8).combined_side_a_ng[4] > 0.1 and daily_report(line8).combined_side_b_ng[4] > 0.1:
                combined_scrap_4_line_8 = (daily_report(line8).combined_side_a_ng[4] + daily_report(line8).combined_side_b_ng[4] + daily_report(line8).combined_side_a_re[4] + daily_report(line8).combined_side_b_re[4]) / 2

            if daily_report(line8).combined_side_a_ng[5] < 0.1 or daily_report(line8).combined_side_b_ng[5] < 0.1:
                combined_scrap_5_line_8 = daily_report(line8).combined_side_a_ng[5] + daily_report(line8).combined_side_b_ng[5] + daily_report(line8).combined_side_a_re[5] + daily_report(line8).combined_side_b_re[5]
            elif daily_report(line8).combined_side_a_ng[5] > 0.1 and daily_report(line8).combined_side_b_ng[5] > 0.1:
                combined_scrap_5_line_8 = (daily_report(line8).combined_side_a_ng[5] + daily_report(line8).combined_side_b_ng[5] + daily_report(line8).combined_side_a_re[5] + daily_report(line8).combined_side_b_re[5]) / 2

            if daily_report(line8).combined_side_a_ng[6] < 0.1 or daily_report(line8).combined_side_b_ng[6] < 0.1:
                combined_scrap_6_line_8 = daily_report(line8).combined_side_a_ng[6] + daily_report(line8).combined_side_b_ng[6] + daily_report(line8).combined_side_a_re[6] + daily_report(line8).combined_side_b_re[6]
            elif daily_report(line8).combined_side_a_ng[6] > 0.1 and daily_report(line8).combined_side_b_ng[6] > 0.1:
                combined_scrap_6_line_8 = (daily_report(line8).combined_side_a_ng[6] + daily_report(line8).combined_side_b_ng[6] + daily_report(line8).combined_side_a_re[6] + daily_report(line8).combined_side_b_re[6]) / 2



            # statements for Line 9
            if daily_report(line9).combined_side_a_ng[0] < 0.1 or daily_report(line9).combined_side_b_ng[0] < 0.1:
                combined_scrap_0_line_9 = daily_report(line9).combined_side_a_ng[0] + daily_report(line9).combined_side_b_ng[0] + daily_report(line9).combined_side_a_re[0] + daily_report(line9).combined_side_b_re[0]
            elif daily_report(line9).combined_side_a_ng[0] > 0.1 and daily_report(line9).combined_side_b_ng[0] > 0.1:
                combined_scrap_0_line_9 = (daily_report(line9).combined_side_a_ng[0] + daily_report(line9).combined_side_b_ng[0] + daily_report(line9).combined_side_a_re[0] + daily_report(line9).combined_side_b_re[0]) / 2

            if daily_report(line9).combined_side_a_ng[1] < 0.1 or daily_report(line9).combined_side_b_ng[1] < 0.1:
                combined_scrap_1_line_9 = daily_report(line9).combined_side_a_ng[1] + daily_report(line9).combined_side_b_ng[1] + daily_report(line9).combined_side_a_re[1] + daily_report(line9).combined_side_b_re[1]
            elif daily_report(line9).combined_side_a_ng[1] > 0.1 and daily_report(line9).combined_side_b_ng[1] > 0.1:
                combined_scrap_1_line_9 = (daily_report(line9).combined_side_a_ng[1] + daily_report(line9).combined_side_b_ng[1] + daily_report(line9).combined_side_a_re[1] + daily_report(line9).combined_side_b_re[1]) / 2

            if daily_report(line9).combined_side_a_ng[2] < 0.1 or daily_report(line9).combined_side_b_ng[2] < 0.1:
                combined_scrap_2_line_9 = daily_report(line9).combined_side_a_ng[2] + daily_report(line9).combined_side_b_ng[2] + daily_report(line9).combined_side_a_re[2] + daily_report(line9).combined_side_b_re[2]
            elif daily_report(line9).combined_side_a_ng[2] > 0.1 and daily_report(line9).combined_side_b_ng[2] > 0.1:
                combined_scrap_2_line_9 = (daily_report(line9).combined_side_a_ng[2] + daily_report(line9).combined_side_b_ng[2] + daily_report(line9).combined_side_a_re[2] + daily_report(line9).combined_side_b_re[2]) / 2

            if daily_report(line9).combined_side_a_ng[3] < 0.1 or daily_report(line9).combined_side_b_ng[3] < 0.1:
                combined_scrap_3_line_9 = daily_report(line9).combined_side_a_ng[3] + daily_report(line9).combined_side_b_ng[3] + daily_report(line9).combined_side_a_re[3] + daily_report(line9).combined_side_b_re[3]
            elif daily_report(line9).combined_side_a_ng[3] > 0.1 and daily_report(line9).combined_side_b_ng[3] > 0.1:
                combined_scrap_3_line_9 = (daily_report(line9).combined_side_a_ng[3] + daily_report(line9).combined_side_b_ng[3] + daily_report(line9).combined_side_a_re[3] + daily_report(line9).combined_side_b_re[3]) / 2

            if daily_report(line9).combined_side_a_ng[4] < 0.1 or daily_report(line9).combined_side_b_ng[4] < 0.1:
                combined_scrap_4_line_9 = daily_report(line9).combined_side_a_ng[4] + daily_report(line9).combined_side_b_ng[4] + daily_report(line9).combined_side_a_re[4] + daily_report(line9).combined_side_b_re[4]
            elif daily_report(line9).combined_side_a_ng[4] > 0.1 and daily_report(line9).combined_side_b_ng[4] > 0.1:
                combined_scrap_4_line_9 = (daily_report(line9).combined_side_a_ng[4] + daily_report(line9).combined_side_b_ng[4] + daily_report(line9).combined_side_a_re[4] + daily_report(line9).combined_side_b_re[4]) / 2

            if daily_report(line9).combined_side_a_ng[5] < 0.1 or daily_report(line9).combined_side_b_ng[5] < 0.1:
                combined_scrap_5_line_9 = daily_report(line9).combined_side_a_ng[5] + daily_report(line9).combined_side_b_ng[5] + daily_report(line9).combined_side_a_re[5] + daily_report(line9).combined_side_b_re[5]
            elif daily_report(line9).combined_side_a_ng[5] > 0.1 and daily_report(line9).combined_side_b_ng[5] > 0.1:
                combined_scrap_5_line_9 = (daily_report(line9).combined_side_a_ng[5] + daily_report(line9).combined_side_b_ng[5] + daily_report(line9).combined_side_a_re[5] + daily_report(line9).combined_side_b_re[5]) / 2

            if daily_report(line9).combined_side_a_ng[6] < 0.1 or daily_report(line9).combined_side_b_ng[6] < 0.1:
                combined_scrap_6_line_9 = daily_report(line9).combined_side_a_ng[6] + daily_report(line9).combined_side_b_ng[6] + daily_report(line9).combined_side_a_re[6] + daily_report(line9).combined_side_b_re[6]
            elif daily_report(line9).combined_side_a_ng[6] > 0.1 and daily_report(line9).combined_side_b_ng[6] > 0.1:
                combined_scrap_6_line_9 = (daily_report(line9).combined_side_a_ng[6] + daily_report(line9).combined_side_b_ng[6] + daily_report(line9).combined_side_a_re[6] + daily_report(line9).combined_side_b_re[6]) / 2



            # statements for Line 10
            if daily_report(line10).combined_side_a_ng[0] < 0.1 or daily_report(line10).combined_side_b_ng[0] < 0.1:
                combined_scrap_0_line_10 = daily_report(line10).combined_side_a_ng[0] + daily_report(line10).combined_side_b_ng[0] + daily_report(line10).combined_side_a_re[0] + daily_report(line10).combined_side_b_re[0]
            elif daily_report(line10).combined_side_a_ng[0] > 0.1 and daily_report(line10).combined_side_b_ng[0] > 0.1:
                combined_scrap_0_line_10 = (daily_report(line10).combined_side_a_ng[0] + daily_report(line10).combined_side_b_ng[0] + daily_report(line10).combined_side_a_re[0] + daily_report(line10).combined_side_b_re[0]) / 2

            if daily_report(line10).combined_side_a_ng[1] < 0.1 or daily_report(line10).combined_side_b_ng[1] < 0.1:
                combined_scrap_1_line_10 = daily_report(line10).combined_side_a_ng[1] + daily_report(line10).combined_side_b_ng[1] + daily_report(line10).combined_side_a_re[1] + daily_report(line10).combined_side_b_re[1]
            elif daily_report(line10).combined_side_a_ng[1] > 0.1 and daily_report(line10).combined_side_b_ng[1] > 0.1:
                combined_scrap_1_line_10 = (daily_report(line10).combined_side_a_ng[1] + daily_report(line10).combined_side_b_ng[1] + daily_report(line10).combined_side_a_re[1] + daily_report(line10).combined_side_b_re[1]) / 2

            if daily_report(line10).combined_side_a_ng[2] < 0.1 or daily_report(line10).combined_side_b_ng[2] < 0.1:
                combined_scrap_2_line_10 = daily_report(line10).combined_side_a_ng[2] + daily_report(line10).combined_side_b_ng[2] + daily_report(line10).combined_side_a_re[2] + daily_report(line10).combined_side_b_re[2]
            elif daily_report(line10).combined_side_a_ng[2] > 0.1 and daily_report(line10).combined_side_b_ng[2] > 0.1:
                combined_scrap_2_line_10 = (daily_report(line10).combined_side_a_ng[2] + daily_report(line10).combined_side_b_ng[2] + daily_report(line10).combined_side_a_re[2] + daily_report(line10).combined_side_b_re[2]) / 2

            if daily_report(line10).combined_side_a_ng[3] < 0.1 or daily_report(line10).combined_side_b_ng[3] < 0.1:
                combined_scrap_3_line_10 = daily_report(line10).combined_side_a_ng[3] + daily_report(line10).combined_side_b_ng[3] + daily_report(line10).combined_side_a_re[3] + daily_report(line10).combined_side_b_re[3]
            elif daily_report(line10).combined_side_a_ng[3] > 0.1 and daily_report(line10).combined_side_b_ng[3] > 0.1:
                combined_scrap_3_line_10 = (daily_report(line10).combined_side_a_ng[3] + daily_report(line10).combined_side_b_ng[3] + daily_report(line10).combined_side_a_re[3] + daily_report(line10).combined_side_b_re[3]) / 2

            if daily_report(line10).combined_side_a_ng[4] < 0.1 or daily_report(line10).combined_side_b_ng[4] < 0.1:
                combined_scrap_4_line_10 = daily_report(line10).combined_side_a_ng[4] + daily_report(line10).combined_side_b_ng[4] + daily_report(line10).combined_side_a_re[4] + daily_report(line10).combined_side_b_re[4]
            elif daily_report(line10).combined_side_a_ng[4] > 0.1 and daily_report(line10).combined_side_b_ng[4] > 0.1:
                combined_scrap_4_line_10 = (daily_report(line10).combined_side_a_ng[4] + daily_report(line10).combined_side_b_ng[4] + daily_report(line10).combined_side_a_re[4] + daily_report(line10).combined_side_b_re[4]) / 2

            if daily_report(line10).combined_side_a_ng[5] < 0.1 or daily_report(line10).combined_side_b_ng[5] < 0.1:
                combined_scrap_5_line_10 = daily_report(line10).combined_side_a_ng[5] + daily_report(line10).combined_side_b_ng[5] + daily_report(line10).combined_side_a_re[5] + daily_report(line10).combined_side_b_re[5]
            elif daily_report(line10).combined_side_a_ng[5] > 0.1 and daily_report(line10).combined_side_b_ng[5] > 0.1:
                combined_scrap_5_line_10 = (daily_report(line10).combined_side_a_ng[5] + daily_report(line10).combined_side_b_ng[5] + daily_report(line10).combined_side_a_re[5] + daily_report(line10).combined_side_b_re[5]) / 2

            if daily_report(line10).combined_side_a_ng[6] < 0.1 or daily_report(line10).combined_side_b_ng[6] < 0.1:
                combined_scrap_6_line_10 = daily_report(line10).combined_side_a_ng[6] + daily_report(line10).combined_side_b_ng[6] + daily_report(line10).combined_side_a_re[6] + daily_report(line10).combined_side_b_re[6]
            elif daily_report(line10).combined_side_a_ng[6] > 0.1 and daily_report(line10).combined_side_b_ng[6] > 0.1:
                combined_scrap_6_line_10 = (daily_report(line10).combined_side_a_ng[6] + daily_report(line10).combined_side_b_ng[6] + daily_report(line10).combined_side_a_re[6] + daily_report(line10).combined_side_b_re[6]) / 2

            return {
            "line_3": 3,
            "line_4": 4,
            "line_5": 5,
            "line_7": 7,
            "line_8": 8,
            "line_9": 9,
            "line_10": 1,
            "day0": day0,
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
                    }


        lines = render_per_line(3, 4, 5, 7, 8, 9, 10)

        return render(request, "dolcegusto/scrap_rate.html", lines)

class Charts_per_Line(View):
    model = daily_report

    def get(self, request):

        return render(request, "dolcegusto/Charts_per_Line.html", {"chart":"chart"})
