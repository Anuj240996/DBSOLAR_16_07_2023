# Generated by Django 3.1.4 on 2023-06-17 14:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0068_auto_20230617_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cust_id',
            field=models.IntegerField(default=uuid.UUID('73dba739-d752-429a-b046-7e4c65faac4f'), primary_key=True, serialize=False),
        ),
    ]