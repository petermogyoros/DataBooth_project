# Generated by Django 2.1.1 on 2018-09-19 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dolcegusto', '0018_delete_dolcegusto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dolcegusto_table',
            name='date_of_csv',
        ),
        migrations.AddField(
            model_name='dolcegusto_table',
            name='csv_date',
            field=models.DateField(default='1980-09-25'),
        ),
        migrations.DeleteModel(
            name='CSV_Date',
        ),
    ]