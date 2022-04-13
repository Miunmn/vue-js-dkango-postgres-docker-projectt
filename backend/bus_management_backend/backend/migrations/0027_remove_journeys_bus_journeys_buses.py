# Generated by Django 4.0.3 on 2022-04-11 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0026_rename_buses_journeys_bus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journeys',
            name='bus',
        ),
        migrations.AddField(
            model_name='journeys',
            name='buses',
            field=models.ManyToManyField(default=1, null=None, to='backend.buses'),
        ),
    ]