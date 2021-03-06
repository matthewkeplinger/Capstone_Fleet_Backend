# Generated by Django 3.2.8 on 2021-10-06 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_rename_type_service_service_type'),
        ('vehicles', '0001_initial'),
        ('vehicle_services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicleservice',
            name='service_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.service'),
        ),
        migrations.AddField(
            model_name='vehicleservice',
            name='vehicle_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle'),
        ),
    ]
