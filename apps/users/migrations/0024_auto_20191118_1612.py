# Generated by Django 2.2.5 on 2019-11-18 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_auto_20190724_1525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='otp_level',
            new_name='mfa_level',
        ),
    ]
