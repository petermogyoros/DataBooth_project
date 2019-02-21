from django.shortcuts import render
from django.views import View
import pandas as pd
from pandas import DataFrame
from datetime import datetime, date, timedelta

from dolcegusto.models import hourly_report, daily_report, weekly_report, monthly_report
from dolcegusto.get_values import past_seven_hours, past_seven_days, past_seven_weeks, past_seven_months


def final_values_to_render(line, values):

    return {
        "line": line,
        "combined_scrap_0_a": values["combined_a_ng_0"] + values["combined_a_re_0"],
        "combined_scrap_0_b": values["combined_b_ng_0"] + values["combined_b_re_0"],
        "combined_scrap_1_a": values["combined_a_ng_1"] + values["combined_a_re_1"],
        "combined_scrap_1_b": values["combined_b_ng_1"] + values["combined_b_re_1"],
        "combined_scrap_2_a": values["combined_a_ng_2"] + values["combined_a_re_2"],
        "combined_scrap_2_b": values["combined_b_ng_2"] + values["combined_b_re_2"],
        "combined_scrap_3_a": values["combined_a_ng_3"] + values["combined_a_re_3"],
        "combined_scrap_3_b": values["combined_b_ng_3"] + values["combined_b_re_3"],
        "combined_scrap_4_a": values["combined_a_ng_4"] + values["combined_a_re_4"],
        "combined_scrap_4_b": values["combined_b_ng_4"] + values["combined_b_re_4"],
        "combined_scrap_5_a": values["combined_a_ng_5"] + values["combined_a_re_5"],
        "combined_scrap_5_b": values["combined_b_ng_5"] + values["combined_b_re_5"],
        "combined_scrap_6_a": values["combined_a_ng_6"] + values["combined_a_re_6"],
        "combined_scrap_6_b": values["combined_b_ng_6"] + values["combined_b_re_6"],

        "combined_ng_0_a":values["combined_a_ng_0"],
        "combined_ng_0_b":values["combined_b_ng_0"],
        "combined_ng_1_a":values["combined_a_ng_1"],
        "combined_ng_1_b":values["combined_b_ng_1"],
        "combined_ng_2_a":values["combined_a_ng_2"],
        "combined_ng_2_b":values["combined_b_ng_2"],
        "combined_ng_3_a":values["combined_a_ng_3"],
        "combined_ng_3_b":values["combined_b_ng_3"],
        "combined_ng_4_a":values["combined_a_ng_4"],
        "combined_ng_4_b":values["combined_b_ng_4"],
        "combined_ng_5_a":values["combined_a_ng_5"],
        "combined_ng_5_b":values["combined_b_ng_5"],
        "combined_ng_6_a":values["combined_a_ng_6"],
        "combined_ng_6_b":values["combined_b_ng_6"],

        "combined_re_0_a":values["combined_a_re_0"],
        "combined_re_0_b":values["combined_b_re_0"],
        "combined_re_1_a":values["combined_a_re_1"],
        "combined_re_1_b":values["combined_b_re_1"],
        "combined_re_2_a":values["combined_a_re_2"],
        "combined_re_2_b":values["combined_b_re_2"],
        "combined_re_3_a":values["combined_a_re_3"],
        "combined_re_3_b":values["combined_b_re_3"],
        "combined_re_4_a":values["combined_a_re_4"],
        "combined_re_4_b":values["combined_b_re_4"],
        "combined_re_5_a":values["combined_a_re_5"],
        "combined_re_5_b":values["combined_b_re_5"],
        "combined_re_6_a":values["combined_a_re_6"],
        "combined_re_6_b":values["combined_b_re_6"],

        "top_ng_0_a":values["top_a_0_ng"],
        "top_ng_0_b":values["top_b_0_ng"],
        "top_ng_1_a":values["top_a_1_ng"],
        "top_ng_1_b":values["top_b_1_ng"],
        "top_ng_2_a":values["top_a_2_ng"],
        "top_ng_2_b":values["top_b_2_ng"],
        "top_ng_3_a":values["top_a_3_ng"],
        "top_ng_3_a":values["top_a_3_ng"],
        "top_ng_4_b":values["top_b_4_ng"],
        "top_ng_4_a":values["top_a_4_ng"],
        "top_ng_5_b":values["top_b_5_ng"],
        "top_ng_5_a":values["top_a_5_ng"],
        "top_ng_6_b":values["top_b_6_ng"],
        "top_ng_6_a":values["top_a_6_ng"],

        "top_re_0_a":values["top_a_0_re"],
        "top_re_0_b":values["top_b_0_re"],
        "top_re_1_a":values["top_a_1_re"],
        "top_re_1_b":values["top_b_1_re"],
        "top_re_2_a":values["top_a_2_re"],
        "top_re_2_b":values["top_b_2_re"],
        "top_re_3_a":values["top_a_3_re"],
        "top_re_3_a":values["top_a_3_re"],
        "top_re_4_b":values["top_b_4_re"],
        "top_re_4_a":values["top_a_4_re"],
        "top_re_5_b":values["top_b_5_re"],
        "top_re_5_a":values["top_a_5_re"],
        "top_re_6_b":values["top_b_6_re"],
        "top_re_6_a":values["top_a_6_re"],

        "bottom_ng_0_a":values["bottom_a_0_ng"],
        "bottom_ng_0_b":values["bottom_b_0_ng"],
        "bottom_ng_1_a":values["bottom_a_1_ng"],
        "bottom_ng_1_b":values["bottom_b_1_ng"],
        "bottom_ng_2_a":values["bottom_a_2_ng"],
        "bottom_ng_2_b":values["bottom_b_2_ng"],
        "bottom_ng_3_a":values["bottom_a_3_ng"],
        "bottom_ng_3_a":values["bottom_a_3_ng"],
        "bottom_ng_4_b":values["bottom_b_4_ng"],
        "bottom_ng_4_a":values["bottom_a_4_ng"],
        "bottom_ng_5_b":values["bottom_b_5_ng"],
        "bottom_ng_5_a":values["bottom_a_5_ng"],
        "bottom_ng_6_b":values["bottom_b_6_ng"],
        "bottom_ng_6_a":values["bottom_a_6_ng"],

        "bottom_re_0_a":values["bottom_a_0_re"],
        "bottom_re_0_b":values["bottom_b_0_re"],
        "bottom_re_1_a":values["bottom_a_1_re"],
        "bottom_re_1_b":values["bottom_b_1_re"],
        "bottom_re_2_a":values["bottom_a_2_re"],
        "bottom_re_2_b":values["bottom_b_2_re"],
        "bottom_re_3_a":values["bottom_a_3_re"],
        "bottom_re_3_a":values["bottom_a_3_re"],
        "bottom_re_4_b":values["bottom_b_4_re"],
        "bottom_re_4_a":values["bottom_a_4_re"],
        "bottom_re_5_b":values["bottom_b_5_re"],
        "bottom_re_5_a":values["bottom_a_5_re"],
        "bottom_re_6_b":values["bottom_b_6_re"],
        "bottom_re_6_a":values["bottom_a_6_re"],

        "side_ng_0_a":values["side_a_0_ng"],
        "side_ng_0_b":values["side_b_0_ng"],
        "side_ng_1_a":values["side_a_1_ng"],
        "side_ng_1_b":values["side_b_1_ng"],
        "side_ng_2_a":values["side_a_2_ng"],
        "side_ng_2_b":values["side_b_2_ng"],
        "side_ng_3_a":values["side_a_3_ng"],
        "side_ng_3_a":values["side_a_3_ng"],
        "side_ng_4_b":values["side_b_4_ng"],
        "side_ng_4_a":values["side_a_4_ng"],
        "side_ng_5_b":values["side_b_5_ng"],
        "side_ng_5_a":values["side_a_5_ng"],
        "side_ng_6_b":values["side_b_6_ng"],
        "side_ng_6_a":values["side_a_6_ng"],

        "side_re_0_a":values["side_a_0_re"],
        "side_re_0_b":values["side_b_0_re"],
        "side_re_1_a":values["side_a_1_re"],
        "side_re_1_b":values["side_b_1_re"],
        "side_re_2_a":values["side_a_2_re"],
        "side_re_2_b":values["side_b_2_re"],
        "side_re_3_a":values["side_a_3_re"],
        "side_re_3_a":values["side_a_3_re"],
        "side_re_4_b":values["side_b_4_re"],
        "side_re_4_a":values["side_a_4_re"],
        "side_re_5_b":values["side_b_5_re"],
        "side_re_5_a":values["side_a_5_re"],
        "side_re_6_b":values["side_b_6_re"],
        "side_re_6_a":values["side_a_6_re"],
        }

