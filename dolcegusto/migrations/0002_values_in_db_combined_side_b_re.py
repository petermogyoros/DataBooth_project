# Generated by Django 2.0.5 on 2018-09-06 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dolcegusto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='values_in_db',
            name='combined_side_b_re',
            field=models.IntegerField(default=0),
        ),
    ]
