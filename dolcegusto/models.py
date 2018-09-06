from django.db import models

class Values_in_db(models.Model):
    raw_time = models.IntegerField()
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
    combined_side_b_re = models.IntegerField(default=0)
    a_top_re = models.IntegerField()
    b_top_re = models.IntegerField()
    a_bottom_re = models.IntegerField()
    b_bottom_re = models.IntegerField()
    a_side_re = models.IntegerField()
    b_side_re = models.IntegerField()

    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.raw_time, self.line, self.batch, self.a_ok,
        self.b_ok, self.combined_side_a_ng, self.combined_side_b_ng)
