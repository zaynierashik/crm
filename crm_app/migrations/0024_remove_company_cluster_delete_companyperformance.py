# Generated by Django 5.1 on 2024-12-25 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0023_staff_resetcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='cluster',
        ),
        migrations.DeleteModel(
            name='CompanyPerformance',
        ),
    ]
