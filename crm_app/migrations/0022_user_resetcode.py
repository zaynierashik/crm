# Generated by Django 5.1 on 2024-11-18 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0021_companyperformance'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='resetcode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
