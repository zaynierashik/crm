# Generated by Django 5.1 on 2024-12-25 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0031_company_partner_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='role',
            field=models.CharField(blank=True, choices=[('Client', 'Client'), ('Partner', 'Partner')], default='Client', max_length=100, null=True),
        ),
    ]
