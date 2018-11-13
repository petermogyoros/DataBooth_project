from django.db import models, connection
import pandas as pd
from pandas import DataFrame

class DolceGusto_table(models.Model):
    csv_datetime = models.DateTimeField(
    default="1980-09-25 00:00:00",max_length=9)
    line = models.IntegerField()
    batch = models.IntegerField()
    a_ok = models.IntegerField()
    b_ok = models.IntegerField()
    combined_side_a_ng = models.IntegerField()
    combined_side_b_ng = models.IntegerField()
    a_top_ng = models.IntegerField()
    b_top_ng = models.IntegerField()
    a_bottom_ng = models.IntegerField()
    b_bottom_ng = models.IntegerField()
    a_side_ng = models.IntegerField()
    b_side_ng = models.IntegerField()
    combined_side_a_re = models.IntegerField()
    combined_side_b_re = models.IntegerField()
    a_top_re = models.IntegerField()
    b_top_re = models.IntegerField()
    a_bottom_re = models.IntegerField()
    b_bottom_re = models.IntegerField()
    a_side_re = models.IntegerField()
    b_side_re = models.IntegerField()
    product = models.CharField(max_length=30, default="Dolce Gusto")
    production_site = models.CharField(max_length=30, default="Eaton Socon")

# bypassing django model and querying SQL views directely
def daily_report(self):

    print(self)
    with connection.cursor() as cursor:
        cursor.execute(
        "SELECT * FROM public.daily_scrap WHERE line = %s LIMIT 7", [self]
        )
        daily_report = cursor.fetchall()
    daily_report_df = DataFrame(daily_report, columns = [
    'line',
    'combined_side_a_ng', 'combined_side_b_ng',
    'combined_side_a_re', 'combined_side_b_re',
    'production_day'])

    return daily_report_df
