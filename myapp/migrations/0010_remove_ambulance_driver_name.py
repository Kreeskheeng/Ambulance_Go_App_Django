# Generated by Django 4.2.7 on 2023-11-18 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_ambulance_driver_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ambulance',
            name='driver_name',
        ),
    ]
