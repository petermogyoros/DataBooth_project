from django.db import models, connection
import pandas as pd
from pandas import DataFrame

# This class is to manage database fields. Add entries here to extend database.
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
def dashboard(self):

    with connection.cursor() as cursor:
        cursor.execute(
        "SELECT * FROM public.daily_scrap WHERE line = %s LIMIT 1", [self]
        )
        daily_report = cursor.fetchall()
    dashboard_df = DataFrame(daily_report, columns = [
    'line', 'batch',
    'a_ok', 'b_ok',
    'combined_side_a_ng', 'combined_side_b_ng',
    'combined_side_a_re', 'combined_side_b_re',
    'a_top_ng', 'b_top_ng',
    'a_bottom_ng', 'b_bottom_ng',
    'a_side_ng', 'b_side_ng',
    'a_top_re', 'b_top_re',
    'a_bottom_re', 'b_bottom_re',
    'a_side_re', 'b_side_re',
    'production_day'])

    # df = pd.DataFrame(dashboard_df)
    # print(df)
    return dashboard_df


def hourly_report(self):

    with connection.cursor() as cursor:
        cursor.execute(
        "SELECT * FROM public.hourly_scrap WHERE line = %s LIMIT 7", [self]
        )
        hourly_report = cursor.fetchall()
    hourly_report_df = DataFrame(hourly_report, columns = [
    'line', 'batch',
    'a_ok', 'b_ok',
    'combined_side_a_ng', 'combined_side_b_ng',
    'combined_side_a_re', 'combined_side_b_re',
    'a_top_ng', 'b_top_ng',
    'a_bottom_ng', 'b_bottom_ng',
    'a_side_ng', 'b_side_ng',
    'a_top_re', 'b_top_re',
    'a_bottom_re', 'b_bottom_re',
    'a_side_re', 'b_side_re',
    'hour'])

    return hourly_report_df

def daily_report(self):

    with connection.cursor() as cursor:
        cursor.execute(
        "SELECT * FROM public.daily_scrap WHERE line = %s LIMIT 7", [self]
        )
        daily_report = cursor.fetchall()
    daily_report_df = DataFrame(daily_report, columns = [
    'line', 'batch',
    'a_ok', 'b_ok',
    'combined_side_a_ng', 'combined_side_b_ng',
    'combined_side_a_re', 'combined_side_b_re',
    'a_top_ng', 'b_top_ng',
    'a_bottom_ng', 'b_bottom_ng',
    'a_side_ng', 'b_side_ng',
    'a_top_re', 'b_top_re',
    'a_bottom_re', 'b_bottom_re',
    'a_side_re', 'b_side_re',
    'production_day'])

    return daily_report_df


def weekly_report(self):

    with connection.cursor() as cursor:
        cursor.execute(
        "SELECT * FROM public.weekly_scrap WHERE line = %s LIMIT 7", [self]
        )
        weekly_report = cursor.fetchall()
    weekly_report_df = DataFrame(weekly_report, columns = [
    'line', 'batch',
    'a_ok', 'b_ok',
    'combined_side_a_ng', 'combined_side_b_ng',
    'combined_side_a_re', 'combined_side_b_re',
    'a_top_ng', 'b_top_ng',
    'a_bottom_ng', 'b_bottom_ng',
    'a_side_ng', 'b_side_ng',
    'a_top_re', 'b_top_re',
    'a_bottom_re', 'b_bottom_re',
    'a_side_re', 'b_side_re',
    'production_week'])

    return weekly_report_df

def monthly_report(self):

    with connection.cursor() as cursor:
        cursor.execute(
        "SELECT * FROM public.monthly_scrap WHERE line = %s LIMIT 7", [self]
        )
        monthly_report = cursor.fetchall()
    monthly_report_df = DataFrame(monthly_report, columns = [
    'line', 'batch',
    'a_ok', 'b_ok',
    'combined_side_a_ng', 'combined_side_b_ng',
    'combined_side_a_re', 'combined_side_b_re',
    'a_top_ng', 'b_top_ng',
    'a_bottom_ng', 'b_bottom_ng',
    'a_side_ng', 'b_side_ng',
    'a_top_re', 'b_top_re',
    'a_bottom_re', 'b_bottom_re',
    'a_side_re', 'b_side_re',
    'production_month'])

    return monthly_report_df
