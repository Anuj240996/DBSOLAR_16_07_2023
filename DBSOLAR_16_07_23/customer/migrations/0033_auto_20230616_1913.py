# Generated by Django 3.1.4 on 2023-06-16 13:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0032_auto_20230616_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('ab51c308-158d-4cf3-9a21-ef91c4b1047c'), primary_key=True, serialize=False),
        ),
    ]
