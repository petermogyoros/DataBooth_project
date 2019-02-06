from dolcegusto.models import daily_report, hourly_report, weekly_report, monthly_report
from datetime import datetime, date, timedelta, time
import datetime

def reset_dictionary():
    # set all values to zero to avoid data contamination from previous requests

    values = {
    "top_a_0":0, "top_a_1":0, "top_a_2":0, "top_a_3":0, "top_a_4":0, "top_a_5":0, "top_a_6":0,
    "side_a_0":0, "side_a_1":0, "side_a_2":0, "side_a_3":0, "side_a_4":0, "side_a_5":0, "side_a_6":0,
    "bottom_a_0":0, "bottom_a_1":0, "bottom_a_2":0, "bottom_a_3":0, "bottom_a_4":0, "bottom_a_5":0, "bottom_a_6":0,
    "combined_a_ng_0":0, "combined_a_ng_1":0, "combined_a_ng_2":0, "combined_a_ng_3":0, "combined_a_ng_4":0, "combined_a_ng_5":0, "combined_a_ng_6":0,
    "combined_a_re_0":0, "combined_a_re_1":0, "combined_a_re_2":0,  "combined_a_re_3":0, "combined_a_re_4":0, "combined_a_re_5":0, "combined_a_re_6":0,

    "top_b_0":0, "top_b_1":0, "top_b_2":0, "top_b_3":0, "top_b_4":0, "top_b_5":0, "top_b_6":0,
    "side_b_0":0, "side_b_1":0, "side_b_2":0, "side_b_3":0, "side_b_4":0, "side_b_5":0, "side_b_6":0,
    "bottom_b_0":0, "bottom_b_1":0, "bottom_b_2":0, "bottom_b_3":0, "bottom_b_4":0, "bottom_b_5":0, "bottom_b_6":0,
    "combined_b_ng_0":0, "combined_b_ng_1":0, "combined_b_ng_2":0, "combined_b_ng_3":0, "combined_b_ng_4":0, "combined_b_ng_5":0, "combined_b_ng_6":0,
    "combined_b_re_0":0, "combined_b_re_1":0, "combined_b_re_2":0, "combined_b_re_3":0, "combined_b_re_4":0, "combined_b_re_5":0, "combined_b_re_6":0,
    }

    return values


