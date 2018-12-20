from dolcegusto.models import daily_report, hourly_report, weekly_report, monthly_report
from datetime import datetime, date, timedelta
import datetime

def reset_dictionaries():
    # set all values to zero to avoid data contamination from previous requests
    top_cam = {
    "a_0":0, "a_1":0, "a_2":0, "a_3":0, "a_4":0, "a_5":0, "a_6":0,
    "b_0":0, "b_1":0, "b_2":0, "b_3":0, "b_4":0, "b_5":0, "b_6":0
    }

    bottom_cam = {
    "a_0":0, "a_1":0, "a_2":0, "a_3":0, "a_4":0, "a_5":0, "a_6":0,
    "b_0":0, "b_1":0, "b_2":0, "b_3":0, "b_4":0, "b_5":0, "b_6":0
    }

    side_cam = {
    "a_0":0, "a_1":0, "a_2":0, "a_3":0, "a_4":0, "a_5":0, "a_6":0,
    "b_0":0, "b_1":0, "b_2":0, "b_3":0, "b_4":0, "b_5":0, "b_6":0
    }

    side_a = {
    "ng_0":0, "ng_1":0, "ng_2":0, "ng_3":0, "ng_4":0, "ng_5":0, "ng_6":0,
    "re_0":0, "re_1":0, "re_2":0, "re_3":0, "re_4":0, "re_5":0, "re_6":0
    }

    side_b = {
    "ng_0":0, "ng_1":0, "ng_2":0, "ng_3":0, "ng_4":0, "ng_5":0, "ng_6":0,
    "re_0":0, "re_1":0, "re_2":0, "re_3":0, "re_4":0, "re_5":0, "re_6":0
    }

    return top_cam, bottom_cam, side_cam, side_a, side_b

def past_seven_hours(line):

    # set all values to zero
    side_a = {
    "ng_0":0, "ng_1":0, "ng_2":0, "ng_3":0, "ng_4":0, "ng_5":0, "ng_6":0,
    "re_0":0, "re_1":0, "re_2":0, "re_3":0, "re_4":0, "re_5":0, "re_6":0
    }

    side_b = {
    "ng_0":0, "ng_1":0, "ng_2":0, "ng_3":0, "ng_4":0, "ng_5":0, "ng_6":0,
    "re_0":0, "re_1":0, "re_2":0, "re_3":0, "re_4":0, "re_5":0, "re_6":0
    }


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