class Hourly_dashboard(View):
    model = hourly_report
    def get(self, request):

        line3 = past_seven_hours(3)
        line4 = past_seven_hours(4)
        line5 = past_seven_hours(5)
        line7 = past_seven_hours(7)
        line8 = past_seven_hours(8)
        line9 = past_seven_hours(9)
        line10 = past_seven_hours(10)

        return render(request, "dolcegusto/weekly_dashboard.html", {
        "line_3": 3,
        "line_4": 4,
        "line_5": 5,
        "line_7": 7,
        "line_8": 8,
        "line_9": 9,
        "line_10": 10,
        "combined_scrap_0_3_a": final_values_to_render(3, line3).combined_a_ng_0,
        "combined_scrap_0_3_b": final_values_to_render(3, line3).combined_b_ng_0,

        "combined_scrap_0_4_a": final_values_to_render(4, line3).combined_a_ng_0,
        "combined_scrap_0_4_b": final_values_to_render(4, line3).combined_b_ng_0,

        "combined_scrap_0_5_a": final_values_to_render(5, line3).combined_a_ng_0,
        "combined_scrap_0_5_b": final_values_to_render(5, line3).combined_b_ng_0,

        "combined_scrap_0_7_a": final_values_to_render(7, line3).combined_a_ng_0,
        "combined_scrap_0_7_b": final_values_to_render(7, line3).combined_b_ng_0,

        "combined_scrap_0_8_a": final_values_to_render(8, line3).combined_a_ng_0,
        "combined_scrap_0_8_b": final_values_to_render(8, line3).combined_b_ng_0,

        "combined_scrap_0_9_a": final_values_to_render(9, line3).combined_a_ng_0,
        "combined_scrap_0_9_b": final_values_to_render(9, line3).combined_b_ng_0,

        "combined_scrap_0_10_a": final_values_to_render(10, line3).combined_a_ng_0,
        "combined_scrap_0_10_b": final_values_to_render(10, line3).combined_b_ng_0,
        })

