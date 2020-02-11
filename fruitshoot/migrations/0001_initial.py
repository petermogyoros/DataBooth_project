# Generated by Django 2.1.1 on 2019-10-22 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FruitShoot_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_datetime', models.DateTimeField(default='1980-09-25 00:00:00', max_length=9)),
                ('program', models.CharField(max_length=30)),
                ('production_line', models.IntegerField()),
                ('ok_caps', models.IntegerField()),
                ('rejects_overal', models.IntegerField()),
                ('reject_search', models.IntegerField()),
                ('reject_remap', models.IntegerField()),
                ('reject_idv', models.IntegerField()),
                ('reject_dimension', models.IntegerField()),
                ('reject_dc_top_view', models.IntegerField()),
                ('reject_cap_inner', models.IntegerField()),
                ('reject_te_band', models.IntegerField()),
                ('reject_body', models.IntegerField()),
                ('reject_spout_top', models.IntegerField()),
                ('reject_spout_side', models.IntegerField()),
                ('reject_dc_ring', models.IntegerField()),
                ('reject_dc_blob', models.IntegerField()),
                ('reject_short_spout', models.IntegerField()),
                ('product', models.CharField(default='Fruit Shoot', max_length=30)),
                ('production_site', models.CharField(max_length=30)),
            ],
        ),
    ]