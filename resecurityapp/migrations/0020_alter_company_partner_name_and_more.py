# Generated by Django 5.0.4 on 2024-05-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resecurityapp', '0019_alter_sector_sector_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='Partner_Name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='Referral_Name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]