# Generated by Django 5.0.6 on 2024-08-12 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='requirements',
        ),
    ]
