# Generated by Django 5.0.6 on 2024-08-27 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0010_request_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='progress',
            field=models.CharField(default='Initiated', max_length=100),
        ),
    ]
