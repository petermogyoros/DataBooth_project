from django.shortcuts import render
from django.views import View
import pandas as pd
from pandas import DataFrame

from dolcegusto.models import daily_report_for_8

class Line(View):
    model = daily_report_for_8

    def get(self, request):

        # TEMPORARY! get the percantage value from db
        try:
<<<<<<< HEAD
            day_1_side_a_ng = (int(past_week_scrap(self)[0]) / 15000) *100
            day_1_side_b_ng = (int(past_week_scrap(self)[1]) / 15000) *100
            day_1_side_a_re = (int(past_week_scrap(self)[2]) / 15000) *100
            day_1_side_b_re = (int(past_week_scrap(self)[3]) / 15000) *100
=======
            day_1_side_a_ng = int(daily_report_for_8(self))
            day_1_side_b_ng = int(daily_report_for_8(self))
            day_1_side_a_re = int(daily_report_for_8(self))
            day_1_side_b_re = int(daily_report_for_8(self))
>>>>>>> 9091b43e685fbab4e231f90f02af8b9f47c96670

        except:
            day_1_side_a_ng = 0
            day_1_side_b_ng = 0
            day_1_side_a_re = 0
            day_1_side_b_re = 0


        try:
            day_2_side_a_ng = (int(past_week_scrap(self)[4]) / 15000) *100
            day_2_side_b_ng = (int(past_week_scrap(self)[5]) / 15000) *100
            day_2_side_a_re = (int(past_week_scrap(self)[6])  / 15000) *100
            day_2_side_b_re = (int(past_week_scrap(self)[7]) / 15000) *100

        except:
            day_2_side_a_ng = 0
            day_2_side_b_ng = 0
            day_2_side_a_re = 0
            day_2_side_b_re = 0


        try:
            day_3_side_a_ng = (int(past_week_scrap(self)[8]) / 15000) *100
            day_3_side_b_ng = (int(past_week_scrap(self)[9]) / 15000) *100
            day_3_side_a_re = (int(past_week_scrap(self)[10]) / 15000) *100
            day_3_side_b_re = (int(past_week_scrap(self)[11]) / 15000) *100

        except:
            day_3_side_a_ng = 0
            day_3_side_b_ng = 0
            day_3_side_a_re = 0
            day_3_side_b_re = 0


        try:
            day_4_side_a_ng = (int(past_week_scrap(self)[12]) / 15000) *100
            day_4_side_b_ng = (int(past_week_scrap(self)[13]) / 15000) *100
            day_4_side_a_re = (int(past_week_scrap(self)[14]) / 15000) *100
            day_4_side_b_re = (int(past_week_scrap(self)[15]) / 15000) *100

        except:
            day_4_side_a_ng = 0
            day_4_side_b_ng = 0
            day_4_side_a_re = 0
            day_4_side_b_re = 0


        try:
            day_5_side_a_ng = (int(past_week_scrap(self)[16]) / 15000) *100
            day_5_side_b_ng = (int(past_week_scrap(self)[17]) / 15000) *100
            day_5_side_a_re = (int(past_week_scrap(self)[18]) / 15000) *100
            day_5_side_b_re = (int(past_week_scrap(self)[19]) / 15000) *100

        except:
            day_5_side_a_ng = 0
            day_5_side_b_ng = 0
            day_5_side_a_re = 0
            day_5_side_b_re = 0


        try:
            day_6_side_a_ng = (int(past_week_scrap(self)[20]) / 15000) *100
            day_6_side_b_ng = (int(past_week_scrap(self)[21]) / 15000) *100
            day_6_side_a_re = (int(past_week_scrap(self)[22]) / 15000) *100
            day_6_side_b_re = (int(past_week_scrap(self)[23]) / 15000) *100

        except:
            day_6_side_a_ng = 0
            day_6_side_b_ng = 0
            day_6_side_a_re = 0
            day_6_side_b_re = 0


        try:
            day_7_side_a_ng = (int(past_week_scrap(self)[24]) / 15000) *100
            day_7_side_b_ng = (int(past_week_scrap(self)[25]) / 15000) *100
            day_7_side_a_re = (int(past_week_scrap(self)[26]) / 15000) *100
            day_7_side_b_re = (int(past_week_scrap(self)[27]) / 15000) *100

        except:
            day_7_side_a_ng = 0
            day_7_side_b_ng = 0
            day_7_side_a_re = 0
            day_7_side_b_re = 0


        return render(request, "dolcegusto/line.html", {
        "day_1_side_a_ng": day_1_side_a_ng, "day_1_side_b_ng": day_1_side_b_ng,
        "day_1_side_a_re": day_1_side_a_re, "day_1_side_b_re": day_1_side_b_re,
        "day_2_side_a_ng": day_2_side_a_ng, "day_2_side_b_ng": day_2_side_b_ng,
        "day_2_side_a_re": day_2_side_a_re, "day_2_side_b_re": day_2_side_b_re,
        "day_3_side_a_ng": day_3_side_a_ng, "day_3_side_b_ng": day_3_side_b_ng,
        "day_3_side_a_re": day_3_side_a_re, "day_3_side_b_re": day_3_side_b_re,
        "day_4_side_a_ng": day_4_side_a_ng, "day_4_side_b_ng": day_4_side_b_ng,
        "day_4_side_a_re": day_4_side_a_re, "day_4_side_b_re": day_4_side_b_re,
        "day_5_side_a_ng": day_5_side_a_ng, "day_5_side_b_ng": day_5_side_b_ng,
        "day_5_side_a_re": day_5_side_a_re, "day_5_side_b_re": day_5_side_b_re,
        "day_6_side_a_ng": day_6_side_a_ng, "day_6_side_b_ng": day_6_side_b_ng,
        "day_6_side_a_re": day_6_side_a_re, "day_6_side_b_re": day_6_side_b_re,
        "day_7_side_a_ng": day_7_side_a_ng, "day_7_side_b_ng": day_7_side_b_ng,
        "day_7_side_a_re": day_7_side_a_re, "day_7_side_b_re": day_7_side_b_re,
        })

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
