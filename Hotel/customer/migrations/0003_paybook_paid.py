# Generated by Django 4.2.7 on 2024-03-18 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_payorder_paybook'),
    ]

    operations = [
        migrations.AddField(
            model_name='paybook',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
