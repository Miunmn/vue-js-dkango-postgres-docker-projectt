# Generated by Django 4.0.3 on 2022-04-05 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_journeys_from_city_journeys_to_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='journeys',
            name='assigned_driver',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='journeys',
            name='assigned_bus',
            field=models.IntegerField(default=0),
        ),
    ]
