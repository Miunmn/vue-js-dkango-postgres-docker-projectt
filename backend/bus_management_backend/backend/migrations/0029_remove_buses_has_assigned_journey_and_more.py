# Generated by Django 4.0.3 on 2022-04-11 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0028_alter_journeys_buses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buses',
            name='has_assigned_journey',
        ),
        migrations.RemoveField(
            model_name='drivers',
            name='has_assigned_bus',
        ),
    ]