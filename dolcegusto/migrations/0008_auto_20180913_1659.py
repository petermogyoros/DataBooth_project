# Generated by Django 2.1.1 on 2018-09-13 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dolcegusto', '0007_auto_20180913_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dolcegusto',
            name='csv_date',
            field=models.DateField(default='1980-09-25'),
        ),
        migrations.AlterField(
            model_name='dolcegusto',
            name='csv_time',
            field=models.TimeField(default='00:00'),
        ),
    ]