def past_seven_weeks(line):

    side_a = {
    "ng_0":0, "ng_1":0, "ng_2":0, "ng_3":0, "ng_4":0, "ng_5":0, "ng_6":0,
    "re_0":0, "re_1":0, "re_2":0, "re_3":0, "re_4":0, "re_5":0, "re_6":0
    }

    side_b = {
    "ng_0":0, "ng_1":0, "ng_2":0, "ng_3":0, "ng_4":0, "ng_5":0, "ng_6":0,
    "re_0":0, "re_1":0, "re_2":0, "re_3":0, "re_4":0, "re_5":0, "re_6":0
    }

    # resets all values of relevant dictionaries to 0
    reset_dictionaries()

    # Return a 3-tuple, (ISO year, ISO week number, ISO weekday)
    week_number_0 = (date.isocalendar(weekly_report(line).production_week[0]))[1]
    week_number_1 = (date.isocalendar(weekly_report(line).production_week[1]))[1]
    week_number_2 = (date.isocalendar(weekly_report(line).production_week[2]))[1]
    week_number_3 = (date.isocalendar(weekly_report(line).production_week[3]))[1]
    week_number_4 = (date.isocalendar(weekly_report(line).production_week[4]))[1]
    week_number_5 = (date.isocalendar(weekly_report(line).production_week[5]))[1]
    week_number_6 = (date.isocalendar(weekly_report(line).production_week[6]))[1]

    this_week = date.isocalendar((datetime.datetime.now()))[1]
    one_week_ago = (date.isocalendar((datetime.datetime.now()))[1])-1
    two_weeks_ago = (date.isocalendar((datetime.datetime.now()))[1])-2
    three_weeks_ago = (date.isocalendar((datetime.datetime.now()))[1])-3
    four_weeks_ago = (date.isocalendar((datetime.datetime.now()))[1])-4
    five_weeks_ago = (date.isocalendar((datetime.datetime.now()))[1])-5
    six_weeks_ago = (date.isocalendar((datetime.datetime.now()))[1])-6

    # assign variables from specific columns from database based on date
    for_count = 0
    for i in weekly_report(line).combined_side_a_ng:
        for_count += 1
        if for_count == 1:
            if week_number_0 == this_week:
                side_a["ng_0"] = i
            elif week_number_0 == one_week_ago:
                side_a["ng_1"] = i
            elif week_number_0 == two_weeks_ago:
                side_a["ng_2"] = i
            elif week_number_0 ==three_weeks_ago:
                side_a["ng_3"] = i
            elif week_number_0 == four_weeks_ago:
                side_a["ng_4"] = i
            elif week_number_0 == five_weeks_ago:
                side_a["ng_5"] = i
            elif week_number_0 == six_weeks_ago:
                side_a["ng_6"] = i


        elif for_count == 2:
            if week_number_1 == one_week_ago:
                side_a["ng_1"] = i
            elif week_number_1 == two_weeks_ago:
                side_a["ng_2"] = i
            elif week_number_1 ==three_weeks_ago:
                side_a["ng_3"] = i
            elif week_number_1 == four_weeks_ago:
                side_a["ng_4"] = i
            elif week_number_1 == five_weeks_ago:
                side_a["ng_5"] = i
            elif week_number_1 == six_weeks_ago:
                side_a["ng_6"] = i

        elif for_count == 3:
            if week_number_2 == two_weeks_ago:
                side_a["ng_2"] = i
            elif week_number_2 ==three_weeks_ago:
                side_a["ng_3"] = i
            elif week_number_2 == four_weeks_ago:
                side_a["ng_4"] = i
            elif week_number_2 == five_weeks_ago:
                side_a["ng_5"] = i
            elif week_number_2 == six_weeks_ago:
                side_a["ng_6"] = i

        elif for_count == 4:
            if week_number_3 ==three_weeks_ago:
                side_a["ng_3"] = i
            elif week_number_3 == four_weeks_ago:
                side_a["ng_4"] = i
            elif week_number_3 == five_weeks_ago:
                side_a["ng_5"] = i
            elif week_number_3 == six_weeks_ago:
                side_a["ng_6"] = i

        elif for_count == 5:
            if week_number_4 == four_weeks_ago:
                side_a["ng_4"] = i
            elif week_number_4 == five_weeks_ago:
                side_a["ng_5"] = i
            elif week_number_4 == six_weeks_ago:
                side_a["ng_6"] = i

        elif for_count == 6:
            if week_number_5 == five_weeks_ago:
                side_a["ng_5"] = i
            elif week_number_5 == six_weeks_ago:
                side_a["ng_6"] = i

        elif for_count == 7:
            if week_number_6 == six_weeks_ago:
                side_a["ng_6"] = i

    # assign variables from specific columns from database based on date
    for_count = 0
    for e in weekly_report(line).combined_side_b_ng:
        for_count += 1
        if for_count == 1:
            if week_number_0 == this_week:
                side_b["ng_0"] = e
            elif week_number_0 == one_week_ago:
                side_b["ng_1"] = e
            elif week_number_0 == two_weeks_ago:
                side_b["ng_2"] = e
            elif week_number_0 ==three_weeks_ago:
                side_b["ng_3"] = e
            elif week_number_0 == four_weeks_ago:
                side_b["ng_4"] = e
            elif week_number_0 == five_weeks_ago:
                side_b["ng_5"] = e
            elif week_number_0 == six_weeks_ago:
                side_b["ng_6"] = e

        elif for_count == 2:
            if week_number_1 == one_week_ago:
                side_b["ng_1"] = e
            elif week_number_1 == two_weeks_ago:
                side_b["ng_2"] = e
            elif week_number_1 ==three_weeks_ago:
                side_b["ng_3"] = e
            elif week_number_1 == four_weeks_ago:
                side_b["ng_4"] = e
            elif week_number_1 == five_weeks_ago:
                side_b["ng_5"] = e
            elif week_number_1 == six_weeks_ago:
                side_b["ng_6"] = e

        elif for_count == 3:
            if week_number_2 == two_weeks_ago:
                side_b["ng_2"] = e
            elif week_number_2 ==three_weeks_ago:
                side_b["ng_3"] = e
            elif week_number_2 == four_weeks_ago:
                side_b["ng_4"] = e
            elif week_number_2 == five_weeks_ago:
                side_b["ng_5"] = e
            elif week_number_2 == six_weeks_ago:
                side_b["ng_6"] = e

        elif for_count == 4:
            if week_number_3 ==three_weeks_ago:
                side_b["ng_3"] = e
            elif week_number_3 == four_weeks_ago:
                side_b["ng_4"] = e
            elif week_number_3 == five_weeks_ago:
                side_b["ng_5"] = e
            elif week_number_3 == six_weeks_ago:
                side_b["ng_6"] = e

        elif for_count == 5:
            if week_number_4 == four_weeks_ago:
                side_b["ng_4"] = e
            elif week_number_4 == five_weeks_ago:
                side_b["ng_5"] = e
            elif week_number_4 == six_weeks_ago:
                side_b["ng_6"] = e

        elif for_count == 6:
            if week_number_5 == five_weeks_ago:
                side_b["ng_5"] = e
            elif week_number_5 == six_weeks_ago:
                side_b["ng_6"] = e

        elif for_count == 7:
            if week_number_6 == six_weeks_ago:
                side_b["ng_6"] = e

    for_count = 0
    for a in weekly_report(line).combined_side_a_re:
        for_count += 1
        if for_count == 1:
            if week_number_0 == this_week:
                side_a["re_0"] = a
            elif week_number_0 == one_week_ago:
                side_a["re_1"] = a
            elif week_number_0 == two_weeks_ago:
                side_a["re_2"] = a
            elif week_number_0 ==three_weeks_ago:
                side_a["re_3"] = a
            elif week_number_0 == four_weeks_ago:
                side_a["re_4"] = a
            elif week_number_0 == five_weeks_ago:
                side_a["re_5"] = a
            elif week_number_0 == six_weeks_ago:
                side_a["re_6"] = a


        elif for_count == 2:
            if week_number_1 == one_week_ago:
                side_a["re_1"] = a
            elif week_number_1 == two_weeks_ago:
                side_a["re_2"] = a
            elif week_number_1 ==three_weeks_ago:
                side_a["re_3"] = a
            elif week_number_1 == four_weeks_ago:
                side_a["re_4"] = a
            elif week_number_1 == five_weeks_ago:
                side_a["re_5"] = a
            elif week_number_1 == six_weeks_ago:
                side_a["re_6"] = a

        elif for_count == 3:
            if week_number_2 == two_weeks_ago:
                side_a["re_2"] = a
            elif week_number_2 ==three_weeks_ago:
                side_a["re_3"] = a
            elif week_number_2 == four_weeks_ago:
                side_a["re_4"] = a
            elif week_number_2 == five_weeks_ago:
                side_a["re_5"] = a
            elif week_number_2 == six_weeks_ago:
                side_a["re_6"] = a

        elif for_count == 4:
            if week_number_3 ==three_weeks_ago:
                side_a["re_3"] = a
            elif week_number_3 == four_weeks_ago:
                side_a["re_4"] = a
            elif week_number_3 == five_weeks_ago:
                side_a["re_5"] = a
            elif week_number_3 == six_weeks_ago:
                side_a["re_6"] = a

        elif for_count == 5:
            if week_number_4 == four_weeks_ago:
                side_a["re_4"] = a
            elif week_number_4 == five_weeks_ago:
                side_a["re_5"] = a
            elif week_number_4 == six_weeks_ago:
                side_a["re_6"] = a

        elif for_count == 6:
            if week_number_5 == five_weeks_ago:
                side_a["re_5"] = a
            elif week_number_5 == six_weeks_ago:
                side_a["re_6"] = a

        elif for_count == 7:
            if week_number_6 == six_weeks_ago:
                side_a["re_6"] = a
    # assign variables from specific columns from database based on date
    for_count = 0
    for u in weekly_report(line).combined_side_b_re:
        for_count += 1
        if for_count == 1:
            if week_number_0 == this_week:
                side_b["re_0"] = u
            elif week_number_0 == one_week_ago:
                side_b["re_1"] = u
            elif week_number_0 == two_weeks_ago:
                side_b["re_2"] = u
            elif week_number_0 ==three_weeks_ago:
                side_b["re_3"] = u
            elif week_number_0 == four_weeks_ago:
                side_b["re_4"] = u
            elif week_number_0 == five_weeks_ago:
                side_b["re_5"] = u
            elif week_number_0 == six_weeks_ago:
                side_b["re_6"] = u

        elif for_count == 2:
            if week_number_1 == one_week_ago:
                side_b["re_1"] = u
            elif week_number_1 == two_weeks_ago:
                side_b["re_2"] = u
            elif week_number_1 ==three_weeks_ago:
                side_b["re_3"] = u
            elif week_number_1 == four_weeks_ago:
                side_b["re_4"] = u
            elif week_number_1 == five_weeks_ago:
                side_b["re_5"] = u
            elif week_number_1 == six_weeks_ago:
                side_b["re_6"] = u

        elif for_count == 3:
            if week_number_2 == two_weeks_ago:
                side_b["re_2"] = u
            elif week_number_2 ==three_weeks_ago:
                side_b["re_3"] = u
            elif week_number_2 == four_weeks_ago:
                side_b["re_4"] = u
            elif week_number_2 == five_weeks_ago:
                side_b["re_5"] = u
            elif week_number_2 == six_weeks_ago:
                side_b["re_6"] = u

        elif for_count == 4:
            if week_number_3 ==three_weeks_ago:
                side_b["re_3"] = u
            elif week_number_3 == four_weeks_ago:
                side_b["re_4"] = u
            elif week_number_3 == five_weeks_ago:
                side_b["re_5"] = u
            elif week_number_3 == six_weeks_ago:
                side_b["re_6"] = u

        elif for_count == 5:
            if week_number_4 == four_weeks_ago:
                side_b["re_4"] = u
            elif week_number_4 == five_weeks_ago:
                side_b["re_5"] = u
            elif week_number_4 == six_weeks_ago:
                side_b["re_6"] = u

        elif for_count == 6:
            if week_number_5 == five_weeks_ago:
                side_b["re_5"] = u
            elif week_number_5 == six_weeks_ago:
                side_b["re_6"] = u

        elif for_count == 7:
            if week_number_6 == six_weeks_ago:
                side_b["re_6"] = u

    return {
    "line":line,
    "line0_a_ng":side_a["ng_0"],
    "line1_a_ng":side_a["ng_1"],
    "line2_a_ng":side_a["ng_2"],
    "line3_a_ng":side_a["ng_3"],
    "line4_a_ng":side_a["ng_4"],
    "line5_a_ng":side_a["ng_5"],
    "line6_a_ng":side_a["ng_6"],

    "line0_b_ng":side_b["ng_0"],
    "line1_b_ng":side_b["ng_1"],
    "line2_b_ng":side_b["ng_2"],
    "line3_b_ng":side_b["ng_3"],
    "line4_b_ng":side_b["ng_4"],
    "line5_b_ng":side_b["ng_5"],
    "line6_b_ng":side_b["ng_6"],

    "line0_a_re":side_a["re_0"],
    "line1_a_re":side_a["re_1"],
    "line2_a_re":side_a["re_2"],
    "line3_a_re":side_a["re_3"],
    "line4_a_re":side_a["re_4"],
    "line5_a_re":side_a["re_5"],
    "line6_a_re":side_a["re_6"],

    "line0_b_re":side_b["re_0"],
    "line1_b_re":side_b["re_1"],
    "line2_b_re":side_b["re_2"],
    "line3_b_re":side_b["re_3"],
    "line4_b_re":side_b["re_4"],
    "line5_b_re":side_b["re_5"],
    "line6_b_re":side_b["re_6"]
    }



