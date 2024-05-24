# Generated by Django 5.0.4 on 2024-04-12 10:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resecurityapp', '0007_transaction_remove_company_partner'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
