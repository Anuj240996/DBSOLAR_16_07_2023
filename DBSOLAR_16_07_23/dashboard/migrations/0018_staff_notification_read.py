# Generated by Django 4.1.5 on 2023-04-14 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_staff_notification_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_notification',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]