class Line3_hourly(View):
    model = hourly_report

    def get(self, request):

        line3 = past_seven_hours(3)
        # print(line3)
        return render(request, "dolcegusto/hourly_data.html", final_values_to_render(3, line3))

class Line4_hourly(View):
    model = hourly_report
    def get(self, request):

        line4 = past_seven_hours(4)

        return render(request, "dolcegusto/hourly_data.html", final_values_to_render(4, line4))

class Line5_hourly(View):
    model = hourly_report
    def get(self, request):

        line5 = past_seven_hours(5)

        return render(request, "dolcegusto/hourly_data.html", final_values_to_render(5, line5))

class Line7_hourly(View):
    model = hourly_report
    def get(self, request):

        line7 = past_seven_hours(7)

        return render(request, "dolcegusto/hourly_data.html", final_values_to_render(7, line7))

class Line8_hourly(View):
    model = hourly_report
    def get(self, request):

        line8 = past_seven_hours(8)

        return render(request, "dolcegusto/hourly_data.html", final_values_to_render(8, line8))

class Line9_hourly(View):
    model = hourly_report
    def get(self, request):

        line9 = apast_seven_hours(9)

        return render(request, "dolcegusto/hourly_data.html", final_values_to_render(9, line9))

class Line10_hourly(View):
    model = hourly_report
    def get(self, request):

        line10 = past_seven_hours(10)

        return render(request, "dolcegusto/hourly_data.html", final_values_to_render(10, line10))


