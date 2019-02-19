from dolcegusto.models import daily_report, hourly_report, weekly_report, monthly_report
from datetime import datetime, date, timedelta, time
import datetime

def reset_dictionary():
    # set all values to zero to avoid data contamination from previous requests

    values = {
    "top_a_0_ng":0, "top_a_1_ng":0, "top_a_2_ng":0, "top_a_3_ng":0, "top_a_4_ng":0, "top_a_5_ng":0, "top_a_6_ng":0,
    "top_a_0_re":0, "top_a_1_re":0, "top_a_2_re":0, "top_a_3_re":0, "top_a_4_re":0, "top_a_5_re":0, "top_a_6_re":0,

    "side_a_0_ng":0, "side_a_1_ng":0, "side_a_2_ng":0, "side_a_3_ng":0, "side_a_4_ng":0, "side_a_5_ng":0, "side_a_6_ng":0,
    "side_a_0_re":0, "side_a_1_re":0, "side_a_2_re":0, "side_a_3_re":0, "side_a_4_re":0, "side_a_5_re":0, "side_a_6_re":0,

    "bottom_a_0_ng":0, "bottom_a_1_ng":0, "bottom_a_2_ng":0, "bottom_a_3_ng":0, "bottom_a_4_ng":0, "bottom_a_5_ng":0, "bottom_a_6_ng":0,
    "bottom_a_0_re":0, "bottom_a_1_re":0, "bottom_a_2_re":0, "bottom_a_3_re":0, "bottom_a_4_re":0, "bottom_a_5_re":0, "bottom_a_6_re":0,

    "combined_a_ng_0":0, "combined_a_ng_1":0, "combined_a_ng_2":0, "combined_a_ng_3":0, "combined_a_ng_4":0, "combined_a_ng_5":0, "combined_a_ng_6":0,
    "combined_a_re_0":0, "combined_a_re_1":0, "combined_a_re_2":0,  "combined_a_re_3":0, "combined_a_re_4":0, "combined_a_re_5":0, "combined_a_re_6":0,

    "top_b_0_ng":0, "top_b_1_ng":0, "top_b_2_ng":0, "top_b_3_ng":0, "top_b_4_ng":0, "top_b_5_ng":0, "top_b_6_ng":0,
    "top_b_0_re":0, "top_b_1_re":0, "top_b_2_re":0, "top_b_3_re":0, "top_b_4_re":0, "top_b_5_re":0, "top_b_6_re":0,

    "side_b_0_ng":0, "side_b_1_ng":0, "side_b_2_ng":0, "side_b_3_ng":0, "side_b_4_ng":0, "side_b_5_ng":0, "side_b_6_ng":0,
    "side_b_0_re":0, "side_b_1_re":0, "side_b_2_re":0, "side_b_3_re":0, "side_b_4_re":0, "side_b_5_re":0, "side_b_6_re":0,

    "bottom_b_0_ng":0, "bottom_b_1_ng":0, "bottom_b_2_ng":0, "bottom_b_3_ng":0, "bottom_b_4_ng":0, "bottom_b_5_ng":0, "bottom_b_6_ng":0,
    "bottom_b_0_re":0, "bottom_b_1_re":0, "bottom_b_2_re":0, "bottom_b_3_re":0, "bottom_b_4_re":0, "bottom_b_5_re":0, "bottom_b_6_re":0,

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
        # In case there are no (or not enough) entries in the DB the try/except will set missing values to zero
        try:
            month_number_0 = int(str(monthly_report(line).production_month[0])[5:7])
        except:
            month_number_0 = 0
        try:
            month_number_1 = int(str(monthly_report(line).production_month[1])[5:7])
        except:
            month_number_1 = 0
        try:
            month_number_2 = int(str(monthly_report(line).production_month[2])[5:7])
        except:
            month_number_2 = 0
        try:
            month_number_3 = int(str(monthly_report(line).production_month[3])[5:7])
        except:
            month_number_3 = 0
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

        combined_side_a_ng_0 = requested_period(line).combined_side_a_ng[0]
        combined_side_b_ng_0 = requested_period(line).combined_side_b_ng[0]
        combined_side_a_re_0 = requested_period(line).combined_side_a_re[0]
        combined_side_b_re_0 = requested_period(line).combined_side_b_re[0]

        a_top_ng_0 = requested_period(line).a_top_ng[0]
        b_top_ng_0 = requested_period(line).b_top_ng[0]
        a_top_re_0 = requested_period(line).a_top_re[0]
        b_top_re_0 = requested_period(line).b_top_re[0]

        a_bottom_ng_0 = requested_period(line).a_bottom_ng[0]
        b_bottom_ng_0 = requested_period(line).b_bottom_ng[0]
        a_bottom_re_0 = requested_period(line).a_bottom_re[0]
        b_bottom_re_0 = requested_period(line).b_bottom_re[0]

        a_side_ng_0 = requested_period(line).a_side_ng[0]
        b_side_ng_0 = requested_period(line).b_side_ng[0]
        a_side_re_0 = requested_period(line).a_side_re[0]
        b_side_re_0 = requested_period(line).b_side_re[0]

        combined_side_a_ng_1 = requested_period(line).combined_side_a_ng[1]
        combined_side_b_ng_1 = requested_period(line).combined_side_b_ng[1]
        combined_side_a_re_1 = requested_period(line).combined_side_a_re[1]
        combined_side_b_re_1 = requested_period(line).combined_side_b_re[1]

        a_top_ng_1 = requested_period(line).a_top_ng[1]
        b_top_ng_1 = requested_period(line).b_top_ng[1]
        a_top_re_1 = requested_period(line).a_top_re[1]
        b_top_re_1 = requested_period(line).b_top_re[1]

        a_bottom_ng_1 = requested_period(line).a_bottom_ng[1]
        b_bottom_ng_1 = requested_period(line).b_bottom_ng[1]
        a_bottom_re_1 = requested_period(line).a_bottom_re[1]
        b_bottom_re_1 = requested_period(line).b_bottom_re[1]

        a_side_ng_1 = requested_period(line).a_side_ng[1]
        b_side_ng_1 = requested_period(line).b_side_ng[1]
        a_side_re_1 = requested_period(line).a_side_re[1]
        b_side_re_1 = requested_period(line).b_side_re[1]

        combined_side_a_ng_2 = requested_period(line).combined_side_a_ng[2]
        combined_side_b_ng_2 = requested_period(line).combined_side_b_ng[2]
        combined_side_a_re_2 = requested_period(line).combined_side_a_re[2]
        combined_side_b_re_2 = requested_period(line).combined_side_b_re[2]

        a_top_ng_2 = requested_period(line).a_top_ng[2]
        b_top_ng_2 = requested_period(line).b_top_ng[2]
        a_top_re_2 = requested_period(line).a_top_re[2]
        b_top_re_2 = requested_period(line).b_top_re[2]

        a_bottom_ng_2 = requested_period(line).a_bottom_ng[2]
        b_bottom_ng_2 = requested_period(line).b_bottom_ng[2]
        a_bottom_re_2 = requested_period(line).a_bottom_re[2]
        b_bottom_re_2 = requested_period(line).b_bottom_re[2]

        a_side_ng_2 = requested_period(line).a_side_ng[2]
        b_side_ng_2 = requested_period(line).b_side_ng[2]
        a_side_re_2 = requested_period(line).a_side_re[2]
        b_side_re_2 = requested_period(line).b_side_re[2]

        combined_side_a_ng_3 = requested_period(line).combined_side_a_ng[3]
        combined_side_b_ng_3 = requested_period(line).combined_side_b_ng[3]
        combined_side_a_re_3 = requested_period(line).combined_side_a_re[3]
        combined_side_b_re_3 = requested_period(line).combined_side_b_re[3]

        a_top_ng_3 = requested_period(line).a_top_ng[3]
        b_top_ng_3 = requested_period(line).b_top_ng[3]
        a_top_re_3 = requested_period(line).a_top_re[3]
        b_top_re_3 = requested_period(line).b_top_re[3]

        a_bottom_ng_3 = requested_period(line).a_bottom_ng[3]
        b_bottom_ng_3 = requested_period(line).b_bottom_ng[3]
        a_bottom_re_3 = requested_period(line).a_bottom_re[3]
        b_bottom_re_3 = requested_period(line).b_bottom_re[3]

        a_side_ng_3 = requested_period(line).a_side_ng[3]
        b_side_ng_3 = requested_period(line).b_side_ng[3]
        a_side_re_3 = requested_period(line).a_side_re[3]
        b_side_re_3 = requested_period(line).b_side_re[3]

        combined_side_a_ng_4 = requested_period(line).combined_side_a_ng[4]
        combined_side_b_ng_4 = requested_period(line).combined_side_b_ng[4]
        combined_side_a_re_4 = requested_period(line).combined_side_a_re[4]
        combined_side_b_re_4 = requested_period(line).combined_side_b_re[4]

        a_top_ng_4 = requested_period(line).a_top_ng[4]
        b_top_ng_4 = requested_period(line).b_top_ng[4]
        a_top_re_4 = requested_period(line).a_top_re[4]
        b_top_re_4 = requested_period(line).b_top_re[4]

        a_bottom_ng_4 = requested_period(line).a_bottom_ng[4]
        b_bottom_ng_4 = requested_period(line).b_bottom_ng[4]
        a_bottom_re_4 = requested_period(line).a_bottom_re[4]
        b_bottom_re_4 = requested_period(line).b_bottom_re[4]

        a_side_ng_4 = requested_period(line).a_side_ng[4]
        b_side_ng_4 = requested_period(line).b_side_ng[4]
        a_side_re_4 = requested_period(line).a_side_re[4]
        b_side_re_4 = requested_period(line).b_side_re[4]

        combined_side_a_ng_5 = requested_period(line).combined_side_a_ng[5]
        combined_side_b_ng_5 = requested_period(line).combined_side_b_ng[5]
        combined_side_a_re_5 = requested_period(line).combined_side_a_re[5]
        combined_side_b_re_5 = requested_period(line).combined_side_b_re[5]

        a_top_ng_5 = requested_period(line).a_top_ng[5]
        b_top_ng_5 = requested_period(line).b_top_ng[5]
        a_top_re_5 = requested_period(line).a_top_re[5]
        b_top_re_5 = requested_period(line).b_top_re[5]

        a_bottom_ng_5 = requested_period(line).a_bottom_ng[5]
        b_bottom_ng_5 = requested_period(line).b_bottom_ng[5]
        a_bottom_re_5 = requested_period(line).a_bottom_re[5]
        b_bottom_re_5 = requested_period(line).b_bottom_re[5]

        a_side_ng_5 = requested_period(line).a_side_ng[5]
        b_side_ng_5 = requested_period(line).b_side_ng[5]
        a_side_re_5 = requested_period(line).a_side_re[5]
        b_side_re_5 = requested_period(line).b_side_re[5]

        combined_side_a_ng_6 = requested_period(line).combined_side_a_ng[6]
        combined_side_b_ng_6 = requested_period(line).combined_side_b_ng[6]
        combined_side_a_re_6 = requested_period(line).combined_side_a_re[6]
        combined_side_b_re_6 = requested_period(line).combined_side_b_re[6]

        a_top_ng_6 = requested_period(line).a_top_ng[6]
        b_top_ng_6 = requested_period(line).b_top_ng[6]
        a_top_re_6 = requested_period(line).a_top_re[6]
        b_top_re_6 = requested_period(line).b_top_re[6]

        a_bottom_ng_6 = requested_period(line).a_bottom_ng[6]
        b_bottom_ng_6 = requested_period(line).b_bottom_ng[6]
        a_bottom_re_6 = requested_period(line).a_bottom_re[6]
        b_bottom_re_6 = requested_period(line).b_bottom_re[6]

        a_side_ng_6 = requested_period(line).a_side_ng[6]
        b_side_ng_6 = requested_period(line).b_side_ng[6]
        a_side_re_6 = requested_period(line).a_side_re[6]
        b_side_re_6 = requested_period(line).b_side_re[6]


        if for_count == 1:
            if period_span["prod_period_0"] == period_span["cur_period_0"]:
                r["combined_a_ng_0"] = combined_side_a_ng_0
                r["combined_a_re_0"] = combined_side_a_re_0
                r["top_a_0_ng"] = a_top_ng_0
                r["top_a_0_re"] = a_top_re_0
                r["bottom_a_0_ng"] = a_bottom_ng_0
                r["bottom_a_0_re"] = a_bottom_re_0
                r["side_a_0_ng"] = a_side_ng_0
                r["side_a_0_re"] = a_side_re_0

                r["combined_b_ng_0"] = combined_side_b_ng_0
                r["combined_b_re_0"] = combined_side_b_re_0
                r["top_b_0_ng"] = b_top_ng_0
                r["top_b_0_re"] = b_top_re_0
                r["bottom_b_0_ng"] = b_bottom_ng_0
                r["bottom_b_0_re"] = b_bottom_re_0
                r["side_b_0_ng"] = b_side_ng_0
                r["side_b_0_re"] = b_side_re_0

            elif period_span["prod_period_0"]  == period_span["cur_period_1"]:
                r["combined_a_ng_1"] = combined_side_a_ng_0
                r["combined_a_re_1"] = combined_side_a_re_0
                r["top_a_1_ng"] = a_top_ng_0
                r["top_a_1_re"] = a_top_re_0
                r["bottom_a_1_ng"] = a_bottom_ng_0
                r["bottom_a_1_re"] = a_bottom_re_0
                r["side_a_1_ng"] = a_side_ng_0
                r["side_a_1_re"] = a_side_re_0

                r["combined_b_ng_1"] = combined_side_b_ng_0
                r["combined_b_re_1"] = combined_side_b_re_0
                r["top_b_1_ng"] = b_top_ng_0
                r["top_b_1_re"] = b_top_re_0
                r["bottom_b_1_ng"] = b_bottom_ng_0
                r["bottom_b_1_re"] = b_bottom_re_0
                r["side_b_1_ng"] = b_side_ng_0
                r["side_b_1_re"] = b_side_re_0

            elif period_span["prod_period_0"]  == period_span["cur_period_2"]:
                r["combined_a_ng_2"] = combined_side_a_ng_0
                r["combined_a_re_2"] = combined_side_a_re_0
                r["top_a_2_ng"] = a_top_ng_0
                r["top_a_2_re"] = a_top_re_0
                r["bottom_a_2_ng"] = a_bottom_ng_0
                r["bottom_a_2_re"] = a_bottom_re_0
                r["side_a_2_ng"] = a_side_ng_0
                r["side_a_2_re"] = a_side_re_0

                r["combined_b_ng_2"] = combined_side_b_ng_0
                r["combined_b_re_2"] = combined_side_b_re_0
                r["top_b_2_ng"] = b_top_ng_0
                r["top_b_2_re"] = b_top_re_0
                r["bottom_b_2_ng"] = b_bottom_ng_0
                r["bottom_b_0_re"] = b_bottom_re_0
                r["side_b_2_ng"] = b_side_ng_0
                r["side_b_2_re"] = b_side_re_0

            elif period_span["prod_period_0"]  == period_span["cur_period_3"]:
                r["combined_a_ng_3"] = combined_side_a_ng_0
                r["combined_a_re_3"] = combined_side_a_re_0
                r["top_a_3_ng"] = a_top_ng_0
                r["top_a_3_re"] = a_top_re_0
                r["bottom_a_3_ng"] = a_bottom_ng_0
                r["bottom_a_3_re"] = a_bottom_re_0
                r["side_a_3_ng"] = a_side_ng_0
                r["side_a_3_re"] = a_side_re_0

                r["combined_b_ng_3"] = combined_side_b_ng_0
                r["combined_b_re_3"] = combined_side_b_re_0
                r["top_b_3_ng"] = b_top_ng_0
                r["top_b_3_re"] = b_top_re_0
                r["bottom_b_3_ng"] = b_bottom_ng_0
                r["bottom_b_3_re"] = b_bottom_re_0
                r["side_b_3_ng"] = b_side_ng_0
                r["side_b_3_re"] = b_side_re_0

            elif period_span["prod_period_0"]  == period_span["cur_period_4"]:
                r["combined_a_ng_4"] = combined_side_a_ng_0
                r["combined_a_re_4"] = combined_side_a_re_0
                r["top_a_4_ng"] = a_top_ng_0
                r["top_a_4_re"] = a_top_re_0
                r["bottom_a_4_ng"] = a_bottom_ng_0
                r["bottom_a_4_re"] = a_bottom_re_0
                r["side_a_4_ng"] = a_side_ng_0
                r["side_a_4_re"] = a_side_re_0

                r["combined_b_ng_4"] = combined_side_b_ng_0
                r["combined_b_re_4"] = combined_side_b_re_0
                r["top_b_4_ng"] = b_top_ng_0
                r["top_b_4_re"] = b_top_re_0
                r["bottom_b_4_ng"] = b_bottom_ng_0
                r["bottom_b_4_re"] = b_bottom_re_0
                r["side_b_4_ng"] = b_side_ng_0
                r["side_b_4_re"] = b_side_re_0

            elif period_span["prod_period_0"]  == period_span["cur_period_5"]:
                r["combined_a_ng_5"] = combined_side_a_ng_0
                r["combined_a_re_5"] = combined_side_a_re_0
                r["top_a_5_ng"] = a_top_ng_0
                r["top_a_5_re"] = a_top_re_0
                r["bottom_a_5_ng"] = a_bottom_ng_0
                r["bottom_a_5_re"] = a_bottom_re_0
                r["side_a_5_ng"] = a_side_ng_0
                r["side_a_5_re"] = a_side_re_0

                r["combined_b_ng_5"] = combined_side_b_ng_0
                r["combined_b_re_5"] = combined_side_b_re_0
                r["top_b_5_ng"] = b_top_ng_0
                r["top_b_5_re"] = b_top_re_0
                r["bottom_b_5_ng"] = b_bottom_ng_0
                r["bottom_b_5_re"] = b_bottom_re_0
                r["side_b_5_ng"] = b_side_ng_0
                r["side_b_5_re"] = b_side_re_0

            elif period_span["prod_period_0"]  == period_span["cur_period_6"]:
                r["combined_a_ng_6"] = combined_side_a_ng_0
                r["combined_a_re_6"] = combined_side_a_re_0
                r["top_a_6_ng"] = a_top_ng_0
                r["top_a_6_re"] = a_top_re_0
                r["bottom_a_6_ng"] = a_bottom_ng_0
                r["bottom_a_6_re"] = a_bottom_re_0
                r["side_a_6_ng"] = a_side_ng_0
                r["side_a_6_re"] = a_side_re_0

                r["combined_b_ng_6"] = combined_side_b_ng_0
                r["combined_b_re_6"] = combined_side_b_re_0
                r["top_b_6_ng"] = b_top_ng_0
                r["top_b_6_re"] = b_top_re_0
                r["bottom_b_6_ng"] = b_bottom_ng_0
                r["bottom_b_6_re"] = b_bottom_re_0
                r["side_b_6_ng"] = b_side_ng_0
                r["side_b_6_re"] = b_side_re_0


        elif for_count == 2:
            if period_span["prod_period_1"]  == period_span["cur_period_1"]:
                r["combined_a_ng_1"] = combined_side_a_ng_1
                r["combined_a_re_1"] = combined_side_a_re_1
                r["top_a_1_ng"] = a_top_ng_1
                r["top_a_1_re"] = a_top_re_1
                r["bottom_a_1_ng"] = a_bottom_ng_1
                r["bottom_a_1_re"] = a_bottom_re_1
                r["side_a_1_ng"] = a_side_ng_1
                r["side_a_1_re"] = a_side_re_1

                r["combined_b_ng_1"] = combined_side_b_ng_1
                r["combined_b_re_1"] = combined_side_b_re_1
                r["top_b_1_ng"] = b_top_ng_1
                r["top_b_1_re"] = b_top_re_1
                r["bottom_b_1_ng"] = b_bottom_ng_1
                r["bottom_b_1_re"] = b_bottom_re_1
                r["side_b_1_ng"] = b_side_ng_1
                r["side_b_1_re"] = b_side_re_1

            elif period_span["prod_period_1"]  == period_span["cur_period_2"]:
                r["combined_a_ng_2"] = combined_side_a_ng_1
                r["combined_a_re_2"] = combined_side_a_re_1
                r["top_a_2_ng"] = a_top_ng_1
                r["top_a_2_re"] = a_top_re_1
                r["bottom_a_2_ng"] = a_bottom_ng_1
                r["bottom_a_2_re"] = a_bottom_re_1
                r["side_a_2_ng"] = a_side_ng_1
                r["side_a_2_re"] = a_side_re_1

                r["combined_b_ng_2"] = combined_side_b_ng_1
                r["combined_b_re_2"] = combined_side_b_re_1
                r["top_b_2_ng"] = b_top_ng_1
                r["top_b_2_re"] = b_top_re_1
                r["bottom_b_2_ng"] = b_bottom_ng_1
                r["bottom_b_2_re"] = b_bottom_re_1
                r["side_b_2_ng"] = b_side_ng_1
                r["side_b_2_re"] = b_side_re_1

            elif period_span["prod_period_1"]  == period_span["cur_period_3"]:
                r["combined_a_ng_3"] = combined_side_a_ng_1
                r["combined_a_re_3"] = combined_side_a_re_1
                r["top_a_3_ng"] = a_top_ng_1
                r["top_a_3_re"] = a_top_re_1
                r["bottom_a_3_ng"] = a_bottom_ng_1
                r["bottom_a_3_re"] = a_bottom_re_1
                r["side_a_3_ng"] = a_side_ng_1
                r["side_a_3_re"] = a_side_re_1

                r["combined_b_ng_3"] = combined_side_b_ng_1
                r["combined_b_re_3"] = combined_side_b_re_1
                r["top_b_3_ng"] = b_top_ng_1
                r["top_b_3_re"] = b_top_re_1
                r["bottom_b_3_ng"] = b_bottom_ng_1
                r["bottom_b_3_re"] = b_bottom_re_1
                r["side_b_3_ng"] = b_side_ng_1
                r["side_b_3_re"] = b_side_re_1

            elif period_span["prod_period_1"]  == period_span["cur_period_4"]:
                r["combined_a_ng_4"] = combined_side_a_ng_1
                r["combined_a_re_4"] = combined_side_a_re_1
                r["top_a_4_ng"] = a_top_ng_1
                r["top_a_4_re"] = a_top_re_1
                r["bottom_a_4_ng"] = a_bottom_ng_1
                r["bottom_a_4_re"] = a_bottom_re_1
                r["side_a_4_ng"] = a_side_ng_1
                r["side_a_4_re"] = a_side_re_1

                r["combined_b_ng_4"] = combined_side_b_ng_1
                r["combined_b_re_4"] = combined_side_b_re_1
                r["top_b_4_ng"] = b_top_ng_1
                r["top_b_4_re"] = b_top_re_1
                r["bottom_b_4_ng"] = b_bottom_ng_1
                r["bottom_b_4_re"] = b_bottom_re_1
                r["side_b_4_ng"] = b_side_ng_1
                r["side_b_4_re"] = b_side_re_1

            elif period_span["prod_period_1"]  == period_span["cur_period_5"]:
                r["combined_a_ng_5"] = combined_side_a_ng_1
                r["combined_a_re_5"] = combined_side_a_re_1
                r["top_a_5_ng"] = a_top_ng_1
                r["top_a_5_re"] = a_top_re_1
                r["bottom_a_5_ng"] = a_bottom_ng_1
                r["bottom_a_5_re"] = a_bottom_re_1
                r["side_a_5_ng"] = a_side_ng_1
                r["side_a_5_re"] = a_side_re_1

                r["combined_b_ng_5"] = combined_side_b_ng_1
                r["combined_b_re_5"] = combined_side_b_re_1
                r["top_b_5_ng"] = b_top_ng_1
                r["top_b_5_re"] = b_top_re_1
                r["bottom_b_5_ng"] = b_bottom_ng_1
                r["bottom_b_5_re"] = b_bottom_re_1
                r["side_b_5_ng"] = b_side_ng_1
                r["side_b_5_re"] = b_side_re_1

            elif period_span["prod_period_1"]  == period_span["cur_period_6"]:
                r["combined_a_ng_6"] = combined_side_a_ng_1
                r["combined_a_re_6"] = combined_side_a_re_1
                r["top_a_6_ng"] = a_top_ng_1
                r["top_a_6_re"] = a_top_re_1
                r["bottom_a_6_ng"] = a_bottom_ng_1
                r["bottom_a_6_re"] = a_bottom_re_1
                r["side_a_6_ng"] = a_side_ng_1
                r["side_a_6_re"] = a_side_re_1

                r["combined_b_ng_6"] = combined_side_b_ng_1
                r["combined_b_re_6"] = combined_side_b_re_1
                r["top_b_6_ng"] = b_top_ng_1
                r["top_b_6_re"] = b_top_re_1
                r["bottom_b_6_ng"] = b_bottom_ng_1
                r["bottom_b_6_re"] = b_bottom_re_1
                r["side_b_6_ng"] = b_side_ng_1
                r["side_b_6_re"] = b_side_re_1


        elif for_count == 3:
            if period_span["prod_period_2"]  == period_span["cur_period_2"]:
                r["combined_a_ng_2"] = combined_side_a_ng_2
                r["combined_a_re_2"] = combined_side_a_re_2
                r["top_a_2_ng"] = a_top_ng_2
                r["top_a_2_re"] = a_top_re_2
                r["bottom_a_2_ng"] = a_bottom_ng_2
                r["bottom_a_2_re"] = a_bottom_re_2
                r["side_a_2_ng"] = a_side_ng_2
                r["side_a_2_re"] = a_side_re_2

                r["combined_b_ng_2"] = combined_side_b_ng_2
                r["combined_b_re_2"] = combined_side_b_re_2
                r["top_b_2_ng"] = b_top_ng_2
                r["top_b_2_re"] = b_top_re_2
                r["bottom_b_2_ng"] = b_bottom_ng_2
                r["bottom_b_2_re"] = b_bottom_re_2
                r["side_b_2_ng"] = b_side_ng_2
                r["side_b_2_re"] = b_side_re_2

            elif period_span["prod_period_2"]  ==period_span["cur_period_3"]:
                r["combined_a_ng_3"] = combined_side_a_ng_2
                r["combined_a_re_3"] = combined_side_a_re_2
                r["top_a_3_ng"] = a_top_ng_2
                r["top_a_3_re"] = a_top_re_2
                r["bottom_a_3_ng"] = a_bottom_ng_2
                r["bottom_a_3_re"] = a_bottom_re_2
                r["side_a_3_ng"] = a_side_ng_2
                r["side_a_3_re"] = a_side_re_2

                r["combined_b_ng_3"] = combined_side_b_ng_2
                r["combined_b_re_3"] = combined_side_b_re_2
                r["top_b_3_ng"] = b_top_ng_2
                r["top_b_3_re"] = b_top_re_2
                r["bottom_b_3_ng"] = b_bottom_ng_2
                r["bottom_b_3_re"] = b_bottom_re_2
                r["side_b_3_ng"] = b_side_ng_2
                r["side_b_3_re"] = b_side_re_2

            elif period_span["prod_period_2"]  == period_span["cur_period_4"]:
                r["combined_a_ng_4"] = combined_side_a_ng_2
                r["combined_a_re_4"] = combined_side_a_re_2
                r["top_a_4_ng"] = a_top_ng_2
                r["top_a_4_re"] = a_top_re_2
                r["bottom_a_4_ng"] = a_bottom_ng_2
                r["bottom_a_4_re"] = a_bottom_re_2
                r["side_a_4_ng"] = a_side_ng_2
                r["side_a_4_re"] = a_side_re_2

                r["combined_b_ng_4"] = combined_side_b_ng_2
                r["combined_b_re_4"] = combined_side_b_re_2
                r["top_b_4_ng"] = b_top_ng_2
                r["top_b_4_re"] = b_top_re_2
                r["bottom_b_4_ng"] = b_bottom_ng_2
                r["bottom_b_4_re"] = b_bottom_re_2
                r["side_b_4_ng"] = b_side_ng_2
                r["side_b_4_re"] = b_side_re_2

            elif period_span["prod_period_2"]  == period_span["cur_period_5"]:
                r["combined_a_ng_5"] = combined_side_a_ng_2
                r["combined_a_re_5"] = combined_side_a_re_2
                r["top_a_5_ng"] = a_top_ng_2
                r["top_a_5_re"] = a_top_re_2
                r["bottom_a_5_ng"] = a_bottom_ng_2
                r["bottom_a_5_re"] = a_bottom_re_2
                r["side_a_5_ng"] = a_side_ng_2
                r["side_a_5_re"] = a_side_re_2

                r["combined_b_ng_5"] = combined_side_b_ng_2
                r["combined_b_re_5"] = combined_side_b_re_2
                r["top_b_5_ng"] = b_top_ng_2
                r["top_b_5_re"] = b_top_re_2
                r["bottom_b_5_ng"] = b_bottom_ng_2
                r["bottom_b_5_re"] = b_bottom_re_2
                r["side_b_5_ng"] = b_side_ng_2
                r["side_b_5_re"] = b_side_re_2

            elif period_span["prod_period_2"]  == period_span["cur_period_6"]:
                r["combined_a_ng_6"] = combined_side_a_ng_2
                r["combined_a_re_6"] = combined_side_a_re_2
                r["top_a_6_ng"] = a_top_ng_2
                r["top_a_6_re"] = a_top_re_2
                r["bottom_a_6_ng"] = a_bottom_ng_2
                r["bottom_a_6_re"] = a_bottom_re_2
                r["side_a_6_ng"] = a_side_ng_2
                r["side_a_6_re"] = a_side_re_2

                r["combined_b_ng_6"] = combined_side_b_ng_2
                r["combined_b_re_6"] = combined_side_b_re_2
                r["top_b_6_ng"] = b_top_ng_2
                r["top_b_6_re"] = b_top_re_2
                r["bottom_b_6_ng"] = b_bottom_ng_2
                r["bottom_b_6_re"] = b_bottom_re_2
                r["side_b_6_ng"] = b_side_ng_2
                r["side_b_6_re"] = b_side_re_2


        elif for_count == 4:
            if period_span["prod_period_3"]  == period_span["cur_period_3"]:
                r["combined_a_ng_3"] = combined_side_a_ng_3
                r["combined_a_re_3"] = combined_side_a_re_3
                r["top_a_3_ng"] = a_top_ng_3
                r["top_a_3_re"] = a_top_re_3
                r["bottom_a_3_ng"] = a_bottom_ng_3
                r["bottom_a_3_re"] = a_bottom_re_3
                r["side_a_3_ng"] = a_side_ng_3
                r["side_a_3_re"] = a_side_re_3

                r["combined_b_ng_3"] = combined_side_b_ng_3
                r["combined_b_re_3"] = combined_side_b_re_3
                r["top_b_3_ng"] = b_top_ng_3
                r["top_b_3_re"] = b_top_re_3
                r["bottom_b_3_ng"] = b_bottom_ng_3
                r["bottom_b_3_re"] = b_bottom_re_3
                r["side_b_3_ng"] = b_side_ng_3
                r["side_b_3_re"] = b_side_re_3

            elif period_span["prod_period_3"]  == period_span["cur_period_4"]:
                r["combined_a_ng_4"] = combined_side_a_ng_3
                r["combined_a_re_4"] = combined_side_a_re_3
                r["top_a_4_ng"] = a_top_ng_3
                r["top_a_4_re"] = a_top_re_3
                r["bottom_a_4_ng"] = a_bottom_ng_3
                r["bottom_a_4_re"] = a_bottom_re_3
                r["side_a_4_ng"] = a_side_ng_3
                r["side_a_4_re"] = a_side_re_3

                r["combined_b_ng_4"] = combined_side_b_ng_3
                r["combined_b_re_4"] = combined_side_b_re_3
                r["top_b_4_ng"] = b_top_ng_3
                r["top_b_4_re"] = b_top_re_3
                r["bottom_b_4_ng"] = b_bottom_ng_3
                r["bottom_b_4_re"] = b_bottom_re_3
                r["side_b_4_ng"] = b_side_ng_3
                r["side_b_4_re"] = b_side_re_3

            elif period_span["prod_period_3"]  == period_span["cur_period_5"]:
                r["combined_a_ng_5"] = combined_side_a_ng_3
                r["combined_a_re_5"] = combined_side_a_re_3
                r["top_a_5_ng"] = a_top_ng_3
                r["top_a_5_re"] = a_top_re_3
                r["bottom_a_5_ng"] = a_bottom_ng_3
                r["bottom_a_5_re"] = a_bottom_re_3
                r["side_a_5_ng"] = a_side_ng_3
                r["side_a_5_re"] = a_side_re_3

                r["combined_b_ng_5"] = combined_side_b_ng_3
                r["combined_b_re_5"] = combined_side_b_re_3
                r["top_b_5_ng"] = b_top_ng_3
                r["top_b_5_re"] = b_top_re_3
                r["bottom_b_5_ng"] = b_bottom_ng_3
                r["bottom_b_5_re"] = b_bottom_re_3
                r["side_b_5_ng"] = b_side_ng_3
                r["side_b_5_re"] = b_side_re_3

            elif period_span["prod_period_3"]  == period_span["cur_period_6"]:
                r["combined_a_ng_6"] = combined_side_a_ng_3
                r["combined_a_re_6"] = combined_side_a_re_3
                r["top_a_6_ng"] = a_top_ng_3
                r["top_a_6_re"] = a_top_re_3
                r["bottom_a_6_ng"] = a_bottom_ng_3
                r["bottom_a_6_re"] = a_bottom_re_3
                r["side_a_6_ng"] = a_side_ng_3
                r["side_a_6_re"] = a_side_re_3

                r["combined_b_ng_6"] = combined_side_b_ng_3
                r["combined_b_re_6"] = combined_side_b_re_3
                r["top_b_6_ng"] = b_top_ng_3
                r["top_b_6_re"] = b_top_re_3
                r["bottom_b_6_ng"] = b_bottom_ng_3
                r["bottom_b_6_re"] = b_bottom_re_3
                r["side_b_6_ng"] = b_side_ng_3
                r["side_b_6_re"] = b_side_re_3


        elif for_count == 5:
            if period_span["prod_period_4"]  == period_span["cur_period_4"]:
                r["combined_a_ng_4"] = combined_side_a_ng_4
                r["combined_a_re_4"] = combined_side_a_re_4
                r["top_a_4_ng"] = a_top_ng_4
                r["top_a_4_re"] = a_top_re_4
                r["bottom_a_4_ng"] = a_bottom_ng_4
                r["bottom_a_4_re"] = a_bottom_re_4
                r["side_a_4_ng"] = a_side_ng_4
                r["side_a_4_re"] = a_side_re_4

                r["combined_b_ng_4"] = combined_side_b_ng_4
                r["combined_b_re_4"] = combined_side_b_re_4
                r["top_b_4_ng"] = b_top_ng_4
                r["top_b_4_re"] = b_top_re_4
                r["bottom_b_4_ng"] = b_bottom_ng_4
                r["bottom_b_4_re"] = b_bottom_re_4
                r["side_b_4_ng"] = b_side_ng_4
                r["side_b_4_re"] = b_side_re_4

            elif period_span["prod_period_4"]  == period_span["cur_period_5"]:
                r["combined_a_ng_5"] = combined_side_a_ng_4
                r["combined_a_re_5"] = combined_side_a_re_4
                r["top_a_5_ng"] = a_top_ng_4
                r["top_a_5_re"] = a_top_re_4
                r["bottom_a_5_ng"] = a_bottom_ng_4
                r["bottom_a_5_re"] = a_bottom_re_4
                r["side_a_5_ng"] = a_side_ng_4
                r["side_a_5_re"] = a_side_re_4

                r["combined_b_ng_5"] = combined_side_b_ng_4
                r["combined_b_re_5"] = combined_side_b_re_4
                r["top_b_5_ng"] = b_top_ng_4
                r["top_b_5_re"] = b_top_re_4
                r["bottom_b_5_ng"] = b_bottom_ng_4
                r["bottom_b_5_re"] = b_bottom_re_4
                r["side_b_5_ng"] = b_side_ng_4
                r["side_b_5_re"] = b_side_re_4

            elif period_span["prod_period_4"]  == period_span["cur_period_6"]:
                r["combined_a_ng_6"] = combined_side_a_ng_4
                r["combined_a_re_6"] = combined_side_a_re_4
                r["top_a_6_ng"] = a_top_ng_4
                r["top_a_6_re"] = a_top_re_4
                r["bottom_a_6_ng"] = a_bottom_ng_4
                r["bottom_a_6_re"] = a_bottom_re_4
                r["side_a_6_ng"] = a_side_ng_4
                r["side_a_6_re"] = a_side_re_4

                r["combined_b_ng_6"] = combined_side_b_ng_4
                r["combined_b_re_6"] = combined_side_b_re_4
                r["top_b_6_ng"] = b_top_ng_4
                r["top_b_6_re"] = b_top_re_4
                r["bottom_b_6_ng"] = b_bottom_ng_4
                r["bottom_b_6_re"] = b_bottom_re_4
                r["side_b_6_ng"] = b_side_ng_4
                r["side_b_6_re"] = b_side_re_4


        elif for_count == 6:
            if period_span["prod_period_5"]  == period_span["cur_period_5"]:
                r["combined_a_ng_5"] = combined_side_a_ng_5
                r["combined_a_re_5"] = combined_side_a_re_5
                r["top_a_5_ng"] = a_top_ng_5
                r["top_a_5_re"] = a_top_re_5
                r["bottom_a_5_ng"] = a_bottom_ng_5
                r["bottom_a_5_re"] = a_bottom_re_5
                r["side_a_5_ng"] = a_side_ng_5
                r["side_a_5_re"] = a_side_re_5

                r["combined_b_ng_5"] = combined_side_b_ng_5
                r["combined_b_re_5"] = combined_side_b_re_5
                r["top_b_5_ng"] = b_top_ng_5
                r["top_b_5_re"] = b_top_re_5
                r["bottom_b_5_ng"] = b_bottom_ng_5
                r["bottom_b_5_re"] = b_bottom_re_5
                r["side_b_5_ng"] = b_side_ng_5
                r["side_b_5_re"] = b_side_re_5

            elif period_span["prod_period_5"]  == period_span["cur_period_6"]:
                r["combined_a_ng_6"] = combined_side_a_ng_5
                r["combined_a_re_6"] = combined_side_a_re_5
                r["top_a_6_ng"] = a_top_ng_5
                r["top_a_6_re"] = a_top_re_5
                r["bottom_a_6_ng"] = a_bottom_ng_5
                r["bottom_a_6_re"] = a_bottom_re_5
                r["side_a_6_ng"] = a_side_ng_5
                r["side_a_6_re"] = a_side_re_5

                r["combined_b_ng_6"] = combined_side_b_ng_5
                r["combined_b_re_6"] = combined_side_b_re_5
                r["top_b_6_ng"] = b_top_ng_5
                r["top_b_6_re"] = b_top_re_5
                r["bottom_b_6_ng"] = b_bottom_ng_5
                r["bottom_b_6_re"] = b_bottom_re_5
                r["side_b_6_ng"] = b_side_ng_5
                r["side_b_6_re"] = b_side_re_5


        elif for_count == 7:
            if period_span["prod_period_6"]  == period_span["cur_period_6"]:
                r["combined_a_ng_6"] = combined_side_a_ng_6
                r["combined_a_re_6"] = combined_side_a_re_6
                r["top_a_6_ng"] = a_top_ng_6
                r["top_a_6_re"] = a_top_re_6
                r["bottom_a_6_ng"] = a_bottom_ng_6
                r["bottom_a_6_re"] = a_bottom_re_6
                r["side_a_6_ng"] = a_side_ng_6
                r["side_a_6_re"] = a_side_re_6

                r["combined_b_ng_6"] = combined_side_b_ng_6
                r["combined_b_re_6"] = combined_side_b_re_6
                r["top_b_6_ng"] = b_top_ng_6
                r["top_b_6_re"] = b_top_re_6
                r["bottom_b_6_ng"] = b_bottom_ng_6
                r["bottom_b_6_re"] = b_bottom_re_6
                r["side_b_6_ng"] = b_side_ng_6
                r["side_b_6_re"] = b_side_re_6


    return r

def assign_production_values_to_dictionary(values, line, r):

    return {
        "line":line,
        "combined_a_ng_0":r["combined_a_ng_0"],
        "combined_a_ng_1":r["combined_a_ng_1"],
        "combined_a_ng_2":r["combined_a_ng_2"],
        "combined_a_ng_3":r["combined_a_ng_3"],
        "combined_a_ng_4":r["combined_a_ng_4"],
        "combined_a_ng_5":r["combined_a_ng_5"],
        "combined_a_ng_6":r["combined_a_ng_6"],

        "combined_b_ng_0":r["combined_b_ng_0"],
        "combined_b_ng_1":r["combined_b_ng_1"],
        "combined_b_ng_2":r["combined_b_ng_2"],
        "combined_b_ng_3":r["combined_b_ng_3"],
        "combined_b_ng_4":r["combined_b_ng_4"],
        "combined_b_ng_5":r["combined_b_ng_5"],
        "combined_b_ng_6":r["combined_b_ng_6"],

        "combined_a_re_0":r["combined_a_re_0"],
        "combined_a_re_1":r["combined_a_re_1"],
        "combined_a_re_2":r["combined_a_re_2"],
        "combined_a_re_3":r["combined_a_re_3"],
        "combined_a_re_4":r["combined_a_re_4"],
        "combined_a_re_5":r["combined_a_re_5"],
        "combined_a_re_6":r["combined_a_re_6"],

        "combined_b_re_0":r["combined_b_re_0"],
        "combined_b_re_1":r["combined_b_re_1"],
        "combined_b_re_2":r["combined_b_re_2"],
        "combined_b_re_3":r["combined_b_re_3"],
        "combined_b_re_4":r["combined_b_re_4"],
        "combined_b_re_5":r["combined_b_re_5"],
        "combined_b_re_6":r["combined_b_re_6"],

        "top_a_ng_0":r["top_a_0_ng"],
        "top_a_ng_1":r["top_a_1_ng"],
        "top_a_ng_2":r["top_a_2_ng"],
        "top_a_ng_3":r["top_a_3_ng"],
        "top_a_ng_4":r["top_a_4_ng"],
        "top_a_ng_5":r["top_a_5_ng"],
        "top_a_ng_6":r["top_a_6_ng"],

        "top_b_ng_0":r["top_b_0_ng"],
        "top_b_ng_1":r["top_b_1_ng"],
        "top_b_ng_2":r["top_b_2_ng"],
        "top_b_ng_3":r["top_b_3_ng"],
        "top_b_ng_4":r["top_b_4_ng"],
        "top_b_ng_5":r["top_b_5_ng"],
        "top_b_ng_6":r["top_b_6_ng"],

        "top_a_re_0":r["top_a_0_re"],
        "top_a_re_1":r["top_a_1_re"],
        "top_a_re_2":r["top_a_2_re"],
        "top_a_re_3":r["top_a_3_re"],
        "top_a_re_4":r["top_a_4_re"],
        "top_a_re_5":r["top_a_5_re"],
        "top_a_re_6":r["top_a_6_re"],

        "top_b_re_0":r["top_b_0_re"],
        "top_b_re_1":r["top_b_1_re"],
        "top_b_re_2":r["top_b_2_re"],
        "top_b_re_3":r["top_b_3_re"],
        "top_b_re_4":r["top_b_4_re"],
        "top_b_re_5":r["top_b_5_re"],
        "top_b_re_6":r["top_b_6_re"],

        "bottom_a_ng_0":r["bottom_a_0_ng"],
        "bottom_a_ng_1":r["bottom_a_1_ng"],
        "bottom_a_ng_2":r["bottom_a_2_ng"],
        "bottom_a_ng_3":r["bottom_a_3_ng"],
        "bottom_a_ng_4":r["bottom_a_4_ng"],
        "bottom_a_ng_5":r["bottom_a_5_ng"],
        "bottom_a_ng_6":r["bottom_a_6_ng"],

        "bottom_b_ng_0":r["bottom_b_0_ng"],
        "bottom_b_ng_1":r["bottom_b_1_ng"],
        "bottom_b_ng_2":r["bottom_b_2_ng"],
        "bottom_b_ng_3":r["bottom_b_3_ng"],
        "bottom_b_ng_4":r["bottom_b_4_ng"],
        "bottom_b_ng_5":r["bottom_b_5_ng"],
        "bottom_b_ng_6":r["bottom_b_6_ng"],

        "bottom_a_re_0":r["bottom_a_0_re"],
        "bottom_a_re_1":r["bottom_a_1_re"],
        "bottom_a_re_2":r["bottom_a_2_re"],
        "bottom_a_re_3":r["bottom_a_3_re"],
        "bottom_a_re_4":r["bottom_a_4_re"],
        "bottom_a_re_5":r["bottom_a_5_re"],
        "bottom_a_re_6":r["bottom_a_6_re"],

        "bottom_b_re_0":r["bottom_b_0_re"],
        "bottom_b_re_1":r["bottom_b_1_re"],
        "bottom_b_re_2":r["bottom_b_2_re"],
        "bottom_b_re_3":r["bottom_b_3_re"],
        "bottom_b_re_4":r["bottom_b_4_re"],
        "bottom_b_re_5":r["bottom_b_5_re"],
        "bottom_b_re_6":r["bottom_b_6_re"],

        "side_a_ng_0":r["side_a_0_ng"],
        "side_a_ng_1":r["side_a_1_ng"],
        "side_a_ng_2":r["side_a_2_ng"],
        "side_a_ng_3":r["side_a_3_ng"],
        "side_a_ng_4":r["side_a_4_ng"],
        "side_a_ng_5":r["side_a_5_ng"],
        "side_a_ng_6":r["side_a_6_ng"],

        "side_b_ng_0":r["side_b_0_ng"],
        "side_b_ng_1":r["side_b_1_ng"],
        "side_b_ng_2":r["side_b_2_ng"],
        "side_b_ng_3":r["side_b_3_ng"],
        "side_b_ng_4":r["side_b_4_ng"],
        "side_b_ng_5":r["side_b_5_ng"],
        "side_b_ng_6":r["side_b_6_ng"],

        "side_a_re_0":r["side_a_0_re"],
        "side_a_re_1":r["side_a_1_re"],
        "side_a_re_2":r["side_a_2_re"],
        "side_a_re_3":r["side_a_3_re"],
        "side_a_re_4":r["side_a_4_re"],
        "side_a_re_5":r["side_a_5_re"],
        "side_a_re_6":r["side_a_6_re"],

        "side_b_re_0":r["side_b_0_re"],
        "side_b_re_1":r["side_b_1_re"],
        "side_b_re_2":r["side_b_2_re"],
        "side_b_re_3":r["side_b_3_re"],
        "side_b_re_4":r["side_b_4_re"],
        "side_b_re_5":r["side_b_5_re"],
        "side_b_re_6":r["side_b_6_re"]
        }

def past_seven_hours(line):

    # set all valeus of the dictionary to 0
    r = reset_dictionary()

    period_span = period("hourly", line)
    requested_period = hourly_report
    # assign values to the dictionary keys
    set_values_for_dictionary = assign_period_values(r, line, period_span, requested_period)

    return assign_production_values_to_dictionary(set_values_for_dictionary, line, r)

def past_seven_days(line):

    # set all valeus of the dictionary to 0
    r = reset_dictionary()

    period_span = period("daily", line)
    requested_period = daily_report
    # assign values to the dictionary keys
    set_values_for_dictionary = assign_period_values(r, line, period_span, requested_period)

    return assign_production_values_to_dictionary(set_values_for_dictionary, line, r)

def past_seven_weeks(line):

    # set all valeus of the dictionary to 0
    r = reset_dictionary()

    period_span = period("weekly", line)
    requested_period = weekly_report
    # assign values to the dictionary keys
    set_values_for_dictionary = assign_period_values(r, line, period_span, requested_period)

    return assign_production_values_to_dictionary(set_values_for_dictionary, line, r)

def past_seven_months(line):

    # set all valeus of the dictionary to 0
    r = reset_dictionary()


    period_span = period("monthly", line)
    requested_period = monthly_report

    # assign values to the dictionary keys
    set_values_for_dictionary = assign_period_values(r, line, period_span, requested_period)

    return assign_production_values_to_dictionary(set_values_for_dictionary, line, r)
