# Generated by Django 3.0.6 on 2020-05-23 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_auto_20200523_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='confirm_password',
        ),
    ]
