# Generated by Django 5.0.2 on 2024-05-23 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resecurityapp', '0026_alter_company_partner_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
    ]