class Daily_dashboard(View):
    model = daily_report
    def get(self, request):

        line3 = past_seven_days(3)
        line4 = past_seven_days(4)
        line5 = past_seven_days(5)
        line7 = past_seven_days(7)
        line8 = past_seven_days(8)
        line9 = past_seven_days(9)
        line10 = past_seven_days(10)

        return render(request, "dolcegusto/daily_dashboard.html", {
        "line_3": 3,
        "line_4": 4,
        "line_5": 5,
        "line_7": 7,
        "line_8": 8,
        "line_9": 9,
        "line_10": 10,
        "combined_scrap_0_3_a": final_values_to_render(3, line3)["combined_a_ng_0"],
        "combined_scrap_0_3_b": final_values_to_render(3, line3)["combined_b_ng_0"],

        "combined_scrap_0_4_a": final_values_to_render(4, line4).combined_a_ng_0,
        "combined_scrap_0_4_b": final_values_to_render(4, line4).combined_b_ng_0,

        "combined_scrap_0_5_a": final_values_to_render(5, line5).combined_a_ng_0,
        "combined_scrap_0_5_b": final_values_to_render(5, line5).combined_b_ng_0,

        "combined_scrap_0_7_a": final_values_to_render(7, line7).combined_a_ng_0,
        "combined_scrap_0_7_b": final_values_to_render(7, line7).combined_b_ng_0,

        "combined_scrap_0_8_a": final_values_to_render(8, line8).combined_a_ng_0,
        "combined_scrap_0_8_b": final_values_to_render(8, line8).combined_b_ng_0,

        "combined_scrap_0_9_a": final_values_to_render(9, line9).combined_a_ng_0,
        "combined_scrap_0_9_b": final_values_to_render(9, line9).combined_b_ng_0,

        "combined_scrap_0_10_a": final_values_to_render(10, line10).combined_a_ng_0,
        "combined_scrap_0_10_b": final_values_to_render(10, line10).combined_b_ng_0,
        })

class Line3_daily(View):
    model = daily_report
    def get(self, request):

        line3 = past_seven_days(3)

        return render(request, "dolcegusto/daily_data.html", final_values_to_render(3, line3))

class Line4_daily(View):
    model = daily_report
    def get(self, request):

        line4 = past_seven_days(4)

        return render(request, "dolcegusto/daily_data.html", final_values_to_render(4, line4))

class Line5_daily(View):
    model = daily_report
    def get(self, request):

        line5 = past_seven_days(5)

        return render(request, "dolcegusto/daily_data.html", final_values_to_render(5, line5))

class Line7_daily(View):
    model = daily_report
    def get(self, request):

        line7 = past_seven_days(7)

        return render(request, "dolcegusto/daily_data.html", final_values_to_render(7, line7))

class Line8_daily(View):
    model = daily_report
    def get(self, request):

        line8 = past_seven_days(8)

        return render(request, "dolcegusto/daily_data.html", final_values_to_render(8, line8))

class Line9_daily(View):
    model = daily_report
    def get(self, request):

        line9 = past_seven_days(9)

        return render(request, "dolcegusto/daily_data.html", final_values_to_render(9, line9))

class Line10_daily(View):
    model = daily_report
    def get(self, request):

        line10 = past_seven_days(10)

        return render(request, "dolcegusto/daily_data.html", final_values_to_render(10, line10))


class Weekly_dashboard(View):
    model = weekly_report
    def get(self, request):

        line3 = assign_a_b_for_period(past_seven_weeks(3))
        line4 = assign_a_b_for_period(past_seven_weeks(4))
        line5 = assign_a_b_for_period(past_seven_weeks(5))
        line7 = assign_a_b_for_period(past_seven_weeks(7))
        line8 = assign_a_b_for_period(past_seven_weeks(8))
        line9 = assign_a_b_for_period(past_seven_weeks(9))
        line10 = assign_a_b_for_period(past_seven_weeks(10))

        return render(request, "dolcegusto/weekly_dashboard.html", {
        "line_3": 3,
        "line_4": 4,
        "line_5": 5,
        "line_7": 7,
        "line_8": 8,
        "line_9": 9,
        "line_10": 10,
        "combined_scrap_0_3_a": line3["period_0_a"],
        "combined_scrap_0_3_b": line3["period_0_b"],

        "combined_scrap_0_4_a": line4["period_0_a"],
        "combined_scrap_0_4_b": line4["period_0_b"],

        "combined_scrap_0_5_a": line5["period_0_a"],
        "combined_scrap_0_5_b": line5["period_0_b"],

        "combined_scrap_0_7_a": line7["period_0_a"],
        "combined_scrap_0_7_b": line7["period_0_b"],

        "combined_scrap_0_8_a": line8["period_0_a"],
        "combined_scrap_0_8_b": line8["period_0_b"],

        "combined_scrap_0_9_a": line9["period_0_a"],
        "combined_scrap_0_9_b": line9["period_0_b"],

        "combined_scrap_0_10_a": line10["period_0_a"],
        "combined_scrap_0_10_b": line10["period_0_b"],
        })

class Line3_weekly(View):
    model = weekly_report
    def get(self, request):

        line3 = past_seven_weeks(3)

        return render(request, "dolcegusto/weekly_data.html", final_values_to_render(3, line3))

