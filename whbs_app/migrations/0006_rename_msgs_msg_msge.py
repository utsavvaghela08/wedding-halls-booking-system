# Generated by Django 5.1.4 on 2025-01-08 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whbs_app', '0005_rename_massages_msg_msgs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='msg',
            old_name='msgs',
            new_name='msge',
        ),
    ]
