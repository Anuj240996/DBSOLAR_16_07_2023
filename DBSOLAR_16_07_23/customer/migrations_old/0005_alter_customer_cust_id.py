# Generated by Django 4.1.5 on 2023-04-23 05:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_customer_cust_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('0d6ba370-410a-48c7-82fb-92bc6cdda9c1'), primary_key=True, serialize=False),
        ),
    ]
