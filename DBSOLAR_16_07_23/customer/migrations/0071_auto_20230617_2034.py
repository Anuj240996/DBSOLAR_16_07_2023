# Generated by Django 3.1.4 on 2023-06-17 15:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0070_auto_20230617_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('43feb61a-f1d3-4426-a527-7b1e717d5a68'), primary_key=True, serialize=False),
        ),
    ]
