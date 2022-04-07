# Generated by Django 4.0.3 on 2022-04-05 15:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_buses_bus_id_alter_drivers_driver_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivers',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(18)]),
        ),
        migrations.AlterField(
            model_name='drivers',
            name='first_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='drivers',
            name='last_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]
