# Generated by Django 5.0.6 on 2024-08-27 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0009_remove_request_contact_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]