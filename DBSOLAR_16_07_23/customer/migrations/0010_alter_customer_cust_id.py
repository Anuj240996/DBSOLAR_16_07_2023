# Generated by Django 4.1.5 on 2023-04-25 17:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_alter_customer_cust_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('fda5303e-fe4d-4256-acdc-a4091514252e'), primary_key=True, serialize=False),
        ),
    ]
