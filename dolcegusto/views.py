from django.shortcuts import render
from django.views import View
import pandas as pd
from pandas import DataFrame
from datetime import datetime, date, timedelta

from dolcegusto.models import daily_report, hourly_report
from dolcegusto.times import get_weekday
from dolcegusto.get_values import past_seven_days



# assign the values to both sides (A and B) for the last 7 days
def daily_a_b(data_dict):
    combined_scrap_0_a = data_dict["line0_a_ng"] + data_dict["line0_a_re"]
    combined_scrap_0_b = data_dict["line0_b_ng"] + data_dict["line0_b_re"]
    combined_scrap_1_a = data_dict["line1_a_ng"] + data_dict["line1_a_re"]
    combined_scrap_1_b = data_dict["line1_b_ng"] + data_dict["line1_b_re"]
    combined_scrap_2_a = data_dict["line2_a_ng"] + data_dict["line2_a_re"]
    combined_scrap_2_b = data_dict["line2_b_ng"] + data_dict["line2_b_re"]
    combined_scrap_3_a = data_dict["line3_a_ng"] + data_dict["line3_a_re"]
    combined_scrap_3_b = data_dict["line3_b_ng"] + data_dict["line3_b_re"]
    combined_scrap_4_a = data_dict["line4_a_ng"] + data_dict["line4_a_re"]
    combined_scrap_4_b = data_dict["line4_b_ng"] + data_dict["line4_b_re"]
    combined_scrap_5_a = data_dict["line5_a_ng"] + data_dict["line5_a_re"]
    combined_scrap_5_b = data_dict["line5_b_ng"] + data_dict["line5_b_re"]
    combined_scrap_6_a = data_dict["line6_a_ng"] + data_dict["line6_a_re"]
    combined_scrap_6_b = data_dict["line6_b_ng"] + data_dict["line6_b_re"]

    return {
    "period_0_a":combined_scrap_0_a,
    "period_0_b":combined_scrap_0_b,
    "period_1_a":combined_scrap_1_a,
    "period_1_b":combined_scrap_1_b,
    "period_2_a":combined_scrap_2_a,
    "period_2_b":combined_scrap_2_b,
    "period_3_a":combined_scrap_3_a,
    "period_3_b":combined_scrap_3_b,
    "period_4_a":combined_scrap_4_a,
    "period_4_b":combined_scrap_4_b,
    "period_5_a":combined_scrap_5_a,
    "period_5_b":combined_scrap_5_b,
    "period_6_a":combined_scrap_6_a,
    "period_6_b":combined_scrap_6_b
    }