def past_seven_days(line):

    side_a = {
    "ng_0":0, "ng_1":0, "ng_2":0, "ng_3":0, "ng_4":0, "ng_5":0, "ng_6":0,
    "re_0":0, "re_1":0, "re_2":0, "re_3":0, "re_4":0, "re_5":0, "re_6":0
    }

    side_b = {
    "ng_0":0, "ng_1":0, "ng_2":0, "ng_3":0, "ng_4":0, "ng_5":0, "ng_6":0,
    "re_0":0, "re_1":0, "re_2":0, "re_3":0, "re_4":0, "re_5":0, "re_6":0
    }

    reset_dictionaries()

    # latest date in the database query
    prod_date0 = str(daily_report(line).production_day[0])
    prod_date0 = prod_date0[0:10]
    prod_date1 = str(daily_report(line).production_day[1])
    prod_date1 = prod_date1[0:10]
    prod_date2 = str(daily_report(line).production_day[2])
    prod_date2 = prod_date2[0:10]
    prod_date3 = str(daily_report(line).production_day[3])
    prod_date3 = prod_date3[0:10]
    prod_date4 = str(daily_report(line).production_day[4])
    prod_date4 = prod_date4[0:10]
    prod_date5 = str(daily_report(line).production_day[5])
    prod_date5 = prod_date5[0:10]
    prod_date6 = str(daily_report(line).production_day[6])
    prod_date6 = prod_date6[0:10]

    # today's date converted to the same format as in DB query
    today = date.today().strftime('%Y-%m-%d')
    yesterday = (date.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    two_days_ago = (date.today() - timedelta(days=2)).strftime('%Y-%m-%d')
    three_days_ago = (date.today() - timedelta(days=3)).strftime('%Y-%m-%d')
    four_days_ago = (date.today() - timedelta(days=4)).strftime('%Y-%m-%d')
    five_days_ago = (date.today() - timedelta(days=5)).strftime('%Y-%m-%d')
    six_days_ago = (date.today() - timedelta(days=6)).strftime('%Y-%m-%d')

    # assign variables from specific columns from database based on date
    for_count = 0
    for i in daily_report(line).combined_side_a_ng:
        for_count += 1
        if for_count == 1:
            if prod_date0 == today:
                print("Helllooooooooooooooooooooooo", i)

                side_a["ng_0"] = i
            elif prod_date0 == yesterday:
                side_a["ng_1"] = i
            elif prod_date0 == two_days_ago:
                side_a["ng_2"] = i
            elif prod_date0 == three_days_ago:
                side_a["ng_3"] = i
            elif prod_date0 == four_days_ago:
                side_a["ng_4"] = i
            elif prod_date0 == five_days_ago:
                side_a["ng_5"] = i
            elif prod_date0 == six_days_ago:
                side_a["ng_6"] = i

        elif for_count == 2:
            if prod_date1 == yesterday:
                side_a["ng_1"] = i
            elif prod_date1 == two_days_ago:
                side_a["ng_2"] = i
            elif prod_date1 == three_days_ago:
                side_a["ng_3"] = i
            elif prod_date1 == four_days_ago:
                side_a["ng_4"] = i
            elif prod_date1 == five_days_ago:
                side_a["ng_5"] = i
            elif prod_date1 == six_days_ago:
                side_a["ng_6"] = i


        elif for_count == 3:
            if prod_date2 == two_days_ago:
                side_a["ng_2"] = i
            elif prod_date2 == three_days_ago:
                side_a["ng_3"] = i
            elif prod_date2 == four_days_ago:
                side_a["ng_4"] = i
            elif prod_date2 == five_days_ago:
                side_a["ng_5"] = i
            elif prod_date2 == six_days_ago:
                side_a["ng_6"] = i

        elif for_count == 4:
            if prod_date3 == three_days_ago:
                side_a["ng_3"] = i
            elif prod_date3 == four_days_ago:
                side_a["ng_4"] = i
            elif prod_date3 == five_days_ago:
                side_a["ng_5"] = i
            elif prod_date3 == six_days_ago:
                side_a["ng_6"] = i

        elif for_count == 5:
            if prod_date4 == four_days_ago:
                side_a["ng_4"] = i
            elif prod_date4 == five_days_ago:
                side_a["ng_5"] = i
            elif prod_date4 == six_days_ago:
                side_a["ng_6"] = i

        elif for_count == 6:
            if prod_date5 == five_days_ago:
                side_a["ng_5"] = i
            elif prod_date5 == six_days_ago:
                side_a["ng_6"] = i

        elif for_count == 7:
            if prod_date6 == six_days_ago:
                side_a["ng_6"] = i

    for_count = 0
    for e in daily_report(line).combined_side_b_ng:
        for_count += 1
        if for_count == 1:
            if prod_date0 == today:
                side_b["ng_0"] = e
            elif prod_date0 == yesterday:
                side_b["ng_1"] = e
            elif prod_date0 == two_days_ago:
                side_b["ng_2"] = e
            elif prod_date0 == three_days_ago:
                side_b["ng_3"] = e
            elif prod_date0 == four_days_ago:
                side_b["ng_4"] = e
            elif prod_date0 == five_days_ago:
                side_b["ng_5"] = e
            elif prod_date0 == six_days_ago:
                side_b["ng_6"] = e


        elif for_count == 2:
            if prod_date1 == yesterday:
                side_b["ng_1"] = e
            elif prod_date1 == two_days_ago:
                side_b["ng_2"] = e
            elif prod_date1 == three_days_ago:
                side_b["ng_3"] = e
            elif prod_date1 == four_days_ago:
                side_b["ng_4"] = e
            elif prod_date1 == five_days_ago:
                side_b["ng_5"] = e
            elif prod_date1 == six_days_ago:
                side_b["ng_6"] = e

        elif for_count == 3:
            if prod_date2 == two_days_ago:
                side_b["ng_2"] = e
            elif prod_date2 == three_days_ago:
                side_b["ng_3"] = e
            elif prod_date2 == four_days_ago:
                side_b["ng_4"] = e
            elif prod_date2 == five_days_ago:
                side_b["ng_5"] = e
            elif prod_date2 == six_days_ago:
                side_b["ng_6"] = e

        elif for_count == 4:
            if prod_date3 == three_days_ago:
                side_b["ng_3"] = e
            elif prod_date3 == four_days_ago:
                side_b["ng_4"] = e
            elif prod_date3 == five_days_ago:
                side_b["ng_5"] = e
            elif prod_date3 == six_days_ago:
                side_b["ng_6"] = e

        elif for_count == 5:
            if prod_date4 == four_days_ago:
                side_b["ng_4"] = e
            elif prod_date4 == five_days_ago:
                side_b["ng_5"] = e
            elif prod_date4 == six_days_ago:
                side_b["ng_6"] = e

        elif for_count == 6:
            if prod_date5 == five_days_ago:
                side_b["ng_5"] = e
            elif prod_date5 == six_days_ago:
                side_b["ng_6"] = e

        elif for_count == 7:
            if prod_date6 == six_days_ago:
                side_b["ng_6"] = e

    for_count = 0
    for a in daily_report(line).combined_side_a_re:
        for_count += 1
        if for_count == 1:
            if prod_date0 == today:
                side_a["re_0"] = a
            elif prod_date0 == yesterday:
                side_a["re_1"] = a
            elif prod_date0 == two_days_ago:
                side_a["re_2"] = a
            elif prod_date0 == three_days_ago:
                side_a["re_3"] = a
            elif prod_date0 == four_days_ago:
                side_a["re_4"] = a
            elif prod_date0 == five_days_ago:
                side_a["re_5"] = a
            elif prod_date0 == six_days_ago:
                side_a["re_6"] = a


        elif for_count == 2:
            if prod_date1 == yesterday:
                side_a["re_1"] = a
            elif prod_date1 == two_days_ago:
                side_a["re_2"] = a
            elif prod_date1 == three_days_ago:
                side_a["re_3"] = a
            elif prod_date1 == four_days_ago:
                side_a["re_4"] = a
            elif prod_date1 == five_days_ago:
                side_a["re_5"] = a
            elif prod_date1 == six_days_ago:
                side_a["re_6"] = a

        elif for_count == 3:
            if prod_date2 == two_days_ago:
                side_a["re_2"] = a
            elif prod_date2 == three_days_ago:
                side_a["re_3"] = a
            elif prod_date2 == four_days_ago:
                side_a["re_4"] = a
            elif prod_date2 == five_days_ago:
                side_a["re_5"] = a
            elif prod_date2 == six_days_ago:
                side_a["re_6"] = a

        elif for_count == 4:
            if prod_date3 == three_days_ago:
                side_a["re_3"] = a
            elif prod_date3 == four_days_ago:
                side_a["re_4"] = a
            elif prod_date3 == five_days_ago:
                side_a["re_5"] = a
            elif prod_date3 == six_days_ago:
                side_a["re_6"] = a

        elif for_count == 5:
            if prod_date4 == four_days_ago:
                side_a["re_4"] = a
            elif prod_date4 == five_days_ago:
                side_a["re_5"] = a
            elif prod_date4 == six_days_ago:
                side_a["re_6"] = a

        elif for_count == 6:
            if prod_date5 == five_days_ago:
                side_a["re_5"] = a
            elif prod_date5 == six_days_ago:
                side_a["re_6"] = a

        elif for_count == 7:
            if prod_date6 == six_days_ago:
                side_a["re_6"] = a

    for_count = 0
    for u in daily_report(line).combined_side_b_re:
        for_count += 1
        if for_count == 1:
            if prod_date0 == today:
                side_b["re_0"] = u
            elif prod_date0 == yesterday:
                side_b["re_1"] = u
            elif prod_date0 == two_days_ago:
                side_b["re_2"] = u
            elif prod_date0 == three_days_ago:
                side_b["re_3"] = u
            elif prod_date0 == four_days_ago:
                side_b["re_4"] = u
            elif prod_date0 == five_days_ago:
                side_b["re_5"] = u
            elif prod_date0 == six_days_ago:
                side_b["re_6"] = u

        elif for_count == 2:
            if prod_date1 == yesterday:
                side_b["re_1"] = u
            elif prod_date1 == two_days_ago:
                side_b["re_2"] = u
            elif prod_date1 == three_days_ago:
                side_b["re_3"] = u
            elif prod_date1 == four_days_ago:
                side_b["re_4"] = u
            elif prod_date1 == five_days_ago:
                side_b["re_5"] = u
            elif prod_date1 == six_days_ago:
                side_b["re_6"] = u

        elif for_count == 3:
            if prod_date2 == two_days_ago:
                side_b["re_2"] = u
            elif prod_date2 == three_days_ago:
                side_b["re_3"] = u
            elif prod_date2 == four_days_ago:
                side_b["re_4"] = u
            elif prod_date2 == five_days_ago:
                side_b["re_5"] = u
            elif prod_date2 == six_days_ago:
                side_b["re_6"] = u

        elif for_count == 4:
            if prod_date3 == three_days_ago:
                side_b["re_3"] = u
            elif prod_date3 == four_days_ago:
                side_b["re_4"] = u
            elif prod_date3 == five_days_ago:
                side_b["re_5"] = u
            elif prod_date3 == six_days_ago:
                side_b["re_6"] = u

        elif for_count == 5:
            if prod_date4 == four_days_ago:
                side_b["re_4"] = u
            elif prod_date4 == five_days_ago:
                side_b["re_5"] = u
            elif prod_date4 == six_days_ago:
                side_b["re_6"] = u

        elif for_count == 6:
            if prod_date5 == five_days_ago:
                side_b["re_5"] = u
            elif prod_date5 == six_days_ago:
                side_b["re_6"] = u

        elif for_count == 7:
            if prod_date6 == six_days_ago:
                side_b["re_6"] = u

    return {
    "line":line,
    "line0_a_ng":side_a["ng_0"],
    "line1_a_ng":side_a["ng_1"],
    "line2_a_ng":side_a["ng_2"],
    "line3_a_ng":side_a["ng_3"],
    "line4_a_ng":side_a["ng_4"],
    "line5_a_ng":side_a["ng_5"],
    "line6_a_ng":side_a["ng_6"],

    "line0_b_ng":side_b["ng_0"],
    "line1_b_ng":side_b["ng_1"],
    "line2_b_ng":side_b["ng_2"],
    "line3_b_ng":side_b["ng_3"],
    "line4_b_ng":side_b["ng_4"],
    "line5_b_ng":side_b["ng_5"],
    "line6_b_ng":side_b["ng_6"],

    "line0_a_re":side_a["re_0"],
    "line1_a_re":side_a["re_1"],
    "line2_a_re":side_a["re_2"],
    "line3_a_re":side_a["re_3"],
    "line4_a_re":side_a["re_4"],
    "line5_a_re":side_a["re_5"],
    "line6_a_re":side_a["re_6"],

    "line0_b_re":side_b["re_0"],
    "line1_b_re":side_b["re_1"],
    "line2_b_re":side_b["re_2"],
    "line3_b_re":side_b["re_3"],
    "line4_b_re":side_b["re_4"],
    "line5_b_re":side_b["re_5"],
    "line6_b_re":side_b["re_6"]
    }