# categorise outputs based on time period
def period(period, line):


    if period == "hourly":

        # current time (hour)
        now = int(str(datetime.datetime.now().time())[0:2])

        # set hour values
        this_hour = now
        hour_ago = now-1
        two_hours_ago = now-2
        three_hours_ago = now-3
        four_hours_ago = now-4
        five_hours_ago = now-5
        six_hours_ago = now-6

        # set hour values taking into account the 24 hour cycle
        if now == 0:
            hour_ago = 23
            two_hours_ago = 22
            three_hours_ago = 21
            four_hours_ago = 20
            five_hours_ago = 19
            six_hours_ago = 18

        elif now == 1:
            two_hours_ago = 23
            three_hours_ago = 22
            four_hours_ago = 21
            five_hours_ago = 20
            six_hours_ago = 19

        elif now == 2:
            three_hours_ago = 23
            four_hours_ago = 22
            five_hours_ago = 21
            six_hours_ago = 20

        elif now == 3:
            four_hours_ago = 23
            five_hours_ago = 22
            six_hours_ago = 21

        elif now == 4:
            five_hours_ago = 23
            six_hours_ago = 22

        elif now == 5:
            six_hours_ago = 23

        # Assign times from database entry
        prod_time0 = int(str(hourly_report(line).hour[0])[11:13])
        prod_time1 = int(str(hourly_report(line).hour[1])[11:13])
        prod_time2 = int(str(hourly_report(line).hour[2])[11:13])
        prod_time3 = int(str(hourly_report(line).hour[3])[11:13])
        prod_time4 = int(str(hourly_report(line).hour[4])[11:13])
        prod_time5 = int(str(hourly_report(line).hour[5])[11:13])
        prod_time6 = int(str(hourly_report(line).hour[6])[11:13])


        periods = {
        "prod_period_0":prod_time0,
        "prod_period_1":prod_time1,
        "prod_period_2":prod_time2,
        "prod_period_3":prod_time3,
        "prod_period_4":prod_time4,
        "prod_period_5":prod_time5,
        "prod_period_6":prod_time6,

        "cur_period_0":this_hour,
        "cur_period_1":hour_ago,
        "cur_period_2":two_hours_ago,
        "cur_period_3":three_hours_ago,
        "cur_period_4":four_hours_ago,
        "cur_period_5":five_hours_ago,
        "cur_period_6":six_hours_ago
        }

        return periods

    elif period == "daily":

        # get production dates from database
        day_number_0 = str(daily_report(line).production_day[0])[0:10]
        day_number_1 = str(daily_report(line).production_day[1])[0:10]
        day_number_2 = str(daily_report(line).production_day[2])[0:10]
        day_number_3 = str(daily_report(line).production_day[3])[0:10]
        day_number_4 = str(daily_report(line).production_day[4])[0:10]
        day_number_5 = str(daily_report(line).production_day[5])[0:10]
        day_number_6 = str(daily_report(line).production_day[6])[0:10]

        # get current dates for the past 7 intervals
        today = date.today().strftime('%Y-%m-%d')
        yesterday = (date.today() - timedelta(days=1)).strftime('%Y-%m-%d')
        two_days_ago = (date.today() - timedelta(days=2)).strftime('%Y-%m-%d')
        three_days_ago = (date.today() - timedelta(days=3)).strftime('%Y-%m-%d')
        four_days_ago = (date.today() - timedelta(days=4)).strftime('%Y-%m-%d')
        five_days_ago = (date.today() - timedelta(days=5)).strftime('%Y-%m-%d')
        six_days_ago = (date.today() - timedelta(days=6)).strftime('%Y-%m-%d')

        periods = {
        "prod_period_0":day_number_0,
        "prod_period_1":day_number_1,
        "prod_period_2":day_number_2,
        "prod_period_3":day_number_3,
        "prod_period_4":day_number_4,
        "prod_period_5":day_number_5,
        "prod_period_6":day_number_6,

        "cur_period_0":today,
        "cur_period_1":yesterday,
        "cur_period_2":two_days_ago,
        "cur_period_3":three_days_ago,
        "cur_period_4":four_days_ago,
        "cur_period_5":five_days_ago,
        "cur_period_6":six_days_ago
        }

        return periods

    elif period == "weekly":

        # Get week number from database date. This will return a 3-tuple, (ISO year, ISO week number, ISO weekday)
        week_number_0 = (date.isocalendar(weekly_report(line).production_week[0]))[1]
        week_number_1 = (date.isocalendar(weekly_report(line).production_week[1]))[1]
        week_number_2 = (date.isocalendar(weekly_report(line).production_week[2]))[1]
        week_number_3 = (date.isocalendar(weekly_report(line).production_week[3]))[1]
        week_number_4 = (date.isocalendar(weekly_report(line).production_week[4]))[1]
        week_number_5 = (date.isocalendar(weekly_report(line).production_week[5]))[1]
        week_number_6 = (date.isocalendar(weekly_report(line).production_week[6]))[1]

        # Current week numbers (past 7 weeks)
        this_week = date.isocalendar((datetime.datetime.now()))[1]
        one_week_ago = (date.isocalendar((datetime.datetime.now()))[1])-1
        two_weeks_ago = (date.isocalendar((datetime.datetime.now()))[1])-2
        three_weeks_ago = (date.isocalendar((datetime.datetime.now()))[1])-3
        four_weeks_ago = (date.isocalendar((datetime.datetime.now()))[1])-4
        five_weeks_ago = (date.isocalendar((datetime.datetime.now()))[1])-5
        six_weeks_ago = (date.isocalendar((datetime.datetime.now()))[1])-6

        periods = {
        "prod_period_0":week_number_0,
        "prod_period_1":week_number_1,
        "prod_period_2":week_number_2,
        "prod_period_3":week_number_3,
        "prod_period_4":week_number_4,
        "prod_period_5":week_number_5,
        "prod_period_6":week_number_6,

        "cur_period_0":this_week,
        "cur_period_1":one_week_ago,
        "cur_period_2":two_weeks_ago,
        "cur_period_3":three_weeks_ago,
        "cur_period_4":four_weeks_ago,
        "cur_period_5":five_weeks_ago,
        "cur_period_6":six_weeks_ago
        }

        return periods

    elif period == "monthly":

        # Month numbers for the past 7 monhts
        this_month = int(date.today().strftime('%m'))
        last_month = int(date.today().strftime('%m')) - 1
        two_months_ago = int(date.today().strftime('%m')) - 2
        three_months_ago = int(date.today().strftime('%m')) - 3
        four_months_ago = int(date.today().strftime('%m')) - 4
        five_months_ago = int(date.today().strftime('%m')) - 5
        six_months_ago = int(date.today().strftime('%m')) - 6

        # Production month numbers
        month_number_0 = int(str(monthly_report(line).production_month[0])[5:7])
        month_number_1 = int(str(monthly_report(line).production_month[1])[5:7])
        month_number_2 = int(str(monthly_report(line).production_month[2])[5:7])
        month_number_3 = int(str(monthly_report(line).production_month[3])[5:7])
        try:
            month_number_4 = int(str(monthly_report(line).production_month[4])[5:7])
        except:
            month_number_4 = 0
        try:
            month_number_5 = int(str(monthly_report(line).production_month[5])[5:7])
        except:
            month_number_5 = 0
        try:
            month_number_6 = int(str(monthly_report(line).production_month[6])[5:7])
        except:
            month_number_6 = 0

        # accounts for current date corerction due to 12 month cycle
        if this_month == 1:
            last_month = 12
            two_months_ago = 11
            three_months_ago = 10
            four_months_ago = 9
            five_months_ago = 8
            six_months_ago = 7

        elif this_month == 2:
            two_months_ago = 12
            three_months_ago = 11
            four_months_ago = 10
            five_months_ago = 9
            six_months_ago = 8

        elif this_month == 3:
            three_months_ago = 12
            four_months_ago = 11
            five_months_ago = 10
            six_months_ago = 9

        elif this_month == 4:
            four_months_ago = 12
            five_months_ago = 11
            six_months_ago = 10

        elif this_month == 5:
            five_months_ago = 12
            six_months_ago = 11

        elif this_month == 6:
            six_months_ago = 12

        periods = {
        "prod_period_0":month_number_0,
        "prod_period_1":month_number_1,
        "prod_period_2":month_number_2,
        "prod_period_3":month_number_3,
        "prod_period_4":month_number_4,
        "prod_period_5":month_number_5,
        "prod_period_6":month_number_6,

        "cur_period_0":this_month,
        "cur_period_1":last_month,
        "cur_period_2":two_months_ago,
        "cur_period_3":three_months_ago,
        "cur_period_4":four_months_ago,
        "cur_period_5":five_months_ago,
        "cur_period_6":six_months_ago
        }

        return periods

