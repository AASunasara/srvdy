# Generated by Django 3.0.3 on 2020-03-04 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0019_auto_20200303_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='days',
            name='cleansing',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='days',
            name='fact_open_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='days',
            name='setup',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
