# Generated by Django 3.2.8 on 2021-10-10 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_remove_vehicle_vehicle_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='image',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]