# Generated by Django 3.2.8 on 2021-10-06 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='mileage',
            new_name='mileage_interval',
        ),
    ]