# Generated by Django 3.0.3 on 2020-03-06 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0020_auto_20200304_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='days',
            name='fact_close_time',
            field=models.TimeField(blank=True, default='10:00 PM', null=True),
        ),
        migrations.AlterField(
            model_name='days',
            name='fact_open_time',
            field=models.TimeField(default='10:00 AM'),
        ),
    ]
