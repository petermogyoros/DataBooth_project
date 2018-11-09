from django.shortcuts import render
from django.views import View
import pandas as pd
from pandas import DataFrame
from datetime import datetime

from dolcegusto.models import daily_report_for_8

class Line(View):
    model = daily_report_for_8

    def get(self, request):

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

        # This gives a function with the result of the weekday name from where the date originated from
        day0 = get_weekday(datetime.strptime(str(daily_report_for_8(8).production_day[0])[0:10], '%Y-%m-%d').date().weekday)
        day1 = get_weekday(datetime.strptime(str(daily_report_for_8(8).production_day[1])[0:10], '%Y-%m-%d').date().weekday)
        day2 = get_weekday(datetime.strptime(str(daily_report_for_8(8).production_day[2])[0:10], '%Y-%m-%d').date().weekday)
        day3 = get_weekday(datetime.strptime(str(daily_report_for_8(8).production_day[3])[0:10], '%Y-%m-%d').date().weekday)
        day4 = get_weekday(datetime.strptime(str(daily_report_for_8(8).production_day[4])[0:10], '%Y-%m-%d').date().weekday)
        day5 = get_weekday(datetime.strptime(str(daily_report_for_8(8).production_day[5])[0:10], '%Y-%m-%d').date().weekday)
        day6 = get_weekday(datetime.strptime(str(daily_report_for_8(8).production_day[6])[0:10], '%Y-%m-%d').date().weekday)


        return render(request, "dolcegusto/line.html", {
        "day0": day0,
        "combined_side_a_ng0": daily_report_for_8(8).combined_side_a_ng[0],
        "combined_side_b_ng0": daily_report_for_8(8).combined_side_b_ng[0],
        "combined_side_a_re0": daily_report_for_8(8).combined_side_a_re[0],
        "combined_side_b_re0": daily_report_for_8(8).combined_side_b_re[0],
        "day1": day1,
        "combined_side_a_ng1": daily_report_for_8(8).combined_side_a_ng[1],
        "combined_side_b_ng1": daily_report_for_8(8).combined_side_b_ng[1],
        "combined_side_a_re1": daily_report_for_8(8).combined_side_a_re[1],
        "combined_side_b_re1": daily_report_for_8(8).combined_side_b_re[1],
        "day2": day2,
        "combined_side_a_ng2": daily_report_for_8(8).combined_side_a_ng[2],
        "combined_side_b_ng2": daily_report_for_8(8).combined_side_b_ng[2],
        "combined_side_a_re2": daily_report_for_8(8).combined_side_a_re[2],
        "combined_side_b_re2": daily_report_for_8(8).combined_side_b_re[2],
        "day3": day3,
        "combined_side_a_ng3": daily_report_for_8(8).combined_side_a_ng[3],
        "combined_side_b_ng3": daily_report_for_8(8).combined_side_b_ng[3],
        "combined_side_a_re3": daily_report_for_8(8).combined_side_a_re[3],
        "combined_side_b_re3": daily_report_for_8(8).combined_side_b_re[3],
        "day4": day4,
        "combined_side_a_ng4": daily_report_for_8(8).combined_side_a_ng[4],
        "combined_side_b_ng4": daily_report_for_8(8).combined_side_b_ng[4],
        "combined_side_a_re4": daily_report_for_8(8).combined_side_a_re[4],
        "combined_side_b_re4": daily_report_for_8(8).combined_side_b_re[4],
        "day5": day5,
        "combined_side_a_ng5": daily_report_for_8(8).combined_side_a_ng[5],
        "combined_side_b_ng5": daily_report_for_8(8).combined_side_b_ng[5],
        "combined_side_a_re5": daily_report_for_8(8).combined_side_a_re[5],
        "combined_side_b_re5": daily_report_for_8(8).combined_side_b_re[5],
        "day6": day6,
        "combined_side_a_ng6": daily_report_for_8(8).combined_side_a_ng[6],
        "combined_side_b_ng6": daily_report_for_8(8).combined_side_b_ng[6],
        "combined_side_a_re6": daily_report_for_8(8).combined_side_a_re[6],
        "combined_side_b_re6": daily_report_for_8(8).combined_side_b_re[6]
        })

        # TEMPORARY! get the percantage value from db
        # try:
        #     day_1_side_a_ng = int(daily_report_for_8(self))
        #     day_1_side_b_ng = int(daily_report_for_8(self))
        #     day_1_side_a_re = int(daily_report_for_8(self))
        #     day_1_side_b_re = int(daily_report_for_8(self))
        #
        # except:
        #     day_1_side_a_ng = 0
        #     day_1_side_b_ng = 0
        #     day_1_side_a_re = 0
        #     day_1_side_b_re = 0
        #
        #
        # try:
        #     day_2_side_a_ng = (int(past_week_scrap(self)[4]) / 15000) *100
        #     day_2_side_b_ng = (int(past_week_scrap(self)[5]) / 15000) *100
        #     day_2_side_a_re = (int(past_week_scrap(self)[6])  / 15000) *100
        #     day_2_side_b_re = (int(past_week_scrap(self)[7]) / 15000) *100
        #
        # except:
        #     day_2_side_a_ng = 0
        #     day_2_side_b_ng = 0
        #     day_2_side_a_re = 0
        #     day_2_side_b_re = 0
        #
        #
        # try:
        #     day_3_side_a_ng = (int(past_week_scrap(self)[8]) / 15000) *100
        #     day_3_side_b_ng = (int(past_week_scrap(self)[9]) / 15000) *100
        #     day_3_side_a_re = (int(past_week_scrap(self)[10]) / 15000) *100
        #     day_3_side_b_re = (int(past_week_scrap(self)[11]) / 15000) *100
        #
        # except:
        #     day_3_side_a_ng = 0
        #     day_3_side_b_ng = 0
        #     day_3_side_a_re = 0
        #     day_3_side_b_re = 0
        #
        #
        # try:
        #     day_4_side_a_ng = (int(past_week_scrap(self)[12]) / 15000) *100
        #     day_4_side_b_ng = (int(past_week_scrap(self)[13]) / 15000) *100
        #     day_4_side_a_re = (int(past_week_scrap(self)[14]) / 15000) *100
        #     day_4_side_b_re = (int(past_week_scrap(self)[15]) / 15000) *100
        #
        # except:
        #     day_4_side_a_ng = 0
        #     day_4_side_b_ng = 0
        #     day_4_side_a_re = 0
        #     day_4_side_b_re = 0
        #
        #
        # try:
        #     day_5_side_a_ng = (int(past_week_scrap(self)[16]) / 15000) *100
        #     day_5_side_b_ng = (int(past_week_scrap(self)[17]) / 15000) *100
        #     day_5_side_a_re = (int(past_week_scrap(self)[18]) / 15000) *100
        #     day_5_side_b_re = (int(past_week_scrap(self)[19]) / 15000) *100
        #
        # except:
        #     day_5_side_a_ng = 0
        #     day_5_side_b_ng = 0
        #     day_5_side_a_re = 0
        #     day_5_side_b_re = 0
        #
        #
        # try:
        #     day_6_side_a_ng = (int(past_week_scrap(self)[20]) / 15000) *100
        #     day_6_side_b_ng = (int(past_week_scrap(self)[21]) / 15000) *100
        #     day_6_side_a_re = (int(past_week_scrap(self)[22]) / 15000) *100
        #     day_6_side_b_re = (int(past_week_scrap(self)[23]) / 15000) *100
        #
        # except:
        #     day_6_side_a_ng = 0
        #     day_6_side_b_ng = 0
        #     day_6_side_a_re = 0
        #     day_6_side_b_re = 0
        #
        #
        # try:
        #     day_7_side_a_ng = (int(past_week_scrap(self)[24]) / 15000) *100
        #     day_7_side_b_ng = (int(past_week_scrap(self)[25]) / 15000) *100
        #     day_7_side_a_re = (int(past_week_scrap(self)[26]) / 15000) *100
        #     day_7_side_b_re = (int(past_week_scrap(self)[27]) / 15000) *100
        #
        # except:
        #     day_7_side_a_ng = 0
        #     day_7_side_b_ng = 0
        #     day_7_side_a_re = 0
        #     day_7_side_b_re = 0
        #
        #
        # return render(request, "dolcegusto/line.html", {
        # "day_1_side_a_ng": day_1_side_a_ng, "day_1_side_b_ng": day_1_side_b_ng,
        # "day_1_side_a_re": day_1_side_a_re, "day_1_side_b_re": day_1_side_b_re,
        # "day_2_side_a_ng": day_2_side_a_ng, "day_2_side_b_ng": day_2_side_b_ng,
        # "day_2_side_a_re": day_2_side_a_re, "day_2_side_b_re": day_2_side_b_re,
        # "day_3_side_a_ng": day_3_side_a_ng, "day_3_side_b_ng": day_3_side_b_ng,
        # "day_3_side_a_re": day_3_side_a_re, "day_3_side_b_re": day_3_side_b_re,
        # "day_4_side_a_ng": day_4_side_a_ng, "day_4_side_b_ng": day_4_side_b_ng,
        # "day_4_side_a_re": day_4_side_a_re, "day_4_side_b_re": day_4_side_b_re,
        # "day_5_side_a_ng": day_5_side_a_ng, "day_5_side_b_ng": day_5_side_b_ng,
        # "day_5_side_a_re": day_5_side_a_re, "day_5_side_b_re": day_5_side_b_re,
        # "day_6_side_a_ng": day_6_side_a_ng, "day_6_side_b_ng": day_6_side_b_ng,
        # "day_6_side_a_re": day_6_side_a_re, "day_6_side_b_re": day_6_side_b_re,
        # "day_7_side_a_ng": day_7_side_a_ng, "day_7_side_b_ng": day_7_side_b_ng,
        # "day_7_side_a_re": day_7_side_a_re, "day_7_side_b_re": day_7_side_b_re,
        # })

# Create your views here.
# class Line8(View):
#     model = DolceGusto_table
#
#     def get(self, request):
#         value_dict = {}
#
#         # loop counters
#         counter_raw_time = 0
#         counter_a_ok = 0
#         counter_b_ok = 0
#         counter_line = 0
#
#         raw_time_sum = 0
#         a_ok_sum = 0
#         b_ok_sum = 0
#         line_sum = 0
#
#         for q in qs:
#             q = str(q)
#             q_individual_values = q.split()
#             object_counter = 0
#             for k in q_individual_values:
#                 object_counter += 1
#                 if object_counter == 1:
#                     value_dict.setdefault("raw_time", [])
#                     value_dict["raw_time"].append(int(k))
#                 elif object_counter == 2:
#                     value_dict.setdefault("line", [])
#                     value_dict["line"].append(int(k))
#                 elif object_counter == 3:
#                     value_dict.setdefault("batch", [])
#                     value_dict["batch"].append(int(k))
#                 elif object_counter == 4:
#                     value_dict.setdefault("a_ok", [])
#                     value_dict["a_ok"].append(int(k))
#                 elif object_counter == 5:
#                     value_dict.setdefault("b_ok", [])
#                     value_dict["b_ok"].append(int(k))
#                 elif object_counter == 6:
#                     value_dict.setdefault("combined_side_a_ng", [])
#                     value_dict["combined_side_a_ng"].append(int(k))
#                 elif object_counter == 7:
#                     value_dict.setdefault("combined_side_b_ng", [])
#                     value_dict["combined_side_b_ng"].append(int(k))
#         print(value_dict)
#         # this is probably going to be a function
#         for raw_time in value_dict["raw_time"]:
#             counter_raw_time += 1
#             raw_time_sum = raw_time_sum + raw_time
#         for a_ok in value_dict["a_ok"]:
#             counter_a_ok += 1
#             a_ok_sum = a_ok_sum + a_ok
#         for b_ok in value_dict["b_ok"]:
#             counter_b_ok += 1
#             b_ok_sum = b_ok_sum + b_ok
#         for line in value_dict["line"]:
#             counter_line += 1
#             line_sum = line_sum + line
#
#         a_ok_avarage = a_ok_sum/counter_a_ok
#         b_ok_avarage = b_ok_sum/counter_b_ok
#         raw_time_avarage = raw_time_sum/counter_raw_time
#         line_avarage = line_sum/counter_line
#
#         return render(request, "dolcegusto/line.html",
#         {"raw_time": int(raw_time_avarage), "line": int(line_avarage),
#         "a_ok": int(a_ok_avarage), "b_ok": int(b_ok_avarage)})
