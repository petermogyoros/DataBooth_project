# Generated by Django 2.1.1 on 2020-01-30 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruitshoot', '0004_fruitshoot_table_spout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruitshoot_table',
            name='spout',
            field=models.IntegerField(),
        ),
    ]