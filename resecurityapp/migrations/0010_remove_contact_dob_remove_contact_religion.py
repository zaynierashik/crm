# Generated by Django 5.0.6 on 2024-07-29 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resecurityapp', '0009_contact_dob_contact_religion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='DOB',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='religion',
        ),
    ]
