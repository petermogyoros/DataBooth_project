
#  use this these line to get an integer for a weekday. the get_weekday function then translates this integer into weekday name
# This gives the function bellow an integer which translates to the weekday name
# 
# day2 = get_weekday(datetime.strptime(str(daily_report(5).production_day[2])[0:10], '%Y-%m-%d').date().weekday)
# day3 = get_weekday(datetime.strptime(str(daily_report(5).production_day[3])[0:10], '%Y-%m-%d').date().weekday)
# day4 = get_weekday(datetime.strptime(str(daily_report(5).production_day[4])[0:10], '%Y-%m-%d').date().weekday)
# day5 = get_weekday(datetime.strptime(str(daily_report(5).production_day[5])[0:10], '%Y-%m-%d').date().weekday)
# day6 = get_weekday(datetime.strptime(str(daily_report(5).production_day[6])[0:10], '%Y-%m-%d').date().weekday)

# assign weekday name to variable
def get_weekday(weekday_number):

    if weekday_number() == 0:
        weekday_name = "Mon"
    elif weekday_number() == 1:
        weekday_name = "Tue"
    elif weekday_number() == 2:
        weekday_name = "Wed"
    elif weekday_number() == 3:
        weekday_name = "Thu"
    elif weekday_number() == 4:
        weekday_name = "Fri"
    elif weekday_number() == 5:
        weekday_name = "Sat"
    elif weekday_number() == 6:
        weekday_name = "Sun"

    return weekday_name
