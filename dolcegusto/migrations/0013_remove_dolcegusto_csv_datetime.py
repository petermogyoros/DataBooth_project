# Generated by Django 2.1.1 on 2018-09-13 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dolcegusto', '0012_dolcegusto_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dolcegusto',
            name='csv_datetime',
        ),
    ]