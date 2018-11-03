from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dolcegusto', '0024_remove_dolcegusto_table_saving_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Past_Week',
            fields=[
                ('combined_side_a_ng_avg_1', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_b_ng_avg_1', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_a_re_avg_1', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_b_re_avg_1', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_a_ng_avg_2', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_b_ng_avg_2', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_a_re_avg_2', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_b_re_avg_2', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_a_ng_avg_3', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_b_ng_avg_3', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_a_re_avg_3', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_b_re_avg_3', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_a_ng_avg_4', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_b_ng_avg_4', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_a_re_avg_4', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_b_re_avg_4', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_a_ng_avg_5', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_b_ng_avg_5', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_a_re_avg_5', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_b_re_avg_5', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_a_ng_avg_6', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_b_ng_avg_6', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_a_re_avg_6', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_b_re_avg_6', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_a_ng_avg_7', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_b_ng_avg_7', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_a_re_avg_7', models.DecimalField(decimal_places=16, max_digits=22)),
                ('combined_side_b_re_avg_7', models.DecimalField(decimal_places=16, max_digits=22)),
            ],
            options={
                'db_table': 'dolcegusto_past_week',
                'db_table': 'public.dolcegusto_past_week',
                'managed': False,
            },
        ),
    ]
