# Generated by Django 5.1.4 on 2025-01-08 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whbs_app', '0002_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('PhoNo', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('massages', models.TextField()),
            ],
        ),
    ]
