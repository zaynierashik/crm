# Generated by Django 5.1 on 2024-09-21 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0012_rename_dob_contact_dob_request_notified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='notified',
        ),
    ]