class Line4_weekly(View):
    model = weekly_report
    def get(self, request):

        line4 = past_seven_weeks(4)

        return render(request, "dolcegusto/weekly_data.html", final_values_to_render(4, line4))

class Line5_weekly(View):
    model = weekly_report
    def get(self, request):

        line5 = past_seven_weeks(5)

        return render(request, "dolcegusto/weekly_data.html", final_values_to_render(5, line5))

class Line7_weekly(View):
    model = weekly_report
    def get(self, request):

        line7 = past_seven_weeks(7)

        return render(request, "dolcegusto/weekly_data.html", final_values_to_render(7, line7))

class Line8_weekly(View):
    model = weekly_report
    def get(self, request):

        line8 = past_seven_weeks(8)

        return render(request, "dolcegusto/weekly_data.html", final_values_to_render(8, line8))

class Line9_weekly(View):
    model = weekly_report
    def get(self, request):

        line9 = past_seven_weeks(9)

        return render(request, "dolcegusto/weekly_data.html", final_values_to_render(9, line9))

class Line10_weekly(View):
    model = weekly_report
    def get(self, request):

        line10 = past_seven_weeks(10)

        return render(request, "dolcegusto/weekly_data.html", final_values_to_render(10, line10))


class Monthly_dashboard(View):
    model = monthly_report
    def get(self, request):

        line3 = assign_a_b_for_period(past_seven_months(3))
        line4 = assign_a_b_for_period(past_seven_months(4))
        line5 = assign_a_b_for_period(past_seven_months(5))
        line7 = assign_a_b_for_period(past_seven_months(7))
        line8 = assign_a_b_for_period(past_seven_months(8))
        line9 = assign_a_b_for_period(past_seven_months(9))
        line10 = assign_a_b_for_period(past_seven_months(10))

        return render(request, "dolcegusto/monthly_dashboard.html", {
        "line_3": 3,
        "line_4": 4,
        "line_5": 5,
        "line_7": 7,
        "line_8": 8,
        "line_9": 9,
        "line_10": 10,
        "combined_scrap_0_3_a": line3["period_0_a"],
        "combined_scrap_0_3_b": line3["period_0_b"],

        "combined_scrap_0_4_a": line4["period_0_a"],
        "combined_scrap_0_4_b": line4["period_0_b"],

        "combined_scrap_0_5_a": line5["period_0_a"],
        "combined_scrap_0_5_b": line5["period_0_b"],

        "combined_scrap_0_7_a": line7["period_0_a"],
        "combined_scrap_0_7_b": line7["period_0_b"],

        "combined_scrap_0_8_a": line8["period_0_a"],
        "combined_scrap_0_8_b": line8["period_0_b"],

        "combined_scrap_0_9_a": line9["period_0_a"],
        "combined_scrap_0_9_b": line9["period_0_b"],

        "combined_scrap_0_10_a": line10["period_0_a"],
        "combined_scrap_0_10_b": line10["period_0_b"],
        })

class Line3_monthly(View):
    model = monthly_report
    def get(self, request):

        line3 = past_seven_months(3)

        return render(request, "dolcegusto/monthly_data.html", final_values_to_render(3, line3))

class Line4_monthly(View):
    model = monthly_report
    def get(self, request):

        line4 = past_seven_months(4)

        return render(request, "dolcegusto/monthly_data.html", final_values_to_render(4, line4))

class Line5_monthly(View):
    model = monthly_report
    def get(self, request):

        line5 = past_seven_months(5)

        return render(request, "dolcegusto/monthly_data.html", final_values_to_render(5, line5))

class Line7_monthly(View):
    model = monthly_report
    def get(self, request):

        line7 = past_seven_months(7)

        return render(request, "dolcegusto/monthly_data.html", final_values_to_render(7, line7))

class Line8_monthly(View):
    model = monthly_report
    def get(self, request):

        line8 = past_seven_months(8)

        return render(request, "dolcegusto/monthly_data.html", final_values_to_render(8, line8))

class Line9_monthly(View):
    model = monthly_report
    def get(self, request):

        line9 = past_seven_months(9)

        return render(request, "dolcegusto/monthly_data.html", final_values_to_render(9, line9))

class Line10_monthly(View):
    model = monthly_report
    def get(self, request):

        line10 = past_seven_months(10)

        return render(request, "dolcegusto/monthly_data.html", final_values_to_render(10, line10))
