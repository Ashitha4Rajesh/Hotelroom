# Generated by Django 4.2.7 on 2024-03-05 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_rename_username_booking_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
