# Generated by Django 5.0.4 on 2024-05-28 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resecurityapp', '0040_requirement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='Brand_Name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='Service_Name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
