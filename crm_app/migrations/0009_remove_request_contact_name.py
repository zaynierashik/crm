# Generated by Django 5.0.6 on 2024-08-26 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0008_request'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='contact_name',
        ),
    ]