def assign_period_values(r, line, period_span, requested_period):

    # assign variables from specific columns from database based on date
    for_count = 0
    for i in requested_period(line).combined_side_a_ng:
        for_count += 1

        if for_count == 1:
            if period_span["prod_period_0"] == period_span["cur_period_0"]:
                r["combined_a_ng_0"] = i
            elif period_span["prod_period_0"]  == period_span["cur_period_1"]:
                r["combined_a_ng_1"] = i
            elif period_span["prod_period_0"]  == period_span["cur_period_2"]:
                r["combined_a_ng_2"] = i
            elif period_span["prod_period_0"]  == period_span["cur_period_3"]:
                r["combined_a_ng_3"] = i
            elif period_span["prod_period_0"]  == period_span["cur_period_4"]:
                r["combined_a_ng_4"] = i
            elif period_span["prod_period_0"]  == period_span["cur_period_5"]:
                r["combined_a_ng_5"] = i
            elif period_span["prod_period_0"]  == period_span["cur_period_6"]:
                r["combined_a_ng_6"] = i


        elif for_count == 2:
            if period_span["prod_period_1"]  == period_span["cur_period_1"]:
                r["combined_a_ng_1"] = i
            elif period_span["prod_period_1"]  == period_span["cur_period_2"]:
                r["combined_a_ng_2"] = i
            elif period_span["prod_period_1"]  == period_span["cur_period_3"]:
                r["combined_a_ng_3"] = i
            elif period_span["prod_period_1"]  == period_span["cur_period_4"]:
                r["combined_a_ng_4"] = i
            elif period_span["prod_period_1"]  == period_span["cur_period_5"]:
                r["combined_a_ng_5"] = i
            elif period_span["prod_period_1"]  == period_span["cur_period_6"]:
                r["combined_a_ng_6"] = i

        elif for_count == 3:
            if period_span["prod_period_2"]  == period_span["cur_period_2"]:
                r["combined_a_ng_2"] = i
            elif period_span["prod_period_2"]  ==period_span["cur_period_3"]:
                r["combined_a_ng_3"] = i
            elif period_span["prod_period_2"]  == period_span["cur_period_4"]:
                r["combined_a_ng_4"] = i
            elif period_span["prod_period_2"]  == period_span["cur_period_5"]:
                r["combined_a_ng_5"] = i
            elif period_span["prod_period_2"]  == period_span["cur_period_6"]:
                r["combined_a_ng_6"] = i

        elif for_count == 4:
            if period_span["prod_period_3"]  ==period_span["cur_period_3"]:
                r["combined_a_ng_3"] = i
            elif period_span["prod_period_3"]  == period_span["cur_period_4"]:
                r["combined_a_ng_4"] = i
            elif period_span["prod_period_3"]  == period_span["cur_period_5"]:
                r["combined_a_ng_5"] = i
            elif period_span["prod_period_3"]  == period_span["cur_period_6"]:
                r["combined_a_ng_6"] = i

        elif for_count == 5:
            if period_span["prod_period_4"]  == period_span["cur_period_4"]:
                r["combined_a_ng_4"] = i
            elif period_span["prod_period_4"]  == period_span["cur_period_5"]:
                r["combined_a_ng_5"] = i
            elif period_span["prod_period_4"]  == period_span["cur_period_6"]:
                r["combined_a_ng_6"] = i

        elif for_count == 6:
            if period_span["prod_period_5"]  == period_span["cur_period_5"]:
                r["combined_a_ng_5"] = i
            elif period_span["prod_period_5"]  == period_span["cur_period_6"]:
                r["combined_a_ng_6"] = i

        elif for_count == 7:
            if period_span["prod_period_6"]  == period_span["cur_period_6"]:
                r["combined_a_ng_6"] = i

    # assign variables from specific columns from database based on date
    for_count = 0
    for e in requested_period(line).combined_side_b_ng:
        for_count += 1
        if for_count == 1:
            if period_span["prod_period_0"]  == period_span["cur_period_0"]:
                r["combined_b_ng_0"] = e
            elif period_span["prod_period_0"]  == period_span["cur_period_1"]:
                r["combined_b_ng_1"] = e
            elif period_span["prod_period_0"]  == period_span["cur_period_2"]:
                r["combined_b_ng_2"] = e
            elif period_span["prod_period_0"]  ==period_span["cur_period_3"]:
                r["combined_b_ng_3"] = e
            elif period_span["prod_period_0"]  == period_span["cur_period_4"]:
                r["combined_b_ng_4"] = e
            elif period_span["prod_period_0"]  == period_span["cur_period_5"]:
                r["combined_b_ng_5"] = e
            elif period_span["prod_period_0"]  == period_span["cur_period_6"]:
                r["combined_b_ng_6"] = e

        elif for_count == 2:
            if period_span["prod_period_1"]  == period_span["cur_period_1"]:
                r["combined_b_ng_1"] = e
            elif period_span["prod_period_1"]  == period_span["cur_period_2"]:
                r["combined_b_ng_2"] = e
            elif period_span["prod_period_1"]  ==period_span["cur_period_3"]:
                r["combined_b_ng_3"] = e
            elif period_span["prod_period_1"]  == period_span["cur_period_4"]:
                r["combined_b_ng_4"] = e
            elif period_span["prod_period_1"]  == period_span["cur_period_5"]:
                r["combined_b_ng_5"] = e
            elif period_span["prod_period_1"]  == period_span["cur_period_6"]:
                r["combined_b_ng_6"] = e

        elif for_count == 3:
            if period_span["prod_period_2"]  == period_span["cur_period_2"]:
                r["combined_b_ng_2"] = e
            elif period_span["prod_period_2"]  ==period_span["cur_period_3"]:
                r["combined_b_ng_3"] = e
            elif period_span["prod_period_2"]  == period_span["cur_period_4"]:
                r["combined_b_ng_4"] = e
            elif period_span["prod_period_2"]  == period_span["cur_period_5"]:
                r["combined_b_ng_5"] = e
            elif period_span["prod_period_2"]  == period_span["cur_period_6"]:
                r["combined_b_ng_6"] = e

        elif for_count == 4:
            if period_span["prod_period_3"]  ==period_span["cur_period_3"]:
                r["combined_b_ng_3"] = e
            elif period_span["prod_period_3"]  == period_span["cur_period_4"]:
                r["combined_b_ng_4"] = e
            elif period_span["prod_period_3"]  == period_span["cur_period_5"]:
                r["combined_b_ng_5"] = e
            elif period_span["prod_period_3"]  == period_span["cur_period_6"]:
                r["combined_b_ng_6"] = e

        elif for_count == 5:
            if period_span["prod_period_4"]  == period_span["cur_period_4"]:
                r["combined_b_ng_4"] = e
            elif period_span["prod_period_4"]  == period_span["cur_period_5"]:
                r["combined_b_ng_5"] = e
            elif period_span["prod_period_4"]  == period_span["cur_period_6"]:
                r["combined_b_ng_6"] = e

        elif for_count == 6:
            if period_span["prod_period_5"]  == period_span["cur_period_5"]:
                r["combined_b_ng_5"] = e
            elif period_span["prod_period_5"]  == period_span["cur_period_6"]:
                r["combined_b_ng_6"] = e

        elif for_count == 7:
            if period_span["prod_period_6"]  == period_span["cur_period_6"]:
                r["combined_b_ng_6"] = e

    for_count = 0
    for a in requested_period(line).combined_side_a_re:
        for_count += 1
        if for_count == 1:
            if period_span["prod_period_0"]  == period_span["cur_period_0"]:
                r["combined_a_re_0"] = a
            elif period_span["prod_period_0"]  == period_span["cur_period_1"]:
                r["combined_a_re_1"] = a
            elif period_span["prod_period_0"]  == period_span["cur_period_2"]:
                r["combined_a_re_2"] = a
            elif period_span["prod_period_0"]  ==period_span["cur_period_3"]:
                r["combined_a_re_3"] = a
            elif period_span["prod_period_0"]  == period_span["cur_period_4"]:
                r["combined_a_re_4"] = a
            elif period_span["prod_period_0"]  == period_span["cur_period_5"]:
                r["combined_a_re_5"] = a
            elif period_span["prod_period_0"]  == period_span["cur_period_6"]:
                r["combined_a_re_6"] = a


        elif for_count == 2:
            if period_span["prod_period_1"]  == period_span["cur_period_1"]:
                r["combined_a_re_1"] = a
            elif period_span["prod_period_1"]  == period_span["cur_period_2"]:
                r["combined_a_re_2"] = a
            elif period_span["prod_period_1"]  ==period_span["cur_period_3"]:
                r["combined_a_re_3"] = a
            elif period_span["prod_period_1"]  == period_span["cur_period_4"]:
                r["combined_a_re_4"] = a
            elif period_span["prod_period_1"]  == period_span["cur_period_5"]:
                r["combined_a_re_5"] = a
            elif period_span["prod_period_1"]  == period_span["cur_period_6"]:
                r["combined_a_re_6"] = a

        elif for_count == 3:
            if period_span["prod_period_2"]  == period_span["cur_period_2"]:
                r["combined_a_re_2"] = a
            elif period_span["prod_period_2"]  ==period_span["cur_period_3"]:
                r["combined_a_re_3"] = a
            elif period_span["prod_period_2"]  == period_span["cur_period_4"]:
                r["combined_a_re_4"] = a
            elif period_span["prod_period_2"]  == period_span["cur_period_5"]:
                r["combined_a_re_5"] = a
            elif period_span["prod_period_2"]  == period_span["cur_period_6"]:
                r["combined_a_re_6"] = a

        elif for_count == 4:
            if period_span["prod_period_3"]  ==period_span["cur_period_3"]:
                r["combined_a_re_3"] = a
            elif period_span["prod_period_3"]  == period_span["cur_period_4"]:
                r["combined_a_re_4"] = a
            elif period_span["prod_period_3"]  == period_span["cur_period_5"]:
                r["combined_a_re_5"] = a
            elif period_span["prod_period_3"]  == period_span["cur_period_6"]:
                r["combined_a_re_6"] = a

        elif for_count == 5:
            if period_span["prod_period_4"]  == period_span["cur_period_4"]:
                r["combined_a_re_4"] = a
            elif period_span["prod_period_4"]  == period_span["cur_period_5"]:
                r["combined_a_re_5"] = a
            elif period_span["prod_period_4"]  == period_span["cur_period_6"]:
                r["combined_a_re_6"] = a

        elif for_count == 6:
            if period_span["prod_period_5"]  == period_span["cur_period_5"]:
                r["combined_a_re_5"] = a
            elif period_span["prod_period_5"]  == period_span["cur_period_6"]:
                r["combined_a_re_6"] = a

        elif for_count == 7:
            if period_span["prod_period_6"]  == period_span["cur_period_6"]:
                r["combined_a_re_6"] = a

    # assign variables from specific columns from database based on date
    for_count = 0
    for u in requested_period(line).combined_side_b_re:
        for_count += 1
        if for_count == 1:
            if period_span["prod_period_0"]  == period_span["cur_period_0"]:
                r["combined_b_re_0"] = u
            elif period_span["prod_period_0"]  == period_span["cur_period_1"]:
                r["combined_b_re_1"] = u
            elif period_span["prod_period_0"]  == period_span["cur_period_2"]:
                r["combined_b_re_2"] = u
            elif period_span["prod_period_0"]  ==period_span["cur_period_3"]:
                r["combined_b_re_3"] = u
            elif period_span["prod_period_0"]  == period_span["cur_period_4"]:
                r["combined_b_re_4"] = u
            elif period_span["prod_period_0"]  == period_span["cur_period_5"]:
                r["combined_b_re_5"] = u
            elif period_span["prod_period_0"]  == period_span["cur_period_6"]:
                r["combined_b_re_6"] = u

        elif for_count == 2:
            if period_span["prod_period_1"]  == period_span["cur_period_1"]:
                r["combined_b_re_1"] = u
            elif period_span["prod_period_1"]  == period_span["cur_period_2"]:
                r["combined_b_re_2"] = u
            elif period_span["prod_period_1"]  ==period_span["cur_period_3"]:
                r["combined_b_re_3"] = u
            elif period_span["prod_period_1"]  == period_span["cur_period_4"]:
                r["combined_b_re_4"] = u
            elif period_span["prod_period_1"]  == period_span["cur_period_5"]:
                r["combined_b_re_5"] = u
            elif period_span["prod_period_1"]  == period_span["cur_period_6"]:
                r["combined_b_re_6"] = u

        elif for_count == 3:
            if period_span["prod_period_2"]  == period_span["cur_period_2"]:
                r["combined_b_re_2"] = u
            elif period_span["prod_period_2"]  ==period_span["cur_period_3"]:
                r["combined_b_re_3"] = u
            elif period_span["prod_period_2"]  == period_span["cur_period_4"]:
                r["combined_b_re_4"] = u
            elif period_span["prod_period_2"]  == period_span["cur_period_5"]:
                r["combined_b_re_5"] = u
            elif period_span["prod_period_2"]  == period_span["cur_period_6"]:
                r["combined_b_re_6"] = u

        elif for_count == 4:
            if period_span["prod_period_3"]  ==period_span["cur_period_3"]:
                r["combined_b_re_3"] = u
            elif period_span["prod_period_3"]  == period_span["cur_period_4"]:
                r["combined_b_re_4"] = u
            elif period_span["prod_period_3"]  == period_span["cur_period_5"]:
                r["combined_b_re_5"] = u
            elif period_span["prod_period_3"]  == period_span["cur_period_6"]:
                r["combined_b_re_6"] = u

        elif for_count == 5:
            if period_span["prod_period_4"]  == period_span["cur_period_4"]:
                r["combined_b_re_4"] = u
            elif period_span["prod_period_4"]  == period_span["cur_period_5"]:
                r["combined_b_re_5"] = u
            elif period_span["prod_period_4"]  == period_span["cur_period_6"]:
                r["combined_b_re_6"] = u

        elif for_count == 6:
            if period_span["prod_period_5"]  == period_span["cur_period_5"]:
                r["combined_b_re_5"] = u
            elif period_span["prod_period_5"]  == period_span["cur_period_6"]:
                r["combined_b_re_6"] = u

        elif for_count == 7:
            if period_span["prod_period_6"]  == period_span["cur_period_6"]:
                r["combined_b_re_6"] = u

    return r


