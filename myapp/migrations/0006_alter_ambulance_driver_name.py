# Generated by Django 4.2.7 on 2023-11-18 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_ambulance_telephone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambulance',
            name='driver_name',
            field=models.CharField(default='Not Provided!', max_length=20),
        ),
    ]
