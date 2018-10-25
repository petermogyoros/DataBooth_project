from django.db import models, connection

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

# bypassing django model and querying SQL views directely
def past_week_scrap(self):

    with connection.cursor() as cursor:
        cursor.execute(
        "SELECT * FROM public.past_week"
        )
        today = cursor.fetchone()
    return today


# class Past_Week(models.Model):
#     # id = models.IntegerField(primary_key = True)
#     combined_side_a_ng_avg_1 = models.DecimalField(max_digits=22, decimal_places=16)
#     combined_side_b_ng_avg_1 = models.DecimalField(max_digits=22, decimal_places=16)
#     combined_side_a_re_avg_1 = models.DecimalField(max_digits=22, decimal_places=16)
#     combined_side_b_re_avg_1 = models.DecimalField(max_digits=22, decimal_places=16)
#
#
#     combined_side_a_ng_avg_2 = models.DecimalField(max_digits=22, decimal_places=16)
#     combined_side_b_ng_avg_2 = models.DecimalField(max_digits=22, decimal_places=16)
#     combined_side_a_re_avg_2 = models.DecimalField(max_digits=22, decimal_places=16)
#     combined_side_b_re_avg_2 = models.DecimalField(max_digits=22, decimal_places=16)
#
#     combined_side_a_ng_avg_3 = models.DecimalField(max_digits=22, decimal_places=16)
#     combined_side_b_ng_avg_3 = models.DecimalField(max_digits=22, decimal_places=16)
#     combined_side_a_re_avg_3 = models.DecimalField(max_digits=22, decimal_places=16)
#     combined_side_b_re_avg_3 = models.DecimalField(max_digits=22, decimal_places=16)
#
#     combined_side_a_ng_avg_4 = models.DecimalField(max_digits=22, decimal_places=16)
#     combined_side_b_ng_avg_4 = models.DecimalField(max_digits=22, decimal_places=16)
#     combined_side_a_re_avg_4 = models.DecimalField(max_digits=22, decimal_places=16)
#     combined_side_b_re_avg_4 = models.DecimalField(max_digits=22, decimal_places=16)
#
#     combined_side_a_ng_avg_5 = models.DecimalField(max_digits=22, decimal_places=16)
#     combined_side_b_ng_avg_5 = models.DecimalField(max_digits=22, decimal_places=16)
#     combined_side_a_re_avg_5 = models.DecimalField(max_digits=22, decimal_places=16)
#     combined_side_b_re_avg_5 = models.DecimalField(max_digits=22, decimal_places=16)
#
#     combined_side_a_ng_avg_6 = models.DecimalField(max_digits=22, decimal_places=16)
#     combined_side_b_ng_avg_6 = models.DecimalField(max_digits=22, decimal_places=16)
#     combined_side_a_re_avg_6 = models.DecimalField(max_digits=22, decimal_places=16)
#     combined_side_b_re_avg_6 = models.DecimalField(max_digits=22, decimal_places=16)
#
#     combined_side_a_ng_avg_7 = models.DecimalField(max_digits=22, decimal_places=16)
#     combined_side_b_ng_avg_7 = models.DecimalField(max_digits=22, decimal_places=16)
#     combined_side_a_re_avg_7 = models.DecimalField(max_digits=22, decimal_places=16)
#     combined_side_b_re_avg_7 = models.DecimalField(max_digits=22, decimal_places=16)
#
#     class Meta:
#         managed = False
#         db_table = 'past_week'