class Daily_dashboard(View):
    model = daily_report
    def get(self, request):

        line3 = daily_a_b(past_seven_days(3))
        line4 = daily_a_b(past_seven_days(4))
        line5 = daily_a_b(past_seven_days(5))
        line7 = daily_a_b(past_seven_days(7))
        line8 = daily_a_b(past_seven_days(8))
        line9 = daily_a_b(past_seven_days(9))
        line10 = daily_a_b(past_seven_days(10))

        return render(request, "dolcegusto/daily_dashboard.html", {
        "line_3": 3,
        "line_4": 4,
        "line_5": 5,
        "line_7": 7,
        "line_8": 8,
        "line_9": 9,
        "line_10": 10,
        "combined_scrap_0_3_a": line3["period_0_a"],
        "combined_scrap_0_3_b": line3["period_0_b"],
        "combined_scrap_1_3_a": line3["period_1_a"],
        "combined_scrap_1_3_b": line3["period_1_b"],
        "combined_scrap_2_3_a": line3["period_2_a"],
        "combined_scrap_2_3_b": line3["period_2_b"],
        "combined_scrap_3_3_a": line3["period_3_a"],
        "combined_scrap_3_3_b": line3["period_3_b"],
        "combined_scrap_4_3_a": line3["period_4_a"],
        "combined_scrap_4_3_b": line3["period_4_b"],
        "combined_scrap_5_3_a": line3["period_5_a"],
        "combined_scrap_5_3_b": line3["period_5_b"],
        "combined_scrap_6_3_a": line3["period_6_a"],
        "combined_scrap_6_3_b": line3["period_6_b"],

        "combined_scrap_0_4_a": line4["period_0_a"],
        "combined_scrap_0_4_b": line4["period_0_b"],
        "combined_scrap_1_4_a": line4["period_1_a"],
        "combined_scrap_1_4_b": line4["period_1_b"],
        "combined_scrap_2_4_a": line4["period_2_a"],
        "combined_scrap_2_4_b": line4["period_2_b"],
        "combined_scrap_3_4_a": line4["period_3_a"],
        "combined_scrap_3_4_b": line4["period_3_b"],
        "combined_scrap_4_4_a": line4["period_4_a"],
        "combined_scrap_4_4_b": line4["period_4_b"],
        "combined_scrap_5_4_a": line4["period_5_a"],
        "combined_scrap_5_4_b": line4["period_5_b"],
        "combined_scrap_6_4_a": line4["period_6_a"],
        "combined_scrap_6_4_b": line4["period_6_b"],

        "combined_scrap_0_5_a": line5["period_0_a"],
        "combined_scrap_0_5_b": line5["period_0_b"],
        "combined_scrap_1_5_a": line5["period_1_a"],
        "combined_scrap_1_5_b": line5["period_1_b"],
        "combined_scrap_2_5_a": line5["period_2_a"],
        "combined_scrap_2_5_b": line5["period_2_b"],
        "combined_scrap_3_5_a": line5["period_3_a"],
        "combined_scrap_3_5_b": line5["period_3_b"],
        "combined_scrap_4_5_a": line5["period_4_a"],
        "combined_scrap_4_5_b": line5["period_4_b"],
        "combined_scrap_5_5_a": line5["period_5_a"],
        "combined_scrap_5_5_b": line5["period_5_b"],
        "combined_scrap_6_5_a": line5["period_6_a"],
        "combined_scrap_6_5_b": line5["period_6_b"],

        "combined_scrap_0_7_a": line7["period_0_a"],
        "combined_scrap_0_7_b": line7["period_0_b"],
        "combined_scrap_1_7_a": line7["period_1_a"],
        "combined_scrap_1_7_b": line7["period_1_b"],
        "combined_scrap_2_7_a": line7["period_2_a"],
        "combined_scrap_2_7_b": line7["period_2_b"],
        "combined_scrap_3_7_a": line7["period_3_a"],
        "combined_scrap_3_7_b": line7["period_3_b"],
        "combined_scrap_4_7_a": line7["period_4_a"],
        "combined_scrap_4_7_b": line7["period_4_b"],
        "combined_scrap_5_7_a": line7["period_5_a"],
        "combined_scrap_5_7_b": line7["period_5_b"],
        "combined_scrap_6_7_a": line7["period_6_a"],
        "combined_scrap_6_7_b": line7["period_6_b"],

        "combined_scrap_0_8_a": line8["period_0_a"],
        "combined_scrap_0_8_b": line8["period_0_b"],
        "combined_scrap_1_8_a": line8["period_1_a"],
        "combined_scrap_1_8_b": line8["period_1_b"],
        "combined_scrap_2_8_a": line8["period_2_a"],
        "combined_scrap_2_8_b": line8["period_2_b"],
        "combined_scrap_3_8_a": line8["period_3_a"],
        "combined_scrap_3_8_b": line8["period_3_b"],
        "combined_scrap_4_8_a": line8["period_4_a"],
        "combined_scrap_4_8_b": line8["period_4_b"],
        "combined_scrap_5_8_a": line8["period_5_a"],
        "combined_scrap_5_8_b": line8["period_5_b"],
        "combined_scrap_6_8_a": line8["period_6_a"],
        "combined_scrap_6_8_b": line8["period_6_b"],

        "combined_scrap_0_9_a": line9["period_0_a"],
        "combined_scrap_0_9_b": line9["period_0_b"],
        "combined_scrap_1_9_a": line9["period_1_a"],
        "combined_scrap_1_9_b": line9["period_1_b"],
        "combined_scrap_2_9_a": line9["period_2_a"],
        "combined_scrap_2_9_b": line9["period_2_b"],
        "combined_scrap_3_9_a": line9["period_3_a"],
        "combined_scrap_3_9_b": line9["period_3_b"],
        "combined_scrap_4_9_a": line9["period_4_a"],
        "combined_scrap_4_9_b": line9["period_4_b"],
        "combined_scrap_5_9_a": line9["period_5_a"],
        "combined_scrap_5_9_b": line9["period_5_b"],
        "combined_scrap_6_9_a": line9["period_6_a"],
        "combined_scrap_6_9_b": line9["period_6_b"],

        "combined_scrap_0_10_a": line10["period_0_a"],
        "combined_scrap_0_10_b": line10["period_0_b"],
        "combined_scrap_1_10_a": line10["period_1_a"],
        "combined_scrap_1_10_b": line10["period_1_b"],
        "combined_scrap_2_10_a": line10["period_2_a"],
        "combined_scrap_2_10_b": line10["period_2_b"],
        "combined_scrap_3_10_a": line10["period_3_a"],
        "combined_scrap_3_10_b": line10["period_3_b"],
        "combined_scrap_4_10_a": line10["period_4_a"],
        "combined_scrap_4_10_b": line10["period_4_b"],
        "combined_scrap_5_10_a": line10["period_5_a"],
        "combined_scrap_5_10_b": line10["period_5_b"],
        "combined_scrap_6_10_a": line10["period_6_a"],
        "combined_scrap_6_10_b": line10["period_6_b"],
        })

