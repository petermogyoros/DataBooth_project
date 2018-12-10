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
