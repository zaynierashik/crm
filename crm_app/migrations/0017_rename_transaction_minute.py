# Generated by Django 5.1 on 2024-09-28 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0016_company_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transaction',
            new_name='Minute',
        ),
    ]
