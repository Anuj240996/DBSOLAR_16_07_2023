# Generated by Django 4.1.5 on 2023-04-23 05:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_customer_cust_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('aaa1d6b8-6681-418b-b92c-48595fc19945'), primary_key=True, serialize=False),
        ),
    ]
