# Generated by Django 5.0.2 on 2024-02-19 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='room',
            unique_together={('hotel', 'room_number')},
        ),
    ]
