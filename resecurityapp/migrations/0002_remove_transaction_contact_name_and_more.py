# Generated by Django 5.0.6 on 2024-07-19 10:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resecurityapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='Contact_Name',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='Created_By',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='Product_Name',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='Requirement_Type',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='service',
        ),
        migrations.AddField(
            model_name='transaction',
            name='requirement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions', to='resecurityapp.requirement'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='remark',
            field=models.TextField(blank=True, null=True),
        ),
    ]