# Generated by Django 5.0.4 on 2024-05-23 09:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resecurityapp', '0025_alter_company_partner_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='Partner_Name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='resecurityapp.partner'),
        ),
    ]