class Line3_daily(View):
    model = daily_report
    def get(self, request):

        line3 = daily_a_b(past_seven_days(3))

        return render(request, "dolcegusto/line3_daily.html", {
        "line": 3,
        "combined_scrap_0_a": line3["period_0_a"],
        "combined_scrap_0_b": line3["period_0_b"],
        "combined_scrap_1_a": line3["period_1_a"],
        "combined_scrap_1_b": line3["period_1_b"],
        "combined_scrap_2_a": line3["period_2_a"],
        "combined_scrap_2_b": line3["period_2_b"],
        "combined_scrap_3_a": line3["period_3_a"],
        "combined_scrap_3_b": line3["period_3_b"],
        "combined_scrap_4_a": line3["period_4_a"],
        "combined_scrap_4_b": line3["period_4_b"],
        "combined_scrap_5_a": line3["period_5_a"],
        "combined_scrap_5_b": line3["period_5_b"],
        "combined_scrap_6_a": line3["period_6_a"],
        "combined_scrap_6_b": line3["period_6_b"]
        })

class Line4_daily(View):
    model = daily_report
    def get(self, request):

        line4 = daily_a_b(past_seven_days(4))

        return render(request, "dolcegusto/line4_daily.html", {
        "line": 4,
        "combined_scrap_0_a": line4["period_0_a"],
        "combined_scrap_0_b": line4["period_0_b"],
        "combined_scrap_1_a": line4["period_1_a"],
        "combined_scrap_1_b": line4["period_1_b"],
        "combined_scrap_2_a": line4["period_2_a"],
        "combined_scrap_2_b": line4["period_2_b"],
        "combined_scrap_3_a": line4["period_3_a"],
        "combined_scrap_3_b": line4["period_3_b"],
        "combined_scrap_4_a": line4["period_4_a"],
        "combined_scrap_4_b": line4["period_4_b"],
        "combined_scrap_5_a": line4["period_5_a"],
        "combined_scrap_5_b": line4["period_5_b"],
        "combined_scrap_6_a": line4["period_6_a"],
        "combined_scrap_6_b": line4["period_6_b"]
        })

class Line5_daily(View):
    model = daily_report
    def get(self, request):

        line5 = daily_a_b(past_seven_days(5))

        return render(request, "dolcegusto/line5_daily.html", {
        "line": 5,
        "combined_scrap_0_a": line5["period_0_a"],
        "combined_scrap_0_b": line5["period_0_b"],
        "combined_scrap_1_a": line5["period_1_a"],
        "combined_scrap_1_b": line5["period_1_b"],
        "combined_scrap_2_a": line5["period_2_a"],
        "combined_scrap_2_b": line5["period_2_b"],
        "combined_scrap_3_a": line5["period_3_a"],
        "combined_scrap_3_b": line5["period_3_b"],
        "combined_scrap_4_a": line5["period_4_a"],
        "combined_scrap_4_b": line5["period_4_b"],
        "combined_scrap_5_a": line5["period_5_a"],
        "combined_scrap_5_b": line5["period_5_b"],
        "combined_scrap_6_a": line5["period_6_a"],
        "combined_scrap_6_b": line5["period_6_b"]
        })

class Line7_daily(View):
    model = daily_report
    def get(self, request):

        line7 = daily_a_b(past_seven_days(7))

        return render(request, "dolcegusto/line7_daily.html", {
        "line": 7,
        "combined_scrap_0_a": line7["period_0_a"],
        "combined_scrap_0_b": line7["period_0_b"],
        "combined_scrap_1_a": line7["period_1_a"],
        "combined_scrap_1_b": line7["period_1_b"],
        "combined_scrap_2_a": line7["period_2_a"],
        "combined_scrap_2_b": line7["period_2_b"],
        "combined_scrap_3_a": line7["period_3_a"],
        "combined_scrap_3_b": line7["period_3_b"],
        "combined_scrap_4_a": line7["period_4_a"],
        "combined_scrap_4_b": line7["period_4_b"],
        "combined_scrap_5_a": line7["period_5_a"],
        "combined_scrap_5_b": line7["period_5_b"],
        "combined_scrap_6_a": line7["period_6_a"],
        "combined_scrap_6_b": line7["period_6_b"]
        })

class Line8_daily(View):
    model = daily_report
    def get(self, request):

        line8 = daily_a_b(past_seven_days(8))

        return render(request, "dolcegusto/line8_daily.html", {
        "line": 8,
        "combined_scrap_0_a": line8["period_0_a"],
        "combined_scrap_0_b": line8["period_0_b"],
        "combined_scrap_1_a": line8["period_1_a"],
        "combined_scrap_1_b": line8["period_1_b"],
        "combined_scrap_2_a": line8["period_2_a"],
        "combined_scrap_2_b": line8["period_2_b"],
        "combined_scrap_3_a": line8["period_3_a"],
        "combined_scrap_3_b": line8["period_3_b"],
        "combined_scrap_4_a": line8["period_4_a"],
        "combined_scrap_4_b": line8["period_4_b"],
        "combined_scrap_5_a": line8["period_5_a"],
        "combined_scrap_5_b": line8["period_5_b"],
        "combined_scrap_6_a": line8["period_6_a"],
        "combined_scrap_6_b": line8["period_6_b"]
        })

class Line9_daily(View):
    model = daily_report
    def get(self, request):

        line9 = daily_a_b(past_seven_days(9))

        return render(request, "dolcegusto/line9_daily.html", {
        "line": 9,
        "combined_scrap_0_a": line9["period_0_a"],
        "combined_scrap_0_b": line9["period_0_b"],
        "combined_scrap_1_a": line9["period_1_a"],
        "combined_scrap_1_b": line9["period_1_b"],
        "combined_scrap_2_a": line9["period_2_a"],
        "combined_scrap_2_b": line9["period_2_b"],
        "combined_scrap_3_a": line9["period_3_a"],
        "combined_scrap_3_b": line9["period_3_b"],
        "combined_scrap_4_a": line9["period_4_a"],
        "combined_scrap_4_b": line9["period_4_b"],
        "combined_scrap_5_a": line9["period_5_a"],
        "combined_scrap_5_b": line9["period_5_b"],
        "combined_scrap_6_a": line9["period_6_a"],
        "combined_scrap_6_b": line9["period_6_b"]
        })

class Line10_daily(View):
    model = daily_report
    def get(self, request):

        line10 = daily_a_b(past_seven_days(10))

        return render(request, "dolcegusto/line10_daily.html", {
        "line": 10,
        "combined_scrap_0_a": line10["period_0_a"],
        "combined_scrap_0_b": line10["period_0_b"],
        "combined_scrap_1_a": line10["period_1_a"],
        "combined_scrap_1_b": line10["period_1_b"],
        "combined_scrap_2_a": line10["period_2_a"],
        "combined_scrap_2_b": line10["period_2_b"],
        "combined_scrap_3_a": line10["period_3_a"],
        "combined_scrap_3_b": line10["period_3_b"],
        "combined_scrap_4_a": line10["period_4_a"],
        "combined_scrap_4_b": line10["period_4_b"],
        "combined_scrap_5_a": line10["period_5_a"],
        "combined_scrap_5_b": line10["period_5_b"],
        "combined_scrap_6_a": line10["period_6_a"],
        "combined_scrap_6_b": line10["period_6_b"]
        })
