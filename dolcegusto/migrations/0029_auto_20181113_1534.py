# Generated by Django 2.1.1 on 2018-11-13 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dolcegusto', '0028_auto_20181113_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dolcegusto_table',
            name='product',
            field=models.CharField(default='Dolce Gusto', max_length=30),
        ),
        migrations.AlterField(
            model_name='dolcegusto_table',
            name='production_site',
            field=models.CharField(default='Eaton Socon', max_length=30),
        ),
    ]
