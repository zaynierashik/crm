# Generated by Django 5.0.2 on 2024-06-01 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resecurityapp', '0053_alter_transaction_company_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='Company_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resecurityapp.company'),
        ),
    ]