def past_seven_hours(line):

    # set all valeus of the dictionary to 0
    r = reset_dictionary()

    period_span = period("hourly", line)
    requested_period = hourly_report
    # assign values to the dictionary keys
    set_values_for_a_dictionary = assign_period_values(r, line, period_span, requested_period)



    return {
    "line":line,
    "line0_a_ng":r["combined_a_ng_0"],
    "line1_a_ng":r["combined_a_ng_1"],
    "line2_a_ng":r["combined_a_ng_2"],
    "line3_a_ng":r["combined_a_ng_3"],
    "line4_a_ng":r["combined_a_ng_4"],
    "line5_a_ng":r["combined_a_ng_5"],
    "line6_a_ng":r["combined_a_ng_6"],

    "line0_b_ng":r["combined_b_ng_0"],
    "line1_b_ng":r["combined_b_ng_1"],
    "line2_b_ng":r["combined_b_ng_2"],
    "line3_b_ng":r["combined_b_ng_3"],
    "line4_b_ng":r["combined_b_ng_4"],
    "line5_b_ng":r["combined_b_ng_5"],
    "line6_b_ng":r["combined_b_ng_6"],

    "line0_a_re":r["combined_a_re_0"],
    "line1_a_re":r["combined_a_re_1"],
    "line2_a_re":r["combined_a_re_2"],
    "line3_a_re":r["combined_a_re_3"],
    "line4_a_re":r["combined_a_re_4"],
    "line5_a_re":r["combined_a_re_5"],
    "line6_a_re":r["combined_a_re_6"],

    "line0_b_re":r["combined_b_re_0"],
    "line1_b_re":r["combined_b_re_1"],
    "line2_b_re":r["combined_b_re_2"],
    "line3_b_re":r["combined_b_re_3"],
    "line4_b_re":r["combined_b_re_4"],
    "line5_b_re":r["combined_b_re_5"],
    "line6_b_re":r["combined_b_re_6"],
    }

def past_seven_days(line):

    # set all valeus of the dictionary to 0
    r = reset_dictionary()

    period_span = period("daily", line)
    requested_period = daily_report
    # assign values to the dictionary keys
    set_values_for_a_dictionary = assign_period_values(r, line, period_span, requested_period)



    return {
    "line":line,
    "line0_a_ng":r["combined_a_ng_0"],
    "line1_a_ng":r["combined_a_ng_1"],
    "line2_a_ng":r["combined_a_ng_2"],
    "line3_a_ng":r["combined_a_ng_3"],
    "line4_a_ng":r["combined_a_ng_4"],
    "line5_a_ng":r["combined_a_ng_5"],
    "line6_a_ng":r["combined_a_ng_6"],

    "line0_b_ng":r["combined_b_ng_0"],
    "line1_b_ng":r["combined_b_ng_1"],
    "line2_b_ng":r["combined_b_ng_2"],
    "line3_b_ng":r["combined_b_ng_3"],
    "line4_b_ng":r["combined_b_ng_4"],
    "line5_b_ng":r["combined_b_ng_5"],
    "line6_b_ng":r["combined_b_ng_6"],

    "line0_a_re":r["combined_a_re_0"],
    "line1_a_re":r["combined_a_re_1"],
    "line2_a_re":r["combined_a_re_2"],
    "line3_a_re":r["combined_a_re_3"],
    "line4_a_re":r["combined_a_re_4"],
    "line5_a_re":r["combined_a_re_5"],
    "line6_a_re":r["combined_a_re_6"],

    "line0_b_re":r["combined_b_re_0"],
    "line1_b_re":r["combined_b_re_1"],
    "line2_b_re":r["combined_b_re_2"],
    "line3_b_re":r["combined_b_re_3"],
    "line4_b_re":r["combined_b_re_4"],
    "line5_b_re":r["combined_b_re_5"],
    "line6_b_re":r["combined_b_re_6"],
    }

