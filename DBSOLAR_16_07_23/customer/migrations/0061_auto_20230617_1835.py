# Generated by Django 3.1.4 on 2023-06-17 13:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0060_auto_20230616_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('d742942a-0b49-4745-8d23-17e9d1a24eba'), primary_key=True, serialize=False),
        ),
    ]