# Generated by Django 5.0.4 on 2024-04-14 08:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resecurityapp', '0008_partner_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='remark',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]