from django.db import models, connection
import pandas as pd
from pandas import DataFrame

# This class is to manage database fields. Add entries here to extend database.
class SecureFlip_I2S_table(models.Model):

    csv_datetime = models.DateTimeField(
    default="1980-09-25 00:00:00",max_length=9)
    program = models.CharField(max_length=30)
    production_line = models.IntegerField()
    ok_caps = models.IntegerField()
    rejects_overal = models.IntegerField()
    reject_search = models.IntegerField()
    reject_remap = models.IntegerField()
    reject_idv = models.IntegerField()
    reject_spout_top = models.IntegerField()
    reject_cap_top = models.IntegerField()
    reject_seal_side = models.IntegerField()
    reject_dc_side = models.IntegerField()
    reject_cap_side = models.IntegerField()
    reject_measure_slit = models.IntegerField()
    product = models.CharField(max_length=30)
    production_site = models.CharField(max_length=30)
