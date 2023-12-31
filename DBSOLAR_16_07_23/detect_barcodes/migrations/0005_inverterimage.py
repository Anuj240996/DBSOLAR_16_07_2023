# Generated by Django 3.1.4 on 2023-06-18 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('detect_barcodes', '0004_auto_20230618_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='InverterImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode_data', models.CharField(max_length=255)),
                ('file_saved_at', models.DateTimeField()),
                ('image', models.ImageField(upload_to='static/barcode_images')),
                ('barcode_type', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=255, null=True)),
                ('wattage', models.CharField(max_length=50, null=True)),
                ('barcode_path', models.ImageField(upload_to='static/barcode_images')),
                ('product_name', models.CharField(max_length=100, null=True)),
                ('company_name', models.CharField(max_length=255, null=True)),
                ('AssignBy', models.IntegerField(default=0)),
                ('AssignTo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
