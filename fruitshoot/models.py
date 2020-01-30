from django.db import models, connection
import pandas as pd
from pandas import DataFrame

# This class is to manage database fields. Add entries here to extend database.
class FruitShoot_table(models.Model):

    csv_datetime = models.DateTimeField(
    default="1980-09-25 00:00:00",max_length=9)
    program = models.CharField(max_length=30)
    production_line = models.IntegerField()
    ok_caps = models.IntegerField()
    rejects_overal = models.IntegerField()
    reject_search = models.IntegerField()
    reject_remap = models.IntegerField()
    reject_idv = models.IntegerField()
    reject_dimension = models.IntegerField()
    reject_dc_top_view = models.IntegerField()
    reject_cap_inner = models.IntegerField()
    reject_te_band = models.IntegerField()
    # reject_body bellow is Knurling
    reject_body = models.IntegerField()
    reject_spout_top = models.IntegerField()
    reject_spout_side = models.IntegerField()
    reject_dc_ring = models.IntegerField()
    reject_dc_blob = models.IntegerField()
    # reject_short_spout is Measure Height
    reject_short_spout = models.IntegerField()
    product = models.CharField(max_length=30, default="Fruit Shoot")
    production_site = models.CharField(max_length=30)
