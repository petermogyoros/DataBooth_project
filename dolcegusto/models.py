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


    # bypassing django model and querying SQL directely
def scrap_rate(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT avg(combined_side_a_ng), avg(combined_side_b_ng), avg(combined_side_a_re), avg(combined_side_b_re) FROM dolcegusto_dolcegusto_table")
        row = cursor.fetchone()
    return row

    # def __str__(self):
    #
    #     return str(mean(self.a_ok))
