# Generated by Django 2.1.1 on 2020-01-30 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruitshoot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruitshoot_table',
            name='production_line',
            field=models.IntegerField(default=13),
        ),
    ]
