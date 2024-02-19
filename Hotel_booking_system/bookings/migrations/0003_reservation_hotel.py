# Generated by Django 5.0.2 on 2024-02-19 05:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_alter_room_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='hotel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='hotel_reservations', to='bookings.hotel'),
            preserve_default=False,
        ),
    ]
