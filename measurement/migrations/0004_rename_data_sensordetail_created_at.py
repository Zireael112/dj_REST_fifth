# Generated by Django 4.1.1 on 2022-09-24 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_rename_date_sensordetail_data_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensordetail',
            old_name='data',
            new_name='created_at',
        ),
    ]