def past_seven_weeks(line):

    # set all valeus of the dictionary to 0
    r = reset_dictionary()

    period_span = period("weekly", line)
    requested_period = weekly_report
    # assign values to the dictionary keys
    set_values_for_a_dictionary = assign_period_values(r, line, period_span, requested_period)



    return {
    "line":line,
    "line0_a_ng":r["combined_a_ng_0"],
    "line1_a_ng":r["combined_a_ng_1"],
    "line2_a_ng":r["combined_a_ng_2"],
    "line3_a_ng":r["combined_a_ng_3"],
    "line4_a_ng":r["combined_a_ng_4"],
    "line5_a_ng":r["combined_a_ng_5"],
    "line6_a_ng":r["combined_a_ng_6"],

    "line0_b_ng":r["combined_b_ng_0"],
    "line1_b_ng":r["combined_b_ng_1"],
    "line2_b_ng":r["combined_b_ng_2"],
    "line3_b_ng":r["combined_b_ng_3"],
    "line4_b_ng":r["combined_b_ng_4"],
    "line5_b_ng":r["combined_b_ng_5"],
    "line6_b_ng":r["combined_b_ng_6"],

    "line0_a_re":r["combined_a_re_0"],
    "line1_a_re":r["combined_a_re_1"],
    "line2_a_re":r["combined_a_re_2"],
    "line3_a_re":r["combined_a_re_3"],
    "line4_a_re":r["combined_a_re_4"],
    "line5_a_re":r["combined_a_re_5"],
    "line6_a_re":r["combined_a_re_6"],

    "line0_b_re":r["combined_b_re_0"],
    "line1_b_re":r["combined_b_re_1"],
    "line2_b_re":r["combined_b_re_2"],
    "line3_b_re":r["combined_b_re_3"],
    "line4_b_re":r["combined_b_re_4"],
    "line5_b_re":r["combined_b_re_5"],
    "line6_b_re":r["combined_b_re_6"],
    }

