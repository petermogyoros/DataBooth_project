from dolcegusto.models import daily_report, hourly_report
from datetime import datetime, date, timedelta


def past_twelve_hours(line):

    # set all values to zero
    top = {"a_0":0, "a_1":0, "a_2":0, "a_3":0, "a_4":0, "a_5":0, "a_6":0,
    "b_0":0, "b_1":0, "b_2":0, "b_3":0, "b_4":0, "b_5":0, "b_6":0}

    bottom = {"a_0":0, "a_1":0, "a_2":0, "a_3":0, "a_4":0, "a_5":0, "a_6":0,
    "b_0":0, "b_1":0, "b_2":0, "b_3":0, "b_4":0, "b_5":0, "b_6":0}

    side = {"a_0":0, "a_1":0, "a_2":0, "a_3":0, "a_4":0, "a_5":0, "a_6":0,
    "b_0":0, "b_1":0, "b_2":0, "b_3":0, "b_4":0, "b_5":0, "b_6":0}


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




def past_seven_days(line):

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

    for_count = 0
    for e in daily_report(line).combined_side_b_ng:
        for_count += 1
        if for_count == 1:
            if prod_date0 == today:
                line0_b_ng = e
            elif prod_date0 == yesterday:
                line1_b_ng = e
            elif prod_date0 == two_days_ago:
                line2_b_ng = e
            elif prod_date0 == three_days_ago:
                line3_b_ng = e
            elif prod_date0 == four_days_ago:
                line4_b_ng = e
            elif prod_date0 == five_days_ago:
                line5_b_ng = e
            elif prod_date0 == six_days_ago:
                line6_b_ng = e


        elif for_count == 2:
            if prod_date1 == yesterday:
                line1_b_ng = e
            elif prod_date1 == two_days_ago:
                line2_b_ng = e
            elif prod_date1 == three_days_ago:
                line3_b_ng = e
            elif prod_date1 == four_days_ago:
                line4_b_ng = e
            elif prod_date1 == five_days_ago:
                line5_b_ng = e
            elif prod_date1 == six_days_ago:
                line6_b_ng = e

        elif for_count == 3:
            if prod_date2 == two_days_ago:
                line2_b_ng = e
            elif prod_date2 == three_days_ago:
                line3_b_ng = e
            elif prod_date2 == four_days_ago:
                line4_b_ng = e
            elif prod_date2 == five_days_ago:
                line5_b_ng = e
            elif prod_date2 == six_days_ago:
                line6_b_ng = e

        elif for_count == 4:
            if prod_date3 == three_days_ago:
                line3_b_ng = e
            elif prod_date3 == four_days_ago:
                line4_b_ng = e
            elif prod_date3 == five_days_ago:
                line5_b_ng = e
            elif prod_date3 == six_days_ago:
                line6_b_ng = e

        elif for_count == 5:
            if prod_date4 == four_days_ago:
                line4_b_ng = e
            elif prod_date4 == five_days_ago:
                line5_b_ng = e
            elif prod_date4 == six_days_ago:
                line6_b_ng = e

        elif for_count == 6:
            if prod_date5 == five_days_ago:
                line5_b_ng = e
            elif prod_date5 == six_days_ago:
                line6_b_ng = e

        elif for_count == 7:
            if prod_date6 == six_days_ago:
                line6_b_ng = e

    for_count = 0
    for a in daily_report(line).combined_side_a_re:
        for_count += 1
        if for_count == 1:
            if prod_date0 == today:
                line0_a_re = a
            elif prod_date0 == yesterday:
                line1_a_re = a
            elif prod_date0 == two_days_ago:
                line2_a_re = a
            elif prod_date0 == three_days_ago:
                line3_a_re = a
            elif prod_date0 == four_days_ago:
                line4_a_re = a
            elif prod_date0 == five_days_ago:
                line5_a_re = a
            elif prod_date0 == six_days_ago:
                line6_a_re = a


        elif for_count == 2:
            if prod_date1 == yesterday:
                line1_a_re = a
            elif prod_date1 == two_days_ago:
                line2_a_re = a
            elif prod_date1 == three_days_ago:
                line3_a_re = a
            elif prod_date1 == four_days_ago:
                line4_a_re = a
            elif prod_date1 == five_days_ago:
                line5_a_re = a
            elif prod_date1 == six_days_ago:
                line6_a_re = a

        elif for_count == 3:
            if prod_date2 == two_days_ago:
                line2_a_re = a
            elif prod_date2 == three_days_ago:
                line3_a_re = a
            elif prod_date2 == four_days_ago:
                line4_a_re = a
            elif prod_date2 == five_days_ago:
                line5_a_re = a
            elif prod_date2 == six_days_ago:
                line6_a_re = a

        elif for_count == 4:
            if prod_date3 == three_days_ago:
                line3_a_re = a
            elif prod_date3 == four_days_ago:
                line4_a_re = a
            elif prod_date3 == five_days_ago:
                line5_a_re = a
            elif prod_date3 == six_days_ago:
                line6_a_re = a

        elif for_count == 5:
            if prod_date4 == four_days_ago:
                line4_a_re = a
            elif prod_date4 == five_days_ago:
                line5_a_re = a
            elif prod_date4 == six_days_ago:
                line6_a_re = a

        elif for_count == 6:
            if prod_date5 == five_days_ago:
                line5_a_re = a
            elif prod_date5 == six_days_ago:
                line6_a_re = a

        elif for_count == 7:
            if prod_date6 == six_days_ago:
                line6_a_re = a

    for_count = 0
    for u in daily_report(line).combined_side_b_re:
        for_count += 1
        if for_count == 1:
            if prod_date0 == today:
                line0_b_re = u
            elif prod_date0 == yesterday:
                line1_b_re = u
            elif prod_date0 == two_days_ago:
                line2_b_re = u
            elif prod_date0 == three_days_ago:
                line3_b_re = u
            elif prod_date0 == four_days_ago:
                line4_b_re = u
            elif prod_date0 == five_days_ago:
                line5_b_re = u
            elif prod_date0 == six_days_ago:
                line6_b_re = u


        elif for_count == 2:
            if prod_date1 == yesterday:
                line1_b_re = u
            elif prod_date1 == two_days_ago:
                line2_b_re = u
            elif prod_date1 == three_days_ago:
                line3_b_re = u
            elif prod_date1 == four_days_ago:
                line4_b_re = u
            elif prod_date1 == five_days_ago:
                line5_b_re = u
            elif prod_date1 == six_days_ago:
                line6_b_re = u

        elif for_count == 3:
            if prod_date2 == two_days_ago:
                line2_b_re = u
            elif prod_date2 == three_days_ago:
                line3_b_re = u
            elif prod_date2 == four_days_ago:
                line4_b_re = u
            elif prod_date2 == five_days_ago:
                line5_b_re = u
            elif prod_date2 == six_days_ago:
                line6_b_re = u

        elif for_count == 4:
            if prod_date3 == three_days_ago:
                line3_b_re = u
            elif prod_date3 == four_days_ago:
                line4_b_re = u
            elif prod_date3 == five_days_ago:
                line5_b_re = u
            elif prod_date3 == six_days_ago:
                line6_b_re = u

        elif for_count == 5:
            if prod_date4 == four_days_ago:
                line4_b_re = u
            elif prod_date4 == five_days_ago:
                line5_b_re = u
            elif prod_date4 == six_days_ago:
                line6_b_re = u

        elif for_count == 6:
            if prod_date5 == five_days_ago:
                line5_b_re = u
            elif prod_date5 == six_days_ago:
                line6_b_re = u

        elif for_count == 7:
            if prod_date6 == six_days_ago:
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
