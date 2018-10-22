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
        cursor.execute(
        "SELECT (SELECT avg(combined_side_a_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime >= TIMESTAMP 'today') combined_side_a_ng_avg_1, (SELECT avg(combined_side_b_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime >= TIMESTAMP 'today') combined_side_b_ng_avg_1, (SELECT avg(combined_side_a_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime >= TIMESTAMP 'today') combined_side_a_re_avg_1, (SELECT avg(combined_side_b_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime >= TIMESTAMP 'today') combined_side_b_re_avg_1, (SELECT avg(combined_side_a_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '1 day' AND csv_datetime < CURRENT_DATE - INTERVAL '0 day') combined_side_a_ng_avg_2, (SELECT avg(combined_side_b_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime >
         CURRENT_DATE - INTERVAL '1 day' AND csv_datetime < CURRENT_DATE - INTERVAL '0 day') combined_side_b_ng_avg_2, (SELECT avg(combined_side_a_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime >
         CURRENT_DATE - INTERVAL '1 day' AND csv_datetime < CURRENT_DATE - INTERVAL '0 day') combined_side_a_re_avg_2, (SELECT avg(combined_side_b_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime >
         CURRENT_DATE - INTERVAL '1 day' AND csv_datetime < CURRENT_DATE - INTERVAL '0 day') combined_side_b_re_avg_2, (SELECT avg(combined_side_a_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime >
         CURRENT_DATE - INTERVAL '2 day' AND csv_datetime < CURRENT_DATE - INTERVAL '1 day') combined_side_a_ng_avg_3, (SELECT avg(combined_side_b_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime >
         CURRENT_DATE - INTERVAL '2 day' AND csv_datetime < CURRENT_DATE - INTERVAL '1 day') combined_side_b_ng_avg_3, (SELECT avg(combined_side_a_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime >
         CURRENT_DATE - INTERVAL '2 day' AND csv_datetime < CURRENT_DATE - INTERVAL '1 day') combined_side_a_re_avg_3, (SELECT avg(combined_side_b_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime >
         CURRENT_DATE - INTERVAL '2 day' AND csv_datetime < CURRENT_DATE - INTERVAL '1 day') combined_side_b_re_avg_3,

-- query for three days ago
(SELECT avg(combined_side_a_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '3 day' AND csv_datetime < CURRENT_DATE - INTERVAL '2 day') combined_side_a_ng_avg_4,
(SELECT avg(combined_side_b_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '3 day' AND csv_datetime < CURRENT_DATE - INTERVAL '2 day') combined_side_b_ng_avg_4,
(SELECT avg(combined_side_a_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '3 day' AND csv_datetime < CURRENT_DATE - INTERVAL '2 day') combined_side_a_re_avg_4,
(SELECT avg(combined_side_b_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '3 day' AND csv_datetime < CURRENT_DATE - INTERVAL '2 day') combined_side_b_re_avg_4,

-- query for four days ago
(SELECT avg(combined_side_a_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '4 day' AND csv_datetime < CURRENT_DATE - INTERVAL '3 day') combined_side_a_ng_avg_5,
(SELECT avg(combined_side_b_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '4 day' AND csv_datetime < CURRENT_DATE - INTERVAL '3 day') combined_side_b_ng_avg_5,
(SELECT avg(combined_side_a_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '4 day' AND csv_datetime < CURRENT_DATE - INTERVAL '3 day') combined_side_a_re_avg_5,
(SELECT avg(combined_side_b_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '4 day' AND csv_datetime < CURRENT_DATE - INTERVAL '3 day') combined_side_b_re_avg_5,

-- query for five days ago
(SELECT avg(combined_side_a_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '5 day' AND csv_datetime < CURRENT_DATE - INTERVAL '4 day') combined_side_a_ng_avg_6,
(SELECT avg(combined_side_b_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '5 day' AND csv_datetime < CURRENT_DATE - INTERVAL '4 day') combined_side_b_ng_avg_6,
(SELECT avg(combined_side_a_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '5 day' AND csv_datetime < CURRENT_DATE - INTERVAL '4 day') combined_side_a_re_avg_6,
(SELECT avg(combined_side_b_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '5 day' AND csv_datetime < CURRENT_DATE - INTERVAL '4 day') combined_side_b_re_avg_6,

-- query for six days ago
(SELECT avg(combined_side_a_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '6 day' AND csv_datetime < CURRENT_DATE - INTERVAL '5 day') combined_side_a_ng_avg_7,
(SELECT avg(combined_side_b_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '6 day' AND csv_datetime < CURRENT_DATE - INTERVAL '5 day') combined_side_b_ng_avg_7,
(SELECT avg(combined_side_a_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '6 day' AND csv_datetime < CURRENT_DATE - INTERVAL '5 day') combined_side_a_re_avg_7,
(SELECT avg(combined_side_b_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '6 day' AND csv_datetime < CURRENT_DATE - INTERVAL '5 day') combined_side_b_re_avg_7
"
        )
        today = cursor.fetchone()
    return today

# SQL View query backup:
# CREATE OR REPLACE VIEW past_week (
# 	combined_side_a_ng_avg_1, combined_side_b_ng_avg_1, combined_side_a_re_avg_1, combined_side_b_re_avg_1,
# 	combined_side_a_ng_avg_2, combined_side_b_ng_avg_2, combined_side_a_re_avg_2, combined_side_b_re_avg_2,
# 	combined_side_a_ng_avg_3, combined_side_b_ng_avg_3, combined_side_a_re_avg_3, combined_side_b_re_avg_3,
# 	combined_side_a_ng_avg_4, combined_side_b_ng_avg_4, combined_side_a_re_avg_4, combined_side_b_re_avg_4,
# 	combined_side_a_ng_avg_5, combined_side_b_ng_avg_5, combined_side_a_re_avg_5, combined_side_b_re_avg_5,
# 	combined_side_a_ng_avg_6, combined_side_b_ng_avg_6, combined_side_a_re_avg_6, combined_side_b_re_avg_6,
# 	combined_side_a_ng_avg_7, combined_side_b_ng_avg_7, combined_side_a_re_avg_7, combined_side_b_re_avg_7
# )
#
# AS SELECT
# -- query for today
# (SELECT avg(combined_side_a_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime >= TIMESTAMP 'today'),
# (SELECT avg(combined_side_b_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime >= TIMESTAMP 'today'),
# (SELECT avg(combined_side_a_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime >= TIMESTAMP 'today'),
# (SELECT avg(combined_side_b_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime >= TIMESTAMP 'today'),
#
# -- query for one day ago
# (SELECT avg(combined_side_a_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '1 day' AND csv_datetime < CURRENT_DATE - INTERVAL '0 day'),
# (SELECT avg(combined_side_b_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '1 day' AND csv_datetime < CURRENT_DATE - INTERVAL '0 day'),
# (SELECT avg(combined_side_a_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '1 day' AND csv_datetime < CURRENT_DATE - INTERVAL '0 day'),
# (SELECT avg(combined_side_b_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '1 day' AND csv_datetime < CURRENT_DATE - INTERVAL '0 day'),
#
# -- query for two days ago
# (SELECT avg(combined_side_a_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '2 day' AND csv_datetime < CURRENT_DATE - INTERVAL '1 day'),
# (SELECT avg(combined_side_b_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '2 day' AND csv_datetime < CURRENT_DATE - INTERVAL '1 day'),
# (SELECT avg(combined_side_a_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '2 day' AND csv_datetime < CURRENT_DATE - INTERVAL '1 day'),
# (SELECT avg(combined_side_b_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '2 day' AND csv_datetime < CURRENT_DATE - INTERVAL '1 day'),
#
# -- query for three days ago
# (SELECT avg(combined_side_a_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '3 day' AND csv_datetime < CURRENT_DATE - INTERVAL '2 day'),
# (SELECT avg(combined_side_b_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '3 day' AND csv_datetime < CURRENT_DATE - INTERVAL '2 day'),
# (SELECT avg(combined_side_a_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '3 day' AND csv_datetime < CURRENT_DATE - INTERVAL '2 day'),
# (SELECT avg(combined_side_b_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '3 day' AND csv_datetime < CURRENT_DATE - INTERVAL '2 day'),
#
# -- query for four days ago
# (SELECT avg(combined_side_a_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '4 day' AND csv_datetime < CURRENT_DATE - INTERVAL '3 day'),
# (SELECT avg(combined_side_b_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '4 day' AND csv_datetime < CURRENT_DATE - INTERVAL '3 day'),
# (SELECT avg(combined_side_a_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '4 day' AND csv_datetime < CURRENT_DATE - INTERVAL '3 day'),
# (SELECT avg(combined_side_b_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '4 day' AND csv_datetime < CURRENT_DATE - INTERVAL '3 day'),
#
# -- query for five days ago
# (SELECT avg(combined_side_a_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '5 day' AND csv_datetime < CURRENT_DATE - INTERVAL '4 day'),
# (SELECT avg(combined_side_b_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '5 day' AND csv_datetime < CURRENT_DATE - INTERVAL '4 day'),
# (SELECT avg(combined_side_a_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '5 day' AND csv_datetime < CURRENT_DATE - INTERVAL '4 day'),
# (SELECT avg(combined_side_b_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '5 day' AND csv_datetime < CURRENT_DATE - INTERVAL '4 day'),
#
# -- query for six days ago
# (SELECT avg(combined_side_a_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '6 day' AND csv_datetime < CURRENT_DATE - INTERVAL '5 day'),
# (SELECT avg(combined_side_b_ng) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '6 day' AND csv_datetime < CURRENT_DATE - INTERVAL '5 day'),
# (SELECT avg(combined_side_a_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '6 day' AND csv_datetime < CURRENT_DATE - INTERVAL '5 day'),
# (SELECT avg(combined_side_b_re) FROM dolcegusto_dolcegusto_table WHERE csv_datetime > CURRENT_DATE - INTERVAL '6 day' AND csv_datetime < CURRENT_DATE - INTERVAL '5 day')
#
# ;