def past_seven_months(line):

    # set all valeus of the dictionary to 0
    r = reset_dictionary()


    period_span = period("monthly", line)
    requested_period = monthly_report

    # assign values to the dictionary keys
    set_values_for_a_dictionary = assign_period_values(r, line, period_span, requested_period)



    return {
    "line":line,
    "line0_a_ng":r["combined_a_ng_0"],
    "line1_a_ng":r["combined_a_ng_1"],
    "line2_a_ng":r["combined_a_ng_2"],
    "line3_a_ng":r["combined_a_ng_3"],
    "line4_a_ng":r["combined_a_ng_4"],
    "line5_a_ng":r["combined_a_ng_5"],
    "line6_a_ng":r["combined_a_ng_6"],

    "line0_b_ng":r["combined_b_ng_0"],
    "line1_b_ng":r["combined_b_ng_1"],
    "line2_b_ng":r["combined_b_ng_2"],
    "line3_b_ng":r["combined_b_ng_3"],
    "line4_b_ng":r["combined_b_ng_4"],
    "line5_b_ng":r["combined_b_ng_5"],
    "line6_b_ng":r["combined_b_ng_6"],

    "line0_a_re":r["combined_a_re_0"],
    "line1_a_re":r["combined_a_re_1"],
    "line2_a_re":r["combined_a_re_2"],
    "line3_a_re":r["combined_a_re_3"],
    "line4_a_re":r["combined_a_re_4"],
    "line5_a_re":r["combined_a_re_5"],
    "line6_a_re":r["combined_a_re_6"],

    "line0_b_re":r["combined_b_re_0"],
    "line1_b_re":r["combined_b_re_1"],
    "line2_b_re":r["combined_b_re_2"],
    "line3_b_re":r["combined_b_re_3"],
    "line4_b_re":r["combined_b_re_4"],
    "line5_b_re":r["combined_b_re_5"],
    "line6_b_re":r["combined_b_re_6"],
    }
