# Generated by Django 4.1.1 on 2022-09-22 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_sensordetail_date_sensordetail_sensor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensordetail',
            old_name='date',
            new_name='data',
        ),
        migrations.RenameField(
            model_name='sensordetail',
            old_name='sensor',
            new_name='sensor_id',
        ),